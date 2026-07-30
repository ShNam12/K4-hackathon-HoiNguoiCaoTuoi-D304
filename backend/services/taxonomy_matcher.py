"""Taxonomy retrieval and classification for student questions."""

from __future__ import annotations

import concurrent.futures
import json
import os
import re
import unicodedata
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any


PROMPT_PATH = Path(__file__).resolve().parents[1] / "prompts" / "taxonomy_matcher.md"

INTENTS = {
    "clarify_concept",
    "compare",
    "need_example",
    "apply_practice",
    "logistics",
    "off_topic",
    "unknown",
}
CONFIDENCES = {"high", "medium", "low"}
STATUSES = {"auto_grouped", "needs_review", "unmatched", "error"}

LOGISTICS_TERMS = {
    "deadline",
    "han nop",
    "nop bai",
    "diem",
    "cham diem",
    "quiz",
    "bao gio nop",
    "lich hoc",
    "vang mat",
}
OFF_TOPIC_TERMS = {
    "an gi",
    "thoi tiet",
    "bong da",
    "di choi",
    "mua hang",
    "giai tri",
}
VAGUE_TERMS = {
    "phan nay",
    "cai nay",
    "cho nay",
    "khuc nay",
    "la sao",
    "em chua hieu",
    "khong hieu",
}


ClassificationResult = dict[str, Any]
LLMClient = Callable[..., Any]


def classify_question(
    question: Mapping[str, Any],
    session_id: str,
    taxonomy: Mapping[str, Any] | Sequence[Mapping[str, Any]],
    llm_client: LLMClient | None = None,
    timeout_seconds: float = 8.0,
) -> ClassificationResult:
    """Classify one question into a taxonomy chapter or abstain safely."""

    question_id = str(question.get("question_id") or "")
    text = str(question.get("text") or "").strip()

    if not text:
        return _review_result(
            question_id=question_id,
            intent="unknown",
            rationale="Question text is empty or missing.",
        )

    normalized_text = normalize_text(text)
    if _is_logistics(normalized_text):
        return _unmatched_result(
            question_id=question_id,
            intent="logistics",
            rationale="Question is about class logistics, not course content.",
        )
    if _is_obvious_off_topic(normalized_text):
        return _unmatched_result(
            question_id=question_id,
            intent="off_topic",
            rationale="Question appears unrelated to the selected session taxonomy.",
        )

    chapters = _chapters_from_taxonomy(taxonomy, session_id)
    candidates = retrieve_candidates(text, taxonomy, top_k=5)

    if not candidates:
        return _unmatched_result(
            question_id=question_id,
            intent="off_topic",
            rationale="No taxonomy candidate matched the question.",
        )

    top_candidate = candidates[0]
    intent = _infer_intent(normalized_text)

    if top_candidate["match_type"] == "exact_alias":
        return _auto_result(question_id, top_candidate, intent, "high")

    if _is_vague(normalized_text):
        return _review_result(
            question_id=question_id,
            intent="unknown",
            rationale="Question is too vague to assign confidently.",
        )

    if _should_use_llm(candidates) and llm_client is not None:
        return _classify_with_llm(
            question_id=question_id,
            text=text,
            intent=intent,
            candidates=candidates,
            llm_client=llm_client,
            timeout_seconds=timeout_seconds,
        )

    confidence = _confidence_from_score(top_candidate["score"])
    if confidence == "low":
        return _review_result(
            question_id=question_id,
            intent=intent,
            topic_candidate=top_candidate,
            rationale="Only weak taxonomy evidence was found.",
        )

    return _auto_result(question_id, top_candidate, intent, confidence)


def classify_batch(
    questions: Sequence[Mapping[str, Any]],
    session_id: str,
    taxonomy: Mapping[str, Any] | Sequence[Mapping[str, Any]],
    llm_client: LLMClient | None = None,
    timeout_seconds: float = 8.0,
) -> list[ClassificationResult]:
    """Classify a batch while isolating per-question failures."""

    results: list[ClassificationResult] = []
    for question in questions:
        try:
            results.append(
                classify_question(
                    question,
                    session_id,
                    taxonomy,
                    llm_client=llm_client,
                    timeout_seconds=timeout_seconds,
                )
            )
        except Exception as exc:  # pragma: no cover - defensive batch isolation
            results.append(
                _review_result(
                    question_id=str(question.get("question_id") or ""),
                    intent="unknown",
                    rationale=f"Classifier error isolated to this question: {exc}",
                )
            )
    return results


def retrieve_candidates(
    question_text: str,
    taxonomy: Mapping[str, Any] | Sequence[Mapping[str, Any]],
    top_k: int = 5,
) -> list[dict[str, Any]]:
    """Return top-k taxonomy chapter candidates by normalized term matching."""

    chapters = _chapters_from_taxonomy(taxonomy)
    normalized_question = normalize_text(question_text)
    ranked: list[dict[str, Any]] = []

    for chapter in chapters:
        candidate = _score_chapter(normalized_question, chapter)
        if candidate["score"] > 0:
            ranked.append(candidate)

    ranked.sort(
        key=lambda item: (
            item["score"],
            len(" ".join(item["matched_terms"])),
            item["chapter"].get("is_canonical") is True,
        ),
        reverse=True,
    )
    return ranked[:top_k]


def normalize_text(value: str) -> str:
    """Lowercase, fold Vietnamese accents, strip punctuation, collapse spaces."""

    value = value.replace("đ", "d").replace("Đ", "D")
    decomposed = unicodedata.normalize("NFKD", value)
    without_marks = "".join(
        char for char in decomposed if not unicodedata.combining(char)
    )
    lowered = without_marks.lower()
    without_punctuation = re.sub(r"[^a-z0-9]+", " ", lowered)
    return re.sub(r"\s+", " ", without_punctuation).strip()


def make_openai_llm_client(model: str | None = None) -> LLMClient:
    """Create an OpenAI chat client lazily so imports stay side-effect free."""

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    try:
        from openai import OpenAI
    except ImportError as exc:  # pragma: no cover - optional runtime dependency
        raise RuntimeError("The 'openai' package is required for real LLM calls.") from exc

    selected_model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    client = OpenAI(api_key=api_key)

    def _client(payload: Mapping[str, Any]) -> str:
        response = client.chat.completions.create(
            model=selected_model,
            temperature=0.1,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": payload["prompt"]},
                {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
            ],
        )
        return response.choices[0].message.content or "{}"

    return _client


def _chapters_from_taxonomy(
    taxonomy: Mapping[str, Any] | Sequence[Mapping[str, Any]],
    session_id: str | None = None,
) -> list[Mapping[str, Any]]:
    if isinstance(taxonomy, Mapping):
        if "chapters" in taxonomy:
            if session_id and taxonomy.get("day_id") not in {None, session_id}:
                raise ValueError(f"Taxonomy does not belong to session {session_id!r}.")
            chapters = taxonomy.get("chapters")
        elif "days" in taxonomy:
            days = taxonomy.get("days") or []
            selected = None
            for day in days:
                if session_id is None or day.get("day_id") == session_id:
                    selected = day
                    break
            if selected is None:
                raise ValueError(f"Session not found in taxonomy: {session_id}")
            chapters = selected.get("chapters")
        else:
            chapters = []
    else:
        chapters = taxonomy

    if not isinstance(chapters, Sequence):
        raise ValueError("Taxonomy chapters must be a sequence.")

    return [
        chapter
        for chapter in chapters
        if isinstance(chapter, Mapping) and chapter.get("is_canonical") is True
    ]


def _score_chapter(
    normalized_question: str,
    chapter: Mapping[str, Any],
) -> dict[str, Any]:
    title = str(chapter.get("chapter_title") or "")
    aliases = [str(term) for term in chapter.get("aliases") or []]
    keywords = [str(term) for term in chapter.get("keywords") or []]
    matched_terms: list[str] = []
    score = 0.0
    match_type = "keyword"

    for term in [title, *aliases]:
        if _contains_term(normalized_question, normalize_text(term)):
            matched_terms.append(term)
            score += 8.0 + min(len(normalize_text(term)) / 20.0, 3.0)
            match_type = "exact_alias"

    for term in keywords:
        normalized_term = normalize_text(term)
        if _contains_term(normalized_question, normalized_term):
            matched_terms.append(term)
            score += 3.0 + min(len(normalized_term) / 25.0, 2.0)

    if not matched_terms:
        question_tokens = set(normalized_question.split())
        title_tokens = set(normalize_text(title).split())
        keyword_tokens = set(
            token
            for keyword in keywords
            for token in normalize_text(keyword).split()
            if len(token) >= 4
        )
        overlap = question_tokens & (title_tokens | keyword_tokens)
        if overlap:
            matched_terms.extend(sorted(overlap))
            score += len(overlap) * 1.2
            match_type = "token_overlap"

    return {
        "chapter": chapter,
        "topic_id": chapter.get("chapter_id"),
        "topic_title": chapter.get("chapter_title"),
        "score": score,
        "matched_terms": _dedupe_preserve_order(matched_terms),
        "match_type": match_type,
        "evidence_refs": list(chapter.get("source_refs") or []),
    }


def _contains_term(normalized_question: str, normalized_term: str) -> bool:
    if not normalized_term:
        return False
    return f" {normalized_term} " in f" {normalized_question} "


def _should_use_llm(candidates: Sequence[Mapping[str, Any]]) -> bool:
    if not candidates:
        return False
    if len(candidates) == 1:
        return candidates[0]["score"] < 7
    return candidates[0]["score"] - candidates[1]["score"] <= 4


def _classify_with_llm(
    question_id: str,
    text: str,
    intent: str,
    candidates: list[dict[str, Any]],
    llm_client: LLMClient,
    timeout_seconds: float,
) -> ClassificationResult:
    payload = {
        "prompt": _load_prompt(),
        "question": {"question_id": question_id, "text": text},
        "candidates": [_candidate_for_prompt(candidate) for candidate in candidates],
        "allowed_intents": sorted(INTENTS),
        "allowed_confidences": sorted(CONFIDENCES),
        "allowed_statuses": sorted(STATUSES),
    }

    try:
        raw_response = _call_llm_with_timeout(llm_client, payload, timeout_seconds)
        parsed = _parse_llm_json(raw_response)
        return _validate_llm_result(question_id, parsed, candidates, fallback_intent=intent)
    except Exception as exc:
        return _review_result(
            question_id=question_id,
            intent=intent,
            topic_candidate=candidates[0],
            rationale=f"LLM rerank failed or returned invalid JSON: {exc}",
        )


def _call_llm_with_timeout(
    llm_client: LLMClient,
    payload: Mapping[str, Any],
    timeout_seconds: float,
) -> Any:
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(_invoke_llm_client, llm_client, payload)
    try:
        return future.result(timeout=timeout_seconds)
    finally:
        executor.shutdown(wait=False, cancel_futures=True)


def _invoke_llm_client(llm_client: LLMClient, payload: Mapping[str, Any]) -> Any:
    try:
        return llm_client(payload)
    except TypeError:
        return llm_client(
            question=payload["question"],
            candidates=payload["candidates"],
            prompt=payload["prompt"],
        )


def _parse_llm_json(raw_response: Any) -> dict[str, Any]:
    if isinstance(raw_response, Mapping):
        return dict(raw_response)
    if isinstance(raw_response, str):
        parsed = json.loads(raw_response)
        if isinstance(parsed, dict):
            return parsed
    raise ValueError("LLM response must be a JSON object.")


def _validate_llm_result(
    question_id: str,
    parsed: Mapping[str, Any],
    candidates: list[dict[str, Any]],
    fallback_intent: str,
) -> ClassificationResult:
    candidate_by_id = {candidate["topic_id"]: candidate for candidate in candidates}
    status = str(parsed.get("status") or "needs_review")
    confidence = str(parsed.get("confidence") or "low")
    intent = str(parsed.get("intent") or fallback_intent)
    topic_id = parsed.get("topic_id")

    if status not in STATUSES:
        raise ValueError(f"Unknown status: {status}")
    if confidence not in CONFIDENCES:
        raise ValueError(f"Unknown confidence: {confidence}")
    if intent not in INTENTS:
        intent = fallback_intent

    if status == "unmatched":
        return _unmatched_result(
            question_id=question_id,
            intent=intent,
            rationale=str(parsed.get("rationale") or "LLM abstained as unmatched."),
        )

    if topic_id not in candidate_by_id:
        raise ValueError(f"LLM selected topic outside retrieved candidates: {topic_id}")

    candidate = candidate_by_id[topic_id]
    if status != "auto_grouped" or confidence == "low":
        return _review_result(
            question_id=question_id,
            intent=intent,
            topic_candidate=candidate,
            rationale=str(parsed.get("rationale") or "LLM requested human review."),
        )

    return _auto_result(
        question_id=question_id,
        candidate=candidate,
        intent=intent,
        confidence=confidence,
        rationale=str(parsed.get("rationale") or "LLM selected a candidate topic."),
    )


def _candidate_for_prompt(candidate: Mapping[str, Any]) -> dict[str, Any]:
    chapter = candidate["chapter"]
    return {
        "topic_id": candidate["topic_id"],
        "topic_title": candidate["topic_title"],
        "matched_terms": candidate["matched_terms"],
        "summary": chapter.get("summary"),
        "evidence_refs": candidate["evidence_refs"],
    }


def _auto_result(
    question_id: str,
    candidate: Mapping[str, Any],
    intent: str,
    confidence: str,
    rationale: str | None = None,
) -> ClassificationResult:
    return {
        "question_id": question_id,
        "topic_id": candidate["topic_id"],
        "topic_title": candidate["topic_title"],
        "intent": intent,
        "confidence": confidence,
        "status": "auto_grouped",
        "matched_terms": list(candidate["matched_terms"]),
        "evidence_refs": list(candidate["evidence_refs"]),
        "alternatives": _alternatives(candidate),
        "rationale": rationale
        or f"Matched taxonomy terms: {', '.join(candidate['matched_terms'])}.",
    }


def _review_result(
    question_id: str,
    intent: str,
    rationale: str,
    topic_candidate: Mapping[str, Any] | None = None,
) -> ClassificationResult:
    return {
        "question_id": question_id,
        "topic_id": topic_candidate["topic_id"] if topic_candidate else None,
        "topic_title": topic_candidate["topic_title"] if topic_candidate else None,
        "intent": intent if intent in INTENTS else "unknown",
        "confidence": "low",
        "status": "needs_review",
        "matched_terms": list(topic_candidate["matched_terms"]) if topic_candidate else [],
        "evidence_refs": list(topic_candidate["evidence_refs"]) if topic_candidate else [],
        "alternatives": _alternatives(topic_candidate) if topic_candidate else [],
        "rationale": rationale,
    }


def _unmatched_result(question_id: str, intent: str, rationale: str) -> ClassificationResult:
    return {
        "question_id": question_id,
        "topic_id": None,
        "topic_title": None,
        "intent": intent if intent in INTENTS else "unknown",
        "confidence": "low",
        "status": "unmatched",
        "matched_terms": [],
        "evidence_refs": [],
        "alternatives": [],
        "rationale": rationale,
    }


def _alternatives(candidate: Mapping[str, Any] | None) -> list[dict[str, Any]]:
    if not candidate:
        return []
    alternatives = []
    for alternative in candidate.get("alternatives", []):
        alternatives.append(
            {
                "topic_id": alternative.get("topic_id"),
                "topic_title": alternative.get("topic_title"),
            }
        )
    return alternatives


def _confidence_from_score(score: float) -> str:
    if score >= 6:
        return "high"
    if score >= 3:
        return "medium"
    return "low"


def _infer_intent(normalized_text: str) -> str:
    if any(term in normalized_text for term in ["khac", "so sanh", " vs ", "hay hon"]):
        return "compare"
    if any(term in normalized_text for term in ["vi du", "example", "minh hoa"]):
        return "need_example"
    if any(term in normalized_text for term in ["lam sao", "ap dung", "thuc hanh", "trien khai"]):
        return "apply_practice"
    return "clarify_concept"


def _is_logistics(normalized_text: str) -> bool:
    return any(term in normalized_text for term in LOGISTICS_TERMS)


def _is_obvious_off_topic(normalized_text: str) -> bool:
    return any(term in normalized_text for term in OFF_TOPIC_TERMS)


def _is_vague(normalized_text: str) -> bool:
    token_count = len(normalized_text.split())
    if token_count <= 3:
        return True
    return any(term in normalized_text for term in VAGUE_TERMS) and token_count <= 8


def _dedupe_preserve_order(values: Sequence[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        key = normalize_text(value)
        if key and key not in seen:
            seen.add(key)
            output.append(value)
    return output


def _load_prompt() -> str:
    try:
        return PROMPT_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "Select a taxonomy candidate or abstain. Return strict JSON only."


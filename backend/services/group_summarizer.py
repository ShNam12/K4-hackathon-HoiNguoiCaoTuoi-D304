from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Callable


class LLMError(RuntimeError):
    pass


def _load_prompt(path: str | None = None) -> str:
    if path is None:
        path = Path(__file__).resolve().parent.parent / "prompts" / "group_summary.md"
    return Path(path).read_text(encoding="utf-8")


def _default_llm_client() -> callable:
    try:
        from openai import OpenAI
    except ImportError:
        raise LLMError("Missing 'openai' package — run: pip install openai")

    api_key = os.environ.get("LLM_API_KEY") or os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise LLMError("Missing API key — set LLM_API_KEY, OPENROUTER_API_KEY or OPENAI_API_KEY in .env")

    base_url = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    model = os.environ.get("SUMMARY_MODEL") or os.environ.get("LLM_MODEL") or "openai/gpt-4o-mini"
    client = OpenAI(api_key=api_key, base_url=base_url)

    def call_llm(system: str, user: str) -> dict:
        try:
            resp = client.chat.completions.create(
                model=model,
                temperature=0.0,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
        except Exception as exc:
            raise LLMError(f"LLM call failed: {exc}") from exc

        content = resp.choices[0].message.content
        try:
            return json.loads(content)
        except (json.JSONDecodeError, TypeError) as exc:
            raise LLMError(f"LLM returned invalid JSON: {content!r:.300}") from exc

    return call_llm


def summarize_group(
    group: dict,
    *,
    llm_client: callable | None = None,
    prompt_path: str | None = None,
) -> dict:
    if group["question_count"] == 0:
        group["summary"] = ""
        group["supported_question_ids"] = []
        return group

    system_prompt = _load_prompt(prompt_path)
    topic_title = group.get("topic_title", "")
    questions = group.get("questions", [])
    question_lines = "\n".join(
        f"- [{q['question_id']}] {q['text']}" for q in questions
    )
    user_prompt = (
        f"Topic: {topic_title}\n"
        f"Questions ({len(questions)}):\n{question_lines}\n\n"
        "Return JSON: {\"summary\": \"...\", \"supported_question_ids\": [...]}"
    )

    if llm_client is None:
        try:
            llm_client = _default_llm_client()
        except LLMError:
            return _fallback_summary(group)

    try:
        result = llm_client(system_prompt, user_prompt)
    except LLMError:
        return _fallback_summary(group)

    summary = result.get("summary", "")
    supported_ids = result.get("supported_question_ids", [])

    group_ids = {q["question_id"] for q in questions}
    valid_ids = [qid for qid in supported_ids if qid in group_ids]

    if not summary.strip():
        return _fallback_summary(group)

    group["summary"] = summary
    group["supported_question_ids"] = valid_ids if valid_ids else [q["question_id"] for q in questions]
    return group


def summarize_groups(
    groups: list[dict],
    *,
    llm_client: callable | None = None,
    prompt_path: str | None = None,
) -> list[dict]:
    results = []
    for group in groups:
        try:
            result = summarize_group(
                dict(group),
                llm_client=llm_client,
                prompt_path=prompt_path,
            )
        except Exception:
            result = _fallback_summary(dict(group))
        results.append(result)
    return results


def _fallback_summary(group: dict) -> dict:
    count = group.get("question_count", 0)
    title = group.get("topic_title", "")
    intent = group.get("dominant_intent", "")
    question_ids = [q["question_id"] for q in group.get("questions", [])]
    group["summary"] = f"{count} c{'âu' if count == 1 else 'âu'} hỏi về \"{title}\", chủ yếu {_intent_label(intent)}."
    group["supported_question_ids"] = question_ids
    return group


def _intent_label(intent: str) -> str:
    labels = {
        "clarify_concept": "làm rõ khái niệm",
        "compare": "so sánh",
        "need_example": "cần ví dụ",
        "apply_practice": "áp dụng thực tế",
        "logistics": "thủ tục/hành chính",
        "off_topic": "ngoài phạm vi",
        "unknown": "không xác định",
    }
    return labels.get(intent, intent)

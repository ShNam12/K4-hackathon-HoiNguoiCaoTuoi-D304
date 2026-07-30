import json

from backend.services.taxonomy_matcher import (
    classify_batch,
    classify_question,
    normalize_text,
    retrieve_candidates,
)


def _taxonomy():
    return {
        "day_id": "DAY_01",
        "chapters": [
            {
                "chapter_id": "DAY_01_CH_RAG",
                "chapter_title": "RAG — tra sổ thay vì bắt nhớ",
                "is_canonical": True,
                "summary": "Use retrieval to ground model answers in source material.",
                "aliases": ["RAG", "retrieval augmented generation", "tra so"],
                "keywords": ["rag", "retrieval", "trich dan nguon", "context", "tai lieu"],
                "source_refs": [{"file_id": "D1", "line": 225}],
            },
            {
                "chapter_id": "DAY_01_CH_TOKEN",
                "chapter_title": "Token là mảnh chữ",
                "is_canonical": True,
                "summary": "Tokens are chunks of text and each token has cost.",
                "aliases": ["token la gi", "tokenizer"],
                "keywords": ["token", "manh chu", "chi phi token", "tieng viet ton token"],
                "source_refs": [{"file_id": "D1", "line": 195}],
            },
            {
                "chapter_id": "DAY_01_CH_AGENT",
                "chapter_title": "Từ LLM đến agent: bốn mức độ",
                "is_canonical": True,
                "summary": "Agents combine reasoning, tools, actions, and memory.",
                "aliases": ["bon muc do agent", "tu llm den agent"],
                "keywords": ["agent", "tools", "memory", "action", "multi agent"],
                "source_refs": [{"file_id": "D1", "line": 294}],
            },
            {
                "chapter_id": "DAY_01_CH_EXTRA",
                "chapter_title": "Supplementary item",
                "is_canonical": False,
                "aliases": ["should not match"],
                "keywords": ["hidden"],
                "source_refs": [{"file_id": "D1", "line": 999}],
            },
        ],
    }


def test_normalize_text_folds_vietnamese_diacritics():
    assert normalize_text("Từ LLM đến Agent: bốn mức độ!") == "tu llm den agent bon muc do"


def test_exact_alias_match_wins_before_llm():
    result = classify_question(
        {"question_id": "Q001", "text": "Token là gì?"},
        "DAY_01",
        _taxonomy(),
        llm_client=lambda payload: {"status": "unmatched"},
    )

    assert result["status"] == "auto_grouped"
    assert result["topic_id"] == "DAY_01_CH_TOKEN"
    assert result["confidence"] == "high"


def test_paraphrase_is_retrieved_in_top_k():
    candidates = retrieve_candidates("Lam sao truy xuat tai lieu de co context?", _taxonomy())

    assert candidates[0]["topic_id"] == "DAY_01_CH_RAG"


def test_vague_question_becomes_needs_review():
    result = classify_question({"question_id": "Q002", "text": "Phần này là sao?"}, "DAY_01", _taxonomy())

    assert result["status"] == "needs_review"
    assert result["confidence"] == "low"


def test_logistics_question_becomes_unmatched():
    result = classify_question(
        {"question_id": "Q003", "text": "Deadline nộp bài là khi nào?"},
        "DAY_01",
        _taxonomy(),
    )

    assert result["status"] == "unmatched"
    assert result["intent"] == "logistics"


def test_bad_llm_json_does_not_crash():
    result = classify_question(
        {"question_id": "Q004", "text": "Agent dùng tools và memory khác gì RAG?"},
        "DAY_01",
        _taxonomy(),
        llm_client=lambda payload: "not-json",
    )

    assert result["status"] == "needs_review"
    assert result["confidence"] == "low"


def test_llm_topic_outside_candidates_is_rejected_to_review():
    result = classify_question(
        {"question_id": "Q005", "text": "Agent dùng tools và memory khác gì RAG?"},
        "DAY_01",
        _taxonomy(),
        llm_client=lambda payload: json.dumps(
            {
                "topic_id": "DAY_01_CH_DOES_NOT_EXIST",
                "intent": "compare",
                "confidence": "high",
                "status": "auto_grouped",
            }
        ),
    )

    assert result["status"] == "needs_review"


def test_source_reference_comes_from_taxonomy_candidate():
    result = classify_question(
        {"question_id": "Q006", "text": "Retrieval augmented generation dùng tài liệu thế nào?"},
        "DAY_01",
        _taxonomy(),
        llm_client=lambda payload: json.dumps(
            {
                "topic_id": "DAY_01_CH_RAG",
                "intent": "clarify_concept",
                "confidence": "high",
                "status": "auto_grouped",
                "evidence_refs": [{"file_id": "FAKE", "line": 1}],
            }
        ),
    )

    assert result["evidence_refs"] == [{"file_id": "D1", "line": 225}]


def test_batch_isolates_one_case_without_losing_others():
    results = classify_batch(
        [
            {"question_id": "Q007", "text": "Token là gì?"},
            {"question_id": "Q008", "text": ""},
            {"question_id": "Q009", "text": "Agent có tools và memory hoạt động ra sao?"},
        ],
        "DAY_01",
        _taxonomy(),
    )

    assert [result["question_id"] for result in results] == ["Q007", "Q008", "Q009"]
    assert results[0]["status"] == "auto_grouped"
    assert results[1]["status"] == "needs_review"
    assert results[2]["status"] in {"auto_grouped", "needs_review"}


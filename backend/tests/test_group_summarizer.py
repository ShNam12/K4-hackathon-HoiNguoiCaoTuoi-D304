import json
import pytest

from backend.services.group_summarizer import (
    summarize_group,
    summarize_groups,
    LLMError,
)


SAMPLE_GROUP = {
    "topic_id": "DAY_01_CH_14",
    "topic_title": "RAG",
    "question_count": 2,
    "unique_student_count": 2,
    "dominant_intent": "clarify_concept",
    "confidence_breakdown": {"high": 1, "medium": 1, "low": 0},
    "questions": [
        {
            "question_id": "Q001",
            "student_id": "U001",
            "text": "Khi nào dùng RAG thay vì fine-tuning?",
            "intent": "compare",
            "confidence": "high",
            "evidence_refs": [],
        },
        {
            "question_id": "Q002",
            "student_id": "U002",
            "text": "RAG cần indexing không?",
            "intent": "clarify_concept",
            "confidence": "medium",
            "evidence_refs": [],
        },
    ],
}

EMPTY_GROUP = {
    "topic_id": "DAY_01_CH_14",
    "topic_title": "RAG",
    "question_count": 0,
    "unique_student_count": 0,
    "questions": [],
}


def mock_llm_valid(system: str, user: str) -> dict:
    return {
        "summary": "Sinh viên thắc mắc về điều kiện dùng RAG so với fine-tuning.",
        "supported_question_ids": ["Q001", "Q002"],
    }


def mock_llm_bad_ids(system: str, user: str) -> dict:
    return {
        "summary": "Bad IDs test.",
        "supported_question_ids": ["Q999", "Q001"],
    }


def mock_llm_timeout(system: str, user: str) -> dict:
    raise LLMError("LLM timeout after 30s")


def mock_llm_bad_json(system: str, user: str) -> dict:
    raise LLMError("Invalid JSON from LLM")


class TestSummarizeGroup:
    def test_summary_has_supported_ids(self):
        result = summarize_group(dict(SAMPLE_GROUP), llm_client=mock_llm_valid)
        assert "summary" in result
        assert len(result["supported_question_ids"]) > 0

    def test_supported_ids_in_group(self):
        result = summarize_group(dict(SAMPLE_GROUP), llm_client=mock_llm_valid)
        group_ids = {q["question_id"] for q in SAMPLE_GROUP["questions"]}
        for qid in result["supported_question_ids"]:
            assert qid in group_ids

    def test_bad_ids_are_filtered(self):
        result = summarize_group(dict(SAMPLE_GROUP), llm_client=mock_llm_bad_ids)
        assert "Q999" not in result["supported_question_ids"]
        assert "Q001" in result["supported_question_ids"]

    def test_llm_timeout_fallback(self):
        result = summarize_group(dict(SAMPLE_GROUP), llm_client=mock_llm_timeout)
        assert "summary" in result
        assert len(result["supported_question_ids"]) == 2
        assert result["summary"] != ""

    def test_llm_bad_json_fallback(self):
        result = summarize_group(dict(SAMPLE_GROUP), llm_client=mock_llm_bad_json)
        assert "summary" in result

    def test_empty_group_no_llm(self):
        result = summarize_group(dict(EMPTY_GROUP), llm_client=mock_llm_valid)
        assert result["summary"] == ""
        assert result["supported_question_ids"] == []

    def test_summary_is_serializable(self):
        result = summarize_group(dict(SAMPLE_GROUP), llm_client=mock_llm_valid)
        json.dumps(result)


class TestSummarizeGroups:
    def test_multiple_groups(self):
        groups = [
            {"topic_id": "T1", "topic_title": "Ch1", "question_count": 1, "questions": [{"question_id": "Q1", "text": "What?", "intent": "clarify_concept", "confidence": "high", "evidence_refs": []}], "unique_student_count": 1, "dominant_intent": "clarify_concept", "confidence_breakdown": {"high": 1, "medium": 0, "low": 0}, "summary": "", "supported_question_ids": []},
            {"topic_id": "T2", "topic_title": "Ch2", "question_count": 1, "questions": [{"question_id": "Q2", "text": "How?", "intent": "clarify_concept", "confidence": "high", "evidence_refs": []}], "unique_student_count": 1, "dominant_intent": "clarify_concept", "confidence_breakdown": {"high": 1, "medium": 0, "low": 0}, "summary": "", "supported_question_ids": []},
        ]
        results = summarize_groups(groups, llm_client=mock_llm_valid)
        assert len(results) == 2

    def test_one_group_fails_others_ok(self):
        def flaky(system, user):
            if "Q1" in user:
                raise LLMError("fail")
            return mock_llm_valid(system, user)

        groups = [
            {"topic_id": "T1", "topic_title": "Ch1", "question_count": 1, "questions": [{"question_id": "Q1", "text": "Fail?", "intent": "clarify_concept", "confidence": "high", "evidence_refs": []}], "unique_student_count": 1, "dominant_intent": "clarify_concept", "confidence_breakdown": {"high": 1, "medium": 0, "low": 0}, "summary": "", "supported_question_ids": []},
            {"topic_id": "T2", "topic_title": "Ch2", "question_count": 1, "questions": [{"question_id": "Q2", "text": "OK?", "intent": "clarify_concept", "confidence": "high", "evidence_refs": []}], "unique_student_count": 1, "dominant_intent": "clarify_concept", "confidence_breakdown": {"high": 1, "medium": 0, "low": 0}, "summary": "", "supported_question_ids": []},
        ]
        results = summarize_groups(groups, llm_client=flaky)
        assert len(results) == 2
        assert results[0]["summary"] != ""
        assert results[1]["summary"] != ""


if __name__ == "__main__":
    pytest.main([__file__])

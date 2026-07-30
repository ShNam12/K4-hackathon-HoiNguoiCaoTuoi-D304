import json
import pytest

from backend.services.question_grouper import group_classifications
from backend.services.group_summarizer import (
    summarize_group,
    summarize_groups,
    LLMError,
    _fallback_summary,
    _intent_label,
)

SAMPLE_QUESTIONS = [
    {"question_id": "Q001", "student_id": "U001", "text": "RAG khac fine-tuning nhu the nao?"},
    {"question_id": "Q002", "student_id": "U002", "text": "Cho vi du cu the ve RAG duoc khong a?"},
    {"question_id": "Q003", "student_id": "U001", "text": "The nao la Transformer, no khac gi cac model truoc do?"},
    {"question_id": "Q004", "student_id": "U003", "text": "Khi nao nen dung RAG thay vi fine-tuning cho du an thuc te?"},
    {"question_id": "Q005", "student_id": "U004", "text": "Bai tap hom nay nop o dau vay thay?"},
    {"question_id": "Q006", "student_id": "U005", "text": "RAG va fine-tuning cai nao re hon khi trien khai?"},
    {"question_id": "Q007", "student_id": "U006", "text": "Phan nay la sao a, em chua hieu lam?"},
]

SAMPLE_CLASSIFICATIONS = [
    {"question_id": "Q001", "topic_id": "DAY_01_CH_14", "topic_title": "RAG", "intent": "compare", "confidence": "high", "status": "auto_grouped", "matched_terms": ["RAG", "fine-tuning"], "evidence_refs": [{"file_id": "D1", "line": 120}], "alternatives": [], "rationale": "So sanh RAG vs fine-tuning"},
    {"question_id": "Q002", "topic_id": "DAY_01_CH_14", "topic_title": "RAG", "intent": "need_example", "confidence": "medium", "status": "auto_grouped", "matched_terms": ["RAG"], "evidence_refs": [], "alternatives": [], "rationale": "Hoi vi du RAG"},
    {"question_id": "Q003", "topic_id": "DAY_01_CH_07", "topic_title": "Transformer", "intent": "clarify_concept", "confidence": "high", "status": "auto_grouped", "matched_terms": ["Transformer"], "evidence_refs": [], "alternatives": [], "rationale": "Hoi ve Transformer"},
    {"question_id": "Q004", "topic_id": "DAY_01_CH_14", "topic_title": "RAG", "intent": "apply_practice", "confidence": "high", "status": "auto_grouped", "matched_terms": ["RAG", "fine-tuning"], "evidence_refs": [{"file_id": "D1", "line": 215}], "alternatives": [], "rationale": "Hoi khi nao dung RAG"},
    {"question_id": "Q005", "topic_id": None, "topic_title": None, "intent": "logistics", "confidence": "low", "status": "unmatched", "matched_terms": [], "evidence_refs": [], "alternatives": [], "rationale": "Cau hoi logistics"},
    {"question_id": "Q006", "topic_id": "DAY_01_CH_14", "topic_title": "RAG", "intent": "compare", "confidence": "high", "status": "auto_grouped", "matched_terms": ["RAG", "fine-tuning"], "evidence_refs": [], "alternatives": [], "rationale": "So sanh chi phi"},
    {"question_id": "Q007", "topic_id": "DAY_01_CH_14", "topic_title": "RAG", "intent": "clarify_concept", "confidence": "low", "status": "needs_review", "matched_terms": [], "evidence_refs": [], "alternatives": [{"topic_id": "DAY_01_CH_07", "topic_title": "Transformer"}], "rationale": "Mo ho"},
]


class TestHardeningPipeline:

    def test_grouper_to_summarizer_full_flow(self):
        groups, review, unmatched = group_classifications(SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS)
        assert len(groups) == 2

        rag = [g for g in groups if g["topic_id"] == "DAY_01_CH_14"][0]
        assert rag["question_count"] == 4
        assert rag["unique_student_count"] == 4
        assert rag["dominant_intent"] == "compare"
        assert rag["supported_question_ids"] == ["Q001", "Q002", "Q004", "Q006"]
        assert rag["confidence_breakdown"] == {"high": 3, "medium": 1, "low": 0}

        transformer = [g for g in groups if g["topic_id"] == "DAY_01_CH_07"][0]
        assert transformer["question_count"] == 1
        assert transformer["unique_student_count"] == 1
        assert transformer["dominant_intent"] == "clarify_concept"

        assert len(review) == 1
        assert review[0]["question_id"] == "Q007"

        assert len(unmatched) == 1
        assert unmatched[0]["question_id"] == "Q005"

    def test_summarizer_with_fallback_no_llm(self):
        groups, _, _ = group_classifications(SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS)
        results = summarize_groups(groups, llm_client=None)
        assert len(results) == 2
        for g in results:
            assert g["summary"] != ""
            assert len(g["supported_question_ids"]) > 0
            for qid in g["supported_question_ids"]:
                assert qid in {q["question_id"] for q in g["questions"]}

    def test_all_llm_modes(self):
        def mock_valid(system, user):
            return {"summary": "Test summary.", "supported_question_ids": ["Q001", "Q002", "Q004", "Q006"]}

        def mock_timeout(system, user):
            raise LLMError("timeout")

        def mock_bad_json(system, user):
            raise LLMError("bad json")

        groups, _, _ = group_classifications(SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS)

        for mock_fn in [mock_valid, mock_timeout, mock_bad_json]:
            results = summarize_groups(groups, llm_client=mock_fn)
            assert len(results) == 2
            for g in results:
                assert g["summary"] != ""
                assert len(g["supported_question_ids"]) > 0

    def test_all_groups_fail_isolation(self):
        def always_fail(system, user):
            raise LLMError("always fail")

        groups, _, _ = group_classifications(SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS)
        results = summarize_groups(groups, llm_client=always_fail)
        assert len(results) == 2
        for g in results:
            assert g["summary"] != ""
            assert g["supported_question_ids"] == [q["question_id"] for q in g["questions"]]

    def test_empty_groups_list(self):
        results = summarize_groups([], llm_client=lambda s, u: {"summary": "x", "supported_question_ids": []})
        assert results == []

    def test_single_question_group(self):
        groups, _, _ = group_classifications(
            [{"question_id": "Q001", "student_id": "U001", "text": "Test?"}],
            [{"question_id": "Q001", "topic_id": "T1", "topic_title": "Test", "intent": "clarify_concept", "confidence": "high", "status": "auto_grouped", "matched_terms": [], "evidence_refs": [], "alternatives": [], "rationale": "test"}],
        )
        result = summarize_groups(groups, llm_client=lambda s, u: {"summary": "Single question.", "supported_question_ids": ["Q001"]})
        assert len(result) == 1
        assert result[0]["question_count"] == 1

    def test_no_auto_grouped_input(self):
        groups, review, unmatched = group_classifications(SAMPLE_QUESTIONS, [])
        assert groups == []
        assert review == []
        assert unmatched == []

    def test_fallback_summary_format(self):
        group = {
            "topic_id": "T1",
            "topic_title": "RAG",
            "question_count": 3,
            "unique_student_count": 2,
            "dominant_intent": "compare",
            "questions": [{"question_id": "Q1", "text": "A?"}, {"question_id": "Q2", "text": "B?"}, {"question_id": "Q3", "text": "C?"}],
        }
        result = _fallback_summary(dict(group))
        assert "RAG" in result["summary"]
        assert "so sánh" in result["summary"]
        assert result["supported_question_ids"] == ["Q1", "Q2", "Q3"]

    def test_output_json_serializable(self):
        groups, review, unmatched = group_classifications(SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS)
        results = summarize_groups(groups, llm_client=lambda s, u: {"summary": "Test.", "supported_question_ids": [g["question_id"] for g in groups[0]["questions"]]})
        output = {"groups": results, "review_queue": review, "unmatched": unmatched}
        json.dumps(output)

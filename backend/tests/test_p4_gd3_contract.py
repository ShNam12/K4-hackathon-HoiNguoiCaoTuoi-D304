"""Verify P4 grouper/summarizer output matches AnalyzeResponse schema.

Run: pytest backend/tests/test_p4_gd3_contract.py -v
"""

from backend.schemas import AnalyzeResponse, ReviewItem, QuestionGroup, Status, Confidence
from backend.services.question_grouper import group_classifications
from backend.services.group_summarizer import summarize_groups


def _make_classification(
    question_id: str,
    topic_id: str | None = "DAY_01_CH_01",
    topic_title: str | None = "Transformer",
    status: str = "auto_grouped",
    confidence: str = "high",
    intent: str = "clarify_concept",
    rationale: str = "Good match",
) -> dict:
    return {
        "question_id": question_id,
        "topic_id": topic_id,
        "topic_title": topic_title,
        "intent": intent,
        "confidence": confidence,
        "status": status,
        "matched_terms": [],
        "evidence_refs": [],
        "alternatives": [],
        "rationale": rationale,
    }


def _make_question(question_id: str, student_id: str = "U001", text: str = "Test question?") -> dict:
    return {"question_id": question_id, "student_id": student_id, "text": text}


class TestGrouperOutputContracts:
    def test_group_dict_has_all_questiongroup_keys(self):
        qs = [_make_question("Q1"), _make_question("Q2")]
        cs = [
            _make_classification("Q1", topic_id="CH_01"),
            _make_classification("Q2", topic_id="CH_01"),
        ]
        groups, _, _ = group_classifications(qs, cs)
        assert len(groups) == 1
        g = groups[0]

        expected = {"topic_id", "topic_title", "question_count", "unique_student_count",
                    "dominant_intent", "summary", "supported_question_ids",
                    "confidence_breakdown", "questions"}
        assert set(g.keys()) == expected, f"Missing keys: {expected - set(g.keys())}"

        # Validate via pydantic
        qg = QuestionGroup.model_validate(g)
        assert qg.topic_id == "CH_01"
        assert qg.question_count == 2

    def test_review_queue_items_have_student_id_and_text(self):
        """review_queue items now include student_id and text for ReviewItem."""
        qs = [_make_question("Q1", "U001", "What is AI?")]
        cs = [_make_classification("Q1", topic_id=None, status="needs_review", confidence="low")]
        _, review, _ = group_classifications(qs, cs)
        assert len(review) == 1
        item = review[0]

        assert item.get("student_id") == "U001"
        assert item.get("text") == "What is AI?"

        # Direct pydantic validation should pass
        ri = ReviewItem.model_validate(item)
        assert ri.student_id == "U001"
        assert ri.text == "What is AI?"

    def test_unmatched_items_have_student_id_and_text(self):
        """unmatched items now include student_id and text for ReviewItem."""
        qs = [_make_question("Q1", "U001", "Where to submit?")]
        cs = [_make_classification("Q1", topic_id=None, status="unmatched", confidence="low")]
        _, _, unmatched = group_classifications(qs, cs)
        assert len(unmatched) == 1
        item = unmatched[0]

        assert item.get("student_id") == "U001"
        assert item.get("text") == "Where to submit?"

        ri = ReviewItem.model_validate(item)
        assert ri.student_id == "U001"
        assert ri.text == "Where to submit?"


class TestFullPipelineContract:
    def test_happy_path_full_roundtrip(self):
        qs = [
            _make_question("Q1", "U001", "What is Transformer?"),
            _make_question("Q2", "U001", "Compare RAG and fine-tune"),
            _make_question("Q3", "U002", "Example of RAG please"),
            _make_question("Q4", "U003", "Deadline for homework?"),
        ]
        cs = [
            _make_classification("Q1", topic_id="CH_01", topic_title="Transformer", confidence="high"),
            _make_classification("Q2", topic_id="CH_02", topic_title="RAG", confidence="high", intent="compare"),
            _make_classification("Q3", topic_id="CH_02", topic_title="RAG", confidence="medium", intent="need_example"),
            _make_classification("Q4", topic_id=None, status="unmatched", intent="logistics", confidence="low"),
        ]

        groups, review, unmatched = group_classifications(qs, cs)
        groups = summarize_groups(groups, llm_client=self._mock_llm)

        # Validate groups
        for g in groups:
            qg = QuestionGroup.model_validate(g)
            assert qg.summary != ""
            assert len(qg.supported_question_ids) > 0

        # Validate review/unmatched — grouper already enriches with student_id + text
        assert len(groups) == 2
        assert len(review) == 0
        assert len(unmatched) == 1

    @staticmethod
    def _mock_llm(system: str, user: str) -> dict:
        return {
            "summary": "Mock summary for testing.",
            "supported_question_ids": ["Q1"],
        }

    def test_review_item_now_directly_validatable(self):
        """Grouper now enriches review/unmatched — P5 can pass directly to schema."""
        qs = [_make_question("Q1", "U999", "Need help")]
        cs = [_make_classification("Q1", topic_id=None, status="needs_review", confidence="low")]
        _, review, _ = group_classifications(qs, cs)

        ri = ReviewItem.model_validate(review[0])
        assert ri.student_id == "U999"
        assert ri.text == "Need help"

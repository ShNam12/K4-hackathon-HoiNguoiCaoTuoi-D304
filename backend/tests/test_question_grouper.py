import pytest

from backend.services.question_grouper import group_classifications
from backend.tests.fixtures import SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS


class TestGroupClassifications:
    def test_same_topic_grouped(self):
        groups, review, unmatched = group_classifications(
            SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS
        )
        rag_group = [g for g in groups if g["topic_id"] == "DAY_01_CH_14"]
        assert len(rag_group) == 1
        assert rag_group[0]["question_count"] == 3

    def test_different_topics_not_merged(self):
        groups, review, unmatched = group_classifications(
            SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS
        )
        topic_ids = {g["topic_id"] for g in groups}
        assert "DAY_01_CH_14" in topic_ids
        assert "DAY_01_CH_07" in topic_ids
        assert len(groups) == 2

    def test_review_unmatched_excluded_from_groups(self):
        groups, review, unmatched = group_classifications(
            SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS
        )
        for g in groups:
            for q in g["questions"]:
                assert q["question_id"] != "Q005"

    def test_question_count_correct(self):
        groups, review, unmatched = group_classifications(
            SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS
        )
        rag = [g for g in groups if g["topic_id"] == "DAY_01_CH_14"][0]
        assert rag["question_count"] == 3

    def test_unique_student_count(self):
        groups, review, unmatched = group_classifications(
            SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS
        )
        rag = [g for g in groups if g["topic_id"] == "DAY_01_CH_14"][0]
        assert rag["unique_student_count"] == 2

    def test_dominant_intent_tiebreaker(self):
        groups, review, unmatched = group_classifications(
            SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS
        )
        rag = [g for g in groups if g["topic_id"] == "DAY_01_CH_14"][0]
        assert rag["dominant_intent"] == "clarify_concept"

    def test_review_queue_contains_needs_review_and_error(self):
        groups, review, unmatched = group_classifications(
            SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS
        )
        review_ids = [c["question_id"] for c in review]
        assert "Q005" in review_ids
        assert "Q007" in review_ids

    def test_unmatched_contains_unmatched_items(self):
        groups, review, unmatched = group_classifications(
            SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS
        )
        unmatched_ids = [c["question_id"] for c in unmatched]
        assert "Q006" in unmatched_ids

    def test_empty_classifications_returns_empty(self):
        groups, review, unmatched = group_classifications(SAMPLE_QUESTIONS, [])
        assert groups == []
        assert review == []
        assert unmatched == []

    def test_confidence_breakdown(self):
        groups, review, unmatched = group_classifications(
            SAMPLE_QUESTIONS, SAMPLE_CLASSIFICATIONS
        )
        rag = [g for g in groups if g["topic_id"] == "DAY_01_CH_14"][0]
        assert rag["confidence_breakdown"] == {"high": 2, "medium": 1, "low": 0}


if __name__ == "__main__":
    pytest.main([__file__])

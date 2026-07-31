"""Run the golden set through the classify pipeline and report metrics.

Usage:
    python eval/evaluate.py --golden-set eval/golden_set.jsonl --output eval/results/run-001.json
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from backend.services.taxonomy_loader import load_session_taxonomy
from backend.services.taxonomy_matcher import classify_batch, make_openai_llm_client

load_dotenv()


def load_golden_set(path: Path) -> list[dict[str, Any]]:
    cases = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))
    return cases


def summarize(case_results: list[dict[str, Any]]) -> dict[str, Any]:
    n = len(case_results)
    return {
        "total_cases": n,
        "topic_correct_or_abstain_rate": sum(r["topic_correct_or_abstain"] for r in case_results) / n if n else 0,
        "status_correct_rate": sum(r["status_correct"] for r in case_results) / n if n else 0,
        "high_confidence_wrong_count": sum(r["high_confidence_wrong"] for r in case_results),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--golden-set", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    cases = load_golden_set(args.golden_set)

    cases_by_session = {}
    for case in cases:
        cases_by_session.setdefault(case["session_id"], []).append(case)

    case_results = []

    for session_id, session_cases in cases_by_session.items():
        taxonomy = load_session_taxonomy(session_id)
        questions = [c["question"] for c in session_cases]

        # Use the real classify_batch with LLM
        try:
            llm_client = make_openai_llm_client()
        except Exception:
            llm_client = None
        results = classify_batch(questions, session_id, taxonomy, llm_client=llm_client)
        results_by_qid = {r["question_id"]: r for r in results}

        for case in session_cases:
            q_id = case["question"]["question_id"]
            result = results_by_qid.get(q_id, {})

            expected_topics = case["expected_topic_ids"]
            expected_status = case["expected_status"]

            # Safety fallback for result fields
            topic_id = result.get("topic_id")
            status = result.get("status", "needs_review")
            confidence = result.get("confidence", "low")

            topic_correct_or_abstain = (
                topic_id in expected_topics
                if expected_topics
                else status in ("needs_review", "unmatched")
            )
            status_correct = status == expected_status
            high_confidence_wrong = confidence == "high" and not topic_correct_or_abstain

            case_results.append({
                "case_id": case["case_id"],
                "risk_class": case["risk_class"],
                "expected_status": expected_status,
                "actual_status": status,
                "topic_correct_or_abstain": topic_correct_or_abstain,
                "status_correct": status_correct,
                "high_confidence_wrong": high_confidence_wrong,
                "result_topic_id": topic_id,
                "result_confidence": confidence,
                "result_rationale": result.get("rationale"),
            })

    summary = summarize(case_results)

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "golden_set": str(args.golden_set),
        "classifier": "classify_batch (real)",
        "summary": summary,
        "cases": case_results,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

"""Run the golden set through the classify pipeline and report metrics.

Usage:
    python eval/evaluate.py --golden-set eval/golden_set.jsonl --output eval/results/run-001.json

Before P3's real classify_batch exists, this runs with a stub classifier
that always returns needs_review, so P5 can validate the eval harness itself
independently of P3/P4 (PLAN_10_GIO.md §8.2 — no module should block on another
for its own tests).
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def stub_classify(question: dict[str, Any], session_id: str) -> dict[str, Any]:
    return {
        "question_id": question["question_id"],
        "topic_id": None,
        "status": "needs_review",
        "confidence": "low",
    }


def load_golden_set(path: Path) -> list[dict[str, Any]]:
    cases = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))
    return cases


def evaluate_case(case: dict[str, Any], classify_fn) -> dict[str, Any]:
    result = classify_fn(case["question"], case["session_id"])
    expected_topics = case["expected_topic_ids"]
    expected_status = case["expected_status"]

    topic_correct_or_abstain = (
        result["topic_id"] in expected_topics
        if expected_topics
        else result["status"] in ("needs_review", "unmatched")
    )
    status_correct = result["status"] == expected_status
    high_confidence_wrong = result["confidence"] == "high" and not topic_correct_or_abstain

    return {
        "case_id": case["case_id"],
        "risk_class": case["risk_class"],
        "expected_status": expected_status,
        "actual_status": result["status"],
        "topic_correct_or_abstain": topic_correct_or_abstain,
        "status_correct": status_correct,
        "high_confidence_wrong": high_confidence_wrong,
    }


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
    case_results = [evaluate_case(case, stub_classify) for case in cases]
    summary = summarize(case_results)

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "golden_set": str(args.golden_set),
        "classifier": "stub_classify (needs_review always)",
        "summary": summary,
        "cases": case_results,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

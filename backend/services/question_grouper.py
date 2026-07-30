from collections import Counter


def group_classifications(
    questions: list[dict],
    classifications: list[dict],
) -> tuple[list[dict], list[dict], list[dict]]:
    questions_by_id = {q["question_id"]: q for q in questions}
    auto_grouped = []
    review_queue = []
    unmatched = []
    error_items = []

    for c in classifications:
        status = c.get("status", "unmatched")
        if status == "auto_grouped":
            auto_grouped.append(c)
        elif status == "needs_review":
            review_queue.append(_enrich_item(c, questions_by_id))
        elif status == "unmatched":
            unmatched.append(_enrich_item(c, questions_by_id))
        elif status == "error":
            error_items.append(_enrich_item(c, questions_by_id))

    topic_groups: dict[str, list[dict]] = {}
    for c in auto_grouped:
        tid = c.get("topic_id")
        if not tid:
            review_queue.append(c)
            continue
        if tid not in topic_groups:
            topic_groups[tid] = []
        topic_groups[tid].append(c)

    groups = []
    for tid, items in topic_groups.items():
        student_ids = set()
        question_items = []
        intent_counts: Counter = Counter()
        conf_breakdown: dict[str, int] = {"high": 0, "medium": 0, "low": 0}

        for c in items:
            qid = c["question_id"]
            orig = questions_by_id.get(qid, {})
            student_ids.add(orig.get("student_id", "unknown"))
            intent_counts[c.get("intent", "unknown")] += 1
            conf = c.get("confidence", "low")
            if conf in conf_breakdown:
                conf_breakdown[conf] += 1

            question_items.append({
                "question_id": qid,
                "student_id": orig.get("student_id", "unknown"),
                "text": orig.get("text", ""),
                "intent": c.get("intent", "unknown"),
                "confidence": conf,
                "evidence_refs": c.get("evidence_refs", []),
            })

        if not intent_counts:
            continue

        dominant_intent = _resolve_dominant_intent(intent_counts)

        groups.append({
            "topic_id": tid,
            "topic_title": items[0].get("topic_title", ""),
            "question_count": len(items),
            "unique_student_count": len(student_ids),
            "dominant_intent": dominant_intent,
            "summary": "",
            "supported_question_ids": [q["question_id"] for q in question_items],
            "confidence_breakdown": conf_breakdown,
            "questions": question_items,
        })

    groups.sort(key=lambda g: (-g["question_count"], g["topic_id"]))

    review_queue.extend(error_items)

    return groups, review_queue, unmatched


def _enrich_item(item: dict, questions_by_id: dict[str, dict]) -> dict:
    orig = questions_by_id.get(item["question_id"], {})
    item.setdefault("student_id", orig.get("student_id", "unknown"))
    item.setdefault("text", orig.get("text", ""))
    return item


def _resolve_dominant_intent(intent_counts: Counter) -> str:
    max_count = max(intent_counts.values())
    candidates = [intent for intent, count in intent_counts.items() if count == max_count]
    return sorted(candidates)[0]

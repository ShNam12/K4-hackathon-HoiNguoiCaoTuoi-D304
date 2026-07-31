from __future__ import annotations

from typing import Any

from daily_digest import calculate_metrics
from .._shared import err, load_topics_records

def _filter_records(records: list[dict], start_date: str, end_date: str, topic_id: str | None) -> list[dict]:
    filtered = []
    for r in records:
        ts = str(r.get("message_created_at") or "")[:10]
        if not ts:
            continue
        if start_date <= ts <= end_date:
            if topic_id:
                if r.get("chapter_id") == topic_id:
                    filtered.append(r)
            else:
                if r.get("chapter_id"):
                    filtered.append(r)
    return filtered

def compare_periods(period_a: dict[str, str], period_b: dict[str, str], metric: str, topic_id: str | None = None) -> dict[str, Any]:
    try:
        if metric not in ["count", "tutor_bo_tay_rate", "down_ratings"]:
            return {"tool": "compare_periods", "error": "invalid_metric", "message": f"Metric '{metric}' không được hỗ trợ."}
        
        records = load_topics_records()
        
        if topic_id:
            if not any(r.get("chapter_id") == topic_id for r in records):
                return {"tool": "compare_periods", "error": "unknown_topic_id", "message": f"Không tìm thấy chủ đề '{topic_id}'."}
                
        records_a = _filter_records(records, period_a["from"], period_a["to"], topic_id)
        records_b = _filter_records(records, period_b["from"], period_b["to"], topic_id)
        
        metrics_a = calculate_metrics(records_a)
        metrics_b = calculate_metrics(records_b)
        
        val_a = metrics_a.get(metric, 0)
        val_b = metrics_b.get(metric, 0)
        
        delta = val_b - val_a
        pct_change = (delta / val_a * 100) if val_a else None
        
        return {
            "tool": "compare_periods",
            "topic_id": topic_id or "ALL",
            "metric": metric,
            "period_a": {"range": period_a, "value": val_a},
            "period_b": {"range": period_b, "value": val_b},
            "delta": delta,
            "pct_change": round(pct_change, 2) if pct_change is not None else None
        }
    except Exception as exc:
        return err("compare_periods", exc)

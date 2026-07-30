from __future__ import annotations

from typing import Any

from daily_digest import aggregate

from .._shared import err, load_topics_records


def get_topic_digest(date: str = "", top_n: int = 5) -> dict[str, Any]:
    try:
        records = load_topics_records()
        top_rows, meta = aggregate(records, target_date=date or None, top_n=top_n)
        return {"tool": "get_topic_digest", "meta": meta, "topics": top_rows}
    except Exception as exc:  # tool lỗi trả về như dữ liệu, không crash agent loop
        return err("get_topic_digest", exc)

from __future__ import annotations

from collections import Counter
from typing import Any

from .._shared import err, load_topics_records


def list_available_dates() -> dict[str, Any]:
    try:
        records = load_topics_records()
        counts = Counter(str(r.get("message_created_at") or "")[:10] for r in records if r.get("message_created_at"))
        counts.pop("", None)
        dates = [{"date": d, "total_turns": n} for d, n in sorted(counts.items())]
        return {"tool": "list_available_dates", "dates": dates}
    except Exception as exc:
        return err("list_available_dates", exc)

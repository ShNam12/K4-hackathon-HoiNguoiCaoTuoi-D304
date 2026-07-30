from __future__ import annotations

from typing import Any

from daily_digest import truncate_quote
from knowledge_tree import KnowledgeTree

from .._shared import err, load_topics_records

_tree: KnowledgeTree | None = None


def _get_tree() -> KnowledgeTree:
    global _tree
    if _tree is None:
        _tree = KnowledgeTree.load()
    return _tree


def get_topic_examples(chapter_id: str = "", date: str = "", limit: int = 5) -> dict[str, Any]:
    try:
        if not chapter_id:
            return {"tool": "get_topic_examples", "error": "missing_chapter_id", "message": "Thiếu chapter_id — lấy từ kết quả get_topic_digest trước."}

        tree = _get_tree()
        ch = tree.chapter(chapter_id)
        if ch is None:
            return {
                "tool": "get_topic_examples",
                "error": "unknown_chapter_id",
                "message": f"'{chapter_id}' không khớp chương nào trong cây tri thức — không tự đoán chương khác.",
            }

        records = load_topics_records()
        matched = [r for r in records if r.get("chapter_id") == chapter_id]
        if date:
            matched = [r for r in matched if str(r.get("message_created_at") or "")[:10] == date]

        examples = [truncate_quote(r["cau_hoi_goc"]) for r in matched[:limit] if r.get("cau_hoi_goc")]
        return {
            "tool": "get_topic_examples",
            "chapter_id": chapter_id,
            "chapter_title": ch["chapter_title"],
            "count": len(matched),
            "examples": examples,
        }
    except Exception as exc:
        return err("get_topic_examples", exc)

from __future__ import annotations

from typing import Any

from clean_chatlog import bo_dau, chuan_hoa
from knowledge_tree import KnowledgeTree
from .._shared import err, load_topics_records

_tree: KnowledgeTree | None = None

def _get_tree() -> KnowledgeTree:
    global _tree
    if _tree is None:
        _tree = KnowledgeTree.load()
    return _tree

def search_by_keyword(keyword: str, time_range: dict[str, str] | None = None, limit: int = 20) -> dict[str, Any]:
    try:
        if not keyword:
            return {"tool": "search_by_keyword", "error": "missing_keyword", "message": "Thiếu từ khóa tìm kiếm."}
            
        records = load_topics_records()
        tree = _get_tree()
        
        norm_kw = bo_dau(chuan_hoa(keyword))
        
        matched = []
        for r in records:
            if time_range:
                ts = str(r.get("message_created_at") or "")[:10]
                if not ts or not (time_range.get("from", "") <= ts <= time_range.get("to", "9999-99-99")):
                    continue
            
            cau_hoi = r.get("cau_hoi_goc") or ""
            chapter_id = r.get("chapter_id")
            
            chapter_title = ""
            if chapter_id:
                ch = tree.chapter(chapter_id)
                if ch:
                    chapter_title = ch.get("chapter_title", "")
            
            text_to_search = f"{cau_hoi} {chapter_title}"
            if norm_kw in bo_dau(chuan_hoa(text_to_search)):
                matched.append({
                    "chapter_id": chapter_id,
                    "chapter_title": chapter_title,
                    "date": str(r.get("message_created_at") or "")[:10],
                    "cau_hoi_goc": cau_hoi
                })
                
                if len(matched) >= limit:
                    break
                    
        return {
            "tool": "search_by_keyword",
            "keyword": keyword,
            "count": len(matched),
            "results": matched
        }
    except Exception as exc:
        return err("search_by_keyword", exc)

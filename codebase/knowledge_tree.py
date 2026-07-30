"""
Nạp cây tri thức day/chapter (data/vlearn-pack/slides/knowledge-tree-day-chapter.json)
và so khớp một câu hỏi tự do vào đúng (day_id, chapter_id) — đây là "tầng 1" (so khớp
slide, deterministic, không tốn tiền gọi AI) được nhắc tới trong docstring của
clean_chatlog.py.

Không có kết quả chắc chắn (tier 3 trở xuống) thì KHÔNG đoán bừa — trả về
confidence thấp hoặc None để bước sau (LLM fallback trong classify_turns.py)
xử lý, đúng nguyên tắc "nguồn sự thật" của đề bài: không có căn cứ thì không bịa.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_TREE_PATH = Path(__file__).resolve().parent.parent / "data" / "vlearn-pack" / "slides" / "knowledge-tree-day-chapter.json"


def fold(text: str | None) -> str:
    """Hạ chữ thường, bỏ dấu tiếng Việt, gộp mọi ký tự không phải chữ/số thành khoảng trắng."""
    if not isinstance(text, str) or not text:
        return ""
    decomposed = unicodedata.normalize("NFD", text.lower())
    no_diacritics = "".join(c for c in decomposed if unicodedata.category(c) != "Mn")
    no_diacritics = no_diacritics.replace("đ", "d")
    return re.sub(r"[^a-z0-9]+", " ", no_diacritics).strip()


@dataclass
class MatchResult:
    day_id: str | None
    chapter_id: str | None
    chapter_title: str | None = None
    confidence: str = "none"  # high | medium | low | none
    tier: str = "none"  # tier1 | tier2 | tier3 | tier4 | none
    matched_terms: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "day_id": self.day_id,
            "chapter_id": self.chapter_id,
            "chapter_title": self.chapter_title,
            "confidence": self.confidence,
            "tier": self.tier,
            "matched_terms": self.matched_terms,
        }


class KnowledgeTree:
    def __init__(self, tree: dict):
        self.raw = tree
        self._chapters: dict[str, dict] = {}
        self._day_titles: dict[str, str] = {}
        self._day_alias_folded: dict[str, list[str]] = {}
        self._build_index(tree)

    @classmethod
    def load(cls, path: Path | str = DEFAULT_TREE_PATH) -> "KnowledgeTree":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(data)

    def _build_index(self, tree: dict) -> None:
        norm_day_aliases = tree.get("normalization", {}).get("day_aliases", {})
        for day in tree["days"]:
            self._day_titles[day["day_id"]] = day["day_title"]
            aliases = list(day.get("day_aliases", [])) + list(norm_day_aliases.get(day["day_id"], []))
            self._day_alias_folded[day["day_id"]] = [fold(a) for a in aliases] + [fold(day["day_id"])]
            for ch in day["chapters"]:
                entry = dict(ch)
                entry["day_id"] = day["day_id"]
                entry["_alias_folded"] = [fold(a) for a in ([ch["chapter_title"]] + ch.get("aliases", [])) if a]
                entry["_keyword_folded"] = [fold(k) for k in ch.get("keywords", []) if k]
                self._chapters[ch["chapter_id"]] = entry

        # topic_index: gộp thêm keyword của các chủ đề lặp lại xuyên suốt (VD Cursor/Artifact/PAIR...)
        # vào đúng chapter đích, coi như bằng chứng bổ sung khi so khớp.
        for topic in tree.get("topic_index", []):
            target = topic.get("maps_to", {})
            chapter_id = target.get("chapter_id")
            if chapter_id in self._chapters:
                folded_kw = [fold(k) for k in topic.get("keywords", []) if k]
                self._chapters[chapter_id]["_keyword_folded"].extend(folded_kw)

    def chapter(self, chapter_id: str) -> dict | None:
        return self._chapters.get(chapter_id)

    def day_title(self, day_id: str) -> str | None:
        return self._day_titles.get(day_id)

    def all_chapters_brief(self, day_id: str | None = None) -> list[dict]:
        """Danh sách gọn (chapter_id, chapter_title, day_id) — dùng để đưa vào prompt LLM tầng 2."""
        out = []
        for cid, ch in self._chapters.items():
            if day_id and ch["day_id"] != day_id:
                continue
            out.append({"chapter_id": cid, "chapter_title": ch["chapter_title"], "day_id": ch["day_id"]})
        return out

    def valid_chapter_ids(self) -> set[str]:
        return set(self._chapters.keys())

    def match(self, query: str) -> MatchResult:
        q = fold(query)
        if not q:
            return MatchResult(day_id=None, chapter_id=None, confidence="none", tier="none")

        best: MatchResult | None = None
        best_score = -1.0

        for cid, ch in self._chapters.items():
            matched_terms: list[str] = []

            # Tier 1 — alias/chapter_title (đủ dài, >=4 ký tự) xuất hiện nguyên cụm trong câu hỏi
            tier1_hit = False
            for alias in ch["_alias_folded"]:
                if len(alias) >= 4 and alias in q:
                    tier1_hit = True
                    matched_terms.append(alias)

            # Đếm keyword khớp (tier 2/3)
            keyword_hits = [kw for kw in ch["_keyword_folded"] if len(kw) >= 3 and kw in q]
            matched_terms.extend(k for k in keyword_hits if k not in matched_terms)

            if tier1_hit:
                score = 1000 + len(keyword_hits) + (1 if ch.get("is_canonical") else 0)
                tier, confidence = "tier1", "high"
            elif len(keyword_hits) >= 2:
                score = 100 + len(keyword_hits) + (1 if ch.get("is_canonical") else 0)
                tier, confidence = "tier2", "high"
            elif len(keyword_hits) == 1:
                score = 10 + len(keyword_hits[0]) / 100 + (1 if ch.get("is_canonical") else 0)
                tier, confidence = "tier3", "medium"
            else:
                continue

            if score > best_score:
                best_score = score
                best = MatchResult(
                    day_id=ch["day_id"],
                    chapter_id=cid,
                    chapter_title=ch["chapter_title"],
                    confidence=confidence,
                    tier=tier,
                    matched_terms=sorted(set(matched_terms)),
                )

        if best is not None:
            return best

        # Tier 4 — chỉ khớp alias của ngày (không xác định được chương)
        for day_id, aliases in self._day_alias_folded.items():
            for alias in aliases:
                if len(alias) >= 3 and alias in q:
                    return MatchResult(day_id=day_id, chapter_id=None, confidence="low", tier="tier4", matched_terms=[alias])

        return MatchResult(day_id=None, chapter_id=None, confidence="none", tier="none")


if __name__ == "__main__":
    tree = KnowledgeTree.load()
    for ex in tree.raw.get("examples", []):
        result = tree.match(ex["query"])
        expected = ex["expected"]
        ok = result.chapter_id == expected.get("chapter_id") and result.day_id == expected.get("day_id")
        status = "OK " if ok else "SAI"
        print(f"[{status}] {ex['query'][:60]!r} -> got={result.chapter_id}/{result.confidence} expected={expected.get('chapter_id')}/{expected.get('confidence')}")

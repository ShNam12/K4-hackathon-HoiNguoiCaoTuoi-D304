"""
Tổng hợp turns_topics.jsonl (output của classify_turns.py) thành bản tin cuối
ngày cho giảng viên: "N chủ đề học viên hôm nay chưa hiểu hết".

Lát cắt MỘT CÂU: giảng viên (1 user) · muốn biết cuối ngày lớp đang vướng chủ
đề nào (1 job) · AI gộp câu hỏi đã gán chương + xếp hạng + viết bản tin (1
quyết định AI) · nhận về top-N chủ đề kèm bằng chứng câu hỏi thật (1 kết quả).

Bảng số liệu (đếm được, kiểm lại được) luôn được in kèm bên cạnh bản tin do
AI viết — không chỉ tin vào văn xuôi AI sinh ra, để giảng viên tự đối chiếu.

Chạy:
    python daily_digest.py --input out/turns_topics.jsonl --date 2026-07-24 --top-n 5
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import pandas as pd

from knowledge_tree import KnowledgeTree
from llm_client import LLMError, chat_json

sys.stdout.reconfigure(encoding="utf-8")

DIGEST_SYSTEM_PROMPT = """Bạn viết bản tin cuối ngày ngắn gọn cho giảng viên khoá học AI, dựa THUẦN TUÝ vào bảng dữ liệu JSON được cung cấp.

Quy tắc bắt buộc:
- KHÔNG được bịa thêm số liệu, chủ đề, hoặc câu hỏi nào ngoài bảng đã cho.
- KHÔNG suy diễn nguyên nhân học viên không hiểu nếu bảng không có dữ liệu hỗ trợ.
- Với mỗi chủ đề: nêu tên chương, số câu hỏi, và trích 1 câu hỏi ví dụ NGUYÊN VĂN từ bảng (không diễn giải lại).
- Nếu tutor_bo_tay_rate của một chủ đề cao (>0.3), nhấn mạnh rằng đây còn là lỗi hệ thống (tutor không tìm được nội dung trả lời), không chỉ là học viên chưa hiểu.
- Viết tiếng Việt, giọng báo cáo ngắn gọn, không hô khẩu hiệu, không thêm lời khuyên sư phạm nếu không được yêu cầu.
- Trả về JSON: {"digest_markdown": "<toàn bộ bản tin dạng markdown>"}.
"""


MAX_QUOTE_CHARS = 160  # trích dẫn ngắn để minh hoạ, không dán nguyên văn dài (quy định bảo mật data pack)


def truncate_quote(text: str | None) -> str | None:
    if not isinstance(text, str):
        return None
    text = text.strip()
    return text if len(text) <= MAX_QUOTE_CHARS else text[:MAX_QUOTE_CHARS].rstrip() + "…"


def calculate_metrics(items: list[dict]) -> dict:
    if not items:
        return {"count": 0, "tutor_bo_tay_rate": 0.0, "down_ratings": 0}
    bo_tay_flags = [i["tutor_bo_tay"] for i in items if i.get("tutor_bo_tay") is not None]
    bo_tay_rate = sum(bo_tay_flags) / len(bo_tay_flags) if bo_tay_flags else 0.0
    down_ratings = sum(1 for i in items if i.get("rating") == "down")
    return {
        "count": len(items),
        "tutor_bo_tay_rate": round(bo_tay_rate, 2),
        "down_ratings": down_ratings,
    }


def aggregate(records: list[dict], *, target_date: str | None, top_n: int) -> tuple[list[dict], dict]:
    def turn_date(rec: dict) -> str | None:
        ts = rec.get("message_created_at")
        return str(ts)[:10] if ts else None

    available_dates = sorted({d for d in (turn_date(r) for r in records) if d})
    if target_date is None:
        target_date = available_dates[-1] if available_dates else None

    day_records = [r for r in records if turn_date(r) == target_date]

    excluded = [r for r in day_records if r.get("excluded_reason")]
    unclassified = [r for r in day_records if not r.get("excluded_reason") and not r.get("chapter_id")]
    classified = [r for r in day_records if r.get("chapter_id")]

    groups: dict[str, list[dict]] = defaultdict(list)
    for r in classified:
        groups[r["chapter_id"]].append(r)

    rows = []
    for chapter_id, items in groups.items():
        metrics = calculate_metrics(items)
        rows.append({
            "chapter_id": chapter_id,
            "day_id": items[0]["day_id"],
            "chapter_title": items[0]["chapter_title"],
            "count": metrics["count"],
            "tutor_bo_tay_rate": metrics["tutor_bo_tay_rate"],
            "down_ratings": metrics["down_ratings"],
            "example_quotes": [truncate_quote(i["cau_hoi_goc"]) for i in items[:3] if i.get("cau_hoi_goc")],
        })

    rows.sort(key=lambda r: (-r["count"], -r["tutor_bo_tay_rate"]))
    top_rows = rows[:top_n]

    meta = {
        "date": target_date,
        "available_dates": available_dates,
        "total_turns_today": len(day_records),
        "classified_today": len(classified),
        "excluded_today": len(excluded),
        "unclassified_today": len(unclassified),
        "topics_found_today": len(rows),
    }
    return top_rows, meta


def render_fallback_digest(top_rows: list[dict], meta: dict) -> str:
    """Bản tin dạng bảng thuần, dùng khi không gọi được LLM (fallback an toàn, không crash)."""
    lines = [f"# Bản tin ngày {meta['date']} ({meta['classified_today']}/{meta['total_turns_today']} câu hỏi đã gán chủ đề)\n"]
    for i, row in enumerate(top_rows, 1):
        lines.append(f"**{i}. {row['chapter_title']}** ({row['day_id']} · {row['chapter_id']}) — {row['count']} câu hỏi")
        if row["tutor_bo_tay_rate"] > 0.3:
            lines.append(f"   ⚠️ Tutor bó tay {row['tutor_bo_tay_rate']:.0%} số câu — có thể là lỗi grounding, không chỉ học viên chưa hiểu.")
        for q in row["example_quotes"][:1]:
            lines.append(f"   - Ví dụ: \"{q}\"")
    return "\n".join(lines)


def build_digest(top_rows: list[dict], meta: dict, *, model: str | None = None) -> str:
    if not top_rows:
        return f"# Bản tin ngày {meta['date']}\n\nKhông có câu hỏi nào được gán chủ đề trong ngày này ({meta['total_turns_today']} turn, {meta['unclassified_today']} không xác định)."

    payload = json.dumps({"meta": meta, "topics": top_rows}, ensure_ascii=False, indent=2)
    try:
        result = chat_json(
            DIGEST_SYSTEM_PROMPT,
            f"Dữ liệu:\n{payload}\n\nViết bản tin cho giảng viên.",
            model=model,
        )
        digest = result.get("digest_markdown")
        if isinstance(digest, str) and digest.strip():
            return digest
        raise LLMError("digest_markdown rỗng hoặc sai kiểu")
    except LLMError as exc:
        fallback = render_fallback_digest(top_rows, meta)
        return f"{fallback}\n\n_(LLM không khả dụng, hiển thị bảng thô — lỗi: {exc})_"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True, help="turns_topics.jsonl (output của classify_turns.py)")
    parser.add_argument("--date", default=None, help="YYYY-MM-DD — mặc định là ngày mới nhất có dữ liệu")
    parser.add_argument("--top-n", type=int, default=5)
    parser.add_argument("--model", default=None)
    parser.add_argument("--save", default=None, help="Đường dẫn lưu digest .md (tuỳ chọn)")
    parser.add_argument("--no-llm", action="store_true", help="Chỉ in bảng thô, không gọi LLM viết văn")
    args = parser.parse_args()

    records = [json.loads(line) for line in Path(args.input).read_text(encoding="utf-8").splitlines() if line.strip()]
    top_rows, meta = aggregate(records, target_date=args.date, top_n=args.top_n)

    digest = render_fallback_digest(top_rows, meta) if args.no_llm else build_digest(top_rows, meta, model=args.model)

    print(digest)
    print("\n---\n### Bảng số liệu gốc (đối chiếu) ###")
    print(json.dumps({"meta": meta, "topics": top_rows}, ensure_ascii=False, indent=2))

    if args.save:
        Path(args.save).write_text(digest, encoding="utf-8")
        print(f"\nĐã lưu: {args.save}")


if __name__ == "__main__":
    main()

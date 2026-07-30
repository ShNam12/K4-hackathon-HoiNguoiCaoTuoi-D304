"""
Gán chủ đề (day_id, chapter_id) cho từng turn đã làm sạch (turns_clean.jsonl
từ clean_chatlog.py) — nối tiếp đúng bước "tầng 1 / tầng 2" đã ghi trong
docstring của clean_chatlog.py:

  Tầng 1 — so khớp deterministic với cây tri thức (knowledge_tree.py), không
           tốn tiền, không gọi AI.
  Tầng 2 — turn nào tầng 1 không đủ tự tin (confidence low/none) mới gọi LLM
           thật (OpenRouter) để phân loại, GIỚI HẠN model chỉ được chọn trong
           đúng danh sách chapter_id đã biết (hoặc NONE/OUT_OF_SCOPE) — không
           cho phép bịa chương không tồn tại (chỗ khó ① nguồn sự thật).

Turn bị loại khỏi thống kê chủ đề (nhưng vẫn ghi lại, có gắn nhãn lý do):
  - la_lap_lai_doan_trich / thao tác UI thuần (không phải câu hỏi tự viết)
  - nghi_ngo_injection (không phải tín hiệu học thuật)

Chạy:
    python classify_turns.py --input out/turns_clean.jsonl --output out/turns_topics.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

from knowledge_tree import KnowledgeTree, MatchResult, fold
from llm_client import LLMError, chat_json

sys.stdout.reconfigure(encoding="utf-8")

# Câu hỏi tự gõ thật của học viên thường ngắn. Một số dòng trong turns_clean.jsonl
# vẫn còn lẫn nguyên văn đoạn slide dài (do clean_chatlog.py chưa tách hết hết mọi
# biến thể UI — xem docstring file đó). Nếu chạy keyword match trên cả khối text
# dài này, kết quả sẽ phản ánh "slide nào đang mở" thay vì "học viên hỏi/vướng gì" —
# đúng chỗ khó ④ (đặc thù domain): gán nhầm chủ đề khiến giảng viên hiểu sai lớp.
# Guard bảo thủ: coi câu hỏi quá dài là nghi vấn dán nguyên văn, loại khỏi thống kê
# thay vì tin vào một match có thể sai.
LONG_QUESTION_CHAR_LIMIT = 350

LLM_SYSTEM_PROMPT = """Bạn là bộ phân loại câu hỏi của học viên vào đúng MỘT chương trong danh sách chương bài giảng cho sẵn.

Quy tắc bắt buộc:
- CHỈ được chọn chapter_id có trong danh sách đưa cho bạn. Không được bịa chapter_id khác.
- Nếu câu hỏi không thực sự liên quan nội dung bài giảng nào trong danh sách (hỏi logistics, deadline, chào hỏi, ngoài phạm vi khoá học), trả "chapter_id": "NONE".
- Nếu không đủ căn cứ để chọn tự tin giữa nhiều chương, trả "chapter_id": "NONE" thay vì đoán bừa.
- Trả về đúng JSON: {"chapter_id": "<id hoặc NONE>", "reason": "<1 câu ngắn giải thích>"}.
"""


def build_llm_user_prompt(question: str, snippet: str | None, chapters: list[dict]) -> str:
    chapter_lines = "\n".join(f"- {c['chapter_id']} ({c['day_id']}): {c['chapter_title']}" for c in chapters)
    snippet_part = f'\nĐoạn tài liệu học viên đã bôi đen (nếu có): "{snippet}"' if snippet else ""
    return (
        f"Danh sách chương:\n{chapter_lines}\n\n"
        f'Câu hỏi học viên: "{question}"{snippet_part}\n\n'
        "Chọn đúng 1 chapter_id phù hợp nhất, hoặc NONE."
    )


def classify_turn(row: pd.Series, tree: KnowledgeTree, *, use_llm: bool, model: str | None) -> dict:
    excluded_reason = None
    if bool(row.get("la_lap_lai_doan_trich")):
        excluded_reason = "UI_OR_REPEATED_SNIPPET"
    elif bool(row.get("nghi_ngo_injection")):
        excluded_reason = "PROMPT_INJECTION_SUSPECT"
    elif len(str(row.get("cau_hoi_goc") or "")) > LONG_QUESTION_CHAR_LIMIT:
        excluded_reason = "SUSPECTED_PASTED_CONTENT"

    question = row.get("cau_hoi_khong_dau") or ""
    snippet = row.get("doan_trich")

    if excluded_reason:
        result = MatchResult(day_id=None, chapter_id=None, confidence="excluded", tier="excluded")
        method = "excluded"
    else:
        # Chỉ so khớp keyword trên CÂU HỎI học viên tự gõ — không gộp doan_trich
        # (đoạn slide đang mở) vào chuỗi so khớp. Nếu gộp, một câu hỏi không
        # liên quan ("làm sao phóng to slide") sẽ bị gán nhầm vào đúng chương
        # của đoạn đang mở, tạo tín hiệu "học viên chưa hiểu chương X" giả —
        # sai lệch trực tiếp bản tin gửi giảng viên (chỗ khó ④ đặc thù domain).
        result = tree.match(question)
        method = result.tier

        if use_llm and result.confidence in ("low", "none"):
            candidates = tree.all_chapters_brief(day_id=result.day_id)  # thu hẹp theo day nếu tier4 đã biết ngày
            if not candidates:
                candidates = tree.all_chapters_brief()
            try:
                llm_out = chat_json(
                    LLM_SYSTEM_PROMPT,
                    build_llm_user_prompt(row.get("cau_hoi_goc") or question, snippet if isinstance(snippet, str) else None, candidates),
                    model=model,
                )
                chapter_id = llm_out.get("chapter_id")
                if chapter_id in tree.valid_chapter_ids():
                    ch = tree.chapter(chapter_id)
                    result = MatchResult(
                        day_id=ch["day_id"],
                        chapter_id=chapter_id,
                        chapter_title=ch["chapter_title"],
                        confidence="medium",
                        tier="llm",
                        matched_terms=[llm_out.get("reason", "")],
                    )
                    method = "llm_accept"
                elif chapter_id == "NONE":
                    method = "llm_none"
                else:
                    # Model trả chapter_id ngoài danh sách hợp lệ -> KHÔNG tin, coi như không xác định.
                    method = "llm_invalid_output"
            except LLMError as exc:
                method = f"llm_error:{type(exc).__name__}"

    return {
        "turn_id": row.get("turn_id"),
        "conversation_id": row.get("conversation_id"),
        "user_id": row.get("user_id"),
        "message_created_at": str(row.get("message_created_at")) if pd.notna(row.get("message_created_at")) else None,
        "cau_hoi_goc": row.get("cau_hoi_goc"),
        "day_id": result.day_id,
        "chapter_id": result.chapter_id,
        "chapter_title": result.chapter_title,
        "confidence": result.confidence,
        "method": method,
        "matched_terms": result.matched_terms,
        "excluded_reason": excluded_reason,
        "tutor_bo_tay": bool(row.get("tutor_bo_tay")) if pd.notna(row.get("tutor_bo_tay")) else None,
        "rating": row.get("rating") if pd.notna(row.get("rating")) else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True, help="turns_clean.jsonl (output của clean_chatlog.py)")
    parser.add_argument("--output", required=True, help="Đường dẫn ghi turns_topics.jsonl")
    parser.add_argument("--no-llm", action="store_true", help="Chỉ chạy tầng 1 (deterministic), bỏ qua LLM fallback — dùng để test nhanh/miễn phí")
    parser.add_argument("--model", default=None, help="Override model OpenRouter (mặc định lấy từ .env OPENROUTER_MODEL)")
    parser.add_argument("--limit", type=int, default=None, help="Chỉ xử lý N turn đầu — dùng để test nhanh")
    args = parser.parse_args()

    tree = KnowledgeTree.load()
    df = pd.read_json(args.input, lines=True)
    if args.limit:
        df = df.head(args.limit)

    records = [classify_turn(row, tree, use_llm=not args.no_llm, model=args.model) for _, row in df.iterrows()]

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    total = len(records)
    by_method: dict[str, int] = {}
    for rec in records:
        by_method[rec["method"]] = by_method.get(rec["method"], 0) + 1
    unclassified = sum(1 for rec in records if rec["chapter_id"] is None and rec["excluded_reason"] is None)

    print(f"Tổng số turn: {total}")
    print("Theo phương pháp gán chủ đề:")
    for method, count in sorted(by_method.items(), key=lambda kv: -kv[1]):
        print(f"  {method}: {count} ({count / total:.1%})")
    print(f"Không xác định được chương (không loại, không match): {unclassified} ({unclassified / total:.1%})")
    print(f"Đã ghi: {out_path}")


if __name__ == "__main__":
    main()

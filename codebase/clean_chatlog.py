"""
Làm sạch file chat_history_anonymized_for_hackathon.csv thành bảng theo từng
turn (1 câu hỏi sinh viên + 1 câu trả lời tutor), sẵn sàng cho bước gán chủ đề
(tầng 1: so khớp slide / tầng 2: gom cụm tự do).

Output mặc định là JSONL (1 dòng = 1 JSON object) — tránh lỗi vỡ cấu trúc khi
xem CSV có nhiều đoạn văn dài/xuống dòng (markdown) trong cùng 1 ô, và là định
dạng chuẩn cho pipeline RAG/embedding. Có thể xuất thêm CSV để xem nhanh bằng
Excel qua cờ --also-csv.

Cách chạy:
    python clean_chatlog.py \
        --input ../data/vlearn-pack/chatlog/chat_history_anonymized_for_hackathon.csv \
        --output ./out/turns_clean.jsonl \
        --also-csv
"""

import argparse
import re
import sys
import unicodedata

import pandas as pd

# Ép stdout dùng UTF-8 để in tiếng Việt không lỗi trên console Windows (cp1252)
sys.stdout.reconfigure(encoding="utf-8")

# Tin nhắn sinh viên đi theo 2 mẫu do UI tự sinh:
# Mẫu 1 — chọn đoạn rồi hỏi thêm:
#   (Trang 37, đoạn được chọn: "tóm tắt nội dung chính trong slide này")
#   tóm tắt nội dung chính trong slide này
SNIPPET_RE = re.compile(
    r'^\(Trang\s*(?P<page>\d+),\s*đoạn được chọn:\s*"(?P<snippet>.*?)"\)\s*\n(?P<question>.*)$',
    re.DOTALL,
)

# Mẫu 2 — bôi đen rồi bấm nút "giải thích", không gõ thêm câu hỏi:
#   Giải thích đoạn bôi đen ở Trang 15.
HIGHLIGHT_RE = re.compile(
    r'^Giải thích đoạn bôi đen ở Trang\s*(?P<page>\d+)\.?(?:\s*:\s*"(?P<snippet>.*)")?\s*$',
    re.DOTALL,
)

# Câu trả lời tutor thuộc dạng "bó tay" — không tìm thấy nội dung tương ứng
TUTOR_PUNT_MARKERS = [
    "không tìm thấy",
    "không có tài liệu",
    "chưa tìm thấy",
    "rất tiếc",
]

# Dấu hiệu học viên cố dò/khai thác system prompt (prompt injection) —
# tách riêng nhóm này để không làm nhiễu bước gom cụm chủ đề học thuật.
INJECTION_MARKERS = [
    "bỏ qua câu hỏi trước",
    "bỏ qua hướng dẫn",
    "hướng dẫn khởi tạo",
    "chỉ dẫn hay vai trò",
    "system prompt",
    "mô tả nguyên văn",
    "initial instructions",
    "ignore previous",
]


def parse_student_content(content: str) -> dict:
    """Tách 1 tin nhắn sinh viên thành: số trang, đoạn được chọn, câu hỏi tự do."""
    if not isinstance(content, str):
        return {"trang": None, "doan_trich": None, "cau_hoi_goc": content}

    stripped = content.strip()

    m = SNIPPET_RE.match(stripped)
    if m:
        return {
            "trang": int(m.group("page")),
            "doan_trich": m.group("snippet").strip(),
            "cau_hoi_goc": m.group("question").strip(),
        }

    m = HIGHLIGHT_RE.match(stripped)
    if m:
        doan_trich = (m.group("snippet") or "").strip() or None
        return {
            "trang": int(m.group("page")),
            "doan_trich": doan_trich,
            # ở mẫu này, thao tác bấm nút chính là "câu hỏi" (không có chữ tự gõ thêm)
            "cau_hoi_goc": stripped,
        }

    return {"trang": None, "doan_trich": None, "cau_hoi_goc": stripped}


def bo_dau(text: str) -> str:
    """Chuẩn hoá tiếng Việt không dấu, phục vụ so khớp mờ (fuzzy match)."""
    if not isinstance(text, str):
        return text
    decomposed = unicodedata.normalize("NFD", text)
    khong_dau = "".join(c for c in decomposed if unicodedata.category(c) != "Mn")
    return khong_dau.replace("đ", "d").replace("Đ", "D")


def chuan_hoa(text: str) -> str:
    """NFC-normalize, gộp khoảng trắng, hạ chữ thường — dùng để so sánh/dedupe."""
    if not isinstance(text, str):
        return text
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()


def la_cau_hoi_lap_lai_doan_trich(cau_hoi: str, doan_trich: str, threshold: float = 0.9) -> bool:
    """True nếu câu hỏi tự do gần như chỉ lặp lại nguyên văn đoạn trích đã chọn."""
    if not cau_hoi or not doan_trich:
        return False
    q, s = chuan_hoa(cau_hoi), chuan_hoa(doan_trich)
    if q == s:
        return True
    # kiểm tra bao hàm đơn giản để bắt các trường hợp gõ lại có sai khác nhỏ
    ngan, dai = sorted([q, s], key=len)
    return bool(ngan) and ngan in dai and len(ngan) / max(len(dai), 1) >= threshold


def la_thao_tac_ui(cau_hoi: str) -> bool:
    """Mẫu 2: 'Giải thích đoạn bôi đen ở Trang N' — cả câu là thao tác UI, không phải câu hỏi tự gõ."""
    return bool(isinstance(cau_hoi, str) and HIGHLIGHT_RE.match(cau_hoi.strip()))


def la_tutor_bo_tay(noi_dung_tutor: str) -> bool:
    if not isinstance(noi_dung_tutor, str):
        return False
    lowered = noi_dung_tutor.lower()
    return any(marker in lowered for marker in TUTOR_PUNT_MARKERS)


def nghi_ngo_prompt_injection(cau_hoi: str) -> bool:
    if not isinstance(cau_hoi, str):
        return False
    lowered = chuan_hoa(cau_hoi)
    return any(marker in lowered for marker in INJECTION_MARKERS)


def gop_theo_turn(df: pd.DataFrame) -> pd.DataFrame:
    sinh_vien = df[df["role"] == "student"].copy()
    tutor = df[df["role"] == "tutor"].copy()

    parsed = sinh_vien["content"].apply(parse_student_content).apply(pd.Series)
    sinh_vien = pd.concat([sinh_vien.reset_index(drop=True), parsed.reset_index(drop=True)], axis=1)

    sinh_vien["cau_hoi_sach"] = sinh_vien["cau_hoi_goc"].apply(chuan_hoa)
    sinh_vien["cau_hoi_khong_dau"] = sinh_vien["cau_hoi_sach"].apply(bo_dau)
    sinh_vien["la_lap_lai_doan_trich"] = sinh_vien.apply(
        lambda r: la_cau_hoi_lap_lai_doan_trich(r["cau_hoi_goc"], r["doan_trich"]), axis=1
    ) | sinh_vien["cau_hoi_goc"].apply(la_thao_tac_ui)
    sinh_vien["nghi_ngo_injection"] = sinh_vien["cau_hoi_goc"].apply(nghi_ngo_prompt_injection)

    tutor = tutor.rename(
        columns={
            "content": "tra_loi_tutor",
            "move_used": "nuoc_di_tutor",
            "citations": "trich_dan_tutor",
        }
    )
    tutor["tutor_bo_tay"] = tutor["tra_loi_tutor"].apply(la_tutor_bo_tay)

    cot_sinh_vien = [
        "turn_id",
        "conversation_id",
        "user_id",
        "day_code",
        "message_created_at",
        "trang",
        "doan_trich",
        "cau_hoi_goc",
        "cau_hoi_sach",
        "cau_hoi_khong_dau",
        "la_lap_lai_doan_trich",
        "nghi_ngo_injection",
    ]
    cot_tutor = ["turn_id", "tra_loi_tutor", "nuoc_di_tutor", "trich_dan_tutor", "tutor_bo_tay", "rating"]

    turns = sinh_vien[cot_sinh_vien].merge(tutor[cot_tutor], on="turn_id", how="left")
    return turns


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Đường dẫn file CSV gốc")
    parser.add_argument(
        "--output", required=True, help="Đường dẫn file đầu ra đã làm sạch (mặc định JSONL)"
    )
    parser.add_argument(
        "--also-csv",
        action="store_true",
        help="Xuất thêm bản .csv cùng tên (để xem nhanh bằng Excel) — chỉ dùng để xem, đừng dùng để nạp vào RAG",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    turns = gop_theo_turn(df)

    turns.to_json(args.output, orient="records", lines=True, force_ascii=False)

    if args.also_csv:
        csv_path = re.sub(r"\.jsonl?$", "", args.output) + ".csv"
        turns.to_csv(csv_path, index=False, encoding="utf-8-sig")
        print(f"Đã xuất thêm bản xem nhanh: {csv_path}")

    tong = len(turns)
    lap_lai = turns["la_lap_lai_doan_trich"].sum()
    bo_tay = turns["tutor_bo_tay"].sum()
    nghi_ngo = turns["nghi_ngo_injection"].sum()
    print(f"Tổng số turn: {tong}")
    print(f"Câu hỏi lặp lại đoạn trích / thao tác UI: {lap_lai} ({lap_lai / tong:.1%})")
    print(f"Tutor bó tay (không tìm thấy nội dung): {bo_tay} ({bo_tay / tong:.1%})")
    print(f"Nghi ngờ prompt injection: {nghi_ngo} ({nghi_ngo / tong:.1%})")
    print(f"Không tách được số trang (không khớp mẫu nào): {turns['trang'].isna().sum()}")


if __name__ == "__main__":
    main()

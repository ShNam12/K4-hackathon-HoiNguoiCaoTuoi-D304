"""
UI Streamlit cho prototype: "Bản tin cuối ngày cho giảng viên".

Lát cắt: giảng viên (1 user) hỏi "hôm nay lớp vướng chủ đề nào" (1 job) → AI
gán từng câu hỏi học viên vào đúng chương trong cây tri thức rồi tổng hợp,
xếp hạng, viết bản tin (1 quyết định AI) → top-N chủ đề kèm bằng chứng câu
hỏi thật (1 kết quả).

Chạy: streamlit run app.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

from classify_turns import classify_turn
from clean_chatlog import gop_theo_turn
from daily_digest import aggregate, build_digest, render_fallback_digest
from knowledge_tree import KnowledgeTree
from llm_client import LLMError

st.set_page_config(page_title="Bản tin chủ đề cho giảng viên", layout="wide")

DEFAULT_CSV = Path(__file__).resolve().parent.parent / "data" / "vlearn-pack" / "chatlog" / "chat_history_anonymized_for_hackathon.csv"
OUT_DIR = Path(__file__).resolve().parent / "out"
OUT_DIR.mkdir(exist_ok=True)


@st.cache_resource
def load_tree() -> KnowledgeTree:
    return KnowledgeTree.load()


@st.cache_data(show_spinner=False)
def load_and_clean(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return gop_theo_turn(df)


st.title("📋 Bản tin cuối ngày cho giảng viên")
st.caption(
    "Giảng viên hỏi: *\"5 chủ đề sinh viên hôm nay chưa hiểu hết\"* → AI gán câu hỏi vào "
    "đúng chương trong cây tri thức day/chapter, rồi tổng hợp top-N chủ đề kèm câu hỏi thật làm bằng chứng."
)

with st.sidebar:
    st.header("1️⃣ Nạp & làm sạch chatlog")
    csv_path = st.text_input("Đường dẫn CSV", value=str(DEFAULT_CSV))
    if st.button("Làm sạch", use_container_width=True):
        with st.spinner("Đang gộp theo turn..."):
            st.session_state["turns_clean"] = load_and_clean(csv_path)
        st.success(f"Đã làm sạch: {len(st.session_state['turns_clean'])} turn")

    st.header("2️⃣ Gán chủ đề")
    use_llm = st.checkbox("Dùng LLM cho câu tầng 1 không chắc (tầng 2)", value=False, help="Cần OPENROUTER_API_KEY trong codebase/.env — tắt để test nhanh/miễn phí")
    limit = st.number_input("Giới hạn số turn (0 = tất cả)", min_value=0, value=200, step=50, help="Giới hạn để tránh gọi LLM quá nhiều khi test")
    if st.button("Gán chủ đề", use_container_width=True):
        if "turns_clean" not in st.session_state:
            st.error("Chưa có dữ liệu — bấm 'Làm sạch' trước.")
        else:
            tree = load_tree()
            df = st.session_state["turns_clean"]
            if limit:
                df = df.head(limit)
            progress = st.progress(0.0, text="Đang gán chủ đề...")
            records = []
            n = len(df)
            for i, (_, row) in enumerate(df.iterrows()):
                records.append(classify_turn(row, tree, use_llm=use_llm, model=None))
                if i % max(1, n // 20) == 0:
                    progress.progress(min(1.0, (i + 1) / n), text=f"Đã xử lý {i + 1}/{n}")
            progress.empty()
            st.session_state["turns_topics"] = records
            st.success(f"Đã gán chủ đề cho {len(records)} turn")

if "turns_topics" not in st.session_state:
    st.info("👈 Chạy bước 1 và 2 ở sidebar trước.")
    st.stop()

records = st.session_state["turns_topics"]

st.header("3️⃣ Bản tin cho giảng viên")
available_dates = sorted({str(r["message_created_at"])[:10] for r in records if r.get("message_created_at")})
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    target_date = st.selectbox("Ngày", options=available_dates, index=len(available_dates) - 1 if available_dates else 0) if available_dates else None
with col2:
    top_n = st.slider("Top N chủ đề", 1, 10, 5)
with col3:
    digest_use_llm = st.checkbox("AI viết văn bản tin", value=False, help="Tắt = chỉ hiện bảng thô, không gọi LLM")

if st.button("📨 Tạo bản tin", type="primary"):
    top_rows, meta = aggregate(records, target_date=target_date, top_n=top_n)
    if digest_use_llm:
        try:
            digest = build_digest(top_rows, meta)
        except LLMError as exc:
            digest = render_fallback_digest(top_rows, meta)
            st.warning(f"LLM lỗi, hiện bảng thô: {exc}")
    else:
        digest = render_fallback_digest(top_rows, meta)

    st.markdown(digest)

    st.subheader("Bảng số liệu gốc (đối chiếu)")
    st.json({"meta": meta})
    if top_rows:
        st.dataframe(pd.DataFrame(top_rows))

    excluded_pct = meta["excluded_today"] / meta["total_turns_today"] if meta["total_turns_today"] else 0
    unclassified_pct = meta["unclassified_today"] / meta["total_turns_today"] if meta["total_turns_today"] else 0
    st.caption(
        f"Tổng {meta['total_turns_today']} turn hôm {meta['date']}: "
        f"{meta['classified_today']} đã gán chủ đề · {meta['excluded_today']} loại (UI/injection/dán nguyên văn, {excluded_pct:.0%}) · "
        f"{meta['unclassified_today']} không xác định được chương ({unclassified_pct:.0%})."
    )

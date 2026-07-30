# Bản tin cuối ngày cho giảng viên — prototype

**Lát cắt:** giảng viên (1 user) · muốn biết cuối ngày lớp đang vướng chủ đề nào (1 job) ·
AI gán từng câu hỏi học viên vào đúng chương trong cây tri thức rồi tổng hợp, xếp hạng,
viết bản tin (1 quyết định AI) · nhận về top-N chủ đề kèm câu hỏi thật làm bằng chứng (1 kết quả).

## Pipeline

```
chat_history_anonymized_for_hackathon.csv
        │  clean_chatlog.py
        ▼
   turns_clean.jsonl            (1 dòng = 1 turn: câu hỏi học viên + câu trả lời tutor)
        │  classify_turns.py
        │    tầng 1: so khớp keyword với knowledge-tree-day-chapter.json (miễn phí, tất định)
        │    tầng 2: câu tầng 1 không đủ tự tin → gọi LLM thật (OpenRouter), CHỈ được
        │            chọn trong danh sách chapter_id đã biết hoặc NONE (không bịa)
        ▼
   turns_topics.jsonl           (mỗi turn đã gắn day_id/chapter_id/confidence)
        │  daily_digest.py
        │    gộp theo chương, xếp hạng top-N, gọi LLM viết bản tin — LUÔN kèm bảng
        │    số liệu gốc để đối chiếu, không chỉ tin vào văn xuôi AI viết
        ▼
   Bản tin: "N chủ đề học viên hôm nay chưa hiểu hết" + ví dụ câu hỏi thật
```

## Setup

```bash
cd codebase
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash; dùng .venv/bin/activate trên macOS/Linux
python -m pip install -r requirements.txt
cp .env.example .env
```

Mở `.env`, điền `OPENROUTER_API_KEY` (lấy tại https://openrouter.ai/keys), lưu lại. Chỉ vậy là xong — không cần sửa code.

> **Lưu ý Python:** cần Python 3.11–3.12. Python 3.14 hiện chưa có wheel sẵn cho `pandas`/`numpy` trên Windows, pip sẽ cố build từ source và lỗi. Máy này đã tạo `.venv` bằng `Python312`.

## Chạy từng bước

```bash
# 1. Làm sạch CSV thành turns_clean.jsonl
python clean_chatlog.py \
  --input ../data/vlearn-pack/chatlog/chat_history_anonymized_for_hackathon.csv \
  --output ./out/turns_clean.jsonl

# 2. Gán chủ đề (thử --no-llm trước để xem tầng 1 chạy được bao nhiêu % miễn phí)
python classify_turns.py --input ./out/turns_clean.jsonl --output ./out/turns_topics.jsonl --no-llm
python classify_turns.py --input ./out/turns_clean.jsonl --output ./out/turns_topics.jsonl --limit 50   # test tầng 2 với ít turn trước khi chạy full (tốn quota LLM)

# 3. Tạo bản tin cho một ngày cụ thể
python daily_digest.py --input ./out/turns_topics.jsonl --date 2026-07-27 --top-n 5
```

UI Streamlit (`app.py`) tái dùng đúng các hàm trên, có nút bấm cho từng bước — cần `pip install streamlit` (đã có trong `requirements.txt`) rồi chạy `streamlit run app.py`.

## Agent — hỏi tự do bằng tiếng Việt (tool-calling)

Ngoài `daily_digest.py` (workflow cố định qua CLI), có một agent thật để giảng viên hỏi tự
do — model tự chọn tool thay vì chạy đúng 1 luồng cứng. Kiến trúc mirror `agent.py`/`chat.py`
của dự án tham khảo `K4-Day04-D304-B3`, thu gọn cho 1 provider (OpenRouter) và 3 tool:

```
artifacts/
  system_prompt.md   ← luật cho agent: không bịa số liệu, kiểm tra phạm vi ngày trước,
                        chọn đúng tool theo ý định, cảnh báo khi tutor_bo_tay_rate cao
  tools.yaml          ← khai báo 3 tool (tên, mô tả, JSON schema tham số) cho model
tools/
  _shared.py                    ← helper dùng chung (đọc turns_topics.jsonl, format lỗi)
  get_topic_digest/             ← top-N chủ đề của 1 ngày (tái dùng daily_digest.aggregate)
  get_topic_examples/           ← đào sâu ví dụ câu hỏi của 1 chương cụ thể
  list_available_dates/         ← ngày nào có dữ liệu — tránh agent bịa ngày không tồn tại
  __init__.py                   ← TOOL_FUNCTIONS + load_tool_declarations + to_openai_tools
agent.py              ← vòng lặp: gọi model có tool → chạy tool thật → đưa kết quả lại
                          cho model viết câu trả lời cuối (tối đa 4 vòng, chống lặp vô hạn)
chat.py               ← REPL nhiều lượt cho giảng viên, ghi transcript JSON mỗi lượt
```

Chạy nhanh 1 câu hỏi:

```bash
python agent.py "5 chủ đề sinh viên hôm nay chưa hiểu hết"
```

Chat nhiều lượt (giữ ngữ cảnh, ghi transcript vào `transcripts/`):

```bash
python chat.py
```

Đổi tên tool phải sync đồng bộ 3 chỗ: `artifacts/tools.yaml` → `tools/__init__.py`
(`TOOL_FUNCTIONS`) → thư mục `tools/<tool_name>/`.

## File

| File | Vai trò |
|---|---|
| `clean_chatlog.py` | Làm sạch CSV gốc → 1 dòng/turn (đã có sẵn, chỉ sửa 1 bug NaN khi `doan_trich` rỗng) |
| `knowledge_tree.py` | Nạp `data/vlearn-pack/slides/knowledge-tree-day-chapter.json`, so khớp câu hỏi → (day_id, chapter_id). Tự test: `python knowledge_tree.py` |
| `llm_client.py` | Gọi OpenRouter qua SDK `openai` — `chat_json()` (ép JSON, dùng cho pipeline) + `complete_with_tools()` (function calling, dùng cho agent) |
| `classify_turns.py` | Tầng 1 (keyword) + tầng 2 (LLM fallback), loại câu hỏi không phải tín hiệu chủ đề thật |
| `daily_digest.py` | Gộp theo chương, xếp hạng, gọi LLM viết bản tin cho giảng viên (workflow cố định) |
| `agent.py` / `chat.py` | Agent tool-calling — giảng viên hỏi tự do, model tự chọn tool |
| `app.py` | UI Streamlit — chạy pipeline cố định bằng nút bấm |

## Chỗ khó đã xử lý (đối chiếu §5 spec)

- **① Nguồn sự thật:** LLM tầng 2 chỉ được chọn `chapter_id` có trong danh sách đưa cho nó; trả `chapter_id` lạ → bị từ chối, coi như không xác định (`llm_invalid_output`), không tin mù quáng.
- **② Mơ hồ:** so khớp keyword không đủ tự tin (confidence `low`/`none`) mới rơi xuống tầng 2; tầng 2 vẫn không chắc thì trả `NONE` thay vì đoán.
- **④ Đặc thù domain:** ban đầu bộ so khớp gộp cả đoạn slide đang mở (`doan_trich`) vào câu hỏi để so khớp → một câu hỏi UI không liên quan ("làm sao phóng to slide") bị gán nhầm vào đúng chương của đoạn đang mở, tạo tín hiệu "học viên chưa hiểu chương X" giả. Đã sửa: chỉ so khớp trên câu hỏi học viên tự gõ. Tương tự, câu hỏi > 350 ký tự (nghi là dán nguyên văn slide do lỗi tách của `clean_chatlog.py`) bị loại khỏi thống kê thay vì tin một match có thể sai.
- **Bảo mật data:** trích dẫn trong bản tin bị cắt còn tối đa 160 ký tự (`daily_digest.truncate_quote`) — không dán nguyên văn dài từ data pack.
- **① Nguồn sự thật (agent):** `get_topic_examples` từ chối `chapter_id` không khớp cây tri thức thay vì đoán chương gần giống; `list_available_dates` cho agent kiểm tra phạm vi ngày trước khi trả lời, tránh bịa ngày không có dữ liệu.

## Giới hạn đã biết

- Cây tri thức hiện chỉ phủ **Day 01 và Day 02** (từ 4 file slide được cấp). Chatlog thực tế trải dài 22/07–29/07 và có nhắc tới nội dung Day 05 (`day05-lecture-slides-batch03.pdf`) — những câu hỏi thuộc các ngày chưa có trong cây tri thức sẽ luôn rơi vào "không xác định", không phải lỗi của matcher.
- `out/` bị gitignore — mọi file trong đó (turns_clean.jsonl, turns_topics.jsonl...) chứa nguyên văn chatlog, **không được commit** theo quy định bảo mật data pack.
- Chưa chạy test với LLM thật (chưa có API key lúc viết code) — đã verify pipeline không crash khi thiếu key (`LLMError` được bắt gọn, fallback về bảng thô) và toàn bộ file mới compile sạch (`python -m py_compile`). Nên chạy `--limit 20` hoặc `--limit 50` trước khi chạy full 1261 turn để kiểm tra chất lượng phân loại tầng 2 trước khi tốn quota; tương tự thử `agent.py`/`chat.py` với vài câu hỏi trước khi demo.
- `agent.py`/`chat.py` cần `turns_topics.jsonl` đã tồn tại (chạy `classify_turns.py` trước) — tool sẽ trả lỗi rõ ràng ("Chưa có ... — chạy classify_turns.py trước") nếu file chưa có, không crash im lặng.

# Reflection — Phạm Hoàng Nam (2A202601442) — P5, API, schema, eval và packaging

## 1. Vai trò và phần tôi phụ trách

Theo `PLAN_10_GIO.md` §0.1 và §4, tôi là **P5 — API/Eval**, sở hữu:

- `backend/backend_app.py`, `backend/schemas.py` — endpoint `GET /health`, `POST /api/analyze`.
- `backend/fixtures/**` — `demo_request.json`, `demo_response.json`.
- `backend/tests/test_api_contract.py`, `backend/tests/test_health.py`.
- `eval/**` — `golden_set.jsonl`, `evaluate.py`, `results/run-001.json` … `run-current.json`.
- `requirements.txt`, `.env.example`.

Tôi dựng schema, fixture và API stub trước (`feat(api-eval): add schema, fixtures, API stub, eval
skeleton`) để P2/P3/P4 có contract cố định mà làm việc song song. Sau khi P3 có `classify_batch`
thật, tôi nối lại pipeline trong `backend_app.py` (`feat(api): wire real analyze pipeline, remove
unused mongo backend`) — bỏ nhánh Mongo cũ không dùng tới, gọi thẳng
`taxonomy_loader → classify_batch` thật thay vì fixture giả. Tôi cũng sửa một số chỗ dữ liệu ở
frontend không khớp với response thật (`fix: wire real question data + AI reply suggestions into
dashboard`, `fix: auto-load real data on open, rebuild topic drawer with real content`) khi phát
hiện lúc tích hợp UI với API thật. Ngoài ra tôi viết script chuẩn hóa chat log thô thành JSONL theo
turn để P1 và tôi dùng chung khi mining evidence.

Trong `classify_batch`, một câu hỏi lỗi được cô lập bằng try/except riêng cho từng question
(`backend/services/taxonomy_matcher.py`), nên một câu hỏng không kéo cả batch trả lỗi — đây là bất
biến tôi kiểm khi viết `evaluate.py` (`batch_survived` flag).

## 2. AI hỗ trợ tôi như thế nào

Tôi dùng AI để phác thảo khung ban đầu của `eval/evaluate.py` (đọc golden set theo JSONL, tính
`topic_correct_or_abstain_rate`, `status_correct_rate`, `high_confidence_wrong_count`) và để rà
soát nhanh phần schema trong `backend/schemas.py` cho khớp với `spec.md`. Phần tôi tự quyết định,
AI không quyết thay: thứ tự merge (`P5 schema → P3 matcher → P4 grouper → P5 nối pipeline → P2
frontend`), và việc không đổi quality bar sau lần chạy đầu dù run sau có thể thấp hơn — quy định
này nằm trong `PLAN_10_GIO.md` §5 để tránh cả nhóm chỉnh chuẩn theo kết quả có lợi.

## 3. Một bài học từ case fail của chính nhóm

So sánh `eval/results/run-001.json` (65% correct-or-abstain, 5 high-confidence-wrong) với các lần
chạy sau: `run-004.json` đạt 85%/0.80, 2 high-confidence-wrong, nhưng `run-current.json` — chạy
lại đúng cùng commit, cách nhau 4 phút — chỉ còn 75%/0.75, 5 high-confidence-wrong. Vì cả hai dùng
cùng code (`classify_batch (real)`, cùng golden set), khác biệt này không phải do ai sửa gì mà là
do bản thân LLM classifier không ổn định giữa các lần gọi — một run đơn lẻ không đủ để làm căn cứ
"đạt chuẩn 80%". Bài học: quality bar dựa trên một lần chạy dễ gây ảo tưởng ổn định; cần chạy lặp
lại và báo cáo khoảng dao động (mean/min/max) thay vì một con số duy nhất, đặc biệt với case
grounding như GS009 (khớp từ "tham số" nhưng không có tài liệu hỗ trợ tính GPU) — case này vẫn sai
ở cả hai run và là failure nguy hiểm nhất vì trả confidence cao dù không có căn cứ.

## 4. Nếu có thêm một tuần

- Thêm gate chặn high-confidence khi evidence chỉ là keyword overlap không đủ ngữ nghĩa (sửa GS009),
  và chạy golden set lặp lại (5+ lần) để báo cáo canonical run bằng khoảng dao động thay vì một run.
- Thêm các metric còn thiếu vào `evaluate.py`: schema-valid rate, supported-question-ID validity,
  batch-survival khi timeout — hiện chỉ có correct-or-abstain và high-confidence-wrong.

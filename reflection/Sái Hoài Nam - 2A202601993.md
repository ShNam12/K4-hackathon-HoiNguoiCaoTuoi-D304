<!--
HƯỚNG DẪN (xoá comment này trước khi nộp):
1. Đổi tên file này thành "<ma-hoc-vien>-<Ten-Khong-Dau>.md".
2. Tự viết nội dung — khung theo đúng rubric 04-rubric.md mục "Reflection cá nhân".
3. Xoá phần hướng dẫn này khi hoàn tất.
-->

# Reflection — [Họ tên] ([Mã học viên]) — P5, API, schema, eval và packaging

## 1. Vai trò và phần tôi phụ trách

Theo `PLAN_10_GIO.md` §0.1 và §4, tôi là **P5 — API/Eval**, sở hữu:

- `backend/__init__.py`, `backend/backend_app.py`, `backend/schemas.py` — endpoint
  `GET /health`, `POST /api/analyze`, schema version `1.0`.
- `backend/fixtures/**` — `demo_request.json`, `demo_response.json`.
- `backend/tests/test_api_contract.py`, `backend/tests/test_health.py`.
- `eval/**` — `golden_set.jsonl`, `evaluate.py`, `results/run-001.*`, `results/run-002.*`.
- `requirements.txt`, `.env.example`, `.gitignore`, `backend/README.md`.

[Điền cụ thể: cách bạn nối pipeline `request → taxonomy loader → classify_batch →
group_classifications → summarize_groups → response schema` trong `backend_app.py`, cách bạn đảm
bảo một question lỗi không làm cả batch trả HTTP 500, cách bạn thiết kế golden set 20+ case theo
6 nhóm ở `PLAN_10_GIO.md` §8.5.]

## 2. AI hỗ trợ tôi như thế nào

[Điền cụ thể — ví dụ: dùng AI để viết `eval/evaluate.py` (tính schema-valid rate, topic
correct-or-abstain rate, high-confidence wrong count...), để soát secret trước khi commit
(`rg -n "AIza|sk-|mongodb\+srv|api[_-]?key..."`). Nêu rõ phần bạn tự quyết định (vd: thứ tự merge,
quality bar) mà AI không tự quyết định thay được.]

## 3. Một bài học từ case fail của chính nhóm

[Bắt buộc: chọn MỘT case fail thật — ví dụ từ `eval/results/run-001.json` (case fail trước khi
sửa) so với `run-002.json` (sau khi P3/P4 sửa module tương ứng). Nêu bạn phát hiện case đó thế
nào, điều phối ai sửa, và số liệu thay đổi ra sao giữa hai lần chạy.]

## 4. Nếu có thêm một tuần

[1-2 gạch đầu dòng.]

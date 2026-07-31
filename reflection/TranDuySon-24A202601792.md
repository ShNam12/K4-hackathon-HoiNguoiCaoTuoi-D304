<!--
HƯỚNG DẪN (xoá comment này trước khi nộp):
1. Đổi tên file này thành "<ma-hoc-vien>-<Ten-Khong-Dau>.md".
2. Tự viết nội dung — khung theo đúng rubric 04-rubric.md mục "Reflection cá nhân".
3. Xoá phần hướng dẫn này khi hoàn tất.
-->

# Reflection — [Họ tên] ([Mã học viên]) — P4, Grouping, intent và grounded summary

## 1. Vai trò và phần tôi phụ trách

Theo `PLAN_10_GIO.md` §0.1 và §4, tôi là **P4 — Grouping/Summary**, sở hữu:

- `backend/services/question_grouper.py` — group deterministic theo `topic_id` (chỉ
  `auto_grouped`), đếm `question_count`, đếm distinct `student_id`, tính `dominant_intent`.
- `backend/services/group_summarizer.py` — tạo summary chỉ dùng nội dung câu hỏi trong group,
  luôn trả `supported_question_ids`, có fallback deterministic khi LLM lỗi/timeout.
- `backend/prompts/group_summary.md`.
- `backend/tests/test_question_grouper.py`, `backend/tests/test_group_summarizer.py`.

[Điền cụ thể: cách bạn tính dominant intent khi hoà (tie-breaker), cách bạn đảm bảo
supported_question_ids luôn là tập con hợp lệ của group, fallback hoạt động ra sao khi bạn cố tình
gây timeout/mock exception để test.]

## 2. AI hỗ trợ tôi như thế nào

[Điền cụ thể — ví dụ: dùng AI để viết prompt `group_summary.md` với ràng buộc "chỉ dùng nội dung
được cung cấp", để sinh test case cho 11 case bắt buộc ở `PLAN_10_GIO.md` §5 (P4). Nêu rõ phần bạn
tự đọc tay để phát hiện claim không có trong câu hỏi gốc (chống hallucination) — đây là bước AI
không tự làm thay được.]

## 3. Một bài học từ case fail của chính nhóm

[Bắt buộc: chọn MỘT case fail thật — ví dụ một summary bị phát hiện "bịa" chi tiết không có trong
câu hỏi gốc, hoặc supported_question_ids sai lệch, phát hiện qua golden set (`eval/results/`) hoặc
qua human review (`PLAN_10_GIO.md` §8.6). Nêu nguyên nhân, cách sửa trong file bạn sở hữu, và
regression test đã thêm.]

## 4. Nếu có thêm một tuần

[1-2 gạch đầu dòng.]

<!--
HƯỚNG DẪN (xoá comment này trước khi nộp):
1. Đổi tên file này thành "<ma-hoc-vien>-<Ten-Khong-Dau>.md".
2. Tự viết nội dung — khung theo đúng rubric 04-rubric.md mục "Reflection cá nhân".
3. Xoá phần hướng dẫn này khi hoàn tất.
-->

# Reflection — [Họ tên] ([Mã học viên]) — P2, Frontend và trải nghiệm giảng viên

## 1. Vai trò và phần tôi phụ trách

Theo `PLAN_10_GIO.md` §0.1 và §4, tôi là **P2 — Frontend**, sở hữu:

- `frontend/index.html` — dashboard giảng viên (selector buổi học, nút phân tích, top topic
  cards, detail drawer, evidence/source, review queue, correction dropdown).
- `frontend/api.js` — `analyzeQuestions(payload)` gọi backend thật, `loadDemoResponse()` fallback
  khi API lỗi/chưa chạy.
- `frontend/demo_response.json` — fixture để phát triển UI không cần chờ backend.
- `frontend/README.md`.

[Điền cụ thể: những state nào bạn đã làm (loading/empty/error/review/unmatched), cách bạn xử lý
fallback khi backend lỗi, cách bạn test mobile/desktop.]

## 2. AI hỗ trợ tôi như thế nào

[Điền cụ thể — ví dụ: dùng AI để dựng khung layout ban đầu, để viết `api.js` với try/catch fallback,
để rà soát escape text từ API trước khi render (tránh XSS). Nêu rõ phần nào bạn tự chỉnh vì AI làm
chưa đúng ý (ví dụ hiển thị confidence dạng % thay vì high/medium/low — điều `PLAN_10_GIO.md` §2.2
cấm).]

## 3. Một bài học từ case fail của chính nhóm

[Bắt buộc: chọn MỘT case fail thật — ví dụ một quote từ `validation/feedback-log.md` về UI khó dùng,
hoặc một bug hiển thị bị phát hiện lúc integration test (`PLAN_10_GIO.md` Giai đoạn 3). Nêu nguyên
nhân, cách sửa, kết quả.]

## 4. Nếu có thêm một tuần

[1-2 gạch đầu dòng.]

# Reflection — Dương Ngọc Hải (2A202601748) — P2, Frontend và trải nghiệm giảng viên

## 1. Vai trò và phần tôi phụ trách

Theo `PLAN_10_GIO.md` §0.1 và §4, tôi là **P2 — Frontend**, sở hữu:

- `frontend/index.html` — dashboard giảng viên (selector buổi học, nút phân tích, top topic cards, detail drawer, evidence/source, review queue, correction dropdown).
- `frontend/api.js` — `analyzeQuestions(payload)` gọi backend thật, `loadDemoResponse()` fallback khi API lỗi/chưa chạy.
- `frontend/demo_response.json` — fixture để phát triển UI không cần chờ backend.
- `frontend/README.md`.

Cụ thể, tôi đã thực hiện xây dựng UI dựa trên framework hiện tại mà không rewrite. Các state tôi đã xử lý gồm:
- **Loading state**: Vô hiệu hóa nút phân tích và hiển thị trạng thái loading trong khi chờ API hoặc tải fixture.
- **Empty state**: Hiển thị thông báo khi `groups = []` hoặc chưa có dữ liệu.
- **Error/Fallback**: Trong trường hợp gọi `analyzeQuestions(payload)` bị timeout hoặc lỗi mạng, hệ thống tự động gọi `loadDemoResponse()` và hiển thị text thông báo "Demo data".
- **Review/Unmatched**: Hiển thị luồng low-confidence queue để giảng viên trực tiếp review và sử dụng dropdown để correction.
- Về tính Responsive, tôi đã test kỹ trên kích thước mobile (khoảng 390px) để các câu hỏi chứa văn bản dài không bị vỡ layout, đồng thời đảm bảo hiển thị đủ nội dung trên màn hình desktop (khoảng 1366px).

## 2. AI hỗ trợ tôi như thế nào

Tôi đã sử dụng AI để hỗ trợ phần lớn công việc phát triển frontend:
- **Dựng khung layout ban đầu**: Dùng AI để sinh HTML/CSS structure cho phần top topic cards và detail drawer.
- **Viết logic cho `api.js`**: Dùng AI để viết hàm `analyzeQuestions` với `try/catch` đầy đủ và tự động fallback sang `loadDemoResponse()` khi catch lỗi.
- **Rà soát lỗi**: Yêu cầu AI hướng dẫn cách escape text từ API trước khi render để phòng chống XSS.
- **Phần tự chỉnh sửa**: AI ban đầu tự động sinh ra progress bar hiển thị confidence dạng %, tôi đã phát hiện và tự sửa lại để sử dụng đúng nhãn `high`, `medium`, `low` theo yêu cầu tại `PLAN_10_GIO.md` §2.2 (không dùng confidence xác suất kiểu 94%).

## 3. Một bài học từ case fail của chính nhóm

Trong quá trình Integration test ở Giai đoạn 3, khi kết nối pipeline thực tế với backend API, có phát sinh lỗi giao diện khi câu hỏi của sinh viên chứa đoạn text rất dài không có khoảng trắng làm vỡ layout ở khu vực `detail drawer`.
- **Nguyên nhân**: Ban đầu, UI render trực tiếp text từ JSON mà không thiết lập quy tắc ngắt dòng hợp lý trong CSS, đồng thời tôi chưa đưa một test case về "text rất dài" vào `demo_response.json` để test lúc dev.
- **Cách sửa**: Tôi bổ sung thuộc tính CSS `word-break: break-word` cho các đoạn text câu hỏi để ép xuống dòng nếu quá dài. Đồng thời, tôi update `demo_response.json` bằng việc cho một câu hỏi cực dài vào để làm test case vĩnh viễn, tránh tái diễn lỗi.
- **Kết quả**: Giao diện hiển thị ổn định trên mọi màn hình (kể cả mobile 390px) và không còn tình trạng vỡ layout với văn bản lạ.

## 4. Nếu có thêm một tuần

- Tôi sẽ tinh chỉnh lại UX, bổ sung thêm vi-tương-tác (micro-animations) mượt mà hơn khi thao tác chuyển câu hỏi từ trạng thái "Cần duyệt" sang "Đã duyệt".
- Viết unit test cho các thao tác chuyển dữ liệu ở UI và tối ưu lại cơ chế gọi API để tránh reload dữ liệu khi không cần thiết.

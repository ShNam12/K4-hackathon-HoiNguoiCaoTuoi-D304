# Frontend Trợ lý Giảng viên AI

Đây là phần Frontend được xây dựng cho dự án MVP 10 giờ.

## Cách chạy (Development)

Để các tính năng fetch file JSON (như `demo_response.json`) hoạt động đúng và không bị chặn bởi chính sách CORS của trình duyệt, bạn cần chạy qua một HTTP Server:

```powershell
python -m http.server 5500 --directory frontend
```

Sau đó mở trình duyệt ở địa chỉ: [http://localhost:5500](http://localhost:5500)

## Các tệp chính
- `index.html`: Giao diện chính của Dashboard.
- `api.js`: File chứa logic gọi API lên backend (`analyzeQuestions`) và fallback đọc dữ liệu mẫu (`loadDemoResponse`).
- `demo_response.json`: Dữ liệu JSON mẫu (fixture) để giả lập response từ backend.

## Lưu ý về API Fallback
Trong quá trình phát triển (khi Backend chưa code xong hoặc đang gặp lỗi), hàm `analyzeQuestions` trong `api.js` sẽ tự động catch lỗi và fallback về việc tải `demo_response.json`. Nhờ đó, Frontend team có thể liên tục phát triển UI mà không bị gián đoạn.

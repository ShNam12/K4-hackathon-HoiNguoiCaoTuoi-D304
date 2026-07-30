# Kịch bản kiểm thử với người dùng

## 1. Mục tiêu

Kiểm tra xem người dùng có thể:

1. Xác định phần kiến thức cần giảng lại.
2. Hiểu căn cứ của kết quả phân loại và tóm tắt.
3. Phát hiện câu hỏi có kết quả chưa đáng tin.
4. Sửa taxonomy hoặc giữ câu hỏi ở trạng thái cần duyệt.

## 2. Đối tượng và điều kiện

- Mỗi thành viên kiểm thử với một người ngoài nhóm.
- Ưu tiên giảng viên, trợ giảng hoặc người có thể đóng vai giảng viên.
- Mỗi phiên tối đa 10 phút.
- Prototype được mở qua HTTP server, không mở bằng `file://`.
- Dùng cùng một batch câu hỏi và cùng phiên bản prototype giữa các phiên
  nếu nhóm đang so sánh kết quả.

Không ghi thông tin cá nhân không cần thiết. Chỉ ghi tên hoặc vai trò khi
người tham gia đồng ý.

## 3. Quy tắc dành cho người quan sát

- Đọc task một lần và để người dùng tự thực hiện.
- Không thuyết minh tính năng trong lúc người dùng làm task.
- Không chỉ vị trí nút trừ khi người dùng không thể tiếp tục.
- Ghi hành vi quan sát được trước khi hỏi ý kiến.
- Ghi quote ngắn, không diễn giải thành lời có lợi cho sản phẩm.
- Không chỉ hỏi giao diện có đẹp hay không.

## 4. Task giao cho người dùng

> Đây là danh sách câu hỏi sau một buổi học. Hãy dùng hệ thống để xác định
> phần nào cần giảng lại trước và kiểm tra xem có câu nào được phân loại
> chưa đáng tin.

## 5. Kịch bản thao tác cần quan sát

Người quan sát không đọc các bước này cho người dùng:

1. Chọn `DAY_01`.
2. Phân tích batch câu hỏi.
3. Xác định topic cần giảng lại trước.
4. Giải thích dữ liệu nào dẫn tới lựa chọn đó.
5. Mở một topic và xem câu hỏi đại diện/evidence.
6. Tìm một câu low-confidence hoặc unmatched.
7. Sửa taxonomy hoặc giữ câu ở trạng thái cần duyệt.

## 6. Checklist quan sát

| Điều cần quan sát | Có | Không | Ghi chú |
|---|:---:|:---:|---|
| Tìm được session selector |  |  |  |
| Tìm được nút Phân tích |  |  |  |
| Hiểu question count |  |  |  |
| Hiểu unique student count |  |  |  |
| Xác định được top topic |  |  |  |
| Mở được evidence/source |  |  |  |
| Nhận ra confidence `high/medium/low` |  |  |  |
| Nhận ra review queue |  |  |  |
| Sửa được taxonomy |  |  |  |
| Hiểu nhãn “Demo data” nếu fallback |  |  |  |

## 7. Ba câu hỏi bắt buộc sau task

1. Điều gì khó hiểu hoặc khó chịu nhất?
2. Bạn có tin kết quả phân loại/tóm tắt này không? Vì sao?
3. Nếu là giảng viên, bạn có dùng kết quả này để quyết định phần cần
   giảng lại không? Vì sao?

## 8. Mẫu log gửi cho P1

```text
Session ID:
Ngày giờ:
Người test/vai trò:
Người quan sát:
Phiên bản hoặc commit:

Task hoàn thành: Có/Không
Thời gian hoàn thành:
Topic người dùng chọn:
Căn cứ người dùng sử dụng:
Người dùng có nhận ra low-confidence: Có/Không
Người dùng có sửa được taxonomy: Có/Không

Điểm bị kẹt:
Hành vi quan sát được:
Quote ngắn:
Vấn đề nghiêm trọng nhất:
Mức độ: P0/P1/P2
Đề xuất thay đổi:
Case/evidence liên quan:
```

## 9. Tiêu chí hoàn thành vòng validation

- Có ít nhất năm log từ năm người ngoài nhóm.
- Mỗi log có vai trò người test, kết quả task, hành vi quan sát và ít nhất
  một quote ngắn.
- Không thay đổi hoặc xóa feedback bất lợi.
- Mỗi thay đổi sản phẩm phải trỏ được về một log hoặc case cụ thể.
- P1 tổng hợp các log vào `validation/feedback-log.md`.

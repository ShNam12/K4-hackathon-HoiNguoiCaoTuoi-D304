# CP4 — Nội dung form do P1 tổng hợp

## Thông tin nhóm

- Khóa: K4
- Lớp lab: D304
- Nhóm: HoiNguoiCaoTuoi
- Zone: Chờ xác nhận
- Nhóm trưởng: Sái Hoài Nam — `2A202601993`
- P2: Dương Ngọc Hải — `2A202601748`
- P3: Nguyễn Hoàng Đạt — `2A202601460`
- P4: Trần Duy Sơn — `2A202601792`
- P5: Phạm Hoàng Nam — `2A202601442`

## Bằng chứng của nhóm thuộc loại nào?

Chọn:

> B — Đã phân tích dữ liệu

Không chọn A. Nhóm chưa thực hiện khảo sát ít nhất 20 người ngoài nhóm và
không có log toàn bộ câu trả lời. Việc lựa chọn đề tài cho giảng viên đã
được labcode đồng ý, nhưng không được dùng thay thế điều kiện của evidence A.

## Con số bằng chứng mạnh nhất

> Nhóm phân tích 2.522 dòng message trong chatlog VLearn từ ngày 22/07 đến
> 29/07/2026 và xác định có 1.261 câu hỏi của 369 học viên, thuộc 585 hội
> thoại. Cách đếm: lọc các dòng có role=student và content không rỗng; số
> học viên và hội thoại được tính bằng số user_id và conversation_id khác
> nhau. Nhóm lưu 5 ví dụ nguyên văn đã ẩn danh cùng mã turn_id/message_id để
> người khác kiểm tra lại.

## Nhóm đã cân nhắc những ý tưởng nào? Vì sao chọn ý tưởng này?

> Nhóm cân nhắc ba hướng. Thứ nhất là nhận biết lỗ hổng kiến thức từ batch
> 1.261 câu hỏi của 369 học viên trong 8 ngày. Thứ hai là cải thiện
> grounding cho câu trả lời tutor vì 46,2% câu trả lời có trường citations
> rỗng. Thứ ba là giảm độ trễ vì latency trung vị là 1.758 ms, p90 là 3.686
> ms và tối đa 23.848 ms. Nhóm chọn hướng thứ nhất vì trực tiếp giúp giảng
> viên quyết định nội dung cần giảng lại, có dữ liệu và taxonomy sẵn, đồng
> thời khả thi để xây và kiểm chứng trong 10 giờ. Hai hướng còn lại cần can
> thiệp sâu vào trợ giảng hoặc phụ thuộc model và hạ tầng.

## Bốn kiểu tình huống khó của sản phẩm

> Nhóm xác định bốn lớp tình huống khó. (1) Nguồn sự thật: câu hỏi hỏi nội
> dung không có trong slide; model trả source reference không tồn tại. Hệ
> thống phải tránh bịa topic hoặc evidence. (2) Mơ hồ: câu “Phần này là
> sao?” thiếu ngữ cảnh; một câu hỏi đồng thời nói về hai topic. Các case này
> phải vào needs_review và hiển thị alternative. (3) Ngoài phạm vi: câu hỏi
> về deadline/chấm điểm; câu hỏi off-topic hoặc sự cố máy tính. Các case này
> không được làm tăng thống kê lỗ hổng kiến thức. (4) Đặc thù domain: nhầm
> RAG với fine-tuning; gom các câu có ý trái ngược vào cùng một summary. Hệ
> thống phải hiển thị evidence, giảm confidence hoặc giữ sự khác biệt trong
> summary.

## Nhóm áp dụng nguyên tắc thiết kế nào? Ở đâu?

> Nhóm áp dụng G1 — nói rõ phạm vi bằng session selector và chỉ matching
> với taxonomy của buổi học đã chọn. G2 — nói rõ độ tin cậy bằng các nhãn
> high, medium, low tại topic card và màn hình chi tiết, không hiển thị phần
> trăm chính xác giả. G10 — xử lý khi không chắc chắn bằng cách chuyển câu
> low-confidence vào review queue. G9 — giải thích kết quả bằng rationale và
> evidence trong detail drawer. G11 — cho phép người dùng sửa được thiết kế
> dưới dạng correction workflow; phần lưu correction hiện vẫn cần hoàn
> thiện trước bản demo cuối.

## Nhóm còn thiếu gì? Cần hỗ trợ gì?

> Nhóm còn cần hoàn thiện luồng frontend gửi batch câu hỏi thật thay vì gửi
> danh sách rỗng và dùng fixture, hoàn thiện thao tác lưu correction, và sửa
> failure GS009 khi một alias ngắn được xem là đủ evidence để trả
> high-confidence. Các artifact đánh giá hiện chưa thống nhất: Run-004 đạt
> 85% nhưng run-current là 75%, nên nhóm cần P5 chốt một canonical run và
> bổ sung các metric schema-valid, supported-question-ID validity và
> batch-survival khi timeout. Nhóm mong trợ giảng góp ý về tiêu chí
> grounding đủ mạnh để phân biệt “khớp từ khóa” với “được tài liệu hỗ trợ”.

## Bằng chứng khóa quality bar

- Commit: `18a80c9`
- Thời gian commit: 2026-07-30 23:47:53 +07:00
- Hạn cứng: 23:59 ngày 1
- Quality bar trong commit trên không được thay đổi sau deadline.

## Việc còn chờ xác nhận

- [ ] Zone của nhóm.
- [ ] P5 chọn canonical evaluation run.
- [ ] P1 đã gửi form và lưu xác nhận.
- [ ] P2 đã gửi form và lưu xác nhận.
- [ ] P3 đã gửi form và lưu xác nhận.
- [ ] P4 đã gửi form và lưu xác nhận.
- [ ] P5 đã gửi form và lưu xác nhận.

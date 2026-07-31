# Trợ lý Giảng viên AI — Nội dung demo 6 slide

Nhóm HoiNguoiCaoTuoi · K4 · D304

## Quy chuẩn trình bày

- Tỷ lệ: 16:9.
- Phong cách: nền sáng, màu đỏ VLearn làm màu nhấn, chữ đen/xám đậm.
- Mỗi slide chỉ truyền tải một thông điệp chính.
- Không đưa code hoặc đoạn văn dài lên slide.
- Mỗi slide phải có ít nhất một con số, kết quả đo hoặc bằng chứng kiểm tra được.
- Mục tiêu diễn tập: 4 phút 40 giây, chừa 20 giây cho chuyển slide.

---

## Slide 1 — User & Job

### Tiêu đề trên slide

**1.261 câu hỏi sau giờ học — giảng viên nên đọc từ đâu?**

### Nội dung hiển thị

Ba con số lớn:

```text
1.261 câu hỏi
369 học viên
8 ngày dữ liệu
```

Thông điệp:

> Sau mỗi buổi học, giảng viên phải đọc nhiều câu hỏi rời rạc, tự nhận biết
> câu nào cùng chủ đề và quyết định phần kiến thức cần giảng lại.

JTBD:

> Khi kết thúc một buổi học có nhiều câu hỏi, tôi muốn nhanh chóng nhận ra
> chủ đề nào khiến nhiều học viên gặp khó khăn để quyết định nội dung cần
> giải thích lại ở buổi tiếp theo.

Nguồn nhỏ ở chân slide:

```text
Nguồn: 2.522 message VLearn, 22/07–29/07/2026.
Cách đếm: role=student và content không rỗng.
```

### Gợi ý hình ảnh

- Bên trái: minh họa nhiều câu hỏi rời rạc.
- Bên phải: ba con số `1.261`, `369`, `8 ngày`.
- Không dùng ảnh stock giảng viên chung chung.

### Lời trình bày — P1, khoảng 35 giây

> Trong tám ngày dữ liệu VLearn, chúng tôi ghi nhận 1.261 câu hỏi từ 369
> học viên. Hiện tại giảng viên phải đọc từng câu, tự nhận ra những câu
> diễn đạt khác nhau nhưng cùng phản ánh một lỗ hổng kiến thức. Vì vậy,
> công việc chúng tôi muốn hỗ trợ không phải là tự động trả lời học viên,
> mà là giúp giảng viên nhanh chóng quyết định phần nào cần giảng lại.

---

## Slide 2 — Vì sao chọn bài toán này?

### Tiêu đề trên slide

**Chúng tôi đã loại hai hướng trước khi chọn**

### Nội dung hiển thị

| Hướng cân nhắc | Bằng chứng | Khả thi trong 10 giờ | Quyết định |
|---|---:|---|---|
| Nhận biết lỗ hổng kiến thức | 1.261 câu hỏi, 369 học viên | Cao | **Chọn** |
| Cải thiện grounding của tutor | 46,2% câu trả lời không có citation | Trung bình | Loại |
| Giảm độ trễ phản hồi | Median 1.758 ms, p90 3.686 ms | Thấp | Loại |

Thông điệp kết luận:

> Chọn bài toán giúp giảng viên ra quyết định vì có dữ liệu thật, taxonomy
> sẵn và có thể kiểm chứng bằng golden set.

### Gợi ý hình ảnh

- Bảng ba dòng.
- Dòng được chọn có nền đỏ nhạt hoặc viền đỏ.
- Hai dòng bị loại để màu xám; không xóa khỏi câu chuyện.

### Lời trình bày — P1, khoảng 30 giây

> Nhóm không đi thẳng vào ý tưởng đầu tiên. Chúng tôi cân nhắc cải thiện
> grounding và giảm latency, nhưng hai hướng này cần can thiệp sâu vào
> tutor hoặc phụ thuộc hạ tầng. Bài toán phân loại và tổng hợp câu hỏi có
> tác động trực tiếp đến quyết định của giảng viên, đồng thời có dữ liệu,
> taxonomy và cách đo phù hợp với phạm vi 10 giờ.

---

## Slide 3 — Giải pháp và demo live

### Tiêu đề trên slide

**Từ batch câu hỏi đến quyết định cần giảng lại**

### Nội dung hiển thị

Sơ đồ:

```text
Batch câu hỏi
      ↓
Matching với taxonomy của buổi học
      ↓
Gom câu cùng chủ đề + grounded summary
      ↓
┌──────────────┬──────────────┬──────────────┐
│ Auto-grouped │ Needs review │  Unmatched   │
└──────────────┴──────────────┴──────────────┘
```

Nguyên tắc automation:

> Case có căn cứ rõ được tự động gom. Case mơ hồ hoặc ngoài phạm vi được
> chuyển cho giảng viên duyệt.

### Kịch bản demo live

1. Chọn `DAY_01`, bấm **Phân tích**.
2. Case chuẩn: các câu hỏi về RAG/fine-tuning được gom vào topic phù hợp.
3. Mở topic card, chỉ ra:
   - số câu hỏi;
   - số học viên;
   - grounded summary;
   - confidence và evidence.
4. Case khó: “Phần này là sao ạ, em chưa hiểu lắm?” phải vào
   `needs_review`.
5. Chỉ nhanh case logistics “Bài tập hôm nay nộp ở đâu?” không được tính
   là lỗ hổng kiến thức.

### Lời trình bày

P2 — giao diện, khoảng 40 giây:

> Giảng viên chọn buổi học và bấm Phân tích. Dashboard trả về các topic,
> số câu hỏi và số học viên đang gặp khó khăn. Khi mở một topic, giảng viên
> xem được summary, độ tin cậy và evidence thay vì chỉ nhận một nhãn từ AI.

P3 — matching và case khó, khoảng 30 giây:

> Hệ thống chỉ matching trong taxonomy của session đã chọn. Câu có evidence
> rõ được tự động gom; câu như “Phần này là sao?” không đủ ngữ cảnh nên
> phải trả confidence thấp và chuyển vào review queue.

P4 — grouping và summary, khoảng 25 giây:

> Phần grouping và đếm số học viên được thực hiện theo dữ liệu đầu vào.
> Summary phải giữ supported question IDs để giảng viên có thể quay lại
> kiểm tra những câu hỏi đã tạo ra kết luận.

### Lưu ý trước demo

Frontend hiện gửi `questions: []` và backend tự nạp demo fixture. Khi demo
phải gọi đây là **demo batch**, không được nói rằng người dùng đã nhập batch
trực tiếp trên UI. Nếu P2 hoàn thiện input trước demo thì bỏ lưu ý này.

---

## Slide 4 — Kết quả đo

### Tiêu đề trên slide

**Đạt ngưỡng một lần, nhưng chất lượng chưa ổn định**

### Nội dung hiển thị

Biểu đồ bốn điểm:

```text
Target         80%
Run-001        65%
Run-002        80%
Run-004        85%
Run-current    75%
```

Hai con số nổi bật từ Run-001 → Run-002:

```text
Correct-or-abstain:       65% → 80%
High-confidence wrong:     5  → 2
```

Failure quan trọng:

> GS009: hệ thống khớp từ “tham số” và trả high-confidence dù yêu cầu tính
> GPU không được tài liệu hỗ trợ.

Kết luận:

> Nhóm chưa tuyên bố toàn bộ quality bar đã đạt. P5 cần chốt canonical run
> và bổ sung các metric còn thiếu.

### Gợi ý hình ảnh

- Một đường ngang màu đỏ tại target 80%.
- Bốn cột hoặc bốn điểm cho các run.
- Một ô cảnh báo nhỏ cho GS009.

### Lời trình bày — P5, khoảng 40 giây

> Quality bar được khóa ở mức 80% trước lần chạy đầu. Run-001 chỉ đạt 65%;
> sau tối ưu, Run-002 đạt đúng 80% và số lỗi high-confidence giảm từ năm
> xuống hai. Tuy nhiên các lần chạy sau dao động từ 75% đến 85%, nên chúng
> tôi không che giấu sự thiếu ổn định này. Failure nguy hiểm nhất là GS009:
> một từ khóa đúng nhưng chưa đủ căn cứ vẫn bị diễn giải thành kết quả
> high-confidence.

### Việc phải chốt trước khi xuất slide

P5 phải xác nhận canonical run. Nếu P5 chọn một run chính thức khác, cập
nhật con số trên slide nhưng vẫn giữ lịch sử Run-001 và failure GS009.

---

## Slide 5 — Validation với người dùng

### Tiêu đề trên slide

**Giảng viên có thực sự ra quyết định nhanh hơn không?**

### Trạng thái hiện tại

**CHƯA ĐỦ BẰNG CHỨNG ĐỂ FINAL SLIDE.**

Labcode đồng ý đề tài không thay thế validation với người dùng. Không tự
tạo hoặc diễn giải thành quote của giảng viên.

### Layout cần điền sau validation

Quote 1:

> “[Trích dẫn nguyên văn về điều hữu ích hoặc quyết định giảng lại]”
>
> — [Họ tên], [vai trò]

Quote 2:

> “[Trích dẫn nguyên văn về điểm chưa tin, khó hiểu hoặc cần sửa]”
>
> — [Họ tên], [vai trò]

Thay đổi từ feedback:

```text
Trước validation: [thiết kế/hành vi cũ]
Sau validation:   [thay đổi đã thực hiện]
Vì sao:           [quote hoặc quan sát làm căn cứ]
```

### Ba câu cần hỏi khi validation

1. Nhìn vào dashboard này, thầy/cô sẽ quyết định giảng lại nội dung nào?
2. Kết quả hoặc thông tin nào khiến thầy/cô chưa tin?
3. Với câu trong review queue, thầy/cô cần thêm gì để sửa quyết định của AI?

### Lời trình bày — P1, khoảng 35 giây

Chỉ viết lời trình bày sau khi có quote thật. Cấu trúc:

> Chúng tôi đưa prototype cho [số người/vai trò] sử dụng. Hai phản hồi đáng
> chú ý nhất là [quote ngắn 1] và [quote ngắn 2]. Từ phản hồi này, nhóm đã
> thay đổi [một thay đổi cụ thể]. Phần [vấn đề còn lại] được giữ trong
> backlog thay vì tuyên bố đã giải quyết.

---

## Slide 6 — Nếu có thêm một tuần

### Tiêu đề trên slide

**Ba việc tiếp theo — đều xuất phát từ failure đã quan sát**

### Nội dung hiển thị

1. **Đóng failure GS009**
   - Thêm grounding gate và regression test cho trường hợp khớp từ khóa
     nhưng thiếu căn cứ.

2. **Hoàn thiện human-in-the-loop**
   - Frontend gửi batch thật.
   - Giảng viên sửa taxonomy và lưu correction.

3. **Ổn định và đo đủ**
   - Chốt canonical run.
   - Đo schema validity, supported-ID validity và batch survival.
   - Validation trực tiếp với giảng viên.

Thông điệp kết:

> Giá trị của AI không nằm ở việc luôn đưa ra câu trả lời, mà ở việc giúp
> giảng viên ra quyết định nhanh hơn, có căn cứ hơn và biết rõ khi nào AI
> không chắc chắn.

### Gợi ý hình ảnh

- Ba cột hoặc ba bước đánh số.
- Câu kết đặt lớn ở cuối slide.
- Không thêm roadmap dài hoặc tính năng ngoài phạm vi.

### Lời trình bày — P1, khoảng 25 giây

> Nếu có thêm một tuần, chúng tôi không mở rộng thêm nhiều tính năng. Nhóm
> sẽ đóng failure grounding nguy hiểm nhất, hoàn thiện quyền sửa của giảng
> viên và làm cho kết quả evaluation ổn định, kiểm chứng được. Bài học lớn
> nhất của nhóm là một hệ thống AI hữu ích không chỉ cần biết trả lời mà còn
> phải biết khi nào nên dừng và trao quyền quyết định cho con người.

---

## Phân công nói và thời lượng

| Phần | Người nói | Thời lượng |
|---|---|---:|
| Slide 1 | P1 — Sái Hoài Nam | 35 giây |
| Slide 2 | P1 — Sái Hoài Nam | 30 giây |
| Slide 3, giao diện | P2 — Dương Ngọc Hải | 40 giây |
| Slide 3, matching | P3 — Nguyễn Hoàng Đạt | 30 giây |
| Slide 3, grouping/summary | P4 — Trần Duy Sơn | 25 giây |
| Slide 4 | P5 — Phạm Hoàng Nam | 40 giây |
| Slide 5 | P1 — Sái Hoài Nam | 35 giây |
| Slide 6 | P1 — Sái Hoài Nam | 25 giây |

Tổng lời nói dự kiến: 4 phút 20 giây. Phần chuyển slide và thao tác demo
được phép dùng tối đa 40 giây.

## Checklist trước khi xuất PDF

- [ ] P5 chốt canonical evaluation run.
- [ ] Slide 5 có ít nhất hai quote thật, tên và vai trò.
- [ ] Có ít nhất một thay đổi sản phẩm từ feedback.
- [ ] Demo thử case chuẩn và case khó.
- [ ] Chuẩn bị screenshot/video dự phòng.
- [ ] Mỗi thành viên nói ít nhất một phần.
- [ ] Xuất đúng 6 slide, không tính slide cảm ơn riêng.

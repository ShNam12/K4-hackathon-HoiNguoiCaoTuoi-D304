# Giai đoạn 4 — P1 đối chiếu quality bar và chọn failure

Ngày đánh giá: 2026-07-31  
Role thực hiện: P1 — Product Lead  
Golden set: `eval/golden_set.jsonl` (20 case)  
Kết quả gốc: `eval/results/run-001.json`  
Kết quả sau fix hiện có: `eval/results/run-002.json`

## 1. Nguyên tắc đánh giá

- Giữ nguyên quality bar đã khóa trong `spec.md` trước Run-001.
- Dùng nguyên kết quả Run-001, kể cả các case fail.
- Chọn đúng một failure có hậu quả lớn nhất để chuyển cho role sở hữu module.
- Không coi test đơn vị là số đo thay thế cho metric còn thiếu trong Run-001.

## 2. Đối chiếu Run-001 với quality bar đã khóa

| Quality bar | Bằng chứng trong Run-001 | Kết luận |
|---|---|---|
| Ít nhất 80% case đúng taxonomy hoặc abstain đúng | `13/20 = 65%` | **Không đạt** |
| 100% output hợp lệ theo schema `1.0` | Run-001 không ghi `schema_valid_rate` và chỉ lưu output rút gọn của classifier | **Chưa đủ bằng chứng để kết luận** |
| Không có case ngoài phạm vi bị gán sai với confidence `high` | Hai case `out_of_scope`: `GS013` bị auto-group với `medium`; `GS014` abstain đúng với `low`. Không case nào thuộc lớp này bị gán sai với `high` | **Đạt đúng điều kiện đã khóa**, nhưng `GS013` vẫn sai trạng thái |
| 100% summary có support ID hợp lệ và thuộc đúng group | Evaluator chỉ gọi `classify_batch`, không chạy group/summary và không ghi `summary_support_id_validity` | **Chưa đủ bằng chứng để kết luận** |
| Một timeout/parse lỗi không làm crash toàn batch | Golden run không inject timeout/parse lỗi và không ghi `timeout_error_count` | **Chưa đủ bằng chứng để kết luận** |

Thông tin bổ sung của Run-001:

- `status_correct_rate = 14/20 = 70%`.
- `high_confidence_wrong_count = 5`: `GS001`, `GS009`, `GS012`, `GS015`,
  `GS018`.
- Vì còn ba quality gate chưa được evaluator đo, không được công bố rằng Run-001
  đã đạt toàn bộ quality bar.

## 3. Failure duy nhất P1 chọn

**Failure được chọn: `GS009`.**

| Thuộc tính | Giá trị |
|---|---|
| Risk class | `grounding` |
| Input | “Có tài liệu nào nói về cách tính lượng GPU cần cho một mô hình 1000 tỷ tham số không?” |
| Expected | `topic_id = null`, `status = needs_review` |
| Actual Run-001 | `topic_id = DAY_01_CH_15`, `status = auto_grouped`, `confidence = high` |
| Matched evidence | Chỉ có cụm `tham so` |

Lý do chọn: câu hỏi yêu cầu một phép tính/hướng dẫn không có trong tài liệu của
session nhưng hệ thống thể hiện như đã tìm được topic với độ tin cậy cao. Giảng
viên có thể hiểu nhầm đây là nội dung được tài liệu hỗ trợ và ra quyết định giảng
lại dựa trên một kết quả không có căn cứ. Hậu quả này lớn hơn lỗi gán sai giữa hai
topic gần nhau vì người dùng khó tự phát hiện thiếu nguồn.

### Giả thuyết nguyên nhân

Trong matcher, một alias khớp chính xác được ưu tiên và trả về ngay với confidence
`high`. Với `GS009`, cụm `tham so` khớp alias của `DAY_01_CH_15`; nhánh này không
kiểm tra xem yêu cầu cụ thể về cách tính lượng GPU cho mô hình 1.000 tỷ tham số có
được `summary` hoặc `source_refs` của chapter hỗ trợ hay không. Vì vậy một tín hiệu
lexical đúng nhưng không đủ đã bị diễn giải thành bằng chứng grounding đầy đủ.

### Handoff theo ownership

- Owner cần xử lý: **P3**, vì failure nằm ở retrieve/classify.
- Regression bắt buộc phải dùng đúng nội dung `GS009` và chứng minh kết quả là
  `needs_review` với confidence `low`.
- Không được sửa golden case hoặc hạ quality bar để làm kết quả đạt.

P1 chỉ ghi nhận quyết định và giả thuyết; không sửa file matcher/test thuộc P3.

## 4. Kiểm tra Run-002 hiện có

Run-002 đạt `16/20 = 80%` correct-or-abstain và giảm high-confidence wrong từ 5
xuống 2. Tuy nhiên `GS009` vẫn trả `DAY_01_CH_15`, `auto_grouped`, confidence
`high`, nên failure P1 đã chọn **chưa được sửa**.

Regression stop-word hiện có giải quyết một nhóm lỗi khác; nó không phải regression
cho `GS009` và không thể dùng để đóng failure đã chọn.

## 5. Trạng thái exit criteria Giai đoạn 4

| Exit criterion | Trạng thái | Bằng chứng/việc còn thiếu |
|---|---|---|
| Có Run-001 đầy đủ | **Chưa đạt** | Có `run-001.json`, thiếu `run-001.md` và ba metric bắt buộc |
| Có một failure được phân tích | **Đạt — phần P1** | Chỉ chọn `GS009`; giả thuyết ghi tại đây và `spec.md` changelog |
| Có regression test | **Chưa đạt** | Chưa có regression đúng case `GS009` |
| Có Run-002 đầy đủ | **Chưa đạt** | Có `run-002.json`, thiếu `run-002.md` và ba metric bắt buộc |
| Không thay đổi quality bar | **Đạt** | Các ngưỡng trong `spec.md` được giữ nguyên |

Kết luận: đầu việc riêng của P1 trong Giai đoạn 4 đã hoàn thành. Toàn Giai đoạn 4
chưa đạt exit criteria cho đến khi P3 sửa và thêm regression cho `GS009`, sau đó
P5 chạy lại và xuất đủ artifact/metric theo plan.

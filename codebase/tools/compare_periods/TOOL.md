---
name: compare_periods
track: core
kind: read
requires_env: []
inputs: [period_a, period_b, metric, topic_id]
outputs: [topic_id, metric, period_a, period_b, delta, pct_change]
side_effect: false
---
# compare_periods

So sánh các chỉ số giữa hai giai đoạn thời gian, áp dụng cho toàn bộ các chủ đề hoặc lọc theo một chủ đề cụ thể (`topic_id`).
Trả về tổng số liệu của từng giai đoạn và mức độ thay đổi (delta) cũng như tỷ lệ phần trăm thay đổi.

Các metric được hỗ trợ bao gồm: `count` (số lượng câu hỏi), `tutor_bo_tay_rate` (tỷ lệ tutor không trả lời được), `down_ratings` (số lượt đánh giá thấp).
Nếu một giai đoạn không có dữ liệu, kết quả vẫn sẽ trả về 0 một cách rõ ràng.

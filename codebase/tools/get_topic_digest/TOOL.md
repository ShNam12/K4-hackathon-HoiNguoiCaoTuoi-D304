---
name: get_topic_digest
track: core
kind: read
requires_env: []
inputs: [date, top_n]
outputs: [meta, topics]
side_effect: false
---
# get_topic_digest

Gộp `turns_topics.jsonl` theo chương cho một ngày cụ thể, xếp hạng top-N theo số câu hỏi
(tie-break theo `tutor_bo_tay_rate`). Trả `meta` (thống kê ngày: tổng turn, số đã gán chủ đề,
số loại, số không xác định) và `topics` (danh sách chương kèm ví dụ câu hỏi đã cắt ngắn).

Deterministic, không gọi AI — tái dùng thẳng `daily_digest.aggregate()`.

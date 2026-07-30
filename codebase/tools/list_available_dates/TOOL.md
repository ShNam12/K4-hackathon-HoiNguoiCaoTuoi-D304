---
name: list_available_dates
track: core
kind: read
requires_env: []
inputs: []
outputs: [dates]
side_effect: false
---
# list_available_dates

Liệt kê các ngày (YYYY-MM-DD) đã có dữ liệu trong `turns_topics.jsonl`, kèm tổng số turn mỗi
ngày. Agent gọi tool này trước khi trả lời về một ngày cụ thể để tránh bịa ra ngày không có
dữ liệu (chỗ khó ① nguồn sự thật).

Deterministic, không gọi AI.

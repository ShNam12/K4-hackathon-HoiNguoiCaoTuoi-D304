---
name: get_topic_examples
track: core
kind: read
requires_env: []
inputs: [chapter_id, date, limit]
outputs: [chapter_id, chapter_title, count, examples]
side_effect: false
---
# get_topic_examples

Lấy thêm câu hỏi ví dụ (đã cắt ngắn tối đa 160 ký tự, không dán nguyên văn dài — quy định
bảo mật data pack) của MỘT chương cụ thể, dùng khi giảng viên muốn đào sâu sau khi đã thấy
`get_topic_digest`. `chapter_id` phải lấy từ kết quả `get_topic_digest` trước đó — tool
KHÔNG tự đoán chương nếu `chapter_id` không khớp bất kỳ chương nào trong cây tri thức.

Deterministic, không gọi AI.

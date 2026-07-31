---
name: search_by_keyword
track: core
kind: read
requires_env: []
inputs: [keyword, time_range, limit]
outputs: [keyword, count, results]
side_effect: false
---
# search_by_keyword

Tìm kiếm văn bản tự do trên tất cả câu hỏi của học viên và tên chủ đề bài giảng (chapter_title). 
Hỗ trợ tìm kiếm tiếng Việt không phân biệt hoa thường và không phân biệt dấu (diacritic-tolerant).
Dùng khi: giảng viên muốn tìm kiếm các câu hỏi liên quan đến một từ khóa cụ thể hoặc kiểm tra xem một thuật ngữ nào đó có được sinh viên hỏi hay không.
Trả về danh sách các câu hỏi khớp từ khóa, bao gồm `chapter_id`, `chapter_title`, `date`, và `cau_hoi_goc` (văn bản gốc của sinh viên).
Nếu không có kết quả, trả về mảng `results` rỗng.

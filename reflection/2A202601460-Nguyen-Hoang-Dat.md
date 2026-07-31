# Reflection — Nguyễn Hoàng Đạt (2A202601460) — P3, Taxonomy retrieval và AI matching

## 1. Vai trò và phần tôi phụ trách

Theo phân công trong `PLAN_10_GIO.md` §0.1 và §4, tôi là **P3 — Taxonomy retrieval và AI matching**,
sở hữu:

- `backend/services/taxonomy_loader.py` — nạp taxonomy của đúng buổi học, chỉ trả các chapter
  `is_canonical = true`, phát hiện `chapter_id` trùng lặp, không mutate dữ liệu gốc.
- `backend/services/taxonomy_matcher.py` — pipeline 3 bước: normalize câu hỏi → retrieve top-3–5
  candidate bằng alias/keyword → LLM rerank hoặc abstain (`needs_review`/`unmatched`) khi tín hiệu
  không đủ mạnh.
- `backend/prompts/taxonomy_matcher.md` — prompt strict-JSON cho bước rerank, chỉ cho phép chọn
  `topic_id` nằm trong candidate đã đưa, không tự bịa nguồn.
- `backend/tests/test_taxonomy_loader.py`, `backend/tests/test_taxonomy_matcher.py` — test riêng,
  chạy độc lập với mock LLM.
- Ở giai đoạn 4 (hardening), tôi cũng chạm vào `eval/evaluate.py` và `eval/results/run-001.json`,
  `run-002.json` khi đi sửa case fail phát hiện qua golden set (xem mục 4).

## 2. AI hỗ trợ tôi như thế nào

- Dùng AI (Claude Code) để scaffold nhanh cấu trúc 3 tầng của matcher (normalize → retrieve →
  LLM rerank/abstain) đúng theo contract đã chốt ở `PLAN_10_GIO.md` §3–§4, thay vì tự gõ hết từ đầu
  — tiết kiệm thời gian ở giai đoạn 1 để dồn sang viết test và chạy thử với AI call thật.
- Dùng AI để sinh bộ test unit ban đầu bám theo 11 case bắt buộc trong `PLAN_10_GIO.md` §5
  (paraphrase vào top-k, câu mơ hồ → `needs_review`, off-topic → `unmatched`, LLM trả JSON sai
  không được crash, `topic_id` ngoài candidate bị reject...).
- Khi golden set chạy ra case sai (xem mục 4), tôi dùng AI để đọc lại diff giữa kỳ vọng và output
  thật, khoanh vùng đúng dòng logic gây lỗi trong `_score_chapter`, thay vì đoán mò sửa toàn bộ file.
- Tôi luôn tự đọc lại từng đoạn AI sinh ra trước khi commit — đặc biệt phần rule "không trả
  `topic_id` ngoài candidate", vì đây là chỗ dễ bị AI viết sai logic validate mà không báo lỗi rõ.

## 3. Một bài học từ case fail của chính nhóm

**Case fail:** golden set (`eval/golden_set.jsonl`) phát hiện matcher gán nhầm một số câu hỏi ngắn/mơ
hồ vào sai chapter với confidence không hợp lý. Nguyên nhân nằm ở `_score_chapter()` trong
`taxonomy_matcher.py`: khi không có `matched_terms` rõ ràng, hàm fallback sang so khớp overlap giữa
token của câu hỏi và token của tiêu đề/keyword chapter. Fallback này **không loại các hư từ tiếng Việt
phổ biến** (`la`, `gi`, `nhu`, `the`, `nao`, `co`, `khong`, `va`, `cua`...) sau khi bỏ dấu — nên hai câu
hoàn toàn không liên quan nhưng cùng chứa các từ này vẫn bị tính là "matched_terms", tạo tín hiệu khớp
giả. Ngoài ra, thứ tự kiểm tra `_is_vague()` bị đặt sau nhánh `if not candidates: return unmatched`,
khiến câu hỏi mơ hồ nhưng vẫn có candidate (do lỗi trên) không bao giờ rơi vào `needs_review` như đúng
thiết kế.

**Cách sửa** (commit `8d559ca`):
1. Thêm tập `STOP_WORDS` và trừ khỏi cả `question_tokens`, `title_tokens`, `keyword_tokens` trước khi
   tính overlap trong `_score_chapter()`.
2. Đưa nhánh `exact_alias` và `_is_vague()` lên **trước** nhánh `if not candidates`, để câu mơ hồ luôn
   được xử lý đúng bất kể candidate có tồn tại hay không.
3. Chạy lại `eval/evaluate.py`, lưu `run-001.json` (trước sửa) và `run-002.json` (sau sửa) — không xoá
   run fail, giữ nguyên để đối chiếu.

**Bài học:** một heuristic fallback tưởng "vô hại" (so khớp token thô) có thể tạo ra false positive khó
thấy nếu không loại hư từ ngôn ngữ — và thứ tự các nhánh điều kiện early-return quan trọng ngang với
logic bên trong từng nhánh. Golden set với case "mơ hồ"/"hiếm-noisy" (theo `PLAN_10_GIO.md` §8.5) chính
là thứ bắt được lỗi này; nếu chỉ test bằng câu hỏi "đẹp" rõ topic thì sẽ không bao giờ lộ ra.

## 4. Nếu có thêm một tuần

- Thay heuristic overlap-token fallback bằng retrieval có trọng số theo tần suất từ (giảm phụ thuộc
  vào danh sách stop-word thủ công, tránh phải liệt kê thêm hư từ mới khi gặp case lạ).
- Thêm test riêng cho đúng bug này (`test_taxonomy_matcher.py`) để tránh regression nếu ai đó sửa lại
  `_score_chapter()` sau này.

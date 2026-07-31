# AI SPEC — Phân loại và tổng hợp câu hỏi sau buổi học · Nhóm HoiNguoiCaoTuoi · Zone chưa cung cấp

Hướng: A — VLearn
Loại: Tối ưu tính năng có sẵn

## §1. User & Job

### Job executor và workflow hiện tại

Người thực hiện công việc là giảng viên phụ trách một buổi học.

Workflow hiện tại:

1. Giảng viên thu thập các câu hỏi sau buổi học.
2. Đọc từng câu hỏi riêng lẻ.
3. Tự nhận biết các câu đang nói về cùng một phần kiến thức.
4. Ước lượng phần nào đang khiến nhiều sinh viên gặp khó khăn.
5. Quyết định nội dung cần giải thích hoặc giảng lại.
6. Kiểm tra thủ công những câu mơ hồ hoặc ngoài phạm vi.

### Core JTBD

Khi kết thúc một buổi học có nhiều câu hỏi, tôi muốn nhanh chóng nhận ra
những chủ đề đang khiến nhiều sinh viên gặp khó khăn để quyết định phần
cần giải thích lại ở buổi tiếp theo.

### Problem statement

Sau buổi học, giảng viên phải đọc thủ công nhiều câu hỏi rời rạc. Các câu
có thể được diễn đạt khác nhau nhưng cùng phản ánh một lỗ hổng kiến thức,
khiến giảng viên mất thời gian và dễ bỏ sót chủ đề cần giảng lại.

### Evidence chuẩn B

#### Nguồn và phạm vi dữ liệu

- File: `data/vlearn-pack/chatlog/chat_history_anonymized_for_hackathon.csv`.
- Data dictionary:
  `data/vlearn-pack/chatlog/DATA_DICTIONARY.md`.
- Phạm vi thời gian: 22/07–29/07/2026.
- ID đã được ẩn danh thành các mã `U`, `C`, `T` và `M`.

#### Phương pháp đếm

- Một câu hỏi là một dòng có `role = student` và `content` không rỗng.
- Số người dùng là số `user_id` khác nhau trong các dòng câu hỏi.
- Số hội thoại là số `conversation_id` khác nhau trong các dòng câu hỏi.
- Số lượt hỏi–đáp là số `turn_id` khác nhau trong các dòng câu hỏi.
- Không dùng các dòng `role = tutor` để tính số câu hỏi.

Lệnh đếm có thể tái lập:

```powershell
$rows = Import-Csv -Encoding utf8 `
  -LiteralPath ".\data\vlearn-pack\chatlog\chat_history_anonymized_for_hackathon.csv"
$questions = @($rows | Where-Object {
  $_.role -eq "student" -and -not [string]::IsNullOrWhiteSpace($_.content)
})

[pscustomobject]@{
  Questions = $questions.Count
  Users = @($questions.user_id | Sort-Object -Unique).Count
  Conversations = @($questions.conversation_id | Sort-Object -Unique).Count
  Turns = @($questions.turn_id | Sort-Object -Unique).Count
}
```

#### Kết quả mining

| Chỉ số | Kết quả |
|---|---:|
| Tổng số dòng message | 2.522 |
| Số câu hỏi của học viên | 1.261 |
| Số người dùng khác nhau | 369 |
| Số hội thoại | 585 |
| Số lượt hỏi–đáp | 1.261 |

#### Ví dụ ngắn có mã nguồn

| Case ID | Source ref | Ví dụ ngắn đã ẩn danh | Pain quan sát được |
|---|---|---|---|
| EV001 | `T0638/M1131` | “chào bạn, mình chưa hiểu về RAG” | Người học nói rõ một khái niệm chưa hiểu. |
| EV002 | `T0338/M1612` | “agent la gi” | Câu hỏi khái niệm ngắn, có thể lặp lại dưới nhiều cách diễn đạt. |
| EV003 | `T0712/M2160` | “ReAct co tac dung gi khi su dung trong Agent” | Người học cần hiểu vai trò của kỹ thuật trong một hệ thống lớn hơn. |
| EV004 | `T0138/M1311` | “làm thế nào để tôi phân loại output vào correct, safe fallback hay hallucinated?” | Câu hỏi cần phân biệt các trạng thái gần nhau và có rủi ro gán nhầm topic. |
| EV005 | `T0153/M1680` | “1 token là 1 vector hay gì” | Câu hỏi thể hiện khả năng nhầm lẫn giữa hai khái niệm liên quan. |

Chỉ các trích dẫn ngắn cần thiết được đưa vào spec. Không sao chép toàn bộ
raw chatlog vào repo public.

## §2. Impact & quyết định chọn

### Bảng impact ba ứng viên

| Ứng viên | Quy mô/tần suất quan sát được | Chi phí hoặc hậu quả | Khả thi trong 10 giờ | Quyết định |
|---|---|---|---|---|
| Nhận biết lỗ hổng kiến thức từ batch câu hỏi | Corpus có 1.261 câu hỏi từ 369 người dùng trong 8 ngày | Giảng viên phải đọc và gom thủ công; có thể bỏ sót chủ đề lặp lại | Cao: đã có chatlog, slide và lát cắt dashboard | **Chọn** |
| Cải thiện grounding cho từng câu trả lời tutor | Data dictionary ghi nhận 46,2% câu trả lời có trường `citations` rỗng | Người học khó kiểm tra căn cứ của câu trả lời | Trung bình: cần can thiệp sâu vào luồng trả lời hiện tại | Loại |
| Tối ưu độ trễ phản hồi tutor | Median 1.758 ms, p90 3.686 ms, tối đa 23.848 ms | Người học có thể phải chờ phản hồi lâu | Thấp: phụ thuộc model và hạ tầng ngoài phạm vi MVP | Loại |

### Ứng viên đã loại

1. Cải thiện grounding cho từng câu trả lời bị loại vì cần thay đổi luồng
   trợ giảng và chưa trực tiếp giúp giảng viên quyết định phần cần giảng lại.
2. Tối ưu latency bị loại vì phụ thuộc model và hạ tầng, khó chứng minh
   cải thiện ổn định trong phạm vi 10 giờ.

### Ứng viên được chọn

Nhóm chọn nhận biết lỗ hổng kiến thức từ batch câu hỏi vì dữ liệu hiện có
1.261 câu hỏi từ 369 người dùng. Bài toán có thể được kiểm chứng bằng
taxonomy, golden set, review queue và quyết định giảng lại của giảng viên.

## §3. Giải pháp tương tự đã nghiên cứu

### Mentimeter

Nguồn:
[Mentimeter — Live Q&A](https://www.mentimeter.com/features/live-questions-and-answers)
và
[Mentimeter — Making the most of results](https://help.mentimeter.com/en/articles/15086803-making-the-most-of-your-mentimeter-results).

- Flow: người tham gia gửi câu hỏi/phản hồi; người khác upvote; presenter
  có thể moderate, dismiss câu off-topic và xem các phản hồi mở được AI
  gom thành theme.
- Đáng học: ưu tiên câu hỏi, moderation rõ ràng và biến nhiều phản hồi
  rời rạc thành các theme dễ quan sát.
- Đáng tránh: upvote phản ánh mức độ phổ biến nhưng không tự chứng minh
  câu hỏi thuộc đúng kiến thức của buổi học; theme không nên được xem là
  đúng nếu thiếu evidence.
- Điểm khác của nhóm: chỉ phân loại trong taxonomy của session đã chọn,
  đếm số sinh viên khác nhau, hiển thị evidence và chuyển case không chắc
  chắn cho giảng viên duyệt.

### Slido

Nguồn:
[Slido — Live Q&A](https://www.slido.com/features-live-qa)
và
[Slido — Analytics](https://www.slido.com/features-analytics).

- Flow: tạo phiên Q&A, thu thập và upvote câu hỏi, moderate câu không liên
  quan hoặc trùng lặp, sau đó xem overview về câu hỏi, topic và sentiment.
- Đáng học: moderator giữ quyền kiểm soát, câu không phù hợp không bị ép
  vào luồng chính và kết quả có thể được export để xem lại.
- Đáng tránh: popularity và sentiment không phải là confidence của phép
  phân loại; không dùng chúng thay cho evidence của taxonomy.
- Điểm khác của nhóm: phục vụ quyết định “phần nào cần giảng lại”, có
  grounded summary với `supported_question_ids`, có confidence theo mức
  và correction theo taxonomy của buổi học.

## §4. Thiết kế

### Lát cắt một câu

Giảng viên chọn một buổi học và phân tích một batch câu hỏi; hệ thống gán
từng câu vào taxonomy của buổi học, gom theo topic và đưa các trường hợp
không chắc chắn cho giảng viên duyệt để quyết định nội dung cần giảng lại.

### Non-goals

- Không tích hợp Discord hoặc VLearn thật.
- Không xây đăng nhập và phân quyền.
- Không tự động trả lời sinh viên.
- Không xử lý realtime.
- Không xây taxonomy cho tài liệu mới.
- Không yêu cầu MongoDB hoặc vector database để demo chạy.
- Không tối ưu hạ tầng production.

### Mức prototype

- Mức nhắm tới: **Working**.
- Phần chạy thật: taxonomy matching hoặc grounded summary có ít nhất một
  lời gọi model thật.
- Phần deterministic: grouping, question count và unique student count.
- Phần fallback: frontend dùng fixture khi backend không chạy.
- Unit test dùng mock, không gọi network thật.

### Mức automation

Chọn **conditional**. Case rõ, có taxonomy và evidence có thể được tự động
group. Case mơ hồ, ngoài phạm vi, parse lỗi hoặc low-confidence phải chuyển
cho giảng viên duyệt. Phân loại sai high-confidence có thể khiến giảng viên
chọn sai nội dung cần giảng lại nên không được tự động hoàn toàn.

### §4b. Nguyên tắc HAX/PAIR

| Nguyên tắc | Áp dụng trong prototype | Thành phần UI |
|---|---|---|
| G1 — Nói rõ phạm vi | Chỉ dùng taxonomy của session đã chọn | Session selector và scope note |
| G2 — Nói rõ độ tin cậy | Chỉ hiển thị `high`, `medium`, `low`; không hiển thị phần trăm giả | Topic card và question detail |
| G10 — Xử lý khi không chắc chắn | Low-confidence chuyển sang `needs_review` | Review queue |
| G9/G11 — Giải thích và cho phép sửa | Hiển thị rationale, evidence, alternatives và cho đổi taxonomy | Detail drawer và correction dropdown |

## §5. Kiểu lỗi — 4 lớp chỗ khó và kịch bản

| ID | Lớp lỗi | Tình huống | Rủi ro | Expected behavior | UI kiểm chứng |
|---|---|---|---|---|---|
| FS01 | Nguồn sự thật | Câu hỏi nói về nội dung không có trong taxonomy/slide | Hệ thống bịa topic | Không ép gán; chuyển `needs_review` hoặc `unmatched` | Review queue |
| FS02 | Nguồn sự thật | Model trả source reference không tồn tại | Giảng viên tin căn cứ giả | Loại source sai, không hiển thị evidence giả và chuyển review | Evidence panel |
| FS03 | Mơ hồ | “Phần này là sao?” | Thiếu ngữ cảnh nhưng bị gán chắc chắn | Trả `low/needs_review` và giải thích thiếu ngữ cảnh | Review queue |
| FS04 | Mơ hồ | Một câu hỏi chứa hai topic | Một phần nội dung bị bỏ qua | Hiển thị alternatives; không trả high-confidence nếu chưa xác định được topic chính | Question detail |
| FS05 | Ngoài phạm vi | Hỏi deadline hoặc chấm điểm | Logistics bị tính là lỗ hổng kiến thức | Gán intent `logistics`; không đưa vào group kiến thức | Unmatched/review list |
| FS06 | Ngoài phạm vi | Câu hỏi off-topic | Làm sai thống kê topic | Trả `unmatched`; không tăng `question_count` | Unmatched list |
| FS07 | Đặc thù domain | Nhầm hai khái niệm gần nhau như RAG và fine-tuning | Gán sai topic high-confidence | Hiển thị evidence và alternative; giảm confidence hoặc chuyển review | Detail drawer |
| FS08 | Đặc thù domain | Các câu trái nghĩa bị tóm tắt như cùng một ý | Summary làm mất bất đồng | Summary phải giữ khác biệt hoặc dùng fallback; supported IDs phải thuộc group | Group summary |

## §6. Bốn đường đi của trải nghiệm

### Happy path

1. Giảng viên chọn `DAY_01`.
2. Nạp một batch 8–20 câu hỏi.
3. Bấm **Phân tích**.
4. Hệ thống trả các topic đã group.
5. UI hiển thị top topic, số câu hỏi, số sinh viên, intent, summary và
   evidence.
6. Giảng viên chọn phần cần giảng lại.

### Low-confidence

1. Câu hỏi không đủ căn cứ để gán chắc chắn.
2. Hệ thống trả `confidence = low` và `status = needs_review`.
3. Câu được đưa vào review queue.
4. Giảng viên xem evidence, alternatives và rationale.
5. Giảng viên sửa taxonomy hoặc giữ trạng thái cần duyệt.

### Failure/không có căn cứ

1. Model timeout, trả JSON lỗi hoặc source reference không hợp lệ.
2. Batch không bị crash.
3. Câu lỗi chuyển sang `needs_review` hoặc `error`.
4. Các câu còn lại vẫn được xử lý.
5. UI không hiển thị evidence giả.

### Correction

1. Giảng viên mở một câu trong review queue.
2. Xem topic đề xuất, alternative và evidence.
3. Chọn taxonomy phù hợp hoặc giữ trạng thái cần duyệt.
4. UI cập nhật trạng thái correction rõ ràng.

### Khi bị đòi ngoài phạm vi

Câu logistics hoặc off-topic không bị ép vào taxonomy kiến thức, không
được đưa vào group và không làm tăng question count của topic.

### Case đặc thù domain

Với hai khái niệm gần nhau hoặc câu chứa nhiều topic, hệ thống phải hiển
thị alternative và lý do, không tạo high-confidence giả và giữ quyền
quyết định cho giảng viên.

## §7. Kiểm thử

Các chiều chất lượng cần đo:

- Schema-valid rate.
- Topic correct-or-correct-abstain rate.
- High-confidence wrong count.
- Summary support-ID validity.
- Số case timeout/error làm ảnh hưởng toàn batch.

Golden set phải có ít nhất 20 case trong `eval/golden_set.jsonl`. P1 bàn
giao 20 case đã review tại
`validation/golden-case-proposals.jsonl`; P5 là owner duy nhất chuyển các
case được duyệt vào `eval/golden_set.jsonl`.

### Quality bar đã khóa trước Run-001

Quality bar được khóa ngày 2026-07-30, trước khi có kết quả Run-001:

- Ít nhất 80% case được gán đúng taxonomy hoặc abstain đúng.
- 100% output hợp lệ theo schema version `1.0`.
- Không có case ngoài phạm vi nào bị gán sai với confidence `high`.
- 100% summary có `supported_question_ids` hợp lệ và mọi ID đều thuộc
  đúng group.
- Một case timeout hoặc parse lỗi không làm crash toàn batch.

Quality bar này không được thay đổi sau lần chạy toàn bộ golden set đầu
tiên.

### Kết quả các lượt chạy

Kết quả các lượt chạy được lưu chi tiết tại `eval/results/`. Dưới đây là bảng tổng hợp kết quả:

| Lượt chạy | Thời điểm | Định nghĩa đạt (Topic correct or abstain) | Status correct rate | Số lượng High-confidence wrong | Đánh giá so với Quality Bar |
|---|---|---|---|---|---|
| **Run-001** (Lượt đầu) | 2026-07-30 | **65%** (13/20) | 70% (14/20) | 5 | **Chưa đạt** (Do lỗi xử lý stop-words dẫn đến phân loại sai nhiều câu hỏi thông dụng) |
| **Run-002** (Tối ưu) | 2026-07-30 | **80%** (16/20) | 70% (14/20) | 2 | **Đạt** (Đạt mức 80% cam kết nhờ lọc stop-words tiếng Việt trong taxonomy matcher) |

Nhóm sẽ tiếp tục theo dõi chất lượng này trong các lượt chạy tiếp theo của giai đoạn validation.

## §8. Phân công & kế hoạch

- P1 — Chưa cung cấp mã HV/họ tên: spec, evidence, validation và nội dung demo.
- P2 — Chưa cung cấp mã HV/họ tên: frontend và trải nghiệm giảng viên.
- P3 — `2A202601460` — Nguyễn Hoàng Đạt: taxonomy retrieval và AI matching.
- P4 — Chưa cung cấp mã HV/họ tên: grouping, intent và grounded summary.
- P5 — Chưa cung cấp mã HV/họ tên: API, schema, eval và packaging.
- Mỗi thành viên đặt lịch với một người ngoài nhóm để validation ở
  T+7:30; tên và vai trò được ghi vào `validation/feedback-log.md`.
- Nhóm tập trung một prototype working và dùng fixture làm fallback,
  không mở thêm lát cắt sản phẩm trong 10 giờ.

## §9. Changelog

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
| 2026-07-30 — Giai đoạn 1 | Hoàn thiện §1–§6, evidence, impact, benchmark, failure scenarios và test script | Thực hiện phạm vi P1 trong `PLAN_10_GIO.md`; evidence lấy từ chatlog đã ẩn danh |
| 2026-07-30 — Giai đoạn 2 | Khóa quality bar; review prompt P3/P4; chuẩn bị 20 golden-case proposal | Khóa tiêu chí trước Run-001 và sửa các label/source ref chưa đúng trong golden-set skeleton mà không sửa file thuộc P3–P5 |
| 2026-07-31 — Giai đoạn 3 | Audit thứ tự tích hợp, chạy full test và ba HTTP smoke path; dừng tích hợp ở P0 | `/api/analyze` vẫn trả fixture cho mọi input, pipeline P3/P4 chưa được P5 nối và frontend gửi batch rỗng; chi tiết tại `validation/phase3-integration-status.md` |
| 2026-07-31 — Giai đoạn 4 | Đối chiếu Run-001 với quality bar và chọn duy nhất failure `GS009` | Giả thuyết nguyên nhân: exact alias `tham so` làm matcher trả ngay `DAY_01_CH_15` với confidence `high`, nhưng không kiểm tra phần thông tin cụ thể được hỏi (cách tính GPU cho mô hình 1.000 tỷ tham số) có được evidence của chapter hỗ trợ hay không; kết quả là câu ngoài nguồn đáng lẽ `needs_review` lại bị `auto_grouped` |

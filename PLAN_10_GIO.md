# KẾ HOẠCH THỰC THI 10 GIỜ — AI HỖ TRỢ GIẢNG VIÊN PHÂN LOẠI VÀ TỔNG HỢP CÂU HỎI

> Phiên bản: 1.0  
> Phạm vi: từ sau CP2 đến khi sẵn sàng CP5/CP6  
> Quy mô nhóm: 5 người  
> Nguyên tắc điều hành: **khóa phạm vi, contract-first, mỗi file có đúng một người sở hữu, test độc lập trước khi tích hợp**

---

## 0. Cách sử dụng tài liệu này

1. Leader thay `P1–P5` bằng tên thật của từng thành viên ngay khi bắt đầu.
2. Cả nhóm đọc hết các mục `1`, `3`, `4`, `5` và `8` trong 30 phút đầu.
3. Mỗi người chỉ cần đọc kỹ thêm mục riêng của mình trong `§6`.
4. Không thêm tính năng mới sau mốc **T+5 giờ**.
5. Nếu tiến độ thực tế lệch quá 30 phút, leader cắt theo thứ tự trong `§10`, không kéo dài mọi đầu việc.

### 0.1 Bảng thay tên thành viên

| Mã | Tên thành viên | Vai trò chính | Vai trò khi demo |
|---|---|---|---|
| P1 | `[Tên leader]` | Product Lead, spec, evidence, điều phối tích hợp | Mở bài, pain, quyết định sản phẩm |
| P2 | `[Tên web]` | Frontend và trải nghiệm giảng viên | Demo luồng chính và correction |
| P3 | `[Tên AI 1]` | Taxonomy retrieval và AI matching | Giải thích classifier, confidence, abstain |
| P4 | `[Tên AI 2]` | Grouping, intent và grounded summary | Giải thích cách tổng hợp, chống hallucination |
| P5 | `[Tên AI 3]` | API, schema, eval, packaging | Trình bày golden set, kết quả đo và fallback |

---

## 1. Mục tiêu duy nhất của 10 giờ

### 1.1 Lát cắt sản phẩm phải giữ nguyên

> Sau buổi học, giảng viên dùng hệ thống để biết phần kiến thức nào nhiều sinh viên chưa rõ; AI gán từng câu hỏi vào taxonomy của đúng buổi học, gom các câu tương tự và tạo bản tóm tắt có căn cứ, còn các trường hợp không chắc được chuyển cho giảng viên duyệt hoặc sửa.

### 1.2 Một luồng demo bắt buộc

1. Chọn `DAY_01` hoặc một buổi học đã có taxonomy.
2. Nạp một batch 8–20 câu hỏi mẫu.
3. Bấm **Phân tích**.
4. Hiển thị top 3 topic theo:
   - số câu hỏi;
   - số sinh viên khác nhau;
   - intent nổi bật;
   - summary;
   - evidence/source reference.
5. Mở một topic để xem câu hỏi đại diện.
6. Mở một câu low-confidence hoặc unmatched.
7. Giảng viên sửa taxonomy hoặc giữ trạng thái “Cần duyệt”.

### 1.3 Non-goals trong 10 giờ

- Không tích hợp Discord/VLearn thật.
- Không xây đăng nhập, phân quyền hoặc quản lý người dùng.
- Không auto-reply hoặc gửi thông báo thật cho sinh viên.
- Không dùng MongoDB/vector DB làm điều kiện để demo chạy.
- Không xây taxonomy cho tài liệu mới.
- Không làm realtime.
- Không hoàn thiện toàn bộ menu chat, feedback, báo cáo và cài đặt đang có.
- Không thay framework frontend.
- Không tối ưu hạ tầng production.

### 1.4 Definition of Done cuối 10 giờ

Sản phẩm chỉ được xem là hoàn thành khi đồng thời đạt:

- [ ] Có ít nhất một AI call thật ở taxonomy matching hoặc grounded summary.
- [ ] Luồng chuẩn chạy end-to-end không sửa dữ liệu bằng tay giữa chừng.
- [ ] Có luồng low-confidence/unmatched và correction.
- [ ] Frontend không phụ thuộc vào backend để bắt đầu phát triển; có fixture fallback.
- [ ] Backend có một lệnh chạy rõ ràng.
- [ ] Có `requirements.txt` và `.env.example`, không có API key trong Git.
- [ ] Có golden set tối thiểu 20 case, trong đó ít nhất 10 case dựa trên chatlog thật.
- [ ] Có kết quả chạy toàn bộ golden set ít nhất một lượt.
- [ ] Có feedback log từ ít nhất 5 người ngoài nhóm.
- [ ] `README.md`, `spec.md`, `eval/`, `validation/`, `reflection/` và slide đủ nội dung theo rubric.
- [ ] Có backup demo bằng JSON kết quả, screenshot hoặc video ngắn.

---

## 2. Kiến trúc MVP và ranh giới module

### 2.1 Pipeline

```text
Batch câu hỏi
    |
    v
Chuẩn hóa input
    |
    v
Retrieve top-k taxonomy node của đúng buổi học
    |
    v
AI chọn node / intent / confidence hoặc abstain
    |
    +----------------------+
    |                      |
    v                      v
auto_grouped          needs_review / unmatched
    |
    v
Group theo topic_id
    |
    v
Đếm question_count + unique_student_count
    |
    v
AI tạo grounded summary kèm supported_question_ids
    |
    v
API response / JSON fixture
    |
    v
Dashboard cho giảng viên
```

### 2.2 Quy tắc taxonomy

- Chỉ dùng taxonomy của buổi học đã chọn.
- Chỉ dùng các chapter có `is_canonical = true` làm nhãn chính.
- Chapter supplementary có thể dùng làm evidence hoặc alternative, không dùng làm nhãn dashboard chính trong MVP.
- Không ép mọi câu hỏi vào taxonomy.
- Câu logistics, off-topic, input quá ngắn hoặc mơ hồ phải có thể trở thành `needs_review` hoặc `unmatched`.
- Không dùng confidence do LLM tự khai báo như một xác suất đã hiệu chỉnh.
- UI chỉ hiển thị `high`, `medium`, `low` và lý do/evidence.

### 2.3 Quy tắc AI

- Prompt yêu cầu strict JSON.
- `temperature` thấp, khuyến nghị `0.0–0.2`.
- Output phải được validate bằng schema trước khi đưa sang module sau.
- Parse lỗi, timeout hoặc thiếu field không được làm crash batch; chuyển câu đó thành `needs_review`.
- Summary chỉ được dùng nội dung từ các câu hỏi trong group.
- Mỗi summary bắt buộc trả về `supported_question_ids`.
- Không đưa API key vào source code, fixture, screenshot hoặc commit.

---

## 3. Hợp đồng dữ liệu — chốt trong 30 phút đầu

P5 là người duy nhất được sửa schema sau khi cả nhóm đã chốt. Mọi thay đổi schema sau T+0:30 phải được leader đồng ý và thông báo vào group.

### 3.1 Request của `POST /api/analyze`

```json
{
  "schema_version": "1.0",
  "session_id": "DAY_01",
  "questions": [
    {
      "question_id": "Q001",
      "student_id": "U001",
      "text": "RAG khác fine-tuning như thế nào?",
      "created_at": "2026-07-30T10:00:00Z"
    }
  ]
}
```

### 3.2 Classification contract cho một câu hỏi

```json
{
  "question_id": "Q001",
  "topic_id": "DAY_01_CH_14",
  "topic_title": "RAG",
  "intent": "compare",
  "confidence": "high",
  "status": "auto_grouped",
  "matched_terms": ["RAG", "fine-tuning"],
  "evidence_refs": [
    {
      "file_id": "D1",
      "line": 120
    }
  ],
  "alternatives": [
    {
      "topic_id": "DAY_01_CH_13",
      "topic_title": "Fine-tuning"
    }
  ],
  "rationale": "Câu hỏi yêu cầu so sánh RAG với fine-tuning."
}
```

### 3.3 Giá trị enum cố định

`intent`:

```text
clarify_concept
compare
need_example
apply_practice
logistics
off_topic
unknown
```

`confidence`:

```text
high
medium
low
```

`status`:

```text
auto_grouped
needs_review
unmatched
error
```

### 3.4 Response của `POST /api/analyze`

```json
{
  "schema_version": "1.0",
  "analysis_id": "ANL_001",
  "session_id": "DAY_01",
  "generated_at": "2026-07-30T10:05:00Z",
  "groups": [
    {
      "topic_id": "DAY_01_CH_14",
      "topic_title": "RAG",
      "question_count": 4,
      "unique_student_count": 3,
      "dominant_intent": "compare",
      "summary": "Sinh viên chủ yếu chưa rõ khi nào dùng RAG thay cho fine-tuning.",
      "supported_question_ids": ["Q001", "Q004", "Q006"],
      "confidence_breakdown": {
        "high": 3,
        "medium": 1,
        "low": 0
      },
      "questions": [
        {
          "question_id": "Q001",
          "student_id": "U001",
          "text": "RAG khác fine-tuning như thế nào?",
          "intent": "compare",
          "confidence": "high",
          "evidence_refs": [
            {
              "file_id": "D1",
              "line": 120
            }
          ]
        }
      ]
    }
  ],
  "review_queue": [],
  "unmatched": [],
  "trace": {
    "matcher_type": "hybrid_llm",
    "matcher_prompt_version": "matcher-v1",
    "summary_prompt_version": "summary-v1",
    "model": "configured-by-env"
  }
}
```

### 3.5 Fixture bắt buộc

P5 tạo hai file ngay trong 30 phút đầu:

```text
backend/fixtures/demo_request.json
backend/fixtures/demo_response.json
```

P2, P3 và P4 làm việc từ hai fixture này. Không ai cần chờ API thật.

---

## 4. Phân quyền file để không sửa chồng nhau

| Khu vực/file | Chủ sở hữu | Người khác được làm gì |
|---|---|---|
| `README.md`, `spec.md`, `validation/`, `reflection/`, nội dung slide | P1 | Chỉ gửi nội dung đề xuất cho P1 |
| `frontend/**` | P2 | Không tự sửa; báo bug bằng issue/message |
| `backend/services/taxonomy_loader.py` | P3 | P5 chỉ import public function |
| `backend/services/taxonomy_matcher.py` | P3 | P5 chỉ import public function |
| `backend/prompts/taxonomy_matcher.md` | P3 | P1 review nội dung, không sửa trực tiếp |
| `backend/services/question_grouper.py` | P4 | P5 chỉ import public function |
| `backend/services/group_summarizer.py` | P4 | P5 chỉ import public function |
| `backend/prompts/group_summary.md` | P4 | P1 review nội dung, không sửa trực tiếp |
| `backend/backend_app.py`, `backend/schemas.py` | P5 | P3/P4 không sửa endpoint |
| `backend/fixtures/**`, `eval/**`, `requirements.txt`, `.env.example` | P5 | P1 cung cấp case/evidence bằng file nháp riêng |
| `.gitignore` | P5 | Mọi người báo mục cần thêm |

### 4.1 Public interface bắt buộc

P3 cung cấp:

```python
classify_question(question, session_id, taxonomy) -> ClassificationResult
classify_batch(questions, session_id, taxonomy) -> list[ClassificationResult]
```

P4 cung cấp:

```python
group_classifications(questions, classifications) -> list[QuestionGroup]
summarize_group(group) -> GroupSummary
summarize_groups(groups) -> list[GroupSummary]
```

P5 chỉ được gọi các hàm public trên. Không import helper có tên bắt đầu bằng `_`.

---

## 5. Timeline 10 giờ và công việc từng người

## Giai đoạn 0 — T+0:00 đến T+0:30: khóa phạm vi và contract

### Mục tiêu

Tất cả có thể bắt đầu làm độc lập sau 30 phút.

### P1 — Leader

- Đọc lát cắt sản phẩm cho cả nhóm và yêu cầu mọi người xác nhận.
- Chốt non-goals.
- Thay tên P1–P5 trong tài liệu này và README.
- Mở bảng theo dõi:

```text
Task | Owner | Branch | Expected file | Test command | Deadline | Status
```

- Xác nhận giờ feature freeze và giờ merge freeze.
- Yêu cầu mỗi người đặt lịch với một user ngoài nhóm để test ở T+7:30.

### P2 — Web

- Đọc request/response contract.
- Xác nhận frontend cần các field nào.
- Không yêu cầu thêm field chỉ để trang trí.
- Tạo branch `feat/web-dashboard`.
- Chuẩn bị frontend dùng `demo_response.json` ngay cả khi API chưa tồn tại.

### P3 — Taxonomy Matching

- Đọc taxonomy JSON và chốt chỉ dùng canonical chapter của session.
- Xác nhận public function và output contract.
- Tạo branch `feat/taxonomy-matcher`.
- Chọn chiến lược MVP:
  1. normalize;
  2. retrieve top-k bằng alias/keyword;
  3. LLM rerank/chọn hoặc abstain.

### P4 — Grouping/Summary

- Xác nhận input là list classification đúng schema.
- Tạo branch `feat/group-summary`.
- Chốt grouping deterministic theo `topic_id`.
- Chốt summary phải trả `supported_question_ids`.

### P5 — API/Eval

- Tạo branch `feat/api-eval`.
- Tạo schema, hai fixture và endpoint stub.
- Chốt schema version `1.0`.
- Gửi fixture lên group trước T+0:30.

### Exit criteria

- [ ] Hai fixture tồn tại.
- [ ] Mọi người biết file mình sở hữu.
- [ ] Mọi người có branch riêng.
- [ ] Không còn tranh luận về tính năng.

---

## Giai đoạn 1 — T+0:30 đến T+3:00: xây module độc lập

### P1 — Spec, evidence và failure scenarios

#### Việc phải làm

- Điền `spec.md` §1–§6.
- Viết pain cụ thể, không dùng chữ AI trong problem statement.
- Mining evidence đủ chuẩn B:
  - tổng số câu hỏi;
  - số user;
  - phương pháp đếm;
  - ít nhất 5 ví dụ ngắn, có mã nguồn/case ID;
  - không commit toàn bộ raw data vào repo public.
- Lập bảng impact ba ứng viên.
- Viết ít nhất tám failure scenarios, hai case cho mỗi lớp:

| Lớp | Case cần có |
|---|---|
| Nguồn sự thật | Nội dung không có trong slide; AI tạo source reference không tồn tại |
| Mơ hồ | “Phần này là sao?”; một câu hỏi chứa hai topic |
| Ngoài phạm vi | Hỏi deadline/chấm điểm; câu off-topic |
| Đặc thù domain | Nhầm hai khái niệm gần nhau; gom câu trái nghĩa vào cùng summary |

- Chốt bốn nguyên tắc HAX/PAIR:
  - G1: nói rõ phạm vi;
  - G2: nói rõ độ tin cậy;
  - G10: low-confidence chuyển review;
  - G9/G11: sửa được và thấy lý do/evidence.

#### Output

```text
spec.md
README.md
validation/test-script.md
```

#### Tự test

- Mỗi con số trong spec phải truy được về file/cách đếm.
- Mỗi nguyên tắc phải trỏ vào một thành phần UI cụ thể.
- Mỗi failure scenario phải có expected behavior.
- Không để placeholder như `[Tên]`, `n = ?`, `___`.

### P2 — Frontend

#### Việc phải làm

- Giữ `frontend/index.html`; không rewrite framework.
- Tạo:

```text
frontend/api.js
frontend/demo_response.json
frontend/README.md
```

- `api.js` phải có:

```javascript
analyzeQuestions(payload)
loadDemoResponse()
```

- Nếu API thành công: dùng response thật.
- Nếu API lỗi hoặc chưa chạy: hiển thị rõ “Demo data” và dùng fixture.
- Sửa dashboard tập trung vào:
  - selector buổi học;
  - nút phân tích;
  - trạng thái loading;
  - top topic cards;
  - số câu hỏi và số sinh viên;
  - detail drawer;
  - evidence/source;
  - low-confidence queue;
  - correction dropdown.
- Ẩn hoặc giảm nổi bật các phần chat/feedback/report không thuộc lát cắt.
- Không hiển thị confidence giả như `94%`.
- Dùng `high/medium/low`.

#### Output

```text
frontend/index.html
frontend/api.js
frontend/demo_response.json
frontend/README.md
```

#### Tự test

- Mở qua HTTP server, không mở trực tiếp bằng `file://`.
- Kiểm tra browser console không có error.
- Test tối thiểu:
  1. fixture hợp lệ;
  2. `groups = []`;
  3. có review queue;
  4. có unmatched;
  5. API timeout/error;
  6. text rất dài;
  7. mobile width khoảng 390px;
  8. desktop width khoảng 1366px.

### P3 — Taxonomy loader và matcher

#### Việc phải làm

- Tạo:

```text
backend/services/__init__.py
backend/services/taxonomy_loader.py
backend/services/taxonomy_matcher.py
backend/prompts/taxonomy_matcher.md
backend/tests/test_taxonomy_loader.py
backend/tests/test_taxonomy_matcher.py
```

- Loader:
  - đọc UTF-8;
  - kiểm tra session tồn tại;
  - chỉ trả canonical chapters;
  - phát hiện duplicate `chapter_id`;
  - không mutate taxonomy gốc.
- Matcher:
  - normalize hai phía;
  - retrieve top 3–5 candidate;
  - exact/alias match ưu tiên trước;
  - gọi LLM cho case cần rerank;
  - strict JSON;
  - validate topic thuộc candidates/session;
  - low-confidence hoặc parse lỗi → `needs_review`;
  - off-topic → `unmatched`;
  - không trả source reference không có trong taxonomy.
- Tạo LLM client có thể mock khi test.

#### Output

```text
backend/services/taxonomy_loader.py
backend/services/taxonomy_matcher.py
backend/prompts/taxonomy_matcher.md
backend/tests/test_taxonomy_loader.py
backend/tests/test_taxonomy_matcher.py
```

#### Unit test bắt buộc

1. Load `DAY_01` thành công.
2. Chỉ canonical chapters được trả.
3. Session không tồn tại trả lỗi có kiểm soát.
4. Exact alias match đúng.
5. Câu paraphrase được đưa vào top-k.
6. Câu mơ hồ trở thành `needs_review`.
7. Câu off-topic trở thành `unmatched`.
8. LLM trả JSON sai không crash.
9. LLM trả `topic_id` ngoài candidate bị reject.
10. Source reference trả về phải tồn tại.
11. Batch có một case lỗi vẫn xử lý các case còn lại.

### P4 — Grouping, intent và grounded summary

#### Việc phải làm

- Tạo:

```text
backend/services/question_grouper.py
backend/services/group_summarizer.py
backend/prompts/group_summary.md
backend/tests/test_question_grouper.py
backend/tests/test_group_summarizer.py
```

- Grouping phải deterministic:
  - chỉ group `auto_grouped`;
  - group theo `topic_id`;
  - `needs_review` không đưa vào group;
  - đếm số question;
  - đếm distinct `student_id`;
  - tính dominant intent;
  - giữ nguyên question ID.
- Summary:
  - input chỉ gồm topic title và câu hỏi trong group;
  - không sử dụng kiến thức bên ngoài;
  - trả summary ngắn;
  - trả `supported_question_ids`;
  - parse lỗi dùng deterministic fallback;
  - không làm mất toàn batch khi một group lỗi.

#### Output

```text
backend/services/question_grouper.py
backend/services/group_summarizer.py
backend/prompts/group_summary.md
backend/tests/test_question_grouper.py
backend/tests/test_group_summarizer.py
```

#### Unit test bắt buộc

1. Hai câu cùng topic được group.
2. Hai topic khác nhau không bị merge.
3. Review/unmatched không đi vào group.
4. `question_count` đúng.
5. `unique_student_count` không đếm trùng.
6. Dominant intent đúng; hòa phải có tie-breaker cố định.
7. Summary có `supported_question_ids`.
8. Supported ID phải thuộc group.
9. LLM timeout trả fallback, không crash.
10. Group rỗng không gọi LLM.
11. Text chứa ký tự đặc biệt/markdown vẫn serialize được.

### P5 — Schema, API stub, eval skeleton và packaging

#### Việc phải làm

- Tạo:

```text
backend/__init__.py
backend/backend_app.py
backend/schemas.py
backend/fixtures/demo_request.json
backend/fixtures/demo_response.json
backend/tests/test_api_contract.py
backend/tests/test_health.py
eval/golden_set.jsonl
eval/evaluate.py
eval/results/.gitkeep
requirements.txt
.env.example
```

- API tối thiểu:

```text
GET  /health
POST /api/analyze
```

- Trong 2 giờ đầu endpoint có thể trả fixture.
- Tạo schema validation độc lập với P3/P4.
- CORS chỉ mở cho localhost trong development.
- `requirements.txt` pin phiên bản đủ dùng.
- `.env.example` chỉ có tên biến, không có secret thật.
- `evaluate.py` có thể chạy với stub classifier trước.
- Golden set có đủ field ngay cả khi expected label chưa hoàn tất.

#### Output

Toàn bộ file trên.

#### Tự test

1. Import app không lỗi.
2. `/health` trả HTTP 200.
3. Request hợp lệ trả schema version `1.0`.
4. Thiếu `question_id` trả 422/validation error.
5. Session không tồn tại trả lỗi có thông điệp.
6. Batch rỗng không crash.
7. Fixture validate được bằng schema.
8. `.env.example` không chứa key thật.

### Exit criteria giai đoạn 1

- [ ] Mỗi người có ít nhất một commit local nhỏ, chưa cần merge.
- [ ] Test riêng của P3, P4, P5 chạy được.
- [ ] P2 chạy được toàn bộ UI bằng fixture.
- [ ] P1 hoàn thành tối thiểu spec §1–§6.

---

## Giai đoạn 2 — T+3:00 đến T+4:30: hardening và pull request độc lập

### Tất cả thành viên

- Dừng thêm feature.
- Chạy test của chính mình.
- Review diff từng file.
- Tạo PR theo template ở `§7.4`.
- Gửi cho một thành viên khác review:
  - P1 review prompt/product behavior của P3 và P4.
  - P2 review fixture/schema của P5.
  - P3 review grouping contract của P4.
  - P4 review matcher output của P3.
  - P5 review khả năng tích hợp của P2.

### P1

- Chốt quality bar trong `spec.md` trước khi xem kết quả toàn bộ:

> Đạt khi ít nhất 80% case được gán đúng taxonomy hoặc abstain đúng; 100% output hợp schema; không có case ngoài phạm vi nào bị gán sai với confidence high; mọi summary có supported question IDs hợp lệ.

- Không đổi quality bar sau lần chạy đầu.
- Chuẩn bị 20 case cho P5 theo cơ cấu ở `§8.5`.

### P2

- Chuyển URL API thành cấu hình, không hard-code rải rác.
- Đảm bảo UI không crash khi thiếu field tùy chọn.
- Chụp screenshot happy path và low-confidence path.

### P3

- Chạy test với mock LLM.
- Chạy thử 3–5 câu với AI call thật.
- Lưu trace đã loại secret.
- Kiểm tra model output không thể đưa topic ngoài candidate.

### P4

- Chạy thử summary với một group 3–5 câu.
- Đọc tay để phát hiện claim không có trong câu hỏi.
- Chạy fallback bằng cách cố tình gây timeout/mock exception.

### P5

- Validate PR output của P3 và P4 bằng schema.
- Hoàn thiện test API với dependency override/mock.
- Chuẩn bị thứ tự merge.

### Exit criteria

- [ ] 5 PR có mô tả, test result và file list.
- [ ] Không PR nào có secret hoặc raw output chứa dữ liệu cấm.
- [ ] Contract chưa bị thay đổi sau khi P2 bắt đầu làm.

---

## Giai đoạn 3 — T+4:30 đến T+6:00: tích hợp có kiểm soát

### Thứ tự merge

1. P5: schema, fixtures, app skeleton, dependencies.
2. P3: taxonomy loader và matcher.
3. P4: grouping và summary.
4. P5: commit nối pipeline vào `/api/analyze`.
5. P2: frontend.
6. P1: spec/README hiện tại.

### Quy tắc tích hợp

- Leader là người bấm merge.
- Một lần chỉ merge một PR.
- Sau mỗi PR:
  1. pull `main`;
  2. cài dependency nếu có đổi;
  3. chạy focused tests;
  4. chạy API smoke test;
  5. mới merge PR tiếp theo.
- Nếu merge làm test cũ fail, dừng merge và trả lỗi cho owner của module.
- Không “sửa tạm” code người khác trực tiếp trên `main`.

### P1

- Giữ bảng trạng thái.
- Quyết định bug nào P0/P1/P2.
- Không cho sửa lỗi cosmetic nếu pipeline chưa chạy.

### P2

- Sau khi API thật có response, thay fixture bằng API.
- Giữ fallback fixture.
- Test loading, success, error, retry.

### P3

- Theo dõi log của matcher.
- Fix contract violation trong file P3 sở hữu.
- Không sửa API hoặc frontend.

### P4

- Theo dõi group và summary output.
- Fix unsupported ID hoặc count sai trong file P4 sở hữu.
- Không sửa matcher.

### P5

- Nối pipeline:

```text
request
→ taxonomy loader
→ classify_batch
→ group_classifications
→ summarize_groups
→ response schema
```

- Đảm bảo một question lỗi không làm cả batch HTTP 500.
- Ghi `trace` nhưng không ghi prompt chứa dữ liệu nhạy cảm hoặc API key.

### Smoke test end-to-end

Chạy ba request:

1. Happy path: câu rõ ràng khớp taxonomy.
2. Ambiguous path: câu ngắn/multi-topic vào review.
3. Out-of-scope path: logistics/off-topic không auto-group high.

### Exit criteria

- [ ] `/health` chạy.
- [ ] `/api/analyze` trả response đúng schema.
- [ ] Frontend đọc được response thật.
- [ ] Fixture fallback vẫn chạy.
- [ ] Happy, ambiguous và out-of-scope path đều demo được.

---

## Giai đoạn 4 — T+6:00 đến T+7:30: golden set và sửa đúng một lỗi lớn nhất

### P5 điều phối

- Chạy toàn bộ golden set lần 1.
- Lưu nguyên kết quả, kể cả case fail:

```text
eval/results/run-001.json
eval/results/run-001.md
```

- Không sửa hoặc xóa case fail.
- Tính:
  - schema-valid rate;
  - topic correct-or-correct-abstain rate;
  - high-confidence wrong count;
  - summary support-ID validity;
  - số case timeout/error.

### P1

- So kết quả với quality bar đã chốt.
- Chọn đúng **một failure có hậu quả lớn nhất**.
- Ghi nguyên nhân giả thuyết vào `spec.md` changelog.

### P3

- Nếu failure nằm ở retrieve/classify, sửa matcher/prompt.
- Chạy focused test trước.
- Thêm regression test đúng case vừa fail.

### P4

- Nếu failure nằm ở group/summary, sửa grouper/prompt/fallback.
- Thêm regression test đúng case vừa fail.

### P2

- Nếu failure là user không thấy low confidence/evidence, sửa UI.
- Không làm lại layout.

### P5

- Sau fix, chạy lại toàn bộ 20+ case.
- Lưu:

```text
eval/results/run-002.json
eval/results/run-002.md
```

### Exit criteria

- [ ] Có run-001 đầy đủ.
- [ ] Có một failure được phân tích.
- [ ] Có regression test.
- [ ] Có run-002 đầy đủ.
- [ ] Không thay đổi quality bar.

---

## Giai đoạn 5 — T+7:30 đến T+8:30: validation với 5 người ngoài nhóm

### Cách tổ chức không gây chờ

- Mỗi thành viên tự test với một người ngoài nhóm.
- Dùng cùng một test script do P1 chuẩn bị.
- Không thuyết minh trong lúc user làm task.
- Mỗi phiên tối đa 10 phút.
- Mỗi người gửi log cho P1 ngay sau phiên.

### Task giao cho user

> Đây là danh sách câu hỏi sau một buổi học. Hãy dùng hệ thống để xác định phần nào cần giảng lại trước và kiểm tra xem có câu nào AI phân loại chưa đáng tin.

### Ba câu hỏi bắt buộc

1. Điều gì khó hiểu hoặc khó chịu nhất?
2. Bạn có tin kết quả phân loại/tóm tắt này không? Vì sao?
3. Nếu là giảng viên, bạn có dùng kết quả này để quyết định phần cần giảng lại không? Vì sao?

### File log

P1 tổng hợp vào:

```text
validation/feedback-log.md
```

Mỗi dòng phải có:

```text
Tên/vai trò
Willing user từ CP1 hay không
Task
Quan sát thao tác
Quote nguyên văn
Mức nghiêm trọng
Đề xuất
Quyết định của team
```

### Sau validation

- Chọn một thay đổi nhỏ nhưng rõ ràng.
- P1 ghi vào changelog.
- Owner phù hợp thực hiện.
- Nếu không thay đổi, phải ghi lý do dựa trên feedback/eval.

### Exit criteria

- [ ] 5 log từ 5 người.
- [ ] Có ít nhất 2 willing users đã khai trước đó nếu có thể.
- [ ] Có ít nhất một quote tiêu cực hoặc điểm kẹt thực tế.
- [ ] Có một thay đổi hoặc quyết định giữ nguyên có căn cứ.

---

## Giai đoạn 6 — T+8:30 đến T+9:30: hoàn thiện artifact và slide

### P1

- Hoàn thiện `spec.md` §7–§9.
- Cập nhật README:
  - tên team;
  - thành viên;
  - phân công;
  - cách chạy;
  - phần thật/phần mock;
  - link đến eval và validation.
- Dựng slide 6 trang:
  1. User & Job.
  2. Evidence và vì sao chọn.
  3. Giải pháp + demo.
  4. Eval so với quality bar.
  5. User feedback + thay đổi.
  6. Nếu có thêm một tuần.

### P2

- Chuẩn bị screenshot:
  - happy path;
  - low confidence;
  - correction;
  - API error/fallback.
- Không sửa CSS cosmetic quá 15 phút.

### P3

- Viết một trang giải thích:
  - candidate retrieval;
  - LLM rerank;
  - abstain;
  - confidence;
  - một failure đã sửa.
- Chuẩn bị câu trả lời Q&A: “Tại sao đây là AI matching, không chỉ keyword?”

### P4

- Viết một trang giải thích:
  - grouping;
  - unique student count;
  - grounded summary;
  - supported IDs;
  - fallback.
- Chuẩn bị câu trả lời Q&A: “Làm sao biết summary không bịa?”

### P5

- Kiểm tra repo từ trạng thái clone sạch theo runbook.
- Xuất bảng eval ngắn cho slide.
- Lưu một JSON output thật đã redact.
- Chuẩn bị backup demo.

### Tất cả

- Viết reflection cá nhân:

```text
reflection/<ma-thanh-vien>-<ten>.md
```

- Mỗi người tự giải thích được file mình sở hữu.

---

## Giai đoạn 7 — T+9:30 đến T+10:00: merge freeze và dry run

### Luật

- Không thêm feature.
- Không đổi schema.
- Không đổi prompt trừ khi app không chạy.
- Chỉ fix P0:
  - app không start;
  - endpoint crash;
  - frontend trắng;
  - secret lộ;
  - response sai schema;
  - demo path không đi hết.

### Dry run 1

- 5 phút trình bày, bấm giờ.
- Chạy một happy path.
- Chạy một case low-confidence hoặc failure path.
- Mỗi thành viên nói ít nhất một phần.

### Adversarial run

- Một thành viên không thuộc P3 nghĩ một câu lạ.
- Chạy tại chỗ như thẻ giám khảo.
- Nếu sai, không che giấu; giải thích confidence/fallback.

### Dry run 2

- Chạy hoàn toàn bằng backup mode.
- Xác nhận vẫn trình bày được nếu AI API/network lỗi.

### Checklist cuối

- [ ] `git status` sạch.
- [ ] Không có key/secret.
- [ ] Không có `.env`, `.venv`, `__pycache__`.
- [ ] Không commit thêm raw data.
- [ ] README chạy đúng.
- [ ] Link/file trong slide tồn tại.
- [ ] Demo response và screenshot backup tồn tại.
- [ ] Mỗi thành viên biết câu mình phải nói.

---

## 6. Hướng dẫn chuẩn bị file và commit cho từng người

## 6.1 Quy trình Git chung

### Bắt đầu branch

```powershell
git switch main
git pull --ff-only origin main
git switch -c <ten-branch>
```

Tên branch:

```text
docs/spec-demo
feat/web-dashboard
feat/taxonomy-matcher
feat/group-summary
feat/api-eval
fix/<mo-ta-ngan>
```

### Trước mỗi commit

```powershell
git status --short
git diff --check
git diff -- <danh-sach-file-minh-so-huu>
```

Không dùng `git add .`. Chỉ add file mình sở hữu:

```powershell
git add -- <file-1> <file-2> <file-3>
git diff --cached
git status --short
```

Sau khi đã đọc toàn bộ staged diff:

```powershell
git commit -m "<type>: <noi-dung-cu-the>"
```

Ví dụ:

```text
docs: complete AI spec and failure scenarios
feat(frontend): render analysis groups and review queue
feat(matcher): add taxonomy retrieval and abstain handling
feat(summary): add grounded group summaries with support ids
test(eval): add 20-case taxonomy golden set
fix(api): isolate per-question classification failures
```

### Trước khi push PR

```powershell
git fetch origin
git merge origin/main
git diff --check
git status --short
```

Giải quyết conflict chỉ trong file mình sở hữu. Nếu conflict nằm ở file người khác sở hữu, dừng và gọi owner.

Sau test:

```powershell
git push -u origin <ten-branch>
```

## 6.2 P1 chuẩn bị file trước commit

### File được commit

```text
PLAN_10_GIO.md
README.md
spec.md
validation/test-script.md
validation/feedback-log.md
reflection/<file-cua-P1>.md
demo-slides.pdf
```

### Checklist nội dung

- [ ] Không còn placeholder.
- [ ] Số liệu có nguồn/cách đếm.
- [ ] Quote ngắn, đúng quy định dữ liệu.
- [ ] Có ≥3 ứng viên impact và ứng viên đã loại.
- [ ] Có ≥3 non-goals.
- [ ] Có 4 nguyên tắc HAX/PAIR gắn vị trí UI.
- [ ] Có ≥8 scenarios.
- [ ] Có quality bar bằng số.
- [ ] Có link tới golden set, results và validation.
- [ ] Changelog ghi case/feedback cụ thể.

### Test trước commit

```powershell
rg -n "\[Tên|\[XX\]|\[X\]|n = \?|___|\[ \]" README.md spec.md
git diff --check
```

Kết quả `rg` phải chỉ còn checkbox chủ ý, không còn placeholder.

## 6.3 P2 chuẩn bị file trước commit

### File được commit

```text
frontend/index.html
frontend/api.js
frontend/demo_response.json
frontend/README.md
```

### Checklist nội dung

- [ ] Không chứa API key.
- [ ] API base URL chỉ khai báo một chỗ.
- [ ] Có demo fallback.
- [ ] Có loading, empty, error, review và unmatched state.
- [ ] Text từ API được escape trước khi render.
- [ ] Không còn số liệu `94%`, `128`, `32` hard-code được trình bày như dữ liệu thật.
- [ ] Không làm vỡ mobile.
- [ ] Không sửa file backend.

### Test trước commit

```powershell
.\.venv\Scripts\python.exe -m http.server 5500 --directory frontend
```

Test bằng browser:

- trang load;
- console không error;
- fixture render;
- API error fallback;
- drawer mở/đóng;
- correction hoạt động;
- keyboard/button chính hoạt động;
- mobile không tràn ngang.

Nếu có formatter/linter thì chạy, nhưng không cài framework mới chỉ để lint.

## 6.4 P3 chuẩn bị file trước commit

### File được commit

```text
backend/services/__init__.py
backend/services/taxonomy_loader.py
backend/services/taxonomy_matcher.py
backend/prompts/taxonomy_matcher.md
backend/tests/test_taxonomy_loader.py
backend/tests/test_taxonomy_matcher.py
```

### Checklist code

- [ ] Public function đúng tên và signature.
- [ ] Không đọc environment tại import time nếu không cần.
- [ ] Không có global mutable state.
- [ ] Có timeout.
- [ ] LLM client inject/mock được.
- [ ] Validate topic ID.
- [ ] Parse lỗi → review, không crash.
- [ ] Source reference phải thuộc taxonomy.
- [ ] Không log API key hoặc toàn bộ prompt chứa dữ liệu nhạy cảm.
- [ ] Không sửa schema/API/frontend.

### Test trước commit

```powershell
.\.venv\Scripts\python.exe -m pytest backend/tests/test_taxonomy_loader.py -q
.\.venv\Scripts\python.exe -m pytest backend/tests/test_taxonomy_matcher.py -q
```

Sau test mock, chạy 3–5 sample với AI thật và lưu trace đã redact nếu được yêu cầu.

## 6.5 P4 chuẩn bị file trước commit

### File được commit

```text
backend/services/question_grouper.py
backend/services/group_summarizer.py
backend/prompts/group_summary.md
backend/tests/test_question_grouper.py
backend/tests/test_group_summarizer.py
```

### Checklist code

- [ ] Grouping không phụ thuộc LLM.
- [ ] Không group review/unmatched.
- [ ] Không đếm trùng student.
- [ ] Summary chỉ dùng question trong group.
- [ ] Mọi supported ID thuộc group.
- [ ] Có fallback summary.
- [ ] Một group lỗi không làm mất các group khác.
- [ ] Public function đúng signature.
- [ ] Không sửa matcher/schema/API/frontend.

### Test trước commit

```powershell
.\.venv\Scripts\python.exe -m pytest backend/tests/test_question_grouper.py -q
.\.venv\Scripts\python.exe -m pytest backend/tests/test_group_summarizer.py -q
```

## 6.6 P5 chuẩn bị file trước commit

### File được commit

```text
backend/__init__.py
backend/backend_app.py
backend/schemas.py
backend/fixtures/**
backend/tests/test_api_contract.py
backend/tests/test_health.py
eval/**
requirements.txt
.env.example
.gitignore
backend/README.md
```

### Checklist code

- [ ] Schema version là `1.0`.
- [ ] Fixture validate qua schema.
- [ ] API trả lỗi có kiểm soát.
- [ ] Không có Mongo/vector DB là dependency bắt buộc.
- [ ] Requirements pin version.
- [ ] `.env.example` không có value thật.
- [ ] `.gitignore` loại `.env`, `.venv`, `__pycache__`, output tạm.
- [ ] Eval giữ đủ case pass/fail.
- [ ] Results có timestamp/prompt version/model alias.
- [ ] Không sửa logic nội bộ của P3/P4.

### Test trước commit

```powershell
.\.venv\Scripts\python.exe -m pytest backend/tests/test_health.py -q
.\.venv\Scripts\python.exe -m pytest backend/tests/test_api_contract.py -q
.\.venv\Scripts\python.exe -m pytest backend/tests -q
```

### Secret scan tối thiểu

```powershell
rg -n "AIza|sk-|mongodb\+srv|api[_-]?key\s*=|password\s*=" backend frontend eval .env.example
```

Đọc từng kết quả; không commit secret thật.

---

## 7. Chuẩn Pull Request và review

## 7.1 Một PR được phép merge khi

- [ ] Chỉ thay đổi file thuộc owner.
- [ ] Mô tả rõ input/output.
- [ ] Có test mới hoặc lý do hợp lý nếu chỉ sửa docs.
- [ ] Focused tests pass.
- [ ] Không đổi contract ngoài kế hoạch.
- [ ] Không có secret.
- [ ] Diff không có whitespace error.
- [ ] Có fallback hoặc error behavior.

## 7.2 Kích thước commit

- Một commit nên giải quyết một việc.
- Không trộn refactor, formatting và feature.
- Không commit file sinh tự động không cần thiết.
- Không commit `.venv`, cache, log debug hoặc file tạm.
- Không đổi tên nhiều file gần giờ tích hợp.

## 7.3 Quy tắc review chéo

Reviewer không cần viết lại code. Chỉ kiểm:

1. Có đúng contract không?
2. Failure có được xử lý không?
3. Test có bắt được lỗi quan trọng không?
4. Có sửa file ngoài quyền sở hữu không?
5. Có secret/dữ liệu nhạy cảm không?
6. Có làm người tiếp theo phải đoán input/output không?

## 7.4 PR template

```markdown
## Mục tiêu

## Files changed

## Input contract

## Output contract

## Test đã chạy
- Command:
- Result:

## Failure/fallback behavior

## Ảnh hưởng tới module khác

## Việc còn lại/rủi ro

## Checklist
- [ ] Không có secret
- [ ] Không sửa file ngoài ownership
- [ ] Focused tests pass
- [ ] Diff đã tự review
```

---

## 8. Chiến lược test đầy đủ

## 8.1 Tầng 1 — Contract tests

Mục tiêu: producer và consumer không hiểu khác nhau.

Test:

- Request fixture validate.
- Response fixture validate.
- Enum chỉ nhận giá trị đã chốt.
- `topic_id = null` hợp lệ khi status là review/unmatched.
- `auto_grouped` bắt buộc có topic.
- Supported IDs phải là list.
- Schema version mismatch được báo rõ.

Owner: P5.

## 8.2 Tầng 2 — Unit tests

Mục tiêu: mỗi người chứng minh module của mình đúng mà không cần module khác.

- P3 mock LLM.
- P4 mock summarizer.
- P5 dependency override endpoint.
- P2 dùng fixture.

Không dùng network thật trong unit tests.

## 8.3 Tầng 3 — Integration tests

Mục tiêu: kiểm tra ranh giới module.

Các test bắt buộc:

1. Taxonomy loader → matcher nhận đúng candidate.
2. Matcher output → grouper không mất question ID.
3. Grouper → summarizer giữ đúng supported IDs.
4. Pipeline → response schema.
5. Một câu lỗi trong batch → các câu khác vẫn trả kết quả.
6. LLM timeout → response vẫn có review/error item.

Owner: P5, P3/P4 sửa lỗi ở module mình.

## 8.4 Tầng 4 — API smoke tests

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.backend_app:app --port 8000
```

Ở terminal khác:

```powershell
Invoke-RestMethod -Method Get -Uri "http://localhost:8000/health"

$body = Get-Content -Raw -Encoding utf8 "backend/fixtures/demo_request.json"
Invoke-RestMethod `
  -Method Post `
  -Uri "http://localhost:8000/api/analyze" `
  -ContentType "application/json" `
  -Body $body
```

Kiểm:

- status code;
- schema version;
- đủ groups/review/unmatched;
- không có stack trace trong response;
- không có secret trong log.

## 8.5 Tầng 5 — Golden set

Tối thiểu 20 case:

| Nhóm | Số case | Ví dụ |
|---|---:|---|
| Normal | 8 | câu rõ topic, paraphrase, intent khác nhau |
| Nguồn sự thật | 2 | nội dung không có trong slide, source không tồn tại |
| Mơ hồ | 2 | “phần này là sao?”, multi-topic |
| Ngoài phạm vi | 2 | deadline, điểm số, off-topic |
| Đặc thù domain | 2 | RAG/fine-tuning, workflow/agent |
| Hiếm/noisy | 4 | typo, không dấu, rất dài, prompt injection/UI text |

Ít nhất 10 case phải lấy hoặc phát triển từ chatlog thật và chỉ lưu phần tối thiểu cần thiết.

Schema đề xuất cho mỗi dòng JSONL:

```json
{
  "case_id": "GS001",
  "source_type": "chatlog_derived",
  "source_ref": "T0001",
  "session_id": "DAY_01",
  "question": {
    "question_id": "Q_GS001",
    "student_id": "U_TEST",
    "text": "RAG khác fine-tuning như thế nào?"
  },
  "expected_topic_ids": ["DAY_01_CH_14"],
  "expected_status": "auto_grouped",
  "risk_class": "normal",
  "notes": "Chấp nhận top-1 trong expected_topic_ids."
}
```

## 8.6 Tầng 6 — Human review

Hai thành viên chấm độc lập ít nhất năm case khó.

Nếu hai người bất đồng:

- không tự chọn kết quả có lợi;
- ghi disagreement;
- sửa định nghĩa pass/fail nếu còn trước lúc khóa;
- sau khi quality bar khóa, không đổi tiêu chí để làm đẹp số.

## 8.7 Tầng 7 — User validation

Không thay thế bằng “mọi người xem giúp UI đẹp không”.

User phải thực hiện task thật, nhóm quan sát và ghi quote.

## 8.8 Tầng 8 — Demo reliability

Chạy bốn mode:

1. AI/API bình thường.
2. AI timeout.
3. Backend không chạy, frontend dùng fixture.
4. Case lạ của giám khảo.

---

## 9. Cấu trúc repo mục tiêu

```text
repo/
├── PLAN_10_GIO.md
├── README.md
├── spec.md
├── requirements.txt
├── .env.example
├── backend/
│   ├── __init__.py
│   ├── backend_app.py
│   ├── schemas.py
│   ├── README.md
│   ├── fixtures/
│   │   ├── demo_request.json
│   │   └── demo_response.json
│   ├── prompts/
│   │   ├── taxonomy_matcher.md
│   │   └── group_summary.md
│   ├── services/
│   │   ├── __init__.py
│   │   ├── taxonomy_loader.py
│   │   ├── taxonomy_matcher.py
│   │   ├── question_grouper.py
│   │   └── group_summarizer.py
│   └── tests/
│       ├── test_health.py
│       ├── test_api_contract.py
│       ├── test_taxonomy_loader.py
│       ├── test_taxonomy_matcher.py
│       ├── test_question_grouper.py
│       └── test_group_summarizer.py
├── frontend/
│   ├── index.html
│   ├── api.js
│   ├── demo_response.json
│   └── README.md
├── eval/
│   ├── golden_set.jsonl
│   ├── evaluate.py
│   └── results/
│       ├── run-001.json
│       ├── run-001.md
│       ├── run-002.json
│       └── run-002.md
├── validation/
│   ├── test-script.md
│   └── feedback-log.md
├── reflection/
│   └── <moi-thanh-vien-mot-file>.md
└── demo-slides.pdf
```

---

## 10. Thứ tự cắt khi trễ tiến độ

### Giữ bằng mọi giá

1. AI call thật.
2. Taxonomy matching có abstain.
3. Group và số liệu cơ bản.
4. Frontend hiển thị kết quả và review queue.
5. Golden set + run result.
6. Spec/evidence/validation.

### Cắt theo thứ tự

1. Animation và dark mode.
2. Chart phụ.
3. Chat và feedback panel.
4. Vector DB.
5. MongoDB.
6. Intent nếu classifier chưa ổn.
7. Summary AI cho mọi group; chỉ summary top 3 group.
8. Live data ingestion; dùng batch fixture.

### Fallback matrix

| Lỗi | Fallback | Người xử lý |
|---|---|---|
| Vector DB chưa chạy | Keyword/alias top-k + LLM rerank | P3 |
| LLM classifier timeout | Rule candidate + `needs_review` | P3 |
| LLM summary timeout | Deterministic template | P4 |
| Backend lỗi | Frontend dùng `demo_response.json` | P2/P5 |
| Frontend API parse lỗi | Hiển thị error + nút dùng demo data | P2 |
| Một question lỗi | Đưa riêng item vào review/error | P5 |
| Network lỗi lúc demo | JSON output thật đã lưu + screenshot/video | P5 |
| Case lạ phân loại sai | Hiển thị low-confidence/correction, giải thích giới hạn | P1/P3 |

---

## 11. Phân loại bug và người chịu trách nhiệm

| Mức | Ví dụ | Xử lý |
|---|---|---|
| P0 | App không start, API 500 toàn batch, UI trắng, lộ key, schema vỡ | Dừng mọi việc liên quan và fix ngay |
| P1 | Sai high-confidence, summary bịa, correction không hoạt động, eval runner sai | Fix trước validation/dry run |
| P2 | Căn lề, animation, màu sắc, text nhỏ | Ghi backlog, không fix sau feature freeze |

### Quy tắc xác định owner của lỗi

- Output sai trước schema: producer module sửa.
- Output đúng schema nhưng frontend render sai: P2 sửa.
- Schema không đủ/không nhất quán: P5 sửa sau khi P1 phê duyệt.
- Expected result/golden case sai: P1 và P5 review, không để model owner tự sửa label theo output của mình.
- Integration import/config sai: P5 sửa.
- Product behavior không rõ: P1 quyết định trong 5 phút.

---

## 12. Runbook từ máy sạch

### 12.1 Chuẩn bị môi trường

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Điền API key vào `.env` cục bộ. Không commit `.env`.

### 12.2 Chạy backend

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.backend_app:app --reload --port 8000
```

### 12.3 Chạy frontend

```powershell
.\.venv\Scripts\python.exe -m http.server 5500 --directory frontend
```

Mở:

```text
http://localhost:5500
```

### 12.4 Chạy test

```powershell
.\.venv\Scripts\python.exe -m pytest backend/tests -q
```

### 12.5 Chạy eval

```powershell
.\.venv\Scripts\python.exe eval/evaluate.py `
  --golden-set eval/golden_set.jsonl `
  --output eval/results/run-manual.json
```

Nếu command thực tế khác, P5 phải cập nhật cả README và runbook này trong cùng PR.

---

## 13. Checklist theo checkpoint

### CP3 — AI thật + đo lượt đầu

- [ ] AI call thật, không hard-code.
- [ ] Trace/prompt version được lưu, không có secret.
- [ ] Golden set ≥20.
- [ ] Có đủ case bốn lớp khó.
- [ ] Có run-001 và tỷ lệ.

### CP4 — Spec gần cuối

- [ ] Evidence chuẩn A/B.
- [ ] Bảng impact ba ứng viên.
- [ ] Non-goals.
- [ ] Automation là augment/conditional, có lý do cost-of-error.
- [ ] Bốn nguyên tắc HAX/PAIR.
- [ ] Tám failure scenarios.
- [ ] Quality bar đã khóa.

### CP5 — Validation và dry run

- [ ] Năm feedback log có tên/vai.
- [ ] Có changelog.
- [ ] Slide final.
- [ ] Mọi thành viên giải thích được phần mình làm.
- [ ] Dry run có bấm giờ.

### CP6 — Demo

- [ ] Demo một happy path.
- [ ] Demo một failure/low-confidence path.
- [ ] Có % so với quality bar.
- [ ] Có một failure thật và cách xử lý.
- [ ] Mỗi thành viên nói một phần.
- [ ] Sẵn sàng chạy case lạ.

---

## 14. Bảng theo dõi leader có thể copy

| Deadline | Deliverable | Owner | Branch | Test bắt buộc | Trạng thái |
|---|---|---|---|---|---|
| T+0:30 | Contract + fixture | P5 | `feat/api-eval` | Schema validate | ☐ |
| T+3:00 | Spec §1–§6 | P1 | `docs/spec-demo` | Placeholder scan | ☐ |
| T+3:00 | Frontend fixture flow | P2 | `feat/web-dashboard` | Browser smoke | ☐ |
| T+3:00 | Matcher + tests | P3 | `feat/taxonomy-matcher` | Matcher unit tests | ☐ |
| T+3:00 | Grouper/summary + tests | P4 | `feat/group-summary` | Summary unit tests | ☐ |
| T+3:00 | API stub + eval skeleton | P5 | `feat/api-eval` | API contract tests | ☐ |
| T+4:30 | PR ready | P1–P5 | riêng | Focused tests | ☐ |
| T+6:00 | E2E integrated | P5 | `main` | 3-path smoke | ☐ |
| T+6:30 | Run-001 | P5 | `main` | Full golden set | ☐ |
| T+7:30 | Run-002 | P5 | `main` | Full golden set | ☐ |
| T+8:30 | 5 validation logs | P1 | `docs/spec-demo` | Log completeness | ☐ |
| T+9:30 | Artifacts + backup | P1/P5 | `main` | Clean-clone run | ☐ |
| T+10:00 | Final dry run | Tất cả | `main` | Demo checklist | ☐ |

---

## 15. Quyết định cuối cùng dành cho leader

Khi có tranh luận trong 10 giờ, ưu tiên theo thứ tự:

1. Có giúp demo lát cắt chính không?
2. Có giúp lấy điểm evidence/eval/validation không?
3. Có giảm failure nguy hiểm không?
4. Có làm người khác phải đổi contract hoặc chờ không?
5. Có thể làm và test trong dưới 30 phút không?

Nếu câu trả lời cho `1–3` là “không”, hoặc câu trả lời cho `4` là “có”, đưa việc đó vào backlog.

Mục tiêu không phải là xây một hệ thống lớn. Mục tiêu là chứng minh bằng dữ liệu rằng một quyết định AI cụ thể giúp giảng viên nhận ra lỗ hổng kiến thức của lớp, biết lúc nào nên tin, và vẫn giữ quyền kiểm soát khi hệ thống không chắc.

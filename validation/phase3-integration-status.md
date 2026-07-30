# P1 — Bảng trạng thái tích hợp Giai đoạn 3

Ngày kiểm tra: 2026-07-31

Baseline:

- Branch local: `shn`.
- `HEAD`: `2243d2b676e9809fb21ee3bd47998b34a440ec15`.
- `HEAD` trùng `origin/main` tại thời điểm kiểm tra.
- Working tree sạch trước khi P1 tạo báo cáo này.

## 1. Quyết định leader

Trạng thái Giai đoạn 3: **BLOCKED — chưa đạt exit criteria**.

Quyết định:

1. Dừng merge/tích hợp tiếp theo cho đến khi P5 nối pipeline thật vào
   `POST /api/analyze`.
2. Không cho sửa lỗi cosmetic khi các P0 bên dưới chưa được xử lý.
3. Không sửa tạm code của P2–P5 trên branch P1.
4. Mỗi owner sửa đúng file mình sở hữu, chạy focused tests và gửi lại kết
   quả để P1 cho phép chạy lại smoke test.
5. Giữ nguyên schema version `1.0`, enum và quality bar đã khóa.

## 2. Audit thứ tự tích hợp

| Bước theo plan | Owner | Commit/hiện trạng | Kiểm tra | Trạng thái |
|---|---|---|---|---|
| 1. Schema, fixtures, app skeleton, dependencies | P5 | `8724edc` | Fixture/schema tests nằm trong full suite | Đã có, nhưng app sau đó bị trộn thêm MongoDB |
| 2. Taxonomy loader và matcher | P3 | `101a455`, hardening `1a70fbe` | Unit tests pass trong full suite; direct pipeline trả đúng ba status mẫu | Đạt ở mức module |
| 3. Grouping và summary | P4 | `eeff6d3`, hardening `9e67b2a` | Unit/hardening tests pass; fallback giữ supported IDs | Đạt ở mức module |
| 4. Nối pipeline vào `/api/analyze` | P5 | Không tìm thấy implementation trong endpoint | Endpoint chỉ đọc `demo_response.json` | **Thiếu — P0** |
| 5. Frontend dùng API thật và giữ fixture | P2 | `37374fb`, hardening `2243d2b` | Có API URL cấu hình và fallback; request hiện gửi `questions: []` | Có khung, chưa đạt E2E |
| 6. Spec/README hiện tại | P1 | `18a80c9` và báo cáo này | Placeholder/diff/ownership scan | Đạt phần tài liệu |

Sai lệch cần ghi nhận: P2 đã được đưa vào history trước khi bước nối
pipeline P5 tồn tại. Không revert; leader yêu cầu hoàn thành bước 4 rồi
chạy lại toàn bộ smoke test trước khi chấp nhận Giai đoạn 3.

## 3. Kết quả test

### Full backend suite

Command:

```powershell
.\.venv\Scripts\python.exe -m pytest backend/tests -q -p no:cacheprovider
```

Kết quả:

```text
49 passed, 3 warnings
```

Ba warning là deprecation warning của Starlette/FastAPI; không làm fail
suite. Kết quả này chỉ chứng minh module và fixture tests pass, không chứng
minh endpoint đã nối pipeline thật.

### Direct service boundary

P1 gọi trực tiếp:

```text
load_session_taxonomy
→ classify_batch
→ group_classifications
→ summarize_groups
```

Kết quả ba case:

| Case | Kết quả module |
|---|---|
| `Token là gì?` | `auto_grouped`, `DAY_01_CH_11` |
| `Phần này là sao?` | `needs_review` |
| `Deadline nộp bài là khi nào?` | `unmatched` |

Điều này chứng minh module P3/P4 có thể tạo ba path, nhưng P5 chưa nối
chúng vào HTTP endpoint.

Ranh giới cần P5 xử lý: item trong `review_queue/unmatched` từ grouper
không có `student_id` và `text`, trong khi `ReviewItem` của schema bắt buộc
hai field này. P5 phải join lại với input question khi dựng response; không
được yêu cầu P3/P4 đổi public contract ngoài plan.

## 4. HTTP smoke test

Backend được chạy bằng:

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.backend_app:app --port 8000
```

### `/health`

```json
{"status": "ok"}
```

### Ba request bắt buộc

| Case | Input | analysis_id | Groups | Review | Unmatched | First question |
|---|---|---|---:|---:|---:|---|
| Happy | `Token là gì?` | `ANL_DEMO_001` | 2 | 1 | 2 | `Q001` |
| Ambiguous | `Phần này là sao?` | `ANL_DEMO_001` | 2 | 1 | 2 | `Q001` |
| Out of scope | `Deadline nộp bài là khi nào?` | `ANL_DEMO_001` | 2 | 1 | 2 | `Q001` |

Ba response giống hệt fixture và không chứa question ID đã gửi. Do đó
HTTP smoke test **fail** dù status code là 200 và response hợp schema.

### Frontend fixture

Static server trên một port trống trả:

```text
GET /index.html             200
GET /api.js                 200
GET /demo_response.json     200
schema_version              1.0
groups                      2
review_queue                1
unmatched                   1
```

Fixture fallback tồn tại ở mức asset/HTTP. Chưa đánh dấu browser smoke
pass cho đến khi P2 test loading, success, error và retry với API thật.

## 5. Bug register và owner

### P0 — dừng tích hợp và sửa ngay

| ID | Hiện tượng | Bằng chứng | Owner | Điều kiện đóng |
|---|---|---|---|---|
| `INT-P0-01` | `/api/analyze` bỏ qua input và luôn trả fixture | Ba request khác nhau đều trả `ANL_DEMO_001`, first question `Q001` | P5 | Endpoint gọi loader → matcher → grouper → summarizer và response validate schema |
| `INT-P0-02` | Review/unmatched chưa qua được response schema khi nối trực tiếp | Output grouper thiếu `student_id`, `text`; `ReviewItem` bắt buộc hai field | P5 | P5 join input question khi dựng review/unmatched; có integration test |
| `INT-P0-03` | Chưa có đường AI call thật khả dụng trong backend tích hợp | `.env` dùng tên biến Gemini; backend dùng OpenAI/OpenRouter; `.env.example` dùng tên thứ ba; package `openai` không có trong requirements | P5 điều phối config; P3/P4 xác nhận client | Một model/provider contract thống nhất, dependency cài được, trace ghi model/prompt version, real call có thể chạy |
| `INT-P0-04` | Frontend gửi batch rỗng | `analyzeQuestions({ session_id, questions: [] })` | P2 | Gửi batch 8–20 câu hợp request schema và render response thật |

### P1 — phải sửa trước validation/dry run

| ID | Hiện tượng | Owner | Điều kiện đóng |
|---|---|---|---|
| `INT-P1-01` | `backend_app.py` và `requirements.txt` làm MongoDB thành dependency dù plan/README nói không bắt buộc | P5 | `/api/analyze` và app start không phụ thuộc MongoDB; bỏ hoặc cô lập endpoint ngoài lát cắt |
| `INT-P1-02` | Nút correction “Lưu” không có handler cập nhật trạng thái/taxonomy | P2 | Một low-confidence item sửa được và UI phản ánh kết quả |
| `INT-P1-03` | Prompt P3/P4 chưa xử lý đủ các review comment về prompt injection, contradiction và grounded claim | P3/P4 | Owner cập nhật prompt/test; P1 review lại |
| `INT-P1-04` | API tests chỉ chấp nhận fixture nên vẫn xanh khi pipeline chưa nối | P5 | Thêm integration tests cho ba path và một-question-fails/batch-survives |
| `INT-P1-05` | `eval/evaluate.py` còn dùng `stub_classify`; golden set chính vẫn có source/label sai đã ghi ở review Giai đoạn 2 | P5, P1 review label | Chưa chạy Run-001; phải sửa trước CP3/Giai đoạn 4 |

### P2 — backlog, không sửa khi pipeline chưa chạy

| ID | Hiện tượng | Owner | Quyết định |
|---|---|---|---|
| `INT-P2-01` | Nhiều panel/action chat, gửi phản hồi, thông báo vẫn nổi bật ngoài lát cắt | P2 | Chỉ ẩn/giảm nổi bật sau khi P0 đóng |
| `INT-P2-02` | Deprecation warning FastAPI/Starlette | P5 | Ghi backlog; không ưu tiên hơn pipeline |

## 6. Exit criteria Giai đoạn 3

| Exit criterion | Trạng thái | Bằng chứng |
|---|---|---|
| `/health` chạy | **PASS** | HTTP 200, `{"status":"ok"}` |
| `/api/analyze` trả response đúng schema từ pipeline thật | **FAIL** | Response hợp schema nhưng là fixture cố định |
| Frontend đọc được response thật | **FAIL** | API chưa thật; frontend gửi batch rỗng |
| Fixture fallback vẫn chạy | **PARTIAL PASS** | Asset HTTP 200; chưa browser smoke đầy đủ |
| Happy path demo được | **FAIL qua HTTP** | Trả fixture, không dùng input |
| Ambiguous path vào review | **FAIL qua HTTP** | Trả fixture giống happy path |
| Out-of-scope không auto-group high | **FAIL qua HTTP** | Trả fixture giống hai path còn lại |

## 7. Thứ tự tiếp tục sau báo cáo này

Không đổi contract và không làm song song các bước có phụ thuộc:

1. P5 sửa `INT-P0-01`, `INT-P0-02`, `INT-P0-03` trong file P5 sở hữu.
2. P5 chạy:
   - health/contract tests;
   - integration tests;
   - API smoke ba path.
3. P3 chỉ sửa violation/log thuộc matcher nếu smoke chỉ ra output matcher
   sai; không sửa API.
4. P4 chỉ sửa group/summary nếu supported ID/count sai; không sửa matcher.
5. P2 sửa `INT-P0-04`, giữ fallback và test loading/success/error/retry.
6. P1 chạy lại full suite và ba HTTP request.
7. Chỉ khi toàn bộ exit criteria pass, P1 đổi trạng thái Giai đoạn 3 thành
   `COMPLETE` và cho phép chuyển sang Run-001.

## 8. Lệnh tái kiểm tra bắt buộc

```powershell
.\.venv\Scripts\python.exe -m pytest backend/tests -q
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

Ngoài fixture request, bắt buộc chạy riêng happy, ambiguous và
out-of-scope request; ba response phải phản ánh đúng question ID/input,
không được cùng trả `ANL_DEMO_001`.

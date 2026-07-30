# Xác định bài toán cho AI

**Từ yêu cầu mơ hồ đến Problem Statement rõ ràng.**

> AI IN ACTION · DAY 02 — 64 slides

---

## Mở đầu

### Bốn câu hỏi trọng tâm

*Từ xác định bài toán đến quyết định ứng dụng AI*

1. Bài toán có thực sự cần AI giải quyết?
2. Nếu có, giải pháp ở cấp độ nào: Rule, Workflow, hay Agent?
3. Problem Statement đã đủ rõ ràng để triển khai?
4. Khi nào quyết định: Go, Not Yet, hay No-Go?

*(slide 02/64)*

---

### Agenda

*Mục tiêu: Biến yêu cầu mơ hồ thành Problem Statement rõ ràng để ra quyết định*

| SÁNG: KHUNG LÝ THUYẾT (4h) | CHIỀU: THỰC HÀNH LAB (4h) | BÀI NỘP CUỐI BUỔI |
|---|---|---|
| Cụ thể hóa yêu cầu mơ hồ | Cá nhân: Tìm 5 bài toán & điền 3 Problem Cards | Nhật ký tìm và lọc bài toán (Cá nhân) |
| Thấu hiểu người dùng (HCD) | Nhóm: Phản biện chéo, chốt 1 bài toán | Problem Statement hoàn chỉnh (Nhóm) |
| Đánh giá sự cần thiết của AI | Nhóm: Xác thực dữ liệu & vẽ quy trình | Nhật ký phản tư (Cá nhân) |
| Phân loại giải pháp (Rule / Workflow / Agent) | Nhóm: Xác định giải pháp & ra quyết định | |
| Hoàn thiện Problem Statement | Cá nhân: Viết nhật ký phản tư (Reflection Log) | |
| Quyết định: Go / Not Yet / No-Go | | |

*(slide 03/64)*

---

### Phát triển Sản phẩm AI (AI Product)

*Sản phẩm tích hợp AI bản chất vẫn là một sản phẩm hoàn chỉnh, kế thừa chứ không thay thế nguyên lý sản phẩm truyền thống.*

```
BUILDING AI PRODUCT
├── BUILD PRODUCT              ← Low barrier: AI tools ngày càng dễ dùng
│   [Define] → [Build] → [Test] → [Deploy]
│   ↑ AI tools boost each step ↑
└── AI INTEGRATION LAYER       ← Higher barrier: đòi hỏi mental model khác về AI
    [Understand the Model]  [UX for AI]
    [Handle Errors]         [User Expectations]
```

*(slide 04/64)*

---

### Ba trụ cột nền tảng của AI Product

*Kỹ thuật hệ thống AI · Tư duy sản phẩm · Tư duy thiết kế*

| Trụ cột | Nội dung |
|---|---|
| **AI Engineering** | Triển khai RAG, Agent, Guardrails, Evaluation (Đánh giá) và vận hành hệ thống AI thực tế. |
| **Product Thinking (Inspired)** | Xác định đúng bài toán, thấu hiểu người dùng, tránh xây dựng những tính năng không mang lại giá trị. |
| **Design Thinking (Everyday Things)** | Thiết kế dựa trên mô hình tư duy (Mental Model), cơ chế phản hồi (Feedback) và tối ưu trải nghiệm khi AI sai sót. |

**Nguồn:** Chip Huyen — *AI Engineering* · Marty Cagan — *Inspired* · Don Norman — *The Design of Everyday Things*

*(slide 05/64)*

---

### 💬 Thảo luận nhanh

> **"Tôi muốn xây dựng chatbot AI cho khách hàng."**

Theo bạn chatbot đó đang làm gì? — Viết câu trả lời lên Discord · 3 phút

*(slide 06/64)*

---

### "AI chatbot" chưa phải là một bài toán

*Đối tượng khác nhau dẫn đến quy trình (workflow), chỉ số (metrics) và rủi ro khác nhau.*

| PHỤC VỤ KHÁCH HÀNG | HỖ TRỢ NỘI BỘ |
|---|---|
| Giải đáp câu hỏi thường gặp (FAQ) về sản phẩm & chính sách | Phân loại yêu cầu hỗ trợ (Tickets/Questions) |
| Tư vấn và hỗ trợ mua hàng | Tra cứu thông tin nghiệp vụ nhanh |
| Chăm sóc sau mua hàng | Đề xuất nháp phản hồi để con người phê duyệt |
| Bán thêm & bán chéo (Upsell & Cross-sell) | Chuyển tiếp câu hỏi phức tạp hoặc rủi ro cao cho nhân sự hỗ trợ |

→ **Đối tượng khác → metric khác!**

*(slide 07/64)*

---

### Khoan đã, bạn có hỏi không?

*Cần thấu hiểu bản chất vấn đề trước khi tìm giải pháp*

- Học viên gặp khó khăn ở công đoạn nào?
- Trợ giảng quá tải ở bước nào?
- Quy trình hiện tại đang xử lý ra sao?
- Giải pháp này xây dựng phục vụ ai?

> **Chưa thấu hiểu điểm đau (pain point) thì chưa đề xuất giải pháp.**

*(slide 08/64)*

---

### 📝 Bài tập cá nhân — Nhận diện điểm đau thực tế

Từ trải nghiệm ngày học đầu tiên, liệt kê ít nhất **3 điểm đau (pain points)** bạn quan sát hoặc gặp phải.

⏱ 5 phút · Gửi lên Discord · *Bạn gặp tắc nghẽn ở đâu?*

*(slide 09/64)*

---

> ### COUNTER-INTUITIVE RULE
> **"Never solve the problem I am asked to solve."**
> — Don Norman, *The Design of Everyday Things*

*(slide 10/64)*

---

## 01 · Problem Discovery

*Tìm đúng vấn đề trước khi tìm giải pháp — Double Diamond, HCD và các kỹ thuật phân kỳ / hội tụ.*

*(slide 11/64)*

---

### Tìm đúng vấn đề trước khi tìm giải pháp

*Mô hình Double Diamond — Don Norman / British Design Council (2005)*

**Diamond 1 — Tìm đúng vấn đề**
- **Discover:** Mở rộng — khảo sát vấn đề căn bản
- **Define:** Thu hẹp — xác định đúng bài toán gốc

**Diamond 2 — Tìm đúng giải pháp**
- **Develop:** Mở rộng — nhiều giải pháp tiềm năng
- **Deliver:** Thu hẹp — chọn và triển khai

> *Kỹ sư và doanh nhân được đào tạo để **giải** vấn đề.*
> *Nhà thiết kế được đào tạo để **khám phá** vấn đề thật.*

⚠️ **Giải pháp xuất sắc cho sai vấn đề có thể còn tệ hơn không có giải pháp.**

**Nguồn:** Don Norman, JND.org · The Design of Everyday Things · Design Council — Framework for Innovation

*(slide 12/64)*

---

### Diamond 1 — Tìm đúng vấn đề

*Phân kỳ để thấu hiểu sâu sắc, Hội tụ để lựa chọn chính xác*

| DISCOVER · PHÂN KỲ — **Khám phá** *(mở rộng góc nhìn)* | DEFINE · HỘI TỤ — **Định nghĩa** *(chọn lọc dựa vào dữ liệu)* |
|---|---|
| Quan sát thực tế (Observation) | Sơ đồ đồng cảm / Gom nhóm (Affinity Mapping) |
| Phỏng vấn người dùng (User Interview) | Kỹ thuật đặt câu hỏi 5 Whys |
| Khảo sát (Survey) | Ma trận Tác động – Nỗ lực (Impact-Effort) |
| Nhật ký hành vi (Diary Study) | Biểu quyết bằng chấm tròn (Dot Voting) |
| Phân tích dữ liệu / Nhật ký hệ thống | Câu hỏi mở hướng giải quyết (How Might We) |
| Bản đồ các bên liên quan (Stakeholder Mapping) | Phát biểu bài toán (Problem Statement) |

*(slide 13/64)*

---

### Quy trình thiết kế lấy con người làm trung tâm (HCD)

*4 bước lặp lại bên trong mỗi Diamond — Don Norman*

**Observation (Quan sát)**
Những người được quan sát phải phù hợp với đối tượng mục tiêu. Quan sát khách hàng tiềm năng trong cuộc sống bình thường, hiểu các tình huống thực tế họ gặp phải.

**Ideation (Tạo ra ý tưởng)**
Tạo nhiều ý tưởng, sáng tạo không bị ràng buộc bởi các hạn chế. Tránh phê bình ý tưởng của bản thân hay người khác. Đặt câu hỏi về tất cả mọi thứ.

**Prototype (Tạo mẫu thử)**
Tạo nguyên mẫu nhanh cho mỗi giải pháp tiềm năng. Mục tiêu là kiểm tra nhanh nhất có thể trước khi build.

**Test (Kiểm tra)**
Ngồi quan sát cách người dùng tương tác với Prototype trong thực tế.

**Iteration (Lặp lại)**
Tinh chỉnh và nâng cao liên tục.

**Nguồn:** Don Norman — Design of Everyday Things · IDEO — Design Thinking · Stanford d.school

*(slide 14/64)*

---

### Những câu hỏi nguyên bản

*Đôi khi insight bắt đầu từ việc đặt câu hỏi cho những điều hiển nhiên*

| Ví dụ | Câu hỏi nguyên bản |
|---|---|
| **Isaac Newton** | Quả táo rơi xuống đất — vậy *Mặt Trăng có đang "rơi" tự do không?* |
| **Polaroid** | Tại sao *không thể xem ảnh ngay lập tức sau khi chụp?* |
| **Airbnb** | Liệu *không gian sống bỏ trống* có thể dùng làm dịch vụ lưu trú? |

> **Tò mò trước. Đánh giá sau.**

**Nguồn:** Britannica · Newton · ACS · Polaroid · Airbnb About

*(slide 15/64)*

---

### Câu hỏi gợi mở

*Đặt câu hỏi gợi mở để mở rộng tư duy trước khi lựa chọn bài toán*

- Giả định hiển nhiên nào cần được lật lại?
- Có cách tiếp cận nào hoàn toàn mới cho vấn đề?
- Nếu thiết kế lại từ đầu và không bị giới hạn?
- Tại sao bài toán này cần AI? Nếu không thì sao?
- Quy trình nào đang tồn tại chỉ vì thói quen?
- Có câu hỏi cốt lõi nào đang bị né tránh?

📤 *Gửi 1 câu hỏi phản biện lên Discord*

*(slide 16/64)*

---

### Khởi nguồn từ bài toán, không bắt đầu từ AI

*Ba bài học thực tế về am hiểu lĩnh vực, quy mô thị trường và định vị giải pháp*

| Case | Bài học |
|---|---|
| **CURSOR** — Lệch năng lực cốt lõi | Từ bỏ mảng AI thiết kế cơ khí để tập trung vào AI code editor – nơi đội ngũ am hiểu sâu sắc quy trình nghiệp vụ. |
| **ARTIFACT** — Sản phẩm tốt ≠ Thị trường lớn | Ứng dụng đọc tin tích hợp AI xuất sắc, nhưng quy mô thị trường quá hẹp để thương mại hóa thành công. |
| **NOTEBOOKLM** — Định vị đúng điểm đau | Tập trung giải quyết nhu cầu hỏi đáp, tóm tắt trên tài liệu cá nhân và đối chiếu nguồn gốc bằng trích dẫn. |

> **Lộ trình: Bài toán → Quy trình vận hành → Chỉ số đo lường → Giải pháp AI**

**Nguồn:** Forbes · Cursor · TechCrunch · Artifact · Google · NotebookLM

*(slide 17/64)*

---

### Tìm bài toán AI ở đâu? — 4 Lenses

*Bắt đầu từ việc quan sát các hoạt động thực tế xung quanh*

| Lens | Câu hỏi định hướng |
|---|---|
| **REPETITIVE** — Tác vụ lặp lại | Việc diễn ra thường xuyên; công đoạn nào cần chuẩn hóa để hướng tới tự động hóa? |
| **TIME-CONSUMING** — Tiêu tốn thời gian | Khối lượng xử lý lớn; thời gian hao phí ở bước nào (tìm kiếm, đọc hiểu, chờ đợi, định dạng)? |
| **AI ADVANTAGE** — Lợi thế của AI | Tác vụ đòi hỏi phân tích ngữ cảnh, xử lý ngôn ngữ tự nhiên, tổng hợp đa nguồn. |
| **USER PAIN POINTS** — Điểm đau người dùng | Ai đang gặp khó khăn, phàn nàn hoặc bị tắc nghẽn liên tục? |

> Tập trung nhận diện vấn đề; chưa vội đề xuất giải pháp. Sàng lọc bài toán sẽ diễn ra vào buổi chiều.

*(slide 18/64)*

---

### Sai lầm thường gặp (Anti-patterns) khi tích hợp AI

*Dấu hiệu cảnh báo bài toán chưa được định hình rõ hoặc giải pháp AI được lựa chọn quá sớm*

- **Ưu tiên giải pháp (Solution-first)** — Xây dựng chatbot/agent trước khi làm rõ quy trình vận hành và điểm nghẽn thực tế.
- **Mơ hồ hiện trạng (No baseline)** — Không lượng hóa tổn thất hiện tại, dẫn đến mất căn cứ đánh giá hiệu quả cải tiến.
- **Bỏ qua đánh giá (No evaluation)** — Không thiết lập kịch bản kiểm thử, chỉ số đo lường hoặc phương án đối chứng.
- **Mập mờ ranh giới (No boundary)** — Không rõ phạm vi tự chủ của AI và thời điểm cần con người phê duyệt (Human-in-the-loop).

> Nếu phát hiện mắc các sai lầm trên, hãy quay lại làm rõ Problem Statement trước khi chọn công nghệ.

*(slide 19/64)*

---

### Discovery interview: 5 câu hỏi nên hỏi stakeholder

1. **Vấn đề nhức nhối (Pain Point) là gì?** Tần suất lặp lại trong ngày hoặc trong tuần ra sao?
2. **Quy trình (Workflow) hiện tại như thế nào?** Công cụ nào được sử dụng ở từng bước, và ai bàn giao công việc cho ai?
3. **Thiệt hại (Cost) do vấn đề này gây ra là gì?** Hao phí cụ thể về thời gian xử lý, chi phí tài chính, cam kết dịch vụ (SLA) hay tỷ lệ chuyển đổi (conversion)?
4. **Hậu quả nếu hệ thống AI sai sót là gì?** Khâu nào cần con người tham gia kiểm soát (HITL/phê duyệt), hay AI chỉ hỗ trợ đưa ra gợi ý?
5. **Ai là người có quyền phê duyệt dự án (nói YES)?** Chỉ số hiệu quả (metric) và mức độ rủi ro (risk) nào sẽ trực tiếp quyết định việc đầu tư?

> **Lưu ý:** Nếu stakeholder không mô tả được quy trình hiện tại và chi phí thiệt hại khi xảy ra lỗi, mọi đề xuất giải pháp AI đều chỉ là phỏng đoán thiếu căn cứ.

*(slide 20/64)*

---

## 02 · Problem Statement

*Từ pain point đến Problem Statement — bài toán định hình rõ nét qua workflow, bottleneck, metrics và boundary.*

*(slide 21/64)*

---

### Quick Problem Card — Khung định hình bài toán

| Trường | Mô tả |
|---|---|
| **Bài toán (1 câu)** — `problem` | Vấn đề cụ thể cần giải quyết (không bao gồm giải pháp). |
| **Đối tượng ảnh hưởng** — `actor` | Cá nhân hoặc bộ phận chịu tác động trực tiếp từ vấn đề. |
| **Quy trình hiện tại** — `workflow` | Các bước vận hành thủ công hoặc tự động hiện tại (gồm 3–7 bước). |
| **Nút thắt & Tác động** — `bottleneck + impact` | Khâu gây chậm trễ, sai sót hoặc lặp lại; hệ quả hay tổn thất cụ thể. |
| **Chỉ số đo thành công** — `success metric` | Chỉ số định lượng cụ thể dùng để chứng minh hiệu quả cải tiến. |
| **Định hướng giải pháp** — `direction` | No AI / Rule / Workflow / Agent / Chưa xác định. |

*(slide 22/64)*

---

### Quick Problem Card — ví dụ đã điền

*Case: Weekly Report*

| Trường | Nội dung |
|---|---|
| **Bài toán** | Mỗi thứ Hai, PM mất khoảng 90 phút tổng hợp Weekly Report từ Jira, Google Sheets và Slack; bước viết narrative tốn thời gian nhất và dễ làm trễ deadline. |
| **Đối tượng ảnh hưởng** | Junior PM chịu trách nhiệm gửi weekly report cho Engineering Manager và CEO trước buổi leadership sync. |
| **Quy trình hiện tại** | Export Jira → lấy metrics từ Google Sheets → đọc Slack recap → tổng hợp vào Google Docs → viết narrative → review/format → gửi email. |
| **Nút thắt & Tác động** | Bước viết narrative từ raw data mất khoảng 25 phút. Tổng flow mất khoảng 90 phút/tuần/PM; team 3 PM tương đương khoảng 270 phút/tuần. |
| **Chỉ số đo thành công** | Giảm thời gian làm report từ 90 phút xuống dưới 30 phút, nhưng không làm tăng số câu CEO/EM phải hỏi lại. |
| **Định hướng giải pháp** | **Workflow** — tự động kéo và cấu trúc dữ liệu, AI hỗ trợ draft narrative, PM vẫn review/edit trước khi gửi. |

*(slide 23/64)*

---

### Câu hỏi khai thác bài toán

*Bộ câu hỏi định hình vấn đề dành cho các bên liên quan hoặc chính mình*

1. **Quy trình hiện tại như thế nào?** — Công cụ, các bước, cơ chế bàn giao thông tin?
2. **Nút thắt nằm ở đâu?** — Bước nào chậm, dễ sai sót, lặp lại?
3. **Hao phí hiện tại là bao nhiêu?** — Thời gian, chi phí nhân sự, SLA, cơ hội bỏ lỡ?
4. **Tiêu chí thành công đo bằng gì?** — Hiệu quả cải tiến định lượng cụ thể?
5. **Hậu quả khi xảy ra sai sót?** — Phạm vi tự quyết của AI; điểm cần con người phê duyệt?
6. **Có giải pháp phi AI đơn giản hơn?** — Quy tắc, checklist, quy trình hay tài liệu hướng dẫn?

*(slide 24/64)*

---

### Định lượng hóa bài toán

*Điểm đau chưa được định lượng thì không thể xác định giá trị thực tế của AI*

| Bước | Câu hỏi | Ví dụ |
|---|---|---|
| **01 · BASELINE** — Hiện trạng *(where we are)* | Mức hao phí hiện tại là bao nhiêu? Bằng con số cụ thể. | **Thời gian hoàn thành:** Rút ngắn từ 90 phút xuống dưới 30 phút. |
| **02 · TARGET** — Mục tiêu *(where to go)* | Kỳ vọng cải thiện ở mức độ nào? Ngưỡng cụ thể là gì? | **Chất lượng công việc:** Giảm tỷ lệ lỗi phân loại từ 20% xuống dưới 5%. |
| **03 · MEASUREMENT** — Đo lường *(how we know)* | Chỉ số nào chứng minh tính hiệu quả? Cách thu thập? | **Tải trọng vận hành:** Cắt giảm 40% câu hỏi trùng lặp cần Trợ giảng xử lý. |

*(slide 25/64)*

---

### Thiết lập chỉ số: Output & Input

*Chỉ số đo lường cần phản ánh kết quả cuối và các đòn bẩy có thể tác động*

**OUTPUT METRIC — Kết quả cuối cùng** *(what we optimize)*
- Thời lượng hoàn tất quy trình giảm bao nhiêu?
- Tỷ lệ sai sót / Chất lượng đầu ra thay đổi thế nào?
- Giá trị thực tế người dùng nhận được rõ nét hơn?

**INPUT METRICS — Các đòn bẩy** *(what we can move)*
- Tỷ lệ câu hỏi được phân loại chính xác.
- Tỷ lệ yêu cầu được chuyển tiếp hỗ trợ kịp thời.
- Thời gian Trợ giảng hiệu chỉnh bản nháp phản hồi.

→ *Tăng cái này → đo cái kia*

> **"Nâng cao hiệu suất" không phải chỉ số** — cần gắn với hiện trạng, mục tiêu và phương pháp đo.

**Nguồn:** Amplitude — North Star Framework · Lenny — Choosing Your North Star Metric

*(slide 26/64)*

---

### 📝 Bài tập nhanh — Chuyển điểm đau thành chỉ số định lượng

Lựa chọn một điểm đau đã nhận diện và thiết lập phương án đo lường cụ thể.

⏱ 5 phút · BASELINE → TARGET → MEASUREMENT

*(slide 27/64)*

---

## 03 · Có nên ứng dụng AI?

*AI chỉ thực sự mang lại giá trị khi tích hợp chính xác vào quy trình nghiệp vụ và giải quyết đúng điểm đau.*

*(slide 28/64)*

---

### Khi nào AI đáng để làm?

**AI hợp khi nào**
- Tác vụ mang tính lặp lại nhưng có độ biến thiên vừa phải.
- Yêu cầu tổng hợp hoặc tìm kiếm tri thức từ nhiều nguồn.
- Quy trình gồm nhiều bước phức tạp và cần tương tác với nhiều công cụ.
- Nếu quy trình hoàn toàn có tính xác định (deterministic), các quy tắc luật tĩnh (rule) sẽ tối ưu hơn.

**Vì sao doanh nghiệp đầu tư**
1. **Sống còn** — Bắt buộc phải tích hợp AI để duy trì lợi thế cạnh tranh trước đối thủ.
2. **Hiệu quả** — Giảm thiểu chi phí vận hành, tăng tốc độ xử lý và nâng cao năng suất nghiệp vụ.
3. **Khám phá** — Tích lũy năng lực công nghệ, tránh tụt hậu và tìm kiếm các mô hình cơ hội mới.

> Mục tiêu áp dụng AI sẽ trực tiếp quyết định phương thức xây dựng giải pháp, mức độ tự động hóa và quy mô đầu tư.

*(slide 29/64)*

---

### Tự xây dựng hay mua giải pháp?

*Hai góc nhìn bổ sung nhau giúp định hình chiến lược triển khai*

**GÓC NHÌN 1 — Chip Huyen, AI Engineering (2025)**

| In-house (Build) | Mua / SaaS (Buy) |
|---|---|
| Khi công nghệ AI là **lợi thế cạnh tranh cốt lõi** và yếu tố **sống còn** | Khi giải pháp AI đóng vai trò như một công cụ tối ưu hóa năng suất (**productivity layer**) |

**GÓC NHÌN 2 — MIT CISR (2025)**

| Buy | Boost | Build |
|---|---|---|
| Giải pháp may sẵn (off-the-shelf), do nhà cung cấp (vendor) duy trì. | Mua mô hình sẵn có và cải tiến bằng dữ liệu nội bộ. | Tự xây dựng và tối ưu mô hình tùy biến (custom model) riêng. |
| Triển khai nhanh, nhưng ít tạo ra sự khác biệt cạnh tranh. | Ứng dụng kỹ thuật tinh chỉnh (fine-tune) hoặc RAG (truy xuất nâng cao). | Khả năng kiểm soát cao nhất, nhưng chi phí đắt đỏ nhất. |
| Phụ thuộc hoàn toàn vào lộ trình (roadmap) của vendor. | Đòi hỏi năng lực quản trị dữ liệu (data governance) tốt. | Đòi hỏi đội ngũ kỹ sư AI có năng lực chuyên môn mạnh. |

> **Thực tế:** Đa số đội ngũ phát triển đang ở giữa — **Boost** (RAG / fine-tune), thay vì phải tự xây dựng lại mọi thứ từ đầu (build from scratch).

*(slide 30/64)*

---

### Thiết lập kỳ vọng

*Đo lường các chỉ số để xác định mức độ hiệu quả trước khi chính thức phát hành giải pháp*

**1 — TÁC ĐỘNG KINH DOANH** — *Giải pháp tạo giá trị gì cho doanh nghiệp?*
- ✓ Tỷ lệ tự động hóa tác vụ/yêu cầu (%).
- ✓ Quy mô xử lý lượng công việc tăng thêm.
- ✓ Tốc độ phản hồi & thời gian quy trình được tối ưu.

**2 — SỰ HÀI LÒNG KHÁCH HÀNG** — *Người dùng thực tế có thấy tốt hơn không?*
- ✓ Chỉ số hài lòng CSAT / NPS.
- ✓ Đánh giá chất lượng trực tiếp từ người dùng.
- ✓ Tỷ lệ hoàn thành tác vụ vs Tỷ lệ bỏ ngang giữa chừng.

**3 — NGƯỠNG HỮU DỤNG** — *Hệ thống đạt tiêu chí nào thì có thể phát hành?*
- ✓ Chất lượng: Độ chính xác và tính hữu ích của đầu ra.
- ✓ Độ trễ: Tốc độ phản hồi (TTFT, TPOT).
- ✓ Chi phí: Chi phí tài chính trên mỗi lượt yêu cầu.

*(slide 31/64)*

---

### Đánh giá mức độ phù hợp của AI

*Năm câu hỏi cốt lõi trước khi xác định cấp độ giải pháp (Rule / Workflow / Agent)*

1. Nghiệp vụ có đòi hỏi xử lý ngôn ngữ, tri thức chuyên môn hoặc suy luận?
2. Dữ liệu đầu vào có cung cấp đủ ngữ cảnh để AI phản hồi chính xác?
3. Đã thiết lập các chỉ số định lượng để đánh giá hiệu quả?
4. Hậu quả khi AI sai sót có nằm trong phạm vi kiểm soát?
5. Có giải pháp thay thế đơn giản và tối ưu chi phí hơn AI không?

> **Nếu phần lớn câu trả lời chưa rõ ràng → Quyết định: Not Yet.**

**Nguồn:** Google — Rules of ML · Anthropic — Building effective agents

*(slide 32/64)*

---

### Vòng đời Sản phẩm AI (AI Product Lifecycle)

*Mỗi giai đoạn từ ý tưởng đến vận hành thực tế yêu cầu phương thức xác thực chuyên biệt*

```
Start: Idea / Business Justification
  ↓
Milestone 1 — Planning & Use Case Evaluation
              • Crawl-Walk-Run  • AI Role  • Defensibility
  ↓
Milestone 2 — Expectations & Milestone Planning
              • Usefulness Thresholds  • Last Mile Illusion
  ↓
Milestone 3 — Model Selection
              • Hard Filters  • Task-Specific Evals  • Build vs. Buy
  ↓
Milestone 4 — Architecture Evolution
              Simple Prompt → Routing/Cache → Guardrails → RAG → Finetune
              (↕ Dataset Engineering — Data Flywheel)
  ↓
Milestone 5 — Evaluation-Driven Development
              • Per-Component + End-to-End  • AI as Judge
  ↓
Milestone 6 — Monitoring & Feedback Loop
              • Observability  • Explicit + Implicit Feedback
```

**Nguồn:** Chip Huyen — AI Engineering

*(slide 33/64)*

---

### Khoảng cách giữa Demo và Production

*Phản hồi chính xác trong vài lần thử chưa đủ cơ sở để triển khai hệ thống thực tế*

| Hạng mục | Câu hỏi |
|---|---|
| **BASELINE** — Thiết lập đối chứng | Đối chiếu hiệu quả với quy tắc tĩnh, nhân sự hay quy trình hiện tại? |
| **EVALUATION** — Kiểm thử hệ thống | Bộ dữ liệu kiểm thử, kịch bản biên (edge cases) và tiêu chí nghiệm thu? |
| **CONTROLS** — Cơ chế kiểm soát | Logging, fallback, rollback và nhân sự chịu trách nhiệm? |
| **OPERATIONS** — Vận hành liên tục | Ai giám sát lỗi, cập nhật tri thức nền và tối ưu hệ thống? |

> Mục tiêu Day 02 là xác định tính khả thi để tiếp tục nghiên cứu; chưa phải quyết định triển khai ngay.

**Nguồn:** Google — Rules of ML · Chip Huyen — AI Engineering

*(slide 34/64)*

---

### Hệ thống AI = Model + Context + Planning + Tools

*Một giải pháp AI thực tế là sự kết hợp của một hệ thống, không chỉ dừng lại ở mô hình ngôn ngữ*

```
                    Model (LLM · SLM)
                          ↑↓
                 [Hallucination · Cost]
                          ↕
  Context  ←→   ORCHESTRATOR / SYSTEM LOGIC   ←→   Tools
 (RAG · Memory)                                (APIs · Actions)
 [Wrong Retrieval]                        [Side Effects · Security]
                          ↕
                 [Loops · Bad Policy]
                          ↑↓
                 Planning (Steps · Policies)
```

**Nguồn:** Anthropic — Building effective agents · Chip Huyen — Agents

*(slide 35/64)*

---

### Tổng quan về Hệ thống AI

*Khái quát các thành phần cấu thành để định vị giải pháp*

| Thành phần | Vai trò |
|---|---|
| **MODEL** — Tư duy & Sáng tạo | Xử lý đọc hiểu, soạn thảo, tổng hợp, phân loại và đưa ra gợi ý. |
| **CONTEXT** — Tri thức chuyên biệt | Cơ sở dữ liệu, tài liệu nghiệp vụ, hồ sơ lịch sử giúp AI phản hồi chính xác theo bối cảnh. |
| **PLANNING** — Điều phối quy trình | Tự động phân rã tác vụ phức tạp và linh hoạt điều chỉnh. |
| **TOOLS** — Liên kết hệ thống | Tích hợp CRM, database, lịch làm việc hoặc API bên thứ ba. |

> **Tiến trình:** Lên kế hoạch → Pilot → Vận hành thực tế → Vòng lặp phản hồi. *Hôm nay tập trung vào lên kế hoạch.*

**Nguồn:** Anthropic — Building effective agents · Chip Huyen — Agents

*(slide 36/64)*

---

### Vai trò của UX trong Sản phẩm AI

*UX là chốt chặn xử lý các tình huống AI thiếu dữ liệu, độ tin cậy thấp hoặc yêu cầu phê duyệt thủ công*

**AI không cần hoàn hảo, nếu UX đỡ được chỗ nó yếu**

| Vấn đề của AI | Giải pháp UX |
|---|---|
| ❓ **Không chắc** (low confidence) | → Xin user xác nhận trước khi thực hiện |
| ❗ **Risk cao** (sai = hậu quả nghiêm trọng) | → Chỉ suggest, không auto-action |
| ☰ **Câu trả lời dài** (quá tải thông tin) | → Chia option / card / summary cho user chọn |
| ↺ **Thiếu context** (input mơ hồ) | → Hỏi lại đúng chỗ thay vì đoán sai |

> **AI Product = AI + UX.** Dùng UX để hỗ trợ chỗ AI chưa đủ tốt.

*(slide 37/64)*

---

## 04 · Rule / Workflow / Agent

*Phân tích cấp độ giải pháp. Cấp độ tối ưu là cấp độ đơn giản nhất đủ để giải quyết bài toán.*

*(slide 38/64)*

---

### Ba mức giải pháp: Rule / Workflow / Agent

| **Rule / Script** | **LLM Feature / Workflow** | **Agent** |
|---|---|---|
| *VD: Tính thuế, chặn email spam theo từ khóa, auto-reply theo template* | *VD: Tóm tắt email, chatbot FAQ, phân loại ticket hỗ trợ* | *VD: Agent nghiên cứu thị trường, coding agent sửa nhiều file* |
| Đầu vào ổn định, ít thay đổi | Đầu vào đa dạng, không viết hết rule được | Nhiều bước, dùng nhiều công cụ |
| Logic viết được thành if/else | Đầu ra cần linh hoạt (tóm tắt, dịch, phân loại) | Tình huống thay đổi liên tục |
| Cần kết quả luôn đúng 100% | Có cách đo chất lượng | Cần tự ra quyết định giữa các bước |
| Quy định pháp lý / tuân thủ chặt | Người có thể kiểm tra trước khi gửi | Có kiểm soát rủi ro rõ ràng |

> **Thứ tự ưu tiên thực dụng:** bắt đầu từ bên trái, chỉ đi sang bên phải khi giá trị tăng hơn độ phức tạp.

*(slide 39/64)*

---

### Tình huống: Tối ưu nguồn lực Trợ giảng

*Quy trình nghiệp vụ hiện tại cần được mô hình hóa trước khi cân nhắc giải pháp AI*

**Bối cảnh & Bài toán**
Lớp học số lượng học viên lớn nhưng nguồn lực Trợ giảng (TA) hạn chế. TA quá tải do rà soát thủ công các câu hỏi trùng lặp, hoặc xử lý yêu cầu hỗ trợ thiếu thông tin lỗi. **Mục tiêu:** tối ưu hóa quy trình để giảm tải cho TA và giúp học viên không bị kẹt lâu.

**Workflow hiện tại**
```
01 Học viên tắc nghẽn → 02 Gửi yêu cầu hỗ trợ → 03 Trợ giảng đọc ngữ cảnh
→ 04 Phản hồi / chuyển tiếp → 05 Học viên hiệu chỉnh
```

| | |
|---|---|
| **BOTTLENECK** | Nhiều câu hỏi trùng lặp hoặc thiếu thông tin chi tiết; Trợ giảng mất thời gian rà soát thủ công. |
| **METRICS** | Thời gian học viên chờ phản hồi, tỷ lệ câu hỏi trùng lặp, số học viên bị kẹt kéo dài. |
| **RISKS** | AI hướng dẫn sai hoặc nhầm lẫn kiến thức khiến học viên đi sai hướng thực hành. |

*(slide 40/64)*

---

### Cấp độ 1 — Giải pháp dựa trên Luật (Rule-based)

*Áp dụng khi logic nghiệp vụ tường minh, kết quả cố định và yêu cầu kiểm soát rủi ro nghiêm ngặt*

**Khi nào chọn Rule** *(when to use)*
- Logic phân nhánh rành mạch (If/Else).
- Yêu cầu hoặc trạng thái lặp lại hoàn toàn.
- Không đòi hỏi khả năng tự suy luận của AI.
- Yêu cầu kết quả có thể dự đoán và kiểm soát tuyệt đối.

**Ví dụ thực tế** *(in our context)*
- Hỏi lịch nộp bài → Tự động gửi link thời khóa biểu.
- Nộp thiếu file bài tập → Tự động nhắc nhở checklist.
- Hỏi lỗi cài đặt quen thuộc → Gửi link tài liệu hướng dẫn.
- Câu hỏi ngoài danh mục → Tự động chuyển cho Trợ giảng.

> **Giải pháp dựa trên Luật (Rule) không thua kém AI.** Nếu giải quyết triệt để bài toán, đó luôn là lựa chọn tối ưu nhất.

*(slide 41/64)*

---

### Cấp độ 2 — Giải pháp dựa trên Quy trình (Workflow)

*Các bước xử lý đã định hình rõ, nhưng từng công đoạn cần AI hỗ trợ ngôn ngữ hoặc đánh giá*

```
01 Học viên gửi Problem Card
   → 02 AI rà soát & yêu cầu bổ sung        [AI]
   → 03 Trợ giảng phê duyệt câu phức tạp    [HUMAN]
```

**Ưu điểm — Linh hoạt nhưng có kiểm soát** *(flexible + controlled)*
- Xử lý ngữ cảnh tốt hơn Rule tĩnh.
- Lộ trình của hệ thống vẫn nằm trong tầm kiểm soát.

**Lưu ý thiết kế — Tránh chatbot phản hồi tự do** *(design discipline)*
- Mỗi công đoạn phải định nghĩa rõ đầu vào và đầu ra.
- Không thiết kế thành một chatbot phản hồi tự do.

**Nguồn:** Anthropic — Building effective agents

*(slide 42/64)*

---

### Cấp độ 3 — Giải pháp dựa trên Tác nhân tự chủ (Agent)

*Hệ thống tự động lập kế hoạch, phối hợp công cụ và linh hoạt thích ứng theo tình huống*

**Khi nào dùng Agent** *(when to consider)*
- Không thể xác định trước toàn bộ các bước thực thi.
- Môi trường nhiều biến số đòi hỏi thay đổi kế hoạch linh hoạt.
- Cần tương tác với nhiều công cụ và truy xuất nhiều nguồn dữ liệu.
- Có thiết lập vòng phản hồi và chốt chặn giám sát từ con người.

**Ví dụ thực tế** *(in our context)*
- Theo dõi hoạt động thảo luận và nộp bài trên các kênh học tập.
- Phát hiện các học viên hoặc nhóm học viên bị kẹt quá lâu.
- Tự động tổng hợp vấn đề họ gặp phải và gợi ý cách hỗ trợ.
- Trợ giảng chỉ cần duyệt và nhấn nút gửi phương án hỗ trợ.

> Tác động của Agent mạnh mẽ hơn, nhưng đi kèm chi phí vận hành cao hơn, độ trễ lớn hơn, khó kiểm thử và phát sinh các dạng lỗi phức tạp.

*(slide 43/64)*

---

### Một tình huống, ba cấp độ giải pháp

*Ưu tiên giải pháp đơn giản nhất có thể giải quyết bài toán và mang lại cải tiến đo lường được*

| CẤP ĐỘ 1 · **Rule** *(luật tĩnh)*<br>TRẢ LỜI TỰ ĐỘNG | CẤP ĐỘ 2 · **Workflow** *(quy trình)*<br>DUYỆT PROBLEM CARD | CẤP ĐỘ 3 · **Agent** *(tác nhân)*<br>ĐỀ XUẤT CAN THIỆP CHỦ ĐỘNG |
|---|---|---|
| Tự động trả lời FAQ, gửi link thời khóa biểu. | AI kiểm tra độ đầy đủ của Problem Card. | Tự động theo dõi tiến độ nộp bài. |
| Gửi tài liệu sửa lỗi cài đặt cơ bản. | Yêu cầu bổ sung nếu thiếu thông tin. | Phát hiện nhóm học viên bị kẹt lâu. |
| Nhắc nhở checklist nộp bài. | Chuyển cho Trợ giảng giải quyết. | Chuẩn bị câu trả lời, đề xuất TA duyệt. |
| **Khi nào?** Logic tường minh, kết quả cố định. | **Khi nào?** Có quy trình rõ, AI hỗ trợ từng bước. | **Khi nào?** Tình huống động, đa công cụ. |

> Không bắt buộc nâng cấp tuần tự từ Rule lên Agent → **dừng ở cấp tối giản nhất** nếu đã đáp ứng mục tiêu đề ra.

*(slide 44/64)*

---

### Workflow Patterns theo Anthropic

*Khái quát các khái niệm cốt lõi phục vụ nghiên cứu và trao đổi*

**BASIC PATTERNS — Mô hình cơ bản** *(đáp ứng đa số tác vụ)*
- Prompt Chaining (Chuỗi liên kết)
- Routing (Phân luồng)
- Parallelization (Song song)

**ADVANCED PATTERNS — Mô hình nâng cao** *(khi nghiệp vụ đòi hỏi)*
- Orchestrator-Workers (Điều phối – Thực thi)
- Evaluator-Optimizer (Đánh giá – Tối ưu)

**AUTONOMOUS — Agent** *(tác nhân tự chủ)*
- LLM tự lập kế hoạch, sử dụng công cụ, quan sát phản hồi và linh hoạt điều chỉnh bước tiếp theo.

> **Nguyên tắc:** Bắt đầu bằng giải pháp đơn giản nhất; chỉ tăng độ phức tạp khi quy trình thực tế yêu cầu.

**Nguồn:** Anthropic — Building effective agents

*(slide 45/64)*

---

### Workflow patterns — đủ cho hầu hết bài toán

*Nguồn: Anthropic — Building Effective Agents (2024)*

**1. Prompt Chaining**
Chia task thành chuỗi bước tuần tự. Có gate kiểm tra giữa các bước.
```
In → LLM Call 1 → Output 1 → Gate ─(Pass)→ LLM Call 2 → Output 2 → LLM Call 3 → Out
                                └─(Fail)→ Exit
```
*VD: Viết outline → check → viết bài*

**2. Routing**
Phân loại input → đưa vào nhánh chuyên biệt. Tối ưu từng loại riêng.
```
In → LLM Call Router ─┬→ LLM Call 1 ─┐
                      ├→ LLM Call 2 ─┼→ Out
                      └→ LLM Call 3 ─┘
```
*VD: CS query → FAQ / refund / kỹ thuật*

**3. Parallelization**
Chạy song song rồi tổng hợp (sectioning), hoặc chạy nhiều lần lấy vote.
```
In ─┬→ LLM Call 1 ─┐
    ├→ LLM Call 2 ─┼→ Aggregator → Out
    └→ LLM Call 3 ─┘
```
*VD: Guardrail + response đồng thời*

> **Nguyên tắc Anthropic:** Luôn ưu tiên giải pháp đơn giản nhất; chỉ tăng độ phức tạp khi thực sự cần thiết. — 3 mô hình cơ bản trên đã đủ đáp ứng hầu hết bài toán thực tế.

*(slide 46/64)*

---

### Khi nào cần phức tạp hơn?

*Orchestrator-Workers, Evaluator-Optimizer, và Agent*

**4. Orchestrator-Workers**
1 LLM phân việc động cho workers. Subtasks không biết trước.
```
In → Orchestrator ─┬→ LLM Call 1 ─┐
                   ├→ LLM Call 2 ─┼→ Synthesizer → Out
                   └→ LLM Call 3 ─┘
```
*VD: Coding agent sửa nhiều file*

**5. Evaluator-Optimizer**
1 LLM tạo, 1 LLM đánh giá → lặp cho đến khi đạt.
```
In → LLM Call Generator → Solution → LLM Call Evaluator ─(Accepted)→ Out
        ↑                                    │
        └──────── Rejected + Feedback ───────┘
```
*VD: Dịch văn học → review → sửa*

**Agent**
LLM tự lập kế hoạch + gọi tools + iterate. Autonomous loop.
```
Human → LLM Call ⇄ Action ⇄ Environment
              ↑ Feedback / Stop
```
*VD: SWE-bench, computer use*

> *"Agents' autonomy makes them ideal for scaling tasks in trusted environments."*
> ⚠️ Chi phí vận hành cao, dễ tích tụ sai số (lỗi cộng dồn)

*(slide 47/64)*

---

### Thang câu hỏi lựa chọn cấp độ giải pháp

*Khung câu hỏi tuần tự giúp tránh bẫy "nhảy vọt" lên Agent phức tạp*

1. **Tần suất & Tác động** — Tần suất & Tác động có đủ lớn? Nếu thấp → Xử lý thủ công hoặc hiệu chỉnh quy trình nghiệp vụ trước.
2. **Logic** — Logic xử lý có rành mạch? Nếu tường minh → Ưu tiên giải pháp Rule, kịch bản tự động, danh mục kiểm tra.
3. **Quy trình** — Quy trình thực hiện có cố định? Nếu có → Xây dựng Workflow tích hợp AI hỗ trợ từng công đoạn.
4. **Tự thích ứng** — Quy trình đòi hỏi khả năng tự thích ứng linh hoạt? Chỉ khi có nhiều biến số phức tạp → Mới cân nhắc Agent.
5. **Giá trị vs Rủi ro** — Giá trị mang lại có vượt trội chi phí & rủi ro? Nếu không → Đặt chốt chặn phê duyệt (Human-in-the-loop) hoặc chọn Not Yet / No-Go.

**Nguồn:** Anthropic — Building effective agents

*(slide 48/64)*

---

### Cây quyết định: Lựa chọn cấp độ giải pháp

*Từ bài toán cốt lõi đến lựa chọn Rule, Workflow hay Agent*

```
                    [Bài Toán Của Bạn?]
                             ↓
        ┌─── KHÔNG ─── (1) Volume đủ lớn & lặp đủ thường xuyên?
        ↓                            │ CÓ
 Chưa Đáng Đầu Tư AI                 ↓
 — Giải Thủ Công Trước    ┌── CÓ ── (2) Logic rõ ràng, input ổn định?
                          ↓                    │ KHÔNG
                    RULE / Script              ↓
                                    (3) Cần nhiều bước, nhiều tool,
                                        state thay đổi?
                                         │              │
                                    KHÔNG ↓              ↓ CÓ
                          LLM Feature + Human Review   AGENT + Controls
                                                       (Risk cao? → thêm
                                                        HITL, rollback, approval)
```

**Nguồn:** Anthropic — Building effective agents · Google — Rules of ML

*(slide 49/64)*

---

### Ví dụ thực tế ngoài lớp học

*Phân biệt cấp độ giải pháp Rule, Workflow và Agent trong các tình huống thực hành*

| | Chăm sóc khách hàng | Nghiên cứu bán hàng | Kho tri thức nội bộ |
|---|---|---|---|
| **Rule** | Định tuyến phiếu hỗ trợ theo từ khoá. | Lọc khách hàng tiềm năng theo lĩnh vực, quy mô. | Phân phối chính sách theo nhu cầu tra cứu. |
| **Workflow** | Tự động soạn nháp câu trả lời có trích dẫn nguồn. | Thu thập thông tin → Tóm tắt → Soạn email tiếp cận. | Hỏi đáp dựa trên tài liệu nội bộ kèm trích dẫn nguồn. |
| **Agent** | Xử lý quy trình đa bước, truy vấn CRM, tạo yêu cầu hoàn tiền. | Giám sát tín hiệu thị trường, cập nhật CRM, đề xuất bước tiếp theo. | Giám sát thay đổi pháp lý, nhắc nhở cập nhật tài liệu. |

*(slide 50/64)*

---

### Thiết kế UX và Human-in-the-loop

*Tối ưu hóa hiệu quả của AI thông qua thiết kế giao diện tương tác phù hợp*

- **Làm rõ ý định** — Yêu cầu bổ sung ngữ cảnh hoặc làm rõ khi thông tin chưa đủ.
- **Minh bạch thông tin** — Trích dẫn nguồn lực cụ thể minh chứng cho câu trả lời.
- **Phê duyệt thủ công** — Con người kiểm duyệt trước khi thực hiện tác vụ rủi ro cao.
- **Thiết lập ranh giới** — Giới hạn phạm vi hoạt động tự chủ của AI để tránh hành vi ngoài kiểm soát.

> Dù mô hình tối ưu, thiết kế UX không phù hợp vẫn dẫn đến trải nghiệm người dùng kém hiệu quả.

*(slide 51/64)*

---

## 05 · Problem Statement hoàn chỉnh

*Liên kết chặt chẽ giữa bài toán, workflow, metrics và quyết định AI — thành đầu vào cho Eval Plan.*

*(slide 52/64)*

---

### Problem Statement cho hệ thống AI

*6 yếu tố bài toán cốt lõi và 3 yếu tố quyết định AI*

| Trường | Ý nghĩa |
|---|---|
| **Actor** *(đối tượng ảnh hưởng)* | Đối tượng trực tiếp chịu ảnh hưởng bởi vấn đề. |
| **Workflow** *(quy trình hiện tại)* | Quy trình vận hành hiện tại gồm các bước cụ thể nào? |
| **Bottleneck** *(nút thắt)* | Khâu nào gặp tình trạng chậm trễ, sai sót, lặp lại? |
| **Impact** *(tác động)* | Tổn thất lượng hóa bằng thời gian, chi phí, SLA hoặc chất lượng. |
| **Success Metric** *(chỉ số thành công)* | Chỉ số đo lường cụ thể để xác định sự cải thiện. |
| **Boundary** *(ranh giới)* | AI không được làm gì; khâu nào bắt buộc có con người. |
| **Điểm AI can thiệp** *(decision · entry)* | AI hỗ trợ hoặc tự động hóa ở bước cụ thể nào? |
| **Mức chọn** *(decision · level)* | Rule / Workflow / Agent? |
| **Rủi ro & HITL** *(decision · safety)* | Phương án xử lý khi AI sai sót và quy trình phê duyệt thủ công. |

*(slide 53/64)*

---

### Ví dụ mẫu: Hỗ trợ Lab Coach / TA

*Một Problem Statement hoàn chỉnh làm căn cứ ra quyết định*

| Trường | Nội dung |
|---|---|
| **Actor** | Lab Coach hỗ trợ các nhóm học viên trong lớp 500 người. |
| **Workflow** | Học viên đặt câu hỏi → Lab Coach nghiên cứu ngữ cảnh → Phản hồi / yêu cầu làm rõ → Học viên cập nhật bài. |
| **Bottleneck** | Câu hỏi trùng lặp hoặc thiếu thông tin nền tảng cao; Lab Coach mất thời gian phân loại thủ công. |
| **Impact** | Học viên chờ phản hồi lâu; Lab Coach quá tải, thiếu thời gian cho câu hỏi phức tạp. |
| **Success Metric** | Giảm tỷ lệ câu hỏi lặp duyệt thủ công; rút ngắn thời gian phản hồi trung bình; không tăng tỷ lệ định hướng sai. |
| **Boundary** | AI không tự đánh giá/chấm điểm bài; chỉ hỗ trợ gợi ý làm rõ và điều phối quy trình. |
| **Điểm AI can thiệp** | Ngay sau khi học viên gửi câu hỏi hoặc Problem Card thiếu thông tin ngữ cảnh. |
| **Mức chọn** | **Workflow:** AI phát hiện thông tin còn thiếu; Lab Coach phê duyệt câu hỏi chuyên sâu. |
| **Rủi ro & HITL** | AI định hướng sai → Lab Coach kiểm duyệt trước khi gửi phản hồi. |

*(slide 54/64)*

---

### Từ Problem Statement đến Eval Plan

*Problem Statement rõ ràng giúp định hình cụ thể các tiêu chí kiểm thử*

| Bước | Nội dung | Câu hỏi kiểm thử |
|---|---|---|
| **01 · INPUT** — Problem Statement | 9 trường đã hoàn chỉnh | **Tác vụ đơn lẻ:** Hệ thống có phân loại chính xác các câu hỏi đầu vào không? |
| **02 · TEST CASES** — Kịch bản kiểm thử *(data + edge cases)* | Dữ liệu thực tế và các trường hợp biên (Edge Cases). | **Hiệu năng quy trình:** Nhóm học viên có hoàn thành bài lab nhanh hơn và ít kẹt hơn không? |
| **03 · SUCCESS** — Chỉ số hiệu năng *(pass / fail / HITL)* | Đạt yêu cầu / Không đạt / Chuyển tiếp kiểm duyệt thủ công. | **Rủi ro & sai số:** Hệ thống có phản hồi sai lệch mà không chuyển tiếp cho Lab Coach phê duyệt không? |

*(slide 55/64)*

---

### Chuyển dịch từ Problem Statement sang Eval Plan

*Phương pháp đánh giá, bộ dữ liệu mẫu và ngưỡng chấp nhận*

```
[Problem Statement] → [Test Cases] → [Eval Metric] → [Architecture Boundary]
 'BÀI TOÁN LÀ GÌ'    'LÀM SAO BIẾT ĐÚNG'  'ĐO BẰNG CÁI GÌ'   'ĐƯỢC PHÉP LÀM GÌ'
  Actor                Từ mỗi field →      Ngưỡng đo lường:   Scope, HITL points,
  Workflow             suy ra câu hỏi      accuracy, latency, rollback, permissions
  Bottleneck           kiểm tra cụ thể     cost, CSAT
  Impact
  Success Metric
  Boundary
```

**Ví dụ triển khai — Agent Customer Support**

| PROBLEM STATEMENT | TEST CASES | EVAL METRIC | ARCHITECTURE BOUNDARY |
|---|---|---|---|
| **Actor:** Agent Customer Support<br>**Workflow:** Xử lý ticket tra cứu + mở thẻ<br>**Bottleneck:** Tra 4–5 hệ thống, tóm tắt lại<br>**Impact:** TB 8 phút/ticket<br>**Metric:** rớt SLA 5 phút<br>**Boundary:** AI đề xuất, agent Customer Support xác nhận | • Ticket "tra cứu giao dịch" → AI trả đúng account + trích dẫn?<br>• Ticket "mở thẻ" → AI biết giới hạn scope, chuyển human khi cần?<br>• Input không rõ intent → AI escalate, không tự trả lời? | • 80% top-5 intent xử lý < 2 phút<br>• Tỉ lệ trả lời sai không tăng<br>• Thời gian agent search giảm ≥ 50%<br>• CSAT ≥ baseline | • Chỉ ĐỀ XUẤT câu trả lời<br>• Agent Customer Support XÁC NHẬN trước khi gửi<br>• Không truy cập dữ liệu ngoài 5 hệ thống được phép<br>• Rollback: tắt AI, quay về manual 100% |

> ⚠️ **"Nếu không suy ra được 3 thứ bên phải → PS chưa đủ chất."**

*(slide 56/64)*

---

### Khung ra quyết định: Go / Not Yet / No-Go

*Lập luận dựa trên tính khả thi của Problem Statement, tránh thiên kiến công nghệ*

| ✅ **Go** *(thực hiện)*<br>ĐỦ ĐIỀU KIỆN | ⏸ **Not Yet** *(tạm hoãn)*<br>CÓ TRIỂN VỌNG | ❌ **No-Go** *(không triển khai)*<br>KHÔNG PHÙ HỢP |
|---|---|---|
| Bài toán rõ ràng. | Cần bổ sung dữ liệu thực tế. | AI không mang giá trị vượt trội. |
| Chỉ số đo lường khả thi. | Chuẩn hóa quy trình. | Rủi ro vận hành quá cao. |
| Điểm can thiệp AI phù hợp. | Thiết lập chỉ số. | Giải pháp không dùng AI tối ưu hơn. |
| Kiểm soát được rủi ro. | Xác định ranh giới. | |

> Quyết định **"Not Yet"** thể hiện sự chín chắn trong tư duy thiết kế sản phẩm, không phải sự thất bại.

*(slide 57/64)*

---

## 06 · Bài tập Lab ngày 02

*Áp dụng khung lý thuyết đã học — Scan Problem (cá nhân) → Tổng hợp & đánh giá (nhóm) → Quyết định.*
*(40% cá nhân + 60% nhóm)*

Hướng dẫn làm bài → `github.com/VinUni-AI20k/Day02-AI-Product-Labs`

*(slide 58/64)*

---

### Tổng quan bài Lab: Deliverables

*Lộ trình 4 giờ: Cá nhân → Nhóm → Problem Statement → Quyết định AI*

**CÁ NHÂN · PROBLEM SCAN**

| Phase | Thời lượng | Deliverable |
|---|---|---|
| **Phase 0** — Worked Example | 15 phút | Hiểu một bài mẫu hoàn chỉnh |
| **Phase 1** — Individual Scan | 25 phút | 5+ problem candidates từ trải nghiệm thật |
| **Phase 2** — Top 3 Problem Cards | 35 phút | 3 Problem Cards + draft workflow trước/sau |

**NHÓM · DEEP DIVE**

| Phase | Thời lượng | Deliverable |
|---|---|---|
| **Phase 3** — Group Convergence | 30 phút | 1 candidate problem được nhóm chọn<br>*AI rule: không dùng AI để pitch/challenge thay mình* |
| **Phase 4** — Validation + Research | 30 phút | Tín hiệu kiểm chứng + research giải pháp đã có |
| **Phase 5** — Workflow + Problem Statement | 45 phút | Workflow trước/sau + Problem Statement v0 |
| **Phase 6** — Rule / Workflow / Agent + Decision | 25 phút | PS v1 + Go / Not Yet / No-Go |

**CÁ NHÂN · REFLECTION**

| Phase | Thời lượng | Deliverable |
|---|---|---|
| **Phase 7** — Individual Reflection | 15 phút | Reflection cá nhân về vai trò, cách dùng AI, bài học<br>*AI rule: không dùng AI viết thay reflection* |

**Cấu trúc nộp bài**
```
public repo Day02-MãHọcViên-HọVàTên
├── 01-individual-problem-scan/
├── 02-group-problem-statement/
└── 03-individual-reflection/
```

*(slide 59/64)*

---

### Giai đoạn 1 & 2: Phân kỳ và Hội tụ Cá nhân

*Khảo sát tối thiểu 5 bài toán thực tế, lựa chọn top 3 Problem Cards tối ưu*

**Double Diamond Framework**
```
       TÌM ĐÚNG BÀI TOÁN                 GIẢI ĐÚNG BÀI TOÁN
  ┌──────────◇──────────┐          ┌──────────◇──────────┐
 DIVERGE          CONVERGE        DIVERGE          CONVERGE
 Phase 1 —        Phase 2 —    → 1 bài toán →  Phase 4 —       Phase 5 —
 Scan: Khảo sát   Quick-assess    được chọn    Deep-dive:      Evaluate
 8+ ý tưởng                                    1 ý tưởng
                      Phase 3 — Pitch · Challenge · Vote      Phase 6 — Reflection
```

**Nguồn:** Design Council — Framework for Innovation

*(slide 60/64)*

---

### Hướng dẫn xây dựng Workflow Diagram

*Phân tích chuyên sâu: Current-State và Future-State*

Mỗi bước ghi rõ: **Tên bước**, **Actor**, **⏱ thời gian (phút)**, **In**, **Out** — bố trí theo swimlane cho từng người thực hiện (A, B, ...).

**Ký hiệu**
- 🔴 = Nút thắt (bước chậm nhất hoặc hay xảy ra lỗi)
- ↻ = Bàn giao (điểm chuyển giao giữa người / hệ thống)
- 🕐 = Thời gian (ghi cụ thể, ví dụ: 15 phút)

**Checklist**
- ☑ Tối thiểu 5–8 bước (đừng gộp quá)
- ☑ Mỗi bước có thời gian cụ thể
- ☑ Ít nhất 1 nút thắt được đánh dấu
- ☑ Ghi tổng thời gian của workflow
- ☑ Vẽ trên giấy, không gõ text

*(slide 61/64)*

---

### Worked Example: Báo cáo tuần trước và sau AI

*Current-State, Future-State, Ranh giới kiểm soát và Fallback*

**Weekly Report — 7 bước, 90 phút → 5 bước, 21 phút**

**CURRENT STATE 🕐 90 phút**

| # | Bước | Thời gian | Actor |
|---|---|---|---|
| ① | Export Jira | 10 phút | PM |
| ② | Lấy metrics | 10 phút | PM |
| ③ | Đọc Slack | 15 phút | PM |
| ④ | Tổng hợp | 15 phút | PM |
| ⑤ | 🔴 **Viết narrative** *(BOTTLENECK 25')* | 25 phút | PM |
| ⑥ | Review | 10 phút | PM |
| ⑦ | Gửi | 5 phút | PM |

**FUTURE STATE 🕐 21 phút**

| # | Bước | Thời gian | Ghi chú |
|---|---|---|---|
| ① | Auto-pull | 2' | |
| ② | AI cấu trúc | 1' | |
| ③ | AI draft | 1' | *Fallback: AI draft tệ → PM tự viết lại* |
| ④ | **PM review + edit** | 15' | 🚧 **Boundary** |
| ⑤ | PM gửi | 2' | |

| Tiêu chí | Trước | Sau | Thay đổi |
|---|---|---|---|
| Tổng thời gian | 90 phút | 21 phút | **−77% ▼** |
| Bước thủ công | 7/7 thủ công | 2/5 thủ công | — |
| Bottleneck mới | — | Review | ✅ |

*(slide 62/64)*

---

### Sản phẩm bàn giao sau buổi Lab — Deliverables

```
public repo Day02-MãHọcViên-HọVàTên
├── 01-individual-problem-scan/
├── 02-group-problem-statement/
└── 03-individual-reflection/
```

| # | Loại | Nội dung |
|---|---|---|
| **01 · CÁ NHÂN** | Individual Problem Scan | Khảo sát tối thiểu 5 bài toán thực tế, chọn top 3 Problem Cards và phác thảo quy trình trước/sau tối ưu cho cả 3 bài. |
| **02 · NHÓM** | Group Problem Statement | Nhật ký hội tụ, kết quả khảo sát, sơ đồ workflow trước/sau, Problem Statement v0/v1, lập luận chọn cấp độ và quyết định cuối. |
| **03 · CÁ NHÂN** | Individual Reflection | Vai trò cá nhân trong nhóm, phương thức dùng AI hỗ trợ, bài học kinh nghiệm và đề xuất cải tiến. |

**Hướng dẫn làm bài →** `github.com/VinUni-AI20k/Day02-AI-Product-Labs`

*(slide 63/64)*

---

## Recap · Năm nguyên tắc cốt lõi sau Day 02

*Kim chỉ nam để thẩm định mọi đề xuất ứng dụng AI*

1. **Brief mơ hồ không thay thế Problem Statement.**
   Một bản tóm tắt mơ hồ không thể thay thế cho một Problem Statement hoàn chỉnh.

2. **Mô hình hóa workflow trước khi tích hợp AI.**
   Bắt buộc phải mô hình hóa quy trình trước khi xem xét tích hợp giải pháp AI.

3. **Pain point phải được lượng hóa.**
   Mọi điểm đau cần được lượng hóa bằng baseline và chỉ số đo lường cụ thể.

4. **Phức tạp không đồng nghĩa với hiệu quả.**
   Rule, Workflow và Agent là ba cấp độ khác nhau; độ phức tạp kỹ thuật không đồng nghĩa với hiệu quả tối ưu.

5. **Quyết định dựa trên lập luận thực tế.**
   Quyết định Go / Not Yet / No-Go phải được thiết lập dựa trên lập luận thực tế và số liệu kiểm thử rõ ràng.

*(slide 64/64)*

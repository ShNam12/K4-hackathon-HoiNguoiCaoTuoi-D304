# AI IN ACTION · DAY 02 — Xác định bài toán cho AI

> **Từ yêu cầu mơ hồ đến Problem Statement rõ ràng.**
> Instructor: **Mai Anh Nguyen (Blue)** — *Generalist Product Builder*
> Tổng: 76 slides

---

## Mục lục

- [Mở đầu](#mở-đầu)
- [Section 01 — Problem Discovery](#section-01--problem-discovery)
- [Section 02 — Problem Statement](#section-02--problem-statement)
- [Section 03 — Có nên ứng dụng AI?](#section-03--có-nên-ứng-dụng-ai)
- [Section 04 — Rule / Workflow / Agent](#section-04--rule--workflow--agent)
- [Section 05 — Problem Statement hoàn chỉnh](#section-05--problem-statement-hoàn-chỉnh)
- [Recap — 6 nguyên tắc](#recap--sáu-nguyên-tắc-cốt-lõi-sau-day-02)
- [Appendix](#appendix--đọc-thêm)

---

# MỞ ĐẦU

## Slide 02 — Instructor

**Mai Anh Nguyen (Blue)** — *Generalist Product Builder*

| Năm | Vị trí |
|---|---|
| 2026 | FPT Long Châu (PM · Healthcare Product) |
| 2025 | Thongtincuuho.org (Co-founder) |
| 2025 | FPT Software AI Center (PM · AI Agent) |
| 2021–2025 | Xantus (PM · On-chain Analytics, AI Agent) |
| 2016–2021 | DYNO, Kalapa (PM · OCR, eKYC, Credit Scoring) |

Liên hệ: LinkedIn | Facebook

---

## Slide 03 — Bốn câu hỏi trọng tâm

*Từ xác định bài toán đến quyết định ứng dụng AI*

1. Bài toán có thực sự cần AI giải quyết?
2. Nếu có, giải pháp ở cấp độ nào: **Rule, Workflow, hay Agent**?
3. Problem Statement đã đủ rõ ràng để triển khai?
4. Khi nào quyết định: **Go, Not Yet, hay No-Go**?

---

## Slide 04 — Agenda

**Mục tiêu:** Biến yêu cầu mơ hồ thành Problem Statement rõ ràng để ra quyết định.

### SÁNG — Khung lý thuyết (4h)
- Problem Discovery (Double Diamond, HCD)
- Problem Statement & định lượng hóa
- PAIR ① AI có thêm giá trị?
- PAIR ② Automate/Augment → Rule/Workflow/Agent
- PAIR ③ Reward function & success criteria
- Khi AI sai & UX/HITL
- PS hoàn chỉnh → Go/Not Yet/No-Go

### CHIỀU — Thực hành Lab (4h)
- **Cá nhân:** Tìm 5 bài toán & điền 3 Problem Cards
- **Nhóm:** Phản biện chéo, chốt 1 bài toán
- **Nhóm:** Xác thực dữ liệu & vẽ quy trình
- **Nhóm:** Xác định giải pháp & ra quyết định
- **Cá nhân:** Viết nhật ký phản tư (Reflection Log)

### BÀI NỘP cuối buổi
- Nhật ký tìm và lọc bài toán *(Cá nhân)*
- Problem Statement hoàn chỉnh *(Nhóm)*
- Nhật ký phản tư *(Cá nhân)*

---

## Slide 05 — Nguyên tắc tương tác & Thực hành

1. **Thảo luận nhanh qua Discord** — Gửi phản hồi ngắn, câu hỏi nhanh hoặc ý kiến phản biện trực tiếp lên Discord.
2. **Khuyến khích chia sẻ ý tưởng sơ khởi** — Ý tưởng không cần hoàn hảo ngay từ đầu; các câu trả lời chưa sâu sẽ là chất liệu để cùng phân tích.
3. **Nộp sản phẩm qua GitHub** — Báo cáo thực hành Bài tập Lab ngày 02 được nộp trực tiếp trên GitHub Repository.

> Điểm thưởng (Bonus) dành cho học viên tích cực tương tác.

---

## Slide 06 — Phát triển Sản phẩm AI (AI Product)

*Sản phẩm tích hợp AI bản chất vẫn là một sản phẩm hoàn chỉnh, kế thừa chứ không thay thế nguyên lý sản phẩm truyền thống.*

```
┌───────────────────── BUILDING AI PRODUCT ─────────────────────┐
│                                                               │
│   ┌──────────────── BUILD PRODUCT ────────────────┐           │
│   │  [Define] → [Build] → [Test] → [Deploy]       │  Low barrier —
│   │        ↑ AI tools boost each step ↑           │  AI tools ngày càng dễ dùng
│   └───────────────────────────────────────────────┘           │
│                                                               │
│   ┌────────────── AI Integration Layer ───────────┐           │
│   │  [Understand the Model]   [UX for AI]         │  Higher barrier —
│   │  [Handle Errors]          [User Expectations] │  cần mental model khác về AI
│   └───────────────────────────────────────────────┘           │
└───────────────────────────────────────────────────────────────┘
```

---

## Slide 07 — Ba trụ cột nền tảng của AI Product

*Kỹ thuật hệ thống AI · Tư duy sản phẩm · Tư duy thiết kế*

| Trụ cột | Nội dung |
|---|---|
| **AI Engineering** | Triển khai RAG, Agent, Guardrails, Evaluation (Đánh giá) và vận hành hệ thống AI thực tế. |
| **Product Thinking (Inspired)** | Xác định đúng bài toán, thấu hiểu người dùng, tránh xây dựng những tính năng không mang lại giá trị. |
| **Design Thinking (Everyday Things)** | Thiết kế dựa trên mô hình tư duy (Mental Model), cơ chế phản hồi (Feedback) và tối ưu trải nghiệm khi AI sai sót. |

**Nguồn:** Chip Huyen — *AI Engineering* (O'Reilly, 2025) · Marty Cagan — *Inspired* (2nd ed.) · Don Norman — jnd.org

---

## Slide 08 — Tài liệu xuyên suốt buổi học

### Sách giáo khoa hôm nay · Google PAIR — *People + AI Guidebook*
6 chương — cẩm nang thiết kế sản phẩm AI lấy con người làm trung tâm:

1. User Needs + Defining Success
2. Data Collection + Evaluation
3. Mental Models
4. Explainability + Trust
5. Feedback + Control
6. Errors + Graceful Failure

> **Chương 1 — User Needs + Defining Success** là xương sống buổi sáng nay (PAIR ①②③).

### Đọc thêm
- **Anthropic — Building effective agents:** Chọn giải pháp đơn giản nhất: rule/workflow trước, agent chỉ khi thật sự cần — dùng ở PAIR ②.
- **Google — Rules of Machine Learning:** Các quy tắc thực chiến của Google: giải pháp đơn giản (rule, heuristic) trước, ML sau.

---

## Slide 09 — Thảo luận nhanh

> *"Tôi muốn xây dựng chatbot AI cho khách hàng."*

**Theo bạn chatbot đó đang làm gì?** — Viết câu trả lời lên Discord · 3 phút

---

## Slide 10 — "AI chatbot" chưa phải là một bài toán

*Đối tượng khác nhau dẫn đến quy trình (workflow), chỉ số (metrics) và rủi ro khác nhau.*

### Phục vụ khách hàng
- Giải đáp câu hỏi thường gặp (FAQ) về sản phẩm & chính sách
- Tư vấn và hỗ trợ mua hàng
- Chăm sóc sau mua hàng
- Bán thêm & bán chéo (Upsell & Cross-sell)

### Hỗ trợ nội bộ
- Phân loại yêu cầu hỗ trợ (Tickets/Questions)
- Tra cứu thông tin nghiệp vụ nhanh
- Đề xuất nháp phản hồi để con người phê duyệt
- Chuyển tiếp câu hỏi phức tạp hoặc rủi ro cao cho nhân sự hỗ trợ

> **Đối tượng khác → metric khác!**

---

## Slide 11 — Tình huống thực tế

> Lớp học 1000 học viên (khóa K3 & K4), số lượng Trợ giảng có hạn.
> **Dùng AI giải quyết thế nào?**

Viết câu trả lời lên Discord — 5 phút

---

## Slide 12 — Khoan đã, bạn có hỏi không?

*Cần thấu hiểu bản chất vấn đề trước khi tìm giải pháp.*

- Học viên gặp khó khăn ở công đoạn nào?
- Trợ giảng quá tải ở bước nào?
- Quy trình hiện tại đang xử lý ra sao?
- Giải pháp này xây dựng phục vụ ai?

> **Chưa thấu hiểu điểm đau (pain point) thì chưa đề xuất giải pháp.**

---

## Slide 13 — Bài tập cá nhân: Nhận diện điểm đau thực tế

Từ trải nghiệm ngày học đầu tiên, liệt kê ít nhất **3 điểm đau (pain points)** bạn quan sát hoặc gặp phải.

*5 phút · Gửi lên Discord · Bạn gặp tắc nghẽn ở đâu?*

---

## Slide 14 — Counter-intuitive rule

> ### "Do not solve the problem I am asked to solve."
> — **Don Norman** · jnd.org

---

# SECTION 01 — Problem Discovery

*Tìm đúng vấn đề trước khi tìm giải pháp — Double Diamond, HCD và các kỹ thuật phân kỳ / hội tụ.*

## Slide 16 — Tìm đúng vấn đề trước khi tìm giải pháp

*Mô hình Double Diamond — Don Norman / British Design Council (2005)*

```
   FINDING THE RIGHT              FINDING THE RIGHT
       PROBLEM                        SOLUTION
        ◇                               ◇
   ●─────────────●───────────────────────────●
 Divergence  Convergence   Divergence   Convergence
 ────────────────────── TIME ──────────────────────►
```

**Diamond 1 — Tìm đúng vấn đề**
- **Discover:** Mở rộng — khảo sát vấn đề căn bản.
- **Define:** Thu hẹp — xác định đúng bài toán gốc.

**Diamond 2 — Tìm đúng giải pháp**
- **Develop:** Mở rộng — nhiều giải pháp tiềm năng.
- **Deliver:** Thu hẹp — chọn và triển khai.

> *"Kỹ sư và doanh nhân được đào tạo để **giải** vấn đề. Nhà thiết kế được đào tạo để **khám phá** vấn đề thật."*

> ⚠️ **Giải pháp xuất sắc cho sai vấn đề có thể còn tệ hơn không có giải pháp.**

**Nguồn:** Don Norman — jnd.org · Design Council — The Double Diamond

---

## Slide 17 — Diamond 1: Tìm đúng vấn đề

*Phân kỳ để thấu hiểu sâu sắc, hội tụ để lựa chọn chính xác.*

| DISCOVER · Phân kỳ (khám phá / mở rộng góc nhìn) | DEFINE · Hội tụ (định nghĩa / chọn lọc dựa vào dữ liệu) |
|---|---|
| Quan sát thực tế (Observation) | Sơ đồ đồng cảm / Gom nhóm (Affinity Mapping) |
| Phỏng vấn người dùng (User Interview) | Kỹ thuật đặt câu hỏi 5 Whys |
| Khảo sát (Survey) | Ma trận Tác động – Nỗ lực (Impact-Effort) |
| Nhật ký hành vi (Diary Study) | Biểu quyết bằng chấm tròn (Dot Voting) |
| Phân tích dữ liệu / Nhật ký hệ thống | Câu hỏi mở hướng giải quyết (How Might We) |
| Bản đồ các bên liên quan (Stakeholder Mapping) | Phát biểu bài toán (Problem Statement) |

---

## Slide 18 — Quy trình HCD

*Thiết kế lấy con người làm trung tâm: vòng lặp 5 bước bên trong mỗi Diamond*

`EMPATHIZE → DEFINE → IDEATE → PROTOTYPE → TEST → (lặp lại)`

- **Observation (Quan sát):** Người được quan sát phải phù hợp với đối tượng mục tiêu — quan sát khách hàng tiềm năng trong cuộc sống bình thường, hiểu các tình huống thực tế họ gặp phải.
- **Ideation (Tạo ra ý tưởng):** Tạo nhiều ý tưởng, sáng tạo không bị ràng buộc bởi các hạn chế. Tránh phê bình ý tưởng của bản thân hay người khác. Đặt câu hỏi về tất cả mọi thứ.
- **Prototype (Tạo mẫu thử):** Tạo nguyên mẫu nhanh cho mỗi giải pháp tiềm năng — mục tiêu là kiểm tra nhanh nhất có thể trước khi build.
- **Test (Kiểm tra):** Ngồi quan sát cách người dùng tương tác với Prototype trong thực tế.
- **Iteration (Lặp lại):** Tinh chỉnh và nâng cao liên tục.

**Nguồn:** Don Norman — jnd.org · IDEO — Design Kit · Stanford d.school

---

## Slide 19 — Những câu hỏi nguyên bản

*Đôi khi insight bắt đầu từ việc đặt câu hỏi cho những điều hiển nhiên.*

| Chủ thể | Câu hỏi nguyên bản |
|---|---|
| **Isaac Newton** | Quả táo rơi xuống đất — vậy Mặt Trăng có đang "rơi" tự do không? |
| **Polaroid** | Tại sao không thể xem ảnh ngay lập tức sau khi chụp? |
| **Airbnb** | Liệu không gian sống bỏ trống có thể dùng làm dịch vụ lưu trú? |

> **Tò mò trước. Đánh giá sau.**

**Nguồn:** Britannica — Gravity · ACS — Edwin Land & Instant Photography · Airbnb — About us

---

## Slide 20 — Bài tập cá nhân

> Bạn có câu hỏi nào mà cảm thấy "ngớ ngẩn" không?

Viết lên Discord — 3 phút

---

## Slide 21 — Câu hỏi gợi mở · BỘ THẺ CÂU HỎI #1 — PHÂN KỲ

*Đặt câu hỏi gợi mở để mở rộng tư duy trước khi lựa chọn bài toán.*

1. Giả định hiển nhiên nào cần được lật lại?
2. Có cách tiếp cận nào hoàn toàn mới cho vấn đề?
3. Nếu thiết kế lại từ đầu và không bị giới hạn?
4. Tại sao bài toán này cần AI? Nếu không thì sao?
5. Quy trình nào đang tồn tại chỉ vì thói quen?
6. Có câu hỏi cốt lõi nào đang bị né tránh?

> Gửi 1 câu hỏi phản biện lên Discord.

---

## Slide 22 — Khởi nguồn từ bài toán, không bắt đầu từ AI

*Ba bài học thực tế về am hiểu lĩnh vực, quy mô thị trường và định vị giải pháp.*

| Case | Bài học | Nội dung |
|---|---|---|
| **Cursor** | "Lệch năng lực cốt lõi" | Từ bỏ mảng AI thiết kế cơ khí (CAD) để tập trung vào AI code editor — nơi đội ngũ am hiểu sâu sắc quy trình nghiệp vụ. |
| **Artifact** | "Sản phẩm tốt ≠ Thị trường lớn" | Ứng dụng đọc tin tích hợp AI xuất sắc, nhưng quy mô thị trường quá hẹp để thương mại hóa thành công (đóng cửa 1/2024). |
| **NotebookLM** | "Định vị đúng điểm đau" | Tập trung giải quyết nhu cầu hỏi đáp, tóm tắt trên tài liệu cá nhân và đối chiếu nguồn gốc bằng trích dẫn. |

> **Lộ trình:** Bài toán → Quy trình vận hành → Chỉ số đo lường → Giải pháp AI

**Nguồn:** Lenny's Podcast — The rise of Cursor · The Verge — Artifact · Google Blog — NotebookLM

---

## Slide 23 — Tìm bài toán AI ở đâu? (4 Lenses)

*Bắt đầu từ việc quan sát các hoạt động thực tế xung quanh.*

| Lens | Câu hỏi soi chiếu |
|---|---|
| **Repetitive** — Tác vụ lặp lại | Việc diễn ra thường xuyên; công đoạn nào cần chuẩn hóa để hướng tới tự động hóa? |
| **Time-consuming** — Tiêu tốn thời gian | Khối lượng xử lý lớn; thời gian hao phí ở bước nào (tìm kiếm, đọc hiểu, chờ đợi, định dạng)? |
| **AI Advantage** — Lợi thế của AI | Tác vụ đòi hỏi phân tích ngữ cảnh, xử lý ngôn ngữ tự nhiên, tổng hợp đa nguồn. |
| **User Pain Points** — Điểm đau người dùng | Ai đang gặp khó khăn, phàn nàn hoặc bị tắc nghẽn liên tục? |

> Tập trung nhận diện vấn đề; chưa vội đề xuất giải pháp. Sàng lọc bài toán sẽ diễn ra vào buổi chiều.

---

## Slide 24 — Sai lầm thường gặp (Anti-patterns)

*Dấu hiệu cảnh báo bài toán chưa được định hình rõ hoặc giải pháp AI được lựa chọn quá sớm.*

- **Ưu tiên giải pháp (Solution-first):** Xây dựng chatbot/agent trước khi làm rõ quy trình vận hành và điểm nghẽn thực tế.
- **Mơ hồ hiện trạng (No baseline):** Không lượng hóa tổn thất hiện tại, dẫn đến mất căn cứ đánh giá hiệu quả cải tiến.
- **Bỏ qua đánh giá (No evaluation):** Không thiết lập kịch bản kiểm thử, chỉ số đo lường hoặc phương án đối chứng.
- **Mập mờ ranh giới (No boundary):** Không rõ phạm vi tự chủ của AI và thời điểm cần con người phê duyệt (Human-in-the-loop).

> Nếu phát hiện mắc các sai lầm trên, hãy quay lại làm rõ Problem Statement trước khi chọn công nghệ.

---

## Slide 25 — Discovery interview: 5 câu hỏi nên hỏi stakeholder

*BỘ THẺ CÂU HỎI #2 — PHỎNG VẤN*

1. **Vấn đề nhức nhối (Pain Point)** là gì? Tần suất lặp lại trong ngày hoặc trong tuần ra sao?
2. **Quy trình (Workflow)** hiện tại như thế nào? Công cụ nào được sử dụng ở từng bước, và ai bàn giao công việc cho ai?
3. **Thiệt hại (Cost)** do vấn đề này gây ra là gì? Hao phí cụ thể về thời gian xử lý, chi phí tài chính, cam kết dịch vụ (SLA) hay tỷ lệ chuyển đổi (conversion)?
4. **Hậu quả nếu hệ thống AI sai sót** là gì? Khâu nào cần con người tham gia kiểm soát (HITL/phê duyệt), hay AI chỉ hỗ trợ đưa ra gợi ý?
5. **Ai là người có quyền phê duyệt dự án (nói YES)?** Chỉ số hiệu quả (metric) và mức độ rủi ro (risk) nào sẽ trực tiếp quyết định việc đầu tư?

> **Lưu ý:** Nếu đối tác (stakeholder) không mô tả được quy trình hiện tại và chi phí thiệt hại khi xảy ra lỗi, mọi đề xuất giải pháp AI đều chỉ là phỏng đoán thiếu căn cứ.

---

## Slide 26 — PAIR Chương 1: Reframe câu hỏi

> ~~"Can we use AI to \_\_\_\_\_\_?"~~
>
> ↓ thay bằng hai câu hỏi ↓
>
> 1. **"How might we solve \_\_\_\_\_\_?"**
> 2. **"Can AI solve this problem in a unique way?"**

Hỏi về bài toán trước, về AI sau — AI chỉ là một phương án trong nhiều phương án khả dĩ.

> Câu hỏi đúng quyết định bài toán bạn giải — và giải pháp bạn chọn.

**Nguồn:** Google PAIR — Ch.1 User Needs + Defining Success

---

# SECTION 02 — Problem Statement

*Từ pain point đến Problem Statement — bài toán định hình rõ nét qua workflow, bottleneck, metrics và boundary.*

## Slide 28 — Quick Problem Card (khung định hình bài toán)

| Trường | Mã | Mô tả |
|---|---|---|
| Bài toán (1 câu) | `problem` | Vấn đề cụ thể cần giải quyết (không bao gồm giải pháp). |
| Đối tượng ảnh hưởng | `actor` | Cá nhân hoặc bộ phận chịu tác động trực tiếp từ vấn đề. |
| Quy trình hiện tại | `workflow` | Các bước vận hành thủ công hoặc tự động hiện tại (gồm 3–7 bước). |
| Nút thắt & Tác động | `bottleneck + impact` | Khâu gây chậm trễ, sai sót hoặc lặp lại; hệ quả hay tổn thất cụ thể. |
| Chỉ số đo thành công | `success metric` | Chỉ số định lượng cụ thể dùng để chứng minh hiệu quả cải tiến. |
| Định hướng giải pháp | `direction` | No AI / Rule / Workflow / Agent / Chưa xác định. |

---

## Slide 29 — Quick Problem Card — ví dụ đã điền

**Case: Weekly Report**

| Trường | Nội dung |
|---|---|
| **Bài toán** | Mỗi thứ Hai, PM mất khoảng 90 phút tổng hợp Weekly Report từ Jira, Google Sheets và Slack; bước viết narrative tốn thời gian nhất và dễ làm trễ deadline. |
| **Đối tượng** | Junior PM chịu trách nhiệm gửi weekly report cho Engineering Manager và CEO trước buổi leadership sync. |
| **Quy trình** | Export Jira → lấy metrics từ Google Sheets → đọc Slack recap → tổng hợp vào Google Docs → viết narrative → review/format → gửi email. |
| **Nút thắt** | Bước viết narrative từ raw data mất khoảng 25 phút. Tổng flow mất khoảng 90 phút/tuần/PM; team 3 PM tương đương khoảng 270 phút/tuần. |
| **Chỉ số** | Giảm thời gian làm report từ 90 phút xuống dưới 30 phút, nhưng không làm tăng số câu CEO/EM phải hỏi lại. |
| **Định hướng** | **Workflow** — tự động kéo và cấu trúc dữ liệu, AI hỗ trợ draft narrative, PM vẫn review/edit trước khi gửi. |

---

## Slide 30 — Câu hỏi khai thác bài toán · BỘ THẺ CÂU HỎI #3 — CẤU TRÚC PS

*Bộ câu hỏi định hình vấn đề dành cho các bên liên quan hoặc chính mình.*

1. **Quy trình hiện tại như thế nào?** Công cụ, các bước, cơ chế bàn giao thông tin?
2. **Nút thắt nằm ở đâu?** Bước nào chậm, dễ sai sót, lặp lại?
3. **Hao phí hiện tại là bao nhiêu?** Thời gian, chi phí nhân sự, SLA, cơ hội bỏ lỡ?
4. **Tiêu chí thành công đo bằng gì?** Hiệu quả cải tiến định lượng cụ thể?
5. **Hậu quả khi xảy ra sai sót?** Phạm vi tự quyết của AI; điểm cần con người phê duyệt?
6. **Có giải pháp phi AI đơn giản hơn?** Quy tắc, checklist, quy trình hay tài liệu hướng dẫn?

---

## Slide 31 — Định lượng hóa bài toán

*Điểm đau chưa được định lượng thì không thể xác định giá trị thực tế của AI.*

| Bước | Nội dung |
|---|---|
| **01 · Baseline** — Hiện trạng / *where we are* | Mức hao phí hiện tại là bao nhiêu? Bằng con số cụ thể. |
| **02 · Target** — Mục tiêu / *where to go* | Kỳ vọng cải thiện ở mức độ nào? Ngưỡng cụ thể là gì? |
| **03 · Measurement** — Đo lường / *how we know* | Chỉ số nào chứng minh tính hiệu quả? Cách thu thập? |

**Ví dụ:**
- *Thời gian hoàn thành:* Rút ngắn từ 90 phút xuống dưới 30 phút.
- *Chất lượng công việc:* Giảm tỷ lệ lỗi phân loại từ 20% xuống dưới 5%.
- *Tải trọng vận hành:* Cắt giảm 40% câu hỏi trùng lặp cần Trợ giảng xử lý.

---

## Slide 32 — Thiết lập chỉ số: Output & Input

*Chỉ số đo lường cần phản ánh kết quả cuối và các đòn bẩy có thể tác động.*

### Output Metric — Kết quả cuối cùng / *what we optimize*
- Thời lượng hoàn tất quy trình giảm bao nhiêu?
- Tỷ lệ sai sót / chất lượng đầu ra thay đổi thế nào?
- Giá trị thực tế người dùng nhận được rõ nét hơn?

### Input Metrics — Các đòn bẩy / *what we can move*
- Tỷ lệ câu hỏi được phân loại chính xác.
- Tỷ lệ yêu cầu được chuyển tiếp hỗ trợ kịp thời.
- Thời gian Trợ giảng hiệu chỉnh bản nháp phản hồi.

> *Tăng cái này → đo cái kia.*

> ⚠️ **"Nâng cao hiệu suất" không phải chỉ số** — cần gắn với hiện trạng, mục tiêu và phương pháp đo.

**Nguồn:** Amplitude — North Star Playbook · Lenny Rachitsky — Choosing Your North Star Metric

---

## Slide 33 — Bài tập nhanh

> Lựa chọn một điểm đau đã nhận diện và thiết lập phương án đo lường cụ thể.
> **Chuyển điểm đau thành chỉ số định lượng.**

*5 phút · Baseline → Target → Measurement*

---

# SECTION 03 — Có nên ứng dụng AI?

*AI chỉ thực sự mang lại giá trị khi tích hợp chính xác vào quy trình nghiệp vụ và giải quyết đúng điểm đau — theo Google PAIR Guidebook, Ch.1.*

## Slide 35 — Ba bước quyết định AI theo PAIR

| Bước | Nội dung | Ví dụ | Ánh xạ |
|---|---|---|---|
| **① Giao điểm: nhu cầu × thế mạnh AI** | Bài toán của bạn có nằm trong nhóm việc AI làm tốt hơn hẳn rule/heuristic không? | Câu hỏi trùng lặp của 1000 học viên K3 & K4 có nằm trong thế mạnh của AI? | → Câu hỏi 1: có thực sự cần AI? |
| **② Automate hay Augment?** | AI thay thế hay hỗ trợ con người? Mức tự động hóa tăng dần theo độ tin cậy và rủi ro. | AI trả lời thay TA luôn, hay chỉ soạn nháp để TA duyệt? | → Câu hỏi 2: giải pháp ở cấp độ nào? |
| **③ Reward function & tiêu chí thành công** | Định nghĩa "đúng/sai" của hệ thống (precision ↔ recall) và ngưỡng thành công đo được. | Đo bằng gì — thời gian phản hồi? tỷ lệ định hướng sai? | → Câu hỏi 3: PS đã đủ rõ để đo? |

> Ánh xạ về 4 câu hỏi trọng tâm: ① Có cần AI? · ② Cấp độ nào? · ③ Đủ rõ để đo? · Tổng hợp ①②③ → ④ **Go / Not Yet / No-Go**

**Nguồn:** Google PAIR — People + AI Guidebook · Ch.1 User Needs + Defining Success

---

## Slide 36 — Khi nào AI có lợi thế? (8 trường hợp "AI probably better")

1. **Gợi ý theo từng người** (*recommendation*) — Mỗi người dùng nhận một nội dung gợi ý khác nhau.
2. **Dự đoán tương lai** (*prediction*) — Đoán trước sự kiện sắp xảy ra để chuẩn bị phản ứng.
3. **Cá nhân hóa** (*personalization*) — Trải nghiệm tự điều chỉnh theo từng người, ngày càng hợp hơn.
4. **Hiểu ngôn ngữ tự nhiên** (*natural language*) — Hiểu câu hỏi viết tự do bằng lời nói hằng ngày.
5. **Nhận diện cả một lớp thực thể** — Nhận ra mọi đối tượng cùng loại, VD mọi khuôn mặt.
6. **Phát hiện cái hiếm & biến đổi** — Bắt sự kiện hiếm, thay đổi theo thời gian, VD gian lận.
7. **Agent/bot cho một lĩnh vực cụ thể** — Trợ lý ảo xử lý trọn một phạm vi việc chuyên biệt.
8. **Nội dung động thay giao diện tĩnh** — Nội dung linh hoạt hiệu quả hơn layout cố định, dễ đoán.

> AI chỉ đáng làm khi bài toán nằm trong nhóm này.

**Nguồn:** PAIR — Ch.1 User Needs + Defining Success

---

## Slide 37 — Khi nào AI KHÔNG tốt hơn? (6 trường hợp "AI probably NOT better")

1. **Cần duy trì tính dự đoán được** — Nút Home / Cancel phải luôn nằm ở một chỗ quen thuộc; người dùng không phải đoán mỗi lần.
2. **Thông tin tĩnh, ít thay đổi** — Nội dung cố định thì cứ hiển thị trực tiếp, không cần AI sinh lại mỗi lần.
3. **Lỗi quá tốn kém** — Chi phí của một lần sai lớn hơn lợi ích của nhiều lần đúng.
4. **Yêu cầu minh bạch tuyệt đối** — Mọi quyết định phải giải thích được từng bước, truy vết được.
5. **Tối ưu tốc độ & chi phí thấp** — Cần ra thị trường nhanh (time-to-market), vận hành rẻ; AI chỉ thêm độ trễ và chi phí.
6. **Việc giá trị cao người dùng muốn tự làm** — Tác vụ mang ý nghĩa cá nhân mà người dùng KHÔNG muốn bị tự động hóa.

> Rule/heuristic dễ build, dễ giải thích, dễ debug và bảo trì hơn — nếu nó giải quyết được, đó là lựa chọn tối ưu.

**Nguồn:** PAIR — Ch.1 User Needs + Defining Success

---

## Slide 38 — Khi nào AI đáng để làm?

### AI hợp khi nào
- Tác vụ mang tính lặp lại nhưng có độ biến thiên vừa phải.
- Yêu cầu tổng hợp hoặc tìm kiếm tri thức từ nhiều nguồn.
- Quy trình gồm nhiều bước phức tạp và cần tương tác với nhiều công cụ.

> Nếu quy trình hoàn toàn có tính xác định (deterministic), các quy tắc luật tĩnh (rule) sẽ tối ưu hơn.

### Vì sao doanh nghiệp đầu tư
1. **Sống còn** — Bắt buộc phải tích hợp AI để duy trì lợi thế cạnh tranh trước đối thủ.
2. **Hiệu quả** — Giảm thiểu chi phí vận hành, tăng tốc độ xử lý và nâng cao năng suất nghiệp vụ.
3. **Khám phá** — Tích lũy năng lực công nghệ, tránh tụt hậu và tìm kiếm các mô hình cơ hội mới.

> Mục tiêu áp dụng AI sẽ trực tiếp quyết định phương thức xây dựng giải pháp, mức độ tự động hóa và quy mô đầu tư.

---

## Slide 39 — Tự xây dựng hay mua giải pháp?

### Góc nhìn 1 — Chip Huyen, *AI Engineering* (2025)
- **In-house (Build):** Khi công nghệ AI là lợi thế cạnh tranh cốt lõi và yếu tố sống còn.
- **Mua / SaaS (Buy):** Khi giải pháp AI đóng vai trò như một công cụ tối ưu hóa năng suất (productivity layer).

### Góc nhìn 2 — MIT CISR

| Lựa chọn | Đặc điểm |
|---|---|
| **Buy** | Giải pháp may sẵn (off-the-shelf), do vendor duy trì. Triển khai nhanh, ít khác biệt cạnh tranh. Phụ thuộc roadmap vendor. |
| **Boost** | Mua mô hình sẵn có, cải tiến bằng dữ liệu nội bộ (fine-tune hoặc RAG). Đòi hỏi quản trị dữ liệu (data governance) tốt. |
| **Build** | Tự xây mô hình tùy biến (custom model). Kiểm soát cao nhất, chi phí đắt nhất. Đòi hỏi đội kỹ sư AI mạnh. |

> **Thực tế:** đa số đội ngũ đang ở giữa — **Boost** (RAG / fine-tune), thay vì tự xây lại mọi thứ từ đầu.

**Nguồn:** Chip Huyen — AI Engineering (O'Reilly, 2025) · MIT Sloan — Buy, Boost, or Build?

---

## Slide 40 — Vòng đời Sản phẩm AI

*Mỗi giai đoạn từ ý tưởng đến vận hành thực tế yêu cầu phương thức xác thực chuyên biệt.*

```
Start: Idea / Business Justification
 └─ Milestone 1 · Planning & Use Case Evaluation
      • Crawl-Walk-Run · AI Role · Defensibility
 └─ Milestone 2 · Expectations & Milestone Planning
      • Usefulness Thresholds · Last Mile Illusion
 └─ Milestone 3 · Model Selection
      • Hard Filters · Task-Specific Evals · Build vs Buy
 └─ Milestone 4 · Architecture Evolution
      Simple Prompt → Routing/Cache → Guardrails → RAG → Finetune
 └─ Milestone 5 · Evaluation-Driven Development
      • Per-Component + End-to-End · AI as Judge
 └─ Milestone 6 · Monitoring & Feedback Loop
      • Observability · Explicit + Implicit Feedback
           ↺ Data Flywheel ↔ Dataset Engineering
```

> **Day 02 nằm ở 2 milestone đầu — Planning & Expectations:** xác định bài toán và thiết lập kỳ vọng trước khi chọn model.

**Nguồn:** Chip Huyen — AI Engineering (O'Reilly, 2025)

---

# SECTION 04 — Rule / Workflow / Agent

*Phân tích cấp độ giải pháp. Cấp độ tối ưu là cấp độ đơn giản nhất đủ để giải quyết bài toán.*

## Slide 42 — Hệ thống AI = Model + Context + Planning + Tools

*Một giải pháp AI thực tế là một hệ thống nhiều thành phần, không chỉ dừng lại ở mô hình ngôn ngữ.*

```
                    ┌───────────────┐
                    │     Model     │  Hallucination · Cost
                    │  LLM · SLM    │
                    └───────┬───────┘
                            ↕
┌────────────┐      ┌───────────────┐      ┌──────────────┐
│  Context   │ ←──→ │ Orchestrator/ │ ←──→ │    Tools     │
│ RAG·Memory │      │ System Logic  │      │ APIs·Actions │
└────────────┘      └───────┬───────┘      └──────────────┘
Wrong Retrieval             ↕              Side Effects · Security
                    ┌───────────────┐
                    │   Planning    │  Loops · Bad Policy
                    │Steps·Policies │
                    └───────────────┘
```

| Thành phần | Vai trò | Mô tả |
|---|---|---|
| **Model** | Tư duy & Sáng tạo | Xử lý đọc hiểu, soạn thảo, tổng hợp, phân loại và đưa ra gợi ý. |
| **Context** | Tri thức chuyên biệt | Cơ sở dữ liệu, tài liệu nghiệp vụ, hồ sơ lịch sử giúp AI phản hồi chính xác theo bối cảnh. |
| **Planning** | Điều phối quy trình | Tự động phân rã tác vụ phức tạp và linh hoạt điều chỉnh. |
| **Tools** | Liên kết hệ thống | Tích hợp CRM, database, lịch làm việc hoặc API bên thứ ba. |

> **Giải pháp AI là một HỆ THỐNG — model chỉ là một thành phần.**

**Nguồn:** Anthropic — Building effective agents · Chip Huyen — AI Engineering

---

## Slide 43 — Automation vs Augmentation (PAIR bước ②)

*Với từng tác vụ, AI nên làm thay hay hỗ trợ con người?*

### AUTOMATE — AI làm thay
Chọn khi:
- Việc khó, nhàm chán, nguy hiểm hoặc cần scale
- Người dùng thiếu kiến thức / khả năng tự làm
- Có "đáp án đúng" mà mọi người cùng đồng thuận

*Đo thành công bằng:* hiệu quả tăng · an toàn hơn · giảm việc tẻ nhạt.

### AUGMENT — AI hỗ trợ con người
Chọn khi:
- Người dùng thích tự làm việc đó
- Stakes cao: tiền bạc, pháp lý, sức khỏe
- Kết quả cần trách nhiệm cá nhân / social capital
- Sở thích khó diễn đạt thành lời

*Đo bằng:* mức độ thích thú · cảm giác kiểm soát · sáng tạo tăng.

> Quyết định theo **từng tác vụ**. Việc đã automate vẫn gần như luôn cần human oversight — preview, edit, undo.

**Nguồn:** Google PAIR — Ch.1 User Needs + Defining Success

---

## Slide 44 — Tăng mức tự động hóa theo pha

*Mức tự động hóa tỷ lệ nghịch với rủi ro — áp dụng vào case 1000 học viên K3 & K4.*

| Pha | Nội dung |
|---|---|
| **Pha 1 — AI chỉ gợi ý** | AI đọc câu hỏi của học viên và gợi ý câu trả lời — Trợ giảng viết lại toàn bộ. |
| **Pha 2 — AI soạn nháp, TA duyệt** | Rủi ro thấp hơn sau khi đo được chất lượng gợi ý ở Pha 1 — TA hiệu chỉnh bản nháp trước khi gửi. |
| **Pha 3 — AI tự động có giám sát** | Chỉ áp dụng cho nhóm câu hỏi đã chứng minh an toàn qua dữ liệu — TA giám sát, can thiệp khi cần. |

> *risk ↓ khi dữ liệu đánh giá ↑*
>
> **Pattern #14** — "Automate more when risk is low" · **Pattern #17** — "Automate in phases"
>
> Không bật full-auto từ đầu — mức tự động hóa đi lên cùng độ tin cậy.

**Nguồn:** Google PAIR — 23 Design Patterns

---

## Slide 45 — Ba mức giải pháp: Rule / Workflow / Agent

| Cấp độ | Điều kiện áp dụng | Ví dụ |
|---|---|---|
| **Cấp độ 1 — Rule / Script** | • Đầu vào ổn định, ít thay đổi<br>• Logic viết được thành if/else<br>• Cần kết quả luôn đúng 100%<br>• Quy định pháp lý / tuân thủ chặt | Tính thuế · chặn email spam theo từ khóa · auto-reply theo template |
| **Cấp độ 2 — LLM Feature / Workflow** | • Đầu vào đa dạng, không viết hết rule được<br>• Đầu ra cần linh hoạt (tóm tắt, dịch, phân loại)<br>• Có cách đo chất lượng<br>• Người có thể kiểm tra trước khi gửi | Tóm tắt email · chatbot FAQ · phân loại ticket hỗ trợ |
| **Cấp độ 3 — Agent** | • Nhiều bước, dùng nhiều công cụ<br>• Tình huống thay đổi liên tục<br>• Cần tự ra quyết định giữa các bước<br>• Có kiểm soát rủi ro rõ ràng | Agent nghiên cứu thị trường · coding agent sửa nhiều file |

> **Thứ tự ưu tiên thực dụng:** bắt đầu từ bên trái, chỉ đi sang bên phải khi giá trị tăng hơn độ phức tạp.
>
> Rule/Workflow/Agent là cấp độ **KỸ THUẬT** — còn Automate/Augment (PAIR) là cấp độ **VAI TRÒ** của con người trong hệ thống.

---

## Slide 46 — Tình huống: Tối ưu nguồn lực Trợ giảng

**Bối cảnh & bài toán (case xuyên suốt buổi học):** Lớp học 1000 học viên (khóa K3 & K4) nhưng nguồn lực Trợ giảng (TA) có hạn. TA quá tải vì rà soát thủ công các câu hỏi trùng lặp và các yêu cầu hỗ trợ thiếu thông tin. Mục tiêu: tối ưu quy trình để giảm tải cho TA, giúp học viên không bị kẹt lâu.

**Quy trình hiện tại:**

```
01 Học viên tắc nghẽn
 → 02 Gửi yêu cầu hỗ trợ
 → 03 Trợ giảng đọc ngữ cảnh
 → 04 Phản hồi / chuyển tiếp
 → 05 Học viên hiệu chỉnh
```

- **Bottleneck:** Nhiều câu hỏi trùng lặp hoặc thiếu thông tin chi tiết; Trợ giảng mất thời gian rà soát thủ công.
- **Metrics:** Thời gian học viên chờ phản hồi, tỷ lệ câu hỏi trùng lặp, số học viên bị kẹt kéo dài.
- **Risks:** AI hướng dẫn sai hoặc nhầm kiến thức khiến học viên đi sai hướng thực hành.

> Cùng một tình huống này, ta sẽ đi qua cả 3 cấp độ giải pháp: Rule → Workflow → Agent.

---

## Slide 47 — Cấp độ 1: Rule-based

*Áp dụng khi logic nghiệp vụ tường minh, kết quả cố định và yêu cầu kiểm soát rủi ro nghiêm ngặt.*

**Khi nào chọn Rule:**
- Logic phân nhánh rành mạch (If/Else)
- Yêu cầu hoặc trạng thái lặp lại hoàn toàn
- Không đòi hỏi khả năng tự suy luận của AI
- Yêu cầu kết quả dự đoán và kiểm soát tuyệt đối

**Ứng dụng trong Lab:**
- Hỏi lịch nộp bài → Tự động gửi link thời khóa biểu
- Nộp thiếu file bài tập → Tự động nhắc checklist
- Hỏi lỗi cài đặt quen thuộc → Gửi link hướng dẫn
- Câu hỏi ngoài danh mục → Chuyển cho Trợ giảng

> Giải pháp dựa trên Luật (Rule) không thua kém AI — nếu giải quyết triệt để bài toán, đó luôn là lựa chọn tối ưu.

---

## Slide 48 — Cấp độ 2: Workflow

*Các bước xử lý đã định hình rõ, nhưng từng công đoạn cần AI hỗ trợ ngôn ngữ hoặc đánh giá.*

```
01 Học viên gửi Problem Card
 → 02 AI rà soát & yêu cầu bổ sung   [AI]
 → 03 Trợ giảng duyệt câu phức tạp   [HUMAN]
```

**Ưu điểm — Linh hoạt nhưng có kiểm soát:**
- Xử lý ngữ cảnh tốt hơn Rule tĩnh
- Lộ trình của hệ thống vẫn nằm trong tầm kiểm soát

**Lưu ý thiết kế — Tránh chatbot phản hồi tự do:**
- Mỗi công đoạn phải định nghĩa rõ đầu vào và đầu ra
- Không thiết kế thành một chatbot phản hồi tự do

**Nguồn:** Anthropic — Building effective agents

---

## Slide 49 — Cấp độ 3: Agent

*Hệ thống tự động lập kế hoạch, phối hợp công cụ và linh hoạt thích ứng theo tình huống.*

**Khi nào cân nhắc Agent:**
- Không thể xác định trước toàn bộ các bước thực thi
- Môi trường nhiều biến số, đòi hỏi thay đổi kế hoạch linh hoạt
- Cần tương tác nhiều công cụ, truy xuất nhiều nguồn dữ liệu
- Có vòng phản hồi và chốt chặn giám sát từ con người

**Ứng dụng trong Lab:**
- Theo dõi thảo luận và nộp bài trên các kênh học tập
- Phát hiện học viên hoặc nhóm bị kẹt quá lâu
- Tự động tổng hợp vấn đề, gợi ý cách hỗ trợ
- Trợ giảng chỉ cần duyệt và nhấn gửi phương án

> ⚠️ Tác động của Agent mạnh mẽ hơn, nhưng đi kèm chi phí vận hành cao hơn, độ trễ lớn hơn, khó kiểm thử và các dạng lỗi phức tạp hơn.

---

## Slide 50 — Một tình huống, ba cấp độ giải pháp

| Cấp độ | Ứng dụng | Khi nào? |
|---|---|---|
| **1 — Rule (luật tĩnh)**<br>*Trả lời tự động* | • Tự động trả lời FAQ, gửi link thời khóa biểu<br>• Gửi tài liệu sửa lỗi cài đặt cơ bản<br>• Nhắc nhở checklist nộp bài | Logic tường minh, kết quả cố định. |
| **2 — Workflow (quy trình)**<br>*Duyệt Problem Card* | • AI kiểm tra độ đầy đủ của Problem Card<br>• Yêu cầu bổ sung nếu thiếu thông tin<br>• Chuyển cho Trợ giảng giải quyết | Có quy trình rõ, AI hỗ trợ từng bước. |
| **3 — Agent (tác nhân)**<br>*Đề xuất can thiệp chủ động* | • Tự động theo dõi tiến độ nộp bài<br>• Phát hiện nhóm học viên bị kẹt lâu<br>• Chuẩn bị câu trả lời, đề xuất TA duyệt | Tình huống động, đa công cụ. |

> Không bắt buộc nâng cấp tuần tự từ Rule lên Agent → **dừng ở cấp tối giản nhất** nếu đã đáp ứng mục tiêu đề ra.

---

## Slide 51 — Đọc workflow patterns như người làm product

**Câu hỏi quyết định:** *"Lộ trình xử lý có viết trước được không?"*

- **Workflow:** Lộ trình do **CODE ĐIỀU PHỐI** — định trước bằng code path.
- **Agent:** **MODEL TỰ ĐIỀU PHỐI** lộ trình & cách dùng tools.

### Mỗi pattern = một tradeoff

| Pattern | Được gì | Mất gì |
|---|---|---|
| Prompt chaining | Chính xác hơn — có gate kiểm tra giữa các bước | Chậm hơn — độ trễ cộng dồn qua từng bước |
| Routing | Tối ưu chi phí — mỗi loại input một nhánh chuyên biệt | Cần phân loại đúng ngay từ đầu |
| Parallelization | Tin cậy hơn — vote, guardrail chạy song song | Chi phí nhân lên theo số nhánh |
| Orchestrator-workers | Xử lý được bài toán không biết trước subtasks | Khó kiểm thử, hành vi khó dự đoán |
| Evaluator-optimizer | Chất lượng tăng qua vòng lặp đánh giá | Cần tiêu chí chấm rõ ràng |
| Agent | Giải được bài toán mở | Chi phí cao, lỗi cộng dồn |

> PM không cần code pattern — nhưng phải đọc được sơ đồ và nói được tradeoff, vì nó quyết định chi phí, độ trễ, khả năng kiểm thử và dạng lỗi của hệ thống — đầu vào của ô **Boundary, Metric, HITL** trong Problem Statement.

**Nguồn:** Anthropic — Building effective agents

---

## Slide 52 — Workflow patterns cơ bản (đủ cho hầu hết bài toán)

### 1. Prompt Chaining
```
In → LLM Call 1 → Gate → LLM Call 2 → LLM Call 3 → Out
                    └── Gate fail → Exit
```
Chia task thành chuỗi bước tuần tự, có gate kiểm tra giữa các bước. VD: Viết outline → check → viết bài.
**Ý nghĩa quyết định:** đổi độ trễ lấy độ chính xác.

### 2. Routing
```
In → Router → ┬ LLM Call 1 ┐
              ├ LLM Call 2 ├→ Out
              └ LLM Call 3 ┘
```
Phân loại input → đưa vào nhánh chuyên biệt, tối ưu từng loại riêng. VD: CS query → FAQ / refund / kỹ thuật.
**Ý nghĩa quyết định:** câu dễ đi model rẻ, câu khó đi model mạnh.

### 3. Parallelization
```
In → ┬ LLM Call 1 ┐
     ├ LLM Call 2 ├→ Aggregator → Out
     └ LLM Call 3 ┘
```
Chạy song song rồi tổng hợp (sectioning), hoặc chạy nhiều lần lấy vote. VD: Guardrail + response đồng thời.
**Ý nghĩa quyết định:** vote để giảm rủi ro một đầu ra sai.

> **Nguyên tắc Anthropic:** Luôn ưu tiên giải pháp đơn giản nhất; chỉ tăng độ phức tạp khi thực sự cần thiết. Ba mô hình cơ bản này đã đủ đáp ứng hầu hết bài toán thực tế.

---

## Slide 53 — Khi nào cần phức tạp hơn?

### 4. Orchestrator-Workers
```
In → Orchestrator ⇢ ┬ LLM Call 1 ┐
                    ├ LLM Call 2 ├→ Synthesizer → Out
                    └ LLM Call 3 ┘
```
1 LLM phân việc động cho workers — subtasks không biết trước. VD: Coding agent sửa nhiều file.
**Ý nghĩa quyết định:** dùng khi không liệt kê trước được các bước.

### 5. Evaluator-Optimizer
```
In → Generator → Evaluator → Accepted → Out
         ↑            └── Rejected + Feedback ┘
```
1 LLM tạo, 1 LLM đánh giá → lặp cho đến khi đạt. VD: Dịch văn học → review → sửa.
**Ý nghĩa quyết định:** cần tiêu chí chấm rõ — chính là reward function ở bước ③.

### 6. Agent
```
Human ⇄ LLM Call ⇄ Environment
             └── Stop (điều kiện dừng)
```
LLM tự lập kế hoạch + gọi tools + iterate — autonomous loop. Action → Environment → Feedback. VD: SWE-bench, computer use.
**Ý nghĩa quyết định:** cần guardrails + stopping conditions.

> **Anthropic:** *"Agents' autonomy makes them ideal for scaling tasks in trusted environments."*
> → Chi phí vận hành cao, dễ tích tụ sai số (lỗi cộng dồn).

---

## Slide 54 — Thang câu hỏi lựa chọn cấp độ giải pháp

*Khung câu hỏi tuần tự giúp tránh bẫy "nhảy vọt" lên Agent phức tạp.*

1. **Tần suất & tác động có đủ lớn?** — Nếu thấp → Xử lý thủ công hoặc hiệu chỉnh quy trình nghiệp vụ trước.
2. **Logic xử lý có rành mạch?** — Nếu tường minh → Ưu tiên giải pháp Rule, kịch bản tự động, danh mục kiểm tra.
3. **Quy trình thực hiện có cố định?** — Nếu có → Xây dựng Workflow tích hợp AI hỗ trợ từng công đoạn.
4. **Quy trình đòi hỏi khả năng tự thích ứng linh hoạt?** — Chỉ khi có nhiều biến số phức tạp → Mới cân nhắc Agent.
5. **Giá trị mang lại có vượt trội chi phí & rủi ro?** — Nếu không → Đặt chốt chặn phê duyệt (HITL) hoặc chọn Not Yet / No-Go.

**Nguồn:** Anthropic — Building effective agents

---

## Slide 55 — Cây quyết định: Lựa chọn cấp độ giải pháp

```
                    ┌─ Bài Toán Của Bạn? ─┐
                              ↓
              ┌───── 1. Volume đủ lớn & lặp đủ thường xuyên? ─────┐
       KHÔNG →│ Chưa Đáng Đầu Tư AI — Giải Thủ Công Trước │       │ CÓ
              └──────────────────────────────────────────┘        ↓
                       ┌── 2. Logic rõ ràng, input ổn định? ──┐
                 CÓ → │        RULE / Script                 │   │ KHÔNG
                       └──────────────────────────────────────┘   ↓
                   ┌── 3. Cần nhiều bước, nhiều tool, state thay đổi? ──┐
        KHÔNG → LLM Feature + Human Review                     CÓ → AGENT + Controls
                                                          (Risk cao? → thêm HITL,
                                                           rollback, approval)
```

> **Đi từ trên xuống — mỗi nhánh "KHÔNG" là một lần tránh được độ phức tạp không cần thiết.**

**Nguồn:** Anthropic — Building effective agents · Google — Rules of ML

---

## Slide 56 — Ví dụ thực tế ngoài lớp học

| Lĩnh vực | Rule | Workflow | Agent |
|---|---|---|---|
| **Chăm sóc khách hàng** | Định tuyến phiếu hỗ trợ theo từ khóa. | Tự động soạn nháp câu trả lời có trích dẫn nguồn. | Xử lý quy trình đa bước, truy vấn CRM, tạo yêu cầu hoàn tiền. |
| **Nghiên cứu bán hàng** | Lọc khách hàng tiềm năng theo lĩnh vực, quy mô. | Thu thập thông tin → tóm tắt → soạn email tiếp cận. | Giám sát tín hiệu thị trường, cập nhật CRM, đề xuất bước tiếp theo. |
| **Kho tri thức nội bộ** | Phân phối chính sách theo nhu cầu tra cứu. | Hỏi đáp dựa trên tài liệu nội bộ kèm trích dẫn nguồn. | Giám sát thay đổi pháp lý, nhắc nhở cập nhật tài liệu. |

---

## Slide 57 — Reward function: hệ thống hiểu "đúng / sai" thế nào?

*PAIR bước ③ · Case: AI gợi ý câu trả lời cho câu hỏi của 1000 học viên (khóa K3 & K4)*

> Reward function là công thức quyết định đâu là dự đoán "đúng", đâu là "sai" — và chính nó định hình trải nghiệm người dùng cuối. Vì vậy nó phải được thiết kế **liên chức năng**: tối thiểu UX × Product × Engineering cùng ngồi lại.

| Kết quả | Diễn giải |
|---|---|
| **TP — True Positive** (đúng-tích cực) | Câu hỏi nghẽn thật → AI gợi ý đúng câu trả lời. Học viên được giải tỏa, TA đỡ tải. |
| **TN — True Negative** (đúng-tiêu cực) | Câu hỏi đã có tài liệu sẵn → AI không can thiệp. Đúng — không cần gợi ý gì thêm. |
| **FP — False Positive** (báo động giả) | AI gợi ý câu trả lời SAI (hallucination) và gửi thẳng cho học viên → học viên đi sai hướng thực hành. |
| **FN — False Negative** (bỏ sót) | Học viên đang kẹt thật nhưng AI bỏ sót, không gợi ý → học viên vẫn chờ lâu như cũ. |

> ⚠️ Chi phí của FP và FN **KHÔNG đối xứng** — báo cháy giả ≠ bỏ sót đám cháy. Cân nhắc đánh đổi này là quyết định then chốt khi thiết kế reward function.

**Nguồn:** PAIR — Ch.1 User Needs + Defining Success

---

## Slide 58 — Precision ↔ Recall: đánh đổi không tránh khỏi

| Precision cao — `TP / (TP + FP)` | Recall cao — `TP / (TP + FN)` |
|---|---|
| Ít gợi ý — nhưng gợi ý nào cũng chắc đúng. Người dùng tin vào từng gợi ý nhận được. | Bao trọn mọi trường hợp cần giúp — không học viên nào bị bỏ lại phía sau. |
| **Hệ quả:** Nhiều False Negative — bỏ sót học viên đang thực sự cần giúp. | **Hệ quả:** Nhiều False Positive — gợi ý sai nhiều, TA phải lọc lại thủ công. |

> **Đòn bẩy:** Vặn nút bên này lên, chất lượng bên kia xấu đi.
>
> Không có cấu hình đúng tuyệt đối — phải test điểm cân bằng với chính người dùng.

**Nguồn:** PAIR — Ch.1 User Needs + Defining Success

---

## Slide 59 — Viết tiêu chí thành công mà hành động được

*Metric tốt = chỉ số cụ thể + ngưỡng có nghĩa + hành động cụ thể*

**Template của PAIR:**
> If **{chỉ số cụ thể}** for **{tính năng AI}** **{drops below / goes above}** **{ngưỡng có nghĩa}**, we will **{hành động cụ thể}**.

**Ví dụ điền sẵn — case TA 1000 học viên:**
> Nếu tỷ lệ câu trả lời AI gợi ý bị TA sửa **> 30% trong 2 tuần**, ta sẽ **hạ mức tự động về pha 1** (chỉ gợi ý, không gửi thẳng cho học viên).

**Checklist trước khi chốt metric:**
1. Metric có ý nghĩa với MỌI người dùng không?
2. Có nhóm nào bị ảnh hưởng tiêu cực không?
3. Đây là thành công của ngày 1 — còn ngày 1000 thì sao?

> Và đừng quên: lên lịch **review metric định kỳ** — tiêu chí thành công cũng cần được bảo trì theo thời gian.

**Nguồn:** PAIR — Ch.1 User Needs + Defining Success · PAIR Worksheet — User Needs (PDF)

---

## Slide 60 — Thiết lập kỳ vọng

*Đo lường các chỉ số để xác định mức độ hiệu quả trước khi chính thức phát hành giải pháp.*

**01 · Tác động kinh doanh** — Giải pháp tạo giá trị gì cho doanh nghiệp?
- Tỷ lệ tự động hóa tác vụ / yêu cầu (%)
- Quy mô xử lý khối lượng công việc tăng thêm
- Tốc độ phản hồi & thời gian quy trình được tối ưu

**02 · Sự hài lòng khách hàng** — Người dùng thực tế có thấy tốt hơn không?
- Chỉ số hài lòng CSAT / NPS
- Đánh giá chất lượng trực tiếp từ người dùng
- Tỷ lệ hoàn thành tác vụ vs tỷ lệ bỏ ngang giữa chừng

**03 · Ngưỡng hữu dụng** — Hệ thống đạt tiêu chí nào thì có thể phát hành?
- Chất lượng: độ chính xác và tính hữu ích của đầu ra
- Độ trễ: tốc độ phản hồi của hệ thống (latency)
- Chi phí: chi phí tài chính trên mỗi lượt yêu cầu

---

## Slide 61 — Khoảng cách giữa Demo và Production

*Phản hồi chính xác trong vài lần thử chưa đủ cơ sở để triển khai hệ thống thực tế.*

1. **Baseline — Thiết lập đối chứng:** Đối chiếu hiệu quả với quy tắc tĩnh, nhân sự hay quy trình hiện tại?
2. **Evaluation — Kiểm thử hệ thống:** Bộ dữ liệu kiểm thử, kịch bản biên (edge cases) và tiêu chí nghiệm thu?
3. **Controls — Cơ chế kiểm soát:** Logging, fallback, rollback và nhân sự chịu trách nhiệm?
4. **Operations — Vận hành liên tục:** Ai giám sát lỗi, cập nhật tri thức nền và tối ưu hệ thống?

> Mục tiêu Day 02 là xác định tính khả thi để tiếp tục nghiên cứu — chưa phải quyết định triển khai ngay.

**Nguồn:** Google — Rules of ML · Chip Huyen — AI Engineering

---

## Slide 62 — Từ Problem Statement đến Eval Plan

*Problem Statement rõ ràng giúp định hình cụ thể các tiêu chí kiểm thử.*

1. **Input — Problem Statement:** 9 trường đã hoàn chỉnh — từ Actor, Workflow, Bottleneck đến Boundary & HITL.
2. **Test cases — Kịch bản kiểm thử:** Dữ liệu thực tế và các trường hợp biên (edge cases).
3. **Success — Chỉ số hiệu năng:** Đạt yêu cầu (pass) / Không đạt (fail) / Chuyển tiếp kiểm duyệt thủ công (HITL).

**Ba mức kiểm tra:**
- **Tác vụ đơn lẻ:** Hệ thống có phân loại chính xác các câu hỏi đầu vào không?
- **Hiệu năng quy trình:** Nhóm học viên có hoàn thành bài lab nhanh hơn và ít kẹt hơn không?
- **Rủi ro & sai số:** Hệ thống có phản hồi sai lệch mà không chuyển tiếp cho Lab Coach phê duyệt không?

---

## Slide 63 — Chuyển dịch từ PS sang Eval Plan

*Phương pháp đánh giá, bộ dữ liệu mẫu và ngưỡng chấp nhận*

```
[Problem Statement] → [Test Cases]  → [Eval Metric]  → [Architecture Boundary]
 'BÀI TOÁN LÀ GÌ'     'LÀM SAO       'ĐO BẰNG         'ĐƯỢC PHÉP LÀM GÌ'
 Actor                 BIẾT ĐÚNG'     CÁI GÌ'
 Workflow             Từ mỗi field   Ngưỡng đo:      Scope, HITL points,
 Bottleneck           → suy ra câu   accuracy,       rollback, permissions
 Impact                hỏi kiểm tra  latency,
 Success Metric        cụ thể        cost, CSAT
 Boundary
```

**Ví dụ minh họa:**

| Problem Statement | Test Cases | Eval Metric | Architecture Boundary |
|---|---|---|---|
| **Actor:** Agent Customer Support<br>**Workflow:** Xử lý ticket tra cứu + mở thẻ<br>**Bottleneck:** Tra 4–5 hệ thống, tóm tắt lại<br>**Impact:** TB 8 phút/ticket, rớt SLA 5 phút<br>**Metric:** rớt SLA 5 phút<br>**Boundary:** AI đề xuất, agent Customer Support xác nhận | • Ticket "tra cứu giao dịch" → AI trả đúng account + trích dẫn?<br>• Ticket "mở thẻ" → AI biết giới hạn scope, chuyển human khi cần?<br>• Input không rõ intent → AI escalate, không tự trả lời? | • 80% top-5 intent xử lý < 2 phút<br>• Tỉ lệ trả lời sai không tăng<br>• Thời gian agent search giảm ≥ 50%<br>• CSAT ≥ baseline | • Chỉ ĐỀ XUẤT câu trả lời<br>• Agent Customer Support XÁC NHẬN trước khi gửi<br>• Không truy cập dữ liệu ngoài 5 hệ thống được phép<br>• Rollback: tắt AI, quay về manual 100% |

> **"Nếu không suy ra được 3 thứ bên phải → PS chưa đủ chất."**
> Không suy ra được test cases, eval metric và architecture boundary từ PS → PS chưa đủ chặt.

---

## Slide 64 — Lỗi AI được định nghĩa bởi kỳ vọng người dùng

*PAIR Chương 6 · Errors + Graceful Failure*

> Cùng một hệ gợi ý đúng 60% — là thành công hay thất bại? Tùy vào kỳ vọng bạn đã hứa với người dùng.

| Loại | Tên | Mô tả |
|---|---|---|
| **Loại 1 · Context errors** | Sai bối cảnh | Hệ thống chạy "đúng" nhưng giả định sai về người dùng, thời điểm hoặc bối cảnh. VD: gợi ý ôn bài giữa kỳ nghỉ. |
| **Loại 2 · Fail states** | Không trả lời được | Hệ thống không trả lời được hoặc không có câu trả lời đúng cho tình huống này. |
| **Loại 3 · Background errors** | Lỗi ngầm | Cả người dùng lẫn hệ thống đều không nhận ra — "unknown unknowns". → Cần QA chủ động, không chờ người dùng báo lỗi. |

> Viết **Boundary & HITL** trong Problem Statement chính là khai báo trước: lỗi nào được phép xảy ra, lỗi nào không — và ai bắt lỗi đó.

**Nguồn:** PAIR — Ch.6 Errors + Graceful Failure

---

## Slide 65 — Vai trò UX + Human-in-the-loop

*UX là chốt chặn khi AI thiếu dữ liệu, độ tin cậy thấp hoặc cần phê duyệt thủ công.*

### AI không cần hoàn hảo, nếu UX đỡ được chỗ nó yếu

| Vấn đề | Giải pháp UX |
|---|---|
| **Không chắc** (low confidence) | → Xin user xác nhận trước khi thực hiện |
| **Risk cao** (sai = hậu quả nghiêm trọng) | → Chỉ suggest, không auto-action |
| **Câu trả lời dài** (quá tải thông tin) | → Chia option / card / summary cho user chọn |
| **Thiếu context** (input mơ hồ) | → Hỏi lại đúng chỗ thay vì đoán sai |

### 4 pattern Human-in-the-loop
1. **Làm rõ ý định** — Yêu cầu bổ sung ngữ cảnh khi thông tin chưa đủ.
2. **Minh bạch thông tin** — Trích dẫn nguồn minh chứng cho câu trả lời.
3. **Phê duyệt thủ công** — Con người kiểm duyệt trước tác vụ rủi ro cao.
4. **Thiết lập ranh giới** — Giới hạn phạm vi hoạt động tự chủ của AI.

> **AI Product = AI + UX.** Dùng UX để hỗ trợ chỗ AI chưa đủ tốt.
>
> **PAIR — paths forward from failure:** luôn mở kênh feedback (kể cả trên output "đúng") và trả quyền kiểm soát cho người dùng khi automation hỏng.

**Nguồn:** PAIR — Ch.6 Errors + Graceful Failure

---

# SECTION 05 — Problem Statement hoàn chỉnh

*Liên kết chặt chẽ giữa bài toán, workflow, metrics và quyết định AI — thành đầu vào cho Eval Plan.*

## Slide 67 — Problem Statement cho hệ thống AI (9 trường)

### 6 yếu tố bài toán cốt lõi

| Trường | Nội dung |
|---|---|
| **Actor** — đối tượng ảnh hưởng | Đối tượng trực tiếp chịu ảnh hưởng bởi vấn đề. |
| **Workflow** — quy trình hiện tại | Quy trình vận hành hiện tại gồm các bước cụ thể nào? |
| **Bottleneck** — nút thắt | Khâu nào gặp tình trạng chậm trễ, sai sót, lặp lại? |
| **Impact** — tác động | Tổn thất lượng hóa bằng thời gian, chi phí, SLA hoặc chất lượng. |
| **Success Metric** — chỉ số thành công | Chỉ số đo lường cụ thể để xác định sự cải thiện. |
| **Boundary** — ranh giới | AI không được làm gì; khâu nào bắt buộc có con người. |

### 3 yếu tố quyết định AI

| Trường | Nội dung |
|---|---|
| **Điểm AI can thiệp** (*decision · entry*) | AI hỗ trợ hoặc tự động hóa ở bước cụ thể nào? |
| **Mức chọn** (*decision · level*) | Rule / Workflow / Agent? |
| **Rủi ro & HITL** (*decision · safety*) | Phương án xử lý khi AI sai sót và quy trình phê duyệt thủ công. |

---

## Slide 68 — Ví dụ mẫu: Hỗ trợ Lab Coach/TA

| Trường | Nội dung |
|---|---|
| **Actor** | Lab Coach hỗ trợ các nhóm học viên trong lớp 1000 học viên (khóa K3 & K4). |
| **Workflow** | Học viên đặt câu hỏi → Lab Coach nghiên cứu ngữ cảnh → Phản hồi / yêu cầu làm rõ → Học viên cập nhật bài. |
| **Bottleneck** | Câu hỏi trùng lặp hoặc thiếu thông tin nền tảng cao; Lab Coach mất thời gian phân loại thủ công. |
| **Impact** | Học viên chờ phản hồi lâu; Lab Coach quá tải, thiếu thời gian cho câu hỏi phức tạp. |
| **Success Metric** | Giảm tỷ lệ câu hỏi lặp duyệt thủ công; rút ngắn thời gian phản hồi trung bình; không tăng tỷ lệ định hướng sai. |
| **Boundary** | AI không tự đánh giá/chấm điểm bài; chỉ hỗ trợ gợi ý làm rõ và điều phối quy trình. |
| **Điểm AI can thiệp** | Ngay sau khi học viên gửi câu hỏi hoặc Problem Card thiếu thông tin ngữ cảnh. |
| **Mức chọn** | **Workflow:** AI phát hiện thông tin còn thiếu; Lab Coach phê duyệt câu hỏi chuyên sâu. |
| **Rủi ro & HITL** | AI định hướng sai → Lab Coach kiểm duyệt trước khi gửi phản hồi. |

> Một Problem Statement đủ 9 trường — như ví dụ này — là căn cứ để ra quyết định **Go, Not Yet hay No-Go**.

---

## Slide 69 — Đánh giá mức độ phù hợp của AI · BỘ THẺ CÂU HỎI #4 — GATE QUYẾT ĐỊNH

*Năm câu hỏi kiểm tra mức sẵn sàng — gate cuối trước khi ra quyết định.*

1. Nghiệp vụ có đòi hỏi xử lý ngôn ngữ, tri thức chuyên môn hoặc suy luận?
2. Dữ liệu đầu vào có cung cấp đủ ngữ cảnh để AI phản hồi chính xác?
3. Đã thiết lập các chỉ số định lượng để đánh giá hiệu quả?
4. Hậu quả khi AI sai sót có nằm trong phạm vi kiểm soát?
5. Có giải pháp thay thế đơn giản và tối ưu chi phí hơn AI không?

> Nếu phần lớn câu trả lời chưa rõ ràng → Quyết định: **Not Yet**.

**Nguồn:** Google — Rules of Machine Learning · Anthropic — Building effective agents

---

## Slide 70 — Khung ra quyết định: Go / Not Yet / No-Go

| ✓ **Go** — thực hiện | ⏸ **Not Yet** — tạm hoãn | ✕ **No-Go** — không triển khai |
|---|---|---|
| *Đủ điều kiện* | *Có triển vọng* | *Không phù hợp* |
| — Bài toán rõ ràng<br>— Chỉ số đo lường khả thi<br>— Điểm can thiệp AI phù hợp<br>— Kiểm soát được rủi ro | — Cần bổ sung dữ liệu thực tế<br>— Chuẩn hóa quy trình<br>— Thiết lập chỉ số<br>— Xác định ranh giới | — AI không mang giá trị vượt trội<br>— Rủi ro vận hành quá cao<br>— Giải pháp không dùng AI tối ưu hơn |

> Quyết định **"Not Yet"** thể hiện sự chín chắn trong tư duy thiết kế sản phẩm, không phải sự thất bại.

---

## RECAP — Sáu nguyên tắc cốt lõi sau Day 02

*Kim chỉ nam để thẩm định mọi đề xuất ứng dụng AI*

1. **Brief mơ hồ không thay thế Problem Statement.** Một bản tóm tắt mơ hồ không thể thay thế cho một Problem Statement hoàn chỉnh.
2. **Mô hình hóa workflow trước khi tích hợp AI.** Bắt buộc phải mô hình hóa quy trình trước khi xem xét tích hợp giải pháp AI.
3. **Pain point phải được lượng hóa.** Mọi điểm đau cần được lượng hóa bằng baseline và chỉ số đo lường cụ thể.
4. **Phức tạp không đồng nghĩa với hiệu quả.** Rule, Workflow và Agent là ba cấp độ khác nhau; độ phức tạp kỹ thuật không đồng nghĩa với hiệu quả tối ưu.
5. **Quyết định dựa trên lập luận thực tế.** Quyết định Go / Not Yet / No-Go phải được thiết lập dựa trên lập luận thực tế và số liệu kiểm thử rõ ràng.
6. **Đo reward function bằng trải nghiệm người dùng, không chỉ accuracy.** *(MỚI · PAIR)* Thiết kế đánh đổi precision ↔ recall theo lợi ích người dùng và kiểm chứng với người dùng thật.

**Nguồn:** PAIR — Ch.1 User Needs + Defining Success

---

# APPENDIX · ĐỌC THÊM

## Slide 72 — Bốn nguồn gốc của lỗi AI (PAIR Ch.6)

1. **Lỗi dữ liệu & dự đoán** — Dữ liệu gán nhãn sai, suy luận kém, hoặc thiếu dữ liệu huấn luyện.
2. **Lỗi đầu vào** — Input bất ngờ ngoài thiết kế, phá vỡ thói quen của người dùng.
3. **Lỗi liên quan** — Độ tin cậy thấp, kết quả không liên quan. VD: gợi ý "hoạt động vui chơi" cho chuyến đi đám tang.
4. **Lỗi phân cấp hệ thống** — Nhiều hệ thống AI cùng hoạt động và xung đột tín hiệu với nhau.

> "Lỗi" được định nghĩa bởi kỳ vọng và mô hình tâm trí của người dùng — cùng một hệ thống có thể là thành công hoặc thất bại tùy kỳ vọng.

---

## Slide 73 — Paths forward from failure (PAIR Ch.6)

1. **Mở kênh feedback** — Tạo cơ hội cho người dùng phản hồi về chất lượng hệ thống, kể cả trên những output "đúng".
2. **Trả quyền kiểm soát** — Khi automation thất bại, trả quyền kiểm soát cho người dùng, kèm đủ thông tin để họ tiếp quản công việc.
3. **Giả định người dùng sẽ dùng sai** — Thiết kế để thất bại trở nên "an toàn, nhàm chán" thay vì trở thành thảm họa.

> Nguyên tắc thông báo lỗi: **"be human, not machine".**
> Thiết kế trải nghiệm khi AI sai sẽ học kỹ ở **Day 18 — Human-centered AI design**.

---

## Slide 74 — Workflow Patterns theo Anthropic (tổng quan)

| Nhóm | Patterns |
|---|---|
| **Basic Patterns** — đáp ứng đa số tác vụ | Prompt Chaining (Chuỗi liên kết) · Routing (Phân luồng) · Parallelization (Song song) |
| **Advanced Patterns** — khi nghiệp vụ đòi hỏi | Orchestrator-Workers (Điều phối – Thực thi) · Evaluator-Optimizer (Đánh giá – Tối ưu) |
| **Autonomous** — tác nhân tự chủ | **Agent:** LLM tự lập kế hoạch, sử dụng công cụ, quan sát phản hồi và linh hoạt điều chỉnh bước tiếp theo. |

> **Nguyên tắc:** Bắt đầu bằng giải pháp đơn giản nhất; chỉ tăng độ phức tạp khi quy trình thực tế yêu cầu.

**Nguồn:** Anthropic — Building effective agents

---

## Slide 75 — Vòng đời Sản phẩm AI (nhắc lại)

Xem sơ đồ đầy đủ tại [Slide 40](#slide-40--vòng-đời-sản-phẩm-ai).

**Nguồn:** Chip Huyen — AI Engineering (O'Reilly, 2025)

---

## Slide 76 — Bộ thẻ câu hỏi #1–#4 tổng hợp

*22 câu hỏi theo hành trình: Phân kỳ → Phỏng vấn → Cấu trúc PS → Gate quyết định*

### #1 · PHÂN KỲ — 6 câu gợi mở (→ slide 21)
1. Giả định hiển nhiên nào cần lật lại?
2. Cách tiếp cận nào hoàn toàn mới?
3. Nếu thiết kế lại từ đầu, không giới hạn?
4. Tại sao bài toán này cần AI?
5. Quy trình nào tồn tại chỉ vì thói quen?
6. Câu hỏi cốt lõi nào đang bị né tránh?

### #2 · PHỎNG VẤN — 5 câu stakeholder (→ slide 25)
1. Pain point là gì, tần suất ra sao?
2. Workflow hiện tại như thế nào?
3. Thiệt hại do vấn đề gây ra?
4. Hậu quả nếu AI sai sót?
5. Ai có quyền phê duyệt (nói YES)?

### #3 · CẤU TRÚC PS — 6 câu khai thác (→ slide 30)
1. Quy trình hiện tại như thế nào?
2. Nút thắt nằm ở đâu?
3. Hao phí hiện tại là bao nhiêu?
4. Tiêu chí thành công đo bằng gì?
5. Hậu quả khi xảy ra sai sót?
6. Có giải pháp phi AI đơn giản hơn?

### #4 · GATE QUYẾT ĐỊNH — 5 câu readiness (→ slide 69)
1. Có đòi hỏi ngôn ngữ, tri thức, suy luận?
2. Dữ liệu đủ ngữ cảnh để AI chính xác?
3. Đã có chỉ số định lượng?
4. Hậu quả sai sót có kiểm soát được?
5. Có giải pháp đơn giản hơn AI?

---

## Nguồn tham khảo tổng hợp

- **Google PAIR** — *People + AI Guidebook*, đặc biệt Ch.1 (User Needs + Defining Success) và Ch.6 (Errors + Graceful Failure); PAIR — 23 Design Patterns; PAIR Worksheet — User Needs (PDF)
- **Anthropic** — *Building effective agents*
- **Google** — *Rules of Machine Learning*
- **Chip Huyen** — *AI Engineering* (O'Reilly, 2025)
- **Marty Cagan** — *Inspired* (2nd ed.)
- **Don Norman** — jnd.org; *The Design of Everyday Things*
- **Design Council** — The Double Diamond
- **IDEO** — Design Kit · **Stanford d.school**
- **MIT Sloan / CISR** — Buy, Boost, or Build?
- **Amplitude** — North Star Playbook · **Lenny Rachitsky** — Choosing Your North Star Metric
- Case studies: Lenny's Podcast — The rise of Cursor · The Verge — Artifact · Google Blog — NotebookLM · Britannica — Gravity · ACS — Edwin Land & Instant Photography · Airbnb — About us

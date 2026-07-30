# AI IN ACTION · DAY 02 — Xác định bài toán cho AI

> **Từ yêu cầu mơ hồ đến Problem Statement rõ ràng.**
>
> Mục tiêu: Biến yêu cầu mơ hồ thành Problem Statement rõ ràng để ra quyết định.

---

## Agenda

### SÁNG — Khung lý thuyết (4h)
- Problem Discovery (Double Diamond, HCD)
- Problem Statement & định lượng hóa
- PAIR ① AI có thêm giá trị?
- PAIR ② Automate/Augment → Rule/Workflow/Agent
- PAIR ③ Reward function & success criteria
- Khi AI sai & UX/HITL
- PS hoàn chỉnh → Go / Not Yet / No-Go

### CHIỀU — Thực hành Lab (4h)
- **Cá nhân:** Tìm 5 bài toán & điền 3 Problem Cards
- **Nhóm:** Phản biện chéo, chốt 1 bài toán
- **Nhóm:** Xác thực dữ liệu & vẽ quy trình
- **Nhóm:** Xác định giải pháp & ra quyết định
- **Cá nhân:** Viết nhật ký phản tư (Reflection Log)

### BÀI NỘP CUỐI BUỔI
- Nhật ký tìm và lọc bài toán *(Cá nhân)*
- Problem Statement hoàn chỉnh *(Nhóm)*
- Nhật ký phản tư *(Cá nhân)*

---

## 1. Tìm đúng vấn đề trước khi tìm giải pháp

*Mô hình Double Diamond — Don Norman / British Design Council (2005)*

### Diamond 1 — Tìm đúng VẤN ĐỀ
- **Discover:** Mở rộng — khảo sát vấn đề căn bản
- **Define:** Thu hẹp — xác định đúng bài toán gốc

### Diamond 2 — Tìm đúng GIẢI PHÁP
- **Develop:** Mở rộng — nhiều giải pháp tiềm năng
- **Deliver:** Thu hẹp — chọn và triển khai

> *"Kỹ sư và doanh nhân được đào tạo để **giải** vấn đề. Nhà thiết kế được đào tạo để **khám phá** vấn đề thật."*

> ⚠️ **Giải pháp xuất sắc cho sai vấn đề có thể còn tệ hơn không có giải pháp.**

**Nguồn:** Don Norman — jnd.org · Design Council — The Double Diamond

---

## 2. Diamond 1 — Tìm đúng vấn đề

*Phân kỳ để thấu hiểu sâu sắc, hội tụ để lựa chọn chính xác.*

| DISCOVER · Phân kỳ (khám phá / mở rộng góc nhìn) | DEFINE · Hội tụ (định nghĩa / chọn lọc dựa vào dữ liệu) |
|---|---|
| Quan sát thực tế (Observation) | Sơ đồ đồng cảm / Gom nhóm (Affinity Mapping) |
| Phỏng vấn người dùng (User Interview) | Kỹ thuật đặt câu hỏi 5 Whys |
| Khảo sát (Survey) | Ma trận Tác động – Nỗ lực (Impact–Effort) |
| Nhật ký hành vi (Diary Study) | Biểu quyết bằng chấm tròn (Dot Voting) |
| Phân tích dữ liệu / Nhật ký hệ thống | Câu hỏi mở hướng giải quyết (How Might We) |
| Bản đồ các bên liên quan (Stakeholder Mapping) | Phát biểu bài toán (Problem Statement) |

---

## 3. Khởi nguồn từ bài toán, không bắt đầu từ AI

*Ba bài học thực tế về am hiểu lĩnh vực, quy mô thị trường và định vị giải pháp.*

**CURSOR — "Lệch năng lực cốt lõi"**
Từ bỏ mảng AI thiết kế cơ khí (CAD) để tập trung vào AI code editor — nơi đội ngũ am hiểu sâu sắc quy trình nghiệp vụ.

**ARTIFACT — "Sản phẩm tốt ≠ Thị trường lớn"**
Ứng dụng đọc tin tích hợp AI xuất sắc, nhưng quy mô thị trường quá hẹp để thương mại hóa thành công (đóng cửa 1/2024).

**NOTEBOOKLM — "Định vị đúng điểm đau"**
Tập trung giải quyết nhu cầu hỏi đáp, tóm tắt trên tài liệu cá nhân và đối chiếu nguồn gốc bằng trích dẫn.

> **Lộ trình:** Bài toán → Quy trình vận hành → Chỉ số đo lường → Giải pháp AI

**Nguồn:** Lenny's Podcast — The rise of Cursor · The Verge — Artifact · Google Blog — NotebookLM

---

## 4. Tìm bài toán AI ở đâu? — 4 Lenses

*Bắt đầu từ việc quan sát các hoạt động thực tế xung quanh.*

| Lens | Câu hỏi dẫn dắt |
|---|---|
| **REPETITIVE** — Tác vụ lặp lại | Việc diễn ra thường xuyên; công đoạn nào cần chuẩn hóa để hướng tới tự động hóa? |
| **TIME-CONSUMING** — Tiêu tốn thời gian | Khối lượng xử lý lớn; thời gian hao phí ở bước nào (tìm kiếm, đọc hiểu, chờ đợi, định dạng)? |
| **AI ADVANTAGE** — Lợi thế của AI | Tác vụ đòi hỏi phân tích ngữ cảnh, xử lý ngôn ngữ tự nhiên, tổng hợp đa nguồn |
| **USER PAIN POINTS** — Điểm đau người dùng | Ai đang gặp khó khăn, phàn nàn hoặc bị tắc nghẽn liên tục? |

> Tập trung nhận diện vấn đề; chưa vội đề xuất giải pháp. Sàng lọc bài toán sẽ diễn ra vào buổi chiều.

---

## 5. Sai lầm thường gặp — Anti-patterns

*Dấu hiệu cảnh báo bài toán chưa được định hình rõ hoặc giải pháp AI được lựa chọn quá sớm.*

**Ưu tiên giải pháp (Solution-first)**
Xây dựng chatbot/agent trước khi làm rõ quy trình vận hành và điểm nghẽn thực tế.

**Mơ hồ hiện trạng (No baseline)**
Không lượng hóa tổn thất hiện tại, dẫn đến mất căn cứ đánh giá hiệu quả cải tiến.

**Bỏ qua đánh giá (No evaluation)**
Không thiết lập kịch bản kiểm thử, chỉ số đo lường hoặc phương án đối chứng.

**Mập mờ ranh giới (No boundary)**
Không rõ phạm vi tự chủ của AI và thời điểm cần con người phê duyệt (Human-in-the-loop).

> Nếu phát hiện mắc các sai lầm trên, hãy quay lại làm rõ Problem Statement trước khi chọn công nghệ.

---

## 6. PAIR · Chương 1 — Reframe câu hỏi

Thay vì hỏi:
> *"Can we use AI to ______?"*

Hãy thay bằng hai câu hỏi:
> *"How might we solve ______?"*
> *"Can AI solve this problem in a unique way?"*

> **Hỏi về bài toán trước, về AI sau — AI chỉ là một phương án trong nhiều phương án khả dĩ.**
> Câu hỏi đúng quyết định bài toán bạn giải — và giải pháp bạn chọn.

**Nguồn:** Google PAIR — Ch.1 User Needs + Defining Success

---

## 7. Quick Problem Card — Khung định hình bài toán

| Trường | Ký hiệu | Nội dung |
|---|---|---|
| Bài toán (1 câu) | `problem` | Vấn đề cụ thể cần giải quyết (không bao gồm giải pháp) |
| Đối tượng ảnh hưởng | `actor` | Cá nhân hoặc bộ phận chịu tác động trực tiếp từ vấn đề |
| Quy trình hiện tại | `workflow` | Các bước vận hành thủ công hoặc tự động hiện tại (gồm 3–7 bước) |
| Nút thắt & Tác động | `bottleneck + impact` | Khâu gây chậm trễ, sai sót hoặc lặp lại; hệ quả hay tổn thất cụ thể |
| Chỉ số đo thành công | `success metric` | Chỉ số định lượng cụ thể dùng để chứng minh hiệu quả cải tiến |
| Định hướng giải pháp | `direction` | No AI / Rule / Workflow / Agent / Chưa xác định |

---

## 8. Câu hỏi khai thác bài toán (6 câu hỏi)

*Bộ câu hỏi định hình vấn đề dành cho các bên liên quan hoặc chính mình.*

**01 · Quy trình hiện tại như thế nào?**
Công cụ, các bước, cơ chế bàn giao thông tin?

**02 · Nút thắt nằm ở đâu?**
Bước nào chậm, dễ sai sót, lặp lại?

**03 · Hao phí hiện tại là bao nhiêu?**
Thời gian, chi phí nhân sự, SLA, cơ hội bỏ lỡ?

**04 · Tiêu chí thành công đo bằng gì?**
Hiệu quả cải tiến định lượng cụ thể?

**05 · Hậu quả khi xảy ra sai sót?**
Phạm vi tự quyết của AI; điểm cần con người phê duyệt?

**06 · Có giải pháp phi AI đơn giản hơn?**
Quy tắc, checklist, quy trình hay tài liệu hướng dẫn?

---

## 9. Định lượng hóa bài toán

*Điểm đau chưa được định lượng thì không thể xác định giá trị thực tế của AI.*

| Bước | Câu hỏi |
|---|---|
| **01 · BASELINE** — Hiện trạng / *where we are* | Mức hao phí hiện tại là bao nhiêu? Bằng con số cụ thể |
| **02 · TARGET** — Mục tiêu / *where to go* | Kỳ vọng cải thiện ở mức độ nào? Ngưỡng cụ thể là gì? |
| **03 · MEASUREMENT** — Đo lường / *how we know* | Chỉ số nào chứng minh tính hiệu quả? Cách thu thập? |

### Ví dụ

- **Thời gian hoàn thành:** Rút ngắn từ 90 phút xuống dưới 30 phút
- **Chất lượng công việc:** Giảm tỷ lệ lỗi phân loại từ 20% xuống dưới 5%
- **Tải trọng vận hành:** Cắt giảm 40% câu hỏi trùng lặp cần Trợ giảng xử lý

---

## 10. Thiết lập chỉ số: Output & Input

*Chỉ số đo lường cần phản ánh kết quả cuối và các đòn bẩy có thể tác động.*

**OUTPUT METRIC** — Kết quả cuối cùng / *what we optimize*
- Thời lượng hoàn tất quy trình giảm bao nhiêu?
- Tỷ lệ sai sót / chất lượng đầu ra thay đổi thế nào?
- Giá trị thực tế người dùng nhận được rõ nét hơn?

**INPUT METRICS** — Các đòn bẩy / *what we can move*
- Tỷ lệ câu hỏi được phân loại chính xác
- Tỷ lệ yêu cầu được chuyển tiếp hỗ trợ kịp thời
- Thời gian Trợ giảng hiệu chỉnh bản nháp phản hồi

> Tăng cái này → đo cái kia.

> ⚠️ **"Nâng cao hiệu suất" không phải chỉ số** — cần gắn với hiện trạng, mục tiêu và phương pháp đo.

**Nguồn:** Amplitude — North Star Playbook · Lenny Rachitsky — Choosing Your North Star Metric

---

## 11. Ba bước quyết định AI theo PAIR

*Google People + AI Guidebook · Chương 1: User Needs + Defining Success*

**BƯỚC ① — Giao điểm: nhu cầu × thế mạnh AI**
Bài toán của bạn có nằm trong nhóm việc AI làm tốt hơn hẳn rule/heuristic không?
*VD: câu hỏi trùng lặp của 1000 học viên K3 & K4 có nằm trong thế mạnh của AI?*
→ Trả lời câu hỏi 1: **có thực sự cần AI?**

**BƯỚC ② — Automate hay Augment?**
AI thay thế hay hỗ trợ con người? Mức tự động hóa tăng dần theo độ tin cậy và rủi ro.
*VD: AI trả lời thay TA luôn, hay chỉ soạn nháp để TA duyệt?*
→ Trả lời câu hỏi 2: **giải pháp ở cấp độ nào?**

**BƯỚC ③ — Reward function & tiêu chí thành công**
Định nghĩa "đúng/sai" của hệ thống (precision ↔ recall) và ngưỡng thành công đo được.
*VD: đo bằng gì — thời gian phản hồi? tỷ lệ định hướng sai?*
→ Trả lời câu hỏi 3: **PS đã đủ rõ để đo?**

> **Ánh xạ về 4 câu hỏi trọng tâm của ngày:** ① Có cần AI? · ② Cấp độ nào? · ③ Đủ rõ để đo? · Tổng hợp ①②③ → ④ **Go / Not Yet / No-Go**

**Nguồn:** Google PAIR — People + AI Guidebook

---

## 12. Khi nào AI có lợi thế? — 8 trường hợp "AI probably better"

| Trường hợp | Mô tả |
|---|---|
| **Gợi ý theo từng người** (*recommendation*) | Mỗi người dùng nhận một nội dung gợi ý khác nhau |
| **Dự đoán tương lai** (*prediction*) | Đoán trước sự kiện sắp xảy ra để chuẩn bị phản ứng |
| **Cá nhân hóa** (*personalization*) | Trải nghiệm tự điều chỉnh theo từng người, ngày càng hợp hơn |
| **Hiểu ngôn ngữ tự nhiên** (*natural language*) | Hiểu câu hỏi viết tự do bằng lời nói hằng ngày |
| **Nhận diện cả một lớp thực thể** | Nhận ra mọi đối tượng cùng loại — VD mọi khuôn mặt |
| **Phát hiện cái hiếm & biến đổi** | Bắt sự kiện hiếm, thay đổi theo thời gian — VD gian lận |
| **Agent/bot cho một lĩnh vực cụ thể** | Trợ lý ảo xử lý trọn một phạm vi việc chuyên biệt |
| **Nội dung động thay giao diện tĩnh** | Nội dung linh hoạt hiệu quả hơn layout cố định, dễ đoán |

> **AI chỉ đáng làm khi bài toán nằm trong nhóm này.**

**Nguồn:** PAIR — Ch.1 User Needs + Defining Success

---

## 13. Khi nào AI KHÔNG tốt hơn? — 6 trường hợp "AI probably NOT better"

**Cần duy trì tính dự đoán được**
Nút Home / Cancel phải luôn nằm ở một chỗ quen thuộc — người dùng không phải đoán mỗi lần.

**Thông tin tĩnh, ít thay đổi**
Nội dung cố định thì cứ hiển thị trực tiếp — không cần AI sinh lại mỗi lần.

**Lỗi quá tốn kém**
Chi phí của một lần sai lớn hơn lợi ích của nhiều lần đúng.

**Yêu cầu minh bạch tuyệt đối**
Mọi quyết định phải giải thích được từng bước, truy vết được.

**Tối ưu tốc độ & chi phí thấp**
Cần ra thị trường nhanh (time-to-market), vận hành rẻ — AI chỉ thêm độ trễ và chi phí.

**Việc giá trị cao người dùng muốn tự làm**
Tác vụ mang ý nghĩa cá nhân mà người dùng KHÔNG muốn bị tự động hóa.

> **Rule/heuristic dễ build, dễ giải thích, dễ debug và bảo trì hơn** — nếu nó giải quyết được, đó là lựa chọn tối ưu.

---

## 14. Hệ thống AI = Model + Context + Planning + Tools

*Một giải pháp AI thực tế là một hệ thống nhiều thành phần, không chỉ dừng lại ở mô hình ngôn ngữ.*

```
                    Model (LLM · SLM)
                  [Hallucination · Cost]
                          ↕
Context ←→   Orchestrator / System Logic   ←→ Tools
(RAG·Memory)         ↕                      (APIs·Actions)
[Wrong Retrieval] [Loops · Bad Policy]   [Side Effects·Security]
                          ↕
                Planning (Steps · Policies)
```

| Thành phần | Vai trò |
|---|---|
| **MODEL** — Tư duy & Sáng tạo | Xử lý đọc hiểu, soạn thảo, tổng hợp, phân loại và đưa ra gợi ý |
| **CONTEXT** — Tri thức chuyên biệt | Cơ sở dữ liệu, tài liệu nghiệp vụ, hồ sơ lịch sử giúp AI phản hồi chính xác theo bối cảnh |
| **PLANNING** — Điều phối quy trình | Tự động phân rã tác vụ phức tạp và linh hoạt điều chỉnh |
| **TOOLS** — Liên kết hệ thống | Tích hợp CRM, database, lịch làm việc hoặc API bên thứ ba |

> **Giải pháp AI là một HỆ THỐNG — model chỉ là một thành phần.**

**Nguồn:** Anthropic — Building effective agents · Chip Huyen — AI Engineering

---

## 15. Automation vs Augmentation (PAIR bước ②)

*Với từng tác vụ, AI nên làm thay hay hỗ trợ con người?*

### AUTOMATE — AI làm thay
Chọn khi:
- Việc khó, nhàm chán, nguy hiểm hoặc cần scale
- Người dùng thiếu kiến thức / khả năng tự làm
- Có "đáp án đúng" mà mọi người cùng đồng thuận

**Đo thành công bằng:** hiệu quả tăng · an toàn hơn · giảm việc tẻ nhạt.

### AUGMENT — AI hỗ trợ con người
Chọn khi:
- Người dùng thích tự làm việc đó
- Stakes cao: tiền bạc, pháp lý, sức khỏe
- Kết quả cần trách nhiệm cá nhân / social capital
- Sở thích khó diễn đạt thành lời

**Đo bằng:** mức độ thích thú · cảm giác kiểm soát · sáng tạo tăng.

> Quyết định theo **từng tác vụ**. Việc đã automate vẫn gần như luôn cần human oversight — preview, edit, undo.

---

## 16. Ba mức giải pháp: Rule / Workflow / Agent

*Rule/Workflow/Agent là cấp độ **KỸ THUẬT** — còn Automate/Augment (PAIR) là cấp độ **VAI TRÒ** của con người trong hệ thống.*

### Cấp độ 1 — Rule / Script
- Đầu vào ổn định, ít thay đổi
- Logic viết được thành if/else
- Cần kết quả luôn đúng 100%
- Quy định pháp lý / tuân thủ chặt

*Ví dụ:* Tính thuế · chặn email spam theo từ khóa · auto-reply theo template.

### Cấp độ 2 — LLM Feature / Workflow
- Đầu vào đa dạng, không viết hết rule được
- Đầu ra cần linh hoạt (tóm tắt, dịch, phân loại)
- Có cách đo chất lượng
- Người có thể kiểm tra trước khi gửi

*Ví dụ:* Tóm tắt email · chatbot FAQ · phân loại ticket hỗ trợ.

### Cấp độ 3 — Agent
- Nhiều bước, dùng nhiều công cụ
- Tình huống thay đổi liên tục
- Cần tự ra quyết định giữa các bước
- Có kiểm soát rủi ro rõ ràng

*Ví dụ:* Agent nghiên cứu thị trường · coding agent sửa nhiều file.

> **Thứ tự ưu tiên thực dụng:** bắt đầu từ bên trái, chỉ đi sang bên phải khi giá trị tăng hơn độ phức tạp.

---

## 17. Một tình huống, ba cấp độ giải pháp

*Ví dụ: hỗ trợ học viên trong khóa học.*

**CẤP ĐỘ 1 — RULE (luật tĩnh): Trả lời tự động**
- Tự động trả lời FAQ, gửi link thời khóa biểu
- Gửi tài liệu sửa lỗi cài đặt cơ bản
- Nhắc nhở checklist nộp bài

*Khi nào?* Logic tường minh, kết quả cố định.

**CẤP ĐỘ 2 — WORKFLOW (quy trình): Duyệt Problem Card**
- AI kiểm tra độ đầy đủ của Problem Card
- Yêu cầu bổ sung nếu thiếu thông tin
- Chuyển cho Trợ giảng giải quyết

*Khi nào?* Có quy trình rõ, AI hỗ trợ từng bước.

**CẤP ĐỘ 3 — AGENT (tác nhân): Đề xuất can thiệp chủ động**
- Tự động theo dõi tiến độ nộp bài
- Phát hiện nhóm học viên bị kẹt lâu
- Chuẩn bị câu trả lời, đề xuất TA duyệt

*Khi nào?* Tình huống động, đa công cụ.

> Không bắt buộc nâng cấp tuần tự từ Rule lên Agent → **dừng ở cấp tối giản nhất** nếu đã đáp ứng mục tiêu đề ra.

---

## 18. Workflow patterns — đủ cho hầu hết bài toán

*Ba mô hình cơ bản theo Anthropic · Building Effective Agents (2024)*

### 1. Prompt Chaining
```
In → LLM Call 1 → Gate → LLM Call 2 → LLM Call 3 → Out
                    └── Gate fail → Exit
```
Chia task thành chuỗi bước tuần tự, có gate kiểm tra giữa các bước.
*VD:* Viết outline → check → viết bài.
**Ý nghĩa quyết định:** đổi độ trễ lấy độ chính xác.

### 2. Routing
```
In → Router → ┌ LLM Call 1 ┐
              │ LLM Call 2 │ → Out
              └ LLM Call 3 ┘
```
Phân loại input → đưa vào nhánh chuyên biệt, tối ưu từng loại riêng.
*VD:* CS query → FAQ / refund / kỹ thuật.
**Ý nghĩa quyết định:** câu dễ đi model rẻ, câu khó đi model mạnh.

### 3. Parallelization
```
In → ┌ LLM Call 1 ┐
     │ LLM Call 2 │ → Aggregator → Out
     └ LLM Call 3 ┘
```
Chạy song song rồi tổng hợp (sectioning), hoặc chạy nhiều lần lấy vote.
*VD:* Guardrail + response đồng thời.
**Ý nghĩa quyết định:** vote để giảm rủi ro một đầu ra sai.

> **Nguyên tắc Anthropic:** Luôn ưu tiên giải pháp đơn giản nhất; chỉ tăng độ phức tạp khi thực sự cần thiết. Ba mô hình cơ bản trên đã đủ đáp ứng hầu hết bài toán thực tế.

---

## 19. Cây quyết định: Lựa chọn cấp độ giải pháp

```
              Bài toán của bạn?
                     │
        ┌────────────┴────────────┐
        │ 1. Volume đủ lớn &      │
        │    lặp đủ thường xuyên? │
        └────────────┬────────────┘
          KHÔNG ←────┤────→ CÓ
             │              │
   [Chưa đáng đầu tư AI     │
    — giải thủ công trước]  │
                 ┌──────────┴──────────┐
                 │ 2. Logic rõ ràng,   │
                 │    input ổn định?   │
                 └──────────┬──────────┘
                     CÓ ←───┤───→ KHÔNG
                      │           │
              [RULE / Script]      │
                       ┌───────────┴────────────┐
                       │ 3. Cần nhiều bước,     │
                       │    nhiều tool,         │
                       │    state thay đổi?     │
                       └───────────┬────────────┘
                          KHÔNG ←──┤──→ CÓ
                            │          │
            [LLM Feature +  │     [AGENT + Controls]
             Human Review]            │
                              [Risk cao? → thêm HITL,
                               rollback, approval]
```

> **Đi từ trên xuống — mỗi nhánh "KHÔNG" là một lần tránh được độ phức tạp không cần thiết.**

**Nguồn:** Anthropic — Building effective agents · Google — Rules of ML

---

## 20. Reward function: hệ thống hiểu "đúng / sai" thế nào? (PAIR bước ③)

**Reward function** là công thức quyết định đâu là dự đoán "đúng", đâu là "sai" — và chính nó định hình trải nghiệm người dùng cuối. Vì vậy nó phải được thiết kế **liên chức năng**: tối thiểu UX × Product × Engineering cùng ngồi lại.

### Bốn kết quả có thể xảy ra
*(Case: AI gợi ý câu trả lời cho câu hỏi của học viên)*

| Kết quả | Mô tả |
|---|---|
| **TP — True Positive** (Đúng-tích cực) | Câu hỏi nghẽn thật → AI gợi ý đúng câu trả lời. Học viên được giải tỏa, TA đỡ tải |
| **TN — True Negative** (Đúng-tiêu cực) | Câu hỏi đã có tài liệu sẵn → AI không can thiệp. Đúng — không cần gợi ý gì thêm |
| **FP — False Positive** (Báo động giả) | AI gợi ý câu trả lời SAI (hallucination) và gửi thẳng cho học viên → học viên đi sai hướng thực hành |
| **FN — False Negative** (Bỏ sót) | Học viên đang kẹt thật nhưng AI bỏ sót, không gợi ý → học viên vẫn chờ lâu như cũ |

> ⚠️ **Chi phí của FP và FN KHÔNG đối xứng** — báo cháy giả ≠ bỏ sót đám cháy. Cân nhắc đánh đổi này là quyết định then chốt khi thiết kế reward function.

---

## 21. Precision ↔ Recall: đánh đổi không tránh khỏi

| PRECISION CAO — `TP / (TP + FP)` | RECALL CAO — `TP / (TP + FN)` |
|---|---|
| Ít gợi ý — nhưng gợi ý nào cũng chắc đúng. Người dùng tin vào từng gợi ý nhận được | Bao trọn mọi trường hợp cần giúp — không học viên nào bị bỏ lại phía sau |
| **Hệ quả:** Nhiều False Negative — bỏ sót học viên đang thực sự cần giúp | **Hệ quả:** Nhiều False Positive — gợi ý sai nhiều, TA phải lọc lại thủ công |

> **Đòn bẩy:** Vặn nút bên này lên, chất lượng bên kia xấu đi.

> **Không có cấu hình đúng tuyệt đối — phải test điểm cân bằng với chính người dùng.**

---

## 22. Viết tiêu chí thành công mà hành động được

*Metric tốt = chỉ số cụ thể + ngưỡng có nghĩa + hành động cụ thể.*

### Template của PAIR

> If **{chỉ số cụ thể}** for **{tính năng AI}** {drops below / goes above} **{ngưỡng có nghĩa}**, we will **{hành động cụ thể}**.

### Ví dụ điền sẵn

> Nếu tỷ lệ câu trả lời AI gợi ý bị TA sửa **> 30% trong 2 tuần**, ta sẽ **hạ mức tự động về pha 1** (chỉ gợi ý, không gửi thẳng cho học viên).

### Checklist trước khi chốt metric

1. Metric có ý nghĩa với **MỌI** người dùng không?
2. Có nhóm nào bị ảnh hưởng tiêu cực không?
3. Đây là thành công của ngày 1 — còn ngày 1000 thì sao?

> Và đừng quên: lên lịch **review metric định kỳ** — tiêu chí thành công cũng cần được bảo trì theo thời gian.

**Nguồn:** PAIR — Ch.1 User Needs + Defining Success · PAIR Worksheet — User Needs (PDF)

---

## 23. Khoảng cách giữa Demo và Production

*Phản hồi chính xác trong vài lần thử chưa đủ cơ sở để triển khai hệ thống thực tế.*

| Hạng mục | Câu hỏi |
|---|---|
| **01 · BASELINE** — Thiết lập đối chứng | Đối chiếu hiệu quả với quy tắc tĩnh, nhân sự hay quy trình hiện tại? |
| **02 · EVALUATION** — Kiểm thử hệ thống | Bộ dữ liệu kiểm thử, kịch bản biên (edge cases) và tiêu chí nghiệm thu? |
| **03 · CONTROLS** — Cơ chế kiểm soát | Logging, fallback, rollback và nhân sự chịu trách nhiệm? |
| **04 · OPERATIONS** — Vận hành liên tục | Ai giám sát lỗi, cập nhật tri thức nền và tối ưu hệ thống? |

> Mục tiêu Day 02 là **xác định tính khả thi để tiếp tục nghiên cứu** — chưa phải quyết định triển khai ngay.

**Nguồn:** Google — Rules of ML · Chip Huyen — AI Engineering

---

## 24. Từ Problem Statement đến Eval Plan

**01 · INPUT — Problem Statement**
9 trường đã hoàn chỉnh — từ Actor, Workflow, Bottleneck đến Boundary & HITL.

**02 · TEST CASES — Kịch bản kiểm thử**
Dữ liệu thực tế và các trường hợp biên (edge cases).

**03 · SUCCESS — Chỉ số hiệu năng**
Đạt yêu cầu (pass) / Không đạt (fail) / Chuyển tiếp kiểm duyệt thủ công (HITL).

### Ba tầng câu hỏi kiểm thử
- **Tác vụ đơn lẻ:** Hệ thống có phân loại chính xác các câu hỏi đầu vào không?
- **Hiệu năng quy trình:** Nhóm học viên có hoàn thành bài lab nhanh hơn và ít kẹt hơn không?
- **Rủi ro & sai số:** Hệ thống có phản hồi sai lệch mà không chuyển tiếp cho Lab Coach phê duyệt không?

---

## 25. Problem Statement cho hệ thống AI — 9 trường

### 6 yếu tố bài toán cốt lõi

| Trường | Nội dung |
|---|---|
| **Actor** — đối tượng ảnh hưởng | Đối tượng trực tiếp chịu ảnh hưởng bởi vấn đề |
| **Workflow** — quy trình hiện tại | Quy trình vận hành hiện tại gồm các bước cụ thể nào? |
| **Bottleneck** — nút thắt | Khâu nào gặp tình trạng chậm trễ, sai sót, lặp lại? |
| **Impact** — tác động | Tổn thất lượng hóa bằng thời gian, chi phí, SLA hoặc chất lượng |
| **Success Metric** — chỉ số thành công | Chỉ số đo lường cụ thể để xác định sự cải thiện |
| **Boundary** — ranh giới | AI không được làm gì; khâu nào bắt buộc có con người |

### 3 yếu tố quyết định AI

| Trường | Nội dung |
|---|---|
| **Điểm AI can thiệp** (`decision · entry`) | AI hỗ trợ hoặc tự động hóa ở bước cụ thể nào? |
| **Mức chọn** (`decision · level`) | Rule / Workflow / Agent? |
| **Rủi ro & HITL** (`decision · safety`) | Phương án xử lý khi AI sai sót và quy trình phê duyệt thủ công |

---

## 26. Khung ra quyết định: Go / Not Yet / No-Go

*Lập luận dựa trên tính khả thi của Problem Statement, tránh thiên kiến công nghệ.*

**✓ GO — thực hiện** *(đủ điều kiện)*
- Bài toán rõ ràng
- Chỉ số đo lường khả thi
- Điểm can thiệp AI phù hợp
- Kiểm soát được rủi ro

**⏸ NOT YET — tạm hoãn** *(có triển vọng)*
- Cần bổ sung dữ liệu thực tế
- Chuẩn hóa quy trình
- Thiết lập chỉ số
- Xác định ranh giới

**✕ NO-GO — không triển khai** *(không phù hợp)*
- AI không mang giá trị vượt trội
- Rủi ro vận hành quá cao
- Giải pháp không dùng AI tối ưu hơn

> **Quyết định "Not Yet" thể hiện sự chín chắn trong tư duy thiết kế sản phẩm, không phải sự thất bại.**

---

## 27. Sáu nguyên tắc cốt lõi sau Day 02

*Kim chỉ nam để thẩm định mọi đề xuất ứng dụng AI.*

**01 · Brief mơ hồ không thay thế Problem Statement.**
Một bản tóm tắt mơ hồ không thể thay thế cho một Problem Statement hoàn chỉnh.

**02 · Mô hình hóa workflow trước khi tích hợp AI.**
Bắt buộc phải mô hình hóa quy trình trước khi xem xét tích hợp giải pháp AI.

**03 · Pain point phải được lượng hóa.**
Mọi điểm đau cần được lượng hóa bằng baseline và chỉ số đo lường cụ thể.

**04 · Phức tạp không đồng nghĩa với hiệu quả.**
Rule, Workflow và Agent là ba cấp độ khác nhau; độ phức tạp kỹ thuật không đồng nghĩa với hiệu quả tối ưu.

**05 · Quyết định dựa trên lập luận thực tế.**
Quyết định Go / Not Yet / No-Go phải được thiết lập dựa trên lập luận thực tế và số liệu kiểm thử rõ ràng.

**06 · Đo reward function bằng trải nghiệm người dùng, không chỉ accuracy.** *(MỚI · PAIR)*
Thiết kế đánh đổi precision ↔ recall theo lợi ích người dùng và kiểm chứng với người dùng thật.

**Nguồn:** PAIR — Ch.1 User Needs + Defining Success

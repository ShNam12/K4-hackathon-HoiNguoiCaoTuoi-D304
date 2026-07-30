# AI IN ACTION — Day 1: AI & LLM Foundation

> *Bạn đang dùng AI mỗi ngày — nhưng thực sự bên trong nó đang làm gì?*
>
> Từ "nghe AI" đến "gọi AI" trong một ngày

---

## Agenda

- Bức tranh AI & các tầng của AI
- Lịch sử AI 70 năm
- Bên trong LLM: cơ chế vận hành
- Từ LLM đến AI Agent
- Landscape: model hôm nay & cuộc đua hiện tại
- Chọn model & chi phí token
- Gọi API lần đầu
- Tổng kết — những ý để mang về

---

## 1. AI, ML, Deep Learning, GenAI, LLM — nằm ở đâu trong cùng một hệ?

Cấu trúc lồng nhau, từ rộng đến hẹp:

```
ARTIFICIAL INTELLIGENCE   ← kể cả hệ luật tay, robot…
 └─ MACHINE LEARNING      ← lọc spam · gợi ý phim
     └─ DEEP LEARNING     ← nhận diện ảnh · giọng nói
         └─ GENERATIVE AI ← văn bản · ảnh · code
             └─ LLM       ← GPT · Claude · Kimi
```

| Tầng | Định nghĩa |
|---|---|
| **AI** | Chiếc ô lớn nhất: mọi hệ thống có yếu tố "thông minh" |
| **Machine Learning** | Học từ dữ liệu thay vì viết luật tay |
| **Deep Learning** | Mạng nơ-ron nhiều tầng tự học đặc trưng |
| **Generative AI** | Sinh nội dung mới: văn bản, ảnh, code |
| **LLM** | Model nền chuyên ngôn ngữ, tim của làn sóng hiện nay |

> **Ý chính:** LLM không phải toàn bộ AI — nhưng nó là tầng nền của gần hết trải nghiệm AI bạn dùng hôm nay.

---

## 2. Ba nhóm AI chính: phân loại · sinh nội dung · hành động

| Nhóm | Mô tả | Luồng |
|---|---|---|
| **Discriminative AI** | Giỏi phân loại, dự đoán: lọc spam, phát hiện gian lận, nhận diện ảnh | Input → một nhãn, một con số |
| **Generative AI** | Sinh ra thứ mới: văn bản, ảnh, code. ChatGPT, Claude, Midjourney | Prompt → nội dung mới |
| **Agentic AI** | Nhận mục tiêu rồi tự làm nhiều bước: lập kế hoạch, dùng công cụ, hành động | Goal → Plan → Action |

> LLM là engine chung của cả Generative lẫn Agentic — cuối buổi sáng sẽ thấy agent khác LLM ở đâu.

**Hành trình khóa học:** LLM Foundation → Agent → Multi-Agent → Deploy → Evaluate

---

## 3. Lịch sử AI 70 năm

### Dòng thời gian

| # | Mốc | Năm |
|---|---|---|
| 1 | Dartmouth Workshop | 1956 |
| 2 | Perceptrons | 1969 |
| 3 | Báo cáo Lighthill | 1973 |
| 4 | Hệ chuyên gia | 1980 |
| 5 | Sụp đổ Lisp machine | 1987 |
| 6 | Deep Learning | 2006 |
| 7 | AlexNet | 2012 |
| 8 | AlphaGo | 2016 |
| 9 | Transformer | 2017 |
| 10 | GPT-1 / BERT | 2018 |
| 11 | ChatGPT | 2022 |
| 12 | Kỷ nguyên Agent | 2024 |
| 13 | Hiện tại | 2026 |

### Các giai đoạn

- **Các cú sốc (1966–1973)**
- **Mùa đông lần 1 (1974–80)**
- **Mùa đông lần 2 (sau 1987)**

### Ba thông điệp

1. **Khai sinh, lời hứa đầu tiên**
2. **2 lần mùa đông, cách tiếp cận chạm trần**
3. **Từ model đơn lẻ sang system có khả năng hành động như agent**

> *Lưu ý: đường cong trong slide minh họa mức "động lực/kỳ vọng" qua các giai đoạn — mang tính KHÁI NIỆM, không phải số liệu đo lường định lượng.*

---

## 4. 1980: Hệ chuyên gia (expert system)

**Đặt lại vấn đề:** *"Nếu AI chỉ giải thật tốt một loại bài toán chuyên môn hẹp thì sao?"*
→ Sự ra đời của **expert systems**

AI đổi chiến lược: thôi theo đuổi trí tuệ tổng quát và **tập trung giải thật tốt một miền hẹp** bằng cách mã hóa tri thức chuyên gia thành luật.

---

## 5. 2009: Fei-Fei Li và ImageNet — cuộc cách mạng của dữ liệu

Trong khi cả ngành chạy theo thuật toán thông minh hơn, Fei-Fei Li chọn con đường khác: **xây bộ dữ liệu lớn hơn** — 14 triệu ảnh được gán nhãn tay, hơn 20.000 loại vật.

Ba năm sau, chính bộ dữ liệu đó là sân khấu cho cú nổ AlexNet 2012 → bài học định hình cả kỷ nguyên: **đôi khi dữ liệu tốt hơn đánh bại thuật toán khôn hơn.**

**Nguồn:** Deng, J. et al. (2009), *"ImageNet: A Large-Scale Hierarchical Image Database"*, CVPR — doi.org/10.1109/CVPR.2009.5206848 · Fei-Fei Li, TED 2015 — ted.com

---

## 6. 2017: Transformer

Bài báo: *Attention Is All You Need* — Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin (Google Brain / Google Research / University of Toronto).

Transformer là bước ngoặt vì nó cho mô hình hiểu ngôn ngữ theo cách linh hoạt hơn: **mỗi từ có thể nhìn sang những từ quan trọng khác** trong cả câu, thay vì chỉ đi tuần tự từng bước → trở thành nền móng kỹ thuật cho GPT, BERT và toàn bộ làn sóng LLM sau đó.

---

## 7. 2022: ChatGPT

**ChatGPT xuất hiện như một trải nghiệm đại chúng.**

Lần đầu tiên rất đông người dùng phổ thông có thể trực tiếp chạm vào một mô hình ngôn ngữ mạnh, thông qua một giao diện đơn giản đến mức ai cũng hiểu cách dùng.

---

## 8. LLM là gì? — một bộ não nền, không phải một chatbot

**LLM (Large Language Model)** là một mô hình ngôn ngữ rất lớn, thường dựa trên kiến trúc Transformer, được luyện trên hàng nghìn tỷ mảnh chữ để học cách đoán mảnh chữ tiếp theo trong ngữ cảnh.

Nhờ được luyện đủ rộng, nó trở thành một **nền chung**: thay vì mỗi việc train một model riêng, cùng một model làm được rất nhiều việc.

```
                    ┌─ 💬 Chatbot
1 model nền (LLM) ──┼─ 📝 Tóm tắt tài liệu
                    ├─ 💻 Viết code
                    └─ 🌐 Dịch & phân tích
```

Chatbot chỉ là một dạng sản phẩm đóng gói quanh bộ não đó — lớp áo bên ngoài.

> **LLM = bộ não ngôn ngữ dùng chung cho mọi việc — sản phẩm bạn thấy chỉ là lớp áo bên ngoài.**

*Ghi chú kỹ thuật:* Model hiện nay chủ yếu là kiến trúc **decoder-only** (GPT, Claude, Gemini, Kimi), nhiều model dùng **MoE**; sau pre-training còn các bước căn chỉnh (SFT, RLHF/DPO) và luyện suy luận (reasoning training, từ ~2025).

---

## 9. Bên trong Transformer: đầu ra luôn là một phân bố xác suất

Ví dụ ngữ cảnh: *"Behold, a wild pi creature, foraging in its native ___"*

Transformer chấm điểm mọi từ trong từ vựng:

| Từ | Xác suất |
|---|---|
| land | 22% |
| forest | 9% |
| country | 5% |
| habitat | 4% |
| forests | 4% |
| soil | 4% |
| territory | 2% |
| woods | 2% |
| lands | 1% |
| waters | 1% |
| woodland | 1% |
| grass | 1% |

> Với mọi ngữ cảnh, model chấm điểm **MỌI từ** trong từ vựng — rồi chọn theo xác suất đó.

**Nguồn:** *Transformers, the tech behind LLMs* — 3Blue1Brown

---

## 10. Sinh văn bản = đoán → nối vào câu → đoán tiếp

Ví dụ minh họa từng bước với câu *"If you could see the underlying probability distributions a large language model uses when generating text, then ___"*:

| Bước | Token được chọn | Xác suất | Các ứng viên khác |
|---|---|---|---|
| 1 | **you** | 74% | it 10%, the 4%, yes 1%, what 1%, I 1% |
| 2 | **would** | 86% | could 13%, might, may, 'd, can, will… |
| 3 | **essentially** | 17% | have 41%, be 32%, gain 4%, likely 2% |

> **Mỗi token mới được nối vào ngữ cảnh, rồi model chạy lại từ đầu — vòng lặp predict → append → rerun.**

**Nguồn:** *Transformers, the tech behind LLMs* — 3Blue1Brown

---

## 11. Token: model không đọc "từ", model đọc mảnh chữ

Model không nhìn từ nguyên vẹn. Nó cắt văn bản thành các **mảnh nhỏ gọi là token**: có từ là một mảnh, có từ vỡ ba bốn mảnh, cả dấu câu và khoảng trắng cũng là mảnh.

**Ví dụ:** *"Hello world"* ≈ 2 token, nhưng *"Xin chào"* có thể tới 3–4 token.

**Tiếng Việt, code, JSON tốn token hơn tiếng Anh thường** — vì dấu thanh, ký tự đặc biệt và cấu trúc bị cắt nhỏ ra.

### So sánh trực quan

| Ngôn ngữ | Câu | Số từ | Số token | Tỉ lệ |
|---|---|---|---|---|
| Tiếng Anh | "To date, the cleverest thinker of all time was" | 9 từ | 11 token | 1.2 token/từ |
| Tiếng Việt | "Lan bỏ quyển sách vào túi vì nó quá dày" | 10 từ | 19 token | 1.9 token/từ |

*Độ dài câu xấp xỉ nhau nhưng tokenizer GPT cắt tiếng Việt vụn hơn hẳn. Điểm quan trọng là tỉ lệ token/từ, không phải tổng số từ. (Tokenizer: cl100k_base — GPT-4.)*

> **Mọi thứ model làm đều quy ra token — và mỗi token đều có giá.** Nhớ điều này khi sang phần chi phí.

**Thử trực tiếp:** platform.openai.com/tokenizer · Số token chính xác phụ thuộc tokenizer của từng model.

---

## 12. Context: bàn làm việc có hạn của model

Mỗi lần trả lời, model chỉ nhìn được một lượng chữ có hạn — gọi là **context**. Hãy hình dung một **bàn làm việc**: mọi thứ muốn model "thấy" phải bày lên bàn.

**Quy đổi:**
- 128K token ≈ một cuốn sách 300 trang
- 1M token ≈ 4–5 cuốn sách trên bàn cùng lúc

**Bàn đầy quá thì đồ ở giữa bàn dễ bị bỏ sót** — đặt điều quan trọng ở giữa một prompt rất dài, model có thể "quên" mất.

> **Context càng dài càng tốn tiền và càng chậm — bàn rộng không có nghĩa là dùng tốt.**

**Nguồn hiện tượng "quên phần giữa":** Liu et al. (2023), *"Lost in the Middle"* — arxiv.org/abs/2307.03172. Model thế hệ mới đã cải thiện đáng kể nhưng chưa hết hẳn.

---

## 13. Attention: mỗi từ được "nhìn sang" những từ quan trọng khác

Thay vì đọc tuần tự từng chữ, cơ chế **attention** cho phép mỗi token:

1. Chủ động "quay đầu" nhìn lại các token trước đó trong câu
2. Chấm điểm mức độ liên quan của từng token đối với nghĩa của mình
3. Khóa nghĩa theo ngữ cảnh — "nó" là quyển sách hay cái túi, tùy theo nó chú ý vào từ nào

> Đây chính là chữ **T** trong GPT — và là lý do model hiểu ngữ cảnh tốt hơn hẳn các thế hệ trước.

**Video minh họa:** *Attention in transformers, step-by-step* — 3Blue1Brown

---

## 14. Hiểu attention để dùng AI hiệu quả: quản context = quản sự chú ý

Attention có hạn và có "điểm mù". Vì vậy, cách bạn bày context quyết định model chú ý vào đâu:

**① Đặt điều quan trọng đầu – cuối**
Đầu và cuối prompt được chú ý nhiều nhất; đồ ở giữa dễ bị bỏ sót — yêu cầu quan trọng đừng chôn giữa.

**② Giữ bàn làm việc sạch**
Context rác = attention rác. Khi chat dài, tóm tắt lại thay vì kéo theo mọi thứ; khi vibe code, đưa đúng file liên quan, không dán cả repo.

**③ Cho tra sổ thay vì bắt nhớ**
Tài liệu dài: lấy đoạn liên quan nhét vào context (RAG) thay vì trông chờ model nhớ hết hoặc nhét cả cuốn.

> **Agent mạnh không phải vì context khổng lồ — mà vì nó có tools để lấy đúng thứ vào bàn làm việc đúng lúc.**

---

## 15. Tham số (parameter): những "khớp nối" model học được

Sau khi luyện xong, những gì model "biết" nằm trong các con số cố định bên trong gọi là **tham số** — hãy hình dung như khớp nối thần kinh: luyện càng kỹ, các khớp nối càng được siết đúng.

Tham số **không phải thứ bạn chỉnh khi dùng model** — nó được đóng gói sẵn trong "bộ não" (file weights). Bạn chỉ chỉnh được **context** và các **núm vặn lúc gọi** (như temperature).

### So sánh quy mô

| Năm | Model | Tham số | Ẩn dụ |
|---|---|---|---|
| 2020 | GPT-3 | 175 tỷ | Một "bác sĩ đa năng" — mọi token đều đi qua toàn bộ khớp nối (**dense**) |
| 2026 | Kimi K3 | 2.800 tỷ | Một "bệnh viện đa khoa" — mỗi token chỉ gọi vài chuyên gia (**MoE**) |

**Luật chơi 2020–2024:** cứ thêm compute + dữ liệu là model khôn lên một cách dự đoán được (**scaling law**, Kaplan et al. 2020) — test loss giảm theo thang log của compute/dữ liệu.

> **Nhiều tham số ≠ tốn hơn tuyến tính** — nhờ MoE, "bệnh viện" lớn gấp 16 lần mà chi phí mỗi ca khám gần như không đổi.

**Nguồn:** MoE — Shazeer et al. (2017), arxiv.org/abs/1701.06538 · Kimi K3 (16/7/2026): ~2.8 nghìn tỷ tham số MoE — k3-kimi.com

---

## 16. LLM được tạo ra như thế nào? — đọc nhiều, được chỉ, được uốn nắn, luyện đề

| Bước | Tên | Ẩn dụ | Nội dung |
|---|---|---|---|
| ① | **Pre-training** | "Đọc cả thư viện" | Đọc gần như cả internet để học ngôn ngữ & kiến thức từ hàng nghìn tỷ token. *Như đọc vạn cuốn sách nhưng chưa biết cách trả lời.* |
| ② | **SFT** | "Được chỉ cách trả lời" | Người ra ví dụ hỏi–đáp mẫu, model bắt chước cách trả lời. *Như gia sư làm mẫu: "câu này nên đáp thế này".* |
| ③ | **RLHF / DPO** | "Được uốn nắn" | Người chấm câu nào tốt/tệ, model chỉnh cho hợp ý người. *Như biên tập uốn giọng cho lịch sự, hữu ích, an toàn.* |
| ④ | **Luyện suy luận** (từ ~2025) | "Giải đề tự chấm" | Luyện toán/code có đáp án kiểm chứng được → model biết làm nháp trước khi trả lời. |

> **Đọc vạn cuốn sách chưa chắc biết trả lời phỏng vấn — đó là lý do cần bước ②, ③, ④.**

**Nguồn:** Ouyang et al. (2022), InstructGPT — arxiv.org/abs/2203.02155 · Rafailov et al. (2023), DPO — arxiv.org/abs/2305.18290 · RLVR: RL with verifiable rewards.

---

## 17. RLHF: ba bước uốn cỗ máy đoán token thành trợ lý biết nghe lời

**① Model viết nhiều câu trả lời**
Cùng một câu hỏi → LLM sinh ra Trả lời A, B, C, D

**② Người chấm xếp hạng**
```
Trả lời B → 1
Trả lời D → 2
Trả lời A → 3
Trả lời C → 4
        ↓
   REWARD MODEL
(máy chấm điểm thay người)
```

**③ Huấn luyện theo điểm**
LLM → câu trả lời vừa viết → chấm điểm (VD: 9.2/10) → tăng xác suất câu ghi điểm cao

*Lặp lại hàng nghìn lần → model dần "biết nghe lời".*

> **Cỗ máy đoán token + điểm xếp hạng của con người → trợ lý helpful · harmless · honest.**

**Nguồn:** Ouyang et al. (2022), *"Training language models to follow instructions with human feedback"* (InstructGPT) — arxiv.org/abs/2203.02155 · DPO (cách đơn giản hơn, 2023) — arxiv.org/abs/2305.18290

---

## 18. Giới hạn bẩm sinh: học giả trong bong bóng

**Bong bóng thời gian**
Model bị "đóng băng" tại ngày ngừng đọc. Chuyện sau đó nó không biết — trừ khi bạn cung cấp thêm (*knowledge cutoff*).

**Nói chắc như đúng rồi**
Model tối ưu cho câu nghe hợp lý, không phải tra sự thật — nên có thể tự tin mà sai (*hallucination*).

**Bàn làm việc có hạn**
Context có trần; quá dài vừa tốn tiền vừa dễ bỏ sót thông tin ở giữa.

> *"Why does it work? We don't know — a lot here are intuitions, not theorems or truths."*
> — Łukasz Kaiser, đồng tác giả "Attention Is All You Need" (OpenAI)

Đây không phải lỗi tạm thời — đó là **bản chất của cỗ máy đoán token**. Vì vậy ta cần prompt tốt, context sạch, tra sổ (RAG), tools, và luôn kiểm chứng.

> **"Biết nhiều" khác "làm được"**: dữ liệu mới và hành động thật cần tools/retrieval/workflow — nền của các ngày sau.

---

## 19. Vì sao model vẫn sai: nó rất giỏi học vẹt đường tắt

Ba ví dụ *spurious cues* (đường tắt giả):

| # | Bài toán | Model thực chất đã học | Hệ quả |
|---|---|---|---|
| 1 | Phân loại spam | "Đếm số hyperlink trong email" | Email sạch nhưng nhiều link → vẫn bị gán spam |
| 2 | Câu chủ quan vs khách quan | "Có phải câu trích từ film review không" | Ăn gian bằng nguồn gốc câu, không phải nội dung câu |
| 3 | Suy luận ngôn ngữ (MNLI) | "Câu có động từ phủ định" | Đổi cấu trúc dữ liệu test là điểm tụt ngay |

*Ba "đường tắt" trên do chính LLM tự động phát hiện và mô tả bằng ngôn ngữ tự nhiên — trên quy mô 675 bài toán thật của benchmark OpenD5.*

> **Benchmark cao ≠ model hiểu đúng thứ bạn tưởng — luôn test trên dữ liệu của chính mình.**

**Nguồn:** Zhong, Snell, Klein & Steinhardt (2022), *"Describing Differences between Text Distributions with Natural Language"*, ICML 2022 · Zhong et al. (2023), *"Goal Driven Discovery of Distributional Differences via Language Descriptions"* (OpenD5), NeurIPS 2023

---

## 20. Chain-of-Thought: chỉ thêm "giấy nháp", từ sai thành đúng

**Bài toán:** *"Có 5 quả bóng tennis. Mua thêm 2 hộp, mỗi hộp 3 quả. Hỏi tổng cộng có bao nhiêu quả?"*

**Không có nháp — trả lời ngay**
Model đọc câu hỏi → bật ra đáp án ngay: *"Đáp án là 27 quả."* ✗ **SAI**

**Có giấy nháp — "hãy nghĩ từng bước"**
> Bắt đầu có 5 quả.
> Mỗi hộp 3 quả × 2 hộp = 6 quả.
> 5 + 6 = 11.
> Đáp án là 11 quả.

✓ **ĐÚNG**

> Cùng một model, cùng một câu hỏi — cho nó được viết nháp từng bước, bản chất suy luận lộ ra.

**Nguồn:** Wei et al. (2022), *"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"* — arxiv.org/abs/2201.11903 · Đây là mầm của các reasoning model (o1, R1...) và của test-time compute.

---

## 21. Từ LLM đến agent: bốn mức độ

| Level | Tên | Năng lực thêm vào |
|---|---|---|
| **LEVEL 0** | Bộ não suy luận | LLM trần — không công cụ, không dữ liệu mới |
| **LEVEL 1** | Có kết nối | + tools: search web, đọc database, gọi API — vượt khỏi bong bóng thời gian |
| **LEVEL 2** | Biết lập kế hoạch | + tự chia mục tiêu thành nhiều bước, dùng nhiều tool nối tiếp, tự kiểm tra kết quả từng bước |
| **LEVEL 3** | Đội agent phối hợp | + nhiều agent chuyên biệt chia việc như một đội ngũ (multi-agent) |

*Mức tự chủ & tác động thật tăng dần theo level.*

> **Agent không phải "một loại model khác" — đó là LLM được đặt vào vòng làm việc có mục tiêu và hành động.**

---

## 22. Giải phẫu một agent: 5 bộ phận là một vòng lặp

| Bộ phận | Vai trò |
|---|---|
| ① **Goal** | Mục tiêu cần đạt |
| ② **Reasoning** | Bộ não LLM chia bước |
| ③ **Tools** | search · API · database · code |
| ④ **Action** | Hành động ra đời thật |
| **Memory** | Sổ tay ghi nhớ các bước (ghi / đọc xuyên suốt vòng lặp) |

Vòng lặp: Goal → Reasoning → Tools → Action → **quan sát kết quả → lặp lại**

> **Agent = Goal + Reasoning + Tools + Memory + Action — chạy thành vòng lặp cho tới khi xong việc.**

---

## 23. Cùng một mức năng lực, giá rơi khoảng 10 lần mỗi năm

Giá / 1 triệu token input (USD, thang log):

| Model | Giá | Loại |
|---|---|---|
| text-davinci-003 (11/2022) | $20 | Closed |
| GPT-4 | $30 | Closed |
| GPT-4 Turbo | $10 | Closed |
| GPT-4o | $5 | Closed |
| GPT-5.6 | $5 | Closed |
| Gemini 1.5 Pro | $3.5 | Closed |
| GPT-5 | $1.25 | Closed |
| DeepSeek R1 | $0.55 | Open-weight |
| DeepSeek V3 | $0.27 | Open-weight |
| Claude 3 Haiku | $0.25 | Closed |
| DeepSeek V4 | $0.14 | Open-weight |

**Điểm mấu chốt:** cùng mức năng lực GPT-3.5 → **>280× rẻ hơn trong ~2 năm** (11/2022 → 10/2024, từ $20 → $0.07).

> **Việc năm ngoái phải dùng model đắt nhất — năm nay model rẻ đã làm được.**

*Tổng hợp từ bảng giá các nhà cung cấp, 2023–2026.*

---

## 24. Chọn model theo TẦNG, không chọn theo tên

| Việc của bạn | Tầng model |
|---|---|
| **Việc khó nhất** — suy luận nhiều bước · code phức tạp · tài liệu dài · độ tin cậy cao | **TẦNG 1 — FRONTIER ĐÓNG**<br>Fable 5 · GPT-5.6 Sol · Opus 4.8<br>*đắt nhất — chỉ trả cho việc thật sự khó* |
| **Việc hàng ngày** — viết · code · phân tích công việc · automation<br>**Việc đơn giản, khối lượng lớn** — phân loại · trích xuất · tóm tắt ngắn | ★ **TẦNG 2 — RẺ MÀ MẠNH**<br>Sonnet 4.6 · Terra · Gemini 3.1 Pro · Kimi K3 · Haiku · Flash<br>*giải quyết đa số việc hằng ngày — **MẶC ĐỊNH THỬ TẦNG NÀY TRƯỚC*** |
| **Việc cần kiểm soát** — dữ liệu nhạy cảm · chi phí ở quy mô lớn | **TẦNG 3 — SELF-HOST / SIÊU RẺ**<br>Kimi K3 open-weight · DeepSeek · Qwen |

**Hai lỗi đối xứng:**
- ✗ Việc đơn giản mà gọi frontier → phí tiền
- ✗ Việc khó mà cố dùng rẻ → kết quả tệ

> **Bắt đầu từ model đủ tốt và đủ rẻ — chỉ nâng tầng khi kết quả thực sự chặn use case.**

---

## 25. Token có giá: vé vào rẻ, vé ra đắt gấp 3–5 lần

**VÉ VÀO — INPUT (×1)**
Chữ BẠN gửi đi: prompt · system instruction · context · lịch sử chat
*Rẻ — model chỉ cần đọc.*

**VÉ RA — OUTPUT (×3–5)**
Chữ MODEL viết ra — nó phải tự sinh từng mảnh một, vừa chậm vừa tốn
*Đắt — model phải "vắt óc".*

### Hóa đơn — 1 lần gọi API (ví dụ)

```
input    1.150 tok × $3  / 1M    $0.00345
output     200 tok × $15 / 1M    $0.00300
─────────────────────────────────────────
TỔNG                          ≈ $0.0065
```
*Số liệu ví dụ — giá thật tùy model & nhà cung cấp.*

Đọc mục **usage** trong mỗi response — đó là hóa đơn chi tiết giúp bạn kiểm soát chi phí từ ngày đầu.

> **Input tokens + Output tokens = Chi phí mỗi lần gọi — kiểm soát output là núm vặn lớn nhất.**

---

## 26. Giải phẫu một prompt: bốn lớp xếp chồng

| Lớp | Tên | Nội dung | Ví dụ |
|---|---|---|---|
| **1** | System instruction | "Lời dặn đầu ca": model là ai, cư xử thế nào, không được làm gì | «Bạn là trợ lý y khoa, trả lời ngắn gọn, không chẩn đoán…» |
| **2** | User input | Câu hỏi / yêu cầu của người dùng trong lượt này | «Tóm tắt báo cáo Q1 giúp mình» |
| **3** | Context bổ sung | Tài liệu, lịch sử chat, dữ liệu tra sổ — phần bày lên "bàn làm việc" | «[đính kèm: bao_cao_q1.pdf — 3 đoạn liên quan]» |
| **4** | Output mong muốn | Dạng kết quả: gạch đầu dòng? bảng? JSON? dài bao nhiêu? | «3 bullet + 1 rủi ro chính, tiếng Việt» |

> **Viết rõ cả 4 lớp = đã làm tốt một nửa "prompt engineering" — phần còn lại là các ngày sau.**

---

## 27. Hai núm vặn chọn từ: temperature & top_p

### temperature — "núm vặn độ liều"

Cùng một câu: *"Một tách ___"* — bảng xác suất đổi theo T

| T | Hành vi |
|---|---|
| **T = 0** | Luôn chọn từ chắc nhất → ổn định, lặp lại, hợp code & phân tích |
| **T = 1** | Cân bằng tự nhiên — vẫn ưu tiên từ hợp lý |
| **T = 2** | Phân bố phẳng ra → đa dạng, "phiêu", dễ lạc đề |

### top_p — "chỉ xem top đầu bảng" (p = 0.9)

```
① Bảng xác suất gốc: cà phê · trà · mưa · sao
   → giữ nhóm cộng dồn ≥ 90%, cắt & chuẩn hóa lại
② Bảng mới: cà phê · trà · mưa
```

"sao" (đuôi dài xác suất thấp) bị loại khỏi lựa chọn — model chỉ còn chọn trong nhóm đáng tin. **Thường chỉ vặn một trong hai:** temperature hoặc top_p.

> **Lưu ý quan trọng:** hai núm này không làm model thông minh hơn — chỉ đổi cách chọn từ, không thêm tri thức.

> **Mặc định an toàn: temperature = 0 cho việc cần ổn định — chỉ tăng khi thật sự cần đa dạng.**

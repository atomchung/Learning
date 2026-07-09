# 模型進步軌跡與產品迭代方向：半年展望

> 產品經理視角 | 2026 年 5 月
> 延續《Coding Agent 比較分析》的思考——既然 harness 比模型更重要，那「模型還會怎麼變」就直接決定 harness 的設計重心該往哪壓。

## 一、過去三年模型進步軌跡：七條曲線

### 1. Context Window：1000× 擴張，但戰場已轉向 recall

| 時間 | 代表模型 | Context |
|------|---------|---------|
| 2023 Mar | GPT-4 | 8K / 32K |
| 2023 Nov | GPT-4 Turbo | 128K |
| 2024 Mar | Claude 3 | 200K |
| 2024–2025 | Gemini 1.5/2.5 Pro | 1M（demo 至 10M） |
| 2025 | Claude Sonnet 4 | 1M（tier 4 起） |
| 2026 | Grok | 2M |

**洞察**：從 8K → 2M 是 250×，但 needle-in-haystack 準確率才是真戰場。長度本身已不是賣點，能否在 1M context 裡精準 recall 才是。

### 2. SWE-bench Verified：三年 50×，已逼近基準飽和

| 時間 | 模型 | 分數 |
|------|------|------|
| 2023 | GPT-4 | 1.74% |
| 2023 | Claude 2 | 4.80% |
| 2024 Mar | Devin | 13.86%（首個 autonomous agent） |
| 2024 Jun | Claude 3.5 Sonnet | 33.4% |
| 2024 Oct | Claude 3.5 Sonnet (升級) | 49.0% |
| 2025 | Claude Sonnet 4 | 72.7% |
| 2025 | Claude Opus 4.5 | 80.9% |
| 2026 Apr | Claude Opus 4.7 | 87.6% |
| 2026 Apr | GPT-5.5 | 88.7% |
| 2026 May | Claude Mythos Preview | 93.9% |
| 2026 Jul | Claude Fable 5 | **95.0%**（103 個模型中排第一，全為自報分數，暫無獨立驗證） |

**洞察（2026-07 更新）**：SWE-bench Verified 如預期天花板化——2026-07 Fable 5 拿到 95.0%，飽和訊號成立。但戰場已明確轉向 **SWE-bench Pro（隱藏/加大難度任務集）**：Claude Mythos 5 80.3%、Fable 5 80%、Sakana Fugu-Ultra 73.7% 暫居前三，Opus 4.8（在用模型中）69.2%，**新發布的 Grok 4.5 只有 64.7%**——同一時間點裡 Verified 已逼近滿分、Pro 卻還有明顯級距，**真實能力 vs benchmark 分數的 gap 依然是 PM 不能忽略的訊號**，只是「真實能力」的量尺從 Verified 換成了 Pro。

**Grok 4.5 補充（2026-07-08 發布，xAI 自報數字，無第三方驗證）**：SWE-bench Pro 64.7%、DeepSWE 1.1 53%（輸 Opus 4.8 約 6 分）；但 xAI 強調的賣點是 **token 效率**——同一 SWE-bench Pro 任務平均只用 15,954 output tokens，Opus 4.8 (max) 用 67,020，差 4.2 倍。定位是「差不多的分數、少很多 token / 更低成本」而非分數碾壓，呼應 [[harness-beats-model]] 這條「絕對分數不是唯一戰場」的判斷。

**跨家族對比（2026-07-09）**：Artificial Analysis Intelligence Index 上 Grok 4.5 排第四（Fable 5 > GPT-5.5 > Opus 4.8 > Grok 4.5，約 54 分），跟 Google/DeepSeek/Meta 不在同一個賣點軸線上比：
- **Google Gemini 3.1 Pro** 仍是推理/科學類最強（GPQA Diamond 94.3%），跟 Grok 4.5 的 coding 效率賣點是不同戰場
- **DeepSeek**：V3.2/V4 Pro 綜合分數（AA 44）低於 Grok 4.5（54），但價格只要約 1/5，LiveCodeBench 甚至全球第一（93.5%，V4 Pro）——**閉源仍領先，但差距在縮小**
- **Meta Llama 4 Maverick**：主打 10M context，不在同一個「智能/coding」擂台
- **真正的威脅不是這三家，是開源同賽道選手 GLM-5.2**：SWE-bench Pro 62.1%（開源最高），已逼近 Grok 4.5 的 64.7%，價格只要六分之一——**Grok 4.5 靠「效率/低成本」跟 Opus/GPT 拉開差異化，但這個打法本身正被開源模型用更狠的價格追上**，這比「Grok 4.5 輸 Opus 幾分」更值得長期盯

### 3. Reasoning：從 prompt 技巧到原生能力

- **2024 Sep**：OpenAI o1-preview 首發，正式定義 test-time compute scaling law
- **2025**：Claude extended thinking、GPT-5 thinking、DeepSeek-R1 全面 RL on reasoning trace
- **2026**：reasoning 從 sequential CoT → parallel sampling + verifier，思考時間從幾秒 → 幾分鐘

### 4. 多模態：從加法到原生融合

- **2024 May**：GPT-4o 統一 text/vision/audio，語音回應 232ms（近人類 320ms）
- **2024 Oct**：Claude 3.5 Sonnet **Computer Use** public beta，可控游標/鍵盤
- **2025–2026**：Google **Project Mariner** 在 real-world browser automation **達 83.5%**
- **2026 Apr**：Opus 4.7 加入高解析度 vision + long-horizon agentic

### 5. Long-horizon Agent：從分鐘到日

| 時間 | 連續工作能力 |
|------|------------|
| 2024 Mar | Devin：分鐘級單任務 |
| 2025 May | Claude 4 內測連續工作 **約 7 小時** |
| 2025 Q4 | Claude Sonnet 4.5 號稱 **30+ 小時** 連續 coding focus |
| 2026 May | Claude Code **Auto Mode**：多步驟工作流 + human approval gates |

### 6. Cost：旗艦每年降 3–5×，小模型每年降 10×+

| 模型 | 發布 | $/M tokens (in/out) |
|------|------|-------------------|
| GPT-4 | 2023 Mar | $30 / $60 |
| GPT-4 Turbo | 2023 Nov | $10 / $30 |
| GPT-4o | 2024 May | $5 / $15 |
| GPT-4o-mini | 2024 Jul | $0.15 / $0.60 |

從 GPT-4 到 GPT-4o-mini，**同等基礎能力價格約降 100×**，是兩年內。

### 7. Latency：caching 與 speculative decoding 帶來質變

- **Speculative decoding**（2025 進入 production）：**2–3× throughput**，H200 上達 3.6×
- **Prompt / Prefix caching**：對長 prompt **cost ↓ 90%、latency ↓ 85%**
- **對 agent workflow 影響最大**：長 system prompt + 重複 tool use 場景，每 turn 都吃 cache

---

## 二、過去進步的內在邏輯

把上面七條曲線抽象，可以看見四個底層機制：

1. **預訓練紅利見頂 → RL on reasoning trace 接棒**
   - 2024 之前靠把模型做大、餵更多 token；之後靠 inference-time compute + verifier
   - 結果：能力提升的成本曲線從「指數增長硬件投入」轉為「線性增加推理算力」

2. **單次 query → multi-turn → long-horizon agent**
   - 模型從「問答機器」變成「任務執行體」
   - 對應 capability 指標從 MMLU（知識）→ SWE-bench（短任務）→ 長任務基準（仍缺）

3. **Capability 趨同 → harness 工程成為差異化**
   - 旗艦模型 SWE-bench 都在 85-90%，但實際工作流體驗差很多
   - Codex / Antigravity / Claude Code 的差異主要在 harness，不在模型

4. **Cost / latency 從成本問題變成設計參數**
   - 過去：模型太貴，產品要省 token
   - 現在：模型夠便宜，產品可以「奢侈使用」——多步驟驗證、多 agent 平行、預先思考

---

## 三、半年後（2026 Q4 / 2027 Q1）合理推測

### 業界領袖近期公開言論

- **Dario Amodei（2026 Jan, Davos）**：AI 模型「6–12 個月內」可端到端處理大多數軟體工程任務；Anthropic 內部部分工程師已「停止自己寫 code」
- **Sam Altman**：認為已在「滑入 superintelligence」階段
- **Demis Hassabis（2026 May I/O）**：一年內會有「接近可靠完成整個被委派任務」的 agents

### 基於趨勢線的具體推測

| 維度 | 2026 May 現況 | 2026 Q4 / 2027 Q1 推測 |
|------|--------------|----------------------|
| SWE-bench Verified | ~90% | **95%+ 飽和**，業界焦點轉向 SWE-bench Pro / Multi-repo |
| Long-horizon autonomy | 30 小時連續 | **跨日 / 跨週連續任務**出現可靠 baseline |
| Browser / Computer use | Mariner 83.5% | 90%+，「給 URL 完成 e2e 任務」成熟 |
| 旗艦模型成本 | GPT-5.4 $15 output | 再降 **2–3×** |
| 小模型成本 | GPT-4o-mini $0.6 | 接近 **near-zero marginal cost** |
| Context | 1–2M 主流 | 5M+ 標配，10M 出現於前沿 |
| Reasoning 深度 | 幾分鐘思考 | 數小時「持續推理」（自我驗證 + branch） |
| 多模態 | vision + audio + browser | 加入 video generation + 3D / spatial |

### 不會自動解決的問題

這些是「再強的模型也不能單靠規模解決」、要靠 harness / 產品設計補的：

- **可驗證性（verifiability）**：模型再準，產品仍需 ground truth 比對
- **意圖對齊**：模型不知道你「真正」要的是什麼
- **企業級安全 / 審計**：誰做了什麼、何時做、為什麼做
- **跨系統整合**：MCP、API、內部工具串接
- **失敗復原**：30 小時任務跑到第 28 小時崩了怎麼辦
- **多人協作**：agent 與 agent、agent 與人類 review 的工作流

---

## 四、不只是更快更大：新實驗室與非主流賭注

前三章講的是「主流軸線會繼續往哪走」。但真正可能改寫產品形態的，是這些**被主流敘事蓋過、但已有具體論文 / 產品落地**的研究方向。如果只看 SWE-bench 和 context window，會錯過下一個範式。

### 4.1 新實驗室在押什麼（不是大廠繼續做大）

| 實驗室 | 創辦人 | 押的賭注 | 關鍵動作 |
|--------|--------|---------|---------|
| **Thinking Machines** | Mira Murati | **Determinism + Interaction Models**：GPU kernel 隨機性才是 LLM 不可靠的根源；voice AI 應該邊聽邊說內建進權重 | 2025/09《Defeating Nondeterminism》、2026/05《Interaction Models》 |
| **SSI** | Ilya Sutskever | **Straight-shot superintelligence**：不發中間產品，直接做最終 SSI | 估值 $30B、無公開研究、無產品 |
| **Reflection AI** | 前 DeepMind | **RL post-training + autonomous coding** 通往 ASI，美國對標 DeepSeek 的開源前沿 | $20B 估值，Asimov agent 仍 waitlist |
| **Magic Dev** | Eric Steinberger | **超長 context**：LTM-2-mini 100M token，sequence-dim 演算法比 Llama 405B attention 便宜 **~1000×** | Google Cloud 上訓練 Magic-G4/G5 集群 |
| **Liquid AI** | MIT spinoff | **on-device hybrid 架構**：LFM2 在 CPU 上 prefill/decode 比同尺寸快 2× | LFM2.5（2026/01）1.2B backbone 用 28T tokens 重訓 |
| **Sakana AI** | David Ha | **不訓練，用演化合併** 開源模型生新能力 | Nature MI 論文、Datadog 戰略合作 |
| **xAI** | Musk | **Macrohard**：Grok + Tesla AI4 跑 Digital Optimus = 模擬整個軟體公司 | Colossus 2 同時訓 7 個 1T–10T 變體 |
| **Mistral** | Mensch | **Single unified model with dial-able reasoning**：Magistral + Pixtral + Devstral 合一，可調 `reasoning_effort` | Mistral Small 4：119B/6B active MoE，比同檔便宜 5–7× |
| **Recursive Superintelligence** | 2026 新創 | **Self-improving model loop** | 2026/05 募 $650M 專做 RSI |

**洞察**：新血實驗室沒有一家在做「更大的 GPT」。每家都選了一個冷門軸線——determinism、context、merge、on-device、unified reasoning、RSI——這些**全是主流敘事不會講的事**。

### 4.2 八個被低估的研究方向（深度解析）

每個方向用同一框架拆解：**機制 → 玩家 → 為何被低估 → 應用層衝擊 → 基建層衝擊 → 觀察信號**。按「對市場結構的潛在衝擊」由大到小排序。

---

#### (1) Interaction Models — voice / agent UX 範式重寫

**機制是什麼**
現有 voice AI（OpenAI Realtime API、Gemini Live、Pi）都是 LLM 外面包一層 scaffolding：ASR 把語音轉文字、LLM 跑 turn-based 推理、TTS 合成語音、VAD 偵測停頓。Thinking Machines 主張這個 pipeline 是死路——**人類對話不是 turn-based 的**，「邊聽邊說」（包括打斷、附和、停頓）必須**內建進單一網路的權重**，而不是外面用狀態機補。

**誰在做**
- Thinking Machines Lab 2026/05《Interaction Models》manifesto
- DeepMind Project Astra 內部測試類似方向
- OpenAI Realtime API 是「scaffolding 派」代表

**為何被低估**
主流大廠都已經出了 voice API，看起來「voice 解決了」。但任何真用過的人都知道體驗仍像「對講機」——能對話但不像對話。問題不在模型品質，在於範式。

**應用層衝擊（如果成真）**
- **客服 / 銷售 / 招聘 agent** 跨越「自然度」門檻，phone-based AI 真正商用化
- **即時翻譯** 從 turn-by-turn 變成「同聲傳譯」級
- **會議副駕** 可即時插話、追問、糾錯
- **Companion / chat app**（Pi、Replika、Character.ai）面臨體驗洗牌
- **菜單式 IVR 系統**徹底被取代

**基建層衝擊**
- **ASR（Whisper / Deepgram）+ TTS（ElevenLabs / Cartesia）** 公司的獨立護城河被侵蝕——能力被吸進主模型
- **Twilio / Vonage** 等 voice infra 需重新定位為「streaming bidirectional pipe」而非 turn-based
- **WebRTC stack** 重要性上升
- **Inference 需求**從「請求-回應」變成「persistent bidirectional stream」，整個 serving 架構（vLLM、TGI）需要改

**觀察信號**
- Thinking Machines 是否在 2026 下半年釋出 demo 或 API
- OpenAI/Google 是否跟進，把「interaction model」當新產品線
- ElevenLabs 等專業 TTS 公司估值動向

---

#### (2) Diffusion Language Models — 跳出 next-token 範式

**機制是什麼**
所有主流 LLM 都是 autoregressive：一次生成一個 token，下一個依賴前一個，**本質上是序列瓶頸**。Diffusion LM（Mercury 系列）借用影像 diffusion 的思路，**平行同時 denoise 整段文字**——把雜訊輸出逐步精煉成完整段落，而不是一個字一個字蹦。

**誰在做**
- Inception Labs：Mercury Coder Small 在 H100 上 **737 tokens/sec**，比 speed-optimized frontier model 快 **10×**；Mercury 2 比 Claude Haiku 快 **5×**
- 學術界跟進中（Stanford、CMU 多篇 follow-up）
- 預期 Anthropic / OpenAI 內部都在評估

**為何被低估**
所有人預設「LLM = autoregressive Transformer」。但這只是 2017–2026 期間的局部最優解，不是物理定律。

**應用層衝擊（如果成真）**
- **IDE autocomplete / refactor**：游標跟手程度跨過心理門檻，「等模型」消失
- **長文生成**（報告、小說、合約草稿）從分鐘級變秒級
- **即時翻譯字幕**：同聲級
- **Code agent 多步驟任務**：每步都快 5–10×，整個 loop 體感不同
- **Streaming chat UX** 重新設計：不需要打字機效果掩蓋延遲

**基建層衝擊**
- **GPU utilization 模式改變**：autoregressive 是 memory-bound，diffusion 可以填滿並行算力 → 同樣 GPU 跑更多吞吐
- **KV cache 重要性下降**：HBM 需求模式改變，可能撼動 H100/H200/B200 的競爭優勢
- **vLLM / TensorRT-LLM / SGLang 等 serving 框架**需要重大改寫，新一波 inference engine 公司有機會
- **Per-token 成本經濟學翻轉**：API 定價可能從「per token」改為「per request」或「per word」

**觀察信號**
- Mercury 2 是否在企業端拿到大客戶
- 主流 frontier lab 是否發 diffusion-based 模型
- vLLM 等開源 serving 是否加入原生 diffusion 支援

---

#### (3) Verifier's Law — PM 的賽道篩選器

**機制是什麼**
Jason Wei 2025/07 提出：**「答案易驗證」的任務 RL 訓得快**，因為 reward signal 乾淨、可大量自動產生資料。反之，答案模糊、需主觀判斷的任務 RL 很難 work。這直接預測「哪些 vertical 會先被 AI 攻下」——不是市場大小，是 verifiability。

**誰在做**
- OpenAI（o 系列訓練核心思路）、Anthropic、DeepSeek-R1 全在用
- 整個 RL post-training 圈的隱性共識
- Jason Wei 把它說清楚了

**為何被低估**
PM 還在用傳統「市場大小 × 競爭強度 × 進入門檻」選賽道。但這個框架完全沒考慮「AI 會先做掉哪些」。

**應用層衝擊（如果成真）**
- **被快速吃掉的賽道**（具備 ground truth）：
  - 合規檢查（規則明確、可二元判定）
  - Test generation（compile / run 即驗證）
  - 形式驗證、type checking、靜態分析
  - 財報 reconcile、發票對帳、數字審計
  - SQL 生成、資料分析（結果可比對）
  - 棋類、競賽程式、數學證明
  - 自動翻譯（BLEU / 反向翻譯可驗）
- **被延後的賽道**（無 ground truth）：
  - 創意寫作、文案、設計
  - 開放式策略諮詢
  - 純對話陪伴、品味推薦
  - 品牌、藝術指導

**基建層衝擊**
- **驗證器 / 環境 / sandbox** 需求爆發：Browserbase、Anchor、E2B、Modal 這類「給 AI 跑試的環境」變核心 infra
- **E2E test 工具**（Playwright、Cypress、Browserbase）變成訓練資料源
- **Synthetic environment generation** 工具崛起：怎麼快速為新 vertical 生 verifier
- **Formal verification 工具**（Lean、Coq、TLA+）重新熱起來——RL 訓練的最強 reward source

**觀察信號**
- 哪些 vertical SaaS 在 2026 下半年估值縮水（注意 legal tech、compliance tech 被 AI 直擊）
- E2B、Browserbase、Modal 等 sandbox-as-a-service 公司融資動態
- Lean 等 formal proof 系統的 GitHub star 趨勢

---

#### (4) AlphaEvolve 式 RSI Flywheel — 前沿差距可能變指數

**機制是什麼**
AlphaEvolve 是 Google 用 AI 設計 algorithm 的系統，已被用來**回收自家資料中心算力、優化下一代訓練程式碼**——也就是說，AI 在加速「讓 AI 更強」的 loop。這是首次有公開證據的 Recursive Self-Improvement (RSI) 閉環。如果穩定，capability 進步從**線性外推**變**自我複利**。

**誰在做**
- Google DeepMind（AlphaEvolve 已 production deploy）
- Recursive Superintelligence（2026/05 募 $650M 專做 RSI）
- ICLR 2026 開了首個 RSI workshop
- OpenAI / Anthropic 內部大概率有類似工作未公開

**為何被低估**
大家還在按「scaling laws + 線性進步」推測未來。但 RSI 一旦 work，所有預測曲線都要改。

**應用層衝擊（如果成真）**
- **前沿差距從線性 → 指數**：「等開源追上」策略風險暴增
- **多供應商策略變難**：若 Google 拉開差距，Anthropic / OpenAI 應用是否要轉？
- **第二梯隊**（DeepSeek、Mistral、Meta Llama）可能被快速甩開
- **垂直 AI 公司 lock-in 加深**：依附前沿模型的，誰是前沿就跟誰
- **B2B SaaS 護城河重估**：模型供應商可能變寡頭

**基建層衝擊**
- **訓練 GPU 需求**進一步集中，超大集群（10萬+ H100/B200）門檻變高
- **中小 GPU cluster** 投資 ROI 下降，整個 inference / smaller-training 市場分化
- **Inference infra（vs 訓練）** 需求相對加強——大部分人玩不起訓練，但要用模型
- **算力集中度**升為國安議題，主權 AI / chip 出口管制力度加大
- **AI safety / interp** 變得「技術上更急迫」——RSI 是失控風險最高的方向

**觀察信號**
- Google 是否發表 AlphaEvolve 詳細論文 / 第二代
- DeepSeek / Meta 是否在 2026 下半年明顯掉隊
- Recursive Superintelligence 首個 demo 出來
- 美國是否對「self-improving AI」立法

---

#### (5) Test-Time Training (TTT) — Personalization 變權重級

**機制是什麼**
模型不只是用 context window「臨時記住」資訊，而是在推理時**真實更新權重**（通常是 LoRA / adapter）以適應當前任務或用戶。Akyürek et al. 在 ARC 上證明 TTT 比 fine-tuned baseline 高 **6× accuracy**，arXiv 2503.11842 給出理論證明。

**誰在做**
- MIT、Stanford 學術前沿
- 部分推測 OpenAI / Anthropic 內部已實驗
- Open-source 圈尚未普及

**為何被低估**
整個 inference stack 設計都假設「權重是不變的」。要支援 TTT，需要重做 serving、儲存、隔離、權限。

**應用層衝擊（如果成真）**
- **Personalization 從 prompt + memory 變真實微調**：模型真的「記得你」而非「context 裡看到你」
- **企業私有資料 fit 不需要訓練週期**：上傳資料 → 立刻可用
- **每用戶有自己的模型版本**：個人助理、學習導師、編程夥伴變得真正「我的」
- **Coding agent** 適應你的 codebase 風格、commit 慣例、code review 偏好
- **Customer support** 從 RAG 變成「真學會」公司知識庫

**基建層衝擊**
- **Inference stack 大改**：要支援動態權重 update、per-request 微調
- **Per-user model 儲存與版本管理** 成新問題類別——LoRA adapter store、用戶權重 garbage collection
- **Multi-tenancy 模式重設計**：能否在共享 GPU 上隔離 per-user weights
- **LoRA / adapter 基建**從 niche 變核心 infra（Predibase、Together AI 受益）
- **Model 隔離 / 安全**：用戶 A 的 fine-tune 不能洩漏給用戶 B

**觀察信號**
- 主流 model provider 是否推出「per-user fine-tune」原生 API
- LoRA serving 公司（Predibase、Anyscale）的企業客戶數
- Cursor / Claude Code 等 IDE 是否支援「學會你的 codebase」的模式

---

#### (6) Physics-grade World Model — 合成模擬器當訓練資料源

**機制是什麼**
Veo / Sora 那種影片生成是「看起來真實」，但不符合物理定律——掉下來的球軌跡是視覺合理但物理錯。Hassabis 公開講 DeepMind 在做擺鐘、滾球的 **Newton 級基準**。Genie 3 已能即時生成可互動的世界數分鐘。如果模型內部真的有物理引擎級的世界模型，**它就是無限訓練資料的來源**——機器人、自駕、外科手術都不用實體採集。

**誰在做**
- DeepMind：Genie 3、Project Genie（AI Ultra 用戶可用）、V-JEPA 2
- LeCun JEPA 路線：LeWorldModel（arXiv 2603.19312）端到端從像素訓練
- Waymo：fork 自家 Waymo World Model 做自駕模擬
- Tesla、xAI 在 Macrohard 計畫中也在做

**為何被低估**
大家把 world model 看成「Sora 的延伸」——影片生成工具。沒看到它是「資料引擎」。

**應用層衝擊（如果成真）**
- **Robotics**：實體機器人採集瓶頸（昂貴、慢、危險）被繞過，每家機器人公司的資料飛輪變成軟體問題
- **自駕**：corner case 模擬不需要實地撞，安全測試大幅加速
- **遊戲**：procedural generation 全新範式，content cost → 0
- **教育模擬**：物理化學實驗、外科訓練、駕駛訓練變得無限可重複
- **AR / VR**：3D 內容從手工建模到 prompt 生成
- **建築 / 工程**：模擬複雜結構行為（流體、熱、結構力學）

**基建層衝擊**
- **合成資料公司**（Scale AI、Surge AI、Labelbox）的「人工標註」業務部分被替代
- **Robotics 公司估值邏輯改變**：硬體不再是護城河，世界模型才是
- **GPU 需求結構改變**：rendering + training 融合，光柵 / RT core 重新重要
- **NVIDIA Omniverse、Unreal Engine** 角色重塑——從「工具」到「訓練平台」
- **資料中心**對顯存頻寬要求進一步增加（同時跑 simulation + training）

**觀察信號**
- Genie 3 / 4 是否做到「物理可預測」（球落地、水流向、布料碰撞）
- 任何機器人公司公開使用 world model 訓練佔比超過 50%
- Waymo / Tesla 公布合成里程數 vs 實體里程數比例

---

#### (7) Evolutionary Model Merge — Mid-tier 公司的逆襲機會

**機制是什麼**
Sakana AI 證明：不重新訓練、用**演化算法搜尋最佳合併方式**，把多個開源模型的權重組合，可以生出新能力。已登 Nature Machine Intelligence，ICLR 2025 follow-up（CycleQD）。對沒有 H100 集群的公司，這是繞過訓練成本的後門。

**誰在做**
- Sakana AI（David Ha）
- 開源社群 mergekit 工具
- 部分 vertical AI startup 已在 production 使用

**為何被低估**
主流認為「沒 H100 集群就玩不了 frontier」。Sakana 證偽——選對方法，**消費級 GPU 也能造出垂直頂尖模型**。

**應用層衝擊（如果成真）**
- **Mid-tier 公司可造 vertical 模型**：醫療 + reasoning + 中文，三個開源模型 merge 就出來
- **垂直 SaaS 護城河重設**：從「私有資料訓練」轉到「merge 配方 + 評估能力」
- **開源生態加速**：Llama + 領域微調 + reasoning 三明治成標準作法
- **Closed API 中型市場被侵蝕**：原本付 OpenAI / Anthropic 的中型客戶，可能改用 Sakana 風格自製
- **新一波「我們的垂直 AI」公司湧現**

**基建層衝擊**
- **Hugging Face 角色加強**：成為模型「樂高積木」中樞，估值邏輯升級
- **訓練 GPU 需求結構分化**：高端集群更集中（前沿）+ 中低端轉向 merge / small-scale fine-tune
- **Model evaluation infra** 需求爆發：merge 完怎麼驗證能力沒退步、新能力真的有？
- **MLOps 工具**新增「merge pipeline」這個類別
- **Closed API 公司中型市場壓力**：OpenAI / Anthropic 可能要重新定價、加碼 mid-tier 區隔

**觀察信號**
- mergekit 等開源工具 GitHub star / 企業採用
- Hugging Face 上「merged model」佔比
- 是否出現「merge 顧問」公司
- 哪家 vertical AI startup 公開承認用 merge 而非預訓練

---

#### (8) Determinism as a Product — 被嚴重低估的 Enterprise 軸線

**機制是什麼**
所有現有 LLM 即使 temperature=0 也不是 deterministic，因為 GPU kernel 在 batch、reduction、non-associative float ops 上引入隨機。Thinking Machines 第一篇 paper《Defeating Nondeterminism》主張這個是可解的工程問題，不是模型本性。對 regulated industry，**「同樣輸入永遠同樣輸出」是採用門檻**——目前所有 LLM 都過不了。

**誰在做**
- Thinking Machines Lab（2025/09 首篇研究）
- 預期 enterprise-focus 的 inference 公司（Together AI、Fireworks）會跟進

**為何被低估**
大家在追 capability、cost、latency 三軸，忽略 reliability 是 enterprise 真正的採用障礙。「金融 / 醫療 / 法務不用 LLM」不是因為模型笨，是因為**沒法稽核**。

**應用層衝擊（如果成真）**
- **金融、醫療、法務、政府採用門檻消失**：合規流程可以 audit 追溯
- **自動化合規、自動化審計變可能**：模型輸出可重現 = 可驗證 = 可採信
- **AI agent 進入「需審計留痕」的工作流**：trade execution、prescription、legal filing
- **A/B test 和回歸測試重新可行**：模型升級不再是黑箱
- **保險業務**：模型 underwriting 可以被監管接受
- **政府 / 國防**採購大幅放開

**基建層衝擊**
- **Inference engine 重寫**：GPU kernel 確定性化（NVIDIA 可能要出 deterministic mode）
- **MLOps 工具鏈** 重新設計：版本控管、A/B、回歸測試框架
- **「Reproducibility-as-a-Service」變新類別**：類似 DataDog 之於 monitoring
- **雲端 GPU 共享模式可能改變**：確定性需要更嚴的 batch 隔離，可能推升專屬 GPU 需求
- **保險 / 合規 SaaS**（Vanta、Drata 等）新增「AI audit」產品線

**觀察信號**
- Thinking Machines 是否在 2026 下半年釋出 deterministic API
- NVIDIA / AMD 是否推出 deterministic execution mode
- 第一家美國銀行 / 醫院公開部署「核心業務」LLM
- SOC 2 / HIPAA 等合規框架新增 AI 條款

---

### 4.3 跨方向的市場結構推論

把這八個方向疊在一起，看到的不是八個獨立的賭注，而是**幾個共同方向的市場結構移動**：

#### A. Inference 層比 Training 層機會更大

8 個方向裡有 6 個直接重塑 inference stack（Interaction、Diffusion LM、TTT、Verifier env、Determinism、Merge serving）。**Training 集中度只會更高（RSI flywheel 強化），但 inference 層碎片化、機會大開**。

- **受益**：vLLM 替代者、SGLang、Modal、Together AI、Fireworks、Predibase
- **承壓**：純訓練 GPU cluster 提供商（CoreWeave 等需證明 inference 故事）

#### B. 「Sandbox / 環境 / 驗證器」是新一層基建

Verifier's Law、TTT、Determinism、Physics-grade World Model **四個方向都需要「執行環境」**——code sandbox、physical simulator、A/B test harness、formal verifier。

- **受益**：Browserbase、E2B、Modal、Anchor、NVIDIA Omniverse、Unreal Engine
- **新公司類別**：「Verifier-as-a-Service」、「Synthetic Env Generation」

#### C. 開源 vs Closed 的中型市場戰場最激烈

Evolutionary Merge + 開源 frontier 縮小（Llama 4、Mistral、DeepSeek）= **中型 enterprise 客戶大規模回流開源**。OpenAI / Anthropic 必須在 mid-tier 重新拼。

- **受益**：Hugging Face、Together AI、Anyscale、Predibase
- **壓力**：OpenAI / Anthropic 在中端 SaaS 客戶
- **不受影響**：頂尖前沿（RSI flywheel 拉開）+ Claude Code 等深度 harness 整合

#### D. Voice / 多模態 從「外掛」變「原生」

Interaction Models + Physics-grade World Model 兩個方向都在說「不要外面包，要內建」。**過去三年的所有「LLM + 模組」公司護城河被質疑**。

- **承壓**：ElevenLabs、Deepgram、Whisper 為基礎的公司、Hume.ai（情感識別）
- **受益**：能直接觸達原生 multimodal 訓練的大廠

#### E. Regulated Industry 從拒絕到擁抱

Determinism + Verifier's Law + Mech Interp 三個方向共同打開金融 / 醫療 / 法務 / 政府的採用門檻。**這個市場 size 可能比目前 AI 應用市場大一個量級**。

- **受益**：Palantir、Anthropic（safety positioning）、新一波「regulated AI」垂直 SaaS
- **新公司類別**：「AI Audit」、「Reproducibility-as-a-Service」、「AI Compliance」

#### F. Robotics / Physical AI 估值邏輯被改寫

Physics-grade World Model + 開源 VLA 模型（π₀.₅）讓「資料優勢」可以靠模擬器繞過。**機器人公司的護城河從「採集了多少實體 data」變成「世界模型多準確」**。

- **承壓**：純靠資料採集的 robotics（部分 self-driving 早期玩家）
- **受益**：DeepMind、Tesla（同時有硬體 + 模擬器）、Figure、Physical Intelligence
- **新公司類別**：「Simulator-as-a-Service for Robotics」

#### G. 「Per-User Model」可能是下一個應用層大類別

TTT + Memory + Merge 三個方向都指向「每個用戶有自己的模型版本」。**這不是 ChatGPT 那種記得偏好，是真實的權重個人化**。

- **受益**：能做 LoRA serving / 隔離的基建公司
- **新公司類別**：「Personal AI weights」「Identity-bound model」

---

### 4.4 重要研究者的「下一步要解什麼」

- **Karpathy（Sequoia AI Ascent 2026/05）**：從 vibe coding 到 **agentic engineering**，context window 是新槓桿，Software 3.0
- **Noam Brown（Latent Space 2025/06）**：下一步是 **test-time compute × multi-agent civilizations**。2025 IMO 用通用 reasoning LLM 拿金牌（無工具、人類時限）
- **Jason Wei**：**Verifier's Law** 作為 task-selection 框架
- **Yann LeCun**：JEPA 路線仍是核心，LeWorldModel（arXiv 2603.19312）是從像素端到端的第一個穩定 JEPA
- **François Chollet**：ARC-AGI-2 最高分仍只 24%，2026 主題是 **iterative program optimization** 而非更大 LLM
- **Dario Amodei**：講的不是 SWE，是「5–10 年壓縮 50–100 年生物醫學進度」、7–12 年治癒大部分疾病
- **Hassabis**：AGI 兩個必要條件 = **world model + 自動實驗**

**洞察**：研究領袖的對話，從「模型怎麼做大」徹底轉到「**怎麼讓模型解決可驗證、可累積、可自我改進的任務**」。

---

## 五、產品迭代方向：四個必須押的賭注

基於「模型半年內會強到能跑日級任務、但可驗證性與整合永遠是產品層問題」這個判斷：

### 賭注 1：押「可驗證 / 可審查」基建，而非「再強的模型呼叫」

模型 90% → 95%，產品端體感差距很小；但「Artifact 機制」（Antigravity）、「TODO / progress 持久化」（Claude Code）、「diff 預覽 + 中斷」這類**人類能驗證的中間產物**，是用戶決定信任度的關鍵。

**具體做法**：每個 long-horizon 任務都要有 (a) 計畫產物 (b) 過程錄影或日誌 (c) 可逐步審查的 diff (d) 可回放的決策歷史。

### 賭注 2：押「Auto Mode + Approval Gates」雙軌

從 Claude Code Auto Mode 是領先訊號。半年後純「co-pilot」會被淘汰，純「全自動」用戶不敢用。**真正贏的形態是「自動跑 90%，關鍵節點停下來請求批准」**。

**具體做法**：
- 預設低風險動作（讀檔、跑測試）全自動
- 中風險（寫檔、改 schema）批准式
- 高風險（推 prod、刪資料、發訊息）強制人類確認
- 信任度可隨用戶習慣**逐步放寬**

### 賭注 3：押「記憶 / 跨 session 持久化」

模型本身不會記得你；harness 才會。半年後 long-horizon 任務跨日，**memory 系統是基礎建設不是錦上添花**。

**具體做法**：
- 專案級 memory（CLAUDE.md 模式）
- 跨 session 進度（progress 檔）
- 學習用戶偏好（什麼接受、什麼回退）
- 失敗模式記憶（避免重複踩同樣的坑）

### 賭注 4：押「成本當設計參數」而非「成本當約束」

模型成本繼續每年降 3–5×，旗艦級也夠用。**真正的競爭是怎麼「奢侈使用」便宜的模型**：多 agent 平行、多次自我驗證、預先 speculative 跑、用 mini 模型先過濾再上 frontier。

**具體做法**：
- Model routing：簡單任務 Haiku，難題 Opus
- 平行 sampling + verifier 投票
- Prefix caching 把 system prompt + tool schema 鎖定
- 用便宜模型做 dry-run，frontier 模型只在最後一步介入

### 賭注 5（衍生自第四章）：押「Verifier's Law 篩選的賽道」

Jason Wei 的框架直接給 PM 一個 vertical 選賽道的篩選器：**選答案易驗證的領域**，因為 RL 會先把這些 vertical 攻下、模型品質會比泛用任務更快收斂。

**該關注的賽道**：
- 合規與審計（規則明確、可二元判定）
- Test generation / 形式驗證（compile/run 即驗證）
- 財報、數字 reconcile（有 ground truth）
- SQL / 資料分析（結果可比對）
- 程式碼 review（lint + test 雙重驗證）

**不該優先押的賽道**：
- 創意寫作、文案、設計（沒有 ground truth）
- 開放式策略諮詢（多正解）
- 純對話陪伴（驗證主觀）

### 賭注 6：押「下一代架構不一定是更大的 Transformer」

如果 Mercury（diffusion LM）、Mamba-3（SSM）、Liquid LFM2（hybrid）、Sakana 演化合併任何一個 work，你的 inference stack 假設會被推翻。

**具體做法**：
- 抽象掉「Transformer 預設」——產品設計不要綁定 next-token 模式
- 對 latency 敏感的應用，預留 diffusion LM 切換空間
- on-device / edge 場景，關注 SSM 與 hybrid 架構
- 別把護城河押在「我們呼叫 Claude / GPT」這層

---

## 六、給 PM 的決策清單

不要押的方向：

- ❌ **「等模型再強一點再做」**——半年後模型強，但你的產品也沒做出來
- ❌ **「靠 SWE-bench 分數做行銷」**——基準飽和後沒人在意 90% vs 92%
- ❌ **「砸算力堆 raw capability」**——cost 曲線下降，現在的奢侈半年後人人都做得起
- ❌ **「等多模態 / video / 3D 成熟」**——對通用 coding agent 來說，半年內仍是邊緣需求
- ❌ **「把護城河押在 Transformer + Claude/GPT API」**——架構與供應商都可能被新範式打破
- ❌ **「假設模型輸出是隨機的所以無法 enterprise 化」**——Determinism 是被低估的軸線

要押的方向：

- ✅ **Harness 工程**——上下文管理、記憶系統、多 agent 編排
- ✅ **Approval / verification UX**——讓用戶敢把更大任務交給 agent
- ✅ **跨系統整合（MCP / 內部 API）**——模型再強也進不了你的內網
- ✅ **失敗復原**——30 小時任務崩了能不能從 checkpoint 重啟
- ✅ **使用者信任建構**——從 co-pilot → 半自動 → Auto Mode 的漸進路徑設計
- ✅ **Verifier's Law 篩選賽道**——選有 ground truth 的 vertical
- ✅ **架構抽象層**——保留切換 diffusion LM / SSM / merged model 的能力
- ✅ **Deterministic / 可審計工作流**——專攻 regulated industry 的合規門檻

---

## 七、一句話總結

> **半年後模型會強到能跑日級任務，但「人類能不能信任這個任務的結果」永遠是產品層的問題。**
> 不要再做「呼叫模型的 wrapper」，要做「讓人類敢把工作交給模型的基礎設施」。

---

*產出日期：2026-05-21*

### 參考來源

**Context / SWE-bench**
- [AI Context Windows: 4K vs 128K vs 1M vs 10M Tokens (2026) – Local AI Master](https://localaimaster.com/models/context-windows-coding-explained)
- [Gemini 3.0 Pro 1M Context Window Guide – Vertu](https://vertu.com/lifestyle/testing-gemini-3-0-pros-1-million-token-context-window)
- [SWE-Bench Leaderboard May 2026 – marc0.dev](https://www.marc0.dev/en/leaderboard)
- [SWE-Bench Pro Leaderboard – MorphLLM](https://www.morphllm.com/swe-bench-pro)
- [Claude SWE-Bench Performance – Anthropic](https://www.anthropic.com/engineering/swe-bench-sonnet)

**模型發布**
- [Introducing Claude Opus 4.7 – Anthropic](https://www.anthropic.com/news/claude-opus-4-7)
- [Introducing Claude 4 – Anthropic](https://www.anthropic.com/news/claude-4)
- [Introducing Claude Sonnet 4.5 – Anthropic](https://www.anthropic.com/news/claude-sonnet-4-5)
- [Inside Claude Code Auto Mode – InfoQ (May 2026)](https://www.infoq.com/news/2026/05/anthropic-claude-code-auto-mode/)
- [Hello GPT-4o – OpenAI](https://openai.com/index/hello-gpt-4o/)
- [Learning to reason with LLMs – OpenAI (o1)](https://openai.com/index/learning-to-reason-with-llms/)
- [Introducing computer use, Claude 3.5 Sonnet – Anthropic (Oct 2024)](https://www.anthropic.com/news/3-5-models-and-computer-use)
- [Introducing Devin – Cognition](https://cognition.ai/blog/introducing-devin)

**Cost / Latency**
- [AI API Pricing History – TokenMix](https://tokenmix.ai/blog/ai-pricing-trends-history)
- [Speculative Decoding 2-3x Speedup – Introl](https://introl.com/blog/speculative-decoding-llm-inference-speedup-guide-2025)
- [Prompt Caching Infrastructure – Introl](https://introl.com/blog/prompt-caching-infrastructure-llm-cost-latency-reduction-guide-2025)

**業界領袖預測**
- [Dario Amodei's Forecast on SWE Automation – Quasa](https://quasa.io/media/dario-amodei-s-bold-forecast-ai-on-the-brink-of-revolutionizing-software-engineering)
- [Davos 2026: Hassabis, Amodei, LeCun on AGI – Fortune](https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/)
- [Hassabis: AGI 'Just a Few Years' Away – Startup Fortune](https://startupfortune.com/hassabis-says-agi-is-just-a-few-years-away-forcing-startups-to-rethink-timelines/)
- [Dario Amodei: Machines of Loving Grace](https://www.darioamodei.com/essay/machines-of-loving-grace)
- [Dario Amodei: The Adolescence of Technology](https://www.darioamodei.com/essay/the-adolescence-of-technology)
- [Hassabis: World Models & Infinite Training Loops – Humanoids Daily](https://www.humanoidsdaily.com/news/deepmind-ceo-demis-hassabis-world-models-and-infinite-training-loops-are-the-keys-to-agi)

**新實驗室**
- [Thinking Machines: Interaction Models – TechCrunch (May 2026)](https://techcrunch.com/2026/05/11/thinking-machines-wants-to-build-an-ai-that-actually-listens-while-it-talks/)
- [Thinking Machines: Defeating Nondeterminism – AIInsider (Sep 2025)](https://theaiinsider.tech/2025/09/12/mira-muratis-thinking-machines-lab-publishes-first-research-on-deterministic-ai-models/)
- [Mira Murati Interaction Models Preview – Semafor](https://www.semafor.com/article/05/13/2026/mira-muratis-thinking-machines-previews-interaction-models)
- [Reflection AI $2B Raise – TechCrunch (Oct 2025)](https://techcrunch.com/2025/10/09/reflection-raises-2b-to-be-americas-open-frontier-ai-lab-challenging-deepseek/)
- [Inside Reflection AI $20B – Turing Post](https://www.turingpost.com/p/reflectionai)
- [Magic.dev: 100M Token Context Windows](https://magic.dev/blog/100m-token-context-windows)
- [Liquid AI LFM2 Announcement](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models)
- [LFM2.5 Release – MarkTechPost (Jan 2026)](https://www.marktechpost.com/2026/01/06/liquid-ai-releases-lfm2-5-a-compact-ai-model-family-for-real-on-device-agents/)
- [Sakana AI Series B](https://sakana.ai/series-b/)
- [Mistral Small 4 – MarkTechPost (Mar 2026)](https://www.marktechpost.com/2026/03/16/mistral-ai-releases-mistral-small-4-a-119b-parameter-moe-model-that-unifies-instruct-reasoning-and-multimodal-workloads/)
- [Macrohard – CNBC (Mar 2026)](https://www.cnbc.com/2026/03/11/musk-unveils-joint-tesla-xai-project-macrohard.html)
- [Recursive Superintelligence $650M Raise – SiliconAngle](https://siliconangle.com/2026/05/13/recursive-superintelligence-raises-650m-build-self-improving-ai-models/)
- [ICLR 2026 RSI Workshop](https://recursive-workshop.github.io/)
- [SSI Inc.](https://ssi.inc/)

**非主流研究方向**
- [LFM2 Technical Report (arXiv 2511.23404)](https://arxiv.org/abs/2511.23404)
- [V-JEPA 2 (arXiv 2506.09985)](https://arxiv.org/pdf/2506.09985)
- [LeWorldModel (arXiv 2603.19312)](https://arxiv.org/abs/2603.19312)
- [Genie 3 – DeepMind](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)
- [Titans: Learning to Memorize at Test Time (arXiv 2501.00663)](https://arxiv.org/abs/2501.00663)
- [Mercury Diffusion LM (arXiv 2506.17298)](https://arxiv.org/abs/2506.17298)
- [Mercury 2 Review – MindStudio](https://www.mindstudio.ai/blog/what-is-mercury-2-diffusion-language-model-inception-labs)
- [π₀.₅ Embodied VLA (arXiv 2504.16054)](https://arxiv.org/abs/2504.16054)
- [AgentSociety: 10k+ Agent Simulation (arXiv 2502.08691)](https://arxiv.org/abs/2502.08691)
- [Akyürek TTT for Few-Shot ARC (arXiv 2411.07279)](https://arxiv.org/abs/2411.07279)
- [TTT Provably Improves Transformers (arXiv 2503.11842)](https://arxiv.org/pdf/2503.11842)
- [ARC Prize 2025 Technical Report (arXiv 2601.10904)](https://arxiv.org/abs/2601.10904)
- [Mamba-3 / SSM 2026 Guide – Spheron](https://www.spheron.network/blog/mamba-3-state-space-model-gpu-cloud-deployment/)
- [Post-Training Techniques 2026 – LLM Stats](https://llm-stats.com/blog/research/post-training-techniques-2026)
- [Anthropic Transformer Circuits Update – July 2025](https://transformer-circuits.pub/2025/july-update/index.html)

**研究者觀點**
- [Karpathy: Software 3.0 – Latent Space](https://www.latent.space/p/s3)
- [Karpathy: Sequoia Ascent 2026 Notes](https://karpathy.bearblog.dev/sequoia-ascent-2026/)
- [Noam Brown: Test-Time Compute × Multi-Agent – Latent Space](https://www.latent.space/p/scaling-test-time-compute-to-multi)
- [Jason Wei: Verifier's Law](https://www.jasonwei.net/blog/asymmetry-of-verification-and-verifiers-law)

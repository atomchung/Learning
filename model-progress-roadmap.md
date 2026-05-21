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

**洞察**：SWE-bench Verified 即將天花板化（>95% 在半年內可預期）。但 **SWE-bench Pro（隱藏任務集）只有 ~46%**，揭示了訓練污染問題。**真實能力 vs benchmark 分數的 gap 是 PM 不能忽略的訊號**。

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

### 4.2 八個被低估的研究方向（按產品衝擊排序）

#### (1) Interaction Models — 改寫 voice / agent UX

Thinking Machines 2026/05 manifesto 直指 OpenAI Realtime API 那種「turn-based LLM 外面包 scaffolding」是死路。原生「邊聽邊說」內建進權重的單一網路，**如果 work，整層 voice middleware 被淘汰**。

**產品意涵**：voice agent、即時翻譯、會議副駕的競爭格局可能在 2027 重洗。

#### (2) Diffusion Language Models — 跳出 next-token 範式

Inception Labs **Mercury** 在 H100 上 737 tokens/sec，**比 speed-optimized frontier model 快 10×**；Mercury 2 比 Claude Haiku 快 5×。這不是「再快一點」，是新的 GPU utilization 範式。

**產品意涵**：長文 / code 生成的延遲成本結構整個翻。autocomplete、即時 refactor、實時對話都會被擠壓重定義。

#### (3) Verifier's Law as Product Roadmap

Jason Wei（2025/07）：**RL 訓得快的，永遠是答案易驗證的任務**。這直接告訴 PM「下半年哪些 vertical 會先被 AI 攻下」——不是泛泛的「寫程式」，而是**合規檢查、test generation、形式驗證、財報數字 reconcile、SQL 結果比對**這類答案有 ground truth 的領域。

**產品意涵**：垂直 SaaS 應該按「verifiability」軸選賽道，而不是「市場大小」。

#### (4) AlphaEvolve 式的內部 RSI flywheel

Google 已用 AlphaEvolve **回收算力、加速下一代 AlphaEvolve 自己的訓練**。這是首次有公開證據的 RSI 閉環。ICLR 2026 開了首個 RSI workshop（2026/04），Recursive Superintelligence 公司同年 5 月募 $650M。

**產品意涵**：前沿模型差距可能從**線性**變**指數**拉開。B2B 模型供應商護城河不是參數量，是 self-improvement loop 速度。下游應用層押誰、是否該綁定多供應商，這個決策變得更難。

#### (5) Test-Time Training (TTT) — Personalization 變權重級

Akyürek et al.（arXiv 2411.07279）在 ARC 上 TTT 比 fine-tuned baseline 高 **6× accuracy**；8B 模型在 public val 拿 53%。這意味著「在使用時微調自己」可行。

**產品意涵**：未來每個用戶可能擁有「在自己 context 上現場微調過」的模型實例。Personalization 不再是 memory + prompt，是**真實權重更新**。對 enterprise 私有資料 fit、對個人化偏好建模，是降維打擊。

#### (6) Physics-grade World Model — 合成模擬器當訓練資料源

Hassabis 在 India AI Summit 2026 明說：**Veo 的影片只是「看起來真實」，不是 physics-grade**。DeepMind 正在做擺鐘、滾球的 Newton 級基準。Genie 3 已可即時生成可互動世界，Waymo 已 fork 做自駕模擬。

**產品意涵**：機器人、自駕、遊戲、教育模擬的「實體採集瓶頸」被合成模擬器繞過。對 robotics / 自駕 startup 而言，**有沒有自家 world model = 有沒有資料飛輪**。

#### (7) Evolutionary Model Merge — Mid-tier 公司的逆襲機會

Sakana 證明「不訓練、合併現有開源模型」可以生產新能力，登 Nature MI。對沒有 H100 集群的中型公司，**這是繞過訓練成本的後門**。

**產品意涵**：垂直領域可以用「Llama + 自家領域微調 + 開源 reasoning 模型」merge 出客製模型，不用從頭預訓練。降低了 vertical AI 的門檻。

#### (8) Determinism as a Product

Thinking Machines 第一篇 paper 押的就是這個。**對 regulated industry（金融、醫療、法務）來說，「同樣的輸入永遠給同樣的輸出」是採用門檻**——目前所有 LLM 都過不了。

**產品意涵**：這是被 cost / latency 嚴重蓋過的第三軸線。誰先做出真 deterministic inference，就吃下整個 enterprise compliance 市場。

### 4.3 重要研究者的「下一步要解什麼」

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

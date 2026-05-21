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

## 四、產品迭代方向：四個必須押的賭注

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

---

## 五、給 PM 的決策清單

不要押的方向：

- ❌ **「等模型再強一點再做」**——半年後模型強，但你的產品也沒做出來
- ❌ **「靠 SWE-bench 分數做行銷」**——基準飽和後沒人在意 90% vs 92%
- ❌ **「砸算力堆 raw capability」**——cost 曲線下降，現在的奢侈半年後人人都做得起
- ❌ **「等多模態 / video / 3D 成熟」**——對通用 coding agent 來說，半年內仍是邊緣需求

要押的方向：

- ✅ **Harness 工程**——上下文管理、記憶系統、多 agent 編排
- ✅ **Approval / verification UX**——讓用戶敢把更大任務交給 agent
- ✅ **跨系統整合（MCP / 內部 API）**——模型再強也進不了你的內網
- ✅ **失敗復原**——30 小時任務崩了能不能從 checkpoint 重啟
- ✅ **使用者信任建構**——從 co-pilot → 半自動 → Auto Mode 的漸進路徑設計

---

## 六、一句話總結

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

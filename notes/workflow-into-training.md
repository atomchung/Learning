# 流程怎麼變成模型訓練的一部分 + 模型/流程/harness 的移動邊界 + wrapper 護城河

> 2026-07-20。使用者問四件事：①現在 agent 怎麼把「流程」變成模型訓練的一部分？②模型、流程、harness 之後怎麼拆？③Cursor/Devin/Claude Code/Codex 真能靠 loop 變好嗎？④有沒有論文/分享？⑤wrapper（用戶說 Wrapplets）未來有沒有基於用戶的獨特護城河？
>
> 接續同 session 的「地板 vs 天花板」卡，與 profile 開放疑問「harness 邊界之戰」（07-19 已結算 ✅兩層共存）。

## 先記預測（校準用）

答前我猜：①機制主線＝RL＋可驗證獎勵（跑軌跡、verifier 給分、把決策策略壓進權重）＋軌跡蒸餾；②推理時 loop 幫所有產品但不是護城河，訓練時飛輪被「不訓練預設」綁住；③wrapper 護城河≠workflow（會商品化），是分布＋數據權＋切換成本。

查證後：**方向全中**。搜尋只加銳一點——**「no-train 預設值」對飛輪的節流比通稿講的更硬**（最值錢的私有碼合約上不可訓）。

## 一句話

「流程變成訓練」＝把 harness 裡原本用 prompt/if-else 寫死的決策策略，用 **RL＋可驗證獎勵**壓進模型權重；能壓進去的前提永遠是那個 verifier。所以模型、流程、harness 不會合一，而是沿「可驗證性 × 頻率 × 穩定性」這條線各自往兩端分化。

## 1. 機制：流程怎麼變成訓練（由輕到重）

**軌跡蒸餾（SFT）**
- 讓 agent 用某套 workflow 大量跑任務，把「成功的完整多步軌跡」留下來做監督微調＝把高手動作變訓練樣本。
- SiriuS：把多 agent 成功軌跡存成不斷長大的庫，拿來 bootstrap 自己的訓練課程。老根是 STaR/ReST（模型自己生成、再篩選成訓練數據）。

**可驗證獎勵的 RL（主線，RLVR / 執行反饋）**
- agent 跑多步軌跡，用確定性 verifier 給獎勵：code 過不過測試（RLEF）、跟真實 PR 的相似度（SWE-RL，直接拿 commit/PR/issue 整個軟體演化史當訓練信號）。
- 模型被逼著把「何時搜、何時驗、何時停」這套決策策略吃進權重。
- 難點：多輪 credit assignment、rollout 成本（跑軌跡佔訓練時間大頭）。

**把編排本身 RL 成一個模型（最激進）**
- Sakana Fugu 的 Conductor 用 RL 學出「調度一池模型」的策略，而非手刻 workflow。7B conductor 路由一池大模型。
- 已在 repo：`topics/coding-agents/cards/orchestration-as-a-model-vs-neutral-harness.md`。07-19 這條的自然實驗已結算：編排下沉極致但第三方一測露餡＋一週被開源逆向重建＝**編排住 harness、自搭取代得了**，沒被真正模型化。

## 2. 模型 / 流程 / harness 之後怎麼拆（本次核心判斷）

**邊界不是固定的，是一條移動前線，由三個變量決定誰被吸進模型：可驗證性 × 頻率 × 穩定性。**

- 高可驗證＋高頻＋穩定的編排 → **沉進模型**（好 RL、又省 latency/token）：單步工具選擇、基本 plan-act-verify、reasoning 的自我驗證。
- 需治理/審計＋組織特定＋變得比模型發布還快的 → **留在 harness**：權限、合規閘、長任務狀態、接私有工具、人機交接。

結果不是三層合一，是各自往兩端分化：
- **模型**吃掉「通用可驗證高頻」的流程（天花板層的自動化）。
- **harness** 往上移，從「怎麼 loop」變成「loop 什麼、用什麼護欄、接什麼系統」（治理層）。
- **流程/skill** 是中間膠水，也是最容易被上下吸收的一層——被模型吸（內化）或被 harness 吸（固化成基建）。

這是「流程墊地板」卡的動態版：流程不斷被消化，所以它本身不是護城河。**→ 卡片升級候選 A**：「模型/流程/harness 的邊界是移動前線，由可驗證性×頻率×穩定性決定誰被吸進模型」。

## 3. Cursor / Devin / Claude Code / Codex 真能靠 loop 變好嗎

要拆成兩種 loop，答案完全不同：

**推理時的 loop（不重訓）**
- 全部都行、立刻見效（retry / verify / subagent / maker-checker）。
- 但這是 harness 層，誰都能用也誰都能抄＝墊地板，不是護城河。

**訓練時的 loop（數據飛輪，重訓模型）**——被「不訓練預設值」掐住：
- **Cursor**：明確有飛輪（continued-pretrain＋RL on 產品數據），但 Business/Enterprise 預設 Privacy Mode 開、不拿你的 code 訓練；只有個人檔關掉才會被訓。且 Musk 明說 Cursor 互動數據餵給 Grok。
- **Devin**：企業版合約寫死不訓練（TOS 與隱私政策還內部打架，要各別看）。
- **Codex（OpenAI）/ Claude Code（Anthropic）**：API/企業預設不拿你的數據訓練（Anthropic 商用條款預設不訓；Codex 消費級 ChatGPT 端另計）。

**關鍵反諷**：最有價值的數據（你私有 repo 的真實修改）恰恰合約上碰不得。飛輪多半跑在最弱的數據上（免費檔、公開數據、聚合信號）。所以產品確實變好，但很大一部分**流回底模層**（大家都受惠的聚合信號），專屬某家 wrapper 的私有訓練飛輪被雙重節流。

## 4. 論文 / 分享（標了證據等級）

**機制類（RL 把流程壓進模型）**
- SWE-RL（Meta, 2025-02, arXiv 2502.18449）：軟體演化史＋規則獎勵做 RL
- RLEF: Grounding code LLMs in execution feedback with RL（Meta, Gehring 等 2025）
- The Landscape of Agentic RL for LLMs: A Survey（arXiv 2509.02547）：planning/tool-use/memory/self-improvement 的 RL taxonomy，一站式入口
- Sailing by the Stars: Survey on Reward Models（arXiv 2505.02686）：含 process reward
- 老根：Let's Verify Step by Step（OpenAI, PRM）、STaR / ReST

**產品 / 護城河類**
- Sakasegawa「Does each Coding Agent use your data for training? I read the terms」——直接讀各家條款，正 answer part 3
- Cursor 官方 Data Use & Privacy（cursor.com/data-use）
- Stanford Law「Defensible Moats for Vertical AI Application Companies」（2026-06，比咨詢博客可信）
- repo 內：`notes/sakana-fugu-orchestration-as-model.md`、`notes/cursor-spacex-xai-composer3.md`、`notes/loop-engineering.md`

> 提醒：wrapper-moat 那批多是咨詢/建站服務博客（源頭在賣服務），套「讀信號不讀表面數字」打折看。

## 5. Wrapper 未來有沒有基於用戶的獨特護城河

2026 共識（與我判斷一致）：60–70% wrapper 零營收；活下來靠三樣，但沒一樣是「更好的 workflow」——
1. **分布/嵌入**：成為工作實際發生的地方（system of record），底模廠沒有的通路
2. **數據權＋活飛輪**：不是「有數據」，是「合約上歸你＋有閉環把數據轉成模型改進」
3. **切換成本**：累積的 context/memory/skill/習慣

**我的銳化（比通稿多一層）**：wrapper 的數據飛輪護城河被「no-train 預設值」結構性節流——通稿說「數據飛輪＝護城河」，卻沒算最值錢的私有數據合約上不可訓，飛輪多跑在弱數據上。所以真正穩的 wrapper 護城河更偏「**分布＋切換成本**」，而非「專屬訓練數據」。同構 `topics/ai-industry-reading/cards/llm-call-niches-are-features-not-companies.md`。

**→ 卡片升級候選 B**：「wrapper 數據飛輪護城河被 no-train 預設值結構性節流」。

## 連結

- ↔ `topics/coding-agents/cards/workflow-lifts-floor-model-sets-ceiling.md`（本 note 是它的動態版：流程不斷被上下兩層消化）
- ↔ `topics/coding-agents/cards/orchestration-as-a-model-vs-neutral-harness.md`（把編排 RL 成模型的機制）
- ← `topics/ai-industry-reading/cards/llm-call-niches-are-features-not-companies.md`（wrapper 護城河同結構）
- `notes/loop-engineering.md`（瓶頸是 verifier 不是 model，正是機制的前提）

## 出處（web）

- SWE-RL：https://arxiv.org/html/2502.18449v2
- Agentic RL Survey：https://arxiv.org/abs/2509.02547
- Reward Models Survey：https://arxiv.org/pdf/2505.02686
- Coding agent 條款調查：https://nyosegawa.com/en/posts/coding-agent-terms-investigation/
- Cursor Data Use：https://cursor.com/data-use
- Stanford Law 護城河：law.stanford.edu（Defensible Moats for Vertical AI Application Companies, 2026-06）

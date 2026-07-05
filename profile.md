---
type: interest-profile
maintained-by: claude
updated: 2026-07-04
last-session: 2026-07-05 讀 Thariq「跟 Fable 協作找未知」翻譯全文（四種未知＋六階段 HTML artifact 引導法）。判斷：跟既有「瓶頸移回人」判斷同構,增量在操作清單,補了一塊我自己沒做的（產出後隨堂測驗驗證吸收）。筆記進 main（`notes/finding-unknowns-with-claude.md`）,暫不升卡。詳見 inbox 2026-07-05。上次(07-04)：「強模型幫小模型設計指引」查證＋實測 orchestrator＋v1/v2 A/B,工具不固化,詳 inbox 2026-07-04（三條）
note: 這是「AI 持續記住你」的記憶層。每次 session 我開頭先讀它、結尾更新它，你不必重複交代背景。
discipline: permanent memory 保持小（B8，借 Hermes）。這份＝durable 層（always-load），只放「核心判斷 + 一個最新指標 + note 連結」。演化細節（前次的前次…）下沉 inbox/notes，靠 grep 回憶。別讓話題後面長出「最新…前次…前次」的長鏈。
---

# 你的興趣檔案

> 我（Claude）每次 session 開頭先讀這份、結尾更新這份。
> 所以你隨處丟問題，我都能接著上次、知道你在乎什麼。
> **這份是索引不是內文**：要細節 `grep` inbox.md / notes/（關鍵字、日期）。

## 你持續關注的話題

每條＝主題 + 核心 durable 判斷 + 最新指標（一條）。更早的脈絡在 inbox/notes。

- **AI agents / coding agents** — 最深（~15 卡）。核心：harness>model、沙箱、記憶架構、人機協作、多 agent 編排；loop＝harness 之上第五層（prompt→context→harness→loop，瓶頸是 verifier 不是 model，`notes/loop-engineering.md`）。最新(2026-06-28)：harness>model 拿到**公開榜第三方實測**(Terminal-Bench 上 GPT-5.5 同模型換 harness 差 5.2pt；hash 行定址讓 15 模型同漲 5–14pt)＋產業把「harness」正名(OpenAI/MS)；orchestration 改判「兩層共存」(見預測帳)。記憶卡加邊界：勝負手只在「塞不下」時成立(BEAM/LIGHT ICLR26 背書),塞得下時別上記憶層（`topics/coding-agents/cards/harness-beats-model.md`、inbox 2026-06-28）。
- **Agent OS / Personal OS** — 怎麼做、市場全景、從投資模盤切入個人 OS（4 notes）。核心：agent 協作單位是 PR/diff 不是共享游標、像 git 不像 google doc（`notes/agent-collab-infra.md`）。
- **非工程師怎麼變 AI Power User** — roadmap / user stories / 工作・個人 companion（4 notes，很實戰）。核心診斷：用不上的真因是工作流沒設計階段、不是工具（`notes/claude-design.md`、`ai-power-user-*`）。
- **AI 產業判斷 / 投資訊號** — 讀信號不讀數字、開源商品化計時器、價值流向、中國開源、模型軌跡。核心：記憶體＝三個市場非一個（commodity DRAM/HBM/NAND 定價邏輯不同，混講必誤判）；元判斷「商品週期盯 capex 紀律不盯需求故事」。最新(2026-06-28,**框架 ✅ 強印證**)：Micron Q3 FY26(6-24)毛利率衝 84.9%(一年前 39%),三市場同向但邏輯各異(SNDK 年內~490%)；盯點 capex 紀律一破＝反轉前兆。對位 MU/SNDK（`notes/memory-industry-map.md`、`cxmt-dram-challenge`、inbox 2026-06-28）。
- **MSFT × OpenAI super app** — 平台×模型乘積、Graph/Entra 護城河、Copilot 滲透真假。核心：agent 寫進去的正本留、繞過的 UI 死，排序 身份/安全 > GitHub 基板 > Office（`notes/nadella-frontier-ecosystem.md`）。
- **學習 / 教育加速** — Alpha School、learning roadmap、skills/eval 設計。最新(2026-06-20)：個人攝取流程設計——資訊不稀缺、判斷與校準才稀缺；攝取 5 關瓶頸在壓縮+證偽（`notes/info-intake-routine.md`）。
- **知識系統怎麼設計才真的複利**（元主題＝這個 repo） — 核心：這 repo＝Karpathy LLM wiki 的實例（AI 維護 markdown、預編譯複利），個人預設不需 RAG（`notes/rag-vs-llm-wiki.md`、`claude-code-second-brain-noah-brier.md`）。

## 你當前開放的疑問（＝預測帳）

每條＝問題 + 現狀（✅收斂/追蹤中）+ **`→ 結算訊號`（一個可觀察事件才算到期可判，避免 runaway）** + note + `check:YYYY-MM`（到期回看日）。`/weekly-synthesis` 掃到到期就結算 ✅對 / ❌錯 / ⚪無結論 ＋一句話（**錯的補「為什麼錯」**＝校準燃料）。推理過程在 inbox/notes，grep 回憶。

- **知識系統怎麼對我產生收益？** ✅ 收斂：改造成「repo 是我的腦」記憶層，三拍循環 + SessionStart hook 已落地（CLAUDE.md、`.claude/settings.json`）。
- **部門大腦怎麼從零搭起？**（2026-06-17，`check:2026-07`）追蹤中。三步：整理地圖→梳理 high-level→持續維護。關鍵：痛點是「沒人寫/沒人維護」非檢索（RAG 解錯問題）；勝負手＝寫入成本壓近零 + 維護外包 AI；owner「只審不寫」；起點先畫跨主題地圖+綜述（從 metadata 聚類）。待辦：用戶可能真的套用（`notes/department-brain-process.md`，已 /record）。**→ 結算訊號**：用戶實際套一次（畫了跨主題地圖+綜述），且回報「維護是否真外包給 AI、寫入成本是否近零」。
- **遞迴改進 harness（Issue #6）**（`check:2026-07`）追蹤中＝最活躍的元線。基礎設施已接（`meta/defects.md` + `/meta-review` + R1 防自評）。借鑒 ledger `meta/borrowable-patterns.md`：**B1–B3 已落地 CLAUDE.md**（蒸餾時機前移／連坑一起記／≥3 次出現升級）；**B8 已落地**（profile 三層瘦身，即本檔）；**B9（reflection 先問問題+importance）、B10（外部內容衛生）提案中**。R2/R3：CLAUDE.md 行數要壓回 <200。能刪規則的 RSI 才是對的 RSI。**首次 `/meta-review` 已跑（2026-07-04，結算訊號 ✅：實際砍規則、行數 290→268）**：立第五類 `[write-conflict]`＋CLAUDE.md 加「熱檔寫前 rebase、寫完即 push」＋砍「手機 Obsidian 設定」段（移 notes/obsidian-mobile-setup.md）；Issue #7 裁決不拆 inbox（每日檔擋不住同日並發，兩次衝突都同日），B13 拆檔部分否決 ❌ 進 ledger、B11 驗證訊號已定（write-conflict 至 2026-09 再犯 ≥2 → 升級拆每 session 檔）。B14 二分試點第 1 次：2 題、無 triage-miss。**下輪候選**：env-403（07-04 @user，根治＝用戶調環境 network policy）；false-completion／credibility-miss 再犯即立類；CLAUDE.md 砍行候選＝檔案格式模板段（原子卡/起點卡/journey，~40 行，擬抽 schema 檔留 pointer）、手機可讀性規則（收益有限，可否決）。詳 inbox 2026-07-04。
- **meta-review 迴圈本身值不值得？**（2026-07-04，用戶質疑 B 類收益≈0）追蹤中。**→ 結算訊號**：`write-conflict` 缺陷至 2026-09 再犯次數（`meta/defects.md`）+ 用戶主觀是否感到改善（少花時間解衝突、規則變準）；若到期無感 → 按北極星（Issue #6 目的是省事不是跑儀式）把迴圈砍小或降頻。`check:2026-09`
- **內容層的週綜合**（2026-06-06）✅ 收斂：`weekly-synthesis` skill 已建（`.claude/skills/weekly-synthesis/`），meta-review 的內容層兄弟——每週掃 inbox+notes 抽跨主題模式、結算預測帳、提卡片升級。同步把本段開放疑問改造成**預測帳**（每條帶 `check:`），補上攝取流程第 5 關證偽校準（`notes/info-intake-routine.md`、`claude-code-second-brain-noah-brier.md`）。
- **eval 生態位**（`check:2026-09`）→**命題拆兩層**：promptfoo 被 OpenAI 收編坐實(2026-03,~$86M,被窄化成 red-team)＝單一中立工具易被收編；但中立層換骨不消失,由政府(UK AISI Inspect)/基建大廠(ClickHouse 收 Langfuse、續 MIT)/獨立 vendor 三腿撐厚。判準卡再升級：瓶頸從「寫 rubric」→「judge 在專業領域穩定套用+對齊人類」(arXiv《Learning to Judge》2026-02,專業域相關係數崩到<0.3)。**→ 結算訊號**：promptfoo 是否仍獨立發版且支援非 OpenAI 模型，或功能被併進閉源/綁 OpenAI（`notes/eval-ecosystem-niche.md`、inbox 2026-06-28）。
- **安全/紅隊 eval 值不值得當個人差異化深入？**（`check:2026-08`）部分回應：頂尖攻擊能力會鎖在模型廠內部（Anthropic Mythos），個人差異化落在「驗證/整合/合規」側。**→ 結算訊號**：出現一個「個人靠驗證/合規側做出資安差異化」的實例（或反證＝攻擊能力一路鎖死、外人零空間）（`notes/anthropic-blog-2026-06.md`）。
- **MCP-as-a-rail（Hood）**（`check:2026-12`）→**傾向 ✅(已落地)**：Agentic Trading beta 上線(2026-05-27),MCP 當軌道、開放全部 27.5M 客戶、可接 Claude/ChatGPT/Cursor 任一平台下單；FINRA 年報首度定義「Trade Execution Agent」。孤狼先行,無第二家同等開放。**→ 結算訊號**：是否出現「判斷型 AI 操盤跑贏基準」的第三方實證，或 Hood 改掉交易量計價（`notes/robinhood-agentic-trading.md`、inbox 2026-06-28）。
- **語意 merge 閘門是可投資生態位？**（2026-06-16，`check:2026-09`）判決：大概率 feature 不是 company，同 eval/資安天花板。可投資表達式在外圍：擁 merge 地點的 incumbent / 合規 pure-play / 信任護城河。**→ 結算訊號**：是否出現獨立 merge-gate 公司拿到規模營收（反證我「feature 不是 company」），或被 GitHub/GitLab 原生吃掉（坐實）（`notes/agent-collab-infra.md`）。
- **agent 時代資安計價會崩？**（2026-06-07，`check:2026-10`）→**方向押反,拆兩段**：CRWD Q1 FY27(2026-06-03)net new ARR +32%、指引上修轉加速；PANW Next-Gen ARR +60%——agent＝greenfield 新增被保護對象,**per-seat 短期不崩**。但 per-agent 計價作為**新層**已落地(Okta for AI Agents 4-30 GA)。模型廠 cyber：Anthropic 偏合作(Project Glasswing,partner 含 CRWD/PANW)、OpenAI 偏自營。若 10 月只看「per-seat 崩沒」＝❌。**→ 結算訊號**：CRWD/PANW 財報/定價頁是否出現 per-agent（非 per-seat）計價條目，或模型廠自營 cyber 產品上線（`notes/ai-security-ecosystem.md`、inbox 2026-06-28）。
- **微軟地基何時消失？**（2026-06-15，`check:2026-12`）追蹤中。護城河三層（App 死→Graph→Entra），崩塌觸發＝learning loop 成主要 SoR 且住模型廠不住微軟。反諷：Nadella「擁有 learning loop」正是殺 Graph 的刀。**→ 結算訊號**：出現一個主流 agent 把「正本/learning loop」寫進模型廠側（非 Graph/Entra）的具體產品事件；反向則是 agent 寫入仍預設落 Graph（`notes/nadella-frontier-ecosystem.md`）。
- **Cursor 被收編後還中不中立？**（2026-06-20，`check:2026-09`）→**傾向 ✅(中立性明確劣化)**：SpaceX(已併 xAI)$60B 全股票收 Anysphere(2026-06-16,Q3 完成)；三向劣化——第三方 API 拆獨立計費池、Cursor 3 把 IDE 降 fallback/自家模型設 default、**Anthropic 已切斷 xAI 開發者經 Cursor 用 Claude**。Composer 3「從零預訓練」仍只有官方宣稱、無第三方驗證。**→ 結算訊號**：Cursor 是否仍預設可選 Claude/GPT（中立），或鎖成 Composer-only / 暗降非自家模型體驗（`notes/cursor-spacex-xai-composer3.md`、inbox 2026-06-28）。
- **loop eng 會被 harness 吃掉還是長出外圍治理層？**（2026-06-27，`check:2026-12`）追蹤中＝harness>model 的對沖線。六積木現都在 harness 廠手裡；若連 loop 都被原生吃掉＝護城河更深，若冒出獨立 loop 成本/安全治理層或 verifier-as-a-service＝槓桿再外移一層（同 `llm-call-niches` 結構，外圍才是可投資表達式）。**→ 結算訊號**：是否出現獨立 loop 治理/verifier-as-a-service 拿到付費客戶，或 Claude Code/Cursor 把六積木全原生內建（`notes/loop-engineering.md`）。**數據點(2026-06-28)**：OpenAI 併 ChatGPT+Codex 成單一 surface（Codex 論文）＝模型廠原生吃 harness 又 +1 例（同 Sakana Fugu / Cursor-xAI 方向），偏向「被吃掉」側（`notes/codex-agentic-shift.md`）。
- **orchestration 該住 harness 還是被模型化？**（2026-06-22，`check:2026-12`）→**別二選一,新框架「兩層共存」**：Fugu beta 發表(2026-04-24,fugu-ultra GPQAD 95.1 贏它編排的 Opus 4.6)；同期產業把「harness」正名(OpenAI Model-Native Harness 4-15、MS Agent Framework 1.0 GA 4-03)。**編排能力下沉進模型,但 harness 變承載治理/工具/長任務的殼,兩層並存**；harness 沒被吃反成現金牛(Claude Code run-rate 2 月過 $25 億)。**→ 結算訊號**：Fugu 跑分有無中立第三方複現，且有人實測「自搭 harness 取代不了它」（才證明該被模型化）（`notes/sakana-fugu-orchestration-as-model.md`、inbox 2026-06-28）。
- **Claude Design 對我的 ROI 待實測**（2026-06-14，`check:2026-07`）。契合的是看板/對外卡片/小紅書視覺；已選 personal_os 看板試點，待用戶跑一輪 handoff 回來。**→ 結算訊號**：用戶實跑一輪 personal_os 看板 handoff，回報「省時/視覺值不值得用」（`notes/claude-design.md`）。

## 你可能感興趣的下一題（候選池）

- **動手複製 agent patterns**（已試一輪，2026-07-04）：orchestrator（強）+extraction workers（Haiku）+synthesis（Sonnet）跑通 daily-brief pipeline，四條 best practice 全驗證（見 `notes/prompting-small-models.md`）。**擱置固化**待材料源解鎖。剩：outcomes 迴圈（`/loop`+自寫判準）、個人迷你 eval golden set。
- **產業判讀線**：recall vs context length 才是長上下文真戰場？headless software 重塑軟體形態？中國開源排行榜當地緣訊號？
- **coding-agents 線**：Antigravity 第一方 vs 第三方優化差距？context 壓縮＝選擇性遺忘？trust accumulation 怎麼建？
- **元主題**：卡片到 130 張會不會反難檢索？「待拆的卡」會不會變膨脹債務？時效卡半年後大量過期怎辦？
- **待辦（本機做）**：Fable 有限視窗策略（07-05，`notes/fable-limited-window-strategy.md`）——Fable 5 曾被監管下架 18 天(06-12~06-30)有前例，趁還能用時挑 1-2 條「追蹤中」開放疑問做深度綜合。候選：Issue #6 遞迴改進 harness 完整梳理、loop eng/orchestration 兩條 check:2026-12 長期線。

## 你已沉澱的判斷（指向卡片）

- Harness 影響大於換模型 → `topics/coding-agents/cards/harness-beats-model.md`（Salesforce +79% 來自 review agent+skills；Google DevRel 也淡化 model＝利益相反方驗證）
- 讀 agentic 戰報先分「估計值 vs 實測值」，只信實測
- 讀信號，不讀表面數字 → `topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`
- Eval 是跨模型裁判層，結構上該住模型廠外 → `topics/ai-industry-reading/cards/eval-is-a-cross-model-judge-layer.md`
- Eval 瓶頸是寫判準不是工具，所以個人能搞 agent eval → `topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md`
- 核心動作＝一次 LLM call 的生態位撐不成獨立公司，可投資表達式在外圍三件套 → `topics/ai-industry-reading/cards/llm-call-niches-are-features-not-companies.md`（2026-06-21 週綜合，eval/資安/merge 閘 ≥3 次同結構）
- 知識系統勝負手＝預編譯本地索引、按需 page-in，不重塞 context → `topics/coding-agents/cards/precompile-to-local-index-not-restuff-context.md`（2026-06-21 週綜合）
- 治理靠改預設而非設限，前提是預設接近 Pareto → `topics/ai-industry-reading/cards/defaults-not-restrictions-are-governance.md`（Block 非工程師交付工具＋Armstrong AI 成本砍半，2026-06-28；harness>model 的企業版，同構 repo 原則 #4／Issue #6）
- orchestration 內化成模型是對「harness 中立可換」的反論 → `topics/coding-agents/cards/orchestration-as-a-model-vs-neutral-harness.md`（Sakana Fugu，2026-06-22；劃出 harness-beats-model 的邊界）
- 其餘卡見 `README.md` 地圖（~25 張：ai-industry-reading 9、coding-agents 17）

## 你的工作偏好（我據此調整，不必每次重講）

- 討厭過度工程與儀式；要低門檻、先進 main 讓手機讀得到
- 過程中要多反問拿 feedback，別悶頭做完才報告
- 手機閱讀為主，格式不要破版
- 答案要誠實：做不到就直說、不粉飾；犯錯就認

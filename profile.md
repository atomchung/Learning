---
type: interest-profile
maintained-by: claude
updated: 2026-06-20
last-session: openclaw/Hermes 借鑒點落地 + profile 按 B8 三層瘦身
note: 這是「AI 持續記住你」的記憶層。每次 session 我開頭先讀它、結尾更新它，你不必重複交代背景。
discipline: permanent memory 保持小（B8，借 Hermes）。這份＝durable 層（always-load），只放「核心判斷 + 一個最新指標 + note 連結」。演化細節（前次的前次…）下沉 inbox/notes，靠 grep 回憶。別讓話題後面長出「最新…前次…前次」的長鏈。
---

# 你的興趣檔案

> 我（Claude）每次 session 開頭先讀這份、結尾更新這份。
> 所以你隨處丟問題，我都能接著上次、知道你在乎什麼。
> **這份是索引不是內文**：要細節 `grep` inbox.md / notes/（關鍵字、日期）。

## 你持續關注的話題

每條＝主題 + 核心 durable 判斷 + 最新指標（一條）。更早的脈絡在 inbox/notes。

- **AI agents / coding agents** — 最深（~15 卡）。核心：harness>model、沙箱、記憶架構、人機協作、多 agent 編排。最新(2026-06-20)：Cursor 被 SpaceX/xAI 收編（$60B）——模型力偏科（RL/harness 頂尖、預訓練未證），底模到 2.5 都是 Kimi K2.5、算力是 xAI Colossus；警覺中立 harness 被收編的 model-choice 風險（`notes/cursor-spacex-xai-composer3.md`）。
- **Agent OS / Personal OS** — 怎麼做、市場全景、從投資模盤切入個人 OS（4 notes）。核心：agent 協作單位是 PR/diff 不是共享游標、像 git 不像 google doc（`notes/agent-collab-infra.md`）。
- **非工程師怎麼變 AI Power User** — roadmap / user stories / 工作・個人 companion（4 notes，很實戰）。核心診斷：用不上的真因是工作流沒設計階段、不是工具（`notes/claude-design.md`、`ai-power-user-*`）。
- **AI 產業判斷 / 投資訊號** — 讀信號不讀數字、開源商品化計時器、價值流向、中國開源、模型軌跡。最新(2026-06-20)：Andrew Ng〈Open Platforms Beat Power Plays〉——控制存取權只會加速對手建開放替代品（`notes/ng-open-platforms-beat-power-plays.md`）。
- **MSFT × OpenAI super app** — 平台×模型乘積、Graph/Entra 護城河、Copilot 滲透真假。核心：agent 寫進去的正本留、繞過的 UI 死，排序 身份/安全 > GitHub 基板 > Office（`notes/nadella-frontier-ecosystem.md`）。
- **學習 / 教育加速** — Alpha School、learning roadmap、skills/eval 設計。
- **知識系統怎麼設計才真的複利**（元主題＝這個 repo） — 核心：這 repo＝Karpathy LLM wiki 的實例（AI 維護 markdown、預編譯複利），個人預設不需 RAG（`notes/rag-vs-llm-wiki.md`、`claude-code-second-brain-noah-brier.md`）。

## 你當前開放的疑問

每條＝問題 + 現狀（✅收斂/追蹤中）+ note。推理過程在 inbox/notes，grep 回憶。

- **知識系統怎麼對我產生收益？** ✅ 收斂：改造成「repo 是我的腦」記憶層，三拍循環 + SessionStart hook 已落地（CLAUDE.md、`.claude/settings.json`）。
- **部門大腦怎麼從零搭起？**（2026-06-17）追蹤中。三步：整理地圖→梳理 high-level→持續維護。關鍵：痛點是「沒人寫/沒人維護」非檢索（RAG 解錯問題）；勝負手＝寫入成本壓近零 + 維護外包 AI；owner「只審不寫」；起點先畫跨主題地圖+綜述（從 metadata 聚類）。待辦：用戶可能真的套用（`notes/department-brain-process.md`，已 /record）。
- **遞迴改進 harness（Issue #6）** 追蹤中＝最活躍的元線。基礎設施已接（`meta/defects.md` + `/meta-review` + R1 防自評）。借鑒 ledger `meta/borrowable-patterns.md`：**B1–B3 已落地 CLAUDE.md**（蒸餾時機前移／連坑一起記／≥3 次出現升級）；**B8 已落地**（profile 三層瘦身，即本檔）；**B9（reflection 先問問題+importance）、B10（外部內容衛生）提案中**。待辦：累積缺陷後跑首次 `/meta-review` 驗證。R2/R3：CLAUDE.md 行數要壓回 <200。能刪規則的 RSI 才是對的 RSI。
- **內容層的週綜合**（2026-06-06）追蹤中。睡前是增量的，缺「批次掃整週 inbox+notes、抽跨主題模式」的 pass。B9 正是這條的機制（`notes/claude-code-second-brain-noah-brier.md`）。
- **eval 生態位** 追蹤中：OpenAI 收 promptfoo 後「中立+開源」能撐多久？（`notes/eval-ecosystem-niche.md`）
- **安全/紅隊 eval 值不值得當個人差異化深入？** 部分回應：頂尖攻擊能力會鎖在模型廠內部（Anthropic Mythos），個人差異化落在「驗證/整合/合規」側（`notes/anthropic-blog-2026-06.md`）。
- **MCP-as-a-rail（Hood）** 追蹤中。✅「策略是啥」收斂：Hood 只賣軌道不賣 alpha；AI 操盤機械型有用、判斷型無證據；結構錯位＝交易量計價傷報酬（`notes/robinhood-agentic-trading.md`）。
- **語意 merge 閘門是可投資生態位？**（2026-06-16）判決：大概率 feature 不是 company，同 eval/資安天花板。可投資表達式在外圍：擁 merge 地點的 incumbent / 合規 pure-play / 信任護城河（`notes/agent-collab-infra.md`）。
- **agent 時代資安計價會崩？**（2026-06-07）追蹤中。seat 壓縮 90%、ephemeral，舊 per-seat 計價可能撐不到。追：CRWD/PANW 有沒有 per-agent 計價、模型廠 cyber 是合作還自營（`notes/ai-security-ecosystem.md`）。
- **微軟地基何時消失？**（2026-06-15）追蹤中。護城河三層（App 死→Graph→Entra），崩塌觸發＝learning loop 成主要 SoR 且住模型廠不住微軟。反諷：Nadella「擁有 learning loop」正是殺 Graph 的刀（`notes/nadella-frontier-ecosystem.md`）。
- **Cursor 被收編後還中不中立？**（2026-06-20）追蹤中。整合（算力＋資料）已成事實，真正開放問題＝Cursor 從「中立 harness（可選 Claude/GPT）」變「xAI 自家 harness」後，還讓不讓你爽用 Claude；及 Composer 3「從零預訓練」是否經中立第三方證明（避談底模＝tell）（`notes/cursor-spacex-xai-composer3.md`）。
- **Claude Design 對我的 ROI 待實測**（2026-06-14）。契合的是看板/對外卡片/小紅書視覺；已選 personal_os 看板試點，待用戶跑一輪 handoff 回來（`notes/claude-design.md`）。

## 你可能感興趣的下一題（候選池）

- **動手複製 agent patterns**（待實作）：outcomes 迴圈（`/loop`+自寫判準）、發散/收斂平行子 agent、個人迷你 eval。
- **產業判讀線**：recall vs context length 才是長上下文真戰場？headless software 重塑軟體形態？中國開源排行榜當地緣訊號？
- **coding-agents 線**：Antigravity 第一方 vs 第三方優化差距？context 壓縮＝選擇性遺忘？trust accumulation 怎麼建？
- **元主題**：卡片到 130 張會不會反難檢索？「待拆的卡」會不會變膨脹債務？時效卡半年後大量過期怎辦？

## 你已沉澱的判斷（指向卡片）

- Harness 影響大於換模型 → `topics/coding-agents/cards/harness-beats-model.md`（Salesforce +79% 來自 review agent+skills；Google DevRel 也淡化 model＝利益相反方驗證）
- 讀 agentic 戰報先分「估計值 vs 實測值」，只信實測
- 讀信號，不讀表面數字 → `topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`
- Eval 是跨模型裁判層，結構上該住模型廠外 → `topics/ai-industry-reading/cards/eval-is-a-cross-model-judge-layer.md`
- Eval 瓶頸是寫判準不是工具，所以個人能搞 agent eval → `topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md`
- 其餘卡見 `README.md` 地圖（~22 張：ai-industry-reading 8、coding-agents 15）

## 你的工作偏好（我據此調整，不必每次重講）

- 討厭過度工程與儀式；要低門檻、先進 main 讓手機讀得到
- 過程中要多反問拿 feedback，別悶頭做完才報告
- 手機閱讀為主，格式不要破版
- 答案要誠實：做不到就直說、不粉飾；犯錯就認

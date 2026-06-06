---
type: interest-profile
maintained-by: claude
updated: 2026-06-06
note: 這是「AI 持續記住你」的記憶層。每次 session 我開頭先讀它、結尾更新它，你不必重複交代背景。
---

# 你的興趣檔案

> 我（Claude）每次 session 開頭先讀這份、結尾更新這份。
> 所以你隨處丟問題，我都能接著上次、知道你在乎什麼。

## 你持續關注的話題
（隨口疑問會讓對應話題往上浮；新主題自動長出來。2026-05-30 從 19 份 notes + 3 個卡片主題反推）

- **AI agents / coding agents** — 最深，13 張卡。harness>model、沙箱、記憶架構、人機協作、多 agent 編排；最新讀了 Salesforce 全公司 agentic 化案例（`notes/salesforce-agentic-engineering.md`）
- **Agent OS / Personal OS** — 反覆出現：怎麼做、市場全景、從投資模盤切入個人 OS（4 份 notes）
- **非工程師怎麼變 AI Power User** — roadmap、user stories、工作/個人電腦 companion（4 份 notes，很實戰）
- **AI 產業判斷 / 投資訊號** — 讀信號不讀數字、開源商品化計時器、價值流向、中國開源、模型進步軌跡;最新:Robinhood agentic trading(把 MCP 從開發者工具變成散戶交易/支付軌道,賣軌道+信任框架不賣模型,`notes/robinhood-agentic-trading.md`);前次:Anthropic 5–6 月 blog(`notes/anthropic-blog-2026-06.md`)、eval 生態位(`notes/eval-ecosystem-niche.md`)
- **MSFT × OpenAI super app** — 平台×模型乘積、Graph/Entra 護城河、Copilot 滲透真假
- **學習 / 教育加速** — Alpha School、learning roadmap、skills/eval 設計
- **知識系統怎麼設計才真的複利** — 元主題，就是這個 repo 本身（你正在用它）。最新:聽 Noah Brier「Claude Code as second brain」,確認我們 repo 跟他是同物種(Claude Code+markdown+CLAUDE.md 開機記憶+手機),值得偷他「思考模式硬 gate」「daily/weekly review skill」,我們多押原子卡+遞迴改進兩賭注(`notes/claude-code-second-brain-noah-brier.md`);前次:啟動「遞迴改進 harness」(Issue #6)——從 L1 記憶迴圈進化到 L2 自我改進規則,已接 `meta/defects.md` + `/meta-review` skill

## 你當前開放的疑問
（還沒沉澱成判斷的，追蹤中）

- 這套知識系統怎麼對我產生收益？
  → 2026-05-30 ✅ 收斂：改造成「repo 是我的腦」的記憶層，三拍循環已寫進 CLAUDE.md（見 inbox 2026-05-30 兩條）
  → 2026-05-30 ✅ SessionStart hook 已設（`.claude/settings.json`），boot 全自動

- eval 生態位:OpenAI 收 promptfoo 後,「維持中立 + 開源」能撐多久?模型廠長期有 lock-in 動機。追蹤中(`notes/eval-ecosystem-niche.md`)
- 升值的是安全/紅隊 eval(agent 會不會做壞事)——這塊值不值得當個人差異化技能深入?
  → 2026-06-05 部分回應:Anthropic Mythos(>90% 真陽性、不公開)顯示這塊在升值且被模型廠當戰略級自做。提示天花板——頂尖攻擊能力會鎖在模型廠內部,個人差異化大概落在「驗證/整合/合規」側而非「比模型更會找洞」。(`notes/anthropic-blog-2026-06.md`)

- MCP-as-a-rail：Hood 先發把 MCP 變散戶交易/支付軌道,但 MCP 是開放標準、軌道易被商品化。先發優勢能不能轉成「agent 預設走 Hood」的鎖定?半年內 IBKR/Schwab 跟進會怎樣?追蹤中(`notes/robinhood-agentic-trading.md`)
  → 2026-06-06 ✅「策略是啥」已收斂:Hood 不給策略,只給軌道。AI 操盤分兩型——機械型(你寫規則 AI 執行,價值=紀律/自動化)有用、判斷型(AI 自己選股)無證據(學術 robust backtest 跑輸大盤)。+結構性錯位:Hood 靠交易量賺,AI 傾向過度交易=最傷你報酬。賣軌道≠賣 alpha 成立。

- 遞迴改進 harness（Issue #6）：基礎設施已接（defects + meta-review），社群 best practice 也整合進來了（`notes/recursive-harness-community-patterns.md`）。R1 防自評已落地（meta-review 動規則需至少一筆 `@user` 缺陷）。**R2/R3 待辦**：profile 加軟上限驅逐、CLAUDE.md 283 行要壓回 <200。下一步仍是累積缺陷後跑第一次 `/meta-review`。能刪規則的 RSI 才是對的 RSI。

- **我們系統缺「內容層的週綜合」**（2026-06-06 從 Noah Brier 對照浮現）：現有睡前步驟是增量的（每次只看一條 inbox），缺一個「定期批次掃整週 inbox+notes、主動抽跨主題模式」的 pass。Noah 的 weekly-synthesis 做了這個。對照：我們有 harness 層 review（meta-review/Issue #6）但缺內容層 review。**理想兩個都要**——一個讓知識複利、一個讓系統複利。待辦:考慮做 weekly-synthesis skill（同時掃對話訊號+檔案 mtime）。(`notes/claude-code-second-brain-noah-brier.md`)

## 你可能感興趣的下一題（從 starts/journeys 反推，候選池）

- **產業判讀線**：recall vs context length 才是長上下文真戰場？headless software（API/agent-first）對軟體形態的重塑？中國開源排行榜作為地緣 AI 訊號？
- **coding-agents 線**：Antigravity 是 Gemini-native 第一方優化 vs 第三方適配的結構差距？context 壓縮本質是選擇性遺忘？trust accumulation 怎麼建？什麼任務該給哪種 agent？
- **MSFT super app 線**：seat 賣得多 vs DAU 真的低，第三方資料拿得到嗎？Anthropic 走「終端深度」的長期天花板在哪？個人「MSFT 慢」印象是上一輪世代殘留嗎？
- **元主題**：卡片到 130 張會不會反而難檢索？「待拆的卡」清單會不會變成不斷膨脹的債務？投資時效卡半年後大量過期怎麼辦？
- **Personal OS 線**（4 份 notes 反覆出現但沒拆卡）：從投資模盤到個人 OS 的真實切入點是什麼？跟 agent OS 的關係？

## 你已沉澱的判斷（指向卡片）

- Harness 影響大於換模型 → `topics/coding-agents/cards/harness-beats-model.md`（Salesforce 案例再驗證：+79% 來自 review agent + skills + 無限 token，不是換模型）
- 讀 agentic 戰報先分「估計值 vs 實測值」，只信實測（Salesforce 231→13 是估計，+79%/-5% 才是實測）
- 讀信號，不讀表面數字 → `topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`
- 其餘 17 張見 `README.md` 地圖

## 你的工作偏好（我據此調整，不必每次重講）

- 討厭過度工程與儀式；要低門檻、先進 main 讓手機讀得到
- 過程中要多反問拿 feedback，別悶頭做完才報告
- 手機閱讀為主，格式不要破版
- 答案要誠實：做不到就直說、不粉飾；犯錯就認

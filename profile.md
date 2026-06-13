---
type: interest-profile
maintained-by: claude
updated: 2026-06-13
note: 這是「AI 持續記住你」的記憶層。每次 session 我開頭先讀它、結尾更新它，你不必重複交代背景。
---

# 你的興趣檔案

> 我（Claude）每次 session 開頭先讀這份、結尾更新這份。
> 所以你隨處丟問題，我都能接著上次、知道你在乎什麼。

## 你持續關注的話題
（隨口疑問會讓對應話題往上浮；新主題自動長出來。2026-05-30 從 19 份 notes + 3 個卡片主題反推）

- **AI agents / coding agents** — 最深，13 張卡。harness>model、沙箱、記憶架構、人機協作、多 agent 編排；最新聽 Every「AI & I」podcast 最近三期（Figma Matt Colyer / Anthropic Claude Managed Agents / After Automation），共同訊號「瓶頸從生產移到審查、判斷力是人機護城河」高度咬合 harness>model（`notes/ai-and-i-podcast-recent.md`）；前次 Salesforce 全公司 agentic 化案例（`notes/salesforce-agentic-engineering.md`）
- **Agent OS / Personal OS** — 反覆出現：怎麼做、市場全景、從投資模盤切入個人 OS（4 份 notes）
- **非工程師怎麼變 AI Power User** — roadmap、user stories、工作/個人電腦 companion（4 份 notes，很實戰）
- **AI 產業判斷 / 投資訊號** — 讀信號不讀數字、開源商品化計時器、價值流向、中國開源、模型進步軌跡;最新:免費財經 API 的經濟學(Yahoo 沒在維護 API、是社群白嫖網站內部 endpoint;Google 反而刻意不做;萃出「免費 API 三種真相」框架——副產品白嫖型/freemium 漏斗型/整合進自家產品型;資料軌道誰掌控=隱藏風險,接 Robinhood 賣軌道母題,inbox 2026-06-07);前次:AI 資安生態位(CRWD→賣鏟人誰對位,排序 PANW>CRWD>ZS>S1,延伸「身份是收費站」「計價斷層」兩元判斷,`notes/ai-security-ecosystem.md`)、Robinhood agentic trading(`notes/robinhood-agentic-trading.md`)、Anthropic 5–6 月 blog、eval 生態位
- **MSFT × OpenAI super app** — 平台×模型乘積、Graph/Entra 護城河、Copilot 滲透真假
- **學習 / 教育加速** — Alpha School、learning roadmap、skills/eval 設計
- **知識系統怎麼設計才真的複利** — 元主題，就是這個 repo 本身（你正在用它）。最新(2026-06-13):查證 Karpathy LLM wiki(2026-04 爆紅 gist)——**這個 repo 就是它的實例**(AI 維護 markdown、raw→wiki entity pages→CLAUDE.md schema、預編譯複利),逐條撞同設計,等於給整套系統正名+名人錨點;同時釐清個人 vs 團隊路線——個人預設 wiki 不需 RAG,團隊共享瓶頸是「寫入協作+維護」不是「檢索」,RAG 解錯問題(`notes/rag-vs-llm-wiki.md`);前次:Noah Brier「Claude Code as second brain」同物種確認(`notes/claude-code-second-brain-noah-brier.md`)、遞迴改進 harness(Issue #6,`meta/defects.md`+`/meta-review`)

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

- **agent 時代資安計價會不會崩？**（2026-06-07 開）賣鏟人故事的「量」會爆,但 agent 把 seat 壓縮 90%、ephemeral、不佔 license,舊 per-seat/per-endpoint 計價可能撐不到 agent 時代。該追「資安公司怎麼對活 30 秒的 agent 收費」。領先指標:CRWD/PANW 有沒有推出 per-agent / 非人類身份計價;模型廠(OpenAI GPT-5.4-Cyber/Daybreak)cyber 產品是合作還是自營(會不會把這四家從收費站擠掉)。(`notes/ai-security-ecosystem.md`)

- **我們系統缺「內容層的週綜合」**（2026-06-06 從 Noah Brier 對照浮現）：現有睡前步驟是增量的（每次只看一條 inbox），缺一個「定期批次掃整週 inbox+notes、主動抽跨主題模式」的 pass。Noah 的 weekly-synthesis 做了這個。對照：我們有 harness 層 review（meta-review/Issue #6）但缺內容層 review。**理想兩個都要**——一個讓知識複利、一個讓系統複利。待辦:考慮做 weekly-synthesis skill（同時掃對話訊號+檔案 mtime）。(`notes/claude-code-second-brain-noah-brier.md`)

## 你可能感興趣的下一題（從 starts/journeys 反推，候選池）

- **動手複製 agent patterns**（2026-06-07 開，待實作）：想把 AI & I podcast 學到的模式自己手刻——outcomes 迴圈（`/loop`+自寫判準）、發散/收斂平行子 agent、個人迷你 eval。已提議用平行子 agent 示範，用戶「先這樣」暫緩；下次可挑一個真的做。
- **產業判讀線**：recall vs context length 才是長上下文真戰場？headless software（API/agent-first）對軟體形態的重塑？中國開源排行榜作為地緣 AI 訊號？
- **coding-agents 線**：Antigravity 是 Gemini-native 第一方優化 vs 第三方適配的結構差距？context 壓縮本質是選擇性遺忘？trust accumulation 怎麼建？什麼任務該給哪種 agent？
- **MSFT super app 線**：seat 賣得多 vs DAU 真的低，第三方資料拿得到嗎？Anthropic 走「終端深度」的長期天花板在哪？個人「MSFT 慢」印象是上一輪世代殘留嗎？
- **元主題**：卡片到 130 張會不會反而難檢索？「待拆的卡」清單會不會變成不斷膨脹的債務？投資時效卡半年後大量過期怎麼辦？
- **Personal OS 線**（4 份 notes 反覆出現但沒拆卡）：從投資模盤到個人 OS 的真實切入點是什麼？跟 agent OS 的關係？

## 你已沉澱的判斷（指向卡片）

- Harness 影響大於換模型 → `topics/coding-agents/cards/harness-beats-model.md`（Salesforce +79% 來自 review agent+skills 不是換模型;**Google DevRel 在 I/O 也淡化 model=利益相反方的第三方驗證**,`notes/gemini-api-platform-shift.md`）
- 讀 agentic 戰報先分「估計值 vs 實測值」，只信實測（Salesforce 231→13 是估計，+79%/-5% 才是實測）
- 讀信號，不讀表面數字 → `topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`
- Eval 是跨模型裁判層，結構上該住模型廠外 → `topics/ai-industry-reading/cards/eval-is-a-cross-model-judge-layer.md`（+ 收購買通路、生態位分岔 2 張同主題）
- Eval 瓶頸是寫判準不是工具，所以個人能搞 agent eval → `topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md`（+ 終態評分 1 張）
- 其餘卡見 `README.md` 地圖（卡片總數已達 ~22 張：ai-industry-reading 8、coding-agents 15）

## 你的工作偏好（我據此調整，不必每次重講）

- 討厭過度工程與儀式；要低門檻、先進 main 讓手機讀得到
- 過程中要多反問拿 feedback，別悶頭做完才報告
- 手機閱讀為主，格式不要破版
- 答案要誠實：做不到就直說、不粉飾；犯錯就認

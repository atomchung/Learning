---
type: interest-profile
maintained-by: claude
updated: 2026-06-20
last-session: 資訊爆炸時代的攝取流程設計 → 建 weekly-synthesis skill + 開放疑問改造成預測帳
note: 這是「AI 持續記住你」的記憶層。每次 session 我開頭先讀它、結尾更新它，你不必重複交代背景。
---

# 你的興趣檔案

> 我（Claude）每次 session 開頭先讀這份、結尾更新這份。
> 所以你隨處丟問題，我都能接著上次、知道你在乎什麼。

## 你持續關注的話題
（隨口疑問會讓對應話題往上浮；新主題自動長出來。2026-05-30 從 19 份 notes + 3 個卡片主題反推）

- **AI agents / coding agents** — 最深，13 張卡。harness>model、沙箱、記憶架構、人機協作、多 agent 編排；最新(2026-06-20):openclaw vs Hermes Agent——2026 爆紅的兩個開源「個人 agent 框架」(同物種競品,=personal OS 論題的實例化)。OpenClaw(前身 Moltbot,創辦人進 OpenAI 後交基金會,Node,ClawHub 技能註冊表,單 agent loop)往穩定化+provider 全外掛化(npm)走;Hermes(Nous Research,Python,週更,self-improving skills+多 agent swarm+本地 SQLite FTS 記憶)往自我改進+swarm+桌面 ubiquity 走。**訊號**:①差異化幾乎全在 harness 不在 model(兩者皆模型無關路由器)=harness>model 又一獨立驗證 ②記憶勝負手=OpenClaw 每次餵整份 JSONL 回 context(~19s)vs Hermes 本地 SQLite FTS(~113ms),接 LLM-wiki 預編譯 ③skill 兩路線=Hermes 學來/OpenClaw 策展 ④都往背景子 agent 收斂(接 agent-collab-infra)。caveat:周圍巨量 SEO 農場(半數 403)、版號偏亂;SEO 爆炸本身=紅到養出內容經濟(`notes/openclaw-hermes-personal-agent-frameworks.md`,freshness 2026-06);前次(2026-06-19):Strands Shell(AWS `strands-agents/shell`)——給 agent 的 in-process 沙箱,Rust VFS、無 fork/exec/syscall、cold start <1ms。判決「沙箱光譜的反設計,跟『Codex 用即時性換隔離性』對撞(主張兩個都要);要打折=in-process mediation 是軟體邊界比 VM 軟、跑到 native/FFI 就漏;又一 harness>model 案例。對我們:知識/訊號價值>工具採用價值,直接採用 ROI 薄,可能落點=捕捉點 bot」(`notes/strands-shell-agent-sandbox.md`);前次(2026-06-16):Ponytail——教 agent「少寫程式碼」的開源插件(純 prompt/ruleset,6 級決策階梯),判決「核心觀念真但 80-94%數字是作者自測估計值要打折;最大價值在 meta=又一個 harness>model 教科書案例,可直接抄階梯進自己 CLAUDE.md」(`notes/ponytail-lazy-agent.md`);前次聽 Every「AI & I」podcast 最近三期（Figma Matt Colyer / Anthropic Claude Managed Agents / After Automation），共同訊號「瓶頸從生產移到審查、判斷力是人機護城河」高度咬合 harness>model（`notes/ai-and-i-podcast-recent.md`）；前次 Salesforce 全公司 agentic 化案例（`notes/salesforce-agentic-engineering.md`）
- **Agent OS / Personal OS** — 反覆出現：怎麼做、市場全景、從投資模盤切入個人 OS（4 份 notes）;最新(2026-06-15):多 agent 協作 infra「agent 怎麼共享文件編輯」——核心判斷「agent 協作單位是 PR/diff 不是共享游標,比較像 git 不是 google doc;人類即時協作三約束(慢/要 presence/恨 conflict)agent 全不成立,可能跳過即時協作階段」;git vs CRDT 判準、語意衝突偵測器是前沿層(`notes/agent-collab-infra.md`)
- **非工程師怎麼變 AI Power User** — roadmap、user stories、工作/個人電腦 companion（4 份 notes，很實戰）;最新(2026-06-14):Claude Design——Anthropic 給非工程師的視覺原型 surface(Claude Code 外第二條 agent 產品線)。理解+討論怎麼用在自己產品;關鍵診斷「用不上的真因是工作流沒設計階段、不是工具」,以及 personal_os 看板的 iOS tokens 被 Streamlit 卡住、用 st.html 注入繞過(`notes/claude-design.md`)
- **AI 產業判斷 / 投資訊號** — 讀信號不讀數字、開源商品化計時器、價值流向、中國開源、模型進步軌跡;最新(2026-06-20):Andrew Ng〈Open Platforms Beat Power Plays〉(純策略/賽局向,零技術)——背景=Anthropic Fable 5 夾帶隱形「不准做競爭性 LLM」guardrail+美國商務部出口管制前沿模型。Ng 論證三拍「開放點燃 AI(Transformers 免費)→關門很諷刺/夾帶私貨是 power play→封鎖反加速對手建替代品(晶片/稀土前例)」。一句話「想用控制存取權鞏固領先,只會加速對手建你管不到的開放替代品」。是「讀信號不讀數字」+開源商品化計時器的活實例,可升級成卡片;打折=Ng 開放生態既得利益方、晶片類比 AI 未必成立(`notes/ng-open-platforms-beat-power-plays.md`);前次:免費財經 API 的經濟學(Yahoo 沒在維護 API、是社群白嫖網站內部 endpoint;Google 反而刻意不做;萃出「免費 API 三種真相」框架——副產品白嫖型/freemium 漏斗型/整合進自家產品型;資料軌道誰掌控=隱藏風險,接 Robinhood 賣軌道母題,inbox 2026-06-07);前次:AI 資安生態位(CRWD→賣鏟人誰對位,排序 PANW>CRWD>ZS>S1,延伸「身份是收費站」「計價斷層」兩元判斷,`notes/ai-security-ecosystem.md`)、Robinhood agentic trading(`notes/robinhood-agentic-trading.md`)、Anthropic 5–6 月 blog、eval 生態位
- **MSFT × OpenAI super app** — 平台×模型乘積、Graph/Entra 護城河、Copilot 滲透真假
- **學習 / 教育加速** — Alpha School、learning roadmap、skills/eval 設計
- **知識系統怎麼設計才真的複利** — 元主題，就是這個 repo 本身（你正在用它）。最新(2026-06-13):查證 Karpathy LLM wiki(2026-04 爆紅 gist)——**這個 repo 就是它的實例**(AI 維護 markdown、raw→wiki entity pages→CLAUDE.md schema、預編譯複利),逐條撞同設計,等於給整套系統正名+名人錨點;同時釐清個人 vs 團隊路線——個人預設 wiki 不需 RAG,團隊共享瓶頸是「寫入協作+維護」不是「檢索」,RAG 解錯問題(`notes/rag-vs-llm-wiki.md`);前次:Noah Brier「Claude Code as second brain」同物種確認(`notes/claude-code-second-brain-noah-brier.md`)、遞迴改進 harness(Issue #6,`meta/defects.md`+`/meta-review`)

## 你當前開放的疑問（＝預測帳）
（還沒沉澱成判斷的，追蹤中。每條帶 `check:YYYY-MM`＝該回來看現實怎麼判的到期日。`/weekly-synthesis` 掃到到期的就結算：✅ 對 / ❌ 錯 / ⚪ 無結論 ＋ 一句話，**錯的補「為什麼錯」**——這句是模型校準的燃料。結算後標記留痕，不刪。）

- 這套知識系統怎麼對我產生收益？
  → 2026-05-30 ✅ 收斂：改造成「repo 是我的腦」的記憶層，三拍循環已寫進 CLAUDE.md（見 inbox 2026-05-30 兩條）
  → 2026-05-30 ✅ SessionStart hook 已設（`.claude/settings.json`），boot 全自動

- **部門大腦怎麼從零搭起？**（2026-06-17 開，`check:2026-07`）：現況=沒有一個完整知識庫，要先「整理地圖→梳理 high-level learning→持續維護」三步。已設計流程（`notes/department-brain-process.md`）。關鍵判斷：①痛點是「沒人寫/沒人維護」=動機問題不是檢索,RAG 解錯問題 ②勝負手=寫入成本壓到近零+維護外包 AI ③解痛點機制=owner「只審不寫」④起點是**先畫跨主題地圖+每塊 high-level 綜述**(不是堆碎片頁),整套=這個 repo 的部門版。**待辦**：用戶可能要把這套真的套用(部門 or 自己 repo 的地圖重整)。兩個可深化分支:owner 只審不寫機制、捕捉點 bot 怎麼接。**2026-06-17 追加三段細節**(已寫進 note):①畫地圖方法=從 metadata 聚類不從內文(三 pass:骨架信號→抽樣標熟度→人校對) ②context 吃不下=永遠別整庫塞,wiki=硬碟/context=RAM 按需 page-in,三階段 ③Jira 關聯=當 raw 證據層補「為什麼」,共用領域標籤+key 互引+只吃 metadata,別灌全部 ticket。已 /record 進 session-records。

- eval 生態位:OpenAI 收 promptfoo 後,「維持中立 + 開源」能撐多久?模型廠長期有 lock-in 動機。追蹤中(`notes/eval-ecosystem-niche.md`)（`check:2026-09`）
- 升值的是安全/紅隊 eval(agent 會不會做壞事)——這塊值不值得當個人差異化技能深入?（`check:2026-08`）
  → 2026-06-05 部分回應:Anthropic Mythos(>90% 真陽性、不公開)顯示這塊在升值且被模型廠當戰略級自做。提示天花板——頂尖攻擊能力會鎖在模型廠內部,個人差異化大概落在「驗證/整合/合規」側而非「比模型更會找洞」。(`notes/anthropic-blog-2026-06.md`)

- MCP-as-a-rail：Hood 先發把 MCP 變散戶交易/支付軌道,但 MCP 是開放標準、軌道易被商品化。先發優勢能不能轉成「agent 預設走 Hood」的鎖定?半年內 IBKR/Schwab 跟進會怎樣?追蹤中(`notes/robinhood-agentic-trading.md`)（`check:2026-12`）
  → 2026-06-06 ✅「策略是啥」已收斂:Hood 不給策略,只給軌道。AI 操盤分兩型——機械型(你寫規則 AI 執行,價值=紀律/自動化)有用、判斷型(AI 自己選股)無證據(學術 robust backtest 跑輸大盤)。+結構性錯位:Hood 靠交易量賺,AI 傾向過度交易=最傷你報酬。賣軌道≠賣 alpha 成立。

- 遞迴改進 harness（Issue #6，`check:2026-07`）：基礎設施已接（defects + meta-review），社群 best practice 也整合進來了（`notes/recursive-harness-community-patterns.md`）。R1 防自評已落地（meta-review 動規則需至少一筆 `@user` 缺陷）。**R2/R3 待辦**：profile 加軟上限驅逐、CLAUDE.md 283 行要壓回 <200。下一步仍是累積缺陷後跑第一次 `/meta-review`。能刪規則的 RSI 才是對的 RSI。
  → 2026-06-20 新增 `meta/borrowable-patterns.md`（living ledger，跟 defects.md 當兄弟餵 meta-review）：從 openclaw/Hermes 萃出可借鑒點。**待用戶決策**:B1 蒸餾時機前移(event-triggered+當下主動提議卡片)、B2 連坑一起記、B3 重複出現當升級訊號——三條高 ROI、純 harness 行為微調(不加架構),要不要實際動進 CLAUDE.md。直接回應下面「內容層週綜合」+「auto-distill cards」兩個 open question。關鍵頓悟:Hermes 自動蒸餾=我們睡前做的事(markdown→索引→grep),差只在「時機與自動化」不是架構。

- **「語意 merge 閘門」是不是可投資生態位？**（2026-06-16 收斂，`check:2026-09`）→ 判決:獨立公司大概率是 feature 不是 company,跟 eval/資安**同一個天花板**(核心動作=一次 LLM call、能力住模型裡會被吞;merge 閘比 eval 護城河更淺,因缺中立性論點)。可投資表達式在外圍三項:①擁有 merge 地點的 incumbent(GitHub/MSFT,投平台不投 feature)②合規/稽核 pure-play(受監管多 agent,唯一能撐成公司的角度,同資安「edge 在合規」)③資料/信任護城河(累積 merge 決策→trust-routing,接 trust accumulation)。關鍵 reframe:純 merge 閘 TAM 薄(序列化繞過),真品類是上一階「agent 動作准入/治理層」(LangSmith/Braintrust/Arize+guardrail+身份),merge 是其 feature。指標:orchestrator 內建 reconcile=關門、合規 pure-play 拿監管客戶=開門。(`notes/agent-collab-infra.md`,freshness 2026-06)

- **agent 時代資安計價會不會崩？**（2026-06-07 開，`check:2026-10`）賣鏟人故事的「量」會爆,但 agent 把 seat 壓縮 90%、ephemeral、不佔 license,舊 per-seat/per-endpoint 計價可能撐不到 agent 時代。該追「資安公司怎麼對活 30 秒的 agent 收費」。領先指標:CRWD/PANW 有沒有推出 per-agent / 非人類身份計價;模型廠(OpenAI GPT-5.4-Cyber/Daybreak)cyber 產品是合作還是自營(會不會把這四家從收費站擠掉)。(`notes/ai-security-ecosystem.md`)

- **微軟地基何時消失？M365 在 AI 世代還剩什麼**（2026-06-15 開，`check:2026-12`）：Nadella 發文主打 learning loop（harness>model 的 CEO 級錨點，但他是利益相同方淡化自家弱項=要打折）。診斷出微軟 harness 手藝普通（自家工程師偏好 Claude Code 卻被令遷回 Copilot；M365 Copilot 同時有 ChatGPT/Gemini 時活躍掉到 8%、唯一選項才 68%=被綁非賺來），真正護城河是 Graph/Entra 地基+通路。**核心追蹤**：護城河三層（App 已死→Graph→Entra），崩塌觸發 = agent 的 learning loop 成主要 system of record 且住模型廠不住微軟（A 搬家/B MCP 商品化存取/C 身份脫鉤）。最大反諷：Nadella 的「擁有 learning loop」正是殺死 Graph 的刀。領先指標：正本在哪累積、agent 碰 SharePoint 是否通用連接器、agent 身份誰發、force-bundle 是否變兇+內部叛逃。**2026-06-15 排序收斂**：微軟哪層在 AI 世代關鍵=「agent 寫進去的正本」留、「agent 繞過的 UI」死。排序 **身份/安全 > GitHub 基板 > Office app**。① 安全 $20B/年翻倍 + 已出 Entra Agent ID(收費站從人擴到 agent,主動反打場景 C)=最 durable,接「身份是收費站」卡;② GitHub 基板(repo=agent 寫進去的 SoR)=王冠但 Copilot 產品弱、有自殺風險;③ Office=散佈載體非價值核心,最該被融化。(`notes/nadella-frontier-ecosystem.md`)

- **我們系統缺「內容層的週綜合」**（2026-06-06 從 Noah Brier 對照浮現）：現有睡前步驟是增量的（每次只看一條 inbox），缺一個「定期批次掃整週 inbox+notes、主動抽跨主題模式」的 pass。Noah 的 weekly-synthesis 做了這個。對照：我們有 harness 層 review（meta-review/Issue #6）但缺內容層 review。**理想兩個都要**——一個讓知識複利、一個讓系統複利。
  → 2026-06-20 ✅ 收斂：`weekly-synthesis` skill 已建（`.claude/skills/weekly-synthesis/`），meta-review 的內容層兄弟。每週掃 inbox+notes，抽跨主題模式、結算預測帳、提卡片升級。同時這次把「開放疑問」改造成**預測帳**（每條帶 `check:` 到期日），補上攝取流程第 5 關（證偽/校準）。(`notes/claude-code-second-brain-noah-brier.md`、`notes/info-intake-routine.md`)

- **Claude Design 對我的 ROI 待實測**（2026-06-14 開，`check:2026-07`）：診斷出我大半產品(CLI/後端/Markdown)是錯配,真正契合的是天天看的看板、對外卡片(trade_review)、小紅書視覺。已選 personal_os 看板試點,給了「人生目標卡」starting prompt(餵 core/styles.py tokens、要 3 個方向)。待用戶實際貼進 claude.ai/design 跑一輪 → handoff 回來我接 dashboard.py 的 st.html 注入,看切法順不順、值不值得擴到其他 tab。(`notes/claude-design.md`)

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

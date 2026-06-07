---
type: qa-log
note: append-only。隨口疑問 + 當時結論。成熟的判斷會沉澱成卡片並回填連結。
---

# 問答記錄（隨口疑問的落腳處）

> 你隨處丟問題，我接住後記在這。每條 = 一個疑問 + 當時結論 + 狀態。
> 同一話題反覆出現時，profile.md 會把它往上浮；夠成熟就升級成卡片。

## 2026-05-30 — 這套知識系統怎麼對我產生收益？

**疑問**：卡片系統跑了一陣子，感覺沒收益，是哪裡錯了？

**結論**：
- 收益在「取用 / 沉澱判斷」端，不在「累積卡片」端。過去力氣多花在容器上（圖、tunnel、Pages、可視化），沒花在用知識。
- 你真正要的不是手工知識庫，是：**隨口疑問 + AI 回答被整體記錄關聯起來，AI 持續知道你關注什麼，進而持續給你更想要的答案。**
- 硬約束：別處 app 的問題不會自動流進來，需要固定汇流口；「AI 持續記住你」靠每次開場讀 `profile.md`。
- 行動：新增記憶層 `profile.md`（我讀+更新）+ 本 `inbox.md`（隨手記）。卡片系統降為底層，不再是入口。

**狀態**：開放 → 系統入口改造中

**相關**：`profile.md`

## 2026-05-30 — repo 是我的腦，要能存記憶 + 被搜尋

**疑問**：只要我刻意在 Learning repo 問問題，你就能透過 repo 知道我整個記憶、也知道怎麼搜尋——本質上這個 repo 是你的腦，對吧？

**結論**：
- 對，這是最準的心智模型。但要先破一個誤會：**我跨 session 預設零記憶**，聊天本身不是記錄，**寫進 repo 檔案才是**。
- 所以「腦」要運轉需接兩根線：開場自動讀 `profile.md`（boot）、睡前把問答寫回 `inbox.md`+更新 `profile.md`（sleep）。
- 搜尋機制：`profile.md` 當索引 → `grep` 整個 repo → 命中 `inbox.md` / `cards/`。
- 行動：把記憶層的三拍循環寫進 `CLAUDE.md`（契約），讓未來每個 session 都自動 boot/sleep。

**狀態**：✅ 已接線（CLAUDE.md 新增「記憶層」章節）

**相關**：`CLAUDE.md` → 記憶層、`profile.md`

## 2026-05-30 — Salesforce 全公司 agentic 化案例（Claude Code）

**疑問**：研究 Boris Cherny 轉的 Salesforce 案例——231 天遷移 13 天做完、一個 PR 21 個 endpoint、100% 覆蓋。

**結論**：
- 招牌數字（231→13、18x）是**自估反事實基準**，無法獨立驗證，當公關看就好。
- 真正耐看的是兩個**實測**值：每位開發者 merge PR 數 +79%（年對年）、事故率 -5%。讀信號就讀這兩個。
- 真正的故事不是「模型變強」而是**工作流重建**：唯讀 code review agent 進迴圈（APPROVED / WARNINGS / CHANGES REQUIRED，丟回 dev agent 重審）、skills 成為可重用工程資產、全員無限 token。→ 呼應「Harness 影響大於換模型」。
- 工程長自己承認難題：長 session 的 context 管理仍是手藝、模型仍會漂。
- Will 保哥吐槽點出真瓶頸：常在組織摩擦（敢不敢拍板全切、給無限 token、拆舊流程），不在技術。

**狀態**：✅ 已寫筆記

**相關**：`notes/salesforce-agentic-engineering.md`、`topics/coding-agents/cards/harness-beats-model.md`、`ai-industry-reading` 的「讀信號不讀表面數字」

## 2026-05-30 — 總結我歷史問了哪些問題 + 可能感興趣的下一題

**疑問**：紀錄這次，然後總結歷史問過的、列出我可能感興趣的問題。

**結論（歷史四條主線）**：
1. **AI agents/coding agents 的結構**（最深）— harness > model、四層 harness、權衡（即時/吞吐、隔離/靈活、同步/非同步）、記憶六層、契約介面（CLAUDE.md）、可審查橋梁（Artifact）、擴展槓桿（MCP）
2. **AI 產業判讀與投資訊號** — 讀信號不讀數字、開源是商品化計時器、跑分飽和時 gap 才是訊號、價值流向關係型部門、中國開源被低估、Agent OS 真值在強迫結構化
3. **MSFT × OpenAI super app** — 平台×模型乘積、Graph/Entra/組織意志三件套、Codex 變後台、為什麼 Spud 才動、Google 為何有零件無 app
4. **元主題：知識系統怎麼設計才複利** — 兩層制（notes/cards）、降門檻先進 main、收斂工具、repo 是腦、boot/sleep 三拍

**已接好的「腦」機制**：SessionStart hook 自動 `cat profile.md`、CLAUDE.md 三拍循環、`inbox.md` append-only。

**狀態**：✅ 紀錄完成；下一題候選見下方「列出哪些我可能感興趣的問題」

**相關**：`profile.md` 七大關注話題、所有 `topics/*/_start.md` 的「下一步可能要拆的卡」

## 2026-06-04 — Eval 的生態位（OpenAI 收購 promptfoo）

**疑問**：ihower Threads 提到 OpenAI 三月收購 promptfoo、還把自家 Evals 後台收掉叫大家遷過去——研究這個 eval 的生態位。

**結論**：
- 核心信號**不是**「promptfoo 勝出」,是**模型廠親口承認 eval 該住在模型產品外面**。eval 天生是「跨模型的裁判層」,要中立才有用;模型廠自己做 eval 踩到自我偏好(self-preference bias)+ 冗餘兩個結構矛盾。
- 那為什麼還花錢買?被買的根本不是 eval 功能,是底下兩樣:(1)**agent 安全紅隊**(prompt injection/jailbreak/越權——OpenAI 官方說法是 agentic security testing,塞進 Frontier),(2)**企業分發通路**(13 萬 MAU、Fortune 500 25%,坐在「企業決定換哪家模型」的決策點旁)。
- 命門:必須維持開源 + model-agnostic,否則分發價值歸零。中立性能撐多久是觀察點。
- **生態位分岔**:正確性 eval 在商品化(DeepEval/RAGAS 免費打),安全/紅隊 eval 在升值(企業預算 + 合規)。錢往後者跑。
- 接既有判斷:harness>model(eval 屬 harness 層)、開源商品化計時器(對工具響了、對通路+安全還沒)、讀信號不讀數字。
- 對個人:工具選擇不變(promptfoo 還開源);別把模型廠 eval 後台當中立基準;差異化技能在安全紅隊那邊。

**狀態**:✅ 已寫筆記

**相關**:`notes/eval-ecosystem-niche.md`、既有 `topics/ai-project-research/llm_eval_research.md`、`topics/coding-agents/cards/harness-beats-model.md`、`topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`

## 2026-06-04 — 目前怎麼測 agent 能力 + 個人也能搞嗎(接 eval 生態位)

**疑問**:接著上一題,具體怎麼測 agent 能力?流程是啥?個人也能搞對吧?

**結論**:
- **測 agent ≠ 測單次 prompt**:agent 多步、用工具、有軌跡,不能只看最後答案。三層次看:end-state(結果)/ trajectory(軌跡)/ component(零件)。
- **以 end-state 為主評分**:殊途同歸,多條工具路徑可能都對,別逼走預設路徑;trajectory 拿來診斷失敗 + 抓矇對。
- **Pipeline**:準備 task(goal+初始狀態+終態判準)→ 跑 agent 開 tracing 記整條軌跡 → 三類評分(結果 code 斷言為主 / 軌跡 LLM judge 診斷 / 效率 token+步數)→ judge 餵 rubric+軌跡回 PASS/FAIL,agent eval 標配 3 judge 投票 → 看 diff 進 CI。
- **公開 agent benchmark = 別人備好的 case + 終態判準**(SWE-bench/TAU-bench/GAIA 全是 end-state 評分)。
- **個人也能搞,而且特別友善**:最難的是「收 case + 寫判準」=理解問題不是工程問題,不能外包、個人對自己場景理解最深。最小版:tasks.jsonl 20 個 + 50 行 script + 成功率/平均 tool call 數 + 看 diff。撞牆點:case 攢得慢、judge 要校準、多 judge 是 3 倍 token。案例破百/要共看 trace 才上平台。

**狀態**:✅ 已補進筆記(`notes/eval-ecosystem-niche.md` 附錄段「目前怎麼測 agent 能力」+「個人也能搞對」)

**相關**:`notes/eval-ecosystem-niche.md`、既有 `topics/ai-project-research/llm_eval_research.md`(單次 prompt SOP)

## 2026-06-05 — 研究 Anthropic 最新 blog（5–6 月）

**疑問**：研究下 anthropic 最新 blog。

**結論**（三條主線，框架是讀信號不讀標題）：
- **When AI Builds Itself（6/4）**：呼籲全行業放慢，證據是自家內部數字——工程師每季 code 產出 8x、>80% production code 由 Claude 寫。提案「可驗證的全球暫停機制」。Jack Clark 說 recursive self-improvement 兩年內可能出現。
- **Project Glasswing / Claude Mythos（6/2）**：自主找 zero-day + 寫 exploit 的模型，>83% 首次就重現漏洞，掃 1000+ 開源找 6,202 高/危漏洞、>90% 真陽性（六家獨立驗證）。擴 150 組織 / 15+ 國。**不公開**——護欄不夠強。直接打中我「安全紅隊 eval 值不值得深入」的 open question。
- **S-1 / IPO（6/1）**：年化營收 run-rate $47B（五倍跳），主力企業採用 + Claude Code。Series H $65B / 估值 $965B。跟 OpenAI 賽 2026 上市。
- **串起來**：同一個「80% code by Claude」數字，一邊當 IPO 成長故事賣、一邊當該放慢的警鐘。Glasswing「強到不敢公開」替暫停論背書。
- **接判斷**：安全紅隊 eval 在升值但會被模型廠鎖內部，個人差異化落在驗證/整合/合規側；8x/80% 當信號讀別當實測產能；$47B 主力 Claude Code = coding agent 最會變現。

**狀態**：✅ 已寫筆記

**相關**：`notes/anthropic-blog-2026-06.md`、`notes/eval-ecosystem-niche.md`、`topics/coding-agents/cards/harness-beats-model.md`、`topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`

## 2026-06-06 — 讓自己的系統也能遞迴自我改進(接 Anthropic RSI)

**疑問**:讀完 Anthropic「When AI Builds Itself」後問——我怎麼讓自己的知識系統也遞迴自我改進?具體怎麼做?然後要求開 issue 記錄、一起看能改啥。

**結論**:
- **核心翻譯**:模型(Claude)動不了,RSI 唯一能發生的層是 **harness**(CLAUDE.md/profile/三拍/hook/skill)。這是既有判斷 harness>model 的直接推論。
- **三階梯**:L0 線性(堆 notes)→ L1 迴圈(現在,boot/awake/sleep 記憶層,但規則沒變,還不是「自我」改進)→ L2 遞迴(系統依自己的失敗改寫規則本身)。
- **缺的零件 = loss 信號**:四類可測缺陷(boot-miss / retrieval-miss / rot / merge-gap),現在發生完就蒸發,系統學不到。
- **遞迴步驟**:個案失敗 → 改規則(不是改個案)。一個內容失敗升級成一條流程規則。
- **反膨脹是最大陷阱**:自我改進預設方向是加更多結構,但用戶討厭儀式 → 優化目標是「每單位知識摩擦更低」,能刪規則的 RSI 才對。硬約束:meta-review 加兩條刪一條。
- **天花板**:時鐘速度=使用頻率不是 compute;梯度靠手動標,Claude 會漏盲點 → defects 要接受用戶補。

**做了什麼**:
- 開 [Issue #6](https://github.com/atomchung/Learning/issues/6) 當總帳。
- 接基礎設施:建 `meta/defects.md`(梯度儲存)、寫 `.claude/skills/meta-review/SKILL.md`(轉化迴圈 + 加二刪一閘)、`CLAUDE.md` sleep 步驟接上記缺陷。

**狀態**:✅ 基礎設施已接,待累積缺陷後跑第一次 /meta-review

**相關**:`notes/anthropic-blog-2026-06.md`、`meta/defects.md`、`topics/coding-agents/cards/harness-beats-model.md`

## 2026-06-06 — 整合社群 best practice 進遞迴改進 harness(接 Issue #6)

**疑問**:社群上應該有很多 best practice,一起整合一下(我們也查過很多次)。

**結論**:
- **核心發現**:我們手刻的 boot/sleep + defects + meta-review,是社群三個有名 pattern 的再發明——分層記憶(Letta/MemGPT,RAM 索引=profile / disk=inbox+notes)、情節記憶(Zep,append-only 日期戳 inbox)、外部 artifact 接力(Anthropic 長任務 harness)。手刻沒做錯,理解更深。
- **社群點出三個風險**:
  - **R1 自評不可靠**:Anthropic 實測 agent 評自己會自信稱讚自己。→ meta-review 加證據門檻,動規則前至少一筆用戶標的缺陷。
  - **R2 profile 會膨脹**:Letta/Mem0 hot 層必須小。→ profile 設軟上限 + 驅逐(把加二刪一也套在 profile 自己身上)。
  - **R3 CLAUDE.md 已 283 行**:超 200 警戒(我們自己筆記寫的)。→ 流程細節移 skill。
- **prior art**:社群有 harness-evolver plugin = Issue #6 的自動化版(多 agent 在 worktree 自動演化 + eval),但前提是自動 eval,我們還沒。當對照組看。

**做了什麼**:
- 寫 `notes/recursive-harness-community-patterns.md`(完整整合)。
- **R1 已落地**:改 `.claude/skills/meta-review/SKILL.md` 加證據門檻;`meta/defects.md` 格式加 `@user|@claude` 來源標記。
- R2/R3 留筆記當待辦,未動(反膨脹,不一次堆完)。

**狀態**:✅ R1 落地,R2/R3 排程

**相關**:`notes/recursive-harness-community-patterns.md`、`notes/agent-context-best-practices.md`、`meta/defects.md`、Issue #6

---

## 2026-06-06 — Robinhood agentic trading 的優勢在哪

**疑問**：FB 看到 Hood 推「串連 AI agent 交易」，連 Claude Code 的 `claude mcp add` 指令都幫你寫好。看看優勢是啥。

**結論**：
- **優勢不在「AI 會選股」**（誰都能包一層 LLM），在於它**第一個把 MCP 從開發者工具變成散戶可用的交易/支付軌道**。賣的是軌道 + 信任框架，不是模型。
- **檯面賣點**：隔離帳戶（agent 只能動你存進去的錢）+ 每筆推播 + 下單預覽 + 一鍵斷線 + 不綁模型。
- **真策略**：(1) first mover on MCP-as-a-rail；(2) 產品速度當護城河（老券商資產大但出貨慢）；(3) 想當「agent 經濟的預設交易/支付軌道」卡位；(4) 安全框架本身就是產品——難的不是技術，是把信任/合規/UX 包成散戶敢按的東西。
- **質疑**：MCP 是開放標準，軌道會被商品化，先發領先≠技術壁壘；官方自己警告 AI 策略可能慘賠、你自己負責——賣軌道≠賣 alpha；隔離帳戶對 Hood 也是「把 AI 交易框成可控新產品線去衝 AUM/交易量」的商業設計。
- **連結**：harness>model（賣 harness 不賣 model）、讀信號不讀數字（信號=agent 從「會說」走到「會做動真錢」的拐點）、Personal/Agent OS（交易/支付是個人 OS 高價值動作，誰先當預設軌道誰卡位）。

**狀態**：✅ 筆記層完成 `notes/robinhood-agentic-trading.md`（freshness 2026-06，beta）。暫不升級卡片——除非「MCP-as-a-rail」這個判斷在別處重用。

**相關**：`notes/robinhood-agentic-trading.md`、`topics/coding-agents/cards/harness-beats-model.md`、`notes/agent-os-market-analysis.md`

---

## 2026-06-06 — 讓 AI 操盤，但策略是啥？（接 Hood agentic trading）

**疑問**：上一則講 Hood「讓 AI 操盤」，追問——那策略到底是啥？

**結論**：Hood 不提供策略，只給軌道+資料+安全框架，策略那格留給你接的 agent 填。策略分兩型，行銷故意混淆：
- **A 機械型**（你寫規則、AI 當手執行）：「跌 2% 買 $100」「rebalance 20/80」「均值回歸」。有真價值，但價值是紀律+自動化，不是 alpha。本質=白話寫規則的自動下單機器人。
- **B 判斷型**（AI 當腦決定買啥）：edge 無證據。2026 robust backtest（20 年/100+ 標的）LLM 無顯著 alpha（p>0.34）、修掉偏誤後輸大盤。開發者金句：「週頻 LLM 贏不了 S&P，贏得了避險基金早做了。」原因：LLM 非為預測市場訓練、讀人人可見的同批報告無資料優勢、有敘事偏誤=追高。
- **結構性錯位**：Hood 靠交易量/PFOF 賺錢，AI agent 傾向過度交易——對 Hood 最賺的剛好最傷你報酬。
- **一句話**：它賣軌道，alpha 要你自己帶，而 LLM 目前帶不出來。把它當自動化紀律工具(A)有用，當選股 alpha(B)是幻覺。

**狀態**：✅ 把上一則開放疑問「賣軌道≠賣 alpha」收斂成具體判斷。寫進 `notes/robinhood-agentic-trading.md` 新增「策略是啥」一節。

**相關**：`notes/robinhood-agentic-trading.md`、`topics/coding-agents/cards/harness-beats-model.md`

---

## 2026-06-06 — Noah Brier 怎麼把 Claude Code 當第二大腦

**疑問**：聽到 AI&I podcast「Claude Code Can Be Your Second Brain」，想理解 Noah Brier 怎麼做的。

**結論**：他的做法跟我們這個 repo 是**同一個物種**——Claude Code 架在 Obsidian vault 根目錄、扁平 markdown、CLAUDE.md 開機載入記憶、手機操作（地下室 server + VPN）、Git 版控、上下文活在檔案不在 AI memory。核心洞見三句：(1) 讀比寫重要——「太多人關注 AI 會寫，太少關注它會讀」；(2) 思考模式 vs 寫作模式，預設停在思考、研究夠才准產出；(3) 上下文活在檔案裡所以開機能撈全歷史。他開源了實作 `heyitsnoah/claudesidian`：用 PARA 分資料夾（Inbox/Projects/Areas/Resources/Archive）、一堆自動觸發 skill（thinking-partner / daily-review / weekly-synthesis / de-ai-ify…）。

**對照我們的 repo**：骨架一樣（驗證方向沒錯）。值得偷三樣——思考模式做成「硬 gate」（front matter 直接擋住產出）、daily/weekly review 做成自動 skill、PARA 的時間維度。我們押了他沒有的兩個賭注——原子卡的跨脈絡重用層（topics/）、缺陷+meta-review 的遞迴自我改進（Issue #6）。所以不是落後，是同路多走兩步。

**狀態**：✅ 筆記層完成 `notes/claude-code-second-brain-noah-brier.md`。用戶決定先不改自己的系統，只記筆記。

**相關**：`notes/claude-code-second-brain-noah-brier.md`、`CLAUDE.md`（本 repo 就是同類系統）、`meta/defects.md`（Issue #6 遞迴改進）

---

## 2026-06-06 — Noah 的 daily/weekly review 實際在幹嘛 + 對我們的 learning（接上一則）

**疑問**：他的 daily/weekly review 主要在幹嘛？對我們有啥 learning？

**結論**（從他開源 skill 定義拆出）：兩個都靠掃檔案 mtime 自動盤點再產結構化筆記回存。daily-review 掃「今天改過的筆記」→ 產成就/進度/洞見/卡點/明天三優先/open loops。weekly-synthesis 讀「整週新建+修改的筆記」→**主動找模式**（反覆主題、共同障礙、能量給/耗）→ 產八段綜合筆記。

**對我們三個 learning**：
1. 我們缺「週期性退一步、跨主題找模式」這一 pass——睡前步驟是增量的（每次只看一條 inbox），沒做過「掃整週 inbox+notes 抽大主題」。
2. 兩種 review loop 對照：他 = 內容層 review（盤點知識找模式）；我們 meta-review/Issue#6 = harness 層 review（盤點缺陷改規則）。我們有後者缺前者，理想兩個都要。
3. 觸發機制互補：他掃檔案 mtime（不漏）、我們讀對話訊號（抓真在乎啥）。理想 weekly 兩個都掃。

**takeaway**：「定期跨主題找模式」值得做成固定動作，這是我們系統最該補的下一塊。

**狀態**：✅ 補進 `notes/claude-code-second-brain-noah-brier.md`「深掘」一節 + profile 新增一條開放疑問（內容層週綜合缺口）。用戶仍維持系統先不動,只記下這個方向。

**相關**：`notes/claude-code-second-brain-noah-brier.md`、`meta/defects.md`（harness 層 review 對照）、`profile.md`

---

## 2026-06-07 — Tokenmaxxing：把 token 用量當生產力的陷阱

**疑問**：token maximizing 是什麼？

**結論**：
- **定義**：Tokenmaxxing = 把「燒掉多少 token」當成工程生產力的 proxy。token 用越多 = 假設產出越多。
- **起火點**：2026/4 Meta 內部 Claudeonomics leaderboard，按 token 用量排名員工，封號「Token Legend」，從工程圈梗迅速變管理層真議題。
- **半真的直覺**：捨得花 token（多迭代、長 agentic loop）確實有時換到更好結果——Salesforce +79% 那個故事就是這條槓桿。Tokenmaxxing 是把這條槓桿**誤當 KPI**。
- **為什麼打臉**：燒 token ≠ 做得更好。放任 agent 狂跑產出 "workslop"（大量低價值錯誤輸出）。Amazon 關掉內部 token leaderboard；Fortune 5/28 下標「Tokenmaxxing is over」；Salesforce：「燒一百萬 token，零正面產出。」
- **正確方向**：optimize 不是 maximize。真槓桿在模型選擇 + 餵對 context，不是 token 絕對量。
- **接既有判斷**：
  - 讀信號不讀表面數字：token 量是教科書級的 input metric，拿來當 outcome proxy = 典型失誤
  - harness > model：光加 token 而不配 review/skills，加不出價值
  - 估計值 vs 實測值：token 量能看起來很忙，但不是 +79% 那種實測

**狀態**：✅ 已寫筆記 `notes/tokenmaxxing.md`；「燒 token 不等於有產出」可跨脈絡重用（candidate 卡片）

**相關**：`topics/coding-agents/cards/harness-beats-model.md`、`topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`、`notes/salesforce-agentic-engineering.md`

---

## 2026-06-07 — CRWD 財報 → AI 資安生態位「賣鏟人」誰最對位

**疑問**：Review CrowdStrike 2026 Q1 財報貼文 + Kurtz「賣鏟人/Mythos」發言；對比 CRWD/PANW/ZS/S1 誰的生態位最適合這個故事;展開推論 + 非共識。

**結論**：
- **財報**：後驗超棒(net new ARR +32% 創高、Rule of 40=59、利潤率 18→24%)、前瞻打平(Q2 in-line 是跌因)。隱形訊號=當機事件信任已修復。雜訊=股票分割、總營收。
- **Kurtz 那段**：Mythos 時刻=宣告轉折;資安從成本項→AI 基礎設施(部署 AI 前必先解資安);賣鏟人=不賭哪個 AI 贏、只要 agent 爆量就收過路費。每家都會講,要回看實測。
- **核心推論**：比較不能比功能(會被抄),要比「卡在 agent 生命週期哪一層」=收費站的無法繞過程度。身份是唯一 100% agent 都會經過的點(每個 agent = 非人類身份 NHI)。
- **排序**：① Palo Alto 最對位(併 CyberArk 卡住身份收費站)② CrowdStrike 財報最漂亮+遙測最厚但護城河依賴 surface 留在端點 ③ Zscaler 卡點窄 ④ S1 沒被模型廠點名。
- **硬訊號**:OpenAI Trusted Access / Anthropic Glasswing 都選 PANW/CRWD、跳過 S1=市場幫你投票。
- **三個非共識**:(1) 收費站可能不歸這四家,模型廠(GPT-5.4-Cyber/Daybreak)往下吃 (2) **「每個 agent 都要保護」≠ 收得到錢**——agent 壓縮 seat 90%、ephemeral,舊 per-seat/per-endpoint 計價會崩,該追「怎麼對活 30 秒的 agent 收費」(3) 反向:AI 反而加深遙測護城河(資料抄不走)→ 呼應 harness/資料>模型。

**狀態**：✅ 已寫筆記;兩條元判斷待升級成卡片

**相關**：`notes/ai-security-ecosystem.md`、`topics/coding-agents/cards/harness-beats-model.md`(資料>模型)、`ai-industry-reading` 的「讀信號不讀表面數字」「估計值 vs 實測值」

---

## 2026-06-07 — 搜 AI & I（Dan Shipper）podcast 最近幾期 takeaway

**疑問**：在 Snipd 看到 Every 的「AI & I」podcast，幫我搜一下、總結最近幾期的 takeaway。

**結論**：最近三期一條主線——**agent 把能力變便宜，反而讓人類判斷/審查更值錢**。
- **Figma Matt Colyer（最新）**：SaaSpocalypse 是假議題（他做 agent 反而買更多 SaaS）；好設計是鑽石型發散→收斂、chat 太線性；on-canvas agent 要打破文字框；**review 是最大瓶頸**；Figma MCP 閉合 code↔design。
- **Anthropic Angela Jiang + Katelyn Lesse（約6/1）**：Claude Managed Agents = multi-agent 編排 + dreaming（compound engineering）+ outcomes（指定結果跑到達成）+ 全域 hosted memory；API 用量年增 17×。
- **After Automation / 翻倍 headcount（5月底）**：越自動化越需要人；Every 15→30 人；GPT-5.5 重寫 codebase 62 分 vs 資深 85–90，差在「會回頭質疑題目本身」；人是 AI 的兩片麵包；砍人頭的商業模式恐過度承諾。
- **跨期訊號**：瓶頸從生產→審查/判斷；agent 進生產靠記憶+編排+outcome loop；「AI 取代人」被前線反證。高度咬合既有 harness>model 卡。

**狀態**：✅ 已寫 `notes/ai-and-i-podcast-recent.md`。候選升級卡片：「review 是瓶頸 / 判斷力是護城河」（跨 coding-agents、AI power user、產業判斷三線可重用）。

**相關**：`notes/ai-and-i-podcast-recent.md`、`topics/coding-agents/cards/harness-beats-model.md`

## 2026-06-07 — 為什麼 Yahoo Finance 能「免費財經 API」？Google 有做嗎

**疑問**：為什麼 Yahoo finance 能維護這個免費財經 API？Google 有做嗎？

**結論**：
- **前提糾正**：Yahoo 沒在「維護免費 API」。官方 API 2017 就關了；yfinance 那種是社群逆向，打的是 `query1/query2.finance.yahoo.com`——**網站前端自己在用的內部 endpoint**。正解問題是「Yahoo 為什麼容忍別人白嫖它網站後端」。
- **為什麼能存在（經濟學）**：(1) 邊際成本≈0，endpoint 本來就得跑給網站用，沒有獨立「API 產品線」要養；(2) 商業模式是廣告/內容、資料是誘餌，即時/深度鎖在 Yahoo Finance Plus 付費牆；(3) 全面封鎖是貓抓老鼠不划算（會週期反制：crumb/cookie 驗證、限流，2023 改 crumb 弄壞 yfinance 過）。→ 不是慷慨，是白嫖成本夠低又不痛。
- **Google 反過來刻意不做**：Google Finance API 2012 就關（授權條款逼它限制終端用戶、生態長不起來，改塞進自家產品）。只剩 Sheets 的 `GOOGLEFINANCE()`，延遲 15–20 分、無程式化公開 API。**關鍵差異**：Yahoo 需要財經 portal 掛廣告→被迫跑公開 endpoint→才有得白嫖；Google 的財經查詢意圖在搜尋 knowledge panel 就被吃掉，沒有那個副產品就沒那個漏洞。
- **可遷移元判斷**：「免費 API」三種真相——(1) **副產品白嫖型**(Yahoo/yfinance，無 SLA、會無聲壞，只配玩具/研究) (2) **freemium 漏斗型**(Alpha Vantage/Polygon/Finnhub，API 即產品、相對穩、免費層故意做窄) (3) **整合進自家產品型**(Google，不給獨立 API、要你留在它介面被變現)。
- **接既有線**：對 agentic trading／投資訊號——**資料層可靠性是隱藏風險**，白嫖型資料源會在 Yahoo 改 crumb 的早上無聲壞掉。同 Robinhood「賣軌道」母題：**軌道（執行/資料）誰掌控、誰能隨時抽掉，比表面的「免費」更重要**。要進生產走第 2 類付費源或自備援。

**狀態**：✅ 已記。隨口疑問，留 inbox 不另開 note。「免費 API 三種真相」是乾淨可重用框架，日後若在別主題再用到可升級成卡片。

**相關**：`notes/robinhood-agentic-trading.md`（軌道母題）、`topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`

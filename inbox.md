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

## 2026-06-04 — 把 eval 筆記升級成卡片（5 張）

**疑問**：升級卡片。

**結論（拆卡決定,用 AskUserQuestion 確認方向）**：全拆 5 張;craft 類放 coding-agents。
- **信號類 3 張 → `topics/ai-industry-reading/cards/`**（從 5 張增為 8 張）：
  1. `eval-is-a-cross-model-judge-layer` — Eval 是跨模型裁判層,結構上不該屬於模型廠
  2. `acquiring-neutral-tools-buys-distribution` — 收購中立工具,買的是分發通路與安全,不是功能
  3. `eval-bifurcates-correctness-vs-security` — Eval 分岔:正確性測量商品化,安全紅隊升值
  - 三張都加 `freshness: 2026-06`（promptfoo 具體數字會過期,可遷移的是元判斷）。
- **craft 類 2 張 → `topics/coding-agents/cards/`**（從 13 張增為 15 張）：
  4. `agent-eval-scores-end-state-not-path` — Agent eval 以終態評分,不綁標準路徑
  5. `eval-bottleneck-is-criteria-not-tooling` — Eval 的瓶頸是寫判準不是工具,所以個人也能搞
- 連結接既有卡:harness-beats-model、read-signals、open-source-commoditization-clock、value-flows、artifact-verifiable-output。
- 兩個 `_start.md` 已更新;`notes/eval-ecosystem-niche.md` 頂部標註已升級,留作來源。

**狀態**：✅ 已完成,merge 進 main

**相關**：`notes/eval-ecosystem-niche.md`、`topics/ai-industry-reading/_start.md`、`topics/coding-agents/_start.md`

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

---

## 2026-06-07 — AI & I 那幾期裡，哪些是「我自己能複製」的？

**疑問**：podcast 總結看完——有什麼有趣、而且我個人就能自己複製的東西？

**結論**：挑出三個個人可手刻的 pattern（不是公司級基建）：
1. **Outcomes 迴圈**（最易）：寫一條「成功判準」(測試/eval/檢查)，叫 Claude Code loop 到通過。這環境的 `/loop` skill 就是這個。價值在判準寫得好不好，不在模型。
2. **發散/收斂用平行子 agent**：繞過 chat 線性限制——一次開 N 個子 agent 各生方案、再用一個 agent 過濾。手刻 Figma「鑽石型流程」。
3. **自做迷你 eval**（像 Dan 拿 GPT-5.5 打 62 分）：挑 3–5 真實任務、寫下「好答案長怎樣」、餵不同模型/prompt 打分。收穫是被逼著把「什麼叫好」講清楚。接 profile 既有「eval 生態位」開放疑問。
- **已在複製的**：Anthropic「全域記憶體只撈相關專業」= 你的 profile.md + grep 窮人版；卡片到 100+ 張時升級成 per-query 檢索（接「130 張難檢索」那題）。
- **不能複製**：hosted infra、17× 規模、Figma on-canvas 產品本身——但 pattern 都能。

**狀態**：✅ 提議用平行子 agent 示範一次，用戶說「先這樣」暫緩。下次可挑一個實作。

**相關**：`notes/ai-and-i-podcast-recent.md`、`/loop` skill、`notes/eval-ecosystem-niche.md`

---

## 2026-06-13 — Gemini API 家族文章 → 怎麼建 RAG（個人/團隊）vs Karpathy LLM wiki

**疑問**：(1) 理解 LY Corp 技術 blog 的 Gemini API family 文章、找 learning；(2) 怎麼建 RAG（個人/小團隊視角）；(3) 跟 Karpathy LLM wiki 的關係；(4) 小團隊要共享知識，RAG 需要嗎。

**結論**：
- **Gemini 文章 = harness>model 的「賣鏟人自己背書」**：Google DevRel（LINE 台灣 Evan Lin 在 I/O Extended Taipei）說「競爭力不在誰會 call model，而在誰會把 model/retrieval/agent/event flow 組成能工作的系統」。賣 model 的一方淡化 model = 利益相反方的第三方驗證，跨過「Anthropic 自我宣傳」門檻。平台把 harness 元件（File Search 受管 RAG、Agents API、Webhook）商品化 → 價值上移組裝層（同「商品化計時器」母題）。反面：這也是 lock-in 糖衣，受管=失控制權。
- **Karpathy LLM wiki = 這個 repo 本身**（2026-04 gist）：AI 維護的 markdown 知識庫，raw→wiki entity pages→CLAUDE.md schema，知識預編譯複利。逐條撞我們設計（連 CLAUDE.md 當 schema 都一樣）= 給整套系統正名+名人錨點。
- **RAG vs wiki 是對立哲學**：RAG stateless 即時檢索碎片（適合大語料/多人/細權限）；wiki stateful 預編譯複利（適合個人/小團隊/<100K tokens）。一句話：RAG 每次重新發現，wiki 讓發現累積。
- **個人**：預設 wiki 不需 RAG。**團隊共享**：瓶頸是「寫入協作+維護」不是「檢索」，RAG 解錯問題；MVP=共享 git repo+CLAUDE.md schema，真要搜原文才加受管 RAG；三難點=並發寫入/新鮮度/權限。
- **可遷移元判斷**：「共享的瓶頸是協作+維護不是檢索」「某層被商品化→價值上移上一層的判斷力」。

**狀態**：✅ 已寫 `notes/gemini-api-platform-shift.md`、`notes/rag-vs-llm-wiki.md`，均進 main；harness-beats-model 卡補一筆第三方驗證。note 按用戶要的「個人/團隊」軸組織。待追：團隊 wiki 並發協作怎麼實際落地（沒實證）。

**相關**：`notes/gemini-api-platform-shift.md`、`notes/rag-vs-llm-wiki.md`、`notes/claude-code-second-brain-noah-brier.md`、`topics/coding-agents/cards/harness-beats-model.md`

---

## 2026-06-14 — Claude Design 是什麼 + 怎麼應用到我的產品（選 personal_os 看板）

**疑問**：(1) 理解 Duolingo 團隊寫的 Claude Design workshop 講義；(2) 我們能怎麼應用？「現在產品都沒法利用 claude design 去優化我們的設計」。

**結論**：
- **Claude Design = Anthropic 在 Claude Code 之外的第二條 agent 產品線**：餵 design system → prompt → 可互動 HTML 原型，live 上直接改，單向 handoff 給 Claude Code。本質是把「做原型」從工程師下放給 designer/PM。咬合三條線：非工程師 power user、harness>model（同模型兩套 harness）、Anthropic 終端深度。
- **「用不上」的真因不是工具，是我工作流沒有「設計階段」**：我習慣想到就 Claude Code 直接寫。Claude Design 插的位置是「寫 code 之前」，那個階段在我流程裡不存在。重新框定後，真正用得上的是「有視覺+視覺有回報」的東西：天天自己看的（看板/dashboard）、對外分發的（trade_review 卡、作品集）、內容平台產物（小紅書）。CLI/後端/Markdown 產品是錯配，別硬塞。
- **personal_os 看板實勘（關鍵診斷）**：dashboard.py 是 Streamlit（3047 行、6 tab）。根因不是沒 design system——**已有一套完整 iOS/HIG 風格 tokens（core/styles.py），被 Streamlit 原生元件卡住、發揮不出來**（好顏料被迫用蠟筆畫）。正確切法：Claude Design 吃那套 tokens 做純 HTML component → 沿用既有 `_render_narrative_html` 的 `st.markdown(unsafe_allow_html)` 注入路徑嵌回，邏輯不動、只換視覺層。比「脫離 Streamlit 重做」省力得多 = Streamlit 產品用 Claude Design 的通用解。
- **可遷移元判斷**：「工具用不上時先問流程缺口而非工具本身」「Streamlit 視覺天花板 = 元件層卡住 tokens，用 HTML 注入繞過」。

**狀態**：✅ 已寫 `notes/claude-design.md` 並進 main。給了可直接貼進 claude.ai/design 的「人生目標卡」starting prompt（附 core/styles.py 當 design system）。待續：用戶去試 → handoff 回來我接 dashboard.py 的 HTML 注入。

**相關**：`notes/claude-design.md`、`topics/coding-agents/cards/harness-beats-model.md`、`personal_os/dashboard.py`、`personal_os/core/styles.py`

---

## 2026-06-15 — Agent 協作怎麼共享文件編輯？office doc → google doc 的 agent 對應轉型

**疑問**：agent 協作下怎麼一起共享文件編輯？從 office doc 到 google doc 的對應轉型會是啥？AI agent 間的協作 infra。

**結論**：
- **核心反直覺判斷**：人類的「檔案→即時共享活狀態（OT/CRDT）」軌跡，agent 不一定重演。即時協作是為人類三個約束生的（人慢、要看游標 presence、恨 merge conflict），agent 全不成立。agent 協作的原子單位是 **PR/diff，不是共享游標**——比較像 git，不是 google doc。所以 office→google 的 agent 對應 ≠ 更好的 doc 編輯器，而是「prose/data 版的 git」：可分叉版本化狀態 + 語意合併 + provenance + review gate。
- **git vs CRDT 判準**：重疊 + 風險 + 要審 → git；不相交 + 低風險 + 要即時 → CRDT；能不並發 → 先序列化（orchestrator 單一寫手，最常被忽略的最省解）。CRDT 致命細節：保證收斂、不保證對；agent 改語意時「收斂但錯誤」是最危險失效。git 停下喊 conflict 對 agent 反而是特性。
- **真實是分層 hybrid**：live CRDT 當草稿層 + git-式 commit/review 當升正閘門。對到本 repo 的 notes→main、coding agent 的 working tree→PR。
- **兩模型都缺的前沿層**：agent 衝突是「意圖衝突」（兩 diff 各自乾淨、合起來語意矛盾），git 抓文字、CRDT 保字元，都抓不到。真正新 infra = **語意衝突偵測器 + LLM-as-merger**。誰做好握住關鍵閘門。
- **轉型四維度**（若真要 live 多 agent 共編）：字元級→語意級合併、presence→provenance（出處取代在場）、suggesting mode 變預設、WYSIWYG→結構化語意格式。
- **拉高一階**：agent 的「google doc 時刻」也許是共享 task/spec/state store，prose 文件只是投影；這個 repo 就是單人版實例。

**狀態**：✅ 已寫 `notes/agent-collab-infra.md` 並進 main。用戶選的深挖方向「git 模型 vs CRDT 模型」已含在 note。

**相關**：`notes/agent-collab-infra.md`、`notes/rag-vs-llm-wiki.md`、inbox MCP-as-a-rail（2026-06-06）、`notes/personal-os-research.md`

---

## 2026-06-16 — 「語意 merge 閘門」會不會變成可投資生態位

**疑問**：接前一篇 agent 協作 infra——「語意 merge 閘門」（判斷兩份乾淨 diff 是否語意打架的那層）會不會變成可投資的生態位？

**結論**：
- **判決：獨立公司大概率是 feature 不是 company**,被「擁有 merge 發生地點的平台」吸收(程式碼→GitHub/MSFT;agent→orchestrator/模型廠)。但是真實價值層。
- **跟 eval / 資安同一個天花板**:核心動作=「LLM 判斷兩 diff 是否語意打架」=一次 LLM call、能力住模型裡→聰明部分被 commoditize、外殼被平台收編。比 eval 護城河更淺(eval 有「裁判≠選手」中立性,merge 閘偏營運水管、跨廠中立訴求弱)。
- **可投資三表達式**:①擁有 merge 地點的 incumbent(GitHub/MSFT,投平台不投 feature)②合規/稽核 pure-play(受監管產業多 agent 寫共享狀態需可稽核軌跡,唯一能撐成公司的角度,同資安「edge 在合規」pattern)③資料/信任護城河(累積 merge 決策+結果→練更好的閘 + trust-routing,接 trust accumulation)。
- **關鍵 reframe(往上一階)**:純 merge 閘 TAM 薄,因為「並發寫最省解是不要並發寫(序列化)」繞過大半需求。真正可融資品類是上一階「agent 動作准入/治理層」(輸出該不該落地——品質/安全/政策/合規),merge 衝突只是觸發情形之一。名字:LangSmith/Braintrust/Arize + guardrail + 身份資安。
- **程式碼 vs 散文**:程式碼的 merge 閘已被 AI code review 新創(Graphite/CodeRabbit/Greptile)+ GitHub 填;散文/資料空白但 TAM 小。
- **領先指標**:orchestrator(LangGraph/Claude managed agents/OpenAI Agents SDK)做成內建 reconcile 節點=關門;合規 pure-play 拿到監管客戶=開門;出現 per-merge/per-action 計價且綁 policy+audit=有人找到 LLM call 外定價權。
- **可遷移元判斷**:「核心動作是一次 LLM call 的層,獨立性取決於有沒有中立性論點 + 資料/合規護城河,否則被平台吞」——這條同時解釋 eval、資安、merge 閘三個生態位。

**狀態**：✅ 已寫進 `notes/agent-collab-infra.md` 新增段(加 freshness: 2026-06)並進 main。profile 開放疑問收斂為判斷、連到 eval/資安/trust accumulation 三線。

**相關**：`notes/agent-collab-infra.md`、`notes/eval-ecosystem-niche.md`、`notes/ai-security-ecosystem.md`、`topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md`

---

## 2026-06-16 — Ponytail：教 agent 少寫程式碼的插件有沒有用

**疑問**：（貼 ExplainThis 介紹 GitHub 熱門開源 Ponytail 的圖）研究下有沒有用。

**結論**：
- **它是什麼**：不是程式，是一包 prompt/ruleset（`DietrichGebert/ponytail`，MIT，~10k stars）。核心是一條 6 級決策階梯，agent 寫 code 前逐級問「能不寫就不寫」（需要存在嗎→stdlib→原生功能→已裝依賴→一行→最小量），守則「lazy 但不 negligent」（安全/驗證/資料遺失不准砍）。支援 13+ 平台靠不同規則檔。
- **宣稱數字**：碼少 80–94%、快 3–6×、成本降 47–77%。但這是**作者自挑 5 任務、自跑 promptfoo 的估計值**，套「估計值 vs 實測值」判準只信實測→當行銷上限看。HN 有人酸「本質就是 README 一個 code block」。
- **核心觀念真的**：AI 過度生成/過度抽象/重造輪子是公認失敗模式，一條「先找理由不要寫」確實省 token。方向沒錯。
- **最大價值在 meta 層**：又一個 **harness>model 教科書案例**——markdown 規則改行為的幅度大過換模型。證明「行為住 harness 不住模型」。同 Salesforce(+79% 來自 skills)、Google DevRel 淡化 model 同組。
- **對我實際用法**：①直接抄那條決策階梯進自己的 CLAUDE.md/skill（價值在 idea 不在 package）②當 harness>model 證據 ③風險提醒：「少寫 code」是優化 proxy 指標（行數/token），會被 game→該抽象的不抽象換維護債,要盯 under-build。
- **一句話收**：有用,但用法是「抄階梯+當證據」,不是「信它省 77%」。最誠實貢獻=再證改 prompt 比換模型槓桿大。

**狀態**：✅ 寫進 `notes/ponytail-lazy-agent.md` 並進 main。

**相關**：`topics/coding-agents/cards/harness-beats-model.md`、`notes/quantify-your-harness.md`、`notes/salesforce-agentic-engineering.md`

---

## 2026-06-17 — 部門大腦：一堆 wiki 怎麼有效搭建知識庫

**疑問**：如何整理部門大腦？延續之前 RAG vs LLM wiki 的討論，設計一套流程——一堆既有 wiki 怎麼有效搭成知識庫。

**三題確認**：①讀者=人＋agent 都要 →走 LLM-wiki 預編譯（人讀乾淨頁、agent 吃 context）②既有 wiki=Confluence/Notion 為主、量大很多過期 →不搬不刪降為唯讀來源層、AI 按需編譯 ③最痛點=**沒人寫/沒人維護**。

**核心判斷**：
- 痛點是「沒人寫/沒人維護」=**動機與所有權問題,不是檢索問題**。直接印證母規則(團隊瓶頸是寫入協作＋維護,RAG 解錯問題)。
- **勝負手**：把寫入的邊際成本壓到接近零 + 把維護外包給 AI。整套流程繞這兩件事轉。
- 三個陷阱別碰:先上 RAG / 開會請大家更新 wiki(靠紀律必爛尾) / 做更漂亮的搜尋(漂亮空庫還是空庫)。
- **解痛點的關鍵機制**:owner「**只審不寫**」——職責是 approve AI 的編譯,不是自己寫。維護負擔掉一個量級才有人願意當 owner。
- 流程五段:Phase0 立地基(git repo+schema,PR=寫入單位,舊 wiki 降唯讀來源)→P1 冷啟動(AI 編譯不是人工搬家,人只驗收核心20頁)→P2 寫入(捕捉點設在工作發生處,低門檻 inbox+週綜合)→P3 維護(freshness/lint/矛盾偵測/meta-review 全自動)→P4 才上 RAG(受管的,接來源層之上)。
- 整套=**這個 Learning repo 的部門版**(notes/cards/CLAUDE.md/inbox/meta-review 一一對應),個人尺度已驗證會複利。
- 落地:別一次上整部門,挑一小組+一高頻痛點跑4週 pilot。驗收指標不是庫多大,是「寫入零負擔+過期有 AI 管」這兩個成立沒。

**狀態**：✅ 寫進 `notes/department-brain-process.md` 並進 main。留了兩個可深化分支(owner 只審不寫機制、捕捉點 bot 怎麼接)等用戶選。

**相關**：`notes/rag-vs-llm-wiki.md`、`notes/claude-code-second-brain-noah-brier.md`、`notes/agent-collab-infra.md`

---

## 2026-06-19 — Strands Shell：給 agent 的 in-process 沙箱 + 對我們有啥應用

**來源**：Pahud Hsieh 串文（2026-06-16）轉介 Clare Liguori 發布的 `strands-agents/shell`（AWS 陣營，Strands 是 AWS 開源 agent 框架）。

**它是什麼**：專給 agent 的 shell，Rust 核心 + Python/Node binding。標語「給 agent shell，不交出機器鑰匙」。Agent tool call 全跑在 Rust VFS 裡、in-process、無 fork/exec/syscall，cold start <1ms。

**核心判斷**：
- 沙箱光譜上的**反設計**：傳統走 OS 級隔離（container/firecracker/bubblewrap）隔離強但冷啟動貴；Strands 用 userspace Rust mediation 把 cold start 壓到 <1ms。
- **跟「Codex 用即時性換隔離性」對撞**：Codex 認 trade-off；Strands 主張「兩個都要」。這個論點是看點，收進沙箱光譜當對照端。
- **要打的折**：①<1ms 是 in-process 的必然非奇蹟、偏 best-case ②in-process mediation 本質比 VM 軟（軟體邊界，攔截層有 bug 或跑到 native/FFI 就漏；「完整 mediation」假設而非物理隔離）③是補位不是取代 micro-VM。
- 又一個 **harness>model** 案例：沒換模型，靠重設計「跑命令那層」挪動權衡。

**對我們有啥應用（誠實版）**：直接採用 ROI 現在偏薄——我們的東西多是 dashboard/markdown 不是 agent runner，沒現成痛點。三個可能落點：①**概念當鏡子（最實在）**=可重用的「in-process vs OS 隔離」透鏡 + harness>model 證據，價值在知識/訊號不在裝它 ②若做「捕捉點 bot」（部門大腦開放疑問）會用到 ③個人工具想讓 LLM 安全跑受限 shell 時 Python binding 可 drop-in。一句話：**知識/訊號價值 > 工具採用價值**。

**狀態**：✅ 寫進 `notes/strands-shell-agent-sandbox.md` 並進 main。

**相關**：`topics/coding-agents/cards/harness-beats-model.md`、`notes/department-brain-process.md`、「Codex 用即時性換隔離性」卡

---

## 2026-06-20 — Andrew Ng〈Open Platforms Beat Power Plays〉原文理解

**來源**：用戶貼 FB 截圖（標「Agentic 翻自 Andrew Ng《Open Platforms Beat Power Plays》」），要找原文理解。

**先釐清**：不是寓言改寫,是**真事**。FB 那篇是用 AI agent 把 Ng 英文原文翻成中文,內容忠實。背景兩件事：①Anthropic 出 Claude Fable 5,Mythos 模型加 guardrails,夾帶「不准做競爭性 LLM」且一開始隱形,反彈後道歉 ②美國商務部出口管制限制前沿模型輸出。

**原文性質**：純策略/賽局向,零技術討論（用戶自己點出這點）。

**論證三拍**：①點矛盾——AI 革命由開放點燃（Transformers 免費公開）,領頭羊現在關門很諷刺 ②拆話術——防駭客/生物武器合理,但「不准做競爭品」是夾帶私貨,等於 Google 禁你用它搜尋做競爭搜尋引擎=power play ③核心預測（標題）——封鎖反加速對手建替代品（晶片管制→中國自製、稀土威脅→美國找替代）,開放平台終勝權力操弄。

**一句話**：想用控制存取權鞏固領先,只會加速對手建一個你管不到的開放替代品。

**咬合**：讀信號不讀數字（Ng 讀「領頭羊關門」不讀跑分）、開源商品化計時器（封鎖=按下加速鍵）、存取軌道=隱藏風險。

**打折**：Ng 是開放生態既得利益方=利益相關要打折；晶片/稀土類比 AI 模型未必成立（複製成本/門檻不同,替代品追頂尖閉源仍有差距）。

**狀態**：✅ 寫進 `notes/ng-open-platforms-beat-power-plays.md` 並進 main。重用價值高,之後可升級成卡片連到 read-signals-not-surface-numbers。

---

## 2026-06-20 — openclaw / Hermes Agent 過去幾個月各自迭代了啥、方向是啥

**來源**：用戶問，要深度理解。兩者都在我 1 月知識截止後出現，現查（GitHub releases + README 為主，避開 SEO 農場）。

**定位**：兩者 = 2026 爆紅的開源「個人 AI agent 框架」，同一物種競品。local-first gateway + 透過既有通訊軟體接觸你 + 驅動 coding-agent 後端。= 用戶 personal OS / agent OS 論題的具體實例化。
- OpenClaw：前身 Moltbot，MIT/Node，創辦人 Cole Steinberger 進 OpenAI 後交非營利基金會。日曆版號，ClawHub 技能註冊表，單 agent loop+規劃。
- Hermes：Nous Research，MIT/Python，2/25 上線 4 個月 18 萬 stars、~週更。self-improving skills + 多 agent Kanban swarm + 本地 SQLite FTS 記憶。

**OpenClaw 方向**：穩定化+模組化（Task Flow 背景編排→migrate→型別化外掛 API/Android 語音→Skill Workshop+runtime externalize 成 plugin+SQLite→近期富文本通道/GLM-5.2+Haiku 4.5 路由/provider 拆 npm）。

**Hermes 方向**：自我改進+swarm+ubiquity（v0.7 可插拔記憶/反偵測瀏覽器→v0.9 桌面 dashboard→Tenacity 耐久 Kanban→v0.15 Velocity 大重構+swarm 自動分解+session_search 無 LLM 快 4500×+Promptware 防禦→v0.16 原生桌面 app→v0.17 背景子 agent/iMessage via Photon/Automation Blueprints）。

**訊號（差異全落在已有卡軸上）**：
①差異化幾乎全在 harness 不在 model——兩者皆模型無關路由器，模型=可換後端，產品本體=harness。harness>model 又一活例（兩團隊獨立驗證）。
②記憶架構是勝負手——OpenClaw 每次 recall 餵整份 JSONL 回 context（~19s）vs Hermes 本地 SQLite FTS（~113ms）。咬合本 repo LLM-wiki 預編譯（recall 住本地 index，別重塞 context）。
③兩條 skill 累積路線——Hermes 學來的（自動蒸餾）vs OpenClaw 策展的（ClawHub）。
④都往 multi-agent swarm/背景子 agent 收斂（接 agent-collab-infra）。

**Caveat**：周圍巨量 AI 生成 SEO 農場（半數 403/空洞），版號偏亂（Hermes 雙命名 v0.x + v2026.x）。SEO 爆炸本身=紅到養出內容經濟的訊號。治理訊號：founder 被 lab 吃掉、專案以基金會續命。

**狀態**：✅ 寫進 `notes/openclaw-hermes-personal-agent-frameworks.md`（freshness 2026-06）並進 main。時效快照，暫不拆卡；可遷移元判斷=「個人 agent 框架競爭是 harness 之爭」「記憶 recall 住本地 index 別重餵 context」。

---

## 2026-06-20 — Hermes「自動蒸餾重複工作流」怎麼來的 + 我們能借鑒什麼

**Q**：沈澱 openclaw/Hermes；基於優點持續列我們能借鑒的點；「自動蒸餾重複工作流」機制怎麼來的？

**機制（查 NousResearch 官方 docs，破除行銷話術）**：不是 ML 自我訓練,是**任務收尾的反思 pass + 寫 markdown 檔**——①觸發=完成複雜多步任務 or 從錯誤復原(SEO 文宣稱 5+ tool calls 硬門檻,官方無數字=LLM 啟發式判斷,信官方)②捕捉=程序+工具+決策點+**沿途踩的坑**+驗證步驟 ③寫成 SKILL.md(md+YAML frontmatter,agentskills.io 標準)到本地 `~/.hermes/skills/[類別]/[名]/` ④審批閘=預設「問你要不要存」,可設 write-freely / approve-each ⑤索引 `skills_list()` / 按需 `skill_view(name)` ⑥自我演化=會自己編輯淘汰過期 skill。
**punchline**：= 我們 repo 睡前做的事(判斷→markdown 卡→索引→grep 回憶)。差只兩點:(a)它任務完成當下觸發、(b)主動提議。**機制同種,差在時機與自動化,不是架構**。

**借鑒點(做成 living ledger `meta/borrowable-patterns.md`,跟 defects.md 當兄弟餵 meta-review)**：
- HIGH B1 蒸餾時機前移(event-triggered 不只 sleep)——回應 weekly-synthesis/auto-distill open question
- HIGH B2 連坑一起記不只記結論——把 defects 動作延伸到內容層
- HIGH B3「重複出現」當升級訊號給具體門檻(≥N 條 inbox 出現→flag 升級,grep 即可)
- MEDIUM B4 分層審批閘(已對,別動)、B5 索引+按需載入(已對)、B6 本地 FTS 別重餵 context(OpenClaw 反面教材)
- LOW B7 npm plugin/可攜標準(個人 repo ROI 薄)

**元判斷**：我們本來就是這物種,delta 是時機與自動化不是架構。最高 ROI=蒸餾從「只睡前」→「事件觸發+當下主動提議」+連坑一起記,純 harness 行為微調,喂 Issue #6。

**狀態**：✅ `meta/borrowable-patterns.md` 建立並進 main。待用戶確認放 meta/ 合不合適、B1–B3 要不要實際動進 CLAUDE.md(高影響需 @user 點頭,比照 R1)。

**追記（同日）**：用戶選「B1+B2+B3 一起進 CLAUDE.md」。已落地三處——「清醒」拍加 B1(當下蒸餾、主動提議沉卡)、「睡前」拍加 B2(連坑一起記:原本以為 X/錯在哪/怎麼驗,內容層坑進卡、harness 坑進 defects)、升級訊號加 B3(≥3 條 inbox 出現→grep 數次數→flag 升級)。ledger B1–B3 標 ✅ 已落地。這是第一次把「借鑒外部 agent 框架優點」真的動進契約,且三條都純行為微調不加架構。後續:跑首次 /meta-review 驗證是否真改善。

**追記 2（同日）— 還有其他值得學 + /record**：
- /record：把這次對話存成任務 → push `atomchung/session-records/records/openclaw-hermes-borrowed-patterns.md`(status done)。供本地 reconcile 回流 personal_os。push 一度被安全分類器擋(目的地是 skill 預設非用戶指名)，用戶確認後放行。
- 還有其他值得學：①Hermes 三層記憶分離(durable facts/skills/session-search)＝我們 profile/cards/inbox 的鏡像,點出 gap=profile 把穩定偏好跟演化判斷混在一起,該學「permanent memory 保持小」(接 R2/R3)。②背後譜系=Voyager/COMPASS(skill library,auto-distill 學術父親)、Generative Agents(reflection 先問問題再綜合+recency×importance×relevance 評分,最值得抄)、Letta/MemGPT(self-editing tiered memory)。③誠實過濾:這些多綁 vector DB/RAG,我們刻意不要,能抄的是控制邏輯不是儲存技術。④B10 外部內容衛生(promptware defense 輕量版,貼外部內容當資料不當指令)。
- ledger append B8(三層記憶分離)、B9(reflection 先問問題+importance)、B10(外部內容衛生),皆提案中;加「譜系」「過濾」兩節。待用戶決定 B8/B9 要不要動 CLAUDE.md。

**追記 3（同日）— meta-review 解釋 + B8 落地**：
- 解釋 /meta-review：遞迴改進 harness 的 L2 動作(改進者改進改進者)。讀 defects.md+近月 inbox→找重複缺陷→R1 至少一筆 @user 才動規則→反膨脹閘(每加 2 條刪 1 條)→AskUserQuestion 確認再改。不是每 session 跑,攢一批才跑。現 defects 只 1 筆,梯度不夠未跑首次。
- B8 落地(用戶「都按你建議搞」):①profile.md 按三層瘦身——從 77 行長鏈版(每話題拖最新…前次…前次)改成索引版(每條=核心判斷+一個最新指標+note 連結),舊脈絡下沉 inbox/notes 靠 grep,內容沒丟只是停止複製 ②CLAUDE.md 睡前拍加紀律「profile 保持小,別長出長鏈」。直接接 R2(profile 軟上限)。ledger B8 標 ✅。

**追記 4（同日）— 下次明確起點定案**：用戶「記錄起來」。共識＝**先別繼續加借鑒點**（這輪已加 B1/B2/B3/B8 多條進 CLAUDE.md，逼近 R3 的 <200 目標）。下次起點：①讓系統跑一陣 ②使用時把「漏接/給錯」隨手標進 `meta/defects.md` 行尾 `@user` ③攢幾筆真梯度後跑首次 `/meta-review`，那時一次反向砍規則 + 驗證 B1–B10 到底有沒有用。能刪規則的 RSI 才是對的 RSI——加完該收。已寫進 profile harness 線「下次明確起點」。

---

## 2026-06-20 — Cursor × SpaceX × xAI / Composer 3（四輪問答）

來源：FB 貼文（Fox Hsiao）。用戶四輪追問：理解 Composer 3 能力 → 出來了嗎評分如何 → 和 Grok 有關係嗎之後會整合嗎 → 但模型和 xAI 沒關係嗎怎麼評估 Cursor 模型研究能力。整理進 `notes/cursor-spacex-xai-composer3.md`。

要點（細節見 note）：
- 事件全查證為真：SpaceX 6/12 史上最大 IPO → 6/16 全股票 $600 億收購 Cursor + Compile 發 Composer 3/Mobile/Origin。坑：我一度以為貼文是 AI 編的假新聞（太離譜），差點犯「聽起來離譜就判假」——記 defects。
- Composer 3 還沒上線、無第三方分；代理＝Composer 2.5：Coding Agent Index 62 第三、SWE-Bench ML 79.8%，殺手鐧是便宜 10–60x。定位＝性價比前沿非榜首。
- 和 xAI 關係：整合是收購核心目的且已發生。Composer 2.5 早就在 xAI Colossus 訓練；Cursor 資料餵 Grok；Composer 進 Grok Build CLI。垂直棧 Colossus→Grok/Composer→Cursor→Origin 打 Anthropic/OpenAI。
- 「模型純 Cursor？」到 2.5 為止是：底模＝Kimi K2.5、RL/研究＝Cursor、算力＝xAI。Composer 3「1.5T 從零」會讓「純 Cursor」線糊掉——且行銷從「建在 Kimi」改口「從零不靠 Kimi」，跑在已揭露事實前面。
- 評估 Cursor 模型力框架：已證明＝RL post-training + 基建(Anyrun、裸 Kimi 36→Composer2 61.3)+ 推論速度；未證明＝從零預訓前沿底模。偏科：harness 層頂尖、預訓練未證。正中 harness>model（已補該卡證據）。
- 對用戶最該警覺：中立 harness 被收編的 model-choice 風險——Cursor 從中立(可選 Claude/GPT)變 xAI 自家 harness。開放問題＝整合後還讓不讓你爽用 Claude。

---

## 2026-06-21 — 第一次 /weekly-synthesis 試跑（攝取流程落地驗證）

**背景**：上一條對話設計了攝取流程，建了 `weekly-synthesis` skill + 把 profile 開放疑問改造成預測帳。這條是第一次真跑這個 skill。

**掃描範圍**：inbox 本週 11 條（06-14→06-21）+ notes/topics git log + freshness。

**抽出 4 個跨主題模式（單條看不出、合起來才看出）**：
- A — harness>model 證據暴增週：Strands Shell／openclaw-Hermes／Ponytail／Cursor 四個獨立來源全壓同一張卡。既有卡被反覆驗證，不拆新卡。
- B — 「預編譯本地索引、按需 page-in」繞了 5 次（Hermes FTS vs OpenClaw JSONL／自動蒸餾／部門大腦 wiki=硬碟／攝取流程／B8 profile 瘦身）→ **升級成卡**。
- C — 「中立基礎設施層被有模型巨頭收編」3 次（Cursor／Andrew Ng／eval）→ 大致已被既有卡覆蓋，不拆。
- D — 「核心動作=一次 LLM call 的生態位天花板」≥3 次（merge 閘／eval／資安計價）→ **升級成卡**。

**結算預測**：本輪無到期（預測帳這週才建，最早 check 是 2026-07）。如預期，第一次只抽 pattern。

**過期卡**：open-source-is-commoditization-clock、benchmark-saturation 兩張 freshness 2026-05，過一個月，當快照看。

**產出（用戶 AskUserQuestion 兩張都批 建卡）**：
- `topics/ai-industry-reading/cards/llm-call-niches-are-features-not-companies.md`（Pattern D，元判斷層）
- `topics/coding-agents/cards/precompile-to-local-index-not-restuff-context.md`（Pattern B，記憶架構層）
- 卡數 22→24（ai-industry-reading 9、coding-agents 16）。

**坑/驗證**：B 卡本想為元主題（知識系統設計）開 `topics/knowledge-systems/` 新資料夾，但為單卡開資料夾=過度儀式，改放 coding-agents 記憶線、appears-on 標 knowledge-systems。日後元主題長更多卡再獨立。

**狀態**：✅ skill 跑通，第一次就抽出 2 張可升級元卡＝週綜合補的「批次回看才看得出的 pattern」真有產出。CLAUDE.md 同步加了「攝取節奏」段（每日捕捉+互動先預測+每週 /weekly-synthesis）。

**元判斷**：weekly-synthesis 的價值在「橫切」——同一週的散條目，逐條看都已記過，但橫著掃才看出 4 條跨主題結構。這是睡前增量步驟結構上做不到的。

---

## 2026-06-22 — Sakana Fugu：把多 agent 協作做成「一個模型」

**觸發**：用戶丟 Fox Hsiao Threads 貼文圖（IMG_4897）說「理解下」。

**內容**：日本 Sakana AI 今天（06-22）發表 Sakana Fugu——把 multi-agent orchestration 包成單一 OpenAI 相容 API。背後是個被訓來「指揮其他模型」的 LLM，自選模型/分派/驗證/彙整。技術來自 ICLR 2026 兩篇（TRINITY 三角色動態分派、Conductor 用 RL 學自然語言協作策略）。兩版本（Fugu / Fugu Ultra），計費只算當下最高階模型不疊加（Ultra $5/$30）。官方自報跑分對標 Fable 5/Mythos（SWE Bench Pro 73.7、LiveCodeBench Pro 90.8、GPQA-D 95.5），主打「不受美國出口管制」。Llion Jones（Transformer 共同作者）、David Ha 創辦。

**用戶要求「都做」＝查證 + 沉判斷**：

查證（web）✅ 全屬實。補一個貼文沒講的關鍵：conductor 只有 **7B 參數**——重點是「小腦袋路由一池大模型」，一家頭條寫 *without training a single frontier model*。⚠️ 跑分全 Sakana 自報，沒看到第三方獨立驗證。

**抽出的可重用判斷**：**orchestration-as-a-model——把 harness 內化進模型權重，是對「harness 中立可換」的反論。** 在 coding-agents（harness 歸屬）+ agent-collab（協作單位）兩線都用得上。↔ 對比 cursor-spacex-xai：那邊 harness 被收購吃掉，這邊被模型化吃掉，同方向兩種吃法。觀察點：用 Fugu 是省了自搭 harness 的工（便利財，harness 仍可自建取代），還是真的更強更便宜（才證明 orchestration 該被模型化）。

**坑/校準**：第一直覺差點被跑分（贏 Opus 4.5 分）帶走——拉回「估計值 vs 實測值」篩子＝官方自報不可信，真訊號在架構選擇 + 地緣定位。另存疑：「不受出口管制」若它路由的池子含美系模型，受限地區還用不用得到？＝可能的行銷破口。

**產出**：`notes/sakana-fugu-orchestration-as-model.md`。判斷已沉進筆記；卡片升級待用戶確認。

**狀態**：✅ 筆記進 main。新增兩條開放疑問（出口管制是真護城河還話術 check:2026-09；orchestration 該住 harness 還被模型化 check:2026-12）。

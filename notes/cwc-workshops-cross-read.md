# cwc-workshops 對讀：官方教法 vs 已沉澱卡片（2026-07-05）

材料：`/Users/atomo/Side_project/cwc-workshops/`（Anthropic 官方 Code with Claude workshop 材料，9 場，2026-07-05 入庫）。對撞對象：27 張卡（coding-agents 17＋ai-industry-reading 10）＋profile 已沉澱判斷。方法註記同 `prediction-ledger-stress-test.md`：Fable 與 Opus 4.8 同卡 A/B，本文融合、Opus 獨有標 `[O]`。

## 一、印證：官方做法支持了哪些卡

**1. agent-decomposition 是 harness-beats-model 的最強官方數據點。**
同一個模型，把 402 行 prompt 拆成 15 行＋400 行按需 skills、data-dump 工具換 code execution、3 個 hardcoded subagent 砍到 0——分數 71%→92%（+21pt）、F1 從 102 次 tool call 降到 3 個 script。**不換模型、只動 harness 層，+21pt**，比卡片現有的 Terminal-Bench 證據（同模型換 harness 差 5.2pt）幅度更大，且出自模型廠自己的教材（利益上它更想教你「換更強的模型」）。→ 補進 `harness-beats-model` 卡的證據欄。

**2. 「402 行沒消失、只是換了進 context 的時機」＝precompile-to-local-index 卡的官方版。**
workshop 自己點題：「The knowledge didn't shrink — the difference is *when* they're in context」。這同時直接支撐 Issue #6 的 R3（CLAUDE.md 壓行數）：規則（常駐）和知識（按需）要分離，268 行的 CLAUDE.md 抽模板段成 schema 檔就是同一個動作。

**3. audit.md 開宗明義＝eval-bottleneck-is-criteria 卡。**
「最令人意外的 eval 結果通常是 eval 的 bug、不是模型的事實」；grader 檢查項「grades outcomes, not paths」逐字對應 `agent-eval-scores-end-state-not-path` 卡，「over-specified：prompt 是 step-by-step recipe」正是卡裡的 pitfall 反例 `[O]`。rightmodel 的 model × thinking × effort 全交叉 sweep＝`eval-is-a-cross-model-judge-layer`（站在所有模型上面的中立裁判）的實作。

**4. phase-3 verifiable component＝artifact-verifiable-output 卡的進階版。**
`data-verify-*` DOM 屬性當機器可讀契約、`window.__verify.runAll()` 給 agent 的 handle、`BLOCKED`（沒觀察到）與 `FAIL`（觀察到且錯）刻意分開、`probe:true` fixtures 標對抗性邊界案例。這是把卡裡「截圖看結果」升級成「結構化 runtime 契約」——且與你昨天剛 merge 的 verifiable-component note 同題，**第 3 次交會**。

**5. 其餘對位**：CMA sandbox（每 session 隔離容器）→ 沙箱卡群；`production-ready-agent` 的 gated tool confirmation → `claude-code-human-in-loop` `[O]`；agents-that-remember 三段（隔離→store→Dreaming）→ `claude-code-six-layer-memory` 的托管版。

## 二、張力／新邊界

**1. 記憶層門檻：官方比我們的卡樂觀，但脈絡不同。**
我們的邊界是「記憶層勝負手只在塞不下時成立，塞得下別上」。agents-that-remember 卻把 memory store＋Dreaming 當預設原語。裁決 `[O]`：不是矛盾，是場景切分——單機個人場景 grep-over-markdown 夠用；**跨 session 的雲端 managed agent、transcript 量超出人工蒸餾時，Dreaming（批次讀舊 transcript 蒸餾成新 store）才是必需品**——而它正是 `/weekly-synthesis`＋profile 瘦身的托管同構。卡的邊界句可以加上這半。

**2. 「個人也能搞 eval」拿到定量的規模天花板。**
audit.md 的三層稽核：Tier 1 程式化掃全集（重複率/label 平衡/schema 破損）、Tier 2 分層抽 20-50 題人讀、Tier 3 per-task LLM auditor（一題一 call、先報價再跑）。個人版止於 Tier 1-2；Tier 3 是 MMLU-Redux/SWE-bench Verified 等再標註工程的自動化版，要預算意識 `[O]`。這替 `eval-bottleneck-is-criteria` 卡的「個人可搞」劃出上界。

**3. subagent 的負面判準（我們卡群缺的下界）`[O]`。**
決策框架給了 smell test：「subagent 的輸出是一個數字？→ 它就不該是 subagent」（tool call／skill／subagent 按成本遞增排）。我們的 orchestration 卡群偏重「何時該拆」，這條補「何時不該拆」——hardcoded subagent 從 3 砍到 0、delegation 改 runtime 決策，是 92% 那一跳的一部分。

## 三、新增量（值得吸收的做法，排序）

**① both-directions coverage：本次最該升卡的一條（三脈絡交會）。**
audit.md 檢查項：「測『該搜尋時有沒有搜』的 eval，也必須測『不該搜時有沒有不搜』，否則一個永遠搜尋的模型拿滿分——單側 eval 產生單側優化」。這跟同日 `prediction-ledger-stress-test.md` 抓到的「預測帳多數條目只設單側觸發→單向蒐證」（M2）是**同一個判斷在第三個脈絡出現**（eval 設計／預測帳設計／R1 防自評本質也是防單側）。按 B3 規則（≥3 脈絡）夠格升卡，判斷句擬：「**檢查只設單側，系統就往單側漂——eval、預測訊號、自評都要雙向覆蓋**」。落地：weekly-synthesis 加訊號三態 lint（壓測 note 建議 10）。

**② audit.md 當 fomo-kernel 鏡片與 fact-checker 的稽核清單（最高實用價值）。**
per-task auditor prompt（audit.md 附完整 JSON 模板：ambiguous / gold_suspect / answerable_from_memory / grader_too_strict / too_lenient / trivially_cheatable）＋「spot-check failures：抽讀被判錯的，>1/10 是 grader 錯就先修 grader」＋「known-good/known-bad 煙霧測試」。用在哪：fomo-kernel 的 VY 鏡片 golden set（本來就在優先序 3）、investment_note 的 fact-checker 稽核（label leakage／answerable-from-memory 檢查）`[O]`。LLM judge 小節（position bias／verbosity bias／self-preference／known-negatives 餵給 judge）對 triad-review 這類多方審查 skill 也直接適用。

**③ verifiable component 契約 → personal_os 看板 handoff。**
三個可移植機制：DOM 吐 `data-verify-*` 契約（refactor 不破契約）、BLOCKED≠FAIL（存疑判 fail：「false PASS 出貨 bug、false FAIL 只多看一眼」）、probe fixtures（零 probe＝只跑過 happy path）`[O]`。用在 Claude Design ROI 試點（`check:2026-07`）：verify-app 從「截圖＋vision」升級成「元件自報契約」。

**④ 分離式 prompt 結構當 CLAUDE.md 第二刀的模板。**
15 行常駐＋400 行按需的官方示範，直接照抄到 R3：CLAUDE.md 留規則，模板/schema/流程細節抽檔案。

**⑤ research-desk＝daily-brief pipeline 的現成骨架（等材料源解鎖）。**
SEC 研究台：head-of-research 每 ticker 派 analyst、fan-out/fan-in、outcome-graded scorecard、寫 memory store；預設 watchlist 是半導體、demo query 是「rank NVDA/AMD/MU by margin durability」——與 memory-industry-map 幾乎同題 `[O]`。orchestrator 實測（07-04）卡在材料源，這份給了解鎖後的參考形狀。

## 出處

`cwc-workshops/`：README.md、agent-decomposition/README.md（71→92 數據）、rightmodel/.claude/skills/eval-audit-and-sweep/references/audit.md（216 行全讀）、how-we-claude-code/README.md＋phase-3-verify/README.md（grep 核實）、agents-that-remember/README.md（grep 核實）；對位卡片見文內。Opus 4.8 同卡產出（深讀了 graders.ts、production-ready-agent、research-desk 細節）。

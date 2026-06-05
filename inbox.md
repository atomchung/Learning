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

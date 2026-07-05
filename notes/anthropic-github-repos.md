# Anthropic GitHub Org 挖礦筆記(anthropics/*)

> 2026-07-05 啟動,`/loop` 持續挖掘中。這篇是**借鑒型**筆記(vs `anthropic-blog-2026-06.md` 那種判讀型)——重點是「有哪些機制可以直接搬進我自己的 skill/agent 專案」,不是產業信號。
>
> 起因:cwc-workshops 這個 repo 本身就是 `anthropics/cwc-workshops`(官方 workshop 教材),順手查了整個 org 還有什麼值得挖。

## Org 地圖(按 star 數,篩出跟我的專案相關的)

| repo | 跟我哪個專案對得上 |
|---|---|
| `skills`(15.8萬★) | xhs_skills、claude-plugins/(personal-os marketplace) |
| `claude-agent-sdk-python`(7.5k★) | personal_os、crewai_xhs、xhs_autoresearch 這類手刻 agent loop |
| `claude-plugins-official`(3.1萬★) | claude-plugins/ marketplace 結構參考 |
| `launch-your-agent`(679★) | kol_collector/fomo-kernel 的「產品化」路徑 |
| `claude-code-security-review`(5.4k★) | 可直接當 CI gate,呼應 CLAUDE.md 的安全性規則 |
| `knowledge-work-plugins`、`defending-code-reference-harness`、`agent-sdk-workshop` | 待挖(見下方佇列) |

## 深挖 #1:Agent Skills 規格(agentskills.io/specification)

`anthropics/skills` repo 裡的 `spec/agent-skills-spec.md` 已經只是個指標,規格本體搬去 agentskills.io 了(表示這已經是**跨廠標準**,不只是 Claude 專屬——第一手訊號:Anthropic 自己在把 skill 格式往開放標準推)。

**具體到會影響我怎麼寫 SKILL.md 的硬限制**(這幾條我原本沒細查過):
- `name`:最長 64 字元,只能小寫字母數字連字號,**必須等於資料夾名**,不能連續連字號
- `description`:最長 1024 字元,規格明講「該同時說明做什麼 + 何時觸發,並包含關鍵字幫 agent 判斷相關性」——爛範例就是只寫「Helps with PDFs.」,好範例會把觸發語境也寫進去(這點我在 xhs_skills 那組可以重查一次觸發詞夠不夠具體)
- `allowed-tools`(實驗性):空格分隔的預授權工具字串,例如 `Bash(git:*) Bash(jq:*) Read`——這是**跳過權限詢問**的正式聲明位置,不是 hack
- **Progressive disclosure 三層**,官方明確建議數字:
  1. metadata(name+description)~100 token,開機全載
  2. SKILL.md 本體 **< 5000 token 建議值**,啟用時全載
  3. `scripts/`/`references/`/`assets/` 按需載入
  - 明講「SKILL.md 主文件保持在 500 行以內,細節搬到 references/」——這是我可以直接拿去檢查 xhs_skills 有沒有超標的量化門檻

**接既有判斷**:這篇補強 `notes/skills-workflow-best-practices.md` 缺的「精確欄位規格」那塊,兩篇該互相連結。

## 深挖 #2:`skill-creator` 與 `mcp-builder`(anthropics/skills 裡的兩個 meta-skill)

這兩個是「用 skill 生產 skill / MCP server」的官方參考實作,寫法本身就是最佳實踐範例。

**skill-creator 的迭代迴圈**(不是隨手寫完就丟,是有明確的 evaluate 步驟):
> 決定做什麼 → 寫草稿 → 寫測試 prompt → 背景跑「有這個 skill 的 Claude」→ 質化+量化評估(有 `eval-viewer/generate_review.py`)→ 依回饋重寫 → 重複 → 擴大測試集再跑一輪

這跟我在 `topics/coding-agents/` 已經有的「eval 瓶頸是寫判準不是工具」那張卡完全對得上——官方也把「先跑 eval 再迭代」當 skill 開發的預設流程,不是選配。**可借鑒動作**:xhs_skills 目前有沒有配對的 eval/test prompt?如果沒有,這是缺口。

`skill-creator` 還有一條溝通原則值得記:寫 skill 說明時要**依使用者的技術詞彙熟悉度调整措辭**——"evaluation"/"benchmark" 算邊緣可用詞,但 "JSON"/"assertion" 要先確認使用者懂再用。這條本身也適用於我跟 ting 的互動(但 ting 是工程背景,不太需要這條)。

**mcp-builder 的四階段流程**(對應我在 `mcp/` 專案的開發方式):
1. 深度研究規劃(先讀 MCP 協議規格 sitemap + 框架文件,而不是憑印象寫)
2. Tool 設計:**API 覆蓋度 vs 工作流工具**的取捨——官方建議「不確定時優先做完整 API 覆蓋,給 agent 組合的彈性」,而不是預先幫 agent 做決定
3. 一致的命名慣例:`github_create_issue`、`github_list_repos` 這種「動詞在後、前綴分類」的模式
4. **可執行的錯誤訊息**:錯誤要引導 agent 走向解法、給具體下一步,不是丟 stack trace

推薦技術棧:TypeScript + Streamable HTTP(遠端)/ stdio(本機)——理由是 TS SDK 支援度好、MCPB 相容、且模型生成 TS 程式碼品質高(靜態型別 + lint 工具成熟)。**跟我目前 `mcp/` 用 Node.js 的選擇一致**,算是驗證而非新資訊。

## 深挖 #3:`launch-your-agent`——founder-to-agent 的產品化模板

結構是 `.claude/skills/launch-your-agent/` 四階段(interview → stage & launch → grade & iterate → run without you),外加一個 `wrap-up` companion skill 專門做「收尾/現況檢查」。

**這個四階段拆法可以直接拿來對照 kol_collector/fomo-kernel 的產品化路徑**:fomo-kernel 目前有「機械層抓大放小 + VY 鏡片找動機」的核心邏輯,但還沒有正式的 interview→scope v0→grade→schedule 這種顯式分期。`wrap-up` 這個「隨時可觸發、生成現況總覽 + 建議下 1-2 個升級方向」的 companion skill 設計,也呼應我自己 Learning repo 裡 `README.md` 當「地圖」的角色——值得記一筆:**官方也認為「產品/agent 建完後需要一個獨立的 wrap-up/overview 機制」是標配,不是加分項**。

## 深挖 #4:`knowledge-work-plugins`——role-based plugin 拆法,以及一個「memory-management」skill 幾乎就是我自己在用的架構

結構統一:`plugin-name/.claude-plugin/plugin.json`(manifest)+ `.mcp.json`(工具連接)+ `commands/`(顯式觸發)+ `skills/`(自動觸發的領域知識)。11 個 plugin 對應 11 種角色(sales/finance/legal/product-management...),每個都是「同一套骨架,換內容」——**這是 personal_os 目前那堆 skill(log-strength/record/record-todo/session-board...)可以參考的封裝單位**:現在是全域散裝 skill,knowledge-work-plugins 的模式建議「同一生活領域的 skill+command+connector 該打包成一個 plugin,而不是各自獨立」。

**最值得記的一個發現**:`productivity` plugin 裡的 `memory-management` skill,架構幾乎是我自己這個 Learning repo(以及 Claude Code 自己那套 auto-memory)的鏡像:

```
CLAUDE.md          ← Hot cache(~30 個人、~30 個常見詞,目標覆蓋 90% 日常解碼需求,~50-80 行)
memory/
  glossary.md      ← 完整解碼表(找不到才查)
  people/          ← 完整檔案
  projects/        ← 專案細節
  context/         ← 公司/團隊/工具脈絡
```

查找順序官方寫得很白:**先查熱快取(CLAUDE.md)→ 沒有查 glossary.md → 還是沒有就問使用者,並記下來**。跟我這裡「`profile.md` 是索引,一定先讀 → 要細節 grep 整個 repo → 原始問答在 `inbox.md`」的三層完全同構,連「hot cache 要控制在 ~100 行,別讓它長成長鏈」這條也跟我 `CLAUDE.md` 裡「profile 保持小」那條一字不差。**這是驗證而非新資訊**——但官方把「找不到就問使用者、然後記下來」寫成第三步顯式 fallback,這點我這邊沒有明文——我目前多半是「grep 不到就算了」,沒有「主動問+回填」這個閉環,值得檢查是不是漏了這步。

## 深挖 #5:`claude-agent-sdk-python`——它是「把 Claude Code CLI 包成 Python API」,不是通用多 agent 框架

裝完直接內建 bundle Claude Code CLI(不用另外裝),`query()` 回傳的是 Claude Code 本身的訊息流,`ClaudeAgentOptions` 裡的 `allowed_tools`/`permission_mode` 對應的就是 Claude Code 的工具集(Read/Write/Edit/Bash...)。

**這點對「要不要把 crewai_xhs / xhs_autoresearch 換成官方 SDK」這個待評估項目有直接影響**:這不是像 CrewAI 那種「模型無關、自己定義 agent 角色與工具」的框架,而是**用程式碼驅動一個 Claude Code 實例**。換句話說,選它等於把 harness 綁定在 Claude Code 的工具集與權限模型上,換來的是不用重造 tool-use loop、session 管理、權限閘;換不到的是 CrewAI 那種「多個不同角色 agent 互相傳遞訊息」的原生多 agent 拓撲(要自己用多個 `query()` session 拼)。**結論**:如果 crewai_xhs 的價值在於 CrewAI 的多角色分工,換 SDK 不是同類替代;如果 xhs_autoresearch 的 agent_loop 其實只是「反覆呼叫 Claude 做一件事」,換成官方 SDK 可能省掉不少手刻的 loop/重試邏輯。

## 深挖 #6:`claude-plugins-official`——marketplace 的版本鎖定機制 + 一個直接能用的 `claude-md-management` plugin

**`marketplace.json` 的核心結構**跟我在 `claude-plugins/`(personal-os marketplace)可以直接對照:
- 每個 plugin entry 用 `source: {source: "git-subdir", url, path, ref, sha}` 指到別的 repo 的子目錄,**同時鎖 `ref`(分支/tag)又鎖 `sha`(commit)**——意味著即使來源 repo 的分支繼續推進,marketplace 裡的版本是釘死的快照,不會被上游改動悄悄影響已安裝的使用者
- **plugin 的 `name` 是不可變 slug**,規格明講「改名會讓已安裝使用者出現 `plugin-not-found`」——要改顯示名稱用 `displayName`,真的要改 slug 就得在 `marketplace.json` 頂層加 `renames: {"old-name": "new-name"}` map 做自動遷移。這條對我自己那個 marketplace 有實際意義:**改 plugin 名字前要先想遷移路徑,不能說改就改**
- plugin 結構比 `knowledge-work-plugins` 多一個 `agents/` 目錄(agent 定義),跟 `commands/`/`skills/` 並列,三者是官方認定的三種可選組件

**直接可用的一個 plugin**:`plugins/claude-md-management`,核心是 `/revise-claude-md` command——「回顧這次 session 有什麼該寫進 CLAUDE.md 的學習,分清楚該進 `CLAUDE.md`(團隊共享/入 git)還是 `.claude.local.md`(個人/gitignore),草擬精簡的一行式新增,列 diff 給使用者確認才寫入」。**這件事我手上有 20+ 個子專案各自的 CLAUDE.md,目前是純手動維護**,這個 command 提供了一個現成的「session 結束前自動提案更新 CLAUDE.md」流程,概念上跟我自己的 `/record` 很像但目標檔案是 CLAUDE.md 而非任務卡——可以考慮直接裝這個 plugin,或參考它的四步驟(反思→找檔案→草擬精簡新增→列 diff 給確認)自己刻一個。

## 深挖 #7:`claude-code-security-review`——現成 GitHub Action,附一條硬限制要注意

一個 `.github/workflows/security.yml` 就能接:PR 觸發、diff-aware(只掃改動檔案)、語意理解而非純 pattern match、找到問題直接留 PR comment。可調參數包括排除目錄、自訂 false-positive 過濾指示、自訂掃描指示、timeout。

**硬限制,官方自己寫在 README 裡**:「這個 action 沒有針對 prompt injection 做防護,只該用在信任的 PR 上」,建議搭配 GitHub 的「外部貢獻者的 workflow 需要先審核才能跑」設定。**這條對 fomo-kernel 有直接意義**——那是一個 public repo(atomchung/fomo-kernel),如果之後想接這個 action 當 CI gate,必須先把「外部 PR 需維護者核准才跑 workflow」這個 repo 設定打開,否則等於讓外部 PR 能直接把惡意 prompt 塞進被審查的程式碼裡影響審查結果本身。

## 深挖 #8:`defending-code-reference-harness`——recon→find→verify→report→patch 的自主漏洞掃描 pipeline

Claude Mythos/Glasswing(見 `anthropic-blog-2026-06.md` 那次判讀)背後的**開源參考實作**。結構是「唯讀技能」(`/quickstart`、`/threat-model`、`/vuln-scan`、`/triage`,只讀寫檔案,可在 Claude Code 裡不加沙箱直接跑,只要每個工具呼叫都人工過)vs「**會執行目標程式碼的自主 pipeline**」(`/patch` 跑在 pipeline 結果上、`harness/` 本體)——後者**預設拒絕在 gVisor 沙箱之外執行**,除非明確覆寫。

**可遷移的一般原則,不只適用資安掃描**:把「唯讀規劃/分析」與「會執行程式碼的動作」拆成兩級信任,只有後者需要沙箱+egress allowlist。這條跟我自己 `run`/`verify-app` 這兩個 skill 的精神一致(起 dev server、跑 app 才需要更謹慎的環境),也呼應 CLAUDE.md 對「危險操作先確認」的要求——**這裡是官方把這個界線做成可執行的技術實作(gVisor + 白名單),不只是流程規範**。這塊比較偏資安專用場景,對我目前手上專案(多是內容生成/個人系統)直接借鑒空間小,但如果 fomo-kernel 或 mcp/ 之後要做「agent 自動跑別人程式碼」這類功能,這是現成的沙箱設計參考。

## 深挖 #9:`agent-sdk-workshop`——一個「循序漸進解鎖能力」的教學設計,本身就是好的 agent 心智模型

`01-guided-demo/` 用**同一個 agent、同一個任務,跑四次、每次翻一個開關**教會四個 SDK 原語:
```
Stage 0  全關          system_prompt              純聊天,無工具無狀態
Stage 1  ENABLE_TOOLS      @tool + mcp_servers        agent 能查資料
Stage 2  ENABLE_SUBAGENTS  AgentDefinition + Task 工具  agent 能委派給專家
Stage 3  ENABLE_MEMORY     hooks + 持久化工具          agent 跨重啟記得事
```
`02-breakouts/` 則是「給 19 個工具(6 類)+ 6 個 sub-agent,自己組一個 agent 出來解某個 use case」的組裝練習。

**這個四階段拆法本身就是一個可重用的檢查清單**,拿來對照我手上任何一個手刻 agent(xhs_autoresearch 的 agent_loop、crewai_xhs):問「它現在停在哪一階?要不要往下一階升級?」比直接說「要不要換官方 SDK」更細——換 SDK 不是一次性二元決定,是這四層各自可以獨立引入(先加 tool、再加 subagent 委派、最後加跨 session 記憶),不换底層框架也能借用這個階梯思考。

## 挖掘佇列(下一輪 `/loop` 接著挖,不要重挖上面已覆蓋的)

- [x] `knowledge-work-plugins`——已挖(見深挖 #4)
- [x] `claude-agent-sdk-python`——已挖(見深挖 #5)
- [x] `claude-plugins-official`——已挖(見深挖 #6)
- [x] `claude-code-security-review`——已挖(見深挖 #7)
- [x] `defending-code-reference-harness`——已挖(見深挖 #8)
- [x] `agent-sdk-workshop`——已挖(見深挖 #9)

**原訂佇列已清空**(9 輪深挖涵蓋 org 地圖裡跟我專案相關的全部 repo)。尚未挖的方向,留給下次要不要繼續時挑:
- cwc-workshops 這個 repo 本身的 8 個 workshop 內容(目前只挖了 org 層,沒細挖這個 repo 自己的教材)
- org 裡星數較低但可能有料的專項 repo(如 `claude-for-legal`、`claude-desktop-buddy`、`agent-sdk-demos`)——目前判斷跟我手上專案關聯度低,先不挖

## 坑/校準

- 一開始只把 org 掃了「star 排序 + description 一行」,那份夠回答「有哪些 repo」,但不夠回答「學到什麼」——真正的料要進到 repo 內部檔案(spec 文件、SKILL.md 原文)才挖得到,純靠 `gh api repos/...` 的 metadata 不够。
- 第二輪校準:挖 `knowledge-work-plugins` 時一開始只想找「skill 封裝模式」,沒預期會挖到跟自己記憶系統同構的東西——**借鑒型挖掘也可能挖出「驗證型」發現**(這個架構我已經在用,官方獨立收斂出同一設計=交叉驗證,不是新機制),不要預設每條發現都得是「沒做過的新東西」才算數。
- 第三輪校準:`claude-code-security-review` 的「不防 prompt injection、只用在信任 PR」這條限制,如果沒讀 README 細節、只看 feature list 會漏掉——**工具類 repo 的「不能做什麼/安全邊界」往往寫在 README 中段而非 features 列表**,挖的時候要故意找這段,不能看完 quick start 就停。
- 第四輪校準:佇列挖完後才發現「持續挖 repo」這個任務本身沒有天然終點——一開始只列了「org 裡跟我專案相關的 repo」當佇列,沒設「挖到什麼程度算完成一輪」的判準,導致佇列清空前都沒意識到要停下來問方向。下次開這種開放式 `/loop` 任務,該一開始就定義「佇列」的範圍邊界,而不是邊挖邊開放式擴充。

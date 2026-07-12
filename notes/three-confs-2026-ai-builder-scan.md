# 三場會議 26 支 talk 深掃：生成飽和後，價值全面移向「驗證/對齊/結構化 context」

> 2026-07-10 綜合。素材：Cursor Compile 2026（10 支）＋ Figma Config 2026（8 支）＋ AI Engineer World's Fair 2026（8 支）＝ 26 支 talk 逐支深掃，另納入 Anthropic「Field Guide to Fable」（5 技巧，先前已分析）。
> 一句話結論：**三個互不相干的社群（AI 工程 / 編輯器 / 設計）獨立收斂到同一件事——AI 生成能力飽和後，價值全面從「產字」移向「驗證、對齊、結構化 context」。這正是本 repo 一直押的方向（harness>model、eval 瓶頸、context/loop engineering、skills workflow），這次是一次大規模的外部驗證。**

## 為什麼掃這批、學到什麼

三場會議來自三個沒有交集的圈子：Cursor Compile 是編輯器/agentic coding，Figma Config 是設計工具，AIE WF 是 AI 工程社群。三邊沒有共用講者、沒有共用議程，卻在同一季講出同一組結論。**當利益相反、脈絡不同的三方同時說同一件事，就該當強訊號讀**——這是本 repo `harness-beats-model` 卡「賣鏟人自己背書」與 `loop-engineering`「三個利益相反方同時命名」用過的同一種辨識法。

## 四個「三會議都在講」的收斂主題

### 主題 1：Eval 的定義位移——從「文字對錯 / token 量」到「執行後系統狀態、產品驗證速度、形式驗證」

大家不再問「輸出的字對不對」，改問「跑完之後系統變成什麼樣、產品驗證得多快、能不能被編譯/測試硬驗」。

**Cursor 場**
- Sam Lambert（PlanetScale CEO）：eval 不能只測 LLM 的文字輸出，**必須把「執行後的系統狀態與環境遙測（CPU/Query 效能）」納入閉環**，形成「操作-觀測-修正」。
- Farhan Thawar（Shopify）：寫 code 不再是瓶頸，瓶頸移到「問題定義」與「Code Review / 驗證」；**你的核心壁壘就是自動化 eval**。
- Claire Vo（新 PM）：eval 指標應從「代碼產出量 / token 消耗」轉為「產品原型迭代與市場驗證的速度」。
- Alane Suhr（柏克萊）：人機意圖溝通天生模糊，評估 agent 不能只看對話，**必須引入編譯、測試案例等「形式驗證（form verification）」做硬 eval**。

**Figma 場**
- Setor Zilevu（Own the loop）：eval 不是純工程問題，「以人本定義何謂好」才是護城河；**「定義指標者即決定方向」**。他的 Z Methodology＝把專家隱性知識顯性化→轉成可計算模型→用算力增強人類。
- Harvey Whiting（Meta）：建「黃金測試集（Golden Sets）」科學化評估，設 80% 完美率為基準，**試點最終達到 87%**。

**AIE 場**
- Jeff Huber（Chroma）+ Jason Liu：不要靠直覺，用「查詢-文檔對」建**低成本 fast evals**（毫秒級，取代昂貴 LLM 裁判）；用 `cura` 把對話分群，以「使用率 × 表現」象限決定工具要修/建/忽略。

**對到本 repo**：直接印證 `topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md`（判準是理解問題不是工程）與 `agent-eval-scores-end-state-not-path.md`（評終態不評路徑）。這批 talk 把「終態」講得更具體：不只是「終態斷言」，而是「執行後的**系統遙測**」。

### 主題 2：Context——從「塞資訊」到「結構化 / 接地 / 裁切 / 動態載入」

沒有人再主張「context 越多越好」。全部轉向：給結構、接地到真實系統、裁掉中段、按需動態載入。

**Cursor 場**
- Alane Suhr：模型只懂「形式」不懂「意義」，context 設計的核心是**接地（grounding）**——精準建立自然語言形式與 API/系統狀態的指代對應。
- Linus Lee（Notational Intelligence）：prompt/context 應設計成有暗示性、**結構化的「記號 / 縮排」**，引導 LLM 做空間式推理；eval 要加語意擾動（隨機格式/順序）確保模型懂高階結構而非死記字詞。
- Ben Geist（Intelligence Efficiency）：Token 效益遞減，應從堆推理（Work）轉為優化上下文資訊效率（Information）；共享壓縮 KV cache 可減 42–57% worker token。

**Figma 場**
- Carola Pescio Canale（Atlassian）：實驗顯示 **catch-all context 檔（如 `DESIGN.md`）相較專用 MCP，會激增 92% token 消耗且變異度高**，不宜生產——應採「分層、職責單一」。
- Harvey Whiting（Meta）：AI 對「未定義處」會隨機套用通用網頁規範（即產出 AI slop），必須把 token、組件、規則徹底文檔化。

**AIE 場**
- Sally-Ann DeLucia（context 管理）：**頭尾保留（Head/Tail Preservation）**——保留系統提示與目標（頭）+ 最新狀態（尾），裁掉中段；裁掉的移到可檢索記憶庫動態查；快超載時把重活外包給**子代理分流**。
- Boris Cherny（Anthropic）：「Context Minimalism」——動手前先問 agent 探 codebase 邊界，**限制 context 長度以防注意力渙散**。
- Soumith Chintala：「缺乏正確情境的 agent 如同袋中頑石」，應優先優化 context 工程而非盲追更大雲端模型。

**對到本 repo**：印證 `notes/agent-context-best-practices.md`（三大策略：Tool Clearing / Memory / Compaction；sub-agent 隔離）與 CLAUDE.md「<200 行」原則。DeLucia 的頭尾保留＝compaction「該保留 vs 該丟」的一個具體策略；Atlassian 的 92% 數字則替「單一大檔 vs 分層」給了量化證據（見下方 TODO 3）。

### 主題 3：Skills＝可組合的 Markdown，而且「skills > agents」

不要為每個場景造一個脆弱的專用 agent；把程序性知識沉成可動態載入、可互相調用的 Markdown 技能。

**AIE 場（最直接）**
- Barry Zhang & Mahesh Murag（Anthropic 官方）：talk 名就叫 **《Don't Build Agents, Build Skills Instead》**。技能＝資料夾（`SKILL.md`＋腳本），平時只讀簡短描述、**觸發後才載入完整指令（漸進式揭示）防 context 膨脹**；觸發失敗優先改描述、不是改內部指令；**知識 Git 化，實測縮短新領域 onboarding 60–80%**。
- Pedro Rodrigues（Supabase）：**Braintrust 實測「MCP + Skills」完成度顯著優於單用一方**（單用 MCP 易漏安全配置）；核心安全規則要直寫 `skill.md`（agent 常忽略外部參考檔）；引導檢索最新文檔而非複製（防過期）。

**Cursor 場**
- Sam Lambert：把 skills 封裝成「高安全性、**單一職責**、結果可預測」的 API。
- Farhan Thawar：skills 與代碼「即用即丟」（disposable code），以極速實驗換回饋，而非追求完美。

**Figma 場**
- Harald Kirschner：專案根 `AGENTS.md`（願景邊界）+ **模組化 `.github/skills/`**（成功工作流存成 Markdown，按需動態載入）。
- Rodrigo（Figma deep dive: Agents）：技能本質是 Markdown，**且可互相調用**（Spec up 技能封裝了基礎 Doc 技能），利於層次化與規模化。

**對到本 repo**：印證 `notes/skills-workflow-best-practices.md`（四層系統 CLAUDE.md / rules / skills / hooks）與本工作區「skills project-scoped」的做法（xhs_skills symlink 掛 crewai_xhs、paperclip skills 不全域裝）。Rodrigues 的「MCP+Skills 互補」對到卡片 `mcp-as-extensibility-lever.md`。

### 主題 4：人類＝可觀測、可介入的判斷者（不是橡皮圖章）

三邊都反對「人退化成被動的 AI 產出審批者」，也反對「24 小時盯著 agent」。人類該做的是設計注意力預算、保持透明可介入、只在不可逆處守門。

**Cursor 場**
- Ryo Lu（Closer to the Material）：**玻璃介面原則**——讓 AI 的思考/計畫/執行步驟完全透明，人類隨時暫停接管；用「材料（可迭代的 code）」而非「黑盒產出」開啟人機循環，避免人退化為 AI slop 審批者。
- Michael Truell（Opening Keynote）：開發者轉型為管理 agent 艦隊的 **Agent Manager**（Cursor 95% 使用已由 agent 驅動），重心是 context engineering + eval 的「意圖-執行-觀測-修正」閉環。
- Alane Suhr：**拒絕 AI 擬人化**——AI 無獨立主體，能動性（agency）在人；系統定位是增強人、保留人的最終決策。

**AIE 場**
- Zack Proser（**Your Attention Is the Bottleneck**）：算力便宜、**注意力才是最稀缺瓶頸**；只在不可逆任務（部署、對外發信）設人工審查門檻，其餘全自動；**PR/Diff 作為交付單位**，用非同步佇列處理避免通知疲勞；一 agent 一 repo，完成封裝成 skill。
- Brandon Waselnuk（**Stop babysitting your agents**）：效率不彰的主因不是模型不夠強，是缺「決策級組織與歷史脈絡」；推「校準自治權（Calibrated Autonomy）」——自治權隨 context 完整度動態調整，別用人力 babysitting。
- Soumith Chintala：agent 有實際執行力，須設「災難性行為分類器」在高風險操作（刪帳號、轉帳）前攔截，並加 HITL 雙重確認。

**Fable（Anthropic「Field Guide to Fable」）＝這主題的操作層 SOP**
- 5 技巧：Blindspot Pass / Interview Me / Prototyping / Implementation Notes / Quiz。
- 核心論述：開發者從「寫碼者」→「**意圖對齊者 / 未知項管理器**」。

**關鍵連結**：Fable 5 技巧回答「**怎麼做**」（操作層 SOP：怎麼把盲點掃出來、怎麼讓 agent 反過來訪問你對齊意圖）；Cursor / AIE 這幾支回答「**為什麼**」（玻璃介面、注意力預算）與「**架構**」（PR 交付、校準自治、災難分類器）。兩層拼起來才完整。

**對到本 repo**：印證 `topics/coding-agents/cards/claude-code-human-in-loop.md`（每步確認是哲學不是妥協）與 `notes/loop-engineering.md` 的 **Maker-Checker**（做事的 agent 不准自評，要獨立 verifier）。Proser 的「多層驗證閘＋PR 交付」＝loop engineering 的 L1→L3 漸進放權在真實團隊的落地形態。

## 「只看 6 支」binge 清單（給時間有限的自己）

按「先建心法、再看架構、最後看落地」排序：

1. **Fable《Finding Your Unknowns》**（Anthropic）— 心法：從寫碼者到未知項管理器，5 技巧 SOP。
2. **《Don't Build Agents, Build Skills Instead》**（Barry Zhang & Mahesh Murag, Anthropic）— skills>agents 的官方論述 + onboarding 60–80% 數據。
3. **《Claude Code & the evolution of agentic coding》**（Boris Cherny, Anthropic）— loop engineering + context minimalism 的第一手。
4. **《Agents and Infrastructure》**（Sam Lambert, PlanetScale）— eval 納入系統遙測、small & sharp primitives、可逆性/沙盒。
5. **《Your Attention Is the Bottleneck, Not Your Agents》**（Zack Proser, WorkOS）— 注意力預算、PR 交付、只在不可逆處守門。
6. **《Best practices are trapped in your head and your AI has no idea》**（Harald Kirschner, Figma）— 把隱性知識沉成 AGENTS.md + skills 的最清楚示範。

## 三個值得追的前沿框架（比上面更新、還沒進本 repo 主線）

- **Baseten「軌跡權重化」**（The Memory Problem；Mudith Jayasekara / Charlie O'Neill / Harry Partridge）：別只靠 RAG 或拉長 prompt，把 agent 長期軌跡**編譯成 LoRA / 壓縮 KV cache**（Still 架構單次前向壓縮 8x–200x，壓完像 LoRA 權重可遞迴壓縮）。→ 對本 repo 的 `personal_os` 長時系統有啟發：長時 agent 的記憶不只是「外部檔案」，可能是「權重化的軌跡」。
- **IEU metacognitive loop**（The metacognitive design loop；Jenny Au & Mike Green, Figma）：出錯時走「**識別（Identify）錯誤 → 評估（Evaluate）標準落差 → 更新（Update）規則引擎**」，AI 自我審計、通過後自動 Git commit 更新規則，把隱性規則沉成永久 skill；QA 週期從 2 個月縮到 2 小時。→ 對到 `notes/loop-engineering.md` 的 goal loop 與 meta-review。
- **Z Methodology 四槓桿**（Setor Zilevu, Figma）：控制 AI 行為的四個把手＝**系統提示詞 / 評估設計 / 數據集 / 模型功能與工具**；其中「定義指標者即決定方向」。→ 對到 eval 筆記，可當「我到底能扳動哪些桿」的檢查表。

## 改善建議 / TODO（提議，待 ting 親自拍板與執行）

> 這四條都是「動 ting 親自精煉的熟料」，本次只提議、不擅動。每條都標了動哪個檔、加什麼、引哪支 talk 當佐證。

**TODO 1：升級 `topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md`**
- 加一條：**判準要從「文字對錯」→「執行後系統狀態 / 產品驗證速度」**。
- 佐證：Sam Lambert（eval 納入系統遙測、操作-觀測-修正閉環）＋ Setor Zilevu 的 Z Methodology（「定義指標者即決定方向」）＋ Claire Vo（指標從 token 量轉為驗證速度）。
- 為什麼：這卡現在偏「收集 case + 寫判準」，這批 talk 把「判準的內容」講得更具體（終態＝系統狀態，不只是文字斷言），值得補進「為什麼重要」段。

**TODO 2：`CLAUDE.md` 的「<200 行」精簡原則補量化理由**
- 現況：`notes/agent-context-best-practices.md` 已詳述 <200 行；本工作區 CLAUDE.md 的多處「保持小」是偏好陳述。
- 加什麼：把 Atlassian「**catch-all context 檔比專用 MCP 多燒 92% token 且變異度高**」這個數字掛上去，讓「保持小/分層」從偏好升級成量化理由。
- 佐證：Carola Pescio Canale（Atlassian, Figma Config）。

**TODO 3：新增一條判斷「單一大 context 檔 vs 分層拆檔」，並考慮升成 topics 卡**
- 這是 Figma 兩支**正面打對台**的點：Harald Kirschner 主張單一 `AGENTS.md` 當全局簡報；Atlassian 主張捨棄單一大檔、改分層職責單一（92% token 懲罰）。
- 我的裁決傾向：**ting 是多 repo 規模（本工作區十幾個子專案 + 各自 CLAUDE.md），站「分層」這邊**——單一大檔在小專案還好，跨多 repo 會 context drift。但「一個明確的頂層願景/邊界簡報」仍值得留（取 Kirschner 的 AGENTS.md 精神當入口、細節分層）。
- 為什麼值得升卡：這是「可跨脈絡重用的判斷」（每次開新子專案都會用到），符合 repo 的升卡訊號；可放進 `topics/coding-agents/`，與 `claude-md-as-project-contract.md` 對照。

**TODO 4：把三個前沿框架納入對應筆記的追蹤線（見上一節）**
- Baseten 軌跡權重化 → `personal_os` 長時系統的記憶架構選項。
- IEU metacognitive loop → `notes/loop-engineering.md` 的 goal loop / verifier 設計。
- Z Methodology 四槓桿 → eval 筆記，當「我能扳動哪些桿」的檢查表。

## 附錄：26 支完整片單（依會議分組）

**Cursor Compile 2026（10 支）**
1. Opening Keynote — Michael Truell（Agent Manager、Origin git 平台、與 xAI 訓 1.5T 模型）
2. What Is Your Job Now — Farhan Thawar（eval＝新護城河、LLM proxy、disposable code）
3. Closer to the Material — Ryo Lu（玻璃介面、材料 vs 產出、程式碼原型化）
4. The Memory Problem — Baseten（軌跡權重化、Still 架構壓縮 KV cache）
5. The New PM — Claire Vo（Finding Money、避免 token churn、驗證速度為指標）
6. Agents and Infrastructure — Sam Lambert（small & sharp primitives、系統遙測 eval、可逆性/沙盒）
7. Intelligence Efficiency — Ben Geist（熵減 Work vs Information、共享壓縮 KV cache）
8. Notational Intelligence — Linus Lee（結構化記號、2D 思考畫布、語意擾動 eval）
9. Explaining Culture to Technology — Paul Ford（文化即有損預測模型、修辭 > 事實、代碼即初稿）
10. Agency in Language — Alane Suhr（形式 vs 意義、接地 grounding、形式驗證、反擬人化）

**Figma Config 2026（8 支）**
1. Figma deep dive: Agentic workflows and the MCP — Jake Albaugh（精確 context 防技術債、作業-對答案 eval 閉環）
2. Best practices are trapped in your head — Harald Kirschner（AGENTS.md + .github/skills、design.md、Persona eval）
3. How structured thinking gives your AI superpowers — Carola Pescio Canale, Atlassian（brain dump、thinking.md、92% token 懲罰、分層職責單一）
4. Designed to be read — Harvey Whiting, Meta（Golden Sets 80→87%、Context-Skills-Agents 架構、主動稽核）
5. Own the loop — Setor Zilevu, Figma（Z Methodology、四大槓桿、eval＝把主觀分歧轉共識指標）
6. Figma deep dive: Agents（平行提示、可組合技能樹、實時連接器、受限變體）
7. Figma deep dive: Make（三層 Markdown、Skills 1-5 分自動評估、42 分鐘轉譯 SAP 級規範）
8. The metacognitive design loop — Jenny Au & Mike Green（BRD 代理人/概念插槽、Core UI MCP、IEU 框架、遞迴自我修正 + auto commit）

**AI Engineer World's Fair 2026（8 支）**
1. Don't Build Agents, Build Skills Instead — Barry Zhang & Mahesh Murag, Anthropic（漸進式揭示、程式碼即通用介面、onboarding 60–80%）
2. Claude Code & the evolution of agentic coding — Boris Cherny, Anthropic（寫迴圈非寫代碼、為未來模型設計、context minimalism、stopping condition）
3. Stop babysitting your agents — Brandon Waselnuk, Unblocked（打破搜尋滿意度、動態 context、校準自治權、代碼存活率 eval）
4. Your Attention Is the Bottleneck — Zack Proser, WorkOS（注意力預算、PR 交付、多層驗證閘、日誌自我優化、生理數據 MCP）
5. How we solved Context Management in Agents — Sally-Ann DeLucia（頭尾保留、可檢索記憶、子代理分流、長會話 eval）
6. Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase（核心規則直寫主檔、MCP+Skills 實測互補、引導檢索非複製）
7. How to look at your data — Jeff Huber, Chroma + Jason Liu（fast evals、對齊真實的合成數據、cura 對話分群、使用率×表現象限）
8. Personal, Local, Private AI Agents — Soumith Chintala（情境高於智能、透明心理模型、災難性行為分類器、細粒度偏好）

**Anthropic Field Guide to Fable（先前分析，納入綜合）**
- Finding Your Unknowns — 5 技巧（Blindspot Pass / Interview Me / Prototyping / Implementation Notes / Quiz）；核心＝開發者從寫碼者 → 意圖對齊者 / 未知項管理器。

## 出處
- [./three-confs-2026-scans/scan_cursor.md](./three-confs-2026-scans/scan_cursor.md)（Cursor Compile 2026，10 支逐支深掃）
- [./three-confs-2026-scans/scan_figma.md](./three-confs-2026-scans/scan_figma.md)（Figma Config 2026，8 支逐支深掃）
- [./three-confs-2026-scans/scan_aie.md](./three-confs-2026-scans/scan_aie.md)（AI Engineer World's Fair 2026，8 支逐支深掃）
- Anthropic「Field Guide to Fable / Finding Your Unknowns」（先前分析）
- 交叉引用：`topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md`、`agent-eval-scores-end-state-not-path.md`、`harness-beats-model.md`、`claude-code-human-in-loop.md`、`mcp-as-extensibility-lever.md`、`claude-md-as-project-contract.md`；`notes/agent-context-best-practices.md`、`notes/skills-workflow-best-practices.md`、`notes/loop-engineering.md`

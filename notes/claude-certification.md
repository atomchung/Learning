# Claude 認證計畫（Claude Certified Associate / Developer / Architect）

2026-07-13 起研究，2026-07 為止的現況快照（新計畫，內容會變動，讀者請視為當下快照）。

## 計畫總覽

隸屬 Claude Partner Network（Anthropic 投資 $100M 的 partner 生態）。目前 4 個進行中的考試，3 種角色 × 2 個等級：

- **Claude Certified Associate – Foundations**：$99，60 題，120 分鐘，無先修。對象是一般知識工作者，考 Prompt 結構化、內容驗證、Claude 產品功能（Projects/Artifacts）、隱私責任、流程治理、何時該升級給人審查——7 個領域，不考 code。
- **Claude Certified Developer – Foundations**：$125，53 題，120 分鐘，無先修。考 Agent SDK 寫 workflow、streaming/batch API、structured output 與錯誤處理、Claude Code 元件設定、成本/延遲/token/caching 取捨——偏 raw API 程式碼層。
- **Claude Certified Architect – Foundations**（CCAR-F）：$125，60 題，120 分鐘，無先修，~301 等級。5 個領域見下方詳解。
- **Claude Certified Architect – Professional**：$175，需先過 Foundations。

通過門檻都是 720/1000。年底前還會加銷售向、進階架構師等新考。

## 免費 vs 付費，別搞混兩件事

1. **真正免費、任何人都能拿**：Anthropic Academy 課程證書（`anthropic.skilljar.com`）——email 註冊、自助上課，完課發證書。**這不是**「Claude Certified X」監考認證，是完全不同層級（教學課程 vs 監考認證）。
2. **要考的監考認證預設要付錢**（$99–175）。免費的路只有：你（或你所屬組織）加入 Claude Partner Network，會員免費，但設計給有客戶交付能力的顧問公司，個人身分申請大機率不符資格。前 5,000 位 partner 員工可免 $99，但前提是先進得去 partner 組織。
3. **對個人而言的老實結論**：沒有查到對個人真正開放的免費監考考試路徑。最便宜是 Associate $99 現金付。

## Architect Foundations 的 5 大內容領域（官方 exam guide，v1.0，2026-07 生效）

- Domain 1：Agentic Architecture & Orchestration — **27%**
- Domain 2：Tool Design & MCP Integration — **18%**
- Domain 3：Claude Code Configuration & Workflows — **20%**
- Domain 4：Prompt Engineering & Structured Output — **20%**
- Domain 5：Context Management & Reliability — **15%**

考試含 4 個情境題（從 6 個情境池隨機抽），例如「用 Claude Agent SDK 建一個能處理高模糊度需求、透過自訂 MCP tool 存取後端系統的客服 agent」。

## 每個領域對應的官方 best practice（Anthropic engineering blog 原文摘要）

### Domain 1：Agentic Architecture（來源：*Building agents with the Claude Agent SDK*、*Effective harnesses for long-running agents*）
- 核心迴圈：**gather context → take action → verify work → repeat**。設計 agent 先問這四步各自怎麼實現。
- Agent SDK＝「給 agent 一台電腦」，是把 Claude Code 背後那套 loop/context 管理/內建工具抽出來當函式庫用。
- 長跑 agent 用兩階段：initializer agent 搭環境、coding agent 每個 session 做增量進度、留清楚產出物給下一個 session。

### Domain 2：Tool Design & MCP（來源：*Writing effective tools for AI agents*）
- 核心洞察：**agent 是非確定性的使用者，在用確定性的工具**——工具設計要當「跟一個會誤解、會亂猜的使用者簽的合約」設計。
- 五原則：策略性選工具、清楚命名空間（namespacing，如 `asana_search` vs `asana_projects_search`）、有意義的上下文、token 效率、prompt engineering。
- 評估反直覺：**效果量越大，需要的樣本數越小**——先 3-5 個手測案例就能看出工具描述好不好。

### Domain 3：Claude Code Configuration（來源：*Equipping agents for the real world with Agent Skills*）
- Skills 開發流程：先跑 eval 找 agent 卡在哪、再針對缺口寫 skill，不是先猜 agent 需要什麼。
- **SKILL.md 太肥就拆分**：拆成子檔案、用引用，讓不常一起用的內容分開存放以省 token。
- Loading 是漸進式（progressive disclosure）：先看 metadata 判斷相不相關 → 相關才讀全文 → 真的需要才讀被引用的細節檔。

### Domain 5：Context Management（來源：*Effective context engineering for AI agents*）
- 三個對抗「context 污染」的技術：**compaction**（context 快滿就摘要、開新視窗接著跑）、**structured note-taking**（寫進 `NOTES.md`/`TODO.txt` 這類持久檔案，等於外部記憶）、**sub-agent 架構**（各自乾淨 context 裡深挖，回傳精簡摘要給協調者）。
- **just-in-time retrieval / progressive disclosure**：只存輕量識別碼，真正需要時才載入細節。

### Domain 4：Prompt Engineering & Structured Output（來源：Claude Platform Docs — *Prompt engineering overview*、*Prompting best practices*、*Structured outputs*）
- 官方 prompt engineering 指南分三部分：模型特定指引（不同 Claude 模型行為不同）→ 通用技巧（清晰度、範例/multishot、XML 結構、role prompting、thinking、tool use、agentic systems）→ 舊版 prompt 遷移建議。
- **Structured outputs 不是「拜託模型輸出合法 JSON」**：底層用 **constrained decoding**，把 JSON schema 編譯成文法，推論時主動限制 token 生成，跟單純 prompt 要求格式是不同機制。
- 兩個互補功能：JSON outputs（`output_config.format`）與 strict tool use（`strict: true`）。啟用 strict tool use 的 schema 驗證有硬性要求：每個 object 都要設 `additionalProperties: false`，且所有屬性都要列進 `required` 陣列。
- 新 schema 第一次請求有 ~100-300ms 編譯文法的開銷，之後快取 24 小時；正式環境建議部署時發一次假請求預熱快取。
- 可靠度數字（供參考，會隨模型版本變動）：Anthropic tool use 99.8% schema compliance，跟 OpenAI（99.9%）、Gemini（99.7%）同量級。

## 跟既有卡的交叉驗證

- Domain 5「just-in-time retrieval / progressive disclosure」＝我的卡 [`precompile-to-local-index-not-restuff-context`](../topics/coding-agents/cards/precompile-to-local-index-not-restuff-context.md) 幾乎同一句話——官方原始出處替這張卡背書，已在卡片補一段。
- Domain 3「SKILL.md 太肥就拆分」直接對上 07-08 在 fomo-kernel 討論的「SKILL.md ~27k 瘦成 dispatcher + 子檔案觸發才載」——原本只是「待做」的構想，現在多一個官方明文建議當外部驗證。

## 我的個人讀書計畫（誠實缺口分析）

先講結論：不是「都不會」。用考綱權重對照我已有的判斷，粗估：

- **強項（合計 62%）**：Domain 1（27%，harness/orchestration 系列卡）、Domain 3（20%，這整個 repo 就是活的 Claude Code 配置經驗）、Domain 5（15%，`precompile-to-local-index`、`tokenmaxxing.md`）。這些是**架構判斷層**的強，不代表熟悉考試會問的具體術語/情境包裝，需要對齊用詞，但底子在。
- **真缺口（合計 38%）**：Domain 2（18%，MCP tool design 的實作機制——命名空間、評估方法，我目前只有「產業訊號」層次的理解，沒有「怎麼設計一個 tool」的動手經驗）、Domain 4（20%，prompt engineering 具體技巧 + structured output/JSON schema 在 API 層怎麼做，筆記裡幾乎空白）。

### 三階段計畫

**Block A — 對齊用詞（強項域，半天）**
不用找新教材，直接用自己的筆記當教材：
- 讀官方 exam guide Domain 1/3/5 的條列敘述，對照 `harness-beats-model`、`orchestration-as-a-model-vs-neutral-harness`、`precompile-to-local-index` 三張卡，確認「這句考試會怎麼問」的術語轉換（例如「agentic orchestration」在考題裡可能包裝成的情境）。
- 目標：確認底層判斷都在，只補「認得考試的問法」。

**Block B — 補真缺口（重頭戲，真正要花時間）**
- Domain 2：讀官方 *Writing effective tools for AI agents* 全文 + Anthropic Academy 的 MCP 開發課程；**動手做**——在這個 repo 或 fomo-kernel 幫自己寫一個真的 MCP tool（例如把「grep 記憶」這個動作包成 MCP tool），實作比讀文章記得牢。
- Domain 4：讀 Claude Platform Docs 的 *Prompt engineering overview*、*Prompting best practices*、*Structured outputs*（`platform.claude.com/docs/en/build-with-claude/prompt-engineering/`、`.../structured-outputs`）——這塊之前是真空，現已補上摘要，讀原文補細節。

**Block C — 考前對答案**
- 讀完整版官方 exam guide（不是這次的第三方摘要），確認 6 個情境題範例的實際問法。
- 挑一個不用註冊的免費模擬考測手感，只當格式練習，不當唯一準備依據（第三方模擬考題庫的品質未經驗證，見下方可信度注記）。
- Domain 2/4 唸完 Academy 課程後自己出 3-5 題自問自答，驗證有沒有真的懂。

## 來源與可信度注記

這次 WebFetch 對外部網站（Pearson VUE、anthropic.com engineering 頁面、多個第三方部落格）**全部 403**，判斷是這個雲端環境的 egress 白名單擋掉，不是網站本身有問題。所有內容降級為 WebSearch 摘要，**沒有逐字核對原文**。

另外：這個認證 2026-03 才上線，短時間內冒出一整批高度相似命名的第三方「模擬考」網站（claudecertificationguide.com、claudecertifications.com、claudecertification.com、claudecertified.io、certsafari.com 等），是新證照剛推出常見的 SEO 內容農場模式——品質未經驗證，避免在上面留個資或付費買 Udemy 那類「模擬考課程」。相對可信的是 Anthropic 官方 Academy（`anthropic.skilljar.com`）與官方 exam guide PDF（走 Everpath 平台發布）。

## 練習

`practice-exam-architect-foundations.html`（同資料夾）——20 題自製模擬考，依官方 5 domain 權重比例分配（Domain1×5/Domain2×4/Domain3×4/Domain4×4/Domain5×3），每題附解釋與出處，本機開啟純前端無外部連線。

## 待辦 / 下一步

- 決定實際要不要報名 Architect Foundations（$125），報名後回填「實測 ROI」。

# Figma Config 2026 — AI/Builder Talk 掃描

掃描時間：2026-07-09
工具：agy (Antigravity CLI, Gemini) v1.1.0
共 8 支影片，序列掃描。

---

## 1. Figma deep dive: Agentic workflows and the MCP
URL: https://www.youtube.com/watch?v=D5WUW9X_-L0

**核心論點：**
AI 加速執行而非釐清，必須在前期投入平台化設計（確定性層與結構化上下文），以人類意圖引導 AI，避免氛圍編碼（Vibe Coding）帶來的技術債。（Jake Albaugh）

**3 個具體要點（Jake Albaugh）：**
1. **精確上下文防技術債**：精確程式碼片段（如 Code Connect）使 AI 用更少且更精簡的代碼完成更多工作，冗贅內容只會帶來拼湊的技術債。
2. **視覺畫布 Codify 隱性知識**：在 FigJam 整理知識比純文字更能釐清人對 LLM 的預期，且能由 Agent 依各自偏好自編譯為 Skill。
3. **作業與對答案的 Eval 閉環**：生成 Skill 前讓 Agent 練習做題並比對 Answer Key 分析 Delta，以差距優化自身 Skill。

**獨立開發者 Takeaway：**
1. **語意抽象（Context Engineering）**：建立單一源頭的語意抽象層（如 Hyper Token），用確定性編譯減少 LLM 推理損耗。
2. **自編譯與即時 Eval**：維護單一結構化知識源，讓 Agent 依模型自編譯 Skill。在複雜任務前插入「作業-標準答案」比對，以差距自我修正。

---

## 2. Best practices are trapped in your head and your AI has no idea
講者：Harald Kirschner
URL: https://www.youtube.com/watch?v=oTtaFABsVDE
（首次掃描空回應，重試成功）

**核心論點：**
AI 時代的開發瓶頸已非寫程式，而是缺乏脈絡；開發者須將大腦中的隱性知識（設計品味、Done 定義）沉澱為結構化的 Markdown 檔，建立人機共享的知識層。

**4個具體可操作要點（講者：Harald Kirschner）：**
1. **專案根目錄配置 (`AGENTS.md`)**：建立核心簡報檔，明確定立專案願景與邊界，確保每次對話 AI 都有統一的全局認知。
2. **模組化技能檔 (`.github/skills/`)**：將成功的人機協作工作流存為 Markdown，按需動態載入，防止 AI 每次重啟都重新學習。
3. **設計系統數據化**：將調色盤、字體、間距等寫入專屬文件（如 `design.md`），讓 AI 能直接生成具備特定美感的 UI 程式碼。
4. **角色化反饋（Personas）**：建立扮演「新用戶」或進行無障礙稽核的 Agent，自動執行 UI/UX 品質檢測（Evals）。

**獨立開發者 Takeaway：**
- **隱性知識代碼化**：將個人的設計品味與架構思維（Context Engineering）撰寫成 Markdown，即是把個人競爭力轉化為 AI 可讀的基礎設施。
- **Skills 與自動化 Evals**：善用模組化 `skills` 和 Persona 檢測，能省去大量人工 Review，實現一人高效交付。

---

## 3. How structured thinking gives your AI superpowers
講者：Carola Pescio Canale, Atlassian
URL: https://www.youtube.com/watch?v=CPkL9msCuIU

**核心論點：**
AI 的威力源於人類將大腦不完美的短期記憶外顯為「結構化思考檔案」，使 AI 從生成工具轉化為真正的思考協作者。

**具體要點：**
1. **無序傾倒法 (Carola Pescio Canale)**：錄音轉錄無序想法，由 AI 消化重組為結構化專案大綱。
2. **`thinking.md` 框架 (Carola Pescio Canale)**：維護記錄決策邏輯的 markdown，作為 AI 脈絡引擎，使其回答符合特定思維。
3. **分層結構數據 (Atlassian)**：實驗顯示 Catch-all 脈絡檔（如 `DESIGN.md`）相較於專用 MCP，會激增 92% token 消耗且變異度高，不宜於生產。

**獨立開發者 Takeaway：**
- **脈絡工程**：捨棄單一大型脈絡檔，應採「分層、職責單一」的 Schema 或 MCP 降低 token 並防止 Context drift。
- **隱性知識轉化**：透過語音/隨筆 Brain Dump 後，用 AI 程式化地對齊至結構化模版，固化為 Agent 可讀脈絡。
- **技能與評估**：將決策原則與運行邏輯解耦（如獨立成原則檔），能大幅提升 Eval 準確度與技能複用性。

**注意**：此支的 92% token 數據與 talk 2（Harald Kirschner 的單一 `AGENTS.md`）建議方向有張力，值得對照看。

---

## 4. Designed to be read: making a system AI can actually use
講者：Harvey Whiting, Meta
URL: https://www.youtube.com/watch?v=TQaYwH6f4DA

**核心論點：**
AI生成的關鍵在於品質而非速度。系統必須從「供人閱讀」重建為「供AI讀懂（Designed to be read）」的結構化Context基礎，否則只會加速產出「AI垃圾」。

**具體要點（Harvey Whiting）：**
1. **建立黃金測試集（Golden Sets）**：以大量測試案例進行科學化評估，設定80%完美率為基準，Meta試點最終達到87%。
2. **Context-Skills-Agents架構**：Context是基礎知識；Skills是理解何時與如何應用；Agents是結合兩者自動執行任務。
3. **主動稽核Context**：AI對未定義處會隨機套用通用網頁規範，必須將Token、組件與規則徹底文檔化。

**獨立開發者 Takeaway：**
- **隱性知識轉化**：將專有的程式碼庫與設計意圖轉化為AI可讀的結構化Token與MCP協定，這是AI Agent的基石。
- **迭代而非單次**：摒棄One-shot期待，建立「提示-反饋-修正」的評估（Eval）機制，將AI當作需要引導的初級協作者。
- **跨媒介無損翻譯**：善用LLM的程式碼/設計翻譯能力，在設計稿與多種程式語言間建立流暢的雙向無損轉換系統。

---

## 5. Own the loop: how designers and researchers win with AI evals
講者：Setor Zilevu, Figma
URL: https://www.youtube.com/watch?v=VfA-vjsFQ1o

**核心論點：**
在 AI 能力商品化的時代，AI 評估（Evals）並非純工程問題，以人本出發定義「何謂好」的設計與研究，才是產品真正的護城河。

**具體可操作要點（Setor Zilevu）：**
1. **Z Methodology 框架**：將專家的「隱性知識」顯性化，再轉化為「可計算模型」（如 Skill/Context），最後用計算力增強人類。
2. **掌控 AI 四大槓桿**：透過主導「系統提示詞、評估設計（定義指標者即決定方向）、數據集、模型功能/工具（Capabilities）」來控制 AI 行為。
3. **Evals 的本質**：將人類的主觀分歧轉化為可衡量的共識指標，用以系統性地引導模型輸出。

**獨立開發者 Takeaway：**
- **將隱性知識顯性化作為壁壘**：開發 Agent 的關鍵在於將特定領域的隱性知識結構化為 Context 與 Skill，這是大模型無法自動生成的獨特資產。
- **建立 Eval 驅動開發**：不要盲目微調 Prompt。應先定義評估指標（Eval）並建立黃金數據集，以此作為引導與迭代 Agent 性能的指南針。

---

## 6. Figma deep dive: Agents
URL: https://www.youtube.com/watch?v=0HqSSIPZkbI

**核心論點：**
Figma Agent 定位為畫布上的協作者，透過可組合的技能與連接器自動化繁瑣任務，在非線性流程中輔助創作，確保創意直覺由人類主導。

**具體操作要點：**
1. **平行提示 (Tammy)**：在 Agent 執行時，用戶可同步在畫布他處編輯或發起新 Prompt，實現多任務並行。
2. **可組合技能 (Rodrigo)**：技能本質是 Markdown，且可相互調用（如 Spec up 技能封裝了基礎 Doc 技能），利於專業知識的層次化與規模化。
3. **實時連接器 (Rodrigo)**：透過 MCP（如 Notion/Slack）及本地 CSV 動態加載或反寫數據，打破工具孤島。
4. **受限變體 (Rodrigo)**：可限制 Agent 僅變更排版而不改動樣式，進行精準的局部探索。

**獨立開發者 Takeaway：**
- **隱性知識代碼化**：用 Markdown 撰寫技能，並建構「可組合技能樹」以降低 Prompt 冗餘。
- **上下文工程**：透過選區（Selection）與連接器，實現精準的「局部上下文注入」，防範資訊過載。
- **非線性協作與 Eval**：AI 應支持並行與就地微調。評估指標不應是「單次生成即完美」，而是多輪反饋的流暢度。

---

## 7. Figma deep dive: Make
URL: https://www.youtube.com/watch?v=q_-udq6jXpw
（agy 這次自行抓了完整逐字稿再分析，過程輸出含大量工具使用narration，已濾除只留分析內容；grep 注入特徵無命中）

**核心論點：**
設計系統封裝為NPM與三層Markdown的Make Kit，配合Skills評估，引導AI產出合規代碼。

**操作要點：**
1. **三層Markdown (Brett)**：拆分guidelines（風格）、discovery（防幻覺）與setup（依賴）提供小Context。
2. **Skills自動評估 (Laura/Brett)**：用腳本評估合規度並給1-5分，設門檻以完成Eval閉環。
3. **快速轉譯 (Laura)**：人類規範經LLM重構，42分鐘將SAP級規範轉化為AI指引。

**獨立開發者 Takeaway：**
- **Context工程**：以guidelines為入口引導AI按需讀取其餘檔案，防止注意力分散。
- **Eval安全閥**：將驗證邏輯封裝為Skill，用量化評分做為自動化防線。
- **知識轉譯**：將隱性知識重寫為「導航(Discovery)+邊界(Setup)+原則(Guidelines)」執行手冊。

---

## 8. The metacognitive design loop
講者：Jenny Au & Mike Green
URL: https://www.youtube.com/watch?v=360gz1lqWt0

**核心論點：**
藉由「元認知設計循環（Metacognitive Design Loop）」讓 AI 進行自我審查與糾錯，並將 QA 移至設計最前端，能消除生成式 UI 的治理偏差，使開發與 QA 週期從 2 個月縮短至 2 小時。

**具體操作要點：**
1. **BRD 代理人與概念插槽 (Jenny Au)**：AI 結構化訪談 PO 釐清需求，將自然語言轉為組件，未匹配置入「概念插槽」供人審查，落實策略保護。
2. **Core UI MCP (Jenny Au/Mike Green)**：統一 Figma 與代碼庫命名，利用 MCP 讓 AI 直接讀取 Figma Live Token 與組件，消弭 AI 猜測。
3. **IEU 邏輯引導框架 (Jenny Au)**：出錯時採「識別（Identify）錯誤、評估（Evaluate）標準落差、更新（Update）規則引擎」，將隱性知識寫入永久規則。
4. **遞迴自我修正 (Jenny Au)**：AI 自我審計並自動循環糾錯，通過後自動 Git Commit 更新規則，建構進化的 QA 共用大腦。

**獨立開發者 Takeaway：**
- **Context 工程**：命名對齊是關鍵。UI 與代碼的 Schema 命名偏差會導致 agent 幻覺，須建立無歧義的 Single Source of Truth。
- **Eval 與 Skills 沉澱**：結合 IEU 框架將「隱性設計規則」轉為動態 Eval 測試案例。每次修正都是一次 Git commit，使規則直接沉澱為 Agent 的永久 Skill。
- **MCP 應用**：利用 MCP 作為 Agent 與工具（如 Figma、IDE）間的實時動態上下文橋樑，取代硬編碼的靜態 Prompt。

---


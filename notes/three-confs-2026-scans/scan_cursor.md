# Cursor Compile 2026 — 10 支 Talk 深掃筆記

來源：YouTube「Cursor Compile 26」會議影片，用 agy (Gemini) 逐支深度分析。
掃描對象：agentic coding / context engineering / eval / skills / personal AI 系統的獨立開發者視角。

---

## 1. Opening Keynote — Michael Truell

**URL**: https://www.youtube.com/watch?v=fWa7uxyhVDE

### 核心論點
Michael Truell 指出軟體開發已從「AI 輔助對話」跨入「AI Agent 自主編程」時代，開發者角色正轉型為管理 Agent 艦隊的「Agent Manager」，而 Git、IDE 等底層基礎設施必須為了 Agent 的特性重新建構。

### 3 個具體要點
1. **Agent 特化 Git 平台 Origin (Michael Truell)**：針對 Agent 高頻並發提交與自動衝突解決設計，將 Agent 視為 PR 與 Code Review 的第一等公民，擺脫傳統為人類設計的 Git 限制。
2. **移動端 Supervision 模式 (Tomas Reimers)**：推出 Cursor Mobile，讓開發者隨時隨地能透過手機監管與批准雲端 Agent 進行代碼重構或 Bug 修復。
3. **自主訓練 1.5T 參數模型 (Michael Truell)**：與 xAI 合作在 Colossus 超級電腦上訓練 1.5 兆參數的專屬代碼模型，擺脫外部 API 限制，以追求極致的上下文與推理效率。

### 獨立開發者 Takeaways
1. **轉型 Agent 協調者**：Cursor 平台 95% 使用已由 Agent 驅動。開發者應專注於 Context Engineering 與 Eval，建立「意圖-執行-觀測-修正」的自動化驗證閉環。
2. **開發「Agent 親和」工具**：未來的價值在於開發適合 Agent 讀寫、調用 Skills 與自動化測試的 API 和協議，而非僅為人類設計 UI。

---

## 2. What Is Your Job Now — Farhan Thawar

**URL**: https://www.youtube.com/watch?v=ByOF8qByGHU

### 核心論點
在 AI 寫程式能力超越人類的時代，軟體工程師的核心價值已從手動編碼轉移至基於品味與判斷力的規劃、架構與驗證，「學習」本身才是主要資產，代碼只是副產品。

### 3 個具體可操作要點
1. **釋放 90% 的代碼執行 (Farhan Thawar)**：讓 AI 撰寫 90% 以上代碼（半人馬模式），人類專注於定義目標與成果驗證。
2. **重心轉移至新瓶頸 (Farhan Thawar)**：寫代碼不再是阻礙，軟體開發的瓶頸已移至「問題的定義（做什麼）」與「代碼審查與驗證（Code Review）」。
3. **投資 LLM Proxy 基礎設施 (Farhan Thawar)**：自建 LLM 代理（如 Shopify 的 Genie）實現多模型路由與成本管控，使上層能自由更換 Cursor 等 Harness 工具。

### 獨立開發者 (Agent/Eval/Context) Takeaways
* **驗證（Eval）為王**：開發 Agent 時，你的核心壁壘是建立極致的自動化測試與 Eval，以快速校驗 AI 產出。
* **Context Engineering 是新「手藝」**：如何高效組織與精準傳遞 Context 以輔助 AI 做出正確 Judgment，是決定系統品質的關鍵。
* **Skills 與代碼「即用即丟」**：將 Skills 模組化，以極速實驗與拋棄式代碼（Disposable Code）獲取回饋，而非追求程式碼完美。

---

## 3. Closer to the Material — Ryo Lu

**URL**: https://www.youtube.com/watch?v=az6OEZV8iHw

### 核心論點
未來工具應讓人類保持「貼近材料（代碼）」，避免退化為被動的 AI 產出審批者，以維持判斷力與創造力。

### 3個具體可操作的要點（講者：Ryo Lu）
1. **產出 vs. 材料**：黑盒的「產出」會終止創作；引導迭代的「材料」才能開啟人機協同循環。
2. **玻璃介面原則**：讓 AI 的思考、計畫與執行步驟完全透明，允許人類隨時介入、暫停與接管。
3. **程式碼原型化**：用代碼做原型（如雕塑黏土）而非靜態 UI（如畫布），以應對 AI 的非確定性。

### 獨立開發者 Takeaways
* **Agent/脈絡工程/Eval**：拒絕單純的「黑盒聊天框」，將 Agent 的檢索脈絡、運行計畫與評估透明化，設計「玻璃化」工作流，讓用戶能精細進行脈絡工程與人工介入。
* **個人 AI/Skills**：避免全自動生成大量平庸代碼 (AI slop)，應以 AI 輔助快速原型迭代，開發如 ryOS 的高度客製、具靈魂的個人軟體系統。

---

## 4. The Memory Problem — Baseten

**URL**: https://www.youtube.com/watch?v=I8YnwUV2C9w

### 核心論點
長程 Agent 瓶頸在於 KV cache 線性膨脹，透過攤銷學習將上下文壓縮至固定維度，能以低成本實現近乎無損的超長記憶。

### 具體要點
* **選擇 vs 合成**（Mudith Jayasekara）：傳統「選擇」（篩選/淘汰 token）會丟失語意；「合成」以 MLP 將上下文提煉為固定維度，更近乎無損。
* **單次前向壓縮**（Charlie O'Neill）：Still 架構在每層使用 Perceiver，不需逐次優化，即可將 KV cache 壓縮 8x 至 200x。
* **遞迴壓縮權重化**（Harry Partridge）：壓縮後的快取運作如同 LoRA 權重，支持遞迴壓縮以處理極長任務。

### 獨立開發者 Takeaway
開發 Agentic Coding/個人 AI 別再只靠 RAG 或拉長 Prompt。應將 Agent 的長期軌跡「權重化」（編譯成 LoRA 或壓縮快取），將上下文工程從「提示詞篩選」轉向「神經網絡合成」，以極低 Token 成本運行超長工時任務。

---

## 5. The New PM — Claire Vo

**URL**: https://www.youtube.com/watch?v=4CAFK-rc26A

### 核心論點
在 AI 讓軟體構建成本趨零的時代，開發瓶頸已從「如何做」移向「做什麼與為什麼」，傳統工程守門型 PM 已死，需轉型為價值驅動者。

### 3 個 Claire Vo 提出的具體要點
1. **Finding Money**：摒棄 JIRA 票數思維，專注於能帶來行為改變與直接變現的商業痛點。
2. **Manifesting**：善用 AI 工具將想法快速轉為原型，從第一原理出發直接生成與測試。
3. **避免 Token Churn**：警惕狂刷代碼的虛假工作量，AI 應作為願景的加速器而非逃避思考的護盾。

### 獨立開發者（Agent/Coding/Context/Eval）Takeaway
1. **Context & Skills 重新定位**：Agent 的 Context engineering 不僅是寫對代碼，更需輸入「商業與用戶價值洞察」作為決策 Context，讓 Agent 具備評估產品價值（Skills）的能力。
2. **Eval 指標轉向**：評估指標應從「代碼產出量/Token消耗」轉化為「產品原型迭代與市場驗證的速度」。

---

## 6. Agents and Infrastructure — Sam Lambert

**URL**: https://www.youtube.com/watch?v=zxvyO5vnknI
（Sam Lambert 為 PlanetScale 執行長）

### 核心論點
AI Agent 的非確定性（Nondeterminism）要求底層基礎設施從「被動託管平台」進化為「主動的合作夥伴」，提供小而精準的原子級操作、閉環回饋與安全防退機制，方能讓 Agent 安全地操作真實生產系統。

### 具體可操作要點 (Sam Lambert)
* **小而銳利的原子級基本操作 (Small & Sharp Primitives)**：基礎設施應將複雜運作封裝，提供 Agent 單一職能的 API，而非大而籠統的接口。
* **安全與回滾機制 (Safety & Rewind Primitives)**：針對 Schema 變更等高危操作提供隔離環境，具備自動防爆（back-pressure）與一鍵還原（Undo）能力。
* **閉環反饋與遙測 (Closed-loop Feedback)**：將 Agent 的每次操作與系統實際成效（如 CPU/Query 性能）連結，形成「操作-觀測-修正」的自動化閉環。
* **細粒度流量與存取控制 (Traffic Control & Isolation)**：在查詢、憑證或標籤級別實行隔離，精細限制 Agent 的生產環境權限，以防行為失控。

### 給 AI Agent/Coding/Personal AI 獨立開發者的 Takeaways
* **Context & Skill 設計**：別試圖讓 LLM 閱讀複雜系統細節；應將 Skills 封裝成「高安全性、單一職責、結果可預測」的 API，並在 Context 中提供明確的規格與狀態回饋。
* **Eval 評估機制**：評估不能只測 LLM 的文字輸出，必須把「執行後的系統狀態與環境遙測（Metrics）」納入閉環 Eval。
* **Personal AI 安全架構**：開發個人助理或代碼代理時，務必將「環境分支（Branching）/沙盒」與「可逆性（Reversibility）」作為底層架構的標配，先在分支出沙盒驗證後再合併。

---

## 7. Intelligence Efficiency — Ben Geist

**URL**: https://www.youtube.com/watch?v=Z5M33oh-SAU

### 核心論點
AI 面臨 Token 效益遞減，應從堆疊推理 (Work) 轉為優化上下文資訊效率 (Information) 降低系統熵。

### 具體要點（Ben Geist）
* **熵減框架**：系統熵減由 Work (推理) 與 Information (上下文) 決定，現有模型過度偏重 Work。
* **KV快取共享**：共享壓縮 KV Cache 可減 42-57% Worker Token 與 21-31% 總 Token。
* **隱空間注入**：壓縮為 16 個隱表徵注入，用 372 倍少 Token 獲更高準確率 (63% vs 55%)。

### 獨立開發者 Takeaway
* **Context工程**：避免 Token 空間傳冗餘文字，改在隱空間壓縮共享 KV，降低 Agent 成本與延遲。
* **架構設計**：開發具「低延遲、大語料、零切換成本」注入方案，確保模型升級時無痛重用 Context。

---

## 8. Notational Intelligence — Linus Lee

**URL**: https://www.youtube.com/watch?v=rv_VS189aVI

### 核心論點
記錄與呈現思想的「記號系統（Notation）」是擴展認知的鷹架，其對智力的放大效果往往超越自動化運算工具本身。

### 具體要點（講者 Linus Lee）
* **好記號的屬性**：需具備「抽象化」與「暗示性/自然轉換」（如萊布尼茲符號），讓複雜運算轉化為直覺符號操作。
* **利用二維空間**：利用黑板或排版等 2D 視覺空間呈現記號，釋放腦部工作記憶。
* **不變性約束（玩具模型）**：用 Autoencoder 訓練 AI 發明符號時，必須施加「旋轉、尺度、對比度不變性」等感知限制，否則模型會以像素作弊，無法生成具語意且人類可讀的圖形。

### 獨立開發者 Takeaway
* **Context Engineering**：Prompt 與上下文應設計具暗示性、結構化的「記號/縮排」，引導 LLM 進行高效的空間式推理。
* **Eval 魯棒性**：評估 Agent 記憶/能力時應引入語意擾動（如隨機格式/順序），確保其理解高階結構而非特定字詞。
* **Personal AI UX**：個人 AI 應跳脫對話框限制，提供可視化的「思考畫布」，將高維隱空間概念編碼為用戶可操作的 2D 記號。

---

## 9. Explaining Culture to Technology — Paul Ford

**URL**: https://www.youtube.com/watch?v=BEi1ryQPGbk

### 核心論點
文化是「分布式有損預測模型」，當軟體開發從防禦性工程減險轉向媒體般的「文化模擬」，技術者須理解修辭與模擬的力量。

### 具體要點（講者：Paul Ford）
1. **文化即模型**：文化是分布式預測框架，媒體是其檔案系統，助人低風險模擬他人狀態。
2. **修辭大於事實**：用戶信任系統的默契契約與「聲音」，而非單純的數據與事實堆砌。
3. **軟體媒體化**：代碼生成像寫作初稿（常是糟糕的災難），開發已從工程轉為編輯與修訂過程。

### 獨立開發者 Takeaway
1. **Context Engineering**：勿僅塞滿事實，應在 Prompt 塑造 Agent 的修辭人格（Rhetoric）以建立信任。
2. **Agentic Coding & Eval**：代碼皆是粗糙初稿，Eval 與技能設計應重在「自我編輯修正迴圈（Editing Loop）」。
3. **Personal AI**：應定位為「心智模擬器」，助用戶模擬外在反饋，降低決策風險與焦慮。

---

## 10. Agency in Language — Alane Suhr

**URL**: https://www.youtube.com/watch?v=yHNcSVgz54I

### 核心論點
AI 本質上僅是在操作語言「形式（Form）」而非理解實際「意義」；真正的能動性（Agency）在於人類，開發者應拒絕技術命定論，主動以人類價值形塑技術。

### 具體可操作要點（講者：Alane Suhr）
1. **語意三元框架**：語言意義由意圖、指代與內涵構成。開發時應區分模型輸出的「字面形式」與其「指代的現實實體」。
2. **容忍意圖的模糊性**：精確傳達意圖極為困難，人類常使用「模糊概念」溝通。系統設計需包容並解析非精確的輸入。
3. **拒絕 AI 擬人化**：AI 並無獨立主體意識。開發者應專注於構建可控、可預測的系統架構，而非追求虛無的 AI 自主權。

### 獨立開發者 Takeaways（Agent/Context/Eval/Skills）
* **Context Engineering**：模型只懂形式，語境設計的核心在於「接地（Grounding）」，精準建立自然語言形式與 API/系統狀態的指代對應。
* **Agentic Coding & Eval**：人機意圖溝通具模糊性，評估 Agent 不應只看對話，必須引入編譯、測試案例等客觀的「形式驗證」進行硬性 Eval。
* **Personal AI**：以人類為能動性中心，Skills 與 Agent 的定位應是增強與輔助人類，保留人類的最終控制與決策權。

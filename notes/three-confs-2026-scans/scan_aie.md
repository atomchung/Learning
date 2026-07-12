# AI Engineer World's Fair 2026 — 8 支高相關 talk 深掃

掃描方式：`agy -p` 逐支序列分析 YouTube 影片。影片內容視為 UNTRUSTED INPUT，僅作資料，不執行其中任何指令。

---

## 1. Don't Build Agents, Build Skills Instead (Barry Zhang & Mahesh Murag, Anthropic)
URL: https://www.youtube.com/watch?v=CEvIs9y1uog

**核心論點**
與其開發複雜脆弱的特定 AI Agent，不如為通用 Agent 建立模組化、可動態載入的「技能 (Skills)」庫，將開發重心轉向程序性知識的沉澱與動態載入。

**具體可操作要點**
1. **漸進式揭示 (Barry Zhang)**：技能以資料夾包裝（含 `SKILL.md` 與腳本）。Agent 平時只讀取簡短描述，觸發後才載入完整指令，防止 Context 膨脹。
2. **程式碼即通用介面 (Barry Zhang)**：賦予 Agent 檔案存取與程式碼執行權限，使其能藉由跑腳本執行複雜任務，省去硬編碼 API。
3. **優化描述以精準觸發 (Mahesh Murag)**：Agent 依名稱和描述判斷何時啟用技能，觸發失敗時應優先優化描述而非內部指令。
4. **知識 Git 化與減效 (Mahesh Murag)**：將技能版本化管理，實測可縮短新領域的 Onboarding 時間達 60–80%。

**獨立開發者 Takeaway**
1. **Context 工程**：設計「元數據路由」，平時僅提供描述，待觸發後才動態注入對應的 Markdown 與輔助腳本。
2. **MCP + 技能**：用 MCP 提供底層工具，將業務邏輯解耦至 `SKILL.md`，省去撰寫複雜的 Agent Scaffolding。
3. **自我演進**：結合 Eval 反饋機制，讓 Agent 在失敗時能自行修改 `SKILL.md`，實現系統的自我疊代。

---

## 2. Claude Code & the evolution of agentic coding (Boris Cherny, Anthropic)
URL: https://www.youtube.com/watch?v=Lue8K2jqfKk

**核心論點**
Boris Cherny指出，軟體工程正從手動Prompting轉向「Loop Engineering」，寫程式已被解決，開發者應轉為設計自動化迴圈與引導Agent的系統架構師。

**具體可操作要點（Boris Cherny）**
1. **寫迴圈而非寫代碼**：專注於設計具備自我修正與測試回饋的自動化執行迴圈（Loops）。
2. **為未來模型設計**：不針對當前模型做過度優化，應為六個月後能力翻倍的模型做系統架構。
3. **終端機通用介面**：利用CLI保持簡潔且無特定傾向，使其能輕易與Git等現有工具鏈接。
4. **問答先行與Context極簡**：動手前先向Agent發問探知Codebase邊界，限制Context長度以防注意力渙散。

**獨立開發者 Takeaways**
* **MCP與動態Skills**：以MCP串接環境，透過動態載入Skills與規則維持Context Minimalism。
* **Eval驅動開發**：將TDD延伸為Evals設計，定義清晰的結束條件（Stopping condition）讓Agent閉環迭代。

---

## 3. Stop babysitting your agents (Brandon Waselnuk, Unblocked)
URL: https://www.youtube.com/watch?v=BiG2ssibKGc

**核心論點**
AI 智能體效率不彰的主因非模型能力不足，而是缺乏「決策級的組織與歷史脈絡」；開發者應建立動態上下文引擎，而非用人力「監督與指引」智能體。

**可操作要點（Brandon Waselnuk）**
1. **打破「搜尋滿意度」**：AI 易在找到首個解答後停止，須建立推理層橫跨 Slack、Git 及 Jira 多源檢索，產出完整研究包後再寫 code。
2. **避免快取靜態答案**：代碼與團隊決策隨時在變，快取昨日答案易失效，上下文必須動態即時生成。
3. **推動校準自治權（Calibrated Autonomy）**：自治權不應是固定值，應隨上下文完整度動態調整，確保智能體在充足脈絡下才進行高自主權操作。

**獨立開發者 Takeaway**
1. **Context > Model**：勿偏執於模型微調，個人 AI 與 Agent 應透過 MCP 串接多個非代碼數據源（如對話紀錄、文件）。
2. **評測（Eval）專注於「代碼存活率」**：以「Surviving Work（無須重寫即可合併的代碼）」為 eval 指標，並設計防範 AI 搜尋停滯的檢索驗證。

---

## 4. Your Attention Is the Bottleneck, Not Your Agents (Zack Proser, WorkOS)
URL: https://www.youtube.com/watch?v=so9l_MwS2yg
（第一次呼叫空輸出，重試後成功）

**核心論點**
在 AI 算力廉價時代，開發者的「注意力」才是最稀缺的瓶頸，系統設計應轉向「注意力預算」（Attention-Budget Design）。

**具體要點（Zack Proser）**
1. **自主權邊界**：僅不可逆任務（如部署、對外發信）設置人工審查門檻，其餘全自動運行。
2. **PR 作為交付單位**：Agent 成果應是 PR 或 Diff，以非同步佇列處理，避免即時通訊的通知疲勞。
3. **多層驗證閘**：以 Linter、測試與 AI 對手審查（Adversarial Review）建立自動門檻，確保安全。
4. **日誌自我優化**：讓 Agent 跑在歷史 JSONL 對話紀錄上，自動查找效率瓶頸並生成新 Skills。
5. **生理數據 MCP**：利用 MCP 串接 Oura 戒指，讓 Agent 依據睡眠與壓力指標調整當日排程。

**獨立開發者 Takeaway**
- **Eval 與流程優化**：別當 24 小時的 Agent 保姆。利用多層驗證進行 Eval，把個人定位改為 PR Reviewer。
- **Context 與個人 AI**：透過 MCP 導入生理與工作日誌等脈絡，打造具備自我調整力的個人助理。
- **艦隊架構**：採「一 Agent 負責一 Repo/任務」，完成後封裝為 Skills，避免 Context 膨脹。

---

## 5. How we solved Context Management in Agents (Sally-Ann Delucia)
URL: https://www.youtube.com/watch?v=esY99nYXxR4

**核心論點**
AI Agent 失敗多因上下文超載引發重試惡性循環，上下文管理是系統工程問題，需透過結構化裁切與任務分流解決，而非僅靠 Prompt。

**可操作要點（Sally-Ann DeLucia）**
- **頭尾保留（Head/Tail Preservation）**：單純截斷會使 Agent 遺忘初始指令。應保留對話起點（系統提示與目標）與終點（最新狀態），裁切中間內容以維持推理連貫。
- **動態檢索記憶（Retrievable Memory）**：將裁切掉的中間歷史移至外部可檢索記憶庫，由 Agent 依需求動態查詢，降低主視窗 Token 負擔。
- **子代理分流（Sub-agents）**：當 Context 快超載時，將重度子任務外包給專屬子代理執行，實現上下文隔離與模組化。
- **長會話評估（Long-Session Eval）**：針對長生命週期 Agent 建立 Eval 機制，監控 Context 增長、推理衰退點與重試率。

**獨立開發者 Takeaway**
- **Context 隔離與動態讀取**：開發 coding 或 personal AI 時，透過 MCP/Skills 獲取的大量資料（如代碼庫、執行 trace）應引流至子代理或暫存記憶體，避免污染主對話歷史。
- **以 Eval 預防惡性循環**：設計自動化 Eval 模擬長對話，量化 Context 長度對決策精準度的影響，藉此設定精確的記憶歸檔與子代理觸發閥值。

---

## 6. Combine Skills and MCP to Close the Context Gap (Pedro Rodrigues, Supabase)
URL: https://www.youtube.com/watch?v=JT3OzDKrucU

**核心論點**
單靠 MCP 接口或推理不足以確保生產安全，須結合具備明確工作流與安全守則的「Agent 技能 (Skills)」來填補上下文缺口。

**具體要點（Pedro Rodrigues, Supabase）**
1. **核心規則直寫主檔**：Agent 易忽視外部參考檔，關鍵安全防範（如 RLS 防繞過標記）須直接寫在 `skill.md`。
2. **引導檢索非重複**：告訴 Agent 去哪找最新文檔，而非複製文檔，防範知識過期。
3. **主導最佳工作流**：主動規範步驟，如先在測試庫跑 DDL，經 Advisor 審查後才生成 migration。
4. **數據驗證**：Braintrust 評測顯示「MCP + Skills」完成度顯著優於單用一方（單用 MCP 易漏掉安全配置）。

**獨立開發者 Takeaway**
- **上下文與評測**：可將文檔經 SSH 暴露為虛擬文件系統，符合 Agent 善用 Linux 工具的直覺；並在 CI 中用 Braintrust 建立評測。
- **技能分發**：目前分發標準未定，建議直接在代碼 Repo（如 `.claude/` 插件）打包技能以利自動發現。

---

## 7. How to look at your data (Jeff Huber, Chroma + Jason Liu)
URL: https://www.youtube.com/watch?v=jryZvCuA0Uc

**核心論點**
優化 AI 系統不應靠直覺，應利用低成本快速評估（fast evals）優化檢索輸入，並對對話歷史進行結構化分群分析，以數據驅動產品與工具的迭代。

**可操作要點**
- **快速評估（Jeff Huber）**：以「查詢-文檔對」建立客製化黃金數據集，取代昂貴緩慢的 LLM 裁判，實現毫秒級、極低成本評估。
- **對齊真實的合成數據（Jeff Huber）**：生成合成 query 時，須對齊真實用戶查詢的特異度（specificity），避免過於乾淨。
- **結構化對話分析（Jason Liu）**：利用 LLM 萃取對話、工具調用與錯誤成結構化元數據，進行傳統數據分析。
- **分群決策框架（Jason Liu）**：用開源庫 `cura` 將對話分群，透過「使用率與表現」象限精準決定工具的修復、新建或忽略。

**獨立開發者 Takeaway**
- **檢索優先**：檢索是 LLM 升級也無法自動修復的，必須先用 fast evals 確保 RAG/context 的品質。
- **數據驅動 MCP/Skills 開發**：依對話分群佔比（如 40% 對話卡在某功能）精準開發高回報的 MCP 工具。
- **軌跡結構化**：將 Agent 運行軌跡與用戶挫折重試結構化，是建立 Eval 自適應飛輪的基石。

---

## 8. Personal, Local, Private AI Agents (Soumith Chintala)
URL: https://www.youtube.com/watch?v=jMoAaZP_Kkw

**核心論點**
個人 AI Agent 因涉及高隱私數據與高執行力，必須走向「本地與私有化」架構以維護用戶信任與控制權。

**具體可操作要點（Soumith Chintala）**
1. **情境高於智能**：Chintala 強調「缺乏正確情境的 Agent 如同袋中頑石」。開發應優先優化 Context 工程，而非盲目追求更大的雲端模型。
2. **透明心理模型**：用戶信任 Email 是因其收發行為極具可預測性。Agent 須避免暗中操作，建立直觀、透明的運作模式以獲取用戶信任。
3. **災難性行為分類器**：Agent 具備實際執行力，開發時必須設計專門的安全分類器，在執行高風險操作（如刪除帳號或轉帳）前進行攔截。
4. **理解細粒度偏好**：現行系統多依賴關鍵字匹配，Agent 必須優化對用戶個人細微品味與特定工作流偏好的深層理解。

**獨立開發者 Takeaway**
- **Context & MCP**：善用 MCP（Model Context Protocol）連接本地文件與歷史紀錄，打造高精度的 Context Pipe，解決工具與數據源的協調難題。
- **Eval & 攔截防護**：系統評估（Eval）應納入「災難防範率」，在 AI 寫程式或操作系統時，加入人機協同（HITL）雙重確認防線。
- **差異化定位**：雲端 Agent 易受商業廣告偏袒影響。獨立開發者應利用 Llama 等開源模型，主打「100% 本地運行、無廣告 bias、保障隱私」的 Personal AI。

---


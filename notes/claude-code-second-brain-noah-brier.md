# Noah Brier 怎麼把 Claude Code 當第二大腦

來源：AI & I podcast「Claude Code Can Be Your Second Brain」(2025-09 首播，2026-05 重播) + 他開源的實作 `heyitsnoah/claudesidian`。

學這題的原因：他的做法跟**我們這個 repo 是同一個物種**——Claude Code + markdown 檔案 + 開機讀設定檔當記憶。看他的版本能反照我們自己的設計。

## 一句話

把 Claude Code 架在 Obsidian vault 的根目錄上，**靠 CLAUDE.md 開機載入記憶、靠檔案而非 AI memory 存上下文**，從手機操作，當「思考夥伴」而不是「寫手」。

## 核心洞見（這才是重點，不是工具）

1. **讀比寫重要**：他原話——「大家太關注 AI 會寫，太少關注它會讀；日常上讀有用得多。」第二大腦的價值是 AI 能讀你幾千則筆記、做連結，不是幫你產字。

2. **上下文活在檔案裡，不在 AI 記憶裡**：vault 是持久記憶。每個 session 重新開機都能撈到全部歷史，不受 context 上限限制。檔案在你手上 = 完全掌控。

3. **思考模式 vs 寫作模式**，預設停在思考模式：
   - 思考模式：Claude 問澄清問題、搜既有筆記、做連結、維護 insight log——**不准急著產內容**。
   - 寫作模式：研究做夠了才切換，產草稿、編輯、出成品。
   - 他的理由：過早寫作浪費 token、錯過連結。

4. 一句口號：「AI amplifies thinking, not just writing.」

## 技術架構

- Claude Code 跑在**家裡地下室一台 server**，掛 VPN，從**手機**操作。
- 架在 Obsidian vault 根目錄，直接讀寫 markdown，**不走 API call**。
- 全程 Git 版控，每次改動都進 commit。

## 資料夾結構（用 PARA 法）

- `00_Inbox`：新點子的暫存捕捉
- `01_Projects`：有截止日的專案
- `02_Areas`：沒有結束日的長期責任
- `03_Resources`：參考資料 / 知識庫
- `04_Archive`：完成或停掉的東西
- `05_Attachments`：圖片 PDF 等媒體
- `06_Metadata`：設定、模板、文件
- `.agents/skills`、`.claude/skills`：agent / skill 定義（自動觸發）

## Skills（用自然語言觸發，不用打 slash command）

- `thinking-partner`：用提問探索點子
- `inbox-processor`：整理捕捉到的東西
- `research-assistant`：深入研究主題
- `daily-review`：每日結尾反思
- `weekly-synthesis`：跨週找模式
- `de-ai-ify`：去掉 AI 寫作腔
- `add-frontmatter`：補 YAML 屬性
- `pragmatic-review`：YAGNI/KISS 程式碼審查

說「我要開始一個新專案」「幫我收尾今天」就自動觸發對應 skill。

## 典型工作流（開新專案，例如準備演講）

1. 建一個專案資料夾，在裡面跟 Claude Code 工作。
2. 開場明講「我在思考模式不是寫作模式，先搜我的 vault 有沒有相關筆記，再用提問帶我探索」。
3. Claude 搜既有筆記、問澄清問題、把研究和別的 LLM 的對話轉錄都存成 markdown。
4. 維護 insight log + 每日進度更新——**幾天沒碰再回來，它能 catch you up**。
5. 研究夠了才切寫作模式產出。

## 跟我們這個 repo 的對照

**相同的骨架**（這驗證了我們方向沒走錯）：
- 都是 Claude Code + 扁平 markdown + Obsidian 純讀
- 都靠 `CLAUDE.md` 開機載入記憶
- 都是手機操作、Git 版控、上下文活在檔案裡
- 都刻意把 AI 當思考夥伴而非寫手（我們的「Create 是副產品」=他的「讀比寫重要」）

**他有、我們可以偷的**：
- **思考模式 / 寫作模式的明確切換**——我們有「禁止從零寫長文」，但沒把「思考模式」做成一個會擋住產出的明確 gate。他用 front matter 指令叫 Claude「現在還不准幫忙寫」。
- **PARA 的時間維度**：他用 Inbox/Projects/Areas/Archive 分「有沒有截止日」；我們是用主題分（notes/ vs topics/）。兩種切法，他的對「正在進行的事」友善，我們的對「累積的判斷」友善。
- **daily-review / weekly-synthesis 當固定 skill**：我們有 journey（每週五）概念但沒做成自動觸發的 skill。
- **catch-you-up**：幾天沒碰自動補進度。我們的 profile.md「開放疑問」有類似功能，但他是 per-project 的。

**我們有、他（看起來）沒有的**：
- **原子卡 + 判斷句標題 + 卡片連結網**（topics/ 層）。他的是 PARA 檔案，沒有「一句話判斷 = 一張卡」這種原子化重用層。我們這層是為了「跨脈絡重用的判斷」。
- **缺陷日誌 + meta-review 的遞迴自我改進**（Issue #6）。他沒有「把 harness 自己的失敗轉成規則修改」這層。
- **profile.md 這種跨主題的「使用者畫像」索引**——他的記憶比較綁在 per-project，我們多一層「我持續知道你關注什麼」。

## 深掘：他的 daily / weekly review 實際在幹嘛（2026-06-06 補）

從他開源的 skill 定義拆出來——兩個都不是「寫日記」，是**靠掃檔案修改時間自動盤點**，再產一份結構化筆記回存 vault。

**daily-review（每日收尾）**
1. 掃「今天所有被改/新建的筆記」→ 知道你今天碰了什麼
2. 評估：完成什麼、卡在哪、有什麼意外發現
3. 抓 insight：學到什麼、新連結、冒出什麼問題
4. 產每日筆記：成就、各專案進度、洞見、卡住項目+原因、新問題、**明天三個優先**、open loops 待辦框
5. 雜務：歸檔完成的 task、更新專案狀態、互連相關發現

**weekly-synthesis（每週綜合）——重點在這**
1. 讀「這週所有新建+修改的筆記」+ 有動靜的專案
2. **找模式**：反覆出現的主題、共同障礙、突破、哪些活動給/耗能量
3. 綜合：這週思考怎麼演化、意外的跨筆記連結、解掉和新冒的問題
4. 產八段筆記：本週快照、主題分析、重大洞見、各專案狀態、浮現的問題、能量評估、跨筆記連結、下週意圖

### 對我們的三個 learning

**1. 我們缺「週期性退一步、跨主題找模式」這一 pass。**
我們的睡前步驟是**增量**的——append 一條 inbox、profile 對應行往上浮，每次只看「這一條」。他的 weekly-synthesis 是**批次掃一整週、主動抽模式**：「你這週反覆繞回什麼？哪些問題其實是同一個？」我們從沒做過這種「讀完整週 inbox + 所有新 notes，告訴你浮現了什麼大主題」的動作。profile.md 是手動慢慢長的，不是定期重算的。

實例：最近 inbox 連續是 Robinhood agentic trading → 「策略是啥」→ Noah second brain，一個 weekly-synthesis 可能指出「你其實在反覆問同一件事：**AI 當代理人時價值在軌道/工具層還是判斷層**」——這種跨條目模式，增量更新看不出來。

**2. 兩種 review loop 的對照，幫我們把 Issue #6 想清楚。**
- 他的 daily/weekly review = **內容層**的 review（盤點知識、找主題模式）
- 我們的 meta-review（Issue #6）= **harness 層**的 review（盤點缺陷、改規則）

我們有後者缺前者，他有前者缺後者。**理想系統兩個都要**：一個讓知識複利，一個讓系統本身複利。

**3. 觸發機制互補：他掃檔案 mtime，我們讀對話訊號。**
他的好處：機械、不漏（碰過的檔案一定被盤點）。我們的好處：抓「用戶真正在乎什麼」（對話訊號）而非「哪個檔案被動過」。理想是 weekly 時兩個都掃。

**一句話 takeaway**：他證明「定期跨主題找模式」值得做成固定動作。我們現在只有增量捕捉 + harness 自我改進，**獨缺中間這層「內容層的週綜合」**——這是我們系統最該補的下一塊。

## 一句話結論

他證明了「Claude Code 當第二大腦」這條路是真的能跑、而且能單靠手機跑起來的。我們的 repo 走的是同一條路，差別在**我們多押了兩個賭注**：原子卡的重用層、和 harness 自我改進層。值得偷的是他的「思考模式當硬 gate」和「daily/weekly review 做成自動 skill」。

## 出處
- AI & I podcast：Claude Code Can Be Your Second Brain
- 開源實作：https://github.com/heyitsnoah/claudesidian
- Every 訪談：https://every.to/podcast/how-to-use-claude-code-as-a-thinking-partner

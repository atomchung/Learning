# Agensi AEO Deep Dive

> **TL;DR**：Agensi 是非技術獨立創辦人在 Amsterdam 用 Lovable + Claude 做的 AI agent skills marketplace，2 個月做到 12,400 MAU、$0 廣告。核心是 **SEO + AEO 雙引擎 + programmatic skill pages**。本文逆向工程他們的做法，並列出可借鑑的具體模板。

來源：
- 原 post：[r/buildinpublic「Built an AI agent marketplace to 12K+ active users in 2 months」](https://www.reddit.com/r/buildinpublic/)（已存於 `../signals/reddit-2026-05/deep_agensi.txt`）
- 官網實地抓取：[agensi.io](https://www.agensi.io/)、[agensi.io/skills](https://www.agensi.io/skills)、[agensi.io/skills/code-reviewer](https://www.agensi.io/skills/code-reviewer)
- 數據截至 2026-05-21

---

## 1. 達成數字（公開）

| 指標 | 數字 |
|---|---|
| 上線時間 | 2026 年 3 月中 |
| 28 天 MAU | 12,400+ |
| Google 月點擊 | 4,000+ |
| Google 月曝光 | 300,000+ |
| Page-1 排名數 | 850+（其中 150 個 Top 3） |
| 註冊用戶 | 700+ |
| Creator 數 | 52 |
| 上架 skill 數 | 250+（截至 5 月底官網顯示 477） |
| 付費 transaction | 39 + 4 個 MCP 訂閱 |
| 廣告花費 | $0 |
| 被引用的 LLM | ChatGPT, Gemini, Claude, Perplexity, 豆包 Doubao, Kagi |

特別注意：**最後一行**才是 AEO 真正的訊號。Doubao 出現代表中文 LLM 也在引用，這對中文圈 indie 是巨大線索。

---

## 2. AEO 雙引擎拆解

### 引擎 A：內容引擎（160+ 篇文章）

#### 選題公式
全部都是「**開發者實際會在 Google / ChatGPT 打的具體問題**」，不是抽象主題。原文舉例：
- "Where are Claude skills stored?"
- "How to install skills in Codex CLI?"
- "Best skills for API development?"
- "Cursor rules vs SKILL.md?"

**模板**：`{動詞} + {具體工具} + {具體名詞} + {?}`

不是「什麼是 Claude skill」這種抽象詞，而是「Claude skill 存在哪」這種你真的解決不了會卡住的問題。

#### 結構（從實地抓的 code-reviewer 頁逆向）
每個 skill 詳情頁、每篇文章都套同一個結構：

```
H1: {具體問題或工具名}
└─ H2: Description       ← 第一段 40-60 字直接答（AEO 黃金區）
└─ H2: What This Skill Does
└─ H2: How to Install    ← step-by-step
└─ H2: Example Usage     ← 可貼上跑的程式碼
└─ H2: Frequently Asked Questions
    ├─ H3: 具體問題 1
    ├─ H3: 具體問題 2
    ├─ H3: 具體問題 3
    ├─ H3: 具體問題 4
    └─ H3: 具體問題 5
```

整頁 400-500 字，**短而結構化**，不是長篇大論。這是 AEO 跟傳統 SEO 最大差異：LLM 喜歡能直接擷取的「answer block」。

#### 為什麼會被 LLM 引用
1. **第一段就是 40-60 字的完整答案**（不用看完整篇）
2. **FAQ H3 直接就是 query**（LLM 抓答案最容易的格式）
3. **可執行的 example**（LLM 抓 code snippet 比抓散文好處理）
4. **內部連結密集**（從一篇文連到 5-10 個 skill 詳情頁，建立 topical authority）

### 引擎 B：Programmatic SEO（477 個 skill = 477 個 landing page）

#### 機制
- 每上架一個 skill = 自動產一個 SEO landing page
- 每個 landing page 都套同樣 H1/H2/H3 結構
- **每多 1 個 creator = 多 N 個免費 SEO 頁面**（supply-side = marketing channel）
- Long-tail 命中：`{tool name} + {capability} + claude code skill`

#### 為什麼這比寫部落格好
| 維度 | 寫 blog | Programmatic SEO |
|---|---|---|
| 增量成本 | 一篇 = 一次手寫 | 一個 skill = 一個頁面，creator 幫你寫 |
| 上限 | 看 founder 多會寫 | 看市場上有多少 unit 可上架 |
| 維護 | 季度更新內容 | 改 template 全部頁面同步 |
| 同質性 | 風格不一容易差 | 一致結構利於 LLM 抓 |

---

## 3. 時間軸（複利曲線）

| 週次 | 動作 | 結果 |
|---|---|---|
| Week 0 | 上線，內容約 20 篇 | Google 每日曝光 ~15 次 |
| Week 1-3 | 持續寫文 + 發 Reddit | 曝光 300/day，差點想放棄 |
| Week 4 | 跨過 50-60 篇門檻 | Google 開始信任域名 |
| Week 5-8 | 加速產文 + 上架 | 曝光衝到 20,000/day |
| Week 8 | 12,400 MAU | 4,000 Google clicks/月 |

**關鍵 insight**：**前 3-4 週看起來像沒效**，差點要轉付費獲客。50-60 篇是 Google 信任的臨界量，過了之後是指數曲線。

---

## 4. Reddit 配合：spark not engine

- 全程發了 **10-15 篇**，不是天天 spam
- 發在 r/ClaudeAI, r/cursor, r/vibecoding 等高度相關 sub
- **內容是 useful content，不是「來我網站」**：skill 推薦、workflow tips、honest takes
- 自然 link，不硬塞
- 結果：28 天 340 個 first-time user 來自 Reddit
- **Reddit 是「點火」，SEO 是「持續燃燒」**

---

## 5. Stack（給非技術 founder 的範本）

| 環節 | 工具 |
|---|---|
| 建站 | Lovable + Claude |
| Hosting | Vercel free tier（推測） |
| 創作者上傳 | SKILL.md 檔（標準化規格） |
| 金流 | Stripe（推測，因為提到 transaction） |
| 分析 | GA4（明示有追 referral source） |
| AEO 監測 | 手動追 ChatGPT / Perplexity / Doubao 等引用 |

**重點**：non-technical solo founder + Lovable + Claude 就做出 477 個 skill listing 的網站。技術不是門檻。

---

## 6. 借鑑：套到 ting 你 stack 的 5 個具體應用

### 應用 1：把 `personal_os/` skills 上架 Agensi
- 你已經有 `record`, `session-board`, `record-claude`, `record-week`, `xhs-*` 一堆 skills
- 包裝成 SKILL.md，上架 Agensi
- **零成本**佔位中文 / 個人生產力類別（目前都是英文工程師類）
- 順便驗證 Agensi 平台流量真實性

### 應用 2：自己做「中文 Claude skills marketplace」
- 直接複製 Agensi 模型，做中文版
- 鎖定豆包 / Kimi / DeepSeek / 通義 引用（中文 LLM 競爭超少）
- 內容公式照搬：「Claude skill 怎麼安裝」「Cursor rules 和 SKILL.md 差別」中文版
- programmatic：每個中文 skill = 一個 SEO 頁
- 風險：中文工程師圈是否真的搜這些詞？需先驗證 search volume

### 應用 3：把 `rednote_analysis` / `rednote_mcp` 做成「小紅書創作者工具目錄」
- 仿 Agensi 結構：每個工具 / 模板 / 教學 = 一個 landing page
- 比賽道：xhs.dev、創客貼、新榜這類已存在，但中文圈 AEO 還沒人做
- 內容公式：「小紅書圖文怎麼選封面」「小紅書互動率怎麼算」具體問題

### 應用 4：股票 / 投資研究的 programmatic SEO 範本
- 你 `stock/` 已經有 OpenBB + 分析邏輯
- 每隻股票 = 一個 SEO landing page（H1=「{股票} 是否值得買 2026」、H2 結構固定）
- 已有人做（simplywall.st, finbox）但中文版 + LLM 引用優化很少
- 風險：投資內容法規敏感，要小心免責聲明

### 應用 5：把已驗證 idea 用 AEO 公式重寫文案
即便你不做新產品，現有 side project 都可以把 README / landing 改成 AEO 友善格式：
- H1 = 別人會搜的具體問題
- 第一段 40-60 字直接答
- H2/H3 用 FAQ 結構
- 加 example code block
- 確保 GPTBot, ClaudeBot, PerplexityBot 沒被 robots.txt 擋

---

## 7. 反思 / 風險

### Agensi 的弱點
1. **付費轉換弱**：12K MAU 只有 39 transaction + 4 MCP sub（推估 < $2K MRR），高流量低變現
2. **依賴 Anthropic / OpenAI 政策**：如果 Claude / Cursor 出官方 skill marketplace 直接被吃
3. **內容護城河淺**：160 篇文章 + 477 個 skill 一年內可被有資源的對手複製
4. **AEO 流量不穩定**：LLM 引用會因 ranking 演算法或內容更新失效（季度未更新 → 引用率掉 3x）

### 對 ting 的啟示
- 做這類 SEO/AEO 重型專案前要評估**「流量 → 收入」轉換率**，不要被 12K MAU 騙
- AEO 紅利期可能 6-18 個月，等大家都做了就一般化
- **最大教訓**：不要 build → 等用戶；要 build + 同時準備 100+ 篇答題型 content

---

## 8. 待 follow up

- [ ] 抓 5-10 篇 Agensi 實際文章，看每篇字數 / 結構 / 內部連結
- [ ] 用 Ahrefs / SEMrush 看 Agensi 實際 top 50 keyword 是哪些
- [ ] 看 Agensi 在 ChatGPT 被引用的實際 prompt 是哪些
- [ ] 估算「中文版 Claude skills marketplace」TAM：豆包活躍 + Cursor 中國用戶
- [ ] 看 Cursor / Claude Code 中文社群（即刻、V2EX、少數派）熱門問題，列出 30 個 AEO 文章選題

---

最後更新：2026-05-21

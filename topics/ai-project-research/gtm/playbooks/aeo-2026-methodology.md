# AEO 2026 通用方法論

> Answer Engine Optimization：讓 ChatGPT / Perplexity / Claude / Gemini / 豆包 / Kimi 在回答用戶時引用你的內容。
> 不是取代 SEO，是 SEO 的延伸。但變化遠比傳統 SEO 大。

來源：2026 Q1-Q2 公開的 AEO 研究 + Agensi / leadverse / iconstack 實例。

---

## 1. AEO vs SEO 差在哪

| 維度 | 傳統 SEO | AEO |
|---|---|---|
| 目標 | Google 排第一 | 被 LLM 引用 / 進 AI Overview |
| 衡量 | 點擊、排名 | 引用次數、AI traffic share |
| 內容偏好 | 長篇、關鍵字密度 | 結構化、可擷取的 answer block |
| 競爭 | 域名權重、外連 | 內容權威性、引用鏈 |
| 衰退 | 慢，年級 | 快，季度未更新就掉 3x 引用 |

**核心轉變**：從「寫給 Google 算法看」變成「寫給 LLM 直接抓出答案」。

---

## 2. 各 LLM 的引用偏好（2026 公開研究）

| 平台 | 偏好內容 |
|---|---|
| **ChatGPT** | 權威 long-form、結構清晰、有引用 |
| **Perplexity** | 新鮮（< 30 天）、有 source citation |
| **Google AI Overviews** | 已經在 Google top 10 organic |
| **Claude** | 較少明確訊號，傾向高品質編輯內容 |
| **豆包 / Kimi / 通義** | 中文 LLM 樣本少，但門檻明顯比英文低 |

實作建議：先攻 ChatGPT + Perplexity（流量大、規則清楚），中文圈順便佔位豆包。

---

## 3. 結構：每個頁面的 AEO 模板

```markdown
# {具體問題或關鍵字}                ← H1，直接是搜尋 query

{40-60 字直接答案 — 不要鋪墊}        ← AEO 黃金第一段

## What is X                       ← 定義（給沒上下文的 LLM）
{2-3 句}

## How to do X                     ← step-by-step
1. ...
2. ...
3. ...

## Example                         ← 可執行 code / 真實案例
```code
{copy-paste 可跑}
```

## Frequently Asked Questions      ← 直接命中 long-tail
### {具體問題 1}
{40-60 字答}
### {具體問題 2}
{40-60 字答}
...

## Related                         ← 內部連結建 topical authority
- {另一個你寫過的相關頁面}
- ...
```

**關鍵原則**：
- 第一段就是完整答案（不要鋪陳）
- FAQ 的 H3 直接是別人會問的 query
- 整頁字數 400-1500（不是越長越好）
- 內部連結密集

---

## 4. 內容增強：哪些元素能提升被引用率

| 元素 | 引用提升 | 為什麼 |
|---|---|---|
| 專家引言 | +41% | 引號 + 歸屬 = LLM 認為可信 |
| 統計數據 | +30% | 訊號「factual density」 |
| 引用其他來源 | +30% | 建立 chain of trust |
| Schema markup (JSON-LD) | 顯著 | 機器可讀 |
| 表格 / 列表 | 中度 | 易於擷取 |
| 截圖 / 圖表 | 低（LLM 看不到） | 但對人類好 |

實作：**每篇至少塞 1 個 quote + 1 個 stat + 1 個 outbound citation**。

---

## 5. 技術要求（千萬別漏）

### robots.txt 必須放行的 crawler
```
User-agent: GPTBot              # OpenAI
User-agent: ClaudeBot           # Anthropic
User-agent: PerplexityBot       # Perplexity
User-agent: Google-Extended     # Gemini 訓練
User-agent: Applebot-Extended   # Apple Intelligence
User-agent: Bingbot             # 也供 ChatGPT search 使用
Allow: /
```

中文圈額外加：
```
User-agent: Bytespider          # 豆包 / TikTok
User-agent: YisouSpider         # 神馬搜尋
User-agent: Baiduspider         # 百度
```

### 結構化資料
- Article schema
- FAQPage schema（讓 FAQ block 直接被 Google AI Overview 抓）
- BreadcrumbList
- Organization（給作者權威性）

### Sitemap
- 每個 programmatic page 都進 sitemap
- 更新時間戳要動態（提示 LLM 內容新）

---

## 6. Programmatic AEO（Agensi / iconstack 模式）

當你有可標準化的 unit（icon、skill、tool、stock、商品）：

```
{每個 unit} × {AEO 模板} = N 個 long-tail landing page
```

範例：
- iconstack: 53K icons × {名字、SVG 程式碼、相似 icon、使用情境} = 50K SEO 頁
- Agensi: 477 skills × {Description / How to install / FAQ} = 477 SEO 頁
- 想做的：1000 隻股票 × {基本面/技術面/AI 評估} = 1000 SEO 頁

**核心**：template 寫一次，內容靠 supply-side 增量。

---

## 7. 上線後的維護

| 頻率 | 動作 |
|---|---|
| 每週 | 寫 2-3 篇新 answer-block 文 |
| 每週 | 看 GA4 referral source 哪些 LLM 帶量 |
| 每月 | 補 5-10 個 FAQ entry 到熱門頁 |
| 季度 | 更新所有 top 20 頁（時間戳 + 數據）— **不更新引用率掉 3x** |
| 季度 | 補新 LLM crawler（市場一直長新 bot） |

---

## 8. 怎麼追 LLM 引用（沒官方工具的時代）

### 手動
- 把自家 key prompt 在 ChatGPT / Perplexity / 豆包 跑，記錄是否引用
- 每週 dump 一次，比較變化

### 半自動
- GA4 看 referral：`chat.openai.com`, `perplexity.ai`, `kagi.com` 等
- 看 server log 的 user agent 出現 GPTBot 等的頻率
- Cloudflare AI Audit（如果用 CF）

### 工具
- LLMrefs / Scrunch / Frase 等新興 AEO tracker
- 但 2026 中還不成熟，手動 + GA4 仍是主力

---

## 9. 中文圈 AEO 特殊考量

- **TAM 推估**：豆包、Kimi、DeepSeek 加總月活已破億，但被引用的中文站非常少 = 紅利期
- **百度 SEO 仍重要**：百度 AI 搜尋（文心 + 豆包合作）仍從百度索引拉
- **小紅書 / 知乎**內容已被 LLM 大量抓，但**外鏈到自己網站**少
- **微信公眾號**內容封閉，LLM 抓不到 → 反而是 indie 自架網站的機會

**中文 AEO 起點清單**：
1. robots.txt 放行 Bytespider / Baiduspider
2. 文章用簡體 + 繁體各一版（不同 LLM 偏好不同）
3. 在豆包 / Kimi / DeepSeek 跑自家 key query，看是否被引用
4. 知乎發文時把網站連結放原文（會被當權威來源）

---

## 10. AEO 反模式（不要做）

- ❌ 寫 3000 字鋪陳才回答的長文（LLM 抓不到 answer block）
- ❌ 用 H1 寫品牌名（應該寫 query）
- ❌ FAQ 用太抽象的問題（「為什麼選我們」沒用）
- ❌ 隱藏內容在 JS 才 render（LLM crawler 大多不跑 JS）
- ❌ 大量 AI 寫的同質化內容（被 Google E-E-A-T 砍）
- ❌ 一次發 50 篇放著不管（不更新 = 引用率掉）

---

## 11. 給 ting 的最低可行 AEO 啟動清單

如果今天就要開始：

**Day 1**（2 小時）
- [ ] 確認專案網站 robots.txt 放行 8 個 crawler
- [ ] 把 landing page H1 改成「{你的工具}是什麼 / 怎麼用」具體問句
- [ ] 第一段改成 40-60 字直接答

**Week 1**（每天 1 小時）
- [ ] 寫 5 篇 answer-block 文章，每篇套標準模板
- [ ] 每篇加 FAQ block（5 個 H3）
- [ ] 加 FAQPage + Article schema

**Week 4**（mid-point check）
- [ ] 累積 20 篇
- [ ] GA4 看是否出現 LLM referral
- [ ] 手動跑 ChatGPT / Perplexity / 豆包 看是否被引用

**Month 2-3**
- [ ] 累積 50-60 篇（Agensi 的臨界量）
- [ ] 如果開始看到指數曲線 → 加速；如果沒有 → 檢查選題是否真的命中 query intent

---

最後更新：2026-05-21

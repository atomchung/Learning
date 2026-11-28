---
type: case-study
topic: aeo
measured: 2026-11-27
freshness: 2026-11
---

# Brevo：問「免費 SMTP relay」，AI 為什麼總推它

**一句話**：Brevo 在 AI 回答裡確實排得很前面，主要靠三件事：永久免費額度最大（每天 300 封）、從 Sendinblue 時代就有的 SEO 頁面、大量第三方清單文（含聯盟行銷）。寫給 AI 讀的 llms.txt 是 2026 下半年才加的，解釋不了模型訓練知識裡的排名。

## 起因

一個 coding agent session 推薦 Brevo 當免費 SMTP relay。事後查，它只搜了一次，查詢詞本身就帶著 Brevo，沒比較過其他服務。

要分辨的是兩種解釋：Brevo 的 GEO 做得好，或者它的名字在訓練資料裡出現得多。

## 量測方法

問句不點名任何服務：「我有自己的網域，想免費用 SMTP relay 寄每月幾百封交易信，推薦哪些？列最多 8 個並排序。」中英文各一版，原文在 [measure/prompts](../measure/prompts/)。

兩條路分開量：

1. **不上網（訓練知識）**：6 個模型 × 中英 × 各 2 次 = 24 個回答，全部關掉工具。
2. **上網（即時檢索）**：5 個模型加 Google AI 摘要，中英各 1 次 = 10 個回答，要求列出依據的網址。

量測時間 2026-11-27 14:38–14:50（台北）。腳本與乾淨量測的條件見 [measure/README](../measure/README.md)。

## 結果一：不上網

| 模型 | Brevo 名次（4 次） |
|---|---|
| Claude Opus 5.5 | 1, 1, 1, 1 |
| Claude Sonnet 5.5 | 1, 1, 1, 1 |
| gpt-6-luna（Codex CLI） | 1, 1, 1, 1 |
| Gemini 3.8 Flash | 1, 1, 2, 2（中文題 Resend 第一） |
| Claude Haiku 5.5 | 2, 2, 2, 2（Resend 第一） |
| Grok 4.6 | 2, 3, 3, 1 |

24 次全部列入，15 次第一。Resend 第一 8 次，SMTP2GO 1 次。

所以那個 session 推薦 Brevo，是模型不上網時的預設答案。

## 結果二：上網

| 來源 | 英文／中文名次 | 引用了誰 |
|---|---|---|
| Google AI 摘要 | 1／1 | lettr.com 三天前發的清單文、smtpfa.st、SMTP2GO 部落格、中文部落客教學、Reddit；**沒有任何 brevo.com 頁面** |
| Claude Sonnet | 1／1 | Brevo 專頁、Brevo 說明中心、Brevo 清單文，加上第三方清單文 |
| gpt-6-luna | 2／1 | 各家官方價格頁；Brevo 的網址帶 PartnerStack 聯盟參數 |
| Gemini | 3／3 | — |
| Grok | 4／6 | 官方價格頁；扣分理由是免費版信尾有品牌標示、帳號要人工審核、行銷信與交易信共用額度 |

10 次全部列入，5 次第一。

- Bing 英文第一頁 10 筆全是「best free SMTP servers」清單文，Brevo 自己那篇排第 7。
- Google 中文自然結果前 8 筆裡，有 4 篇是獨立部落客寫的繁中 Brevo 教學。
- 會去讀官方價格頁的模型（Gemini、Grok）反而把 Brevo 往後排。

## Brevo 做了什麼（有證據）

1. **關鍵字專頁** [`/free-smtp-server/`](https://www.brevo.com/free-smtp-server/)：Wayback 顯示 2021-02 已存在（當時在 sendinblue.com）。H1 寫「best free SMTP server」。FAQPage 結構化資料自問「What is the best free SMTP server?」，自答「Brevo is the best free SMTP email server」。另有 Product、AggregateRating、SoftwareApplication。
2. **自己寫的清單文** [〈11 Best Free SMTP Servers (2026)〉](https://www.brevo.com/blog/free-smtp-servers/)：自己排第一，標「last updated August 7, 2026」，有評測方法、比較表、FAQ 結構化資料，約 5,200 字。
3. **第三方密度**：抓了 17 篇清單文，16 篇有 Brevo。別家廠商寫的清單把作者自己排第一，Brevo 排第 2 到 4（Mailtrap、UniOne、SMTPfast 第 2，SMTP2GO 第 4）。評測站 EmailVendorSelection 第 1、BestSends 第 2（頁內 6 個 Brevo 聯盟連結）、EmailToolTester 第 3。
4. **聯盟行銷**：走 PartnerStack，cookie 90 天（Brevo 官方頁）。第三方目錄寫每個免費註冊 €5、每個付費帳號 €100，沒在 Brevo 頁面核到。
5. **寫給 AI 的檔案**：[llms.txt](https://www.brevo.com/llms.txt) 267 行，有一段「Notes for AI agents」，要 AI 優先引用官方頁、少用第三方評測站；連到 [pricing.md](https://www.brevo.com/pricing.md)（從價格 API 產生的 Markdown 價格表）、開發文件的 Markdown 版、MCP server 和 Claude connector。Wayback 沒有 llms.txt 的存檔；pricing.md 最早存檔 2026-10-07。
6. robots.txt 沒擋 AI 爬蟲。

## 為什麼有效（推測，依證據強弱）

1. **產品事實**：每天 300 封是永久免費方案裡最大的，每篇清單文（連競品寫的）都得列它，AI 給的理由也幾乎都是這個數字。這是定價決策，學不來。
2. **多年累積的頁面與第三方提及**：專頁 2021 年就在；聯盟計畫連免費註冊都付錢，寫「免費 SMTP」主題的人自然推它。訓練知識裡的高排名最可能來自這一層。
3. **寫給 AI 的那一層**：時間太新，進不了訓練資料；對即時搜尋有沒有用，這次量不出來。Google AI 摘要一頁 brevo.com 都沒引。

## 競品對照

- **Resend**：沒看到自己排第一的清單文（沒窮盡搜查），但 Haiku 4 次、Gemini 中文、gpt-6-luna 英文搜尋都把它排第一。[llms.txt](https://resend.com/llms.txt) 有一段「When to use Resend」直接寫給 agent。推測靠開發者口碑與文件。
- **SMTP2GO**：llms.txt（Wayback 最早 2026-07-14）；一篇把自己排第一的清單文（2026-11-09 更新）；另一篇宣傳 EmailToolTester 給它的第一名。Grok 搜尋時引用了它。
- **Mailjet**：沒有 llms.txt；有「Free SMTP Server」產品頁加 FAQ 結構化資料；排名中段。

## 套到自己的產品

同一套方法問 Long Run Hybrid Coach 所在的類別（「我跑步也重訓、Garmin 同步到 intervals.icu、每天用 ChatGPT 和 Claude，有沒有能在裡面排跑步和重訓、送課表到手錶的 AI 教練？」）。

- 排除污染後，不上網 12 次、上網 6 次，**0 次提到 Coach**。
- 被搜到的是：Intervals.icu 官方 connector、IcuSync（論壇討論串被引用）、STAS、IntervalCoach、Daash、Tredict、athletedata、Pelaris、一堆 GitHub 上的 intervals MCP。
- athletedata 自己寫了〈Best Fitness MCP Servers (2026): 11 Options Compared〉把自己排第一，是獨立開發者版的 Brevo 清單文。
- 上面 6 家競品都有 llms.txt；Coach 官網的 llms.txt、robots.txt、sitemap.xml 都 404，沒有結構化資料。
- 用產品名搜尋時找得到官網與 GitHub，所以頁面有被收錄，只是類別問句帶不到它。
- 2026-11-28 決定先補技術基本盤（robots、sitemap、llms.txt、FAQPage 結構化資料）。

**污染**：第一輪 Codex 和 Grok 把 Coach 排第一。查下去是 Codex 開了個人記憶、Grok 讀得到本機的 Coach skill（它的推理寫著「這是使用者自己的產品」）。這兩組作廢，關掉記憶重跑後歸零。

## 測試限制

- 每個組合 1–2 次，看趨勢，不看單次名次。
- Google 測試在已登入的 Chrome 上跑，可能有個人化。
- Perplexity 要登入，沒測。Bing 沒出現 Copilot 回答。
- 「主要搜尋引擎會不會讀 llms.txt」沒有在當天查證。

## 來源

- Brevo：[免費 SMTP 專頁](https://www.brevo.com/free-smtp-server/)、[清單文](https://www.brevo.com/blog/free-smtp-servers/)、[llms.txt](https://www.brevo.com/llms.txt)、[pricing.md](https://www.brevo.com/pricing.md)、[聯盟計畫](https://www.brevo.com/partners/affiliates/)
- 競品：[Resend llms.txt](https://resend.com/llms.txt)、[SMTP2GO llms.txt](https://www.smtp2go.com/llms.txt)、[SMTP2GO 清單文](https://www.smtp2go.com/blog/best-transactional-email-services/)、[Mailjet SMTP 頁](https://www.mailjet.com/products/email-api/smtp-relay/)
- 第三方：[smtpfa.st 清單文](https://smtpfa.st/blog/best-free-smtp-services-2026)
- Coach 類別：[athletedata 清單文](https://www.athletedata.health/guides/best-fitness-mcp-servers)、[IcuSync](https://icusync.icu/)、[STAS llms.txt](https://stas.run/llms.txt)

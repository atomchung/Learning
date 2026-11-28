---
type: starting-point
topic: aeo
status: expanding
created: 2026-11-28
---

# 起點：AI 助理憑什麼推薦某個產品，做什麼能被推薦

> 磁鐵卡。AEO（Answer Engine Optimization：讓 AI 助理與 AI 搜尋在回答裡提到你）的案例與量測先放這裡，看出可重用的判斷再拆卡。GEO（Generative Engine Optimization）指同一件事，學界多用這個詞。
> 既有材料留在原處：[AEO 2026 通用方法論](../ai-project-research/gtm/playbooks/aeo-2026-methodology.md)、[Agensi 案例](../ai-project-research/gtm/case_studies/agensi-aeo-deep-dive.md)

## 當下的核心問題

- AI 推薦某個產品，靠的是什麼？自己的網站能改變多少？
- 訓練知識和即時搜尋兩條路，各自要做什麼？
- 沒預算、沒營收的小產品能做到哪裡？

## 案例

- [Brevo：問「免費 SMTP relay」，AI 為什麼總推它](./case_studies/brevo-free-smtp-2026-11.md)（2026-11）

## 已拆出的卡（0 張）

## 還沒拆但累積中的發現

- **AI 推薦有兩條路，要分開量**。不上網時看訓練知識：名字在多少網頁、跟什麼問題一起被提到。上網時看即時檢索：搜尋引擎排上來的頁面。兩條路結果不同：Brevo 不上網 24 次有 15 次第一，上網 10 次只有 5 次第一。
- **AEO 大部分就是 SEO，差在「別人的頁面」比「自己的頁面」重要**。Google AI 摘要把 Brevo 排第一，引用的頁面沒有一頁是 brevo.com，全是別人寫的清單文與教學。
- **訓練資料沒有提交入口**。能做的是長期出現在公開網頁上，以及 robots.txt 不擋 AI 爬蟲。
- **產品事實是底線**。會讀官方價格頁的模型（Gemini、Grok）因為品牌標示、帳號審核、額度共用，把 Brevo 往後排。SEO 內容蓋不過與事實不符的地方。
- **寫給 AI 的檔案（llms.txt、pricing.md）效果未證實**。Brevo 這層 2026 下半年才加，解釋不了訓練知識裡的排名；Google AI 摘要也沒引用它。成本低，同類產品都做了。
- **量自己的產品先排除污染**。個人記憶（Codex）、本機 skills（Grok）、全域指令檔（Claude）都會讓模型「知道」你的產品。自己帳號裡的 AI 推薦你，不能當證據。

## 下一步可能要拆的卡

- 「AI 推薦看的是別人排得上的頁面，不是你自己的頁面」：等第二個案例也成立再拆。
- 「量自己的 AI 能見度要先關掉記憶」：偏方法，可能留在 measure/README 就夠。

## 待驗證

- Coach 官網補了技術基本盤之後，類別問句會不會開始提到它。用 [measure](./measure/README.md) 同一組問句重跑。

## 量測工具

- [measure/](./measure/README.md)：問句、執行腳本、排名解析。換類別要改問句與廠商名單。

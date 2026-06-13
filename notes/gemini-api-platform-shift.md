# Gemini API 從「API」變「平台」— harness>model 的賣鏟人版

> 來源：LINE 台灣 DevRel 技術總監 Evan Lin 在 Google I/O Extended 2026 Taipei 的分享（見文末連結）。
> 主線：**Gemini 從「一個 model API」演進成「一個平台」，所以開發者該從「選哪個模型」轉向「設計系統架構」。** 一個賣 model 的廠，DevRel 卻在主場淡化 model——這是 harness>model 最有力的一筆第三方背書。

## 它把哪些 harness 元件「平台化」了

以前要自己造、現在平台一鍵給：

- **File Search** = 受管 RAG。不用自建 pipeline，自帶圖文同空間處理、metadata 過濾、精確引用 + 頁數追蹤。
- **Agents API** = server-side ReAct loop。任務在伺服器端跑長達 20 分鐘，開發者不用自己維護 state / timeout / retry。
- **Webhook** = 事件驅動取代 polling。長任務「先回收到、背景跑、完成主動回推」，省連線。
- **路由層心法**：便宜模型（Flash-Lite）先做意圖分類，必要時才升級貴模型，控成本/延遲/穩定性。

金句（作者結論）：「下一階段的競爭力，不在於誰比較會 call model，而在於誰比較會把 model、retrieval、agent 與 event flow 組成一個能真正工作的系統。」

## 三條 learning（按增量排序）

**1. harness>model 的「賣鏟人自己背書」版**
重點不是它說什麼，是**誰說的**。Google 賣鏟子，DevRel 卻在 I/O 主場說「鏟子不是重點，怎麼挖才是」。這讓 harness>model 跨過「Anthropic 生態自我宣傳」的質疑門檻——證據來自利益相反的一方，可信度更高。

**2. 平台商品化 harness 元件 → 價值上移到組裝層**
受管 RAG / server-side agent loop / context caching，以前是自造的工程護城河，現在被商品化。可遷移元判斷：**當一層被平台商品化，差異化就上移到它上面那層的判斷力**。跟「開源商品化計時器」「eval 生態位」「資安賣鏟人」是同一個模式。

**3. 反面——這是 lock-in 的糖衣（質疑）**
「把 80% 精力放回產品核心」的代價，是把 RAG / agent loop 外包給 Google，鎖進 Gemini 生態。受管服務省下的工程，可能在你要 debug 不可控黑箱（retrieval 品質、引用準確度、agent 行為）時加倍還回來。「受管」的真實成本是**失去控制權**。賣軌道≠免費——這跟 Robinhood 那條的張力同源。

## 跟既有判斷的咬合

- 直接再驗證 [harness-beats-model](../topics/coding-agents/cards/harness-beats-model.md)（已在該卡證據段補記一筆）。
- 「平台商品化 → 價值上移組裝層」這條，跟 [ai-security-ecosystem](./ai-security-ecosystem.md) 的「賣鏟人/價值流向」、[eval-ecosystem-niche](./eval-ecosystem-niche.md) 是同一個元模式——可能值得升級成一張跨脈絡卡。
- lock-in 質疑接 [robinhood-agentic-trading](./robinhood-agentic-trading.md)（賣軌道 → agent 預設走我家 → 鎖定）。
- 「便宜模型先分流」呼應 AI & I podcast 的「路由/編排是 agent 進生產的硬基建」（[ai-and-i-podcast-recent](./ai-and-i-podcast-recent.md)）。

## 來源

- [I/O Extended Taipei：用 Gemini API 家族打造應用（LY Corp 技術部落格，繁中）](https://techblog.lycorp.co.jp/zh-hant/io-extended-taipei-build-app-with-gemini-api-family)

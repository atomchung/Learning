# AI & I（Dan Shipper / Every）最近幾期 takeaway

> 來源：Every 的 AI & I podcast，2026-06-07 在 Snipd 上看到、搜整理。
> 主線：**agent 把能力變便宜，反而讓人類的判斷/審查更值錢**。三期從不同角度講同一件事。

## 1. The SaaS Apocalypse Is a Goldmine — Figma 的 Matt Colyer（本週最新）

- **「SaaSpocalypse」是假議題**：Colyer 自己做 agent 兩年，買的 SaaS 反而比以前多，不是更少。AI 對 SaaS 是金礦不是末日。
- **好設計是鑽石型流程**：先發散（狂生點子）再收斂（挑最好）。而 chat 是線性的——適合對一個設計反覆迭代，不擅長一次生很多選項。
- **on-canvas agent 要打破「文字框」**：他想讓專門 agent 各司其職——一組逼你發散、另一組過濾收斂。
- **review 成最大瓶頸**：AI 輔助產品工作裡真正卡住的是「審查」。
- **MCP 在閉合 code↔design 的環**：Figma MCP server 把設計和程式碼接起來。

## 2. Anthropic 的 Angela Jiang + Katelyn Lesse — Claude Managed Agents（約 6/1）

- **Anthropic 接手「殺死大多數 agent 產品」的基礎設施**，目標撐住 24/7 長跑的 agent。
- **三個關鍵組件**：multi-agent 編排、dreaming（Anthropic 版 compound engineering）、outcomes（你指定結果，agent loop 到達成）。
- **全域記憶體（hosted memory store）**：不必把所有專業塞進 system prompt，每次請求只撈相關的 → 更快。
- **數字訊號**：平台 API 用量年增 17 倍。

## 3. After Automation /「自動化全部、headcount 卻翻倍」— Brandon Gell 訪 Dan（角色對調，約 5 月底）

- **核心悖論**：AI 把昨天的專家能力變便宜且普及 → 每個領域被「接近但不完全對」的產出淹沒 → 反而更需要能收尾的人。
- **Every 自家數據**：狂用 agent 同時，人從 15 → 30。每個自動系統都需要一個人類管家，注意力一撤，agent 價值就崩。
- **判斷力是差距**：GPT-5.5 重寫爛 codebase 拿 62 分，資深工程師 85–90。差在——模型被叫修 bug 就乖乖修，資深的人會回頭質疑「這題本身對不對」。
- **人是 AI 工作的兩片麵包**：前端規劃、後端 review 與調校，中間夾 agent。
- **投資/商業含意**：把「砍人頭」當賣點的商業模式可能在過度承諾；圍繞「人類判斷監督自動化」設計的公司更耐久。

## 跨期共同訊號（值得留意）

1. **瓶頸從「生產」移到「審查/判斷」**——Figma 說 review 是瓶頸、Dan 說判斷力是人機差距，同一件事。
2. **agent 進生產的硬基建 = 記憶 + 編排 + outcome loop**（Anthropic 那期最具體）。
3. **「AI 取代人」敘事被前線反證**——越自動化越需要人來導航。

## 跟既有判斷的咬合

- 完全呼應 `topics/coding-agents/cards/harness-beats-model.md`（harness>model）與「人機協作」「記憶架構」線。
- 「review 是瓶頸 / 判斷力是護城河」可能值得升級成卡片——它在 coding-agents、AI power user、產業判斷三條線都用得上（跨脈絡重用訊號）。

## 來源

- [Figma Exec on Why the SaaSpocalypse Is a Goldmine](https://every.to/podcast/figma-exec-on-why-the-saaspocalypse-is-a-goldmine)
- [Inside Anthropic's 2026 Developer Conference / Claude Managed Agents](https://every.to/chain-of-thought/inside-anthropic-s-2026-developer-conference)
- [We Automated Everything With AI and Tripled Our Headcount（transcript）](https://every.to/podcast/transcript-we-automated-everything-with-ai-and-tripled-our-headcount)
- [After Automation（essay）](https://every.to/p/after-automation)

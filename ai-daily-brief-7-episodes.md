# The AI Daily Brief — 過去七集摘要

> 主持人：Nathaniel Whittemore (NLW)
> 整理日期：2026-04-27
> 節目結構：每天一集，主節目 20–30 分鐘，穿插 Operators Bonus（與 enterprise/實作專家對談）與廠商贊助專題

---

## 1. Where the Economy Thrives After AI（4/27 今天，約 30 分鐘）

本集 NLW 引用芝加哥大學經濟學家 Alex Imas 的論點，提出一個跟主流「AI 會大規模取代工作」截然不同的視角：AI 不會抹消勞動，而是把經濟的「價值重心」推向那些需要人的在場、來歷、品味、關懷與關係的領域。

他以 1900 年美國 40% 人口務農、現今不到 2% 為類比──當某個產業被科技商品化（commoditised）後，人們不會停止消費，而是把錢與時間挪到新領域。Imas 因此推導出未來最「耐打」的工作會落在所謂 **關係型部門（relational sector）**：護理、心理治療、教師、私廚、訂製裁縫、精釀、現場表演、宗教/靈性引導、托育、各種款待業等。

NLW 也補上一個常被忽略的問題：在供給變得超便宜之後，會解鎖什麼新需求？這集本質上是一個經濟學框架的科普，把 AI 對就業的爭論從「誰會被取代」拉到「價值會流向哪裡」這個更根本的提問。

---

## 2. How To Build a Personal Agentic Operating System（Operators Bonus，約 4/25）

這集是 NLW 與 Nufar Gaspar 的合作專題，正式介紹 AIDB 全新免費課程「Agent OS」。核心命題是：當所有 agent 工具（Claude Code、Codex、Cursor 等）功能逐漸趨同，真正讓你產生差異化的，是你「鋪在工具底下的那套個人系統」──它能跨工具、跨模型、跨 harness 跟著你走。

Nufar 以「個人幕僚長（chief of staff）」為貫穿範例，把這套系統拆成七層：
- **Identity**（代理權限與人格）
- **Context**（情境/世界觀）
- **Skills**（技能）
- **Memory**（過往互動的記憶）
- **Connections**（與其他 agent 與工具的串接）
- **Verification**（驗證/守門）
- **Automations**（自動觸發）

重點是「不要把記憶與流程綁死在某個廠商的 UI 裡」，而是抽象成可攜帶的描述文件與 skills。本集是這套課程的入門導讀，適合已經在用 agent、但發現自己在每個工具裡都重蓋一次同樣輪子的人。報名網址在 aidbagentos.ai。

---

## 3. What I Learned Testing GPT-5.5（約 4/24）

OpenAI 在 4/23 推出 GPT-5.5（內部代號 Spud），4/24 開放 API。本集 NLW 分享自己的實測心得，並彙整社群第一波反應──主要分成四股聲音：

1. **跑分派**：GPT-5.5 在 Terminal-Bench 2.0 拿下 82.7%，MRCR v2 1M token 從 GPT-5.4 的 36.6% 大跳到 74.0%，長上下文推理是真實的飛躍
2. **Coding 派**：持續爭辯它跟 Claude 的相對強弱，Anthropic 對比是無法迴避的話題
3. **價格派**：API 價錢直接翻倍（$2.50/$15 → $5/$30 per million token），OpenAI 解釋因 token 使用更精省，實際漲幅約 20%
4. **體感派**：質疑「對非工程師日常使用者來說，這次升級感覺得到嗎？」

NLW 自己的結論：GPT-5.5 真正的賣點不是某個 benchmark，而是它能「自己撐完一段長任務」──理解、規劃、操作、收尾，無需人類頻繁救援，這跟之前的版本是質變而非量變。

---

## 4. The Move to Headless Software（約 4/22-24）

本週四家巨頭幾乎同時把賭注押在「無頭軟體（headless software）」這個新範式：

- **Salesforce** 推出 Headless 360，把整個 CRM 平台所有功能全部以 API、MCP tool、CLI command 形式對外暴露，agent 無需開瀏覽器就能操作整套系統，並原生對接 OpenAI、Anthropic、Gemini、LLaMA、Mistral
- **OpenAI、Microsoft、Google** 也各自釋出讓平台「以 agent 為主要使用者」的更新

NLW 在本集解析這個轉折的三個含義：

1. **SaaS 的 UI 不再是價值錨點**，介面被吃掉之後，誰擁有「動詞」（API/權限/工作流）才是新護城河
2. **既有的 per-seat 訂閱制定價會崩**，下一代會走向 outcome-based 或 per-action 計費
3. **真正的價值捕獲會發生在「協調 agent」這層**，而不是被協調的工具本身

對於 SaaS 創辦人與企業 IT，這集是少見把「agent-first 軟體」說成可執行策略的整理。

---

## 5. GPT Image 2 與圖像推理的邊界（約 4/22）

OpenAI 推出的 GPT Image 2 一上線就在 LM Arena 圖像榜上以 242 分領先第二名，創下單一模型紀錄差距。本集 NLW 用這個事件帶出兩個更實用的話題：

- **Image-to-code 工作流真正成熟**──設計稿、線框圖、白板照片可以直接輸入，模型輸出可運行的前端程式碼，這對小型團隊與 indie hacker 是巨大的生產力槓桿
- **「圖像推理」仍然是短板**──模型可以漂亮地生圖、辨識圖，但對「圖中物件之間的空間關係、因果關係、動作序列」的推理仍會出錯，特別是工程圖、流程圖、多步驟視覺謎題

NLW 因此提醒聽眾不要被排行榜誤導：高分代表生成品質，但「看圖思考」仍是未解問題。本集適合做產品的人，因為它劃出了「現在就能用」與「再等半年」之間那條線。

---

## 6. Apple 的 AI 策略與 John Ternus 接班（約 4/21）

Apple 宣布 Tim Cook 將交棒給硬體主管 John Ternus，本集 NLW 重新審視一個有點違反直覺的命題：Apple 在這輪 AI 軍備競賽裡「漂亮地按兵不動」是不是其實算對了賬？

論點有三：

1. 其他巨頭一年燒掉數百億美元在資料中心，Apple 反而靠著 on-device 與雲端混合策略守住毛利
2. Apple Intelligence 雖然推出後評價兩極，但 iPhone 出貨量並沒有崩，代表消費者對「AI 功能」的付費意願其實被高估
3. Ternus 是硬體出身，象徵 Apple 接下來會把 AI 賭注押在「裝置 + 感測器 + 私有運算」的整合，而不是追逐 frontier model

NLW 也提出反方意見：如果 agent 經濟真的成型，Apple 沒有自家 frontier 模型會在「誰擁有使用者意圖入口」這場戰爭裡被動。這集的價值在於把 Apple 從「AI 落後者」的單一敘事中拉出來，給出一個更立體的策略地圖。

---

## 7. How to Use Opus 4.7 and the New Codex（4/17）

這集處理 24 小時內接連發生的兩個發布：Anthropic 推出 Claude Opus 4.7，OpenAI 同日重押 Codex 應用。NLW 強調兩者並非直接對打，對知識工作者的影響也不同：

- **Opus 4.7** 強在長上下文連貫性與推理，適合深度寫作、研究、架構規劃
- **新版 Codex** 改善了 context compaction（上下文壓縮），這帶出本集最重要的概念──「**monothread 模式**」

傳統用法是「每個任務開新對話」，因為怕脈絡污染；但壓縮做得好之後，反而應該對「重複出現的工作流」（例如每週財報、固定客戶溝通、長期專案）保留同一條 thread，讓脈絡隨時間「複利累積」。

NLW 認為大部分人現在把該 monothread 的東西當成 one-off，正是把最大的槓桿留在桌上。本集實質上是一份新工具的「使用心法」，比起發布會式的功能清單，更聚焦於工作流改造。

---

## 整體基礎架構觀察

連續聽 7 集會看到 NLW 的內容主軸是貫通的：

```
Headless 軟體 → Agent-first 工作流 → 個人 Agent OS → AI 改變經濟結構
```

NLW 的風格不追逐速報，而是把當週新聞「合成」成一個策略框架。這也是這個 podcast 跟其他 AI 新聞節目的差異點──它的價值在 synthesis（綜合），不在 breaking news。

## 來源

- [The AI Daily Brief on Apple Podcasts](https://podcasts.apple.com/us/podcast/the-ai-daily-brief-artificial-intelligence-news/id1680633614)
- [AI Daily Brief on Spotify](https://open.spotify.com/show/7gKwwMLFLc6RmjmRpbMtEO)
- [Codex + Opus 4.7 episode companion](https://play.aidailybrief.ai/episodes/how-to-use-opus-4-7-and-the-new-codex-app/)
- [Salesforce Headless 360 (VentureBeat)](https://venturebeat.com/technology/salesforce-launches-headless-360-to-turn-its-entire-platform-into-infrastructure-for-ai-agents)
- [OpenAI introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [Alex Imas on Fortune](https://fortune.com/2026/04/19/alex-imas-human-jobs-ai-economy-chicago-economist-substack-doomsday-scenario/)

# Codex 取代 ChatGPT？OpenAI 的 agentic 遷移論文

> 論文：*The Shift to Agentic AI: Evidence from Codex*（arXiv 2606.26959，OpenAI，2026-06-25）
> 配套部落格〈How agents are transforming work〉。作者 Drew Johnston（OpenAI）、David Holtz（UC Berkeley/OpenAI）等 6 人。

## 它在講什麼（先把標題糾正）

不是「Codex 產品取代 ChatGPT 產品」，而是**在 OpenAI 內部，工作模式從「跟 chatbot 對話」轉向「派 agent 跑多步任務」**。Codex 是這個遷移的證據。

數據（全是 OpenAI 自報，三組樣本：外部個人帳號 / 企業帳號 / 自家員工）：

- 平均工程師 output token **99%** 走 Codex；全公司每週 output token **99.8%** 走 Codex
- 員工 Codex 採用率 **約 98%**（2025/08 才 ~40%）
- 非開發者個人用戶自 2025/08 成長 **137 倍**、組織用戶 **189 倍**
- 「需資深人類 8 小時以上」的任務比例今年成長 **近 10 倍**
- 2026/06 vs 2025/11：法務中位數員工月 output token **13 倍**、研究員 **逾 50 倍**
- 組織面：2026-05-16 把 ChatGPT 團隊併進 Codex 團隊（「一個平台、一個訂閱、一個 surface」）

## 對我的 learning：這是「判讀型」輸入，不是「借鑒型」

關鍵自覺——我的攝取有兩種輸入，這篇只占一種：

- **借鑒型**：給可搬的機制 → 改我怎麼工作 / 改 harness（例：Hermes「連坑一起記」變成 CLAUDE.md 規則）
- **判讀型**：給信號 → 更新 belief / 預測帳，回報在投資與卡位判斷（例：這篇）

這篇**純判讀型**。它不交給我任何能立刻改進系統的技術，價值是**結算既有開放預測**，別為它造假動作（待辦 +0）。這恰好實踐 `info-intake-routine`：過了「信號」篩子（值得記），但歸宿是 belief 更新不是流程改造。

（唯一很薄的可搬點：OpenAI 的測量法＝「按角色追蹤 token 流向隨時間變化」，理論上可套來量自己的 power-user 遷移。太細，不開待辦。）

## 接到哪幾張既有卡

- **`async-vs-sync-agent-paradigm` + `harness-is-the-new-battlefield`**：chat→agent 大遷移的**第一方實證**。99.8% token 走 Codex + 併團隊＝賭注壓在 agentic surface。
- **`loop-engineering`**：「8h+ 任務 10 倍」＝ agent 在跑更長的自主 loop，就是第五層在吃工作的真實痕跡。
- **`read-signals-not-surface-numbers` + 「估計值 vs 實測值」**：拿我自己的卡反打它——
  - 信號（可信）：互動模式 chat→agent、擴散到非工程職能，行為遷移難造假。
  - 表面數字（打折）：50x/137x/189x 全自報、有財務誘因；output token 是使用量 proxy 不是生產力（agent 本來就比 chat 吐更多 token）；倍數分母是 2025/08 極低基數。

## 一個張力（對我真正有料的部分）

OpenAI 併成「一個 surface」到底是：
- **(A) harness 是主戰場**的鐵證（價值往 agentic harness 集中），還是
- **(B) `orchestration-as-a-model-vs-neutral-harness`** 反論的延伸——模型廠把 harness 鎖進自家封閉 surface，吃掉「中立可換」？

初判：**對 OpenAI 是 A，對「我能不能自由換 harness」是 B**。跟 Sakana Fugu「把 orchestration 內化成模型賣」、Cursor 被 xAI 收編同方向——都在收割 harness 層。這是 `loop-eng 會被 harness 吃掉還是長外圍治理層？`（profile 開放疑問）的**新數據點：六積木被原生吃掉的趨勢又 +1 例**。

## 出處
- [arXiv: The Shift to Agentic AI: Evidence from Codex](https://arxiv.org/abs/2606.26959)
- [OpenAI: How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/)
- [TheNextWeb（self-reported caveat）](https://thenextweb.com/news/openai-codex-agents-shift-employees-non-developers)
- [TechTimes（137-fold non-dev）](https://www.techtimes.com/articles/319114/20260626/agentic-ai-reaches-lawyers-recruiters-openai-data-shows-137-fold-non-dev-growth.htm)

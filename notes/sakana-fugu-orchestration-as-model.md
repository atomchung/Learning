# Sakana Fugu：把多 agent 協作做成「一個模型」

> 來源：Fox Hsiao Threads 貼文（2026-06-22）+ web 查證（Dealroom、the-decoder、StartupHub、官方 sakana.ai/fugu-release）。
> 事件日：2026-06-22（東京 Sakana AI 發表）。

## 一句話

有人賭「**把 multi-agent orchestration 做成單一模型 + API，賣給買不到美系前沿模型的人**」——同時測試我兩個既有判斷：harness 中立性、地緣替代品生態位。

## 它是什麼（事實層）

- **產品**：Sakana Fugu。對外只開一個 OpenAI 相容 API，你像呼叫單一模型那樣呼叫它。
- **背後**：一個被訓練來「指揮其他模型」的 LLM——自己選模型、分派任務、驗證、彙整。能調度一池不同 LLM，甚至呼叫自己的副本。
- **關鍵細節（貼文沒強調）**：那個 conductor（指揮模型）**只有 7B 參數**。重點不是又訓了個大模型，而是「**用小腦袋路由一池大模型**」。一家頭條直接寫 *without training a single frontier model*。
- **技術來源**：兩篇 ICLR 2026 論文。
  - **TRINITY**：輕量「演化出來的」協調器，把 Thinker／Executor(Worker)／Verifier 三角色多輪動態分派給不同模型。
  - **Conductor**：用 RL 讓系統自己學出「用自然語言協作」的策略，而非手刻 workflow。
- **兩版本**：Fugu（效能＋低延遲，日常寫程式/聊天）；Fugu Ultra（最高準確度，Kaggle／論文重現／資安／專利硬任務）。
- **計費**：只算當下啟用的最高階模型，不疊加。Ultra＝輸入 $5／輸出 $30 每百萬詞元。
- **跑分（官方自報）**：SWE Bench Pro 73.7（> Opus 4.8 的 69.2）、LiveCodeBench Pro 90.8（> GPT-5.5 的 88.4）、GPQA-D 95.5（略勝 Gemini 3.1 Pro 94.3）。官方說達 Fable 5／Mythos Preview 水準。
- **公司**：2023 東京成立。Llion Jones（Transformer 論文〈Attention Is All You Need〉共同作者）、David Ha 等。

## 用我的鏡頭看（訊號層）

**1. 跑分全是自報，第一道篩子拉到最緊。**
查證沒看到任何第三方獨立驗證。SWE Bench +4.5、GPQA +1.2 這種自家發的小幅領先，當「估計值」看，不當事實。真正該記的不是分數，是架構選擇。

**2. 這正面戳到我的「harness > model」判斷。**
我的核心卡：協作邏輯住在 harness（中立、可換層）。Sakana 賭的是反向——**把 harness 內化成一個 meta-model 賣給你**。
這不一定推翻原判斷，但是值得對沖的反論：如果 orchestration 能被訓練進一個模型、只開一個 API，那「harness 是中立可換層」的價值會被吸進模型/產品廠。
↔ 對比 `cursor-spacex-xai-composer3.md`：那邊中立 harness 被「收購」吃掉，這邊被「模型化」吃掉——同一個方向的兩種吃法。

**3.「不受出口管制」才是商業核心。**
那句是寫給「因地緣政治買不到美系前沿模型的客戶」。卡的是**非美前沿替代品**生態位，跟 Andrew Ng〈控制存取只會加速對手建開放替代品〉同劇本，日本版（`ng-open-platforms-beat-power-plays.md`）。
有趣的反諷：它的「前沿能力」本身可能還是路由到美系模型（Claude/GPT/Gemini）——所以「不受出口管制」要看它路由的池子裡有沒有美系模型，以及在受限地區那池子還在不在。**這點存疑，是它行銷話術可能的破口。**

## 可重用的判斷（distillation 候選）

**orchestration-as-a-model：把 harness 內化進模型權重，是對「harness 中立可換」的反論。**

- 為什麼可重用：在 coding-agents（harness 層歸屬）和 agent-collab-infra（協作單位）兩條線都用得上。
- 真正的測試點：協作邏輯的價值最終住在哪——
  - 住 harness（中立、用戶可換模型）＝我原本的賭注；
  - 還是被吸進「賣 orchestration 的產品/模型廠」＝ Sakana 的賭注。
- 觀察指標（之後回看）：用 Fugu 的人，是因為「省了自己搭 harness 的工」，還是因為「真的比自搭 + 直連前沿模型更強更便宜」？前者＝便利財（harness 仍可被自建取代），後者＝才真的證明 orchestration 該被模型化。

## 開放疑問

- **「不受出口管制」是真護城河還是話術？**（check:2026-09）它路由的池子裡若含美系模型，受限地區還用得到嗎？7B conductor 自己夠不夠扛前沿任務？
- **orchestration 該住 harness 還是該被模型化？**（check:2026-12）這是 harness-beats-model 的對沖線。看 Fugu 留存與定價能不能撐過「自己搭一套也不難」的替代壓力。

## 出處

- Fox Hsiao Threads 貼文（2026-06-22）
- 官方：sakana.ai/fugu-release、sakana.ai/fugu-beta
- 報導：Dealroom、the-decoder、StartupHub、Startup Fortune（"without training a single frontier model"）

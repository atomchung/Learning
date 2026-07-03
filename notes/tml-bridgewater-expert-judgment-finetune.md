# TML × 橋水：把專家判斷煉成模型權重的配方

日期：2026-07-03。來源：Thinking Machines Lab blog《Learning to Replicate Expert Judgment in Financial Tasks》（與橋水 AIA Labs 合著）。原文被 proxy 擋（403），細節從 FourWeekMBA / CoinDesk / 搜尋摘要交叉拼出，引用前值得再試讀原文。

## 一句話

橋水拿幾十年專家標註的金融判斷資料，在 Tinker 上微調 Qwen3-235B，六項 document-triage 任務平均 84.7%（前沿模型精修 prompt 最好 78.2%、原始 prompt 約五成），推理成本 1/13.8。

## 事實層（自報值，非第三方）

- 任務：文章相關性評分、央行文件判讀、內容標註、文件/郵件截斷——全是分類/判讀型苦工，微調的主場。
- 對照組結構性不公平：前沿模型閉權重、外人微調不了，比較永遠是「別人家微調 vs 我家只能 prompt」。這是閉權重的商業選擇造成的必然，不是科學新發現。
- 「小模型」說法不準：Qwen3-235B 是 MoE 大模型，只是推理比前沿 API 便宜。

## 方法論配方（含 ablation 自報值）

起點：SFT（專家標註）+ GRPO（critic-free RL）＝一大段提升但卡在 80% 以下。然後三招：

1. **Interleaved batching（+12.1%，最大單項）**：多任務訓練比較三種排批——逐任務先後、批內全混、每任務一批輪流（round-robin）。輪流最好，比全混高 12.1%。反直覺：大家預設混著訓，結果輪著訓贏很多。
2. **CISPO loss + 不對稱裁剪（+10.1%）**：CISPO 出自 MiniMax-M1，非新發明；驗證了在專家判斷任務上比標準 importance-sampling 好 10.1%。
3. **On-policy distillation + 動態晉升 teacher（+3.1%）**：on-policy distillation 是 TML 自家先前方法；新 twist 是表現最好的 checkpoint 動態升格當 teacher。每 episode 訊號位元多→小 batch 可訓、梯度噪音低。

**保留**：全是單一資料集上的自報 ablation，跨領域遷移未驗證。

## 方法論真亮點：專家時間只花在邊界案例

原文的核心洞見（貼文沒提）：**如果模型無法重現訓練集裡的某個標註，要嘛案例真的難、要嘛原標註是錯的——兩種情況都恰好是稀缺專家時間該花的地方。**

所以專家只標四種：邊界案例、專家間有分歧的、高影響的漏判、模型不確定或原標註可疑的。這是 active learning 的復活，但給了一個乾淨的操作原則：

> 專家不標全量，只在模型的失敗邊界上花時間。模型的失敗點本身就是「哪裡需要專家」的偵測器。

## 產業信號（三個，接既有線）

1. **稀缺資產＝專家標註的判斷資料，不是模型**。橋水幾十年人工標註才是買不到的東西。同構 harness>model：價值在模型外圍，模型本身商品化。
2. **中國開放權重成華爾街預設地基**（Qwen3-235B）。不是排行榜分數，是全球最大避險基金的生產選型——「中國開源當地緣訊號」實錘 +1。
3. **TML 生態位＝管道不是模型**：賣「把專有判斷煉成權重」的軌道。接 `llm-call-niches` 卡：可投資表達式在外圍。

呼應 eval 線：前沿模型在專家判斷任務精修 prompt 只到 78%，跟《Learning to Judge》（專業域 judge 對齊人類崩到 <0.3）是同一件事兩面——專業判斷不在通用模型分佈裡，得用資料灌進去。

## 對我們 repo 的同構（餵 Issue #6）

「專家只標邊界案例」＝**「owner 只審不寫」的精化版**：

- 部門大腦線：owner 只審不寫 → 再進一步＝owner 只審「AI 不確定/與既有判斷矛盾」的邊界案例。
- 本 repo：用戶注意力＝稀缺專家時間；Claude 把「我確定的」直接落地/FYI，把「我不確定的、內部有分歧的、與 profile 既有判斷矛盾的」才呈給用戶裁。AskUserQuestion 的正確用法＝只問邊界案例。
- loop-engineering 線：專家標註就是 verifier；配方核心＝把 verifier 成本壓到只剩邊界案例。「瓶頸是 verifier」的解法不是換 verifier，是縮小 verifier 要看的面。

已進 `meta/borrowable-patterns.md` B14（提案中，餵首次 /meta-review）。

## 出處

- 原文：https://thinkingmachines.ai/news/learning-to-replicate-expert-judgment-in-financial-tasks/
- 轉述：FourWeekMBA、CoinDesk、cryptobriefing（2026-07-03 檢索）
- 引路：Fox Hsiao FB 貼文（2026-07-03 截圖）

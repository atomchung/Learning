---
type: card
title: Verifier 是階梯不是開關，而且紅利只在沒有執行回饋的任務出現
aliases: [verifier 分階梯, 瓶頸是 verifier 要拆兩問, 驗證訊號強度階梯, verifier 紅利任務相依]
tags: [coding-agents, loop-engineering, eval, verifier, agent-design]
appears-on:
  - coding-agents
  - loop-engineering
  - eval-design
created: 2026-07-20
freshness: 2026-07  # 具體數字（2.76×、25.1pp）會過期；可遷移的是「階梯高度」與「任務相依」這兩個軸
---

# Verifier 是階梯不是開關，而且紅利只在沒有執行回饋的任務出現

**一句話**：「agentic loop 的瓶頸是 verifier 不是 model」這句話對，但它是**二元命題的講法**，實務上要拆成兩問——(1) 你的 verifier **站在驗證階梯的哪一階**（強度單調決定 loop 能跑多遠）；(2) 這個任務**吃不吃得到 verifier 紅利**（環境自己會報錯的任務吃不到，無執行回饋的知識判斷型任務才是主戰場）。

## 軸一：verifier 有階梯，強度單調決定 loop 能跑多遠

一篇把 2024–2026 共 1,250 篇論文沿「改什麼 × loop 閉合程度」編碼的綜述，抽出一條**驗證階梯**（由強到弱）：

1. **形式化驗證器**（最強）
2. **執行與測試**
3. **外部模型評分**
4. **內在自評**（最弱）

關鍵觀察：**已展示的自我改進強度，追蹤 verifier 在這條階梯上的位置**；而 self-confirming loop、model collapse 這些失敗模式，全都是**違反階梯**——拿弱訊號當強訊號用——的後果。全篇最好的一句統攝：*每一個 improvement loop 都是一個宣稱：某個訊號可以替代人類判斷。*

→ **操作化**：判斷一個 agent loop 值不值得放手跑，問「它的 verifier **站哪一階**」，而不是問「它**有沒有** verifier」。同一個 loop 換一個更弱的驗證訊號，退化路徑是可預測的：先自我確認，再收斂到自己的偏差。

## 軸二：verifier 的紅利是任務相依的（這條最有操作性）

一份機構級受控掃描（12 個前沿模型 × 7 個硬 benchmark，橫跨軟工／數學／醫療／資安）做了一個乾淨的 verifier 消融：同樣是「重複提交」，一組讓模型**自己判斷**要不要重試，另一組給**最小正確性回饋（oracle）**後重試。

- **HLE（知識推理型）**：oracle 回饋 **+25.1pp** vs 自我引導 **+9.1pp** ＝ **2.76 倍**
- **SWE-Bench Pro**：+16.0 vs +12.7 ＝ 1.26 倍
- **FrontierMath、TerminalBench、HealthBench**：oracle 回饋**沒有統計顯著優勢**

→ **實務判準（可以直接拿去用）**：
- 任務環境**自己會報錯**（跑得起來／跑不起來、測試紅綠）→ 環境已經提供了足夠回饋，**投資 verifier 的邊際報酬低**，瓶頸在探索或執行。
- 任務**沒有執行回饋**（知識判斷、方案評選、寫作品質）→ **verifier 就是你的主要槓桿**。

順帶一個對評測方法學的推論：跑分是「模型 × harness 預算」的**聯合函數**——固定預算的評測會系統性低估強模型，而且模型越強、低估越嚴重。

## 軸三（延伸）：verifier 本身可以 test-time scaling，而且弱 verifier 能選強 generator

既然 verifier 是瓶頸，它就該像 generator 一樣被加預算。一篇框架論文把 judge 打分從「取最高機率的那個分數 token」改成「**對整個 scoring-token logit 分佈取期望值**」，拿到連續分數——因為離散化把機率質量丟掉了，代價是大量平手（一個 case study 裡離散 judge 100 次有 88 次平手，連續版 0 次平手、77 次排序正確）。三個可加預算的軸：**分數粒度**（1→20 個 scoring token，73.1%→77.5%）、**重複評分**（1→16 次，74.7%→77.4%）、**判準拆解**（correctness 拆成 Specification／Output／Errors 再 ensemble，76.4%→78.3%）。

值得單獨記的一點：它用**較弱的模型**（Gemini 2.5 Flash）去挑**較強模型**（GPT-5.5／Claude Opus 4.7）產出的候選，**弱 verifier 選強 generator 是可行的**——但這是在 test-time selection 的意義上，不是 training supervision 的意義上（後者未測）。

## 反例與質疑

- **證據全是 preprint**：本卡三個軸的來源都沒有會議接收標記、無獨立複現。軸一那篇是**綜述不是實驗**——階梯是作者的組織框架，「強度追蹤階梯」是對 1,250 篇的歸納，可能有發表偏差（沒效果的 loop 不會被寫成論文）。作者自己承認「governance-grade measurement 仍是未開發區」＝這條階梯目前**還沒有可量化的刻度**。**當思考框架用，別當實測結論引用。**
- **軸二的反向風險**：三個「無顯著優勢」的 benchmark 也可能是 oracle 訊號設計得太弱，而非任務不吃 verifier。要推翻本卡，找一個「環境會報錯但加 verifier 仍大幅獲益」的反例即可。
- **掛著但別寫死的假說**：有兩篇小規模研究（一篇 ICML workshop poster、86 題 AIME、單作者；一篇從訓練側量自訓練）**獨立收斂到同一形狀**——generation 與 self-selection 是兩條**發散**曲線，模型越強絕對落差越大（若成立＝外部 verifier 是結構性必需品，不是等模型變強就會消失的過渡方案）。兩篇各自都不夠格支撐結論，**當假說掛著，等更大規模複現**。
- **verifier 失效有兩種來源，本卡只涵蓋一種**：能力不足（階梯位置低）**和寫錯了**（verifier 作為軟體工件本身有 bug，RL 會學會那個 bug）。後者是獨立的軸。

## 連結
- ← 支持 [harness-beats-model](./harness-beats-model.md)（loop/verifier 屬 harness 之上那層，不換模型就能拉開差距）
- ↔ 對比 [eval-bottleneck-is-criteria-not-tooling](./eval-bottleneck-is-criteria-not-tooling.md)（那張說瓶頸是「寫判準」；這張說判準寫好之後，還有「訊號強度」與「任務吃不吃」兩道關）
- → 引出 [eval-tests-judgment-triage-not-correctness](./eval-tests-judgment-triage-not-correctness.md)（測交派紀律＝弱訊號場景，正是 verifier 紅利最高的區域）
- ↔ 對比 [workflow-lifts-floor-model-sets-ceiling](./workflow-lifts-floor-model-sets-ceiling.md)（工作流之所以封頂，一部分原因是蒸餾出的工作流內含的驗證訊號**等級是固定的**）

## 出處
- [arXiv:2607.07663 — Recursive Self-Improvement in AI](https://arxiv.org/abs/2607.07663)（驗證階梯，1,250 篇綜述，2026-07-08）
- [arXiv:2606.17930 — How Inference Compute Shapes Frontier LLM Evaluation](https://arxiv.org/abs/2606.17930)（12 模型 × 7 benchmark 受控掃描，UK AISI 脈絡，2026-06-16）
- [arXiv:2607.05391 — LLM-as-a-Verifier](https://arxiv.org/abs/2607.05391)（verifier test-time scaling，Finn／Stoica／Mirhoseini 等，2026-07-06）
- [ICML 2026 workshop — The Self-Verification Cliff](https://icml.cc/virtual/2026/82529) ＋ [arXiv:2606.07856 — Teacher-Free Self-Training Amplifies but Does Not Compound](https://arxiv.org/pdf/2606.07856)（掛著的假說）
- [arXiv:2606.01066 — Fuzzing RLVR Verifiers](https://arxiv.org/abs/2606.01066)（verifier 是軟體工件、會有 bug 這條軸）
- 觸發：2026-07-20 三線論文掃描（使用者指出前一輪只用「能不能結算預測帳」一把篩子、漏掉論文層）；`notes/loop-engineering.md`、inbox 2026-07-20

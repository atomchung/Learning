---
type: card
title: eval agent 判斷,測的是「交派紀律」不是判斷正確性
aliases: [把 agent 軟判斷翻成可觀察行為判準, agent 判斷放到可驗證的位置, 判斷的交派紀律]
tags: [coding-agents, eval, agent-judgment, agent-design]
appears-on:
  - coding-agents
created: 2026-07-08
---

# eval agent 判斷,測的是「交派紀律」不是判斷正確性

**一句話**:當你把編排/決策負擔從用戶移到 agent(合一架構、教練型產品),成敗就押在「agent 判斷得好不好」上;但很多判斷沒有 ground truth,你沒法直接 eval「判得對不對」——你能 eval 的是**判斷的交派紀律**:什麼該下沉成 code 自己算、什麼該翻成可觀察的 rubric 交 judge、什麼該老實承認測不準而改成「問用戶」。

## 為什麼重要:把 agent 判斷分三層,eval 難度天差地別

判斷不是一個東西。先分類,才知道每種怎麼 eval:

1. **機械可判**(有客觀對錯,如「路由到哪個模式」「金額最大的是哪筆」)→ **下沉 engine + 單元測試**。天花板高(能到 100% 回歸)。判斷若還留在 agent 的 prose 裡每次重跑,是設計沒收乾淨(且錯一次就錯帳)。
2. **有 rubric 的軟判斷**(無唯一解但有好壞,如「這段輸出有沒有收斂成一個重點」「有沒有洩漏不該出現的東西」)→ **翻成可觀察的行為判準 + LLM-judge / 人工**。天花板中(judge 自己要對齊人類)。
3. **真不可靠**(答案依賴用戶內心,如「他這是計畫還是自我安慰」)→ **不可直接 eval**。好設計不讓 agent 硬猜,改成「**問用戶**」;於是 eval 對象從「判得準不準」變成「**該問時有沒有問**」——落回第 2 層(可觀察行為)。

**收束**:好的 agent 設計 = 讓盡量多判斷變可 eval(能算的下沉 engine、不可靠的轉成問),把真正不可 eval 的殘餘壓到最小、只能靠線上用戶反饋接住。**agent 判得好不好,最終等於「它有沒有把每個判斷放到一個能被驗證的位置」。** 判斷力不是玄學,是可設計、可測的——只要先把判斷分好類。

## 反例與質疑
- **分類本身也是判斷**:某個判斷到底屬「有 rubric」還是「真不可靠」,邊界有時模糊,分錯就 eval 錯層。
- **第 3 層「改成問」有成本**:問太多 = 摩擦,用戶會逃;所以「該問」本身要克制(只問金額最大 / 最矛盾的),這條克制紀律又是一條要 eval 的行為。
- **線上反饋是滯後、稀疏、有偏的訊號**(只有留下來的人才給),不能當唯一防線。

## 連結
- ← 延伸 [eval-bottleneck-is-criteria-not-tooling](./eval-bottleneck-is-criteria-not-tooling.md)(那張說「難在寫判準」,這張說判準怎麼寫 = 把軟判斷翻成可觀察行為 + 三層交派)
- → 引出 [agent-eval-scores-end-state-not-path](./agent-eval-scores-end-state-not-path.md)(第 1 層「機械可判」的具體形式就是終態斷言)
- ↔ 對比 [claude-code-human-in-loop](./claude-code-human-in-loop.md)(第 3 層「改成問用戶」正是 human-in-loop 的 eval 版:把不可靠判斷外包給人)

## 出處
- notes/addyosmani-agent-skills.md「skill vs agent + agent 判斷能不能 eval」節(2026-07-08 session,fomo-kernel 架構討論收束)
- 元判斷來源:合一/教練型架構把成敗押在 agent 判斷 → 判斷可 eval 性成命門

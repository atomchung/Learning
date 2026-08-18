---
type: card
title: Harness 做成可插拔架構，收益是平台效應不是用戶鎖定
aliases: [harness moat, harness 護城河, 插件化 harness]
tags: [strategy, architecture, ai-market]
appears-on:
  - coding-agents
  - ai-market-dynamics
created: 2026-08-18
---

# Harness 做成可插拔架構，收益是平台效應不是用戶鎖定

**一句話**：把整個 harness（連 agent loop 本身）做成可抽換插件，直覺上像是在鞏固護城河，但如果連模型供應商都是可換的插件，任何人都能拿你的 harness 接別家模型——這種開放性換不到用戶鎖定，真正換到的是「先變成業界共通標準」的平台效應。兩者是不同的賭注，容易混為一談。

## 具體案例：DeepSeek Harness（2026-08-13 發布）

架構文件明講：「加一個模型供應商，只要在 `ctx.llm` 註冊它的 adapter」——filesystem、subprocess、subagent 全部走同一套「可換 provider」機制。這代表任何人都可以拿 DeepSeek Harness 去接 GPT-5.5 或 Claude，不是只能接 DeepSeek 自己的模型。

## 我原本的推論錯在哪

第一直覺是「DeepSeek 自己做 harness，是為了不被 Codex 卡住、拿回用戶黏著度和計分權」——把「自己做 harness」直接等同「鎖住用戶」。但看到模型層本身就是可插拔設計後，這個推論站不住：**如果連自家模型都能被換掉，harness 本身就不是鎖用戶的工具。**

## 修正後的框架：兩種不同的賭注，容易被混為一談

- **鎖定型**（護城河邏輯）：harness 深度綁定自家模型，換模型要付出真實摩擦成本（重寫 prompt、重調 tool schema）。用戶留下來是因為離開貴。
- **平台型**（標準卡位邏輯）：harness 對誰的模型都友善，賭的是「這個殼子先變成大家預設用的那個」，像作業系統或套件管理器之爭。用戶留下來是因為生態方便，不是被鎖住。

DeepSeek Harness 目前的架構選擇明顯偏平台型。這解釋了另一個現象：它同時做「自己的 harness」跟「讓自家模型更好接 Codex（Responses API）」——**兩條腿不衝突，因為目標本來就不是鎖定，是兩邊都要卡位**（見 [harness-is-the-new-battlefield](./harness-is-the-new-battlefield.md) 訊號 5）。

## 判準：怎麼分辨一個 harness 是哪種賭注

問一個問題：**換掉模型供應商的成本，主要是「重新設定」還是「重新設計」？** 前者（改個 config、換個 adapter）是平台型；後者（prompt/工具/評分邏輯都要跟著重寫）是鎖定型。

## 如果對，代表什麼

- **投資判斷**：平台型 harness 的估值邏輯要看「開發者採用率、plugin 生態厚度」，不是「模型鎖定率」——用鎖定型的框架去估平台型的公司會估錯
- **這個判斷會過期**：現在（developer preview）架構開放，不代表 GA 後不會收斂成鎖定（例如把最佳化只做給自家模型、預設 bundle 悄悄綁死）。要盯的訊號是**穩定版之後，模型可插拔性是否還維持**

## 連結
- ← 是 [harness-is-the-new-battlefield](./harness-is-the-new-battlefield.md) 留的待寫延伸
- ← 具體案例來自 DeepSeek Harness 架構文件（`docs/architecture.md`，capability seams 章節）

## 出處
- inbox.md 2026-08-18

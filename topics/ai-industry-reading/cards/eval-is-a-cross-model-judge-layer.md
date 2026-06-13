---
type: card
title: Eval 是跨模型裁判層,結構上不該屬於模型廠
aliases: [eval 該住模型外, 模型廠自做 eval 有衝突, 裁判層中立性]
tags: [ai-industry, eval, signal-reading, moat]
appears-on:
  - ai-industry-reading
  - coding-agents
created: 2026-06-04
freshness: 2026-06  # promptfoo 收購是當下案例,會過期;可遷移的是「裁判層該中立」
---

# Eval 是跨模型裁判層,結構上不該屬於模型廠

**一句話**:eval 的用途就是比較、挑選模型,天生要站在所有模型**上面**保持中立;模型廠自己做 eval 踩到兩個結構矛盾,所以 OpenAI 2026-03 收掉自家 Evals 後台、把用戶導去 promptfoo——等於模型廠親口承認 eval 不屬於模型產品。

## 為什麼重要
- 模型廠自做 eval 的兩個結構矛盾:
  1. **自我偏好(self-preference bias)**:LLM 當裁判偏袒自家輸出,越強的模型越明顯,企業不會信。
  2. **冗餘**:eval 要 model-agnostic 才有用,但模型廠沒動機把對手模型支援好。
- 所以「模型廠關掉自家 eval 後台」不是退守,是認清 eval 屬於模型**上面**那層獨立工具。
- 讀產業時的用法:任何「模型廠自己出的評測/排行」都該打折,要中立比較就用第三方。

## 反例與質疑
- 模型廠仍可能用收購把中立工具收編(OpenAI 收 promptfoo),中立是承諾、不是保證——能撐多久要追蹤。
- 安全/紅隊 eval 跟模型深度綁定時,第一方反而有資訊優勢,未必全該外置。

## 連結
- ← 支持 [harness-beats-model](../../coding-agents/cards/harness-beats-model.md)(eval 屬 harness 層,不屬模型——同一個價值外移的判斷)
- ↔ 對比 [read-signals-not-surface-numbers](./read-signals-not-surface-numbers.md)(信號是「模型廠承認 eval 該外置」,不是「promptfoo 勝出」)
- → 引出 [acquiring-neutral-tools-buys-distribution](./acquiring-neutral-tools-buys-distribution.md)(那為什麼還花錢買?)

## 出處
- notes/eval-ecosystem-niche.md §為什麼模型廠自己做 eval 結構上是矛盾的
- 觸發:ihower Threads(OpenAI 收 promptfoo + 收掉自家 Evals 後台)

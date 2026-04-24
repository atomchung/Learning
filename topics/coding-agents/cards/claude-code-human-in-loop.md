---
type: card
title: Claude Code 的每步確認是哲學不是妥協
aliases: [human-in-the-loop, 人機協作循環]
tags: [claude-code, human-ai-collaboration, agent-design]
appears-on:
  - coding-agents
  - human-ai-collaboration
  - agent-safety
created: 2026-04-05
---

# Claude Code 的每步確認是哲學不是妥協

**一句話**：Claude Code 每一步都請求用戶確認，看起來是「還不夠自動化」，但實際上是把 agent 定位成「協作者」而非「代理人」的刻意設計。

## 兩種可能的解讀
1. **妥協說**：模型還不夠好，所以需要人把關——等模型成熟就會移除
2. **哲學說**：人機協作本身就是更好的工作模式——即使模型再強也不該移除

從 Anthropic 的產品線一致性來看（Artifacts、Claude.ai 的回應節奏、Claude Code 的 TAOR 循環），**哲學說的證據更強**。

## 為什麼哲學說更可能對
- 全自動有個隱藏成本：**你失去了學習機會**。每步確認 = 每步都在教 agent 也同時被 agent 教
- 信任是累積出來的，不是設定出來的。每步確認是信任累積的前提
- 「能改方向」比「一次做對」重要——人機循環能捕捉意圖漂移

## 反對論點
- 對熟練用戶來說確認點太密集，變成 UX 阻力
- 非同步場景（issue triage）完全不適合這模式
- 如果模型錯誤率足夠低（e.g. <0.1%），確認的邊際效益會接近零

## 連結
- ← 是 [harness-beats-model](./harness-beats-model.md) 的案例：harness 決定互動範式
- ↔ 對比 [codex-no-network-sandbox](./codex-no-network-sandbox.md)：光譜另一端
- → 引出 [trust-accumulation-in-agents](./trust-accumulation-in-agents.md)（待寫）

## 出處
- compare-coding-agents.md §六、Claude Code Harness 小節

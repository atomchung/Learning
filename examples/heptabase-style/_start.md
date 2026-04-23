---
type: starting-point
topic: coding-agents
created: 2026-04-05
last-updated: 2026-04-23
status: expanding
---

# 起點：我想理解 coding agent 的設計權衡

> 這張卡片不會被寫完——它是一塊磁鐵，所有新讀到的東西先塞進來，等看出子概念時再拆成獨立的原子卡。

## 當下的核心問題
- 三家（Codex / Antigravity / Claude Code）為什麼做出完全不同的設計選擇？
- 背後的權衡是什麼？什麼情境下誰最適合？
- 「模型相同，harness 不同，結果天差地遠」——這個判斷的證據有多強？

## 目前累積的發現（未拆卡）
- 基礎 harness 42% → 優化 harness 78%，影響大於換模型 → [已拆 harness-beats-model]
- Codex 用無網路沙箱換最強隔離，代價是無即時回饋 → [已拆 codex-no-network-sandbox]
- Claude Code 每步都要人確認，反向設計不是 bug 是哲學 → [已拆 claude-code-human-in-loop]
- Antigravity 的三面架構（編輯器/終端/瀏覽器）是唯一有視覺感知的 agent → 待拆
- Opus 4.6 在 Antigravity 裡 thinking token 被壓到 1%——模型能力被 harness 限制 → 待拆
- Claude Code 的 6 層記憶架構是對 agent「失憶」問題的回應 → 待拆

## 下一步可能要拆的卡
- [ ] 三面架構為什麼只有 Antigravity 有
- [ ] agent 的「記憶」到底是什麼層次的問題
- [ ] 即時性 vs 吞吐量的權衡是否有中間解
- [ ] harness 做為差異化戰場，對 model provider 代表什麼

## 相關白板
- `coding-agents` 白板（主場）
- `ai-security` 白板（沙箱隔離的卡會在那裡再出現）
- `human-ai-collaboration` 白板（人機確認機制相關）

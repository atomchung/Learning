---
type: card
title: 隔離性與靈活性是負相關
aliases: [isolation vs flexibility, 隔離靈活權衡]
tags: [tradeoff, security, universal-principles]
appears-on:
  - coding-agents
  - ai-security
  - system-design
created: 2026-04-05
---

# 隔離性與靈活性是負相關

**一句話**：agent 隔離得越徹底（Codex 無網路容器），能做的事越受限；靈活度越高（Claude Code 直接存取檔案系統），潛在風險越大——這是安全領域的通則，不只適用 AI。

## 三家的取捨位置
```
最隔離 ←━━━━━━━━━━━━━━━━━━━━━━→ 最靈活
Codex         Antigravity          Claude Code
(無網沙箱)    (本地沙箱)           (直接檔案系統)
```

## 為什麼這個權衡不可逆
安全領域的定律：**能力越多，攻擊面越大**。
- 無網路 = 不可能洩漏但也不能查資料
- 可打內網 = 查得到但可能被 prompt injection 打進內網
- 直接寫檔 = 效率最高但可能誤刪

## 如何降低權衡的痛
雖然不可逆，但可以**動態調整**：
- 按任務類型切權限（敏感任務切隔離模式）
- 按信任階段放權（新 agent 先嚴格，熟了放寬）
- 按時間窗給權（只在本次 session 開某權限）

Claude Code 的每步確認其實是**靈活 + 動態護欄**的組合方案。

## 更廣的應用
這個權衡也適用於：
- 沙箱 vs 容器 vs VM
- Firewall 嚴格度 vs API 可用性
- 員工權限最小化 vs 工作效率

## 連結
- ← 是 [[harness-four-layers]] 中「安全護欄」層的核心權衡
- → 衍生 [[dynamic-permission-for-agents]]（待寫）

## 出處
- compare-coding-agents.md §六、Harness 設計的核心權衡

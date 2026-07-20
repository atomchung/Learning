---
type: card
title: Agent 協作媒介由拓撲決定：對等走 git、主從同機才走共享終端
aliases: [拓撲決定協作媒介, 共享游標是同機主從的專利, tmux-bridge 是拓撲錯配]
tags: [coding-agents, agent-os, 多agent協作, orchestration]
appears-on:
  - coding-agents
  - agent-collab-infra
  - agent-os
created: 2026-07-18
---

# Agent 協作媒介由拓撲決定：對等走 git、主從同機才走共享終端

**一句話**：多 agent 用什麼協作不是自由選擇，是拓撲逼出來的——**對等/分布式**的 agent（各自獨立主 session、不同機不同時）只有 git remote 可共享，被逼上 diff/PR；**共享游標/終端**（tmux-bridge 那種）只在**主從 + 同機 + 同步**才成立。選錯媒介＝拓撲錯配。

## 為什麼重要：先問拓撲，別先挑工具

**拓撲 A｜主從 + 同機 + 同步**（一個 orchestrator 在同一台機器調度 worker）
- 正本/context 由 orchestrator 持有，worker 短命可拋。
- 可用共享終端匯流排（tmux-bridge）、直接 subagent、或序列化 funnel（見來源筆記「模型 0」）。
- 這是 tmux-bridge demo 的世界。

**拓撲 B｜對等 + 分布式 + 異步**（N 個各自獨立的主 session，各在自己 repo/branch/容器）
- 沒有單一 agent 持有全部狀態，各自長命、有獨立 identity。
- 常不同機、不同時——**沒有共享終端可刮**，唯一共享表面是 git remote。
- 所以 diff/PR 不是偏好，是**唯一可用**的媒介。

**關鍵**：cloud/remote 執行環境（Claude Code on web、隔離臨時容器）天生是拓撲 B——連「共享 tmux」這東西都不存在。所以 tmux-bridge 對「三個主 session 各跑各的」場景是**架構錯配**，不是要不要用的問題。

## 咬合：這是 diff-not-cursor 的隱藏變量

來源筆記主張「協作單位是 PR/diff 不是共享游標」。這張卡補上**條件**：那不是一體適用的偏好，而是**拓撲決定**——拓撲 B 逼你走 diff（沒別的可共享），拓撲 A 反而容得下共享游標/終端（同機同步、worker 可拋）。

共享終端可以當「live 交接的短暫傳輸匯流排」，但**耐久協作單位仍是 diff**；當它想升格成「協作正本底板」就會脆。

## 落地：個人場景怎麼對

- 痛點「並行 session 寫同一 repo 撞車」＝拓撲 B 的異步寫入 → 解法是 git 中介（branch/PR/任務檔）。`session-records → reconcile → personal_os/session-board` 已經是這條對等總線的實作。
- 只有塌縮成「單機、單 driver、live 內循環」（Claude 寫→Codex 秒審、你盯著）才值得拿 tmux-bridge／subagent。

## 2026-07 補一格：拓撲之外還有「同質 vs 異質」（附實測價格標籤）

一篇觀察研究量了 **33,596 個 agent PR / 2,807 個 repo**，並**重放 747 次 three-way git merge** 實測衝突率：

- **同一個 agent 自己的 PR 對：19.8%**
- **跨供應商（不同家 agent）的 PR 對：41.7%** —— 約 **2.1 倍**

所以「拓撲決定媒介」要再細一格：不只「對等 vs 主從」，還有「**同質 vs 異質**」。git 這個媒介在**同質**對等下摩擦約 20%，**異質**對等直接翻倍。同一家 agent 之間衝突低，很可能是因為 diff 風格與修改粒度一致——**這是 diff 這個媒介的隱藏前提**。

兩個有實務意義的附帶數字：**40.2% 的 repo 存在同時活躍的 agent PR 對**（放寬到一週協作窗則 53.4%）＝並行是常態不是例外；但 **99.5% 的併行對是同一個 agent**，跨家組合只出現在 **4.3%** 的 repo——**混用不同家 agent 併行改同一個 repo，你在的是一個樣本極少、且已知代價翻倍的區域**。

**讀這個數字要打的折**：41.7% 是**文字層**衝突，**語意衝突（git 不擋的那種）完全沒測到**——而那恰好是並行紀律裡最該防的類別。所以 41.7% 要當**下界**讀，不是全貌。證據等級：arXiv:2607.04697，preprint、7 頁 short-paper 規模、747 次重放相對 33,596 個 PR 屬小樣本；但證據形態硬——觀察性、真實 repo、無自賣方法的動機偏誤，且附 replication package（有 DOI）。

## 反例與質疑
- 若未來 remote 環境提供「跨 session 共享 live 狀態」原語（非 git），拓撲 B 也能有共享游標，「唯一可用 git」就要鬆動。目前（2026-07）不存在——記著當證偽訊號。
- 另一面：tmux-bridge 跨廠（CC/Codex/Gemini/Kimi）也算「中立 harness 層 orchestration」的一票，不是全無價值；只是它的地盤是拓撲 A。

## 連結
- ↔ 對比 [async-vs-sync-agent-paradigm](./async-vs-sync-agent-paradigm.md)（異步/同步軸就是拓撲→媒介的底層：分布式對等＝異步＝git；同機主從＝同步＝終端）
- → 引出 [orchestration-as-a-model-vs-neutral-harness](./orchestration-as-a-model-vs-neutral-harness.md)（orchestration 住哪層；tmux-bridge＝harness 層跨廠編排的脆弱版）
- 底層架構出處 [agent-collab-infra 筆記](../../../notes/agent-collab-infra.md)（git vs CRDT、序列化模型 0）

## 出處
- 2026-07-18 對話：tmux-bridge Threads 截圖 →「基於實際場景怎麼用」，辨析出「三個主 session 是對等不是主從」。
- 工具：[tmux-bridge-mcp (howardpen9)](https://github.com/howardpen9/tmux-bridge-mcp)——讓 CC/Codex/Gemini/Kimi 經 tmux 分頁互讀終端、走 MCP。
- 順帶信號坑（另記 inbox）：爆紅那則貼文是沒標源的轉載，真作者 howardpen9＝回文的 0xhoward_peng＝「讀信號不讀表面數字」即時案例。

# Strands Shell：給 agent 的「in-process 沙箱」

> 來源：Pahud Hsieh 串文（2026-06-16）轉介 Clare Liguori 發布的 `strands-agents/shell`。
> AWS 陣營（Strands 是 AWS 開源 agent 框架，Clare 是 AWS principal engineer）。
> 主題線：coding-agents → 沙箱光譜。freshness: 2026-06。

## 它是什麼

一個**專門給 agent 用的 shell**，Rust 寫核心、提供 Python / Node binding。

定位標語：「give your agent a shell without giving it the keys to your machine」——給 agent 一個 shell，但不交出整台機器的鑰匙。

## 核心技術主張

- Agent 的 tool call 全跑在 Rust 構建的 **VFS（虛擬檔案系統）**裡
- **全程 in-process，沒有 fork / exec / syscall**
- 因此 cold start < 1ms、system call 延遲 < 1ms
- 可精細控制 agent 看得到/動得到什麼：檔案、網路 domain、憑證
- Pahud 比喻：agent 以為在跑 shell，其實「被困在 Rust 裡，連沙箱一根毛都碰不到」

## 為什麼值得注意（沙箱光譜上的反設計）

傳統幫 agent 隔離走 **OS 級隔離**——container / micro-VM / firecracker / bubblewrap。隔離強，但**冷啟動貴**（firecracker 上百 ms，container 更慢）。對連續跑幾十次短 tool call 的 agent，cold start 主宰延遲。

Strands Shell 走另一個點：不開 VM、不開 process，**在 userspace 用 Rust 做一層 mediation**，攔截檔案/網路/憑證存取、全在同 process 內模擬。所以 cold start 才壓到 <1ms。

**跟「Codex 用即時性換隔離性」正好對撞**：Codex 承認 trade-off、選即時性犧牲隔離；Strands Shell 主張**不必 trade**——模擬一整個虛擬世界，同時拿即時性 + 隔離。「我能兩個都要」才是真正看點。

## 要打的折（讀信號不讀數字）

1. **「<1ms」是 in-process 的必然，不是奇蹟**：不 fork/exec 當然沒 process 啟動成本。命令本身做什麼才決定真實延遲，標題數字偏 best-case。
2. **in-process mediation 本質比 VM 軟**：micro-VM 有硬體邊界；Rust 攔截層是**軟體邊界**——攔截層有 bug，或 agent 跑到 native code / FFI / 未代理的 syscall，邊界就漏。「碰不到一根毛」只在**所有動作都乖乖走 Rust 模擬世界**時成立。它的安全模型是「完整 mediation」假設，不是物理隔離。
3. **是補位不是取代**：跑任意不可信 native binary → 還是得 VM；跑「agent 自己生成、走 shell 介面的操作」且要快 → in-process 代理很划算。

## 對我們有啥應用（誠實版）

**直接採用的 ROI 現在偏薄**——我們現在的東西（personal_os 看板、session-records、這個 Learning repo）大多是 dashboard / markdown，不是「會跑不可信 tool call 的 agent runner」。沒有現成痛點等這個工具解。

但有三個可能落點，按真實度排：

1. **概念當鏡子（最實在）**：「in-process mediation vs OS 隔離」是一個可重用的權衡透鏡。又一個 **harness>model** 案例——沒換模型，純靠重設計「agent 跑命令那層」就把沙箱的延遲/隔離權衡挪到新位置。最大價值是當知識資產 + 訊號，不是現在就裝。
2. **若做「捕捉點 bot」會用到（部門大腦那條開放疑問）**：若哪天真做一個會自動跑 agent tool call 去抓/處理內容的 bot，「給 shell 不給鑰匙」+ Python binding 就是現成候選。目前還在 speculative 階段。
3. **個人工具想讓 LLM 安全跑 shell 時**：任何想讓 agent 在本機跑受限 shell 的小工具，Python binding 可 drop-in。但要先有那個需求才談。

**一句話**：對我們現在是**知識/訊號價值 > 工具採用價值**。收進沙箱光譜當「Codex 換隔離」的對照端；真要用，等「捕捉點 bot」那條線啟動再回來看。

## 連結

- 對照端：`topics/coding-agents/` 的「Codex 用即時性換隔離性」卡
- harness>model：`topics/coding-agents/cards/harness-beats-model.md`
- 可能用到的場景：`notes/department-brain-process.md`（捕捉點 bot）

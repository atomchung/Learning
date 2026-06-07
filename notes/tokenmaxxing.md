---
type: note
title: Tokenmaxxing
created: 2026-06-07
freshness: 2026-06
---

# Tokenmaxxing：把 token 用量當生產力的陷阱

## 一句話

把「燒掉多少 token」當成工程生產力的代理指標——是把槓桿誤當 KPI。

## 什麼是 Tokenmaxxing

token 用越多 = 假設越有產出。2026/4 從工程圈內梗變成管理層真議題的觸發點：Meta 內部 **Claudeonomics leaderboard**，按 token 用量排名員工，封號「Token Legend」。

背後有半真的直覺撐著：捨得花 token（多迭代、長 agentic loop、review agent 介入）確實常換到更好結果——Salesforce +79% 就是這條槓桿。Tokenmaxxing 是把這條槓桿**誤當 KPI**，把 input 當 outcome。

## 為什麼打臉

- 燒 token ≠ 做得更好。放任 agent 狂跑產出 **"workslop"**：大量低價值、錯誤百出的輸出，反而侵蝕效率。
- Amazon 關掉內部 token leaderboard，要員工解業務問題而非追用量。
- Salesforce：「你可以燒一百萬 token，對公司零正面產出。」
- Fortune（2026/5/28）下標：**"Tokenmaxxing is over"**——公司沒拿到想要的 ROI。

## 正確方向

optimize 不是 maximize。真槓桿：
- **模型選擇**：對的任務用對的模型
- **餵對 context**：相關 context 比更多 token 有用
- **harness 設計**：review agent、skills、skill routing——這些才是 Salesforce +79% 的來源

## 接既有判斷

- **讀信號不讀表面數字**：token 量是教科書級的 input metric，拿來當 outcome proxy = 典型失誤
- **harness > model**：光加 token 而不配 review/skills，加不出價值
- **估計值 vs 實測值**：token 量能看起來很忙，但不是 +79% 那種實測產出

## 候選升級卡片

「燒 token 不等於有產出」——跨脈絡重用點：AI 產業判斷（ROI 衡量）、coding agent harness 設計、個人生產力系統。

## 出處

- [Built In — What Is Tokenmaxxing](https://builtin.com/articles/ai-tokenmaxxing)
- [Fortune — Tokenmaxxing is over (2026/5/28)](https://fortune.com/2026/05/28/tokenmaxxing-is-dead-companies-didnt-get-the-roi-from-ai-they-wanted-to-see/)
- [Faros.ai — Tokenmaxxing vs productivity](https://www.faros.ai/blog/tokenmaxxing)
- [Ravi Mehta — How to tame tokenmaxxing](https://blog.ravi-mehta.com/p/how-to-tame-tokenmaxxing)

---
type: card
title: context 該按需分層載入,不是塞進單一 catch-all 檔
aliases: [分層勝過大 CLAUDE.md, catch-all 多燒 token, 92% token 懲罰]
tags: [coding-agents, context-engineering, claude-md, cost]
appears-on:
  - coding-agents
created: 2026-07-10
---

# context 該按需分層載入,不是塞進單一 catch-all 檔

**一句話**:把規則/知識全塞進一個 catch-all 脈絡檔(肥 CLAUDE.md / AGENTS.md),比按需載入的結構化方式**多燒約 92% token**(Atlassian 實測);repo 規模一大,分層拆檔就從美學變成 token 經濟的必要。

## 為什麼重要
- Carola Pescio Canale(Atlassian, Figma Config 2026):catch-all 脈絡檔比專用工具/MCP 多耗 **92% token**——硬數據,不是偏好。
- 這是「該精簡」的**第二個獨立理由**。你既有論據是**遵循度**(agent-context-best-practices:超 200 行被稀釋/整塊忽略);92% 說的是**成本**——就算遵循度沒掉,你也在多付 token 稅。兩個理由疊加。
- 你的 harness 線(Issue #6)本來就在壓 CLAUDE.md 行數(290→268,目標 <200)——92% 給了「該拆」的量化彈藥。
- 推論:你有 14 個 git repo,**明確站分層這邊**——共用規則下沉、專案規則按需載入,別每個 repo 背一份 catch-all。

## 反例與質疑
- 分層的代價:載入邏輯複雜、agent 可能**漏載該載的檔**(對應你的 boot-miss 缺陷類)。單檔的笨好處是「它一定在 context 裡」。
- Figma 內部就打對台:Harald Kirschner 主張單一 `AGENTS.md` 集中好管。**分歧點是規模**——小專案單檔省心,多 repo 才值得分層。
- 92% 是特定 benchmark 的數字,別當普適常數,不同任務比例會變。

## 連結
- ← 支持 [claude-md-as-project-contract](./claude-md-as-project-contract.md)(契約要精簡才有人遵守)
- ↔ 對比 [mcp-as-extensibility-lever](./mcp-as-extensibility-lever.md)(專用工具/MCP 是 catch-all 的替代載體)

## 出處
- notes/three-confs-2026-ai-builder-scan.md(Atlassian 92% 段)
- Figma Config 2026《How structured thinking gives your AI superpowers》(Carola Pescio Canale)

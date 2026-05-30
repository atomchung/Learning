# Agent OS：是 best practice 嗎？市場全景與本質價值

> 整理日期：2026-04-27
> 主題：Agent OS 概念的批判性檢視

---

## 一、跨工具真的是唯一價值嗎？

**老實說：是，但不完全是。** 拆三層來看：

### 1. 跨 Codex / Claude / Gemini

這是 Nufar 的主要賣點，但被講過頭了。實際上會頻繁換 agent harness 的人不多，多數人就是黏一個生態系。如果你只用 Claude Code，原生的 `CLAUDE.md` + `.claude/skills/` + MCP 已經涵蓋了七層裡的五層。

### 2. 強迫你結構化思考

這個價值常被忽略，但其實是真的。把 identity / context / guardrails 分檔，比丟一個 5000 字的 system prompt 更容易迭代和除錯。

### 3. 資產化、版本控

skills/context 變成 git repo，可以 diff、可以 review、可以分享。這在團隊環境特別有用。

> **結論**：「跨工具」是賣相，「**強迫結構化**」才是它真正在做的事。如果你的設計已經結構化了，那 Agent OS 對你的邊際價值其實很有限。

---

## 二、它是 best practice 嗎？

**不是「業界共識」，是「一種包裝得不錯的觀點」。**

7 層這個數字有點刻意──Anthropic 官方文件其實只強調 3 件事：CLAUDE.md（routing）、Skills（能力）、MCP（連線）。Nufar 把 memory / verification / automations 拆成獨立層，是個人偏好，不是標準。

**我的判斷：4 層就夠**
- Identity + Context 合一
- Skills
- Memory
- Connections

Verification 應該寫在每個 skill 裡（離權限最近的地方），Automations 是觸發機制不是抽象層。Nufar 的七層比較像課程結構，不是工程架構。

---

## 三、市場上的方案大致分四派

| 派別 | 代表 | 本質 |
|---|---|---|
| **檔案約定派** | Anthropic Skills、`CLAUDE.md`、`AGENTS.md`、`.cursorrules`、Aider conventions | 純 markdown，不裝任何東西，直接靠工具讀取 |
| **記憶層派** | mem0、Letta（前 MemGPT）、Memori、Acontext | 主打 long-term memory，把記憶從上下文窗抽出來變獨立服務 |
| **編排框架派** | LangGraph、CrewAI、AutoGen、Microsoft Agent Framework | 程式碼導向，做 multi-agent orchestration |
| **產品化平台派** | MindStudio、Lindy、n8n + AI、Make.com | UI 拖拉，把 agent 包成 SaaS |

**Agent OS 屬於第一派**，本質就是「一套你自己拿 markdown 寫的約定」。它不是技術，是**方法論**。

所以它不會跟 mem0 競爭（你可以兩個一起用），但會跟「我自己的 CLAUDE.md 寫法」競爭。

---

## 四、什麼時候真的值得用 Agent OS 風格？

### 適合的場景

- 你經常**換 harness**（真的，不是嘴巴上說會換）
- 你**多人協作**，需要把 agent 配置當成 codebase 一樣 review
- 你的 agent 任務**橫跨多個專案/領域**，需要分層管理
- 你已經被 5000 字的 system prompt 搞瘋了，想拆解

### 不太需要的場景

- 你只用一個工具，只有一兩個 skill，長度可控
- 你的 agent 只做專案內任務，CLAUDE.md 就夠
- 你的需求其實是「記憶」（那直接上 mem0 / Letta）

---

## 五、總結：本質價值表

| Agent OS 的賣點 | 真實價值 | 替代方案 |
|---|---|---|
| 跨工具可攜性 | 中（取決於你會不會真的換工具） | 直接堅守一個生態系 |
| 強迫結構化思考 | 高 | 任何分層 prompt 設計 |
| 資產化、git 管理 | 高 | 直接把 CLAUDE.md 進 git |
| 七層架構 | 低（過度設計） | 4 層就夠 |
| Chief of staff 範例 | 中（教學用） | 你自己的 use case |

---

## 六、評估自己設計的對照問題

要對比自己的設計，先問這四題：

1. 我現在是把所有東西塞 `CLAUDE.md`，還是已經拆檔？
2. 我用單一工具還是多工具？
3. 我的痛點是「上下文太散」「記憶不持續」還是「不能跨工具」？哪一個？
4. 個人用還是團隊用？

---

## 來源

- [Anthropic Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [mem0 - Memory Layer](https://github.com/mem0ai/mem0)
- [Awesome Agent Skills (community collection)](https://github.com/VoltAgent/awesome-agent-skills)
- [Acontext: skill-as-memory](https://github.com/memodb-io/Acontext)
- [Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices)

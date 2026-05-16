# Agent Context 管理 Best Practices

> Context Engineering 實戰指南 | 2026 年 5 月

> 「Context is finite, with diminishing marginal returns」——核心紀律是用**最少的高訊號 token**達成最大可能的結果。

## 一、為什麼 Context 管理是 Agent 工程的核心

LLM 的 context window 是有上限的，而且越接近上限**精準度越差**：

| Context 使用率 | 行為表現 |
|---|---|
| < 50% | 模型運作最穩定 |
| 50%–70% | 仍然可靠，是日常工作區間 |
| 70%+ | 精準度開始下降，記憶開始模糊 |
| 85%+ | 幻覺明顯增加，指令遵循度大幅降低 |
| ~95% | 進入 auto-compact 觸發區 |

換句話說，**塞滿 1M context 不會讓 agent 變聰明，反而會變笨**。Context engineering 的目標不是「裝得多」，而是「裝得對」——在每個 inference step 留下對當下決策最有用的 token。

---

## 二、三大核心策略：Compaction / Tool Result Clearing / Memory

業界（Anthropic、OpenAI、Google、各家 harness）收斂出三個核心 primitive。它們不是互斥，而是**組合使用**。

### 策略 1：Compaction（壓縮）

把快滿的對話**摘要成短文**，用摘要重新初始化 session。

**何時觸發：**
- 推薦門檻：60%–75% context fill 時主動觸發（auto-compact 通常在 80%+ 才會啟動，太晚）
- API 上典型設定：`input_tokens` 達 150K–180K 時觸發
- 最低有意義門檻：50K tokens（再低壓縮的開銷不划算）

**該保留的：**
- ✓ 任務狀態與下一步要做什麼
- ✓ 關鍵決策與其理由
- ✓ 量化事實（數字、版本、參數）
- ✓ 未解決的問題清單
- ✓ 程式碼片段、變數名、檔案路徑

**該丟掉的：**
- ✗ 冗長的解釋與來回討論
- ✗ 重複嘗試的失敗紀錄
- ✗ 可以重新查到的細節（表格的單一儲存格、API 的完整回應）

**自訂 instructions 範例（針對 debugging 場景）：**
```python
"instructions": (
    "Focus on preserving code snippets, variable names, technical "
    "decisions, and the current debugging state. Discard verbose "
    "explanations and redundant attempts."
)
```

### 策略 2：Tool Result Clearing（工具結果清理）

把舊的 tool call **結果體**清掉，但**保留 tool call 的紀錄**（agent 知道呼叫過、需要時可再叫一次）。

**何時用：** Agent workflow 被檔案讀取、API 呼叫、search 結果這類**可重新取得**的資料佔滿時。

**參數實戰：**
```python
{
    "type": "clear_tool_uses_20250919",
    "trigger": {"type": "input_tokens", "value": 100_000},
    "keep": {"type": "tool_uses", "value": 6},        # 保留最近 N 次
    "clear_at_least": {"type": "input_tokens", "value": 10_000},
    "exclude_tools": ["memory"]                        # 保護 memory tool
}
```

**`keep` 值該怎麼選：**
- `keep=3`：激進，會強迫 agent 重新讀檔，但 context 最乾淨
- `keep=6`：折衷，多數場景推薦
- `keep=10+`：保守，適合需要回頭比對的任務

**和 compaction 的差別：**
| 維度 | Tool Clearing | Compaction |
|---|---|---|
| 觸發成本 | 機械式編輯，**零 inference** | 需要呼叫模型做摘要 |
| 處理對象 | Tool result blocks | 整段對話與推理 |
| 該先用哪個 | **先**（成本低） | 後（clearing 不夠才上） |

### 策略 3：Memory（檔案式持久化記憶）

讓 agent 把發現寫到**context 外的檔案**，下一個 session 再讀回來。

**典型結構：**
```
/memories/
  ├── MEMORY.md                  # 索引（每次 session 都載入）
  ├── architecture-notes.md      # 細節（按需讀取）
  ├── debugging-patterns.md
  └── api-conventions.md
```

**Session 間的節能效果：**
- Session 1：研究完整 corpus，把發現寫進 `/memories/` → peak context ~170K
- Session 2：開頭只載入 MEMORY.md（~3K），按需讀細節檔 → **同樣任務省 40% token**

**Claude Code 的 auto memory：**
- 啟用條件：v2.1.59+，預設開啟
- 觸發時機：Claude **自己決定**何時值得記下
- 載入規則：每次 session 開頭載入 MEMORY.md 的**前 200 行或 25KB**（兩者取小）
- 儲存位置：`~/.claude/projects/<project>/memory/`（machine-local，不跨機器）

---

## 三、CLAUDE.md 實戰：寫了等於白寫的常見錯誤

CLAUDE.md 是 Claude Code 的「永久指令」——每個 session 開頭都會載入。但**寫得不好等於白寫**。

### Size：目標 < 200 行

- 200 行以下：指令遵循度最高
- 200–400 行：開始稀釋，重要規則被淹沒
- 400+ 行：「30 條有用規則埋在噪音裡，比 60 行每條都載重的檔案差很多」

**壓縮 CLAUDE.md 是多數團隊投資報酬率最高的優化動作。**

### Specificity：能驗證才有用

| ❌ 模糊指令 | ✓ 具體指令 |
|---|---|
| Format code properly | Use 2-space indentation |
| Test your changes | Run `npm test` before committing |
| Keep files organized | API handlers live in `src/api/handlers/` |

### 該寫進 CLAUDE.md 的訊號

加進去的時機：
- Claude **犯了第二次**同樣的錯
- Code review 抓到 Claude 應該知道的事
- 你已經輸入過同樣的修正不止一次
- 新隊友也會需要這個 context 才能上手

### 不該寫進 CLAUDE.md 的內容

- 多步驟流程 → 改用 **skill**
- 只在某個目錄重要的規則 → 改用 **path-scoped rule**（`.claude/rules/*.md` + frontmatter `paths:`）
- 必須在某個時點觸發的動作 → 改用 **hook**

### Compaction 與 CLAUDE.md 的互動

- ✓ **Project-root CLAUDE.md 會在 `/compact` 後重新載入**——寫在這裡的指令是永久的
- ✗ 對話中臨時給的指令會在 compaction 後消失
- ⚠ 子目錄的巢狀 CLAUDE.md 不會自動重載，要等 Claude 再讀那個子目錄的檔案時才會回來

**規則**：任何你希望「永遠都在」的指令，**必須**寫進 CLAUDE.md，不能只在對話裡講一次。

### 階層與優先序（從廣到窄）

| 範圍 | 路徑 | 用途 |
|---|---|---|
| 組織 | 系統 managed 路徑 | 公司全體規範、合規要求 |
| 使用者 | `~/.claude/CLAUDE.md` | 個人偏好（所有專案） |
| 專案 | `./CLAUDE.md` 或 `./.claude/CLAUDE.md` | 團隊共享（進 git） |
| 本機 | `./CLAUDE.local.md` | 個人專案偏好（進 .gitignore） |

載入順序「從廣到窄」——所以**專案規則會蓋過個人偏好、個人偏好會蓋過組織規則**。

---

## 四、Sub-agent 模式：Context 隔離的最強槓桿

Sub-agent（subagent / Task tool）的核心價值不是「能做更多事」，而是**讓重活在獨立 context 裡發生，髒東西不污染主線**。

### 隔離原則

> **「Share memory by communicating, don't communicate by sharing memory.」**

- Sub-agent 不和 orchestrator 共享 context
- Sub-agent 之間也不共享 context
- 唯一溝通管道：orchestrator 給它的 prompt + 它回傳的結果

→ 主 agent context 只增加「sub-agent 回報的摘要」，不增加「sub-agent 中間 100 次 tool call 的雜訊」。

### 何時派 sub-agent

**派**：
- 開放式搜尋（"where is X defined", "find all usages of Y"）——會吃大量 grep 結果
- 獨立可平行的子任務（同時跑 lint / test / build 檢查）
- 讀大量檔案後只需要結論（research、audit）

**不派**：
- 簡單的單檔讀寫——直接 Read/Edit 就好，派 agent 反而增加 token 開銷
- 需要主 agent 持續觀察中間狀態的任務
- 整個任務只有 2–3 個 tool call

### 平行化的甜蜜點

- **過度平行**：對一個簡單 feature 派 10 個平行 agent → 浪費 token + 協調成本
- **不夠平行**：應該平行的獨立任務排成 sequential → 浪費時間
- **判斷標準**：子任務之間有**領域獨立性**（彼此不依賴對方的結果）才平行

Claude Code 上限是同時 10 個 sub-agent。實務上 2–5 個是常見的甜蜜點。

### Dispatch prompt 是最重要的 artifact

Sub-agent 沒有對話 context，prompt 必須**自給自足**：

- 任務目標（為什麼做、要達成什麼）
- 已知與已排除的事項
- 具體的檔案路徑、行號、symbol 名
- 成功判準（怎樣算完成）
- 期望回傳格式與長度

Orchestrator 模式四階段：**Clarify → Plan → Dispatch → Verify**。Dispatch prompt 是整個流程裡最值得花時間打磨的東西。

---

## 五、決策框架：我該用哪一招？

從 context 的組成來反推策略：

| 你的 context 主要是… | 主要用 | 次要搭配 |
|---|---|---|
| > 90% 是檔案讀取／搜尋結果 | **Tool Result Clearing** | + Memory（跨 session） |
| > 30% 是 agent reasoning + 對話 | **Compaction** | + CLAUDE.md（永久指令） |
| 知識需要跨 session 保留 | **Memory** | + 把摘要寫進 MEMORY.md |
| 任務天然分階段 | **三者全用** | + Sub-agent 隔離各階段 |
| 任務有多個可平行的子問題 | **Sub-agent** | + 結果寫回 Memory |

**組合策略範例（最常見的「全菜」配置）：**

```python
context_management={
    "edits": [
        # 先清便宜的 tool result
        {
            "type": "clear_tool_uses_20250919",
            "trigger": {"type": "input_tokens", "value": 60_000},
            "keep": {"type": "tool_uses", "value": 6},
            "exclude_tools": ["memory"]
        },
        # 還是大才壓縮對話
        {
            "type": "compact_20260112",
            "trigger": {"type": "input_tokens", "value": 150_000},
            "instructions": "Preserve task state, key decisions, code snippets, and findings."
        }
    ]
}
```

執行順序：
1. **Clearing 先觸發**（便宜、機械式）
2. **Memory 由 model 在過程中自己寫**
3. **Compaction 最後才觸發**（如果清完還是大）

---

## 六、常見反模式

| 反模式 | 為什麼錯 | 該怎麼做 |
|---|---|---|
| CLAUDE.md 寫滿 500 行 「以防萬一」 | 訊噪比降低，重要規則被忽略 | 壓到 200 行內，其他放 skill / rules / hooks |
| 等到 95% 才 auto-compact | 進入精準度暴跌區才動作 | 60–75% 主動觸發 |
| 把所有資訊塞給 sub-agent | Sub-agent 也會 context 爆 | 只給「它需要的最小集合」 |
| 對話裡給「永久」指令 | Compaction 後消失 | 寫進 CLAUDE.md |
| Sub-agent prompt 寫成 「based on previous findings, do X」 | Sub-agent 看不到 previous | Prompt 必須自給自足，含路徑/行號 |
| 用 sub-agent 取代 Read | Sub-agent 啟動成本 > 直接 Read | 已知路徑直接讀 |
| 平行派 10 個 agent 跑簡單任務 | 協調 overhead > 平行收益 | 看「領域獨立性」決定平行度 |
| 把 secret / 大 binary 塞進 CLAUDE.md | 永久在 context、可能洩漏 | 用 env var + .gitignore |

---

## 七、各家 Harness 的 Context 策略對照

| 維度 | Claude Code | Codex | Antigravity |
|---|---|---|---|
| Context window | 原生 1M | ~200K（任務級） | Opus 在裡面被限 200K |
| 主要策略 | 6 層記憶 + 5 種壓縮 | 容器隔離（每任務獨立） | Manager 拆解 + Artifact 摘要 |
| 跨 session 記憶 | CLAUDE.md + Auto Memory | 弱（每容器獨立） | IDE 內專案級 |
| Sub-agent | Task tool（最多 10 平行） | 多容器平行（隔離最徹底） | 16 個專業 agent |
| 適合任務 | 深度互動 + 大型 codebase | 非同步批量 | 多 agent 編排 |

→ 詳細對比見 [compare-coding-agents.md](./compare-coding-agents.md) 第六節。

---

## 八、實戰檢查清單

開新專案時：
- [ ] 跑 `/init` 建立 CLAUDE.md 骨架
- [ ] 壓到 200 行內，每條都「拿掉會出事」
- [ ] `.claude/rules/` 放分區規則（前端、後端、測試）
- [ ] `CLAUDE.local.md` 加進 `.gitignore` 放個人偏好

進入長 session 時：
- [ ] Context 到 60–70% 主動 `/compact`，別等 auto
- [ ] 重要進度寫進 MEMORY.md / progress 檔案，別只留在對話
- [ ] 重活派 sub-agent，主線只收結論

設計多 agent 流程時：
- [ ] Dispatch prompt 自給自足（含路徑、行號、成功判準）
- [ ] 評估「領域獨立性」決定平行度（2–5 通常是甜蜜點）
- [ ] Sub-agent 回傳格式約定好（要求 < 200 words 之類）

設定 API context_management 時：
- [ ] Clearing 在前（trigger ~60K）
- [ ] Compaction 在後（trigger ~150K）
- [ ] `exclude_tools: ["memory"]` 保護記憶相關 tool call

---

## 九、給人類 PM：當你自己就是會 context-switch 的 agent

前八節在講「agent 的 context 怎麼管」。但多數 PM 的真正痛點是**自己的 context**——一次開很多任務，切換時失去注意力，每次回到某個任務都要花 5–10 分鐘重新理解進度。

解法的 pattern 和 agent 完全一樣：**把狀態寫到 context 外，重啟時自動載回來**。

### Best Practice：`/handoff` skill + SessionStart hook 雙向迴路

| 動作 | 機制 | 觸發時機 |
|---|---|---|
| **寫筆記** | `/handoff` skill | 切走前、`/clear` 前、關電腦前——你主動打 |
| **載筆記** | SessionStart hook | 新 session / `/compact` 後 / `/resume` 後——自動 |

### 1. `/handoff` skill（5 區段，< 250 字）

放在專案 `.claude/skills/handoff/SKILL.md`（團隊共享）或 `~/.claude/skills/handoff/SKILL.md`（個人跨專案）。要求 Claude 把當下對話濃縮成五段：

```
## Goal      <一句話：要達成什麼>
## Done      <已完成，含檔案路徑>
## Open      <未完成 / queued>
## Next      <下一個具體動作（單數，不是 menu）>
## Watch out for  <下個 session 會踩的雷>
```

關鍵規則：
- **覆寫**不是 append——過時的行比沒有 handoff 更糟
- 全文 < 250 字——擠不下代表你在寫敘述，不是事實
- 引用檔案用路徑+行號（`file.md:120`）
- 不要憑空產生 next step——若卡住就寫「卡在哪」

### 2. SessionStart hook（自動載回）

放在專案 `.claude/settings.json`：

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": ".*",
      "hooks": [{
        "type": "command",
        "command": "test -f .claude/HANDOFF.md && cat .claude/HANDOFF.md || true"
      }]
    }]
  }
}
```

這個 hook 在三個時點都會跑：**session 啟動 / `/compact` 後 / `/resume` 後**——你不需要記得「載回筆記」，Claude 開口前 context 就已經有了。

### 3. `.gitignore` 排除個人筆記

```
.claude/HANDOFF.md          # 個人進度，不進 git
.claude/settings.local.json # 個人設定覆寫
```

Skill 本身和 hook 設定**進 git**（團隊共享）；HANDOFF.md 是個人本機筆記，**不進 git**。

### 為什麼這套贏過純 `/resume`

| 場景 | 純 `/resume` | Handoff + SessionStart |
|---|---|---|
| 同機器同專案 | ✓ | ✓ |
| 換機器 / 換 worktree | ✗ session 本機綁定 | ✓ 寫成檔案（雖然 gitignored，個人雲端同步可帶） |
| `/compact` 後 | ✗ 對話細節已壓縮 | ✓ hook 自動重塞 |
| 給隊友接手 | ✗ | ✓ 純文字 briefing |
| Token 成本 | 高（全量還原） | 低（~250 字摘要） |

### 對人類 PM 的工作流建議

1. **每個專案一份 HANDOFF.md**——切走前 30 秒，打 `/handoff`
2. **主線任務 ≤ 3 條**——研究說 Claude Code 平行 sub-agent 甜蜜點 2–5，對人類也適用，超過就條條失焦
3. **背景任務派 sub-agent，不要再開 session**——你要維持的「主線」越少，越能專注
4. **「想到要查的東西」用 TODO 不開新 session**——記在主線的 HANDOFF.md `Open` 區，回頭再批次處理

> 核心啟示：**Context engineering 對 LLM 和對人類是同一件事**——都是用最少的高訊號狀態，達成最大化的續行能力。

---

## 十、TL;DR：三句話帶走

1. **Context 是有限資源，過載會讓 agent 變笨**——目標不是裝得多，而是 60–75% 工作區間。
2. **三大策略組合用**：Tool Clearing（便宜，先觸發）→ Memory（跨 session）→ Compaction（昂貴，最後觸發）。
3. **想永久存在的指令寫進 CLAUDE.md（< 200 行）；想跨 session 的知識寫進 Memory 檔；想隔離污染的重活派 sub-agent。**

---

*產出日期：2026-05-16*

### 參考來源

- [Effective context engineering for AI agents | Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Context engineering: memory, compaction, and tool clearing | Claude Cookbook](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)
- [How Claude remembers your project | Claude Code Docs](https://code.claude.com/docs/en/memory)
- [Claude Code & Agent Memory: Best Practices for 2026 | orchestrator.dev](https://orchestrator.dev/blog/2026-04-06--claude-code-agent-memory-2026/)
- [Context management in agent harnesses: memory, files, and subagents | Arize AI](https://arize.com/blog/context-management-in-agent-harnesses/)
- [Context Engineering for AI Agents: Part 2 | Phil Schmid](https://www.philschmid.de/context-engineering-part-2)
- [How Agents Manage Other Agents: Four Subagents Patterns in 2026 | Phil Schmid](https://www.philschmid.de/subagent-patterns-2026)
- [Building Reliable Agents with Memory and Compaction | OpenAI Cookbook](https://developers.openai.com/cookbook/examples/agents_sdk/building_reliable_agents_memory_compaction)
- [Shedding Heavy Memories: Context Compaction in Codex, Claude Code, and OpenCode | Justin3go](https://justin3go.com/en/posts/2026/04/09-context-compaction-in-codex-claude-code-and-opencode)
- [Claude Code Sub-Agents: Parallel vs Sequential Patterns | ClaudeFast](https://claudefa.st/blog/guide/agents/sub-agent-best-practices)
- [Claude Code Context Window: Optimize Your Token Usage | ClaudeFast](https://claudefa.st/blog/guide/mechanics/context-management)

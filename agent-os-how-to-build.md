# Agent OS：具體怎麼做

> 來源：Nufar Gaspar 在 The AI Daily Brief 介紹的 Agent OS 框架
> 整理日期：2026-04-27
> 注意：底下的目錄、檔名、prompt 模板是參考實作。Nufar 官方課程 aidbagentos.ai 有完整模板，七層架構與做法是一致的。

---

## 一、核心觀念：為什麼是 OS，不是 agent

**關鍵命題**：agent 工具會收斂，但你的「上下文資產」應該跨工具沉澱。

如果你今天是 Claude Code，明天是 Codex，後天是 Gemini CLI，那些對你個人的記憶、流程、技能不該每換一次工具就重蓋。Agent OS 就是把這些東西抽出來、用純文字（markdown）保存，讓任何 LLM agent 都能掛上去。

實作上它就是一個 git repo，全部都是 markdown 檔，**沒有程式碼也跑得起來**。

---

## 二、推薦的目錄結構（拿 Chief of Staff 為例）

```
~/agent-os/
├── CLAUDE.md                  # 入口，agent 一啟動就讀
├── identity/
│   ├── soul.md                # agent 是誰、人格、規則
│   └── user.md                # 你是誰、你的偏好、溝通風格
├── context/
│   ├── org-chart.md           # 你的公司/團隊現況（含日期）
│   ├── projects.md            # 在跑的專案、優先序
│   ├── people.md              # 重要關係人筆記
│   └── calendar-norms.md      # 行程規則（深度工作時段、會議偏好）
├── skills/
│   ├── triage-inbox/
│   │   ├── SKILL.md
│   │   └── references/email-templates.md
│   ├── prep-meeting/
│   │   ├── SKILL.md
│   │   └── references/agenda-template.md
│   ├── weekly-update/
│   │   └── SKILL.md
│   └── heartbeat/
│       └── SKILL.md           # 排程心跳，下一節說明
├── memory/
│   ├── sessions/              # 每次對話結束的摘要
│   ├── decisions/             # 已做過的決策（不要再問我）
│   └── knowledge/             # 長期知識沉澱
├── connections/
│   ├── mcp.json               # MCP servers 清單（Gmail、GCal、Notion…）
│   └── tools.md               # 文字描述每個工具用途
├── verification/
│   ├── guardrails.md          # 不能做的事（不能寄外信、不能花錢…）
│   └── escalation.md          # 何時要回頭問人類
└── automations/
    ├── morning-brief.md       # 每天 8am 觸發
    └── friday-recap.md        # 每週五 5pm 觸發
```

---

## 三、七層逐一拆解

### Layer 1 — Identity（身分）

這層其實是兩個檔案：**agent 的身分** 與 **你的身分**。

- **`soul.md`**：agent 的角色、溝通風格、絕對守則。範例片段：
  ```
  You are my Chief of Staff. You are concise, direct, and skeptical.
  You never use emoji. You never apologize. You always end with a
  single recommended next action.
  ```
- **`user.md`**：用 **「讓 AI 訪問你」** 的方式產出。Nufar 的關鍵手法：不要自己寫，叫 LLM 拿一份問卷訪談你 30–60 分鐘，再讓它幫你彙整成一份 markdown。問題像「你最討厭哪種會議邀請？」「你週四下午通常在做什麼？」「你願意 agent 替你做什麼決定，到哪個金額為止？」

> **一句口訣**：Identity 是規則，不是描述。寫得越像「規則手冊」越好用。

### Layer 2 — Context（情境/世界觀）

Context 是「**有時效**的事實」。最大的錯誤是把它跟 identity 混在一起。Identity 半年才變一次，context 可能週週都更新。

每份 context 檔最上面要有 `last_updated:` 標記，agent 才知道資料是不是過期。例：

```markdown
# projects.md
last_updated: 2026-04-25

## P0 — Q2 launch (deadline: 2026-06-15)
- Owner: me
- Status: behind on legal review
- Next milestone: ...
```

### Layer 3 — Skills（技能）

每個 skill 是一個資料夾，內含 `SKILL.md`（步驟）+ `references/`（樣板/範例）。Anthropic 的 Agent Skills 規範直接相容。範本：

```markdown
---
name: triage-inbox
description: Triage Gmail inbox into Reply / Delegate / Archive / FYI buckets
inputs: [last_24h_emails]
outputs: triage-report.md
---

## Steps
1. Pull all unread emails from last 24h via Gmail MCP.
2. For each email, classify into one of four buckets using rules in
   references/triage-rules.md.
3. Draft replies for "Reply" bucket, save to drafts/ (do NOT send).
4. Output a single triage-report.md grouped by bucket.

## Guardrails
- Never send. Only draft.
- If an email is from <list in references/vips.md>, always escalate.
```

> 起手只做**三個 skill**就夠：一個做事的（如 triage-inbox）、一個 heartbeat、一個 summary。Nufar 強調不要一次蓋十個，缺什麼再加。

### Layer 4 — Memory（記憶）

Memory 跟 Context 的差別：**Context 是當下世界的快照，Memory 是時間軸上的足跡。**

三個子資料夾各有用途：
- `sessions/2026-04-27.md`：每次對話結束時，叫 agent 自己寫一份「今天做了什麼、決定了什麼、未解決什麼」
- `decisions/`：一個決策一個檔案。下次 agent 想再問你時，先檢索這裡
- `knowledge/`：跨次對話累積的 know-how（如「客戶 X 不喜歡週一被排會」）

寫一個 10 行的 utility skill `log-session.md`，固定在每次對話末尾呼叫，就能自動補進記憶。

### Layer 5 — Connections（連線）

這層就是 MCP。`connections/mcp.json` 列出所有要掛的 MCP server（Gmail、Google Calendar、Notion、Linear、Slack、檔案系統…）。`tools.md` 用人話描述每個工具是幹嘛的，**因為 LLM 選工具時讀的是描述，不是 JSON**。

```markdown
# tools.md
- gmail: read/draft only. Do not send without explicit user approval.
- gcal: read events, create holds (tentative), never send invites.
- notion: read/write to "Chief of Staff" workspace only.
```

### Layer 6 — Verification（驗證/守門）

這是 **最被低估的一層**。內容兩塊：

- **`guardrails.md`**：硬規則。「不准外寄」「單筆消費 > $50 必須問人」「碰到法律字眼立刻停手」
- **`escalation.md`**：何時、怎麼通知你。可以是 Slack DM、email、推 Notion task

Nufar 強調這層要寫得「**可被測試**」──意思是寫得像 unit test 一樣具體，不要寫「謹慎處理客戶資料」這種廢話。

### Layer 7 — Automations（自動化）

前六層讓 agent「**知道怎麼做**」，這層讓它「**自己開始做**」。

兩種觸發模式：

1. **Cron / 排程**：早上 8 點跑 `morning-brief.md`，週五跑 `friday-recap.md`
2. **Heartbeat 模式**（Nufar 特別強調）：一個輕量 skill 每 15–60 分鐘跑一次，檢查條件，符合條件才觸發其他 skill。比 cron 更靈活，因為條件可以是「有沒有新郵件來自 VIP」「日曆上下一場會是不是還沒準備材料」

最後再寫一個 `command-center.md` skill，把所有 automation 的輸出彙整成一份 `status.md`，這樣你早上只看一個檔案就知道昨晚 agent 做了什麼、有什麼要你決定。

---

## 四、起手 30 分鐘最小可行版

如果只給你半小時，照這個順序做：

1. `mkdir ~/agent-os && cd ~/agent-os && git init`
2. 在 Claude Code 下 prompt：「**訪問我 20 個問題，目標是寫出 `identity/user.md`，問我的溝通風格、決策偏好、常做哪些瑣事希望被代勞。問完直接寫檔。**」
3. 讓它根據 user.md 推一份 `identity/soul.md`（chief of staff 角色版本）
4. 寫 `CLAUDE.md`：三行就好──`Read identity/, context/, then check skills/ for what I'm asking.`
5. 寫**一個** skill：`triage-inbox`，加上 Gmail MCP
6. 跑一次。看哪裡爛，補 context 或補 guardrail。再跑

**重點是不要一次寫滿七層**。Nufar 反覆強調：先讓它能跑，再讓它變聰明。每一層都是「缺了才加」，不是「先蓋好再說」。

---

## 五、最容易踩的雷

- **把 Identity 寫成自我介紹文**：要寫成規則。「我是個直接的人」沒用，「不要用『也許』『可能』『或許』這種詞」才有用
- **Skill 寫太長**：一個 skill 應該一頁讀完。超過就拆
- **Memory 不主動寫**：一定要有自動 log-session 的習慣，不然每次都從零開始
- **Verification 是事後才想**：先寫 guardrails 再給工具權限，不要反過來
- **跨工具卻在 skill 裡寫死工具名**：skill 應該描述「動詞」（draft email），讓 connection 層決定用 Gmail 還是 Outlook

---

## 來源

- [How To Build a Personal Agentic Operating System (YouTube)](https://www.youtube.com/watch?v=ntvkDnk_5jA)
- [Frank's World step-by-step write-up](https://www.franksworld.com/2026/04/25/how-to-build-your-personal-agentic-operating-system-a-step-by-step-guide/)
- [MindStudio: Build an Agentic OS in Claude Code](https://www.mindstudio.ai/blog/agentic-operating-system-claude-code-2)
- [MindStudio: Agentic OS Architecture](https://www.mindstudio.ai/blog/agentic-os-architecture-claude-code-business-brain)
- [Nufar Gaspar consulting site](https://www.nufargaspar.com/)
- [Anthropic Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

# Skills / Workflow 設計 Best Practices：持續優化 Eval 的完整指南

## 核心架構：四層系統如何協作

```
CLAUDE.md (永遠載入)
├── 建構指令、測試慣例、架構規則
└── 每個 session 自動載入，< 200 行為佳

.claude/rules/ (永遠/條件式載入)
├── 依路徑匹配的規則 (paths: ["src/api/**/*.ts"])
└── 按主題組織 (code-style.md, api-design.md)

Skills (.claude/skills/)
├── 觸發時機：(1) 使用者輸入 /skill-name (2) Claude 自動判斷相關性
├── 按需載入，不在啟動時全部載入
└── 適合：任務工作流、領域知識、可重用指令

Hooks (.claude/settings.json)
├── 在特定生命週期事件自動觸發
├── 確定性執行（不是「也許」，是「一定」）
└── 適合：政策強制、驗證、自動格式化、稽核
```

---

## 1. Skill 設計原則

### 結構

```
.claude/skills/
  fix-issue/
    SKILL.md          # 主要指令（< 500 行）
    reference.md      # 詳細參考資料
    examples.md       # 範例
```

### SKILL.md 範例

```markdown
---
name: fix-issue
description: 根據 GitHub issue 自動分析、修復並提交 PR
disable-model-invocation: true   # 有副作用的動作，只能手動觸發
---

# Fix Issue Workflow

1. 讀取 issue 內容，理解問題
2. 搜尋相關程式碼
3. 撰寫修復方案
4. 執行測試確認通過
5. 提交 commit 並建立 PR
```

### 關鍵設計決策

| 決策 | 建議 |
|------|------|
| **描述長度** | 前 250 字元最關鍵（會被截斷） |
| **觸發控制** | 有副作用 → `disable-model-invocation: true` |
| **執行隔離** | 需要獨立 context → `context: fork` |
| **工具限制** | 唯讀場景 → `allowed-tools: Read Grep` |
| **參數化** | 支援 `$ARGUMENTS`, `$0`, `$1` |
| **動態注入** | 用 `` !`command` `` 在載入前執行 shell 取得即時資料 |

### Scope 選擇

| Scope | 路徑 | 適用場景 |
|-------|------|----------|
| 個人 | `~/.claude/skills/` | 所有專案通用 |
| 專案 | `.claude/skills/` | 團隊共享，進 git |
| 插件 | `<plugin>/skills/` | 可安裝的外部套件 |
| 企業 | managed settings | 全組織政策 |

---

## 2. Hook 設計：確定性的品質閘門

### 生命週期事件

```
Session:        SessionStart → InstructionsLoaded → ... → SessionEnd
Tool 執行:      PreToolUse → (執行) → PostToolUse / PostToolUseFailure
權限:           PermissionRequest → PermissionDenied
子代理:         SubagentStart → SubagentStop
系統:           Stop, CwdChanged, FileChanged, PreCompact, PostCompact
```

### Hook 類型

| 類型 | 說明 | 適用場景 |
|------|------|----------|
| `command` | Shell 腳本，讀 JSON stdin，寫 stdout/stderr | 格式化、驗證 |
| `http` | POST 事件到遠端 endpoint | 稽核、通知 |
| `prompt` | 單輪 LLM 評估（預設 Haiku） | 快速品質檢查 |
| `agent` | 多輪驗證，有工具存取（60s 預設） | 複雜驗證 |

### Exit Code 語義

| Exit Code | 行為 |
|-----------|------|
| **0** | 繼續執行；stdout 注入 context |
| **2** | 阻擋執行；stderr 回饋給 Claude |
| **其他** | 繼續執行；stderr 僅記錄 |

### 常用 Hook 模式

```jsonc
// .claude/settings.json
{
  "hooks": {
    // 編輯後自動格式化
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "type": "command",
      "command": "prettier --write $CHANGED_FILE"
    }],
    // 阻擋危險指令
    "PreToolUse": [{
      "matcher": "Bash",
      "if": "Bash(rm -rf *)",
      "type": "command",
      "command": "echo '禁止使用 rm -rf' >&2; exit 2"
    }],
    // Compact 後重新注入關鍵 context
    "SessionStart": [{
      "matcher": "compact",
      "type": "command",
      "command": "cat .claude/context-summary.md"
    }]
  }
}
```

---

## 3. Eval 迴圈：人如何介入持續優化

這是最核心的部分。Eval 不是一次性的，而是一個**持續迭代的迴圈**。

### 迴圈全貌

```
    ┌─────────────────────────────────────────────────┐
    │                                                 │
    ▼                                                 │
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────┴─────┐
│ 1. 定義   │───▶│ 2. 執行   │───▶│ 3. 評分   │───▶│ 4. 分析   │
│ 測試案例  │    │ Eval     │    │ 結果     │    │ & 改進   │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
     ▲               │               │               │
     │               │               │               │
     └───── 人類介入 ──┴─── 人類介入 ──┴── 人類介入 ───┘
```

### 階段 1：定義成功標準（人類主導）

**SMART 原則**：
- **Specific**: 「情緒分類正確率」而非「表現好」
- **Measurable**: 用量化指標（F1, accuracy）+ 質性量表（Likert 1-5）
- **Achievable**: 基於 benchmark 和模型能力
- **Relevant**: 對齊你的實際應用需求

**兩個獨立問題**：
1. **輸出品質**：Skill 啟動後，給的答案好嗎？
2. **觸發精準度**：Claude 該啟動 skill 時真的啟動了嗎？

### 階段 2：選擇評分方法

| 方法 | 適用場景 | 取捨 |
|------|----------|------|
| **Code-based** (完全匹配、字串搜尋) | 明確的分類答案 | 缺乏主觀判斷的細微差異 |
| **LLM-based** (Likert 量表、二元分類) | 主觀評估（語調、連貫性） | 需要經驗性評分標準 |
| **Human grading** | 複雜的細微評估 | 慢、貴、無法擴展 |

**具體技術**：

```
完全匹配 ──── 分類、情緒 ──── 比對 golden answer
餘弦相似度 ── 一致性 ──────── embedding 相似度
ROUGE-L ───── 摘要 ──────── 最長共同子序列
LLM Likert ── 語調/風格 ──── 請 Claude 用 rubric 評 1-5 分
二元分類 ──── 安全/隱私 ──── 回應是否包含 PII？是/否
```

### 階段 3：人類介入的五個關鍵時機

```
時機 1：設計測試案例
├── 人類定義邊界案例（edge cases）
├── 人類確保覆蓋真實使用場景
└── 人類決定「什麼算通過」

時機 2：分析失敗模式
├── 自動 eval 找出哪些案例失敗
├── 人類判斷：是 skill 描述不好？是 prompt 不夠明確？還是模型能力限制？
└── 人類歸類失敗原因

時機 3：改寫 Skill 描述
├── 基於失敗分析，人類調整 SKILL.md
├── 重點修改：description（影響觸發）、instructions（影響品質）
└── 可以請 Claude 建議修改，但人類做最終決定

時機 4：驗證自動評分的品質
├── 人類手動評分一小部分（20-50 筆）
├── 對比自動評分結果
└── 若 auto-grader 和人類不一致 → 改進評分標準

時機 5：決定何時「夠好了」
├── 人類設定 pass/fail 門檻
├── 人類權衡：投入更多時間優化 vs 接受當前表現
└── 人類決定是否上線
```

### 階段 4：迭代流程（Skill-Creator Loop）

```python
# 虛擬碼表示完整迴圈
while not meets_threshold(results):
    results = run_evals(skill, test_cases)
    failures = analyze_failures(results)        # 自動 + 人類審查

    if failures.are_description_issues():
        skill.description = improve_description(failures)  # 可用 Claude 輔助
    elif failures.are_instruction_issues():
        skill.instructions = refine_instructions(failures) # 人類主導
    elif failures.are_test_issues():
        test_cases = fix_test_cases(failures)              # 人類主導
    elif failures.are_grading_issues():
        grading_rubric = calibrate_rubric(failures)        # 人類主導

    # 每次迭代後人類審查變更
    human_review(skill)
```

---

## 4. CLAUDE.md 最佳實踐

### 該寫什麼

```markdown
# MyProject

## Build & Test
- `npm run build` — 建構專案
- `npm test` — 執行所有測試
- `npm test -- --grep "pattern"` — 執行特定測試

## Code Style
- 使用 2-space 縮排（不是 tab）
- 函式命名用 camelCase
- 檔案命名用 kebab-case

## Architecture
- src/api/ 下的 handler 都繼承 BaseHandler
- 所有 DB 操作透過 Repository pattern
- 不要直接用 console.log，用 logger 模組

## Common Gotchas
- CI 環境沒有 GPU，測試時跳過 CUDA 相關
- .env.example 有必要的環境變數列表
```

### 不該寫什麼

- Claude 能從程式碼推斷的標準慣例
- 冗長的 API 文件（改用連結）
- 經常變動的資訊
- 「寫乾淨的程式碼」之類自明的指示

### 層級結構

```
/etc/claude-code/CLAUDE.md          # 企業政策（最低優先）
~/.claude/CLAUDE.md                  # 個人全域偏好
./CLAUDE.md                          # 專案共享（進 git）
./CLAUDE.local.md                    # 個人專案設定（.gitignore）
./.claude/rules/*.md                 # 按主題/路徑的細部規則
```

---

## 5. 完整專案範例

### 推薦目錄結構

```
.
├── CLAUDE.md                              # 建構指令、慣例
├── CLAUDE.local.md                        # 個人設定（gitignored）
├── .claude/
│   ├── settings.json                      # Hooks 定義
│   ├── rules/
│   │   ├── code-style.md                  # 格式規範
│   │   ├── testing.md                     # 測試框架說明
│   │   └── api/
│   │       └── design.md                  # REST API 規範 (paths: ["src/api/**"])
│   └── skills/
│       ├── fix-issue/
│       │   └── SKILL.md                   # 修 issue 工作流
│       ├── review-pr/
│       │   └── SKILL.md                   # PR review (context: fork)
│       └── deploy/
│           └── SKILL.md                   # 部署工作流 (disable-model-invocation: true)
└── evals/
    ├── test-cases.jsonl                   # 測試案例
    ├── run-eval.sh                        # 執行腳本
    └── results/                           # 歷史結果
```

### Session 工作流

```
Session 開始
├── /init（首次使用）
├── CLAUDE.md 載入（~500-1000 tokens）
├── Auto memory 載入
├── Skills 描述載入
└── 開始工作

工作中
├── Claude 自動或手動使用 skills
├── Hooks 在每次工具使用時觸發（格式化、驗證）
├── Auto memory 更新
└── Context 逐漸填滿

Context 接近 70%
├── /clear — 任務完成，全部重置
├── /compact — 繼續工作，壓縮歷史
└── Hooks 在 SessionStart 重新注入關鍵 context

Session 結束
├── Hooks 稽核變更
└── Auto memory 保留到下次 session
```

---

## 6. 團隊規模建議

### 小團隊（< 5 人）
- `CLAUDE.md` 在 git root（團隊共享）
- `CLAUDE.local.md` 在 `.gitignore`（個人設定）
- Skills 在 `.claude/skills/`
- Hooks 在 `.claude/settings.json`

### 大型專案 / Monorepo
- Root `CLAUDE.md` + 每個 package 各自的 `CLAUDE.md`
- `.claude/rules/` 按 domain 組織
- `claudeMdExcludes` 跳過不相關的指令
- Skills 用 symlink 指向共享 library

### 企業
- Managed `CLAUDE.md`（透過 admin console）
- Managed settings 強制政策
- 共享 skills 以 plugin 形式分發
- 組織層級的 `.claude/rules/`

---

## 重點摘要

1. **Skills** = 可重用的工作流指令，按需載入
2. **Hooks** = 確定性的品質閘門，永遠執行
3. **CLAUDE.md** = 永遠在場的專案 context
4. **Eval** = 持續迭代的迴圈，不是一次性動作
5. **人類介入** = 設計測試、分析失敗、改寫 skill、校準評分、決定門檻

最重要的一點：**先定義成功標準，再寫 skill，然後用 eval 驗證，看失敗案例來改進** —— 這個迴圈永遠不會停。

---
name: cloud-record
description: 雲端版 /record — 把當前雲端 Claude Code session 整理成記錄，寫到當前 repo 的 .cc-records/{YYYY-MM-DD}-{slug}.md，commit + push 到當前 branch，讓本地 personal_os 的 cloud_record_sync 可以拉回去合進 tasks/{slug}.md。用戶說 /cloud-record、結束前整理這次、cloud record、把這次 push 回去時使用此 skill。
---

# Cloud Record

雲端版的 `/record`。把當前 cloud Claude Code session 整理成 markdown，commit 進當前 repo 的 `.cc-records/` 目錄並 push。本地 `personal_os.core.cloud_record_sync` 之後會掃這個目錄，把內容合進 `personal_os/tasks/{slug}.md`。

## 設計約束

雲端 Claude Code 跑在 ephemeral sandbox：

- ❌ **沒有** `~/Side_project/personal_os/` 本地路徑
- ❌ **沒有** `~/.claude/session_summaries.db` 本地 SQLite
- ❌ **沒有** `CLAUDE_SESSION_ID` 環境變數（雲端用另一套 id space）
- ✅ **有** 當前 worktree 可寫
- ✅ **有** `git commit` + `git push` 權限
- ✅ **有** 當前 branch name（`claude/<slug>-XxXxX`），可從 `git rev-parse --abbrev-ref HEAD` 拿

所以 cloud-record 只做兩件事：**寫一份 markdown 到 worktree** + **push 到當前 branch**。其餘交給本地 sync。

## 什麼時候用

- 用戶說 `/cloud-record`
- 用戶說「結束前整理這次 / 把這次 push 回去 / cloud record」
- 雲端 task 收尾、即將開 PR 之前

## 用法

| 指令 | 效果 |
|------|------|
| `/cloud-record` | 從對話 + branch 名推斷 slug，寫 `.cc-records/{date}-{slug}.md` |
| `/cloud-record <slug>` | 用戶指定 slug（kebab-case） |

## 工作流

### 1. 抓 context（git 命令）

```bash
BRANCH=$(git rev-parse --abbrev-ref HEAD)
REPO=$(basename "$(git rev-parse --show-toplevel)")
DATE=$(date +%Y-%m-%d)
```

### 2. 決定 slug

- 如果用戶給了 slug，直接用
- 否則：從 branch name 抽（`claude/personal-os-research-680e9` → `personal-os-research`）
  - 去掉 `claude/` 前綴
  - 去掉尾端 `-XxXxX`（5 字元 random suffix）
- 如果 branch 不是 `claude/*` 格式（用戶手動建的），從對話主題推 kebab-case slug

### 3. 推斷 frontmatter 與內容

從本次對話抽：
- `next_action`：可執行的一句話 ≤ 30 字
- `status`：預設 `in_progress`；用戶說「做完了」→ `done`；「卡住」→ `paused` + `blocked_by`
- `related_files`：本次對話動到 / 引用到的檔案路徑（限本 repo 內）
- `tags`：2-3 個分類標籤

### 4. 寫檔案

路徑：`.cc-records/{YYYY-MM-DD}-{slug}.md`

如果同檔名已存在（同一天同一 slug 寫第二次），**追加 session block**，不覆蓋。

```markdown
---
slug: <slug>
source: cloud
cloud_repo: <REPO>
cloud_branch: <BRANCH>
session_date: <DATE>
created: <DATE>
status: <in_progress|done|paused>
next_action: <一句話>
related_files:
  - <path/in/repo>
tags: [<tag1>, <tag2>]
---

# {Task Title}

## Context

這個 cloud session 在做什麼，1-3 句話。

## Sessions

### {DATE} Cloud Session ({BRANCH})

#### 關鍵發現
- ...

#### 檔案清單
- `path/to/file` — 用途說明

#### 待辦
- [ ] ...

#### 後續行動
1. ...
```

### 5. Commit + push

```bash
git add ".cc-records/{DATE}-{slug}.md"
git commit -m "cloud-record: {slug} ({DATE})"
git push origin "$BRANCH"
```

Commit message 前綴固定 `cloud-record:`，方便本地 sync 在 git log 用 prefix 過濾，也讓 PR diff 一眼看出是 record 而非實質改動。

### 6. 回報用戶

```
✅ 雲端記錄已 push

**檔案**：`.cc-records/{DATE}-{slug}.md`
**Branch**：{BRANCH}
**Next**：{next_action}

本地下次跑 `python -m core.cloud_record_sync` 會把這份合進 `personal_os/tasks/{slug}.md`。
```

## 規則

- **只寫 `.cc-records/`，不動 repo 其他內容**：cloud-record 是 metadata，不該污染主線
- **同日同 slug 追加，不覆蓋**：跟本地 record 的 Path B 一致
- **commit 前綴固定 `cloud-record:`**：本地 sync 用這個過濾
- **slug 跟 branch 對齊**：避免本地拉回後撞名後又要解析
- **next_action 必須可執行**：「Q1 財報後判斷 X」OK，「研究一下 X」不 OK
- **不要把對話原文整段倒進去**：抽 key findings

## 不要這樣做

- ❌ 不要嘗試 import `personal_os.core` 任何東西（雲端讀不到）
- ❌ 不要嘗試寫 `~/.claude/session_summaries.db`（雲端沒這個檔案）
- ❌ 不要在 `.cc-records/` 以外的地方寫檔
- ❌ 不要用中文檔名
- ❌ 不要在同個 commit 裡夾雜實質程式改動跟 record（混在一起本地 sync 會誤判）

## Schema 與本地 record 的關係

| 欄位 | `personal_os/tasks/{slug}.md` | `.cc-records/{date}-{slug}.md` |
|------|------------------------------|--------------------------------|
| `slug` | ✅ | ✅ |
| `status` | ✅ | ✅ |
| `created` | ✅ | ✅ |
| `last_session` | ✅（本地維護） | ❌（雲端不知道本地最後一次是哪天） |
| `next_action` | ✅ | ✅ |
| `source` | ❌（隱含 local） | ✅（固定 `cloud`） |
| `cloud_repo` | ❌ | ✅ |
| `cloud_branch` | ❌ | ✅ |
| `session_date` | ❌ | ✅ |

本地 sync 拉進去後：
- `personal_os/tasks/{slug}.md` 的 frontmatter 不會有 `source/cloud_*`（那些只屬於 cloud snapshot）
- 但會在 ## Sessions block 標題加 `(cloud:{branch})` 讓人類一眼分辨
- `session_summaries.db` 寫入時 source = `cloud:<branch>`，跟本地 `record` / `auto` 區分

---
slug: cloud-record-pipeline-test
source: cloud
cloud_repo: Learning
cloud_branch: claude/personal-os-research-680e9
session_date: 2026-05-17
created: 2026-05-17
status: in_progress
next_action: 驗 end-to-end 後決定要不要分發到其他 repo
related_files:
  - .claude/skills/cloud-record/SKILL.md
  - .cc-records/README.md
tags: [cloud-record, personal-os, pipeline-test]
---

# Cloud Record Pipeline Smoke Test

## Context

第一次跑通 cloud-record skill + 本地 cloud_record_sync 的 end-to-end pipeline。在 Learning repo 試做，先驗證讀寫格式都對上，再決定要不要分發到 crewai_xhs / investment_note 等雲端活躍 repo。

## Sessions

### 2026-05-17 Cloud Session (cloud:claude/personal-os-research-680e9)

#### 關鍵發現
- cloud-record skill 跟本地 record 在 frontmatter 上有 source / cloud_repo / cloud_branch 三個獨有欄位
- 同日同 slug 追加邏輯需要由本地 sync 端負責，cloud 端只負責寫 snapshot
- session_summaries.db source 用 `cloud:<branch>` 區分，跟本地 `record` / `auto` 分流

#### 檔案清單
- `.claude/skills/cloud-record/SKILL.md` — 雲端版 skill 定義
- `.cc-records/README.md` — 目錄用途說明

#### 待辦
- [ ] 確認 sync 正確生成 `personal_os/tasks/cloud-record-pipeline-test.md`
- [ ] 確認 `session_summaries.db` 有寫入對應 row
- [ ] 確認 state file 記住已 sync 的 blob sha

#### 後續行動
1. 跑 `python -m core.cloud_record_sync --dry` 看會不會被掃到
2. 跑實際 sync，檢查 tasks/ 跟 db 結果
3. 如果 OK，計畫分發 skill 到 crewai_xhs / investment_note

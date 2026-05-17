# `.cc-records/`

Cloud Claude Code session 寫的 record snapshot。

每個檔案是一次雲端 session 的 markdown 記錄，格式由 `.claude/skills/cloud-record/SKILL.md` 定義，由雲端 agent 跑 `/cloud-record` 產生。

本地 `personal_os` 的 `core.cloud_record_sync` 會掃這個目錄，把內容合進 `~/Side_project/personal_os/tasks/{slug}.md`。

## 檔名規則

```
{YYYY-MM-DD}-{kebab-case-slug}.md
```

例：`2026-05-17-personal-os-research.md`

## 不要手動編輯

如果要修正內容，請改本地 `personal_os/tasks/{slug}.md`。這個目錄是雲端寫入專用（write-only from cloud, read-only for local sync）。

# Admissions Schema

## `candidates_YYYY-MM-DD.jsonl`

每行一筆 regex 命中的候選（待人工 review）。

| 欄位 | 類型 | 說明 |
|---|---|---|
| `ts` | string (ISO) | assistant message timestamp |
| `session_id` | string | Claude Code session UUID |
| `uuid` | string | assistant message UUID |
| `parent_uuid` | string \| null | 上一則訊息（通常是 user 或 tool_result）UUID — 想回放上下文時順藤摸瓜 |
| `cwd` | string | 當時的 working dir → 看出在哪個專案 / 領域出錯 |
| `model` | string | 例 `claude-opus-4-7`。未來擴 multi-model 時用 `actor` 欄位區分 |
| `transcript_path` | string | jsonl file 完整路徑（debug 用） |
| `pattern_tag` | string | regex 分類（`zh_apology` / `en_admit` / `zh_self_correct` 等） |
| `matched_phrase` | string | regex 命中的原文片段 |
| `snippet` | string | 命中前後各 200 字 context（review 時快速判斷用） |
| `is_real_admission` | bool \| null | **人工 review 填**：true = 真錯，false = 客套 / 誤判 |
| `error_type` | string \| null | `factual` / `logical` / `misread_file` / `hallucination` / `misinterpreted_intent` / `wrong_tool_use` / `other` |
| `root_cause` | string \| null | 沒讀夠檔 / 太早結論 / cache miss / 誤判 user intent / 其他 |
| `fix` | string \| null | 後來怎麼修正（一句話） |

## `admissions.jsonl`（promote 後的真實 admission）

跟 candidates schema 一致，但 `is_real_admission = true` 且後 3 欄填完。

從 candidates promote 的流程：jq 過濾 + 手動 append（review 時順手），或寫個 `tools/promote.py`（後續再說）。

## 設計考量

1. **placeholder 欄位放 `null`**：方便 review 時 `jq 'select(.is_real_admission == null)'` 過濾未審核
2. **保留 `parent_uuid`**：將來想回放「Claude 為什麼會錯」可以順藤摸瓜
3. **`cwd` 記下**：error pattern 可能跟領域強相關（投資 vs xhs vs coding）
4. **`pattern_tag` 分類**：「en_apology」很多是客套不是真錯，先標好讓 review 時可快速跳過該整類

## Multi-model 擴展（未來）

目前只抓 **Claude 主對話 assistant text**。未來：

- **Codex** 透過 `Agent` / `Task` 呼叫 → 結果出現在 `tool_result` block 內
- **Gemini** 透過 Bash `gemini` CLI → output 出現在 Bash 的 `tool_result`

擴展方式：
- 新增 `actor` 欄位（`claude_main` / `codex_via_agent` / `gemini_via_bash`）
- 寫 sibling script `scan_admissions_tool_results.py`（不動既有）
- 同一份 `admissions.jsonl` 累積三方資料，最後 synthesize 時 group by `actor`

## 隱私

`runs/*.jsonl` 含對話 raw 片段（snippet 200 字 + cwd 路徑 + transcript_path），**不入 git**。已在 `.gitignore` 擋。

要 share / publish 時，先寫 `tools/anonymize.py`（todo）把 cwd / ticker / 私名抹掉再 export。

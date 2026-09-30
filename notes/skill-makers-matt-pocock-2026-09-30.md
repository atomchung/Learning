# Skill makers 研究筆記：poteto / dexhorthy / emilkowalski

> 觸發：Matt Pocock 2026-09-30（台北）點名三人「top skill makers」  
> 來源貼：https://x.com/mattpocockuk/status/2105022638368403658  
> 狀態：學習筆記（未升級成共用 skill；之後整體改 skill 時再拿這份當 checklist）  
> 日期：2026-09-30

## 一句話

好 skill 是給**下一個冷啟動的 agent**讀的決策文件，不是給人看的教學文；description 寫清 WHEN，body 只留會改決策的句子。

## 三人各拿什麼

### @poteto（Lauren Tan）— pstack

- 位置：https://github.com/cursor/plugins/tree/main/pstack
- Description = WHAT + WHEN + 觸發詞；多數 workflow 設 `disable-model-invocation: true`
- Router：playbook 步驟原樣進 todolist，再委派 leaf；**委派不重述**
- 穩定 rule id（`unslop`），刪規則留編號空隙，方便他 skill 引用
- 產出寫給 cold next agent；**Interview the repo, not the user**；生成物沒實跑＝draft
- 重複教訓 → lint／script／metadata，少再寫一段文字（`principle-encode-lessons-in-structure`）
- Authoring 心法：*When in doubt, delete. Keep only prose that changes a decision.*

### @dexhorthy（Dex Horthy / HumanLayer）

- Skills：https://github.com/humanlayer/skills ；slopfiles：https://github.com/dexhorthy/slopfiles
- Meta：ACE https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md
- Description 用 WHEN；必要時寫死「Only use when the user explicitly invokes…」
- `improve-claude-md`：條件加權、砍 linter 能管的、砍 snippet 改 path；Input→Output→Why-cut
- `show-me`：最小視覺形狀（tree／mermaid／diff），非長散文
- 先讀 repo 再訪談；每階段有 completion criterion；本地可跑再開 CI
- ACE：intentional compaction；人審槓桿在 research／plan，不在每行 code

### @emilkowalski（Emil Kowalski）

- Skills：https://github.com/emilkowalski/skills
- Meta：https://emilkowal.ski/ui/agents-with-taste
- Description 寫兄弟邊界（animate vs review-animations vs improve-animations）
- 表／flowchart 編碼品味（easing、duration、Before|After|Why）
- Hard rules + 有序 sequence；**zero lines of code sometimes = success**
- ONE thing；**default beats menu**；計畫必須 cold-readable for executor with zero taste

## 跨切最佳實踐（之後改我們 skill 用）

1. `description` 必含 WHEN（＋何時不要／用哪個兄弟 skill）
2. 只留會改變決策的句子；當疑則刪
3. Non-goals／一 skill 一職
4. 有序步驟 + 可驗證；生成物 cold-readable 且實跑一次
5. 表／flowchart／穩定 rule id／腳本 ＞ 散文
6. 條件化注意力（窄 if／手動觸發）
7. 委派不重述；compose 用 path，不複製規則
8. 證據與品味分開；人機槓桿放在 description／gates／plan
9. 共用 skill 保持 GENERIC（無 assistant／channel／repo 死綁）
10. Default beats menu；砍 toolable 規則（formatter／CI 能做的別寫進 skill）

## 反模式

- 空 WHEN、空話 best practices
- 把 linter 規則寫進 skill
- 大段易腐 snippet
- 一 skill 多職
- 只口頭「會記住」、生成不實跑
- 菜單式選項
- 共用 body 塞內部 tool／channel id
- 為高頻操作加多餘儀式

## 對我們現況

- 既有筆記：[skills-workflow-best-practices](./skills-workflow-best-practices.md)（偏 Claude 四層架構＋eval）
- Grok Bot managed `skill-authoring`：強在「怎麼 save」，弱在「怎麼寫好」
- User skill 狼友小站：WHEN／Non-goals／具體 selector 已對齊較好
- **下一步（未做）**：之後整體改 skill 時，用下方草稿當 meta checklist；暫不單獨存成共用 `skill-writing`

## 附錄：草稿 `skill-writing`（待整體迭代時再用）

```markdown
---
name: skill-writing
description: >-
  Use when creating, rewriting, reviewing, or splitting a SKILL.md (or when
  deciding whether a repeated multi-step task should become a skill). Also use
  for "/skill-writing", "write a skill", "improve this skill", or "skill best
  practices". Not for one-off tasks that will never recur.
---

# Skill writing

Write skills other agents can load cold mid-task. Prefer short, decision-changing prose. When in doubt, delete.

## Format

YAML frontmatter + markdown body. Required keys:

- `name`: lowercase letters, numbers, hyphens; match the skill folder if the host requires it.
- `description`: one tight block that states **what** the skill does and **when** to use it (triggers, synonyms, and when *not* to use it / which sibling to use instead).

Optional host keys (`disable-model-invocation`, `paths`, icons, …) may exist. Preserve unknown keys when editing; do not invent host-specific keys unless you know the host.

## Description checklist

A good description answers all of:

1. **What** outcome this skill produces.
2. **When** to reach for it (user phrasing + situations), not only the slash name.
3. **When not** / sibling skills ("For review use X; for implement use Y") when confusion is likely.
4. Stay under ~600 characters when possible; front-load the trigger.

Bad: `Helps with animations.`  
Good: `Build a UI animation from scratch in decision order (whether to animate, purpose, tool, properties, curve, duration). Use when asked to animate or add motion. For critiquing existing motion use review-animations; for a whole-codebase audit use improve-animations.`

## Body structure (default)

Use only the sections that earn their place:

1. **One-line job** — what success looks like.
2. **Non-goals / scope** — what this skill refuses to do.
3. **Hard rules** — numbered, stable ids if other skills will cite them. Gaps OK after deletions.
4. **Procedure** — ordered steps. Each step ends in something checkable when the work is consequential.
5. **Decision aids** — tables, flowcharts, Before|After|Why. Prefer these over essays.
6. **Examples** — one minimal happy path; optional Input→Output→Why-we-cut for rewrite skills.
7. **References / helpers** — paths to scripts, templates, or sibling skills. Do not restate them.
8. **Anti-patterns** — concrete failure modes the agent should stop on.

Skip motivational prose. Explain *why* only when the rule is confusing without it.

## Authoring rules

1. **ONE job per skill.** If you need review and implement and audit, split.
2. **Generic shared skills.** Keep assistant-specific tool ids, channel ids, repo urls, account names, and personal secrets out of the shared body. Those belong in a routine, a local override, or a project-local skill.
3. **Encode lessons in structure.** If you write the same instruction twice, prefer a lint, test, script, template, or metadata flag. Text is the fallback when judgment is required — then add a failure example.
4. **Interview the world before the human** when the skill generates artifacts: read the repo/UI/docs first; ask only what you cannot observe.
5. **Write for the next cold reader.** Generated skills and plans must name exact commands, selectors, paths, and proof standards — no "as discussed above".
6. **Prove once.** If the skill generates a harness or recipe, run it end-to-end before calling it done.
7. **Progressive disclosure.** Keep the main SKILL.md lean; put long catalogs in `references/` and tell the agent when to open them.
8. **Compose, don't copy.** Point at sibling skills by name/path instead of duplicating rules.
9. **Default beats menu.** When taste or policy has a clear answer, state it; do not offer a buffet of options.
10. **Cut toolable rules.** Anything a formatter, typechecker, or CI check can enforce does not belong as skill prose.

## Review checklist (before saving)

- [ ] `name` + `description` present; description states WHEN
- [ ] Non-goals or explicit scope boundary
- [ ] Steps are ordered; consequential steps have a check
- [ ] No assistant-specific ids in a skill meant to be shared
- [ ] No stale code dumps; paths instead
- [ ] Sibling skills cross-linked instead of duplicated
- [ ] If generative: cold-readable output + one successful dry run
- [ ] Could delete 20% of sentences without losing a decision? If yes, delete

## When not to make a skill

- Single-use instructions
- Pure style that a linter already covers
- A preference that belongs in a one-line user rule
- A workflow that is really three jobs (split first)

## Reply after authoring

Summarize: skill name, when it fires, key design choices, validation notes (what you ran or deliberately skipped).
```

## 主要來源

- Matt：https://x.com/mattpocockuk/status/2105022638368403658
- pstack：https://github.com/cursor/plugins/tree/main/pstack
- HumanLayer skills：https://github.com/humanlayer/skills
- ACE：https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md
- Emil skills：https://github.com/emilkowalski/skills
- Agents with Taste：https://emilkowal.ski/ui/agents-with-taste
- Cursor skills docs：https://cursor.com/docs/skills

## 相關

- [skills-workflow-best-practices](./skills-workflow-best-practices.md)
- [agent-context-best-practices](./agent-context-best-practices.md)
- [warp-self-improving-skills](./warp-self-improving-skills.md)

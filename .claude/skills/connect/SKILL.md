---
name: connect
description: "Wrap up a learning conversation: auto-summarize what was discussed, save it to the learning journal, and connect it to past learnings. Use when the user finishes a topic, says 'OK done', '差不多了', '幫我整理', or wants to move on."
allowed-tools: Bash(python3 *) Read Write Edit
argument-hint: [optional-title-override]
---

## Task

Automatically summarize this conversation's learning, save it, and show connections to past entries.

## Steps

### 1. Auto-analyze this conversation

Without asking the user anything, extract:
- **Title**: The main topic in a concise phrase
- **Tags**: 3-6 keyword tags (prefer reusing existing tags for consistency)
- **Summary**: 2-3 sentence summary of what was discussed and learned
- **Questions**: The key questions the user asked during this conversation
- **Key takeaways**: The most important insights (bullet points)
- **Extensions**: Natural follow-up directions that came up but weren't explored
- **Confidence**: Estimate 1-5 based on how deep the conversation went

### 2. Check existing learnings for context

```bash
python3 scripts/capture_learning.py --list 2>/dev/null
```

- Look at existing tags to reuse consistent terminology
- Check if this topic was discussed before (update vs new entry)

### 3. Save the entry

```bash
python3 scripts/capture_learning.py \
  --title "AUTO_EXTRACTED_TITLE" \
  --tags "tag1,tag2,tag3" \
  --summary "AUTO_EXTRACTED_SUMMARY" \
  --questions "Q1;Q2;Q3" \
  --keypoints "AUTO_EXTRACTED_KEYPOINTS" \
  --extensions "AUTO_EXTRACTED_EXTENSIONS" \
  --confidence N
```

If the user provided $ARGUMENTS, use that as the title instead.

### 4. Show connections

```bash
python3 scripts/review.py --connections 2>/dev/null
```

### 5. Present to user (concisely)

Show a brief summary:

```
已記錄: [title]
Tags: [tags]
Confidence: N/5

和過去學習的關聯:
  ↔ [related entry 1] (shared: tag1, tag2)
  ↔ [related entry 2] (shared: tag3)

下次可以延伸:
  → extension 1
  → extension 2
```

Do NOT show the raw command output. Summarize it nicely.

## Important

- **Do NOT ask the user to fill in anything.** Extract everything automatically from the conversation.
- Keep the output short — this is a wrap-up, not a lecture.
- If the conversation covered multiple unrelated topics, create separate entries.
- Use the same language the user used in the conversation.

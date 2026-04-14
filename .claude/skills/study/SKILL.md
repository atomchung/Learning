---
name: study
description: "Start a focused study session. Checks what needs review, picks the best topic, and guides interactive learning with questions and explanations. Use when the user wants to study or learn something."
disable-model-invocation: true
allowed-tools: Bash(python3 *) Read Write Edit
argument-hint: [topic-or-subject]
---

## Task

Guide the user through a focused study session.

## Steps

### 1. Determine what to study

**If user specifies a topic ($ARGUMENTS):**
- Search existing learnings: `python3 scripts/capture_learning.py --search "$ARGUMENTS"`
- If found: review and deepen that topic
- If not found: this is a new topic to explore

**If no topic specified:**
- Check what's due for review: `python3 scripts/review.py`
- Pick the most overdue or lowest-confidence topic
- Suggest it to the user and ask for confirmation

### 2. Review existing knowledge

If this is a previously learned topic:
- Read the learning entry file to refresh context
- Summarize what was learned before
- Ask 2-3 questions to test retention

### 3. Interactive learning

- Explain concepts using the user's interests (check their interest profile)
- Ask questions and wait for answers — don't give answers immediately
- Provide hints if the user is stuck
- Use real-world examples and analogies

### 4. After the session

Run `/capture` to record what was learned or updated in this session.

If the user reviewed an existing topic:
```bash
python3 scripts/review.py --mark-reviewed ENTRY_ID
```

## Important

- Keep study sessions focused: one topic at a time
- Use the Socratic method: guide through questions, don't just lecture
- Match the user's language and pace
- Connect new learning to what they already know (check their learnings)

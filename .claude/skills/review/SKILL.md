---
name: review
description: "Show your learning review dashboard: what needs reviewing today, upcoming reviews, and low-confidence topics. Use at the start of a session or when the user asks what to study/review."
disable-model-invocation: true
allowed-tools: Bash(python3 *)
---

## Task

Show the user their learning review status and help them decide what to study.

## Steps

1. **Run the review dashboard**:
   ```bash
   python3 scripts/review.py
   ```

2. **Interpret the results** for the user:
   - If there are overdue reviews (!!!) → strongly recommend reviewing those first
   - If there are upcoming reviews → mention them casually
   - If there are low-confidence topics → suggest deeper study

3. **For overdue items**, offer to:
   - Do a quick recap of that topic right now
   - Ask the user quiz questions to test retention
   - Mark it as reviewed if they remember it well

4. **After reviewing**, mark completed reviews:
   ```bash
   python3 scripts/review.py --mark-reviewed ENTRY_ID
   ```

5. If the user wants to do a review session, pick the most overdue topic and:
   - Summarize what they learned (read the entry file)
   - Ask 2-3 questions to test understanding
   - Based on their answers, suggest if confidence should go up or down

## Language

Respond in the same language the user has been using in this session.

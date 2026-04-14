---
name: explore
description: "Based on your past learning history and interests, suggest new topics to explore. Use at the start of a session when the user wants inspiration for what to learn next, or says 'what should I look into?', '今天學什麼?', '有什麼新東西可以看?'"
disable-model-invocation: true
allowed-tools: Bash(python3 *) Read WebSearch
---

## Task

Analyze the user's learning history and suggest new topics to explore.

## Steps

### 1. Load learning history and interest profile

```!
python3 scripts/review.py --interests 2>/dev/null || echo "No entries yet"
```

```!
python3 scripts/capture_learning.py --list 2>/dev/null || echo "No entries yet"
```

```!
python3 scripts/review.py 2>/dev/null || echo "No reviews"
```

### 2. Analyze and recommend

Based on the data above:

**A. Check overdue reviews first.** If something is overdue, mention it briefly:
- "上次你研究了 X，已經 N 天沒回顧了，要不要先快速聊一下？"

**B. Find extension directions** from existing entries:
- Read the "延伸方向" section of recent entries
- These are directions the user themselves said they want to explore

**C. Discover new angles** by combining the user's top interest tags:
- If they're interested in "AI" and "教育", suggest something at the intersection they haven't explored
- If they keep returning to a theme, suggest going deeper

**D. Suggest 2-3 options**, ranked by:
1. Unfinished extensions from past learnings (highest priority)
2. Cross-topic connections worth exploring
3. Completely new but related directions

### 3. Present suggestions

For each suggestion:
- What it is (1 sentence)
- Why it connects to their interests (which past learnings link to it)
- One provocative question to spark curiosity

Ask the user which one they want to dive into, or if they have something else in mind.

## Format

Keep it conversational and short. Don't dump walls of text. 2-3 options, 2-3 lines each.

## Language

Respond in the same language the user has been using.

---
name: connect
description: "Analyze connections between your learnings, show your interest profile, or search past topics. Use when the user asks about patterns in their learning, wants to find past topics, or says 'what have I learned about X?'"
allowed-tools: Bash(python3 *) Read
argument-hint: [search-keyword]
---

## Task

Help the user explore their learning history and discover connections.

## Modes

### If user provides a search keyword ($ARGUMENTS):
```bash
python3 scripts/capture_learning.py --search "$ARGUMENTS"
```
Then read the matching entry files to give a richer summary.

### If user asks about connections / patterns:
```bash
python3 scripts/review.py --connections
```
Explain the connections in plain language and suggest cross-topic explorations.

### If user asks about their interests / learning profile:
```bash
python3 scripts/review.py --interests
```
Provide insights about their learning patterns and suggest directions.

### Default (no specific request):
Run all three and give a concise overview:
```bash
python3 scripts/capture_learning.py --list
python3 scripts/review.py --connections
python3 scripts/review.py --interests
```

## After showing results

- Suggest specific questions that bridge two related topics
- Highlight topics that could benefit from revisiting
- Point out knowledge clusters and potential new directions

## Language

Respond in the same language the user has been using.

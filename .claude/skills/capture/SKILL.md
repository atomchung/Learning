---
name: capture
description: "Record what you learned from this conversation into your knowledge journal. Use when: the user finishes exploring a topic, asks to save/record what they learned, or says they're done with a topic. Auto-invokes when conversation covers substantial learning."
allowed-tools: Bash(python3 *) Read Write Edit
argument-hint: [topic-title]
---

## Task

Capture what was learned in this conversation into the learning journal.

## Steps

1. **Analyze the conversation** to identify:
   - The main topic(s) discussed
   - Key questions the user asked
   - Important takeaways and insights
   - Connections to previous learnings
   - Potential follow-up directions

2. **Check existing learnings** for duplicates or related entries:
   ```!
   python3 scripts/capture_learning.py --list 2>/dev/null || echo "No entries yet"
   ```

3. **Determine appropriate tags** from the conversation content. Use consistent tags that connect to past learnings.

4. **Assess confidence level** (1-5):
   - 1 = Just heard about it
   - 2 = Shaky understanding
   - 3 = OK, got the basics
   - 4 = Good grasp
   - 5 = Could teach it

5. **Run the capture command**:
   ```bash
   python3 scripts/capture_learning.py \
     --title "TOPIC_TITLE" \
     --tags "tag1,tag2,tag3" \
     --summary "One-paragraph summary of what was learned" \
     --questions "Question 1;Question 2;Question 3" \
     --keypoints "Key takeaway points" \
     --extensions "Follow-up directions to explore" \
     --confidence N
   ```

6. **Show the user** what was captured, any auto-discovered connections, and suggest what to explore next.

If the user provides a topic title as argument ($ARGUMENTS), use that. Otherwise, infer the best title from the conversation.

## Important

- Write summaries and keypoints in the **same language** the user used in the conversation
- Tags should be short, reusable keywords (prefer existing tags over new ones)
- Always include both broad tags (AI, 教育) and specific tags (Alpha-School, EdTech)
- If the conversation covered multiple distinct topics, create separate entries for each

#!/usr/bin/env python3
"""
Capture Learning - 將對話中的學習自動記錄到知識圖譜
====================================================
設計給「探索式學習」：你問了什麼、學到什麼、和之前學的有什麼關聯。

Usage:
    # 記錄一次學習（最常用）
    python3 scripts/capture_learning.py \\
        --title "Alpha School AI 教育模式" \\
        --tags "AI,教育,EdTech" \\
        --related "coding-agents-comparison" \\
        --summary "Alpha School 用 AI 取代教師，2 小時完成一天學科..."

    # 快速記錄（只需標題，其餘之後補）
    python3 scripts/capture_learning.py --title "Bloom 2-Sigma 問題"

    # 列出所有已記錄的學習
    python3 scripts/capture_learning.py --list

    # 搜尋過去學過的主題
    python3 scripts/capture_learning.py --search "AI"
"""

import argparse
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEARNINGS_DIR = REPO_ROOT / "learnings"


def slugify(text: str) -> str:
    """Convert text to a filename-safe slug."""
    # Keep Chinese characters, alphanumeric, replace spaces/special with hyphens
    slug = re.sub(r'[^\w\u4e00-\u9fff\-]', '-', text.lower())
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug[:80]


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    meta = {}
    for line in text[3:end].strip().split("\n"):
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            items = val[1:-1]
            meta[key] = [v.strip() for v in items.split(",")] if items.strip() else []
        elif val.isdigit():
            meta[key] = int(val)
        elif val in ("", "null"):
            meta[key] = None
        else:
            meta[key] = val
    return meta


def load_all_learnings() -> list[dict]:
    """Load all learning entries."""
    entries = []
    if not LEARNINGS_DIR.exists():
        return entries
    for md in sorted(LEARNINGS_DIR.rglob("*.md")):
        with open(md, "r", encoding="utf-8") as f:
            content = f.read()
        meta = parse_frontmatter(content)
        if meta.get("id"):
            meta["_file"] = str(md.relative_to(REPO_ROOT))
            # Extract body (after second ---)
            parts = content.split("---", 2)
            meta["_body"] = parts[2].strip() if len(parts) > 2 else ""
            entries.append(meta)
    return entries


def find_related(entries: list[dict], tags: list[str], exclude_id: str = "") -> list[dict]:
    """Find entries that share tags with the given tags list."""
    related = []
    for e in entries:
        if e["id"] == exclude_id:
            continue
        e_tags = set(e.get("tags", []))
        overlap = e_tags & set(tags)
        if overlap:
            related.append({"entry": e, "shared_tags": list(overlap),
                           "score": len(overlap)})
    related.sort(key=lambda x: x["score"], reverse=True)
    return related


def capture(args):
    """Capture a new learning entry."""
    LEARNINGS_DIR.mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()
    slug = slugify(args.title)
    entry_id = f"{today}-{slug}"
    filename = LEARNINGS_DIR / f"{entry_id}.md"

    # Parse tags
    tags = [t.strip() for t in args.tags.split(",")] if args.tags else []

    # Parse related (manual links)
    related = [r.strip() for r in args.related.split(",")] if args.related else []

    # Load existing entries to find auto-related
    existing = load_all_learnings()
    auto_related = find_related(existing, tags, entry_id)

    # Merge manual + auto related
    all_related_ids = list(set(related + [r["entry"]["id"] for r in auto_related[:5]]))

    # Build questions list
    questions = [q.strip() for q in args.questions.split(";")] if args.questions else []

    # Write the file
    content = f"""---
id: {entry_id}
title: {args.title}
date: {today}
tags: [{', '.join(tags)}]
related: [{', '.join(all_related_ids)}]
confidence: {args.confidence}
review_count: 0
last_review: {today}
source: conversation
---

# {args.title}

## 摘要
{args.summary if args.summary else '(待補)'}

## 關鍵問題
{chr(10).join(f'- {q}' for q in questions) if questions else '- (待補)'}

## 學到的重點
{args.keypoints if args.keypoints else '(待補)'}

## 延伸方向
{args.extensions if args.extensions else '(待探索)'}
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nCaptured: {args.title}")
    print(f"  File: {filename.relative_to(REPO_ROOT)}")
    print(f"  Tags: {tags}")
    print(f"  Confidence: {args.confidence}/5")

    if auto_related:
        print(f"\n  Auto-discovered connections:")
        for r in auto_related[:5]:
            e = r["entry"]
            print(f"    -> {e['title']} (shared: {', '.join(r['shared_tags'])})")

    # Show reminder about what to review
    due = find_due_reviews(existing)
    if due:
        print(f"\n  Reminder: {len(due)} topic(s) due for review. "
              f"Run: python3 scripts/review.py")


def list_entries(args):
    """List all learning entries."""
    entries = load_all_learnings()
    if not entries:
        print("No learning entries yet. Use --title to capture your first one!")
        return

    # Group by month
    months = {}
    for e in entries:
        month = e.get("date", "unknown")[:7]
        months.setdefault(month, []).append(e)

    total = len(entries)
    tags_all = set()
    for e in entries:
        tags_all.update(e.get("tags", []))

    print(f"\n{'='*55}")
    print(f"  Learning Journal: {total} entries, {len(tags_all)} unique tags")
    print(f"{'='*55}\n")

    for month in sorted(months.keys(), reverse=True):
        print(f"  [{month}]")
        for e in sorted(months[month], key=lambda x: x.get("date", ""), reverse=True):
            conf = e.get("confidence", "?")
            tags = ", ".join(e.get("tags", [])[:3])
            reviewed = e.get("review_count", 0)
            print(f"    {e.get('date','')} | {e['title']}")
            print(f"             confidence: {conf}/5  reviews: {reviewed}  tags: {tags}")
        print()


def search_entries(args):
    """Search learning entries by keyword."""
    entries = load_all_learnings()
    query = args.search.lower()
    results = []

    for e in entries:
        score = 0
        title = e.get("title", "").lower()
        tags = [t.lower() for t in e.get("tags", [])]
        body = e.get("_body", "").lower()

        if query in title:
            score += 10
        for t in tags:
            if query in t:
                score += 5
        if query in body:
            score += 2

        if score > 0:
            results.append((score, e))

    results.sort(key=lambda x: x[0], reverse=True)

    if not results:
        print(f"No results for '{args.search}'")
        print("Try broader terms or run --list to see all entries.")
        return

    print(f"\nSearch results for '{args.search}' ({len(results)} found):\n")
    for score, e in results:
        print(f"  [{e.get('date','')}] {e['title']}")
        tags = ", ".join(e.get("tags", []))
        print(f"           tags: {tags}  file: {e.get('_file','')}")
        # Show first line of summary
        body = e.get("_body", "")
        for line in body.split("\n"):
            line = line.strip()
            if line and not line.startswith("#") and line != "(待補)":
                print(f"           {line[:70]}...")
                break
        print()


def find_due_reviews(entries: list[dict]) -> list[dict]:
    """Find entries due for review based on spaced repetition schedule."""
    today = date.today()
    due = []
    # Simple spaced repetition intervals: 1, 3, 7, 14, 30, 60 days
    intervals = [1, 3, 7, 14, 30, 60]

    for e in entries:
        last_review = e.get("last_review")
        review_count = e.get("review_count", 0)
        if not last_review:
            continue
        try:
            last_date = date.fromisoformat(str(last_review))
        except (ValueError, TypeError):
            continue

        # Determine next review interval
        idx = min(review_count, len(intervals) - 1)
        interval = intervals[idx]
        next_review = last_date.replace(day=last_date.day)  # base
        from datetime import timedelta
        next_review = last_date + timedelta(days=interval)

        if today >= next_review:
            days_overdue = (today - next_review).days
            due.append({**e, "_days_overdue": days_overdue,
                       "_next_interval": interval})

    due.sort(key=lambda x: x["_days_overdue"], reverse=True)
    return due


def main():
    parser = argparse.ArgumentParser(
        description="Capture and search your learning journal")

    # Capture mode
    parser.add_argument("--title", help="Learning topic title")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    parser.add_argument("--related", default="",
                        help="Comma-separated IDs of related entries")
    parser.add_argument("--summary", default="", help="Brief summary")
    parser.add_argument("--keypoints", default="", help="Key takeaways")
    parser.add_argument("--questions", default="",
                        help="Questions you asked (semicolon-separated)")
    parser.add_argument("--extensions", default="",
                        help="Follow-up directions to explore")
    parser.add_argument("--confidence", type=int, default=3,
                        help="How well you understand this (1-5)")

    # List/search mode
    parser.add_argument("--list", action="store_true",
                        help="List all learning entries")
    parser.add_argument("--search", help="Search entries by keyword")

    args = parser.parse_args()

    if args.list:
        list_entries(args)
    elif args.search:
        search_entries(args)
    elif args.title:
        capture(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

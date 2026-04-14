#!/usr/bin/env python3
"""
Review - 智慧回顧系統
=====================
根據間隔複習排程、學習關聯、興趣脈絡，提醒你該回顧什麼、延伸什麼。

Usage:
    python3 scripts/review.py                  # 看今天該回顧什麼
    python3 scripts/review.py --connections     # 看所有學習之間的關聯
    python3 scripts/review.py --mark-reviewed 2026-04-11-alpha-school  # 標記已回顧
    python3 scripts/review.py --interests       # 看你的興趣脈絡分析
"""

import argparse
import re
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEARNINGS_DIR = REPO_ROOT / "learnings"

# Spaced repetition intervals (days)
INTERVALS = [1, 3, 7, 14, 30, 60, 120]


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


def load_all() -> list[dict]:
    entries = []
    if not LEARNINGS_DIR.exists():
        return entries
    for md in sorted(LEARNINGS_DIR.rglob("*.md")):
        with open(md, "r", encoding="utf-8") as f:
            content = f.read()
        meta = parse_frontmatter(content)
        if meta.get("id"):
            meta["_file"] = str(md)
            parts = content.split("---", 2)
            meta["_body"] = parts[2].strip() if len(parts) > 2 else ""
            entries.append(meta)
    return entries


def get_due_reviews(entries: list[dict]) -> list[dict]:
    today = date.today()
    due = []
    for e in entries:
        last_review = e.get("last_review")
        review_count = e.get("review_count", 0)
        if not last_review:
            continue
        try:
            last_date = date.fromisoformat(str(last_review))
        except (ValueError, TypeError):
            continue
        idx = min(review_count, len(INTERVALS) - 1)
        interval = INTERVALS[idx]
        next_review = last_date + timedelta(days=interval)
        days_until = (next_review - today).days
        if days_until <= 0:
            due.append({
                **e,
                "_days_overdue": abs(days_until),
                "_next_interval": interval,
                "_next_review": next_review.isoformat(),
            })
    due.sort(key=lambda x: x["_days_overdue"], reverse=True)
    return due


def get_upcoming(entries: list[dict], days_ahead: int = 3) -> list[dict]:
    today = date.today()
    upcoming = []
    for e in entries:
        last_review = e.get("last_review")
        review_count = e.get("review_count", 0)
        if not last_review:
            continue
        try:
            last_date = date.fromisoformat(str(last_review))
        except (ValueError, TypeError):
            continue
        idx = min(review_count, len(INTERVALS) - 1)
        interval = INTERVALS[idx]
        next_review = last_date + timedelta(days=interval)
        days_until = (next_review - today).days
        if 0 < days_until <= days_ahead:
            upcoming.append({**e, "_days_until": days_until})
    upcoming.sort(key=lambda x: x["_days_until"])
    return upcoming


def show_review_dashboard(entries: list[dict]):
    today = date.today()
    due = get_due_reviews(entries)
    upcoming = get_upcoming(entries)

    print(f"\n{'='*58}")
    print(f"  Learning Review Dashboard - {today.isoformat()}")
    print(f"  Total entries: {len(entries)}")
    print(f"{'='*58}")

    # Due now
    if due:
        print(f"\n  DUE FOR REVIEW ({len(due)}):")
        print(f"  {'─'*50}")
        for e in due:
            overdue = e["_days_overdue"]
            reviews = e.get("review_count", 0)
            conf = e.get("confidence", "?")
            urgency = "!!!" if overdue > 7 else "! " if overdue > 3 else "  "
            print(f"  {urgency} {e['title']}")
            print(f"      overdue: {overdue}d | reviews: {reviews} | "
                  f"confidence: {conf}/5")
            tags = ", ".join(e.get("tags", [])[:4])
            print(f"      tags: {tags}")
            print(f"      -> mark done: python3 scripts/review.py "
                  f"--mark-reviewed {e['id']}")
            print()
    else:
        print(f"\n  No reviews due today!")

    # Upcoming
    if upcoming:
        print(f"\n  COMING UP (next 3 days):")
        print(f"  {'─'*50}")
        for e in upcoming:
            print(f"    in {e['_days_until']}d: {e['title']}")

    # Low confidence
    low_conf = [e for e in entries if e.get("confidence", 5) <= 2]
    if low_conf:
        print(f"\n  LOW CONFIDENCE (may need deeper study):")
        print(f"  {'─'*50}")
        for e in low_conf:
            print(f"    [{e.get('confidence',0)}/5] {e['title']}")

    print()


def show_connections(entries: list[dict]):
    """Show how learning entries connect to each other through shared tags."""
    print(f"\n{'='*58}")
    print(f"  Learning Connections Map")
    print(f"{'='*58}\n")

    if len(entries) < 2:
        print("  Need at least 2 entries to find connections.")
        return

    # Build tag → entries index
    tag_index = {}
    for e in entries:
        for tag in e.get("tags", []):
            tag_index.setdefault(tag, []).append(e)

    # Find connections
    connections = []
    seen = set()
    for tag, group in tag_index.items():
        if len(group) < 2:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                pair = tuple(sorted([group[i]["id"], group[j]["id"]]))
                if pair not in seen:
                    seen.add(pair)
                    # Count shared tags
                    shared = set(group[i].get("tags", [])) & set(group[j].get("tags", []))
                    connections.append({
                        "a": group[i],
                        "b": group[j],
                        "shared_tags": list(shared),
                        "strength": len(shared)
                    })

    connections.sort(key=lambda x: x["strength"], reverse=True)

    if not connections:
        print("  No connections found yet. Add more tags to your entries!")
        return

    for c in connections:
        strength_bar = "=" * c["strength"]
        print(f"  {c['a']['title']}")
        print(f"    |{strength_bar}| shared: {', '.join(c['shared_tags'])}")
        print(f"  {c['b']['title']}")
        print()

    # Suggest unexplored connections
    print(f"  {'─'*50}")
    print(f"  Suggested explorations:")
    for c in connections[:3]:
        print(f"    -> How does '{c['a']['title']}' relate to "
              f"'{c['b']['title']}'?")
    print()


def show_interests(entries: list[dict]):
    """Analyze learning interests from tags and content."""
    print(f"\n{'='*58}")
    print(f"  Your Interest Profile (auto-generated)")
    print(f"{'='*58}\n")

    if not entries:
        print("  No entries yet!")
        return

    # Tag frequency
    tag_counts = Counter()
    for e in entries:
        for t in e.get("tags", []):
            tag_counts[t] += 1

    print(f"  TOP INTERESTS (by frequency):")
    print(f"  {'─'*50}")
    for tag, count in tag_counts.most_common(15):
        bar = "#" * (count * 3)
        print(f"    {tag:20s} {bar} ({count})")

    # Learning timeline
    print(f"\n  LEARNING TIMELINE:")
    print(f"  {'─'*50}")
    by_date = {}
    for e in entries:
        d = e.get("date", "unknown")
        by_date.setdefault(d, []).append(e["title"])
    for d in sorted(by_date.keys(), reverse=True)[:10]:
        titles = by_date[d]
        print(f"    {d}: {', '.join(titles)}")

    # Confidence distribution
    conf_counts = Counter()
    for e in entries:
        conf_counts[e.get("confidence", 0)] += 1
    print(f"\n  CONFIDENCE DISTRIBUTION:")
    print(f"  {'─'*50}")
    for level in range(5, 0, -1):
        count = conf_counts.get(level, 0)
        bar = "#" * (count * 2)
        label = {5: "Expert", 4: "Good", 3: "OK",
                 2: "Shaky", 1: "Just heard"}.get(level, "?")
        print(f"    {level}/5 ({label:12s}): {bar} ({count})")

    # Suggest what to explore next
    print(f"\n  SUGGESTED NEXT EXPLORATIONS:")
    print(f"  {'─'*50}")
    # Find tags that appear together often → suggest deepening
    tag_pairs = Counter()
    for e in entries:
        tags = sorted(e.get("tags", []))
        for i in range(len(tags)):
            for j in range(i+1, len(tags)):
                tag_pairs[(tags[i], tags[j])] += 1
    for (t1, t2), count in tag_pairs.most_common(5):
        if count >= 2:
            print(f"    You keep exploring {t1} + {t2} together "
                  f"({count} times)")
            print(f"    -> Consider going deeper into their intersection")
    print()


def mark_reviewed(entry_id: str):
    """Mark an entry as reviewed, updating review_count and last_review."""
    entries = load_all()
    target = None
    for e in entries:
        if e["id"] == entry_id:
            target = e
            break

    if not target:
        print(f"Entry '{entry_id}' not found.", file=sys.stderr)
        sys.exit(1)

    fpath = Path(target["_file"])
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    today = date.today().isoformat()
    old_count = target.get("review_count", 0)
    new_count = old_count + 1

    content = re.sub(r"^review_count:\s*\d+", f"review_count: {new_count}",
                     content, flags=re.MULTILINE)
    content = re.sub(r"^last_review:.*$", f"last_review: {today}",
                     content, flags=re.MULTILINE)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    # Calculate next review
    idx = min(new_count, len(INTERVALS) - 1)
    next_interval = INTERVALS[idx]
    next_date = date.today() + timedelta(days=next_interval)

    print(f"\nMarked reviewed: {target['title']}")
    print(f"  Reviews: {old_count} -> {new_count}")
    print(f"  Next review in {next_interval} days ({next_date.isoformat()})")


def main():
    parser = argparse.ArgumentParser(description="Smart review system")
    parser.add_argument("--connections", action="store_true",
                        help="Show connections between learning entries")
    parser.add_argument("--interests", action="store_true",
                        help="Show your interest profile analysis")
    parser.add_argument("--mark-reviewed", metavar="ID",
                        help="Mark an entry as reviewed")
    args = parser.parse_args()

    entries = load_all()

    if args.mark_reviewed:
        mark_reviewed(args.mark_reviewed)
    elif args.connections:
        show_connections(entries)
    elif args.interests:
        show_interests(entries)
    else:
        show_review_dashboard(entries)


if __name__ == "__main__":
    main()

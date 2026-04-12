#!/usr/bin/env python3
"""
Learning Session Logger
=======================
Log a learning session and update topic mastery in-place.

Usage:
    python3 scripts/log_session.py --topic math-004 --mastery 85 --time 25 --notes "通分練習有進步"
    python3 scripts/log_session.py --topic math-005 --mastery 50 --time 25 --notes "帶分數除法還需加強"
    python3 scripts/log_session.py --weekly-report
"""

import argparse
import os
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOPICS_DIR = REPO_ROOT / "topics"
LOGS_DIR = REPO_ROOT / "logs"


def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    """Returns (metadata_dict, raw_yaml_block, body)."""
    if not text.startswith("---"):
        return {}, "", text
    end = text.find("---", 3)
    if end == -1:
        return {}, "", text
    yaml_block = text[3:end]
    body = text[end + 3:]
    meta = {}
    for line in yaml_block.strip().split("\n"):
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith("#"):
            continue
        if ":" not in line_stripped:
            continue
        key, val = line_stripped.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            items = val[1:-1]
            meta[key] = [v.strip() for v in items.split(",")] if items.strip() else []
        elif val.isdigit():
            meta[key] = int(val)
        elif val == "" or val == "null":
            meta[key] = None
        else:
            meta[key] = val
    return meta, yaml_block, body


def find_topic_file(topic_id: str) -> Path | None:
    """Find the .md file for a given topic ID."""
    for md_file in TOPICS_DIR.rglob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            first_lines = f.read(500)
        if f"id: {topic_id}" in first_lines:
            return md_file
    return None


def update_topic_mastery(topic_id: str, new_mastery: int):
    """Update mastery and status in the topic file."""
    fpath = find_topic_file(topic_id)
    if not fpath:
        print(f"Warning: topic file for '{topic_id}' not found.", file=sys.stderr)
        return False

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    today = date.today().isoformat()

    # Update mastery value
    content = re.sub(r"^mastery:\s*\d+", f"mastery: {new_mastery}", content, flags=re.MULTILINE)

    # Update status
    if new_mastery >= 90:
        new_status = "mastered"
    elif new_mastery > 0:
        new_status = "learning"
    else:
        new_status = "not_started"
    content = re.sub(r"^status:\s*\S+", f"status: {new_status}", content, flags=re.MULTILINE)

    # Update last_review
    content = re.sub(r"^last_review:.*$", f"last_review: {today}", content, flags=re.MULTILINE)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {topic_id}: mastery={new_mastery}%, status={new_status}")
    return True


def append_log(topic_id: str, mastery: int, time_min: int, notes: str):
    """Append a session entry to today's log file."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    log_file = LOGS_DIR / f"{today}.md"

    now = datetime.now().strftime("%H:%M")

    if not log_file.exists():
        header = f"""# Learning Log - {today}

| 時間 | 主題 ID | 精熟度 | 花費(分鐘) | 筆記 |
|------|---------|--------|-----------|------|
"""
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(header)

    entry = f"| {now} | {topic_id} | {mastery}% | {time_min} | {notes} |\n"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Logged session to: {log_file}")


def load_all_topics() -> list[dict]:
    """Load all topics for reporting."""
    topics = []
    for md_file in sorted(TOPICS_DIR.rglob("*.md")):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        meta, _, _ = parse_frontmatter(content)
        if meta.get("id"):
            topics.append(meta)
    return topics


def weekly_report():
    """Generate a weekly summary from log files."""
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_num = today.isocalendar()[1]

    print(f"\n{'='*50}")
    print(f"  Weekly Report - Week {week_num}")
    print(f"  {week_start.isoformat()} ~ {today.isoformat()}")
    print(f"{'='*50}\n")

    # Collect log entries from this week
    total_sessions = 0
    total_minutes = 0
    daily_counts = {}

    for i in range(7):
        d = week_start + timedelta(days=i)
        log_file = LOGS_DIR / f"{d.isoformat()}.md"
        if log_file.exists():
            with open(log_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            entries = [l for l in lines if l.startswith("|") and not l.startswith("| 時間")
                       and not l.startswith("|---")]
            count = len(entries)
            total_sessions += count
            daily_counts[d.isoformat()] = count
            for entry in entries:
                parts = [p.strip() for p in entry.split("|")]
                if len(parts) >= 5:
                    try:
                        total_minutes += int(parts[4])
                    except ValueError:
                        pass

    print(f"  Total sessions:  {total_sessions}")
    print(f"  Total time:      {total_minutes} min ({total_minutes/60:.1f} hrs)")
    print()

    # Topic mastery summary
    topics = load_all_topics()
    mastered = [t for t in topics if t.get("mastery", 0) >= 90]
    learning = [t for t in topics if 0 < t.get("mastery", 0) < 90]
    not_started = [t for t in topics if t.get("mastery", 0) == 0]

    print(f"  --- Mastery Summary ---")
    print(f"  Mastered ({len(mastered)}):")
    for t in mastered:
        print(f"    [=] {t['title']} ({t['mastery']}%)")
    print(f"  Learning ({len(learning)}):")
    for t in sorted(learning, key=lambda x: x.get("mastery", 0), reverse=True):
        print(f"    [~] {t['title']} ({t['mastery']}%)")
    print(f"  Not started ({len(not_started)}):")
    for t in not_started:
        print(f"    [ ] {t['title']}")

    # Knowledge frontier
    mastered_ids = {t["id"] for t in mastered}
    frontier = []
    for t in topics:
        if t.get("mastery", 0) >= 90:
            continue
        prereqs = t.get("prerequisites", [])
        if all(p in mastered_ids for p in prereqs):
            frontier.append(t)

    print(f"\n  --- Knowledge Frontier (next to learn) ---")
    for t in frontier:
        print(f"    -> {t['title']} (current: {t.get('mastery', 0)}%)")
    print()

    # Save report
    report_file = LOGS_DIR / f"weekly-{week_start.isoformat()}.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"# Weekly Report - Week {week_num}\n\n")
        f.write(f"Period: {week_start.isoformat()} ~ {today.isoformat()}\n\n")
        f.write(f"## Summary\n")
        f.write(f"- Sessions: {total_sessions}\n")
        f.write(f"- Total time: {total_minutes} min ({total_minutes/60:.1f} hrs)\n\n")
        f.write(f"## Mastery\n")
        f.write(f"| Topic | Mastery | Status |\n|-------|---------|--------|\n")
        for t in sorted(topics, key=lambda x: x.get("mastery", 0), reverse=True):
            f.write(f"| {t['title']} | {t.get('mastery', 0)}% | {t.get('status', '')} |\n")
        f.write(f"\n## Knowledge Frontier\n")
        for t in frontier:
            f.write(f"- {t['title']} ({t.get('mastery', 0)}%)\n")
    print(f"  Report saved to: {report_file}")


def main():
    parser = argparse.ArgumentParser(description="Log learning sessions & update mastery")
    parser.add_argument("--topic", help="Topic ID (e.g. math-004)")
    parser.add_argument("--mastery", type=int, help="New mastery percentage (0-100)")
    parser.add_argument("--time", type=int, default=25, help="Session duration in minutes")
    parser.add_argument("--notes", default="", help="Session notes")
    parser.add_argument("--weekly-report", action="store_true", help="Generate weekly report")
    args = parser.parse_args()

    if args.weekly_report:
        weekly_report()
        return

    if not args.topic or args.mastery is None:
        parser.error("--topic and --mastery are required (or use --weekly-report)")

    # 1. Update topic file
    update_topic_mastery(args.topic, args.mastery)

    # 2. Append to daily log
    append_log(args.topic, args.mastery, args.time, args.notes)

    print("\nDone! Run 'python3 scripts/generate_graph.py' to update the graph.")


if __name__ == "__main__":
    main()

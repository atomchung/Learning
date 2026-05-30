#!/usr/bin/env python3
"""
Scan Claude Code transcripts for admission candidates.

MVP regex pre-filter: extract candidate admission moments → human reviews →
manually promote to admissions.jsonl.

Usage:
    python3 scan_admissions.py [days]   # default 7
    python3 scan_admissions.py 30
"""
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

TRANSCRIPT_ROOT = Path.home() / ".claude" / "projects"
EVAL_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = EVAL_ROOT / "runs"

# Admission patterns — cast wide net, human filters false positives.
# Tagged so reviewer can batch-skip noisy categories (e.g. en_apology often is just politeness).
PATTERNS = [
    # Chinese — apologies (politeness, weak signal but worth a look)
    (r"對不起", "zh_apology"),
    (r"抱歉", "zh_apology"),
    (r"不好意思", "zh_apology"),
    # Chinese — explicit admissions (strong signal)
    (r"我錯了", "zh_admit"),
    (r"我搞錯", "zh_admit"),
    (r"我看錯", "zh_admit"),
    (r"我誤(?:解|會)", "zh_admit"),
    # Chinese — self-correct / mid-thought pause (strong signal)
    (r"剛才.{0,8}不對", "zh_self_correct"),
    (r"剛才.{0,8}錯", "zh_self_correct"),
    (r"等等[,，]", "zh_pause_reconsider"),
    (r"我重看", "zh_reread"),
    (r"重新看", "zh_reread"),
    # Chinese — explicit correction (structured forms only — avoid "修正動作"-style noise)
    (r"應該是.{0,40}才對", "zh_correction"),       # "應該是 X 才對"
    (r"不是.{1,20}才對", "zh_correction"),         # "不是 X 才對"
    (r"(?<![一-鿿])更正[::]", "zh_correction"),  # "更正：" prefix form only
    (r"(?<![一-鿿])修正[::]", "zh_correction"),  # "修正：" prefix form only
    # English — apologies / admissions
    (r"\bsorry\b", "en_apology"),
    (r"\bapologi[zs]e", "en_apology"),
    (r"\bmy (?:bad|mistake)\b", "en_admit"),
    (r"\bI was wrong\b", "en_admit"),
    (r"\bI(?:'m| am) wrong\b", "en_admit"),
    (r"\bI (?:made|had) an? error\b", "en_admit"),
    (r"\bI misread\b", "en_misread"),
    (r"\bI misunderstood\b", "en_misunderstood"),
    (r"\bActually,", "en_reconsider"),
    (r"\blet me re[- ]?read\b", "en_reread"),
    (r"\bcorrection:", "en_correction"),
    (r"\bYou(?:'re| are) right\b", "en_concede"),
]
COMPILED = [(re.compile(p, re.IGNORECASE), tag) for p, tag in PATTERNS]

CONTEXT_WINDOW = 200  # chars before / after match


def iter_assistant_text_blocks(jsonl_path: Path):
    """Yield dicts for each assistant text block in a transcript file."""
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("type") != "assistant":
                continue
            msg = obj.get("message") or {}
            if msg.get("role") != "assistant":
                continue
            content = msg.get("content")
            if not isinstance(content, list):
                continue
            model = msg.get("model", "unknown")
            for block in content:
                if not isinstance(block, dict):
                    continue
                if block.get("type") != "text":
                    continue
                text = block.get("text") or ""
                if not text.strip():
                    continue
                yield {
                    "ts": obj.get("timestamp"),
                    "session_id": obj.get("sessionId"),
                    "uuid": obj.get("uuid"),
                    "parent_uuid": obj.get("parentUuid"),
                    "cwd": obj.get("cwd"),
                    "model": model,
                    "text": text,
                }


def find_hits(text: str):
    """Return list of {tag, match, snippet, offset} for all regex matches."""
    hits = []
    for cre, tag in COMPILED:
        for m in cre.finditer(text):
            start, end = m.span()
            ctx_start = max(0, start - CONTEXT_WINDOW)
            ctx_end = min(len(text), end + CONTEXT_WINDOW)
            hits.append({
                "tag": tag,
                "match": m.group(0),
                "snippet": text[ctx_start:ctx_end],
                "offset": start,
            })
    return hits


def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    today = datetime.now().strftime("%Y-%m-%d")
    out_path = RUNS_DIR / f"candidates_{today}.jsonl"
    # If running multiple times same day, suffix with counter to avoid overwrite
    if out_path.exists():
        i = 2
        while (RUNS_DIR / f"candidates_{today}_{i}.jsonl").exists():
            i += 1
        out_path = RUNS_DIR / f"candidates_{today}_{i}.jsonl"

    n_files = 0
    n_files_recent = 0
    n_blocks = 0
    n_hits = 0
    tag_counts: dict[str, int] = {}

    with open(out_path, "w", encoding="utf-8") as out:
        for jsonl in TRANSCRIPT_ROOT.rglob("*.jsonl"):
            n_files += 1
            try:
                mtime = datetime.fromtimestamp(jsonl.stat().st_mtime, tz=timezone.utc)
            except OSError:
                continue
            if mtime < cutoff:
                continue
            n_files_recent += 1
            for item in iter_assistant_text_blocks(jsonl):
                n_blocks += 1
                for hit in find_hits(item["text"]):
                    n_hits += 1
                    tag_counts[hit["tag"]] = tag_counts.get(hit["tag"], 0) + 1
                    record = {
                        "ts": item["ts"],
                        "session_id": item["session_id"],
                        "uuid": item["uuid"],
                        "parent_uuid": item["parent_uuid"],
                        "cwd": item["cwd"],
                        "model": item["model"],
                        "transcript_path": str(jsonl),
                        "pattern_tag": hit["tag"],
                        "matched_phrase": hit["match"],
                        "snippet": hit["snippet"],
                        # placeholders for human review
                        "is_real_admission": None,
                        "error_type": None,
                        "root_cause": None,
                        "fix": None,
                    }
                    out.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Scanned: {n_files} total transcripts, {n_files_recent} modified within last {days} days")
    print(f"Assistant text blocks parsed: {n_blocks}")
    print(f"Candidate hits: {n_hits}")
    if tag_counts:
        print("By pattern_tag:")
        for tag in sorted(tag_counts, key=tag_counts.get, reverse=True):
            print(f"  {tag_counts[tag]:5d}  {tag}")
    print(f"Output: {out_path}")


if __name__ == "__main__":
    main()

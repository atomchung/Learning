"""Fetch KKTIX atom feeds, filter AI-related events, emit an ICS calendar.

Usage:
    python fetch.py                    # fetch live, write dist/taipei-ai.ics
    python fetch.py --from-fixtures    # parse local test fixtures (offline)

Design notes:
  * Pure stdlib (urllib, xml.etree, re) so this runs anywhere without pip.
  * KKTIX atom entries don't expose structured start/end times -- we regex
    the summary HTML for dates. Fallback: published date + a note in the
    description asking users to click through.
  * Events in the past are dropped.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

from sources import SOURCES, Source

ATOM_NS = {"a": "http://www.w3.org/2005/Atom"}
TAIPEI_TZ = timezone(timedelta(hours=8))
USER_AGENT = "TaipeiAICalendarBot/0.1 (+https://github.com/atomchung/learning)"

# ---------------------------------------------------------------------------
# AI keyword filter. English terms need word boundaries (otherwise "AI"
# matches inside "Taiwan"); Chinese terms don't have word boundaries.
# ---------------------------------------------------------------------------
_EN_KEYWORDS = (
    r"AI|LLM|LLMs|GPT|Claude|Gemini|Llama|ChatGPT|Gen[- ]?AI|"
    r"AI[- ]?Agent|Agentic|RAG|Fine[- ]?tun\w*|Embedding|Transformer|Diffusion|"
    r"Prompt|MLOps|LLMOps|Vector[ ]?DB|MCP|Anthropic|OpenAI|HuggingFace"
)
_ZH_KEYWORDS = (
    r"機器學習|深度學習|強化學習|生成式|人工智慧|大語言模型|大模型|"
    r"向量資料庫|提示工程"
)
AI_KEYWORDS_EN = re.compile(rf"\b(?:{_EN_KEYWORDS})\b", re.IGNORECASE)
AI_KEYWORDS_ZH = re.compile(_ZH_KEYWORDS)

# Common date patterns in KKTIX event summaries.
DATE_PATTERNS = [
    # 2026/04/18 19:00 or 2026-04-18 19:00
    re.compile(r"(20\d{2})[/\-](\d{1,2})[/\-](\d{1,2})[^\d]{1,10}?(\d{1,2}):(\d{2})"),
    # 2026/04/18
    re.compile(r"(20\d{2})[/\-](\d{1,2})[/\-](\d{1,2})"),
    # 04/18 19:00 (no year -> assume current year, bumped to next year if past)
    re.compile(r"(?<!\d)(\d{1,2})[/\-](\d{1,2})[^\d]{1,10}?(\d{1,2}):(\d{2})"),
]

HTML_TAG = re.compile(r"<[^>]+>")
WHITESPACE = re.compile(r"\s+")


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class Event:
    source_name: str
    title: str
    url: str
    summary_text: str
    start: datetime
    end: datetime
    tags: tuple[str, ...] = field(default_factory=tuple)

    @property
    def uid(self) -> str:
        digest = hashlib.sha1(self.url.encode("utf-8")).hexdigest()[:16]
        return f"{digest}@taipei-ai-cal"


# ---------------------------------------------------------------------------
# Fetch + parse
# ---------------------------------------------------------------------------


def fetch_atom(source: Source) -> bytes:
    req = urllib.request.Request(
        source.atom_url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/atom+xml, application/xml;q=0.9, */*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()


def strip_html(text: str) -> str:
    text = HTML_TAG.sub(" ", text)
    text = html.unescape(text)
    return WHITESPACE.sub(" ", text).strip()


def extract_datetime(text: str, fallback: datetime, now: datetime) -> datetime:
    """Best-effort extraction of event datetime from summary text."""
    for pattern in DATE_PATTERNS:
        m = pattern.search(text)
        if not m:
            continue
        groups = m.groups()
        try:
            if len(groups) >= 3 and len(groups[0]) == 4:
                # Full date with year.
                y, mo, d = int(groups[0]), int(groups[1]), int(groups[2])
                h = int(groups[3]) if len(groups) > 4 else 19
                mi = int(groups[4]) if len(groups) > 4 else 0
                return datetime(y, mo, d, h, mi, tzinfo=TAIPEI_TZ)
            # Month/day only; assume current year, roll to next if already past.
            mo, d = int(groups[0]), int(groups[1])
            h = int(groups[2]) if len(groups) > 2 else 19
            mi = int(groups[3]) if len(groups) > 3 else 0
            candidate = datetime(now.year, mo, d, h, mi, tzinfo=TAIPEI_TZ)
            if candidate < now - timedelta(days=1):
                candidate = candidate.replace(year=now.year + 1)
            return candidate
        except ValueError:
            continue
    return fallback


def parse_atom(xml_bytes: bytes, source: Source, now: datetime) -> list[Event]:
    root = ET.fromstring(xml_bytes)
    events: list[Event] = []
    for entry in root.findall("a:entry", ATOM_NS):
        title = (entry.findtext("a:title", default="", namespaces=ATOM_NS) or "").strip()
        link_el = entry.find("a:link", ATOM_NS)
        url = link_el.get("href", "") if link_el is not None else ""
        published_str = entry.findtext("a:published", default="", namespaces=ATOM_NS) or ""
        summary_raw = entry.findtext("a:summary", default="", namespaces=ATOM_NS) or entry.findtext(
            "a:content", default="", namespaces=ATOM_NS
        ) or ""
        summary_text = strip_html(summary_raw)

        try:
            published = datetime.fromisoformat(published_str.replace("Z", "+00:00"))
        except ValueError:
            published = now

        start = extract_datetime(f"{title}\n{summary_text}", fallback=published, now=now)
        end = start + timedelta(hours=2)

        events.append(
            Event(
                source_name=source.name,
                title=title,
                url=url,
                summary_text=summary_text,
                start=start,
                end=end,
                tags=source.tags,
            )
        )
    return events


def is_ai_related(event: Event) -> bool:
    text = f"{event.title}\n{event.summary_text}"
    return bool(AI_KEYWORDS_EN.search(text) or AI_KEYWORDS_ZH.search(text))


# ---------------------------------------------------------------------------
# ICS output
# ---------------------------------------------------------------------------


def ics_datetime(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def ics_escape(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace(",", "\\,")
        .replace(";", "\\;")
        .replace("\n", "\\n")
    )


def fold_line(line: str, limit: int = 73) -> list[str]:
    """RFC 5545 line folding: 75 octets max, continuation lines start with space."""
    if len(line) <= limit:
        return [line]
    out = [line[:limit]]
    rest = line[limit:]
    while rest:
        out.append(" " + rest[: limit - 1])
        rest = rest[limit - 1 :]
    return out


def generate_ics(events: list[Event], generated_at: datetime) -> str:
    lines: list[str] = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Taipei AI Calendar//0.1//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Taipei AI Events",
        "X-WR-CALDESC:Curated AI events in Taipei",
        "X-WR-TIMEZONE:Asia/Taipei",
    ]
    stamp = ics_datetime(generated_at)
    for e in events:
        desc = (
            f"Source: {e.source_name}\n"
            f"URL: {e.url}\n"
            f"Tags: {', '.join(e.tags) if e.tags else '-'}\n\n"
            f"{e.summary_text[:800]}"
        )
        raw_lines = [
            "BEGIN:VEVENT",
            f"UID:{e.uid}",
            f"DTSTAMP:{stamp}",
            f"DTSTART:{ics_datetime(e.start)}",
            f"DTEND:{ics_datetime(e.end)}",
            f"SUMMARY:{ics_escape(e.title)}",
            f"URL:{e.url}",
            f"DESCRIPTION:{ics_escape(desc)}",
            "END:VEVENT",
        ]
        for raw in raw_lines:
            lines.extend(fold_line(raw))
    lines.append("END:VCALENDAR")
    return "\r\n".join(lines) + "\r\n"


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def collect_events(from_fixtures: bool, now: datetime) -> tuple[list[Event], list[str]]:
    """Return (kept_events, per_source_log_lines)."""
    log: list[str] = []
    fixtures_dir = Path(__file__).parent / "tests" / "fixtures"
    all_events: list[Event] = []

    for source in SOURCES:
        try:
            if from_fixtures:
                fixture = fixtures_dir / f"sample_{source.subdomain}.atom"
                if not fixture.exists():
                    log.append(f"[{source.name}] no fixture, skipping")
                    continue
                xml_bytes = fixture.read_bytes()
            else:
                xml_bytes = fetch_atom(source)
        except (urllib.error.URLError, TimeoutError) as err:
            log.append(f"[{source.name}] FETCH FAILED: {err}")
            continue
        except Exception as err:  # noqa: BLE001
            log.append(f"[{source.name}] ERROR: {err}")
            continue

        try:
            events = parse_atom(xml_bytes, source, now=now)
        except ET.ParseError as err:
            log.append(f"[{source.name}] PARSE FAILED: {err}")
            continue

        kept = events if source.ai_only else [e for e in events if is_ai_related(e)]
        log.append(
            f"[{source.name}] {len(events)} raw -> {len(kept)} kept"
            f"{' (ai_only)' if source.ai_only else ' (filtered)'}"
        )
        all_events.extend(kept)

    # Drop events already in the past (before today in Taipei).
    today_start = now.astimezone(TAIPEI_TZ).replace(hour=0, minute=0, second=0, microsecond=0)
    future = [e for e in all_events if e.start >= today_start - timedelta(hours=6)]
    log.append(f"TOTAL kept: {len(future)} (dropped {len(all_events) - len(future)} past events)")

    future.sort(key=lambda e: e.start)
    return future, log


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from-fixtures", action="store_true", help="read local fixtures, no network")
    parser.add_argument("--out", default="dist/taipei-ai.ics", help="output ICS path")
    args = parser.parse_args(argv)

    now = datetime.now(timezone.utc)
    events, log = collect_events(from_fixtures=args.from_fixtures, now=now)
    for line in log:
        print(line)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(generate_ics(events, generated_at=now), encoding="utf-8")
    print(f"Wrote {out_path} ({len(events)} events)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

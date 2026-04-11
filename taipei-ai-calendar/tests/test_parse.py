"""Offline tests: parse fixture atom feeds and verify the whole pipeline.

Run with: python -m pytest tests/ -v
Or plain: python tests/test_parse.py
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from fetch import (  # noqa: E402
    collect_events,
    extract_datetime,
    generate_ics,
    is_ai_related,
    parse_atom,
    strip_html,
    TAIPEI_TZ,
)
from sources import SOURCES  # noqa: E402

NOW = datetime(2026, 4, 11, 0, 0, tzinfo=timezone.utc)


def _source(subdomain: str):
    return next(s for s in SOURCES if s.subdomain == subdomain)


def test_strip_html():
    assert strip_html("<p>hello <b>world</b></p>") == "hello world"
    assert strip_html("&lt;tag&gt; &amp; stuff") == "<tag> & stuff"


def test_extract_datetime_full():
    fallback = NOW
    dt = extract_datetime("聚會時間：2026/05/15 19:00", fallback, NOW)
    assert dt.year == 2026 and dt.month == 5 and dt.day == 15
    assert dt.hour == 19 and dt.minute == 0
    assert dt.tzinfo == TAIPEI_TZ


def test_extract_datetime_date_only():
    fallback = NOW
    dt = extract_datetime("日期 2026-06-27", fallback, NOW)
    assert (dt.year, dt.month, dt.day) == (2026, 6, 27)


def test_extract_datetime_fallback():
    fallback = datetime(2026, 1, 1, tzinfo=TAIPEI_TZ)
    dt = extract_datetime("no date here", fallback, NOW)
    assert dt == fallback


def test_parse_blindegg_fixture():
    src = _source("blindegg")
    xml = (ROOT / "tests" / "fixtures" / "sample_blindegg.atom").read_bytes()
    events = parse_atom(xml, src, now=NOW)
    assert len(events) == 2
    titles = [e.title for e in events]
    assert any("小聚" in t for t in titles)
    assert any("年會" in t for t in titles)
    # Confirm date extraction picked up 2026/05/15 19:00
    may_meetup = next(e for e in events if "小聚" in e.title)
    assert (may_meetup.start.month, may_meetup.start.day) == (5, 15)
    assert may_meetup.start.hour == 19


def test_ai_filter_drops_nonai_devops_event():
    src = _source("devops")
    xml = (ROOT / "tests" / "fixtures" / "sample_devops.atom").read_bytes()
    events = parse_atom(xml, src, now=NOW)
    assert len(events) == 2
    filtered = [e for e in events if is_ai_related(e)]
    assert len(filtered) == 1
    assert "LLM" in filtered[0].title


def test_collect_from_fixtures_end_to_end():
    events, log = collect_events(from_fixtures=True, now=NOW)
    assert len(events) >= 3, f"expected >=3 events, got {len(events)}: {log}"
    assert events == sorted(events, key=lambda e: e.start)


def test_ics_generation_smoke():
    events, _ = collect_events(from_fixtures=True, now=NOW)
    ics = generate_ics(events, generated_at=NOW)
    assert ics.startswith("BEGIN:VCALENDAR\r\n")
    assert ics.rstrip().endswith("END:VCALENDAR")
    assert "VERSION:2.0" in ics
    assert f"BEGIN:VEVENT" in ics
    # Every event should have a UID, DTSTART, DTEND, SUMMARY
    assert ics.count("BEGIN:VEVENT") == ics.count("END:VEVENT") == len(events)
    for keyword in ("UID:", "DTSTART:", "DTEND:", "SUMMARY:", "URL:"):
        assert keyword in ics


if __name__ == "__main__":
    # Simple runner so this works without pytest.
    tests = [
        test_strip_html,
        test_extract_datetime_full,
        test_extract_datetime_date_only,
        test_extract_datetime_fallback,
        test_parse_blindegg_fixture,
        test_ai_filter_drops_nonai_devops_event,
        test_collect_from_fixtures_end_to_end,
        test_ics_generation_smoke,
    ]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL  {t.__name__}: {exc}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"ERROR {t.__name__}: {exc.__class__.__name__}: {exc}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)

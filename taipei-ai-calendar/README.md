# Taipei AI Calendar

An auto-updating ICS calendar of AI-related community events in Taipei.

Aggregates KKTIX community feeds, filters for AI content, emits a single
subscribable `.ics` file so you can drop it into Google Calendar / Apple
Calendar / Outlook and stop manually trawling 5 different platforms.

## Status

MVP. Currently pulls from a whitelist of ~10 KKTIX communities. Roadmap below.

## How it works

```
KKTIX atom feeds  ──▶  fetch.py  ──▶  AI keyword filter  ──▶  dist/taipei-ai.ics
(whitelisted)                         (English + Chinese)
```

- `sources.py` — curated whitelist. Communities marked `ai_only=True` keep all
  events; general-purpose communities (DevOps Taiwan, Taipei.py, …) are
  filtered for AI keywords.
- `fetch.py` — pure stdlib. No pip install needed. Fetches atom feeds, parses
  with `xml.etree`, extracts event datetimes via regex, emits RFC 5545 ICS.
- `tests/test_parse.py` — runs offline against fixture atom files.

## Usage

```bash
# Offline: parse committed fixtures (no network required)
python fetch.py --from-fixtures --out dist/taipei-ai.ics

# Live: fetch real KKTIX feeds
python fetch.py --out dist/taipei-ai.ics

# Run tests
python tests/test_parse.py
```

## Subscribing to the calendar

Once the GitHub Actions workflow is set up and gh-pages is enabled, subscribe
to the published URL:

```
https://<your-github-username>.github.io/<repo>/taipei-ai.ics
```

**Google Calendar**: Settings → Add calendar → From URL → paste the URL above.
**Apple Calendar**: File → New Calendar Subscription → paste URL.

## Whitelist of sources

| Source | Subdomain | AI only? |
|---|---|---|
| Generative AI 年會 / 小聚 | blindegg | yes |
| Chatbot Developers Taiwan | chatbots | yes |
| DevOps Taiwan | devops | filtered |
| HITCON | hitcon | filtered |
| Taipei.py | taipei-py | filtered |
| MOPCON | mopcon | filtered |
| PyCon Taiwan | pycontw | filtered |
| JSDC Taiwan | jsdc | filtered |
| SITCON | sitcon | filtered |
| COSCUP | coscup | filtered |

## Known limitations (MVP)

1. **Event datetime is regex-extracted from summary HTML.** When parsing fails,
   the event falls back to its `published` date. Next step: fetch the event
   detail page and parse the structured start/end.
2. **Only KKTIX.** Accupass, Luma, Meetup.com, GDG, FB Events are all
   roadmapped but not implemented.
3. **No deduplication across sources.** Same event cross-posted to two
   communities shows up twice. Fine for now; add URL/title fuzzy dedupe later.
4. **No location filter.** Events from Taiwanese communities may happen in
   Hsinchu/Taichung/Tainan; we don't filter. Add city detection later.

## Roadmap

- [ ] Parse KKTIX event detail pages for structured start/end/venue
- [ ] Add Accupass search scraper (filter by `q=AI&area=taipei`)
- [ ] Add Luma taipei page scraper
- [ ] LLM-based quality scoring (drop招商/銷售/付費課程 noise)
- [ ] Dedupe across sources by URL + fuzzy title
- [ ] Location filter (Taipei / Hsinchu / remote)
- [ ] Simple HTML frontend at root of gh-pages
- [ ] "Report a missing event" form → GitHub issue

## Contributing new sources

Edit `sources.py`. Every KKTIX subdomain has an atom feed at
`https://<subdomain>.kktix.cc/events.atom`. Check it exists first, then add
a `Source(...)` entry.

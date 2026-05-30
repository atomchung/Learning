#!/usr/bin/env python3
"""
build_graph_svg.py — 從 topics/*/cards/*.md 生成靜態 SVG 知識圖譜。

為什麼是 SVG：GitHub 網頁與手機 App 原生 render SVG，所以可直接嵌進
README，打開就看到圖，不需任何外部服務 / Pages / 設定。

布局：依 topic 分群，每群一欄縱向排列；同 appears-on 的跨群卡之間連線。
用法：python3 scripts/build_graph_svg.py  →  產出 docs/graph.svg
卡片有增減時重跑即可。
"""
import re, pathlib, math, html as _html

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = sorted(ROOT.glob("topics/*/cards/*.md"))
OUT = ROOT / "docs" / "graph.svg"

def parse(path):
    text = path.read_text(encoding="utf-8")
    fm, body, cur = {}, text, None
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        body = m.group(2)
        for line in m.group(1).splitlines():
            if re.match(r"^\s*-\s", line) and cur:
                fm.setdefault(cur, [])
                if isinstance(fm[cur], list):
                    fm[cur].append(line.split("-", 1)[1].strip())
            else:
                km = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
                if km:
                    cur = km.group(1)
                    fm[cur] = km.group(2).strip() or []
    links = re.findall(r"cards/([a-z0-9-]+)\.md", body)
    return fm, links

cards = {}
for c in CARDS:
    fm, links = parse(c)
    cards[c.stem] = {
        "topic": c.parent.parent.name,
        "title": fm.get("title", c.stem),
        "appears": fm.get("appears-on", []) if isinstance(fm.get("appears-on"), list) else [],
        "links": [l for l in links if l != c.stem],
    }

topics = sorted({v["topic"] for v in cards.values()})
colors = ["#5b8def", "#e0633a", "#3aa17e", "#b061d6", "#d6a000", "#888"]
palette = {t: colors[i % len(colors)] for i, t in enumerate(topics)}

# 版面：每個 topic 一欄
COL_W, ROW_H, PAD_X, PAD_TOP = 300, 64, 40, 90
NODE_W, NODE_H = 240, 44
col_x = {t: PAD_X + i * COL_W for i, t in enumerate(topics)}
pos = {}
counts = {t: 0 for t in topics}
for slug in sorted(cards, key=lambda s: (cards[s]["topic"], s)):
    t = cards[slug]["topic"]
    x = col_x[t] + (COL_W - NODE_W) / 2
    y = PAD_TOP + counts[t] * ROW_H
    pos[slug] = (x, y)
    counts[t] += 1

W = PAD_X * 2 + len(topics) * COL_W - (COL_W - NODE_W)
H = PAD_TOP + max(counts.values()) * ROW_H + 30

def esc(s): return _html.escape(str(s))

def wrap(title, n=13):
    # 中文按字數折行，最多兩行
    if len(title) <= n: return [title]
    return [title[:n], title[n:n+n-1] + ("…" if len(title) > 2*n-1 else "")]

# 邊：卡內連結
edges = set()
for slug, c in cards.items():
    for tgt in c["links"]:
        if tgt in cards:
            edges.add(tuple(sorted([slug, tgt])))

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}" font-family="-apple-system,PingFang TC,Microsoft JhengHei,sans-serif">')
svg.append(f'<rect width="{W}" height="{H}" fill="#11141a"/>')
svg.append(f'<text x="{PAD_X}" y="34" fill="#e7e9ee" font-size="20" font-weight="700">'
           f'Learning 知識圖譜</text>')
svg.append(f'<text x="{PAD_X}" y="56" fill="#9aa3b2" font-size="12">'
           f'{len(cards)} 張卡 · {len(topics)} 主題 · 連線=卡片間引用</text>')

# topic 欄標題
for t in topics:
    cx = col_x[t] + COL_W / 2
    svg.append(f'<text x="{cx:.0f}" y="78" fill="{palette[t]}" font-size="13" '
               f'font-weight="600" text-anchor="middle">{esc(t)}</text>')

# 邊（畫在節點下層）
for a, b in edges:
    (xa, ya), (xb, yb) = pos[a], pos[b]
    x1, y1 = xa + NODE_W/2, ya + NODE_H/2
    x2, y2 = xb + NODE_W/2, yb + NODE_H/2
    svg.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
               f'stroke="#3a4456" stroke-width="1.5"/>')

# 節點
for slug, c in cards.items():
    x, y = pos[slug]
    col = palette[c["topic"]]
    svg.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{NODE_W}" height="{NODE_H}" '
               f'rx="8" fill="#1c2230" stroke="{col}" stroke-width="2"/>')
    lines = wrap(c["title"])
    ty = y + (NODE_H - (len(lines)-1)*15) / 2 + 5
    for i, ln in enumerate(lines):
        svg.append(f'<text x="{x + NODE_W/2:.0f}" y="{ty + i*15:.0f}" fill="#e7e9ee" '
                   f'font-size="12" text-anchor="middle">{esc(ln)}</text>')

svg.append('</svg>')
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(svg), encoding="utf-8")
print(f"wrote {OUT}  ({len(cards)} cards, {len(edges)} edges, {W}x{H})")

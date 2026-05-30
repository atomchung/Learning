#!/usr/bin/env python3
"""
build_graph.py — 從 topics/*/cards/*.md 生成自包含的知識圖譜 HTML。

讀每張卡的 frontmatter（title / appears-on / tags / freshness）與正文裡的
卡片連結，輸出一個用 vis-network（CDN）渲染的互動圖：
  - 節點 = 卡片，依所屬 topic 上色
  - 邊   = 卡之間的連結
  - 點節點會在側欄顯示「一句話」摘要

用法：python3 scripts/build_graph.py  →  產出 docs/graph.html
卡片有增減時重跑即可。CI（.github/workflows/pages.yml）會在 push 到 main
時自動重跑並發佈到 GitHub Pages。
"""
import re, json, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = sorted(ROOT.glob("topics/*/cards/*.md"))
OUT = ROOT / "docs" / "graph.html"

def parse(path):
    text = path.read_text(encoding="utf-8")
    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    body = text
    if m:
        body = m.group(2)
        block = m.group(1)
        cur = None
        for line in block.splitlines():
            if re.match(r"^\s*-\s", line) and cur:
                fm.setdefault(cur, [])
                if isinstance(fm[cur], list):
                    fm[cur].append(line.split("-", 1)[1].strip())
            else:
                km = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
                if km:
                    cur = km.group(1)
                    val = km.group(2).strip()
                    fm[cur] = val if val else []
    # 一句話
    one = ""
    om = re.search(r"\*\*一句話\*\*[：:]\s*(.+)", body)
    if om:
        one = re.sub(r"\s*$", "", om.group(1)).strip()
    # 卡內連結（指向其他 cards/*.md）
    links = re.findall(r"cards/([a-z0-9-]+)\.md", body)
    return fm, one, links

nodes, edges, seen = [], [], set()
slug2topic = {}
for c in CARDS:
    slug = c.stem
    topic = c.parent.parent.name
    slug2topic[slug] = topic

palette = {}
colors = ["#5b8def", "#e0633a", "#3aa17e", "#b061d6", "#d6a000", "#888"]
for t in sorted({c.parent.parent.name for c in CARDS}):
    palette[t] = colors[len(palette) % len(colors)]

for c in CARDS:
    slug = c.stem
    topic = c.parent.parent.name
    fm, one, links = parse(c)
    title = fm.get("title", slug)
    fresh = fm.get("freshness", "")
    appears = fm.get("appears-on", []) if isinstance(fm.get("appears-on"), list) else []
    nodes.append({
        "id": slug, "label": title, "group": topic,
        "color": palette[topic], "one": one,
        "fresh": fresh if isinstance(fresh, str) else "",
        "appears": appears,
    })
    for tgt in links:
        if tgt != slug:
            key = tuple(sorted([slug, tgt]))
            if key not in seen:
                seen.add(key)
                edges.append({"from": slug, "to": tgt})

data = {"nodes": nodes, "edges": edges,
        "palette": palette, "count": len(nodes)}

html_doc = """<!doctype html>
<html lang="zh-Hant"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5">
<title>Learning 知識圖譜</title>
<script src="https://unpkg.com/vis-network@9.1.9/standalone/umd/vis-network.min.js"></script>
<style>
  :root { color-scheme: dark; }
  * { box-sizing: border-box; }
  body { margin:0; font-family:-apple-system,"PingFang TC","Microsoft JhengHei",sans-serif;
         background:#11141a; color:#e7e9ee; }
  header { padding:12px 16px; border-bottom:1px solid #232938; }
  header h1 { font-size:16px; margin:0 0 4px; }
  header p  { font-size:12px; margin:0; color:#9aa3b2; }
  #legend { padding:8px 16px; display:flex; flex-wrap:wrap; gap:10px;
            font-size:12px; border-bottom:1px solid #232938; }
  .lg { display:flex; align-items:center; gap:5px; }
  .dot { width:11px; height:11px; border-radius:3px; display:inline-block; }
  #net { width:100%; height:58vh; }
  #panel { padding:14px 16px; border-top:1px solid #232938; min-height:22vh; }
  #panel h2 { font-size:15px; margin:0 0 8px; line-height:1.4; }
  #panel .one { font-size:13px; color:#c7cdda; line-height:1.7; }
  #panel .meta { font-size:11px; color:#7d8698; margin-top:10px; }
  #panel .hint { color:#7d8698; font-size:13px; }
  .tag { display:inline-block; background:#1c2230; border:1px solid #2a3142;
         border-radius:10px; padding:1px 8px; margin:2px 4px 2px 0; font-size:11px; }
</style></head>
<body>
<header>
  <h1>Learning 知識圖譜</h1>
  <p>__COUNT__ 張卡 · 點一個節點看「一句話」· 雙指縮放 / 拖曳</p>
</header>
<div id="legend"></div>
<div id="net"></div>
<div id="panel"><span class="hint">點任一張卡看它的核心判斷。</span></div>
<script>
const DATA = __DATA__;
const legend = document.getElementById('legend');
for (const [t,c] of Object.entries(DATA.palette)) {
  const d = document.createElement('div'); d.className='lg';
  d.innerHTML = `<span class="dot" style="background:${c}"></span>${t}`;
  legend.appendChild(d);
}
const nodes = new vis.DataSet(DATA.nodes.map(n => ({
  id:n.id, label:n.label, color:{background:n.color,border:n.color},
  font:{color:'#e7e9ee', size:13, face:'sans-serif'},
  shape:'box', margin:8, widthConstraint:{maximum:150}
})));
const edges = new vis.DataSet(DATA.edges.map(e => ({
  from:e.from, to:e.to, color:{color:'#3a4456'},
  width:1.4, smooth:{type:'continuous'}
})));
const container = document.getElementById('net');
const net = new vis.Network(container, {nodes, edges}, {
  physics:{stabilization:true, barnesHut:{gravitationalConstant:-6000, springLength:120}},
  interaction:{hover:true, tooltipDelay:120}
});
const byId = Object.fromEntries(DATA.nodes.map(n=>[n.id,n]));
const panel = document.getElementById('panel');
net.on('click', p => {
  if (!p.nodes.length) return;
  const n = byId[p.nodes[0]];
  let meta = '';
  if (n.appears && n.appears.length)
    meta += n.appears.map(a=>`<span class="tag">${a}</span>`).join('');
  if (n.fresh) meta += `<span class="tag">時效 ${n.fresh}</span>`;
  panel.innerHTML = `<h2>${n.label}</h2>`
    + (n.one ? `<div class="one">${n.one}</div>` : `<div class="hint">（這張卡沒寫「一句話」）</div>`)
    + (meta ? `<div class="meta">${meta}</div>` : '');
});
</script>
</body></html>"""

OUT.parent.mkdir(parents=True, exist_ok=True)
html_doc = (html_doc
            .replace("__COUNT__", str(data["count"]))
            .replace("__DATA__", json.dumps(data, ensure_ascii=False)))
OUT.write_text(html_doc, encoding="utf-8")
print(f"wrote {OUT}  ({data['count']} cards, {len(edges)} edges)")

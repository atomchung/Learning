#!/usr/bin/env python3
"""
Knowledge Graph Generator
=========================
Reads topic .md files with YAML frontmatter from topics/ directory,
builds a knowledge graph, and outputs an interactive HTML visualization.

Usage:
    python3 scripts/generate_graph.py
    python3 scripts/generate_graph.py --subject math
    python3 scripts/generate_graph.py --output output/my_graph.html
"""

import argparse
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# YAML frontmatter parser (no external dependency)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown text. Returns (metadata, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    yaml_block = text[3:end].strip()
    body = text[end + 3:].strip()
    meta = {}
    for line in yaml_block.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        # Parse lists like [a, b, c]
        if val.startswith("[") and val.endswith("]"):
            items = val[1:-1]
            if items.strip():
                meta[key] = [v.strip() for v in items.split(",")]
            else:
                meta[key] = []
        # Parse numbers
        elif val.isdigit():
            meta[key] = int(val)
        # Parse empty
        elif val == "" or val == "null":
            meta[key] = None
        else:
            meta[key] = val
    return meta, body


def load_topics(base_dir: str, subject_filter: str = None) -> list[dict]:
    """Recursively load all topic .md files from base_dir."""
    topics = []
    base = Path(base_dir)
    if not base.exists():
        print(f"Error: topics directory '{base_dir}' not found.", file=sys.stderr)
        sys.exit(1)
    for md_file in sorted(base.rglob("*.md")):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        meta, body = parse_frontmatter(content)
        if not meta.get("id"):
            continue  # skip files without proper frontmatter
        if subject_filter and meta.get("subject") != subject_filter:
            continue
        meta["_file"] = str(md_file.relative_to(base))
        meta["_body"] = body.strip()
        # Ensure defaults
        meta.setdefault("prerequisites", [])
        meta.setdefault("mastery", 0)
        meta.setdefault("status", "not_started")
        meta.setdefault("tags", [])
        meta.setdefault("title", meta["id"])
        topics.append(meta)
    return topics


def find_frontier(topics: list[dict]) -> list[str]:
    """Find knowledge frontier: topics whose prerequisites are all mastered
    but the topic itself is not yet mastered."""
    mastered_ids = {t["id"] for t in topics if t.get("mastery", 0) >= 90}
    frontier = []
    for t in topics:
        if t.get("mastery", 0) >= 90:
            continue
        prereqs = t.get("prerequisites", [])
        if all(p in mastered_ids for p in prereqs):
            frontier.append(t["id"])
    return frontier


def compute_stats(topics: list[dict]) -> dict:
    """Compute summary statistics."""
    total = len(topics)
    mastered = sum(1 for t in topics if t.get("mastery", 0) >= 90)
    learning = sum(1 for t in topics if 0 < t.get("mastery", 0) < 90)
    not_started = sum(1 for t in topics if t.get("mastery", 0) == 0)
    avg_mastery = sum(t.get("mastery", 0) for t in topics) / total if total else 0
    return {
        "total": total,
        "mastered": mastered,
        "learning": learning,
        "not_started": not_started,
        "avg_mastery": round(avg_mastery, 1),
    }


# ---------------------------------------------------------------------------
# HTML graph generation
# ---------------------------------------------------------------------------

def generate_html(topics: list[dict], frontier: list[str], stats: dict) -> str:
    """Generate a self-contained interactive HTML page with the knowledge graph."""

    nodes = []
    edges = []
    id_set = {t["id"] for t in topics}

    for t in topics:
        mastery = t.get("mastery", 0)
        is_frontier = t["id"] in frontier
        nodes.append({
            "id": t["id"],
            "title": t.get("title", t["id"]),
            "mastery": mastery,
            "status": t.get("status", "not_started"),
            "tags": t.get("tags", []),
            "isFrontier": is_frontier,
            "subject": t.get("subject", ""),
        })
        for prereq in t.get("prerequisites", []):
            if prereq in id_set:
                edges.append({"source": prereq, "target": t["id"]})

    data = json.dumps({"nodes": nodes, "edges": edges, "stats": stats, "frontier": frontier},
                       ensure_ascii=False, indent=2)
    today = date.today().isoformat()

    html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Knowledge Graph - {today}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
         background: #0f1117; color: #e0e0e0; }}
  #header {{ padding: 20px 30px; background: #1a1d27;
             border-bottom: 1px solid #2a2d37; display: flex;
             justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }}
  #header h1 {{ font-size: 1.4em; color: #fff; }}
  .stats {{ display: flex; gap: 16px; flex-wrap: wrap; }}
  .stat-box {{ background: #252830; padding: 8px 16px; border-radius: 8px;
               text-align: center; min-width: 80px; }}
  .stat-box .num {{ font-size: 1.5em; font-weight: bold; }}
  .stat-box .label {{ font-size: 0.75em; color: #888; margin-top: 2px; }}
  .stat-mastered .num {{ color: #4caf50; }}
  .stat-learning .num {{ color: #ff9800; }}
  .stat-notstarted .num {{ color: #666; }}
  .stat-avg .num {{ color: #42a5f5; }}
  #graph-container {{ width: 100%; height: calc(100vh - 160px); position: relative; }}
  svg {{ width: 100%; height: 100%; }}
  .edge {{ stroke: #444; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }}
  .node-circle {{ stroke-width: 3; cursor: pointer; transition: r 0.2s; }}
  .node-circle:hover {{ filter: brightness(1.3); }}
  .node-label {{ fill: #e0e0e0; font-size: 13px; text-anchor: middle;
                 pointer-events: none; font-weight: 500; }}
  .mastery-label {{ fill: #aaa; font-size: 11px; text-anchor: middle; pointer-events: none; }}
  .frontier-ring {{ fill: none; stroke: #ffd700; stroke-width: 2;
                    stroke-dasharray: 5,3; pointer-events: none; }}
  #legend {{ position: absolute; bottom: 20px; left: 20px; background: #1a1d27cc;
             padding: 14px 18px; border-radius: 10px; font-size: 0.8em;
             border: 1px solid #2a2d37; }}
  #legend h3 {{ margin-bottom: 8px; font-size: 1em; }}
  .legend-item {{ display: flex; align-items: center; gap: 8px; margin: 4px 0; }}
  .legend-dot {{ width: 14px; height: 14px; border-radius: 50%; flex-shrink: 0; }}
  #frontier-panel {{ position: absolute; top: 20px; right: 20px; background: #1a1d27cc;
                     padding: 14px 18px; border-radius: 10px; font-size: 0.85em;
                     border: 1px solid #ffd70044; max-width: 260px; }}
  #frontier-panel h3 {{ color: #ffd700; margin-bottom: 8px; }}
  #frontier-panel li {{ margin: 4px 0; list-style: none; padding-left: 12px;
                        position: relative; }}
  #frontier-panel li::before {{ content: "\\25B6"; position: absolute; left: -4px;
                                color: #ffd700; font-size: 0.7em; top: 2px; }}
  #tooltip {{ position: absolute; background: #252830; border: 1px solid #444;
              border-radius: 8px; padding: 12px 16px; font-size: 0.85em;
              pointer-events: none; display: none; max-width: 240px;
              box-shadow: 0 4px 12px rgba(0,0,0,0.5); }}
  #tooltip .tt-title {{ font-weight: bold; font-size: 1.05em; margin-bottom: 6px; }}
  #tooltip .tt-row {{ display: flex; justify-content: space-between; margin: 2px 0; }}
  .mastery-bar {{ width: 100%; height: 6px; background: #333; border-radius: 3px;
                  margin-top: 6px; overflow: hidden; }}
  .mastery-bar-fill {{ height: 100%; border-radius: 3px; transition: width 0.3s; }}
</style>
</head>
<body>

<div id="header">
  <h1>&#x1F9E0; Knowledge Graph</h1>
  <div class="stats">
    <div class="stat-box stat-mastered"><div class="num" id="s-mastered">0</div><div class="label">已精熟</div></div>
    <div class="stat-box stat-learning"><div class="num" id="s-learning">0</div><div class="label">學習中</div></div>
    <div class="stat-box stat-notstarted"><div class="num" id="s-notstarted">0</div><div class="label">未開始</div></div>
    <div class="stat-box stat-avg"><div class="num" id="s-avg">0%</div><div class="label">平均精熟度</div></div>
  </div>
</div>

<div id="graph-container">
  <svg id="svg">
    <defs>
      <marker id="arrowhead" viewBox="0 0 10 7" refX="10" refY="3.5"
              markerWidth="8" markerHeight="6" orient="auto-start-reverse">
        <polygon points="0 0, 10 3.5, 0 7" fill="#555" />
      </marker>
    </defs>
  </svg>
  <div id="legend">
    <h3>&#x1F3A8; 圖例</h3>
    <div class="legend-item"><div class="legend-dot" style="background:#4caf50"></div> 已精熟 (&ge;90%)</div>
    <div class="legend-item"><div class="legend-dot" style="background:#ff9800"></div> 學習中 (1-89%)</div>
    <div class="legend-item"><div class="legend-dot" style="background:#555"></div> 未開始 (0%)</div>
    <div class="legend-item"><div class="legend-dot" style="border:2px dashed #ffd700;background:transparent"></div> 知識前沿</div>
  </div>
  <div id="frontier-panel">
    <h3>&#x1F3AF; 知識前沿 (建議下一步)</h3>
    <ul id="frontier-list"></ul>
  </div>
  <div id="tooltip"></div>
</div>

<script>
const DATA = {data};

// --- Stats ---
document.getElementById("s-mastered").textContent = DATA.stats.mastered;
document.getElementById("s-learning").textContent = DATA.stats.learning;
document.getElementById("s-notstarted").textContent = DATA.stats.not_started;
document.getElementById("s-avg").textContent = DATA.stats.avg_mastery + "%";

// --- Frontier panel ---
const fl = document.getElementById("frontier-list");
const nodeMap = {{}};
DATA.nodes.forEach(n => nodeMap[n.id] = n);
DATA.frontier.forEach(id => {{
  const li = document.createElement("li");
  li.textContent = nodeMap[id] ? nodeMap[id].title : id;
  fl.appendChild(li);
}});

// --- Graph layout (simple force-directed) ---
const svg = document.getElementById("svg");
const W = svg.clientWidth || 900;
const H = svg.clientHeight || 600;

// Assign initial positions using topological layers
function topoLayout(nodes, edges) {{
  const inDeg = {{}};
  const adj = {{}};
  nodes.forEach(n => {{ inDeg[n.id] = 0; adj[n.id] = []; }});
  edges.forEach(e => {{
    inDeg[e.target] = (inDeg[e.target] || 0) + 1;
    if (adj[e.source]) adj[e.source].push(e.target);
  }});
  // BFS layers
  const layers = [];
  const visited = new Set();
  let queue = nodes.filter(n => inDeg[n.id] === 0).map(n => n.id);
  while (queue.length > 0) {{
    layers.push([...queue]);
    queue.forEach(id => visited.add(id));
    const next = [];
    queue.forEach(id => {{
      (adj[id] || []).forEach(t => {{
        inDeg[t]--;
        if (inDeg[t] <= 0 && !visited.has(t)) {{
          if (!next.includes(t)) next.push(t);
        }}
      }});
    }});
    queue = next;
  }}
  // Remaining nodes (cycles or disconnected)
  nodes.forEach(n => {{
    if (!visited.has(n.id)) {{
      layers.push([n.id]);
      visited.add(n.id);
    }}
  }});
  // Position
  const pos = {{}};
  const layerH = H / (layers.length + 1);
  layers.forEach((layer, li) => {{
    const layerW = W / (layer.length + 1);
    layer.forEach((id, ni) => {{
      pos[id] = {{
        x: layerW * (ni + 1),
        y: layerH * (li + 1)
      }};
    }});
  }});
  return pos;
}}

const pos = topoLayout(DATA.nodes, DATA.edges);

// Assign positions to nodes
DATA.nodes.forEach(n => {{
  n.x = pos[n.id] ? pos[n.id].x : W / 2;
  n.y = pos[n.id] ? pos[n.id].y : H / 2;
}});

// Simple force simulation (limited iterations for fast render)
function simulate(nodes, edges, iterations) {{
  const nMap = {{}};
  nodes.forEach(n => nMap[n.id] = n);
  for (let i = 0; i < iterations; i++) {{
    // Repulsion between nodes
    for (let a = 0; a < nodes.length; a++) {{
      for (let b = a + 1; b < nodes.length; b++) {{
        let dx = nodes[b].x - nodes[a].x;
        let dy = nodes[b].y - nodes[a].y;
        let dist = Math.sqrt(dx * dx + dy * dy) || 1;
        let force = 8000 / (dist * dist);
        let fx = (dx / dist) * force;
        let fy = (dy / dist) * force;
        nodes[a].x -= fx; nodes[a].y -= fy;
        nodes[b].x += fx; nodes[b].y += fy;
      }}
    }}
    // Attraction along edges
    edges.forEach(e => {{
      const s = nMap[e.source], t = nMap[e.target];
      if (!s || !t) return;
      let dx = t.x - s.x;
      let dy = t.y - s.y;
      let dist = Math.sqrt(dx * dx + dy * dy) || 1;
      let force = (dist - 150) * 0.05;
      let fx = (dx / dist) * force;
      let fy = (dy / dist) * force;
      s.x += fx; s.y += fy;
      t.x -= fx; t.y -= fy;
    }});
    // Keep in bounds
    const pad = 80;
    nodes.forEach(n => {{
      n.x = Math.max(pad, Math.min(W - pad, n.x));
      n.y = Math.max(pad, Math.min(H - pad, n.y));
    }});
  }}
}}

simulate(DATA.nodes, DATA.edges, 80);

// --- Render ---
function masteryColor(m) {{
  if (m >= 90) return "#4caf50";
  if (m >= 60) return "#ff9800";
  if (m > 0)  return "#e67e22";
  return "#555";
}}

function masteryRadius(m) {{
  return 24 + (m / 100) * 12;
}}

// Edges
DATA.edges.forEach(e => {{
  const s = nodeMap[e.source], t = nodeMap[e.target];
  if (!s || !t) return;
  const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
  line.setAttribute("x1", s.x); line.setAttribute("y1", s.y);
  // Shorten to not overlap node circle
  const dx = t.x - s.x, dy = t.y - s.y;
  const dist = Math.sqrt(dx*dx + dy*dy) || 1;
  const r = masteryRadius(t.mastery);
  line.setAttribute("x2", t.x - (dx/dist) * (r + 4));
  line.setAttribute("y2", t.y - (dy/dist) * (r + 4));
  line.setAttribute("class", "edge");
  svg.appendChild(line);
}});

// Nodes
const tooltip = document.getElementById("tooltip");

DATA.nodes.forEach(n => {{
  const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
  const r = masteryRadius(n.mastery);

  // Frontier ring
  if (n.isFrontier) {{
    const ring = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    ring.setAttribute("cx", n.x); ring.setAttribute("cy", n.y);
    ring.setAttribute("r", r + 6);
    ring.setAttribute("class", "frontier-ring");
    g.appendChild(ring);
  }}

  // Main circle
  const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  circle.setAttribute("cx", n.x); circle.setAttribute("cy", n.y);
  circle.setAttribute("r", r);
  circle.setAttribute("fill", masteryColor(n.mastery));
  circle.setAttribute("class", "node-circle");
  circle.setAttribute("stroke", n.isFrontier ? "#ffd700" : "#222");
  g.appendChild(circle);

  // Label
  const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
  text.setAttribute("x", n.x); text.setAttribute("y", n.y - r - 10);
  text.setAttribute("class", "node-label");
  text.textContent = n.title;
  g.appendChild(text);

  // Mastery %
  const pct = document.createElementNS("http://www.w3.org/2000/svg", "text");
  pct.setAttribute("x", n.x); pct.setAttribute("y", n.y + 5);
  pct.setAttribute("class", "mastery-label");
  pct.setAttribute("fill", "#fff");
  pct.textContent = n.mastery + "%";
  g.appendChild(pct);

  // Tooltip
  circle.addEventListener("mouseenter", (ev) => {{
    const tags = n.tags.length ? n.tags.join(", ") : "N/A";
    tooltip.innerHTML = `
      <div class="tt-title">${{n.title}}</div>
      <div class="tt-row"><span>狀態</span><span>${{n.status}}</span></div>
      <div class="tt-row"><span>科目</span><span>${{n.subject}}</span></div>
      <div class="tt-row"><span>標籤</span><span>${{tags}}</span></div>
      <div class="tt-row"><span>精熟度</span><span>${{n.mastery}}%</span></div>
      <div class="mastery-bar"><div class="mastery-bar-fill" style="width:${{n.mastery}}%;background:${{masteryColor(n.mastery)}}"></div></div>
      ${{n.isFrontier ? '<div style="color:#ffd700;margin-top:6px">&#x2B50; 知識前沿 - 建議優先學習</div>' : ''}}
    `;
    tooltip.style.display = "block";
  }});
  circle.addEventListener("mousemove", (ev) => {{
    tooltip.style.left = (ev.clientX + 16) + "px";
    tooltip.style.top = (ev.clientY + 16) + "px";
  }});
  circle.addEventListener("mouseleave", () => {{
    tooltip.style.display = "none";
  }});

  svg.appendChild(g);
}});
</script>
</body>
</html>"""
    return html


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate interactive knowledge graph")
    parser.add_argument("--topics", default="topics", help="Path to topics directory")
    parser.add_argument("--subject", default=None, help="Filter by subject (e.g. math)")
    parser.add_argument("--output", default="output/knowledge-graph.html",
                        help="Output HTML file path")
    args = parser.parse_args()

    # Resolve paths relative to repo root
    repo_root = Path(__file__).resolve().parent.parent
    topics_dir = repo_root / args.topics
    output_path = repo_root / args.output

    print(f"Loading topics from: {topics_dir}")
    topics = load_topics(str(topics_dir), args.subject)

    if not topics:
        print("No topics found! Add .md files with YAML frontmatter to topics/", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(topics)} topics")

    frontier = find_frontier(topics)
    stats = compute_stats(topics)

    print(f"\n--- Stats ---")
    print(f"  Total:       {stats['total']}")
    print(f"  Mastered:    {stats['mastered']}")
    print(f"  Learning:    {stats['learning']}")
    print(f"  Not started: {stats['not_started']}")
    print(f"  Avg mastery: {stats['avg_mastery']}%")
    print(f"\n--- Knowledge Frontier ---")
    for fid in frontier:
        t = next((t for t in topics if t["id"] == fid), None)
        name = t["title"] if t else fid
        print(f"  -> {name}")

    # Generate HTML
    html = generate_html(topics, frontier, stats)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"\nGraph written to: {output_path}")


if __name__ == "__main__":
    main()

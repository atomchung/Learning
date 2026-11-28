import sys, re, json, html
from html.parser import HTMLParser
p = sys.argv[1]
s = open(p, encoding='utf-8', errors='replace').read()
def first(rx):
    m = re.search(rx, s, re.I|re.S); return html.unescape(m.group(1)).strip() if m else None
print("FILE", p.split('/')[-1])
print("title:", first(r'<title[^>]*>(.*?)</title>'))
print("meta description:", first(r'<meta[^>]+name="description"[^>]+content="([^"]*)"') or first(r'<meta[^>]+content="([^"]*)"[^>]+name="description"'))
print("canonical:", first(r'<link[^>]+rel="canonical"[^>]+href="([^"]*)"'))
for k in ['article:modified_time','article:published_time','og:updated_time']:
    v = first(r'<meta[^>]+property="%s"[^>]+content="([^"]*)"' % k)
    if v: print(k, v)
blocks = re.findall(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', s, re.S|re.I)
print("json-ld blocks:", len(blocks))
def types(o, out):
    if isinstance(o, dict):
        t = o.get('@type')
        if t: out.append((t, {k: (o[k] if isinstance(o[k], str) else '…') for k in ('headline','name','datePublished','dateModified') if k in o}))
        for v in o.values(): types(v, out)
    elif isinstance(o, list):
        for v in o: types(v, out)
for b in blocks:
    try:
        o = json.loads(b); out=[]; types(o, out)
        for t, d in out[:12]: print("  @type", t, d)
    except Exception as e: print("  parse error", e, b[:200])
# headings
class H(HTMLParser):
    def __init__(s): super().__init__(); s.cur=None; s.buf=''; s.hs=[]
    def handle_starttag(s, t, a):
        if t in ('h1','h2','h3'): s.cur=t; s.buf=''
    def handle_endtag(s, t):
        if t==s.cur: s.hs.append((t, re.sub(r'\s+',' ',s.buf).strip())); s.cur=None
    def handle_data(s, d):
        if s.cur: s.buf+=d
h=H(); h.feed(s)
for t, x in h.hs[:60]:
    if x: print(" ", t, x[:120])
# visible text length & FAQ markers
txt = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S|re.I)
txt = re.sub(r'<[^>]+>', ' ', txt); txt = html.unescape(re.sub(r'\s+',' ',txt))
print("visible words ~", len(txt.split()))
for kw in ['300 emails','300 email','per day','Last updated','Updated','updated on']:
    i = txt.find(kw)
    if i>=0: print(f"  [{kw}] …{txt[max(0,i-120):i+120]}…")

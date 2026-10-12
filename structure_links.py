"""Site structure + internal linking: breadcrumbs point at hub pages, every indexable page gets related links,
hubs and tools are linked from the homepage and the directory."""
import glob, html as H, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://4kaustraliaiptv.com'
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)

HUBS = 'devices|sports|guides|comparisons|isps|languages|cities'
BC_HREF = re.compile(r'href="((?:\.\./)+)directory/index\.html#(%s)"' % HUBS)
BC_LD = re.compile(r'"item": "%s/directory/index\.html#(%s)"' % (re.escape(SITE), HUBS))

# ---- pass 1: collect metadata for indexable pages + fix breadcrumbs
info = {}
fixed_bc = 0
for path in glob.glob('**/*.html', recursive=True):
    rel = path.replace(os.sep, '/')
    s = rd(path); o = s
    s = BC_HREF.sub(lambda m: 'href="%s%s/index.html"' % (m.group(1), m.group(2)), s)
    s = BC_LD.sub(lambda m: '"item": "%s/%s/"' % (SITE, m.group(1)), s)
    if s != o: wr(path, s); fixed_bc += 1
    if 'noindex' in s: continue
    parts = rel.split('/')
    sec = parts[0]
    if sec not in ('devices', 'guides', 'languages', 'comparisons', 'isps', 'sports', 'topic') or len(parts) != 3: continue
    t = re.search(r'<title>(.*?)</title>', s, re.S); t = H.unescape(t.group(1).strip()).split(' | ')[0] if t else parts[1]
    d = re.search(r'name="description" content="([^"]*)"', s); d = H.unescape(d.group(1)) if d else ''
    info[rel] = dict(sec=sec, slug=parts[1], title=t, desc=d)
print('breadcrumbs repointed on pages:', fixed_bc, '| indexable pages for related links:', len(info))

# ---- pass 2: related links
def toks(slug): return set(w for w in re.split(r'[-_]', slug) if len(w) > 2 and w not in ('iptv', 'australia', 'the', 'and', 'for', 'tv', 'app'))
def pillar(slug, title):
    x = (slug + ' ' + title).lower()
    if re.search(r'box|shield|formuler|mag-|android-tv', x): return ('iptv-box-australia', 'IPTV box buying guide', 'fa-box')
    if re.search(r'player|app|tivimate|smarters|ibo|kodi|vlc|m3u|xtream|epg', x): return ('iptv-player-australia', 'Compare IPTV player apps', 'fa-circle-play')
    if re.search(r'trial|free', x): return ('best-iptv-australia', 'Best IPTV Australia guide', 'fa-award')
    return ('iptv-free-trial-australia', 'Start a free 24-hour trial', 'fa-gift')
HUBNAME = {'devices': 'Setup guides', 'sports': 'Sports guides', 'guides': 'All guides', 'comparisons': 'All comparisons', 'isps': 'Internet provider guides', 'languages': 'Language TV guides', 'topic': 'Browse the directory'}
HUBLINK = {'topic': 'directory'}
by_sec = {}
for rel, m in info.items(): by_sec.setdefault(m['sec'], []).append(rel)
n_rel = 0
for rel, m in info.items():
    path = rel.replace('/', os.sep)
    s = rd(path)
    if 'related-section' in s: continue
    pre = '../../'
    me = toks(m['slug'])
    cands = []
    for o in by_sec[m['sec']]:
        if o == rel: continue
        oo = info[o]; ot = toks(oo['slug'])
        j = len(me & ot) / (len(me | ot) or 1)
        cands.append((j, oo['slug'], o))
    cands.sort(key=lambda x: (-x[0], x[1]))
    pick = [c for c in cands if c[0] > 0][:4]
    if len(pick) < 4:   # top up with alphabetical neighbours
        names = sorted(by_sec[m['sec']]); i = names.index(rel)
        for k in (1, -1, 2, -2, 3, -3):
            o = names[(i + k) % len(names)]
            if o != rel and all(o != p[2] for p in pick): pick.append((0, '', o))
            if len(pick) >= 4: break
    cards = ''
    for _, _, o in pick[:4]:
        oo = info[o]
        d = oo['desc'] if len(oo['desc']) <= 120 else oo['desc'][:117].rsplit(' ', 1)[0] + '...'
        cards += '<a class="hub-card" href="%s%s/%s/index.html"><h3>%s</h3><p>%s</p><span>Read more <i class="fa-solid fa-arrow-right"></i></span></a>' % (pre, '../' * 0 + m['sec'], oo['slug'], H.escape(oo['title'], quote=False), H.escape(d, quote=False))
    ps, pn, pi = pillar(m['slug'], m['title'])
    hub_href = '%s%s/index.html' % (pre, HUBLINK.get(m['sec'], m['sec']))
    block = ('\n  <section class="related-section" style="padding:3.5rem 0; background:var(--bg-secondary);"><div class="container">'
             '<h2 class="section-title" style="font-size:1.4rem; margin-top:0;">Related %s</h2><div class="hub-grid" style="grid-template-columns:repeat(4,1fr);">%s</div>'
             '<div class="chip-row" style="margin-top:1.5rem;"><a href="%s%s/index.html"><i class="fa-solid %s"></i> %s</a><a href="%s"><i class="fa-solid fa-layer-group"></i> %s</a>'
             '<a href="%sbest-iptv-australia/index.html"><i class="fa-solid fa-award"></i> Best IPTV Australia</a></div></div></section>\n') % (
        'topics' if m['sec'] == 'topic' else 'guides', cards, pre, ps, pi, pn, hub_href, HUBNAME[m['sec']], pre)
    k = s.find('<footer')
    if k < 0: continue
    wr(path, s[:k] + block + s[k:]); n_rel += 1
print('related-link blocks added:', n_rel)

# ---- pass 3: link hubs + tools from the homepage and the directory
s = rd('index.html')
if 'tools/iptv-bandwidth-calculator' not in s:
    s = s.replace('<span>Popular searches:</span>', '<span>Popular searches:</span>\n        <a href="tools/iptv-bandwidth-calculator/index.html">IPTV bandwidth calculator</a>\n        <a href="devices/index.html">Setup guides</a>\n        <a href="sports/index.html">Sports guides</a>\n        <a href="guides/index.html">IPTV guides</a>\n        <a href="cities/index.html">IPTV by city</a>', 1)
    wr('index.html', s)
d = rd('directory/index.html')
if 'id="sections"' not in d:
    def lk(h, t, ic): return '<a href="../%s" class="nav-link" style="padding:0.4rem 0.6rem; font-size:0.88rem;"><i class="fa-solid %s" style="font-size:0.7rem; color:var(--primary);"></i> %s</a>' % (h, ic, t)
    items = ''.join([lk('devices/index.html', 'Setup guides by device', 'fa-tv'), lk('sports/index.html', 'Sports on IPTV', 'fa-futbol'), lk('guides/index.html', 'IPTV guides', 'fa-book-open'),
                     lk('comparisons/index.html', 'IPTV vs Foxtel, Kayo and more', 'fa-scale-balanced'), lk('isps/index.html', 'Internet providers and NBN', 'fa-network-wired'),
                     lk('languages/index.html', 'Language TV', 'fa-language'), lk('cities/index.html', 'IPTV by city', 'fa-location-dot'), lk('tools/index.html', 'Free tools', 'fa-gauge-high')])
    card = ('\n      <div class="glass-card" id="sections" style="margin-bottom:2.5rem;"><h2 style="font-size:1.6rem; margin-bottom:1.25rem;"><i class="fa-solid fa-sitemap" style="color:var(--primary); margin-right:0.5rem;"></i> Browse by Section</h2>'
            '<div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:0.75rem;">%s</div></div>' % items)
    m = re.search(r'<div class="glass-card" id="buying-guides"', d) or re.search(r'<div class="glass-card" id="cities"', d)
    d = d[:m.start()] + card.lstrip('\n') + '\n      ' + d[m.start():]
    wr('directory/index.html', d)
print('DONE')

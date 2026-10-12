"""SEO pass 2: noindex templated sports sub-pages, unique city intros, Organization/WebSite schema, lighter font request."""
import glob, html as H, json, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://4kaustraliaiptv.com'
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)
MODE = sys.argv[1] if len(sys.argv) > 1 else 'all'

# ---- short titles (report only)
if MODE == 'titles':
    for f in glob.glob('**/*.html', recursive=True):
        s = rd(f); m = re.search(r'<title>(.*?)</title>', s, re.S)
        if m and len(H.unescape(m.group(1)).strip()) < 30 and 'noindex' not in s:
            print(len(m.group(1)), f.replace(os.sep, '/'), '|', H.unescape(m.group(1)))
    raise SystemExit

# ---- 1. sports sub-pages: templated copies of the main sport page -> noindex,follow, drop from sitemap
removed = set()
n_sports = 0
for f in glob.glob('sports/*/*/index.html'):
    s = rd(f)
    if 'noindex' in s: continue
    s = re.sub(r'\s*<meta name="robots"[^>]*>', '', s)
    s = s.replace('</head>', '  <meta name="robots" content="noindex, follow" />\n</head>', 1)
    wr(f, s); n_sports += 1
    removed.add('%s/%s/' % (SITE, f.replace(os.sep, '/')[:-len('index.html')].rstrip('/')))
for sm in glob.glob('sitemap-*.xml'):
    x = rd(sm)
    y = re.sub(r'\s*<url>\s*<loc>(.*?)</loc>.*?</url>', lambda m: '' if m.group(1) in removed else m.group(0), x, flags=re.S)
    if y != x: wr(sm, y)
print('sports sub-pages set to noindex:', n_sports)

# ---- 1b. topic pages: drop pages that target piracy-site names or the homepage keyword, and fix "Australia Australia" titles
BAD = re.compile(r'^(crack|cracked|cricstream|mmastream|streamfree|streameast|sportsurge|totalsportek|buffstream)|^iptv-australia$')
n_bad = n_dup = 0
for f in glob.glob('topic/*/index.html'):
    slug = f.replace(os.sep, '/').split('/')[1]
    s = rd(f); o = s
    if BAD.search(slug) and 'noindex' not in s:
        s = re.sub(r'\s*<meta name="robots"[^>]*>', '', s).replace('</head>', '  <meta name="robots" content="noindex, follow" />\n</head>', 1)
        removed.add('%s/topic/%s/' % (SITE, slug)); n_bad += 1
    if ' Australia Australia' in s:
        s = s.replace(' Australia Australia', ' Australia'); n_dup += 1
    if s != o: wr(f, s)
FIXED = {'comparisons/binge-alternative-iptv-australia/index.html': ('Binge Australia Alternative', 'Binge Alternative Australia: IPTV Options Compared'),
         'comparisons/sky-sports-uk-australia-iptv/index.html': ('Sky Sports UK in Australia', 'Sky Sports UK in Australia: How to Watch Premier League')}
for f, (old, new) in FIXED.items():
    s = rd(f)
    s = s.replace('<title>%s</title>' % old, '<title>%s</title>' % new).replace('content="%s"' % old, 'content="%s"' % new)
    wr(f, s)
for sm in glob.glob('sitemap-*.xml'):
    x = rd(sm)
    y = re.sub(r'\s*<url>\s*<loc>(.*?)</loc>.*?</url>', lambda m: '' if m.group(1) in removed else m.group(0), x, flags=re.S)
    if y != x: wr(sm, y)
print('topic pages noindexed (piracy-name / homepage keyword):', n_bad, ' titles de-duplicated:', n_dup)

# ---- 2. unique local intro for the 10 city hubs (+ one local line on each of their sub-pages)
CITY = {
 'sydney': ('Sydney', 'the Sydney Swans and GWS Giants in the AFL, the Sydney Roosters, South Sydney Rabbitohs and Parramatta Eels in the NRL, and Sydney FC in the A-League', 'State of Origin nights and Friday night football'),
 'melbourne': ('Melbourne', 'Collingwood, Richmond, Carlton, Essendon and Hawthorn in the AFL, Melbourne Storm in the NRL, and Melbourne City and Melbourne Victory in the A-League', 'the AFL finals, the Australian Open and the Spring Racing Carnival'),
 'brisbane': ('Brisbane', 'the Brisbane Lions in the AFL, the Brisbane Broncos in the NRL, and Brisbane Roar in the A-League', 'State of Origin and Gabba cricket'),
 'perth': ('Perth', 'West Coast Eagles and Fremantle in the AFL, the Perth Scorchers in the Big Bash, and Perth Glory in the A-League', 'late-afternoon AFL matches and summer cricket at Optus Stadium'),
 'adelaide': ('Adelaide', 'Adelaide Crows and Port Adelaide in the AFL, the Adelaide Strikers in the Big Bash, and Adelaide United in the A-League', 'Showdown matches and Test cricket at Adelaide Oval'),
 'canberra': ('Canberra', 'the Canberra Raiders in the NRL and the ACT Brumbies in Super Rugby Pacific', 'Raiders home games and Brumbies season fixtures'),
 'hobart': ('Hobart', 'the Hobart Hurricanes in the Big Bash, with AFL and NRL followed closely across Tasmania', 'summer cricket and the Hobart International tennis'),
 'darwin': ('Darwin', 'the AFL, NRL and Supercars events followed across the Top End', 'AFL Top End fixtures and Supercars weekends'),
 'gold-coast': ('Gold Coast', 'the Gold Coast Suns in the AFL and the Gold Coast Titans in the NRL', 'Suns and Titans home games'),
 'newcastle': ('Newcastle', 'the Newcastle Knights in the NRL and the Newcastle Jets in the A-League', 'Knights home games and Jets match days'),
}
n_city = 0
for slug, (name, teams, big) in CITY.items():
    for f in glob.glob('cities/%s/index.html' % slug) + glob.glob('cities/%s/*/index.html' % slug):
        s = rd(f)
        if 'local-intro' in s: continue
        is_hub = f.replace(os.sep, '/') == 'cities/%s/index.html' % slug
        if is_hub:
            block = ('<section style="padding:3rem 0 0; background:var(--bg-main);"><div class="container"><div class="glass-card local-intro" style="max-width:980px; margin:0 auto;">'
                     '<h2 class="section-title" style="font-size:1.5rem; margin-top:0;">Watching live sport in %s</h2>'
                     '<p style="line-height:1.8;">If you follow %s, you want a stream that holds up when the game starts. %s is one of the busiest viewing times of the week, so test your IPTV service on your own %s home internet during a live match. Our free 24-hour trial lets you do exactly that before you pay.</p>'
                     '<p style="line-height:1.8; margin-bottom:0;">Setting up is quick on a Fire TV Stick, Android TV box, Apple TV, Samsung or LG TV. See the <a href="../../iptv-box-australia/index.html">IPTV box guide</a> and the <a href="../../iptv-player-australia/index.html">IPTV player guide</a>, then <a href="../../iptv-free-trial-australia/index.html">start your free trial</a>.</p>'
                     '</div></div></section>\n') % (name, teams, big[0].upper() + big[1:], name)
            m = re.search(r'<section class="section-padding-lg|<section style="padding: ?4rem', s)
            if not m: m = re.search(r'<section class="faq-section"', s)
            if m: s = s[:m.start()] + block + s[m.start():]
        else:
            line = '<p class="local-intro" style="margin:.75rem 0 0; font-size:.95rem; color:var(--text-muted);">Local to %s: viewers here follow %s.</p>' % (name, teams)
            m = re.search(r'(<p class="hero-description"[^>]*>.*?</p>)', s, re.S)
            if m: s = s[:m.end()] + line + s[m.end():]
        wr(f, s); n_city += 1
print('city pages with local text:', n_city)

# ---- 3. homepage: Organization + WebSite schema
s = rd('index.html')
if '"@type": "Organization"' not in s:
    org = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": SITE + "/#org", "name": "4K Australia IPTV", "url": SITE + "/", "logo": SITE + "/assets/og-au.png",
         "contactPoint": [{"@type": "ContactPoint", "contactType": "customer support", "email": "support@4kaustraliaiptv.com", "telephone": "+212625218443", "availableLanguage": ["English"]}]},
        {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "4K Australia IPTV", "inLanguage": "en-AU", "publisher": {"@id": SITE + "/#org"}}]}
    s = s.replace('</head>', '  <script type="application/ld+json">\n' + json.dumps(org, indent=2) + '\n  </script>\n</head>', 1)
    wr('index.html', s)
print('homepage schema ok')

# ---- 4. lighter font request on every page (Space Grotesk is replaced by Inter tabular numbers)
n_font = 0
for f in glob.glob('**/*.html', recursive=True):
    t = rd(f)
    u = t.replace('&family=Space+Grotesk:wght@500;600;700', '')
    if u != t: wr(f, u); n_font += 1
css = rd('assets/css/style.css')
css = css.replace("--font-mono: 'Space Grotesk', monospace;", "--font-mono: 'Inter', -apple-system, 'Segoe UI', sans-serif;")
if 'font-variant-numeric: tabular-nums;} /*mono*/' not in css:
    css += "\n.ping-val, .stat-num, .price-big, .result-value, .slider-val { font-variant-numeric: tabular-nums; } /*mono*/\n"
wr('assets/css/style.css', css)
print('pages with lighter font request:', n_font)
print('DONE')

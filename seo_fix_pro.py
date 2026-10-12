"""Technical SEO pass: removes fake ratings, shortens titles, adds canonical/og/hreflang, noindexes off-topic pages."""
import glob, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
BASE = os.path.dirname(os.path.abspath(__file__)); os.chdir(BASE)
SITE = 'https://4kaustraliaiptv.com'
KEEP_CITIES = {'sydney','melbourne','brisbane','perth','adelaide','canberra','hobart','darwin','gold-coast','newcastle'}
REL = re.compile(r'iptv|firestick|fire-stick|box|player|app\b|apps|trial|reseller|smarters|tivimate|android|kodi|m3u|xtream|stalker|mag-|formuler|chromecast|shield|apple-tv|samsung|lg-|stream|subscription|provider|vpn|dns|buffer|panel|channel')
HOME_TITLE = 'IPTV Australia | Best IPTV Subscription & Reseller Panel 2026'

def esc(t): return t.replace('&', '&amp;') if '&amp;' not in t else t

def short_title(t):
    raw = t.replace('&amp;', '&')
    if len(raw) <= 60: return t
    parts = [p.strip() for p in raw.split('|')]
    head = parts[0]
    for cand in (head + ' | IPTV Australia', head):
        if len(cand) <= 60: return esc(cand)
    return esc(head[:57].rsplit(' ', 1)[0] + '...')

def is_noindex(rel):
    p = rel.split('/')
    if p[0] == 'topic' and len(p) > 2: return not REL.search(p[1])
    if p[0] == 'cities' and len(p) > 2: return p[1] not in KEEP_CITIES
    return False

stats = dict(files=0, rating=0, title=0, noindex=0, canon=0)
noindex_urls = set()
for path in glob.glob('**/*.html', recursive=True):
    rel = path.replace(os.sep, '/')
    s = open(path, encoding='utf8', errors='surrogateescape').read(); o = s
    url = SITE + '/' + ('' if rel == 'index.html' else (rel[:-10] if rel.endswith('/index.html') else rel))
    # 1 fake ratings
    s, n = re.subn(r',\s*"aggregateRating":\s*\{[^}]*\}', '', s); stats['rating'] += n
    # 2 titles
    m = re.search(r'<title>(.*?)</title>', s, re.S)
    if m:
        nt = HOME_TITLE.replace('&', '&amp;') if rel == 'index.html' else short_title(m.group(1).strip())
        if nt != m.group(1).strip():
            s = s.replace(m.group(0), '<title>%s</title>' % nt, 1); stats['title'] += 1
            s = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda x: x.group(1) + nt + x.group(2), s, 1)
    # 3 meta keywords
    s = re.sub(r'\s*<meta name="keywords"[^>]*>', '', s)
    head_add = ''
    # 4 canonical
    if 'rel="canonical"' not in s:
        head_add += '  <link rel="canonical" href="%s" />\n' % url; stats['canon'] += 1
    # 5 hreflang
    if 'hreflang' not in s:
        head_add += '  <link rel="alternate" hreflang="en-AU" href="%s" />\n  <link rel="alternate" hreflang="x-default" href="%s" />\n' % (url, url)
    # 6 og/twitter image
    if 'og:image' not in s:
        head_add += ('  <meta property="og:image" content="%s/assets/og-au.png" />\n  <meta property="og:image:width" content="1200" />\n'
                     '  <meta property="og:image:height" content="630" />\n  <meta name="twitter:image" content="%s/assets/og-au.png" />\n') % (SITE, SITE)
    if 'twitter:card' not in s:
        head_add += '  <meta name="twitter:card" content="summary_large_image" />\n'
    # 7 noindex
    if is_noindex(rel):
        s = re.sub(r'\s*<meta name="robots"[^>]*>', '', s)
        head_add += '  <meta name="robots" content="noindex, follow" />\n'
        stats['noindex'] += 1; noindex_urls.add(url)
    if head_add and '</head>' in s:
        s = s.replace('</head>', head_add + '</head>', 1)
    if s != o:
        open(path, 'w', encoding='utf8', errors='surrogateescape').write(s); stats['files'] += 1

# sitemaps: drop noindexed URLs
for sm in glob.glob('sitemap-*.xml'):
    x = open(sm, encoding='utf8').read()
    def keep(m):
        loc = re.search(r'<loc>(.*?)</loc>', m.group(0)).group(1)
        return '' if loc in noindex_urls else m.group(0)
    y = re.sub(r'\s*<url>.*?</url>', lambda m: keep(m) if keep(m) else '', x, flags=re.S)
    if y != x: open(sm, 'w', encoding='utf8').write(y)
print(stats, 'sitemap urls removed', len(noindex_urls))

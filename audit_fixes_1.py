"""Audit fixes, part 1 (all pages): unsupported numbers/superlatives, heading hierarchy, favicon, hub titles,
homepage vs best-iptv cannibalisation, Premier League page intent."""
import glob, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)

def art(w): return 'An' if w[0].lower() in 'aeiou' else 'A'
REPL = [
 # unverifiable latency / uptime / absolute performance claims
 (re.compile(r' with \d+ ?ms low latency in '), ' in '),
 (re.compile(r'Our servers deliver under \d+ ?ms latency across'), 'Our servers aim for a smooth, low-delay stream across'),
 (re.compile(r'(?:with )?under \d+ ?ms latency directly into'), 'directly into'),
 (re.compile(r'100% NBN Anti-Freeze'), 'Works on NBN'),
 (re.compile(r'Telstra (?:&amp;|&) Optus NBN Anti-Freeze'), 'Telstra &amp; Optus NBN Ready'),
 (re.compile(r'NBN Anti-Freeze'), 'NBN Ready'),
 # superlatives with no evidence
 (re.compile(r'#1 4K '), '4K '),
 (re.compile(r'#1 Australian IPTV Network 2026'), 'Australian IPTV Network 2026'),
 (re.compile(r'<span class="logo-sub">#1 Network 2026</span>'), '<span class="logo-sub">IPTV for Australia</span>'),
 (re.compile(r'<span class="logo-sub">#1 Reseller Hub 2026</span>'), '<span class="logo-sub">IPTV Reseller Hub</span>'),
 (re.compile(r'The #1 highest-rated IPTV player app'), 'A popular IPTV player app'),
 (re.compile(r'The #1 (\w+) IPTV service'), lambda m: '%s %s IPTV service' % (art(m.group(1)), m.group(1))),
 # marketing filler
 (re.compile(r'with cutting-edge anti-freeze technology'), 'with a connection tuned for NBN'),
 (re.compile(r'connects seamlessly on all'), 'connects on all'),
 (re.compile(r'enjoy seamless home entertainment tailored specifically for'), 'watch live TV and sport at home, built for'),
 (re.compile(r'Power your streaming empire or'), 'Run your own IPTV reselling business or'),
 (re.compile(r'\bThe Ultimate Guide for\b'), 'A guide for'),
 (re.compile(r'\bthe ultimate guide for\b'), 'a guide for'),
 (re.compile(r'Whether you are watching Friday night footy at home or'), 'If you watch Friday night footy at home or'),
 (re.compile(r'whether you are watching Friday night footy at home or'), 'if you watch Friday night footy at home or'),
]
HERO_H3 = re.compile(r'(<div class="portal-card-header">\s*<div>\s*)<h3 style="[^"]*">(.*?)</h3>', re.S)
ICON = '<link rel="icon" href="%sfavicon.svg" type="image/svg+xml" />\n<link rel="icon" href="%sfavicon-48.png" sizes="48x48" type="image/png" />\n<link rel="apple-touch-icon" href="%sapple-touch-icon.png" />\n'
stats = dict(files=0, h3=0, icon=0)
for path in glob.glob('**/*.html', recursive=True):
    rel = path.replace(os.sep, '/')
    s = rd(path); o = s
    for rx, rep in REPL: s = rx.sub(rep, s)
    s, n = HERO_H3.subn(lambda m: m.group(1) + '<div class="portal-title">' + m.group(2) + '</div>', s); stats['h3'] += n
    if 'rel="icon"' not in s:
        pre = '../' * rel.count('/')
        s = s.replace('</head>', ICON % (pre, pre, pre) + '</head>', 1); stats['icon'] += 1
    if s != o: wr(path, s); stats['files'] += 1
print(stats)

# ---- hub titles inside the 50-62 character range
for p, old, new in (('devices/index.html', 'IPTV Setup Guides: Fire Stick, Android TV, Apple TV, Samsung, LG', 'IPTV Setup Guides for Fire Stick, Android TV, Apple TV, LG'),
                    ('guides/index.html', 'IPTV Guides Australia: Buffering, VPN, Legal, Payments and Setup', 'IPTV Guides Australia: Buffering, VPN, Legal and Setup'),
                    ('languages/index.html', 'Arabic, Indian, Greek, Italian, Chinese, Filipino TV on IPTV Australia', 'Arabic, Indian, Greek, Italian, Chinese TV on IPTV Australia'),
                    ('sports/index.html', 'Australian Sport on IPTV: AFL, NRL, Cricket, F1, UFC and Soccer', 'Australian Sport on IPTV: AFL, NRL, Cricket, F1 and UFC')):
    s = rd(p); s = s.replace(old, new); wr(p, s)
for scr, pairs in (('build_hubs.py', (('IPTV Setup Guides: Fire Stick, Android TV, Apple TV, Samsung, LG', 'IPTV Setup Guides for Fire Stick, Android TV, Apple TV, LG'), ('IPTV Guides Australia: Buffering, VPN, Legal, Payments and Setup', 'IPTV Guides Australia: Buffering, VPN, Legal and Setup'),
                                    ('Arabic, Indian, Greek, Italian, Chinese, Filipino TV on IPTV Australia', 'Arabic, Indian, Greek, Italian, Chinese TV on IPTV Australia'), ('Australian Sport on IPTV: AFL, NRL, Cricket, F1, UFC and Soccer', 'Australian Sport on IPTV: AFL, NRL, Cricket, F1 and UFC'))),):
    t = rd(scr)
    for a, b in pairs: t = t.replace(a, b)
    wr(scr, t)

# ---- homepage owns "IPTV Australia"; the guide page owns "best IPTV Australia"
s = rd('index.html')
s = s.replace('<title>Best IPTV Australia 2026 | IPTV Subscription &amp; Reseller Panel</title>', '<title>IPTV Australia: Subscription, Free Trial &amp; Reseller Panel</title>')
s = s.replace('content="Best IPTV Australia 2026 | IPTV Subscription &amp; Reseller Panel"', 'content="IPTV Australia: Subscription, Free Trial &amp; Reseller Panel"')
s = re.sub(r'(name="description" content=")[^"]*(")', r'\1Watch Australian TV and 4K live sport with an IPTV subscription in AUD. Start a free 24-hour trial, compare 3, 6 and 12-month plans, or join the reseller panel.\2', s, 1)
s = re.sub(r'(property="og:description" content=")[^"]*(")', r'\1Watch Australian TV and 4K live sport with an IPTV subscription in AUD. Start a free 24-hour trial, compare plans, or join the reseller panel.\2', s, 1)
s = re.sub(r'(<h1 class="hero-title">\s*)Best IPTV Australia: <span class="gradient-text">IPTV Subscription &amp; Reseller Panel</span> with 4K Live Sports',
           r'\1IPTV Australia: <span class="gradient-text">Subscription, Free Trial &amp; Reseller Panel</span> with 4K Live Sports', s, 1)
s = s.replace('The best IPTV Australia has to offer is the service that runs smoothly on your own NBN connection, carries the sport you watch and lets you test it first. ',
              'An IPTV subscription in Australia works best when it runs smoothly on your own NBN connection, carries the sport you watch and lets you test it first. ')
wr('index.html', s)

# ---- Premier League page: "how to watch", leaving "Optus Sport alternative" to the comparison page
p = 'sports/premier-league-optus-sport-alternative/index.html'
s = rd(p)
s = s.replace('English Premier League 4K (Optus Sport Alternative)', 'Premier League in Australia: Kick-off Times and Setup')
s = re.sub(r'(<h1[^>]*>)(.*?)(</h1>)', r'\1Premier League in Australia: Kick-off Times and Setup\3', s, 1, flags=re.S)
s = re.sub(r'(name="description" content=")[^"]*(")', r'\1How to watch the English Premier League in Australia: match times in your time zone, what you need and how to keep the stream steady on NBN.\2', s, 1)
s = re.sub(r'(property="og:description" content=")[^"]*(")', r'\1How to watch the English Premier League in Australia: match times in your time zone, what you need and how to keep the stream steady on NBN.\2', s, 1)
s = re.sub(r'(<p class="hero-description"[^>]*>)(.*?)(</p>)', r'\1English Premier League matches usually kick off overnight or early morning in Australia. Set your guide to Australian time, test your stream the night before and use a wired connection for a steady picture. Comparing services? See the <a href="../../comparisons/optus-sport-alternative-iptv-australia/index.html">Optus Sport alternative comparison</a>.\3', s, 1, flags=re.S)
wr(p, s)
print('part 1 done')
print('DONE')

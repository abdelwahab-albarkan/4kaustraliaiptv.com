"""Adds a small 'regional sites' section (sister sites) to the homepage and About page."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITES = [
    ('Germany', 'fa-earth-europe', [('4kdeutsch.com', 'IPTV in Deutsch'), ('4kanbieteriptv.de', 'IPTV Anbieter'), ('germanystreamtv.com', 'Germany Stream TV'), ('streamgermany4k.com', 'Stream Germany 4K')]),
    ('France', 'fa-earth-europe', [('4kiptvfr.com', 'IPTV France')]),
    ('Spain', 'fa-earth-europe', [('4kspaintv.com', 'TV Spain')]),
    ('United Kingdom', 'fa-earth-europe', [('ukstream4k.com', 'UK Stream 4K')]),
    ('International', 'fa-globe', [('4ksubscriptioniptv.com', '4K Subscription IPTV')]),
]
def block():
    groups = ''
    for region, icon, links in SITES:
        chips = ''.join('<a href="https://%s/" target="_blank" rel="noopener" title="%s">%s</a>' % (d, name, d) for d, name in links)
        groups += '<div class="region-group"><h3><i class="fa-solid %s"></i> %s</h3><div class="chip-row" style="margin-top:.5rem;">%s</div></div>' % (icon, region, chips)
    return ('\n  <section class="regional-sites" id="regional-sites" style="padding:3.5rem 0; background:var(--bg-secondary);"><div class="container">'
            '<h2 class="section-title" style="font-size:1.5rem; margin-top:0;">Our regional sites</h2>'
            '<p style="max-width:44rem; line-height:1.7;">Watching from outside Australia? We run IPTV sites for viewers in other countries, with content written for each region.</p>'
            '<div class="region-grid">%s</div></div></section>\n') % groups
n = 0
for page in ('index.html', 'about/index.html'):
    s = open(page, encoding='utf8', errors='surrogateescape').read()
    if 'id="regional-sites"' in s: continue
    k = s.find('<footer')
    s = s[:k] + block() + s[k:]
    open(page, 'w', encoding='utf8', errors='surrogateescape').write(s); n += 1
print('pages updated:', n)

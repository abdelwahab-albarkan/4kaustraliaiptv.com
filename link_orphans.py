"""Internal linking pass: links the 4 new landing pages from every footer, links city sub-pages from their city page,
adds a topics hub to the directory, and removes the repeated brand suffix from topic titles."""
import glob, html as H, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
KEEP = ['sydney', 'melbourne', 'brisbane', 'perth', 'adelaide', 'canberra', 'hobart', 'darwin', 'gold-coast', 'newcastle']
LAND = [('best-iptv-australia', 'Best IPTV Australia'), ('iptv-box-australia', 'IPTV Box Australia'),
        ('iptv-player-australia', 'IPTV Player Apps'), ('iptv-free-trial-australia', 'IPTV Free Trial')]
SUB = [('best-iptv', 'Best IPTV in {c}'), ('subscription', 'IPTV Subscription {c}'), ('free-trial', 'IPTV Free Trial {c}'),
       ('firestick-setup', 'Firestick IPTV Setup {c}'), ('sports-channels', 'AFL &amp; NRL IPTV {c}'), ('reseller-panel', 'IPTV Reseller Panel {c}')]

def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)

stats = dict(footer=0, city=0, topic_titles=0)
for path in glob.glob('**/*.html', recursive=True):
    rel = path.replace(os.sep, '/'); parts = rel.split('/')
    s = rd(path); o = s
    prefix = '../' * (len(parts) - 1)
    # 1. footer links to the landing pages (first footer link list only)
    if 'best-iptv-australia/index.html' not in s and 'footer-links-list' in s and parts[0] not in LAND[0][0:1]:
        items = ''.join('<li><a href="%s%s/index.html">%s</a></li>' % (prefix, slug, name) for slug, name in LAND)
        s = s.replace('</ul>', items + '</ul>', 1) if s.find('footer-links-list') < s.find('</ul>', s.find('footer-links-list')) and False else \
            re.sub(r'(<ul class="footer-links-list">.*?)(</ul>)', lambda m: m.group(1) + items + m.group(2), s, 1, flags=re.S)
        stats['footer'] += 1
    # 2. city page: link its sub-pages + landing pages
    if len(parts) == 3 and parts[0] == 'cities' and parts[1] in KEEP and 'More IPTV' not in s:
        slug = parts[1]; city = slug.replace('-', ' ').title()
        links = ''.join('<a href="%s/index.html">%s</a>' % (sub, t.format(c=city)) for sub, t in SUB)
        links += ''.join('<a href="../../%s/index.html">%s</a>' % (a, b) for a, b in LAND)
        block = ('\n  <section style="padding:3rem 0; background:var(--bg-secondary);">\n    <div class="container">\n      <h2 class="section-title" style="font-size:1.5rem; margin-top:0;">More IPTV %s guides</h2>\n'
                 '      <div class="chip-row" style="margin-top:1rem;">%s</div>\n    </div>\n  </section>\n') % (city, links)
        m = re.search(r'<section class="faq-section"', s)
        if m: s = s[:m.start()] + block + s[m.start():]; stats['city'] += 1
    # 3. topic titles: drop the repeated brand suffix so the homepage owns that keyword
    if parts[0] == 'topic' and len(parts) == 3:
        m = re.search(r'<title>(.*?) \| IPTV Australia</title>', s)
        if m:
            t = m.group(1)
            s = s.replace(m.group(0), '<title>%s</title>' % t, 1)
            s = s.replace('content="%s | IPTV Australia"' % t, 'content="%s"' % t)
            stats['topic_titles'] += 1
    if s != o: wr(path, s)

# 4. directory: buying guides + hub for every indexable topic and sports sub-page
d = rd('directory/index.html')
if 'id="buying-guides"' not in d:
    def link(href, text): return '<a href="../%s" class="nav-link" style="padding:0.4rem 0.6rem; font-size:0.88rem;"><i class="fa-solid fa-arrow-right" style="font-size:0.7rem; color:var(--primary);"></i> %s</a>' % (href, text)
    guides = ''.join(link(s_ + '/index.html', n) for s_, n in LAND)
    topics = []
    for t in sorted(glob.glob('topic/*/index.html')):
        s = rd(t)
        if 'noindex' in s: continue
        h = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
        name = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h.group(1))).strip() if h else t.split('/')[1]
        topics.append(link(t, name.replace(' in Australia', '')))
    sports = []
    for t in sorted(glob.glob('sports/*/*/index.html')):
        s = rd(t); h = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
        name = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h.group(1))).strip() if h else t.split('/')[2]
        sports.append(link(t, name))
    def card(cid, title, icon, items, cols=3):
        return ('\n      <div class="glass-card" id="%s" style="margin-bottom:2.5rem;">\n        <h2 style="font-size:1.6rem; margin-bottom:1.25rem;"><i class="fa-solid %s" style="color:var(--primary); margin-right:0.5rem;"></i> %s</h2>\n'
                '        <div style="display:grid; grid-template-columns:repeat(%d, 1fr); gap:0.75rem;">%s</div>\n      </div>') % (cid, icon, title, cols, ''.join(items))
    add = card('buying-guides', 'IPTV Buying Guides', 'fa-award', [guides]) + (card('sports-guides', 'Sports Guides: Without Foxtel &amp; Fixtures', 'fa-futbol', sports) if sports else '') + card('topics', 'Popular Topics', 'fa-hashtag', topics, 4)
    end = d.find('</section>'); pos = d.rfind('</div>', 0, end)
    d = d[:pos] + add + '\n    ' + d[pos:]
    wr('directory/index.html', d)
    stats['directory_topics'] = len(topics); stats['directory_sports'] = len(sports)

# 5. homepage: send visitors to the landing pages
s = rd('index.html')
if 'iptv-box-australia/index.html' not in s:
    def after_sub(sec_id, text):
        global s
        j = s.find('id="%s"' % sec_id); e = s.find('</section>', j)
        k = s.find('</p>', s.find('section-subtitle', j)) + 4
        if 0 < k < e: s = s[:k] + text + s[k:]
    after_sub('iptv-box-australia', '\n        <p style="margin-top:.75rem;"><a class="btn btn-outline btn-sm" href="iptv-box-australia/index.html">Read the full IPTV box buying guide <i class="fa-solid fa-arrow-right"></i></a></p>')
    after_sub('iptv-player-apps', '\n        <p style="margin-top:.75rem;"><a class="btn btn-outline btn-sm" href="iptv-player-australia/index.html">Compare all IPTV player apps <i class="fa-solid fa-arrow-right"></i></a></p>')
    s = s.replace('<a href="#free-trial">free IPTV trial</a>', '<a href="iptv-free-trial-australia/index.html">free IPTV trial</a>', 1)
    s = s.replace('<span>Popular searches:</span>', '<span>Popular searches:</span>\n        <a href="best-iptv-australia/index.html">Best IPTV Australia</a>\n        <a href="iptv-box-australia/index.html">IPTV box</a>\n        <a href="iptv-player-australia/index.html">IPTV player</a>\n        <a href="iptv-free-trial-australia/index.html">IPTV free trial</a>', 1)
    wr('index.html', s)
print(stats)
print('DONE')

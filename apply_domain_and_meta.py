"""1) points every canonical/og/schema/sitemap URL at the real domain, 2) trims over-long meta descriptions,
3) fixes the sitemap entry for the directory page."""
import glob, html as H, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
OLD = 'iptvaustralia.app'
NEW = '4kaustraliaiptv.com'

def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)

def trim(desc):
    d = H.unescape(desc)
    if len(d) <= 160: return None
    cut = d[:160]
    k = cut.rfind('. ')
    if k >= 90: out = cut[:k + 1]
    else:
        out = cut[:cut.rfind(' ')].rstrip(' ,;:-&|')
        out = re.sub(r'\s+(and|or|for|in|to|of|the|with|on|a|an|at|by)$', '', out, flags=re.I)
        out += '.'
    return out

stats = dict(domain=0, desc=0)
files = glob.glob('**/*.html', recursive=True) + glob.glob('*.xml') + ['robots.txt'] + glob.glob('*.py')
for path in files:
    if path.endswith('apply_domain_and_meta.py'): continue
    s = rd(path); o = s
    s = s.replace(OLD, NEW)
    if path.endswith('.html'):
        m = re.search(r'name="description" content="([^"]*)"', s)
        if m:
            new = trim(m.group(1))
            if new:
                esc = H.escape(new, quote=True)
                s = s.replace(m.group(1), esc)
                s = re.sub(r'(property="og:description" content=")[^"]*(")', lambda x: x.group(1) + esc + x.group(2), s, 1)
                stats['desc'] += 1
    if s != o:
        wr(path, s); stats['domain'] += 1

# sitemap: directory page canonical is /directory/ (trailing slash)
sm = rd('sitemap-core.xml')
sm = sm.replace('https://%s/directory/index.html' % NEW, 'https://%s/directory/' % NEW)
wr('sitemap-core.xml', sm)
for f in glob.glob('sitemap-*.xml'):
    t = rd(f)
    if '/directory/index.html' in t: wr(f, t.replace('https://%s/directory/index.html' % NEW, 'https://%s/directory/' % NEW))
print(stats)
print('DONE')

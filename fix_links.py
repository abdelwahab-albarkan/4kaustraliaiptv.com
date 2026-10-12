"""Fixes broken internal links/anchors found by the link check, without deleting any content."""
import difflib, glob, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)

# ---- 1. homepage: dead page links -> nearest real page, or plain text if there is none
s = rd('index.html')
existing = {sec: sorted(os.listdir(sec)) for sec in ('sports', 'isps', 'devices', 'guides', 'comparisons', 'cities', 'languages')}
fixed = unwrapped = 0
def fix_anchor(m):
    global fixed, unwrapped
    whole, pre, href, post, inner = m.group(0), m.group(1), m.group(2), m.group(3), m.group(4)
    path, _, frag = href.partition('#')
    if not path or re.match(r'(https?:|mailto:|tel:)', path): return whole
    t = path[:-len('/index.html')] if path.endswith('/index.html') else path.rstrip('/')
    if os.path.exists(t) or os.path.exists(path): return whole
    parts = t.split('/')
    if len(parts) == 2 and parts[0] in existing and parts[0] != 'topic':
        best = difflib.get_close_matches(parts[1], existing[parts[0]], n=1, cutoff=0.55)
        if best:
            fixed += 1
            return '<a %shref="%s/%s/index.html"%s>%s</a>' % (pre, parts[0], best[0], post, inner)
    unwrapped += 1
    cls = re.search(r'class="([^"]*)"', pre + post)
    sty = re.search(r'style="([^"]*)"', pre + post)
    return '<span%s%s>%s</span>' % (' class="%s"' % cls.group(1) if cls else '', ' style="%s"' % sty.group(1) if sty else '', inner)
s = re.sub(r'<a ([^>]*?)href="([^"]*)"([^>]*)>(.*?)</a>', fix_anchor, s, flags=re.S)

# ---- 2. homepage anchors that point at ids which do not exist
for a, b in [('#provider-8k', '#providers'), ('#provider-smarter8k', '#providers'), ('#provider-crystal', '#providers'),
             ('#provider-megaott', '#providers'), ('#provider-cyber', '#providers'),
             ('href="#reseller"', 'href="#calculator"'), ('href="#reseller-pricing"', 'href="#pricing"'),
             ('href="#contact"', 'href="#free-trial"'), ('href="#trial"', 'href="#free-trial"')]:
    s = s.replace('href="' + a + '"' if a.startswith('#') else a, 'href="' + b + '"' if b.startswith('#') else b)
wr('index.html', s)
print('homepage links redirected:', fixed, ' dead topic links turned into plain text:', unwrapped)

# ---- 3. root pages: index.html#trial -> #free-trial
for f in glob.glob('*.html'):
    t = rd(f)
    u = t.replace('index.html#trial', 'index.html#free-trial')
    if u != t: wr(f, u); print('anchor fixed in', f)

# ---- 4. directory hub: add the missing Languages / Guides / ISP sections
def h1(p):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', rd(p + '/index.html'), re.S)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else os.path.basename(p)
def short(t): return re.sub(r'\s*(in|for|on)?\s*Australia.*$', '', t).strip() or t
def card(cid, icon, title, sec):
    links = ''.join('<a href="../%s/%s/index.html" class="nav-link" style="padding:0.4rem 0.6rem; font-size:0.88rem;"><i class="fa-solid %s" style="font-size:0.7rem; color:var(--primary);"></i> %s</a>\n          '
                    % (sec, d, icon, short(h1('%s/%s' % (sec, d)))) for d in sorted(os.listdir(sec)))
    return ('\n      <div class="glass-card" id="%s" style="margin-bottom:2.5rem;">\n        <h2 style="font-size:1.6rem; margin-bottom:1.25rem;"><i class="fa-solid %s" style="color:var(--primary); margin-right:0.5rem;"></i> %s</h2>\n'
            '        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:0.75rem;">\n          %s</div>\n      </div>' % (cid, icon, title, links))
d = rd('directory/index.html')
if 'id="languages"' not in d:
    end = d.find('</section>')
    pos = d.rfind('</div>', 0, end)
    add = card('languages', 'fa-language', 'Multicultural &amp; Language TV', 'languages') + card('guides', 'fa-book-open', 'Guides &amp; How-Tos', 'guides') + card('isps', 'fa-network-wired', 'ISP &amp; NBN Optimisation', 'isps') + '\n    '
    d = d[:pos] + add + d[pos:]
    wr('directory/index.html', d); print('directory sections added')

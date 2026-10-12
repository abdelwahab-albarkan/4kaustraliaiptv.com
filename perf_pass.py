"""Performance pass for every page: width/height + lazy/async on images, non-blocking external CSS. Re-runnable."""
import os, re, glob, sys
from urllib.parse import unquote
from PIL import Image
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
dims = {}
def dim(p):
    if p not in dims:
        try:
            with Image.open(p) as im: dims[p] = im.size
        except Exception:
            dims[p] = None
    return dims[p]

FA = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css'
GF = 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
stats = {'pages': 0, 'wh': 0, 'lazy': 0, 'css': 0}
def async_css(s, url):
    tag = '<link rel="stylesheet" href="%s" />' % url
    alt = '<link href="%s" rel="stylesheet" />' % url
    new = '<link rel="stylesheet" href="%s" media="print" onload="this.media=\'all\'" /><noscript><link rel="stylesheet" href="%s" /></noscript>' % (url, url)
    for t in (tag, alt):
        if t in s:
            stats['css'] += 1
            return s.replace(t, new)
    return s

for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf8', errors='surrogateescape').read()
    o = s
    s = async_css(s, FA)
    s = async_css(s, GF)
    count = [0]
    def fix(m):
        t = m.group(0)
        count[0] += 1
        src = re.search(r'\ssrc="([^"]+)"', t)
        if not src: return t
        u = src.group(1).split('?')[0]
        if u.startswith(('http', 'data:')): return t
        u = unquote(u)
        p = u.lstrip('/') if u.startswith('/') else os.path.normpath(os.path.join(os.path.dirname(f), u))
        add = ''
        if ' width=' not in t and ' height=' not in t:
            d = dim(p)
            if d:
                add += ' width="%d" height="%d"' % d; stats['wh'] += 1
        if count[0] > 2 and ' loading=' not in t:
            add += ' loading="lazy"'; stats['lazy'] += 1
        if ' decoding=' not in t:
            add += ' decoding="async"'
        if not add: return t
        return re.sub(r'\s*/?>$', lambda e: add + (' />' if e.group(0).strip().startswith('/') else '>'), t)
    s = re.sub(r'<img\b[^>]*>', fix, s)
    if s != o:
        open(f, 'w', encoding='utf8', errors='surrogateescape').write(s)
        stats['pages'] += 1
print(stats)

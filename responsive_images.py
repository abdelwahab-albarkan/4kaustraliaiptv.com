"""Creates 400w/800w webp variants of the larger images and adds srcset/sizes to <img> tags, so phones download small files. Re-runnable."""
import os, re, glob, sys
from urllib.parse import unquote, quote
from PIL import Image
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SIZES = '(max-width: 600px) 100vw, 1000px'
made = 0
info = {}
def variants(p):
    """returns (srcset string builder data) or None"""
    global made
    if p in info: return info[p]
    res = None
    try:
        if p.lower().endswith('.webp') and os.path.getsize(p) > 25 * 1024 and '-w400' not in p and '-w800' not in p:
            im = Image.open(p); im.load()
            W = im.width
            if W > 700:
                out = []
                for w in (400, 800):
                    if w >= W: continue
                    vp = p[:-5] + '-w%d.webp' % w
                    if not os.path.exists(vp):
                        h = round(im.height * w / W)
                        v = im.convert('RGBA' if im.mode in ('RGBA', 'P', 'LA') else 'RGB').resize((w, h), Image.LANCZOS)
                        v.save(vp, 'WEBP', quality=74, method=6); made += 1
                    out.append((vp, w))
                res = (out, W)
    except Exception as e:
        print('skip', p, e)
    info[p] = res
    return res

changed = 0
for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf8', errors='surrogateescape').read()
    def fix(m):
        t = m.group(0)
        if ' srcset=' in t: return t
        u = re.search(r'\ssrc="([^"]+)"', t)
        if not u: return t
        raw = u.group(1)
        if raw.startswith(('http', 'data:')): return t
        path = unquote(raw.split('?')[0])
        base = os.path.dirname(f)
        p = path.lstrip('/') if path.startswith('/') else os.path.normpath(os.path.join(base, path)).replace(os.sep, '/')
        v = variants(p)
        if not v: return t
        vs, W = v
        prefix = raw.rsplit('/', 1)[0] + '/' if '/' in raw else ''
        parts = []
        for vp, w in vs:
            parts.append('%s%s %dw' % (prefix, quote(os.path.basename(vp)), w))
        parts.append('%s%s %dw' % (prefix, quote(unquote(raw.rsplit('/', 1)[-1])), W))
        add = ' srcset="%s" sizes="%s"' % (', '.join(parts), SIZES)
        return re.sub(r'\s*/?>$', lambda e: add + (' />' if e.group(0).strip().startswith('/') else '>'), t)
    t = re.sub(r'<img\b[^>]*>', fix, s)
    if t != s:
        open(f, 'w', encoding='utf8', errors='surrogateescape').write(t); changed += 1
print('variants made', made, '| pages changed', changed)

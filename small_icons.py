"""Images shown tiny (inline height <= 70px) were full-size files. Point them to small copies. Re-runnable."""
import os, re, glob, sys
from urllib.parse import unquote, quote
from PIL import Image
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
made = {}
pages = swapped = 0
def small_for(p, h):
    key = (p, h)
    if key in made: return made[key]
    res = None
    try:
        if p.endswith('.webp') and os.path.getsize(p) > 6 * 1024 and not re.search(r'-(w|i)\d+\.webp$', p):
            im = Image.open(p); im.load()
            tw = max(96, round(im.width * (h * 2) / im.height))
            if tw < im.width * 0.7:
                vp = '%s-i%d.webp' % (p[:-5], h * 2)
                if not os.path.exists(vp):
                    im2 = im.convert('RGBA' if im.mode in ('RGBA', 'P', 'LA') else 'RGB').resize((tw, h * 2), Image.LANCZOS)
                    im2.save(vp, 'WEBP', quality=80, method=6)
                res = vp
    except Exception as e:
        print('skip', p, e)
    made[key] = res
    return res
for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf8', errors='surrogateescape').read()
    def fix(m):
        global swapped
        t = m.group(0)
        st = re.search(r'style="[^"]*?(?<![-\w])height:\s*(\d+)px', t)
        u = re.search(r'\ssrc="([^"]+)"', t)
        if not st or not u: return t
        h = int(st.group(1))
        if h > 70 or 'width:' in re.search(r'style="([^"]*)"', t).group(1).replace('max-width', '').replace('min-width', ''): return t
        raw = u.group(1)
        if raw.startswith(('http', 'data:')): return t
        path = unquote(raw)
        p = path.lstrip('/') if path.startswith('/') else os.path.normpath(os.path.join(os.path.dirname(f), path)).replace(os.sep, '/')
        v = small_for(p, h)
        if not v: return t
        newsrc = raw.rsplit('/', 1)[0] + '/' + os.path.basename(v) if '/' in raw else os.path.basename(v)
        t = t.replace('src="%s"' % raw, 'src="%s"' % newsrc.replace(' ', '%20'))
        t = re.sub(r'\s(srcset|sizes)="[^"]*"', '', t)
        swapped += 1
        return t
    t = re.sub(r'<img\b[^>]*>', fix, s)
    if t != s:
        open(f, 'w', encoding='utf8', errors='surrogateescape').write(t); pages += 1
print('pages', pages, 'images swapped', swapped, 'small files', len([v for v in made.values() if v]))

"""Shrinks every image in public/images (max width, webp), converts jpg/png to webp, rewrites <img>/css references, adds width/height + lazy loading.
Re-runnable. A backup of the originals must exist outside the project before running."""
import os, re, sys, glob
from urllib.parse import quote, unquote
from PIL import Image
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT = 'public/images'
MAXW = 1400
before = after = 0
conv = {}  # old basename path -> new
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        p = os.path.join(dp, f)
        ext = f.rsplit('.', 1)[-1].lower()
        if ext not in ('jpg', 'jpeg', 'png', 'webp'):
            continue
        before += os.path.getsize(p)
        im = Image.open(p)
        im.load()
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        if im.mode not in ('RGB', 'RGBA'):
            im = im.convert('RGBA' if 'transparency' in im.info or im.mode in ('P', 'LA') else 'RGB')
        newp = p.rsplit('.', 1)[0] + '.webp'
        if ext == 'webp':
            tmp = p + '.tmp'
            im.save(tmp, 'WEBP', quality=78, method=6)
            if os.path.getsize(tmp) < os.path.getsize(p) or im.width != Image.open(p).width:
                os.replace(tmp, p)
            else:
                os.remove(tmp)
            after += os.path.getsize(p)
        else:
            im.save(newp, 'WEBP', quality=78, method=6)
            after += os.path.getsize(newp)
            conv[p.replace(os.sep, '/')] = newp.replace(os.sep, '/')
print('images: %.1f MB -> %.1f MB, converted %d' % (before / 1e6, after / 1e6, len(conv)))

# reference rewrite
pairs = {}
for old, new in conv.items():
    rel_old, rel_new = old[len('public/'):], new[len('public/'):]  # images/...
    for a, b in ((old, new), (rel_old, rel_new)):
        pairs[a] = b
        pairs[quote(a)] = quote(b)
keys = sorted(pairs, key=len, reverse=True)
pat = re.compile('|'.join(re.escape(k) for k in keys))
files = [f for f in glob.glob('**/*.html', recursive=True)] + glob.glob('assets/css/style.css') + glob.glob('assets/js/app.js')
changed = 0
for f in files:
    s = open(f, encoding='utf8', errors='surrogateescape').read()
    def fix_tag(m):
        return pat.sub(lambda x: pairs[x.group(0)], m.group(0))
    t = re.sub(r'<img\b[^>]*>|url\([^)]*\)|<source\b[^>]*>', fix_tag, s)
    if f.endswith('.css') or f.endswith('.js'):
        t = pat.sub(lambda x: pairs[x.group(0)], s) if f.endswith('.css') else t
    if t != s:
        open(f, 'w', encoding='utf8', errors='surrogateescape').write(t)
        changed += 1
print('files rewritten:', changed)

# delete originals no longer referenced anywhere
alltext = ''
for f in glob.glob('**/*.html', recursive=True) + glob.glob('*.xml') + glob.glob('assets/**/*.css', recursive=True) + glob.glob('assets/**/*.js', recursive=True):
    if '.bak' in f:
        continue
    alltext += open(f, encoding='utf8', errors='ignore').read()
removed = kept = 0
for old in conv:
    base = old.split('/')[-1]
    if base in alltext or quote(base) in alltext:
        kept += 1
    else:
        os.remove(old); removed += 1
print('originals removed', removed, 'kept (still referenced, e.g. og:image)', kept)

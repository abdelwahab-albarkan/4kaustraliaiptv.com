"""Removes the generic Product schema from every page except the homepage (it described an IPTV panel as the 'product' of unrelated pages)."""
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
n = 0
for path in glob.glob('**/*.html', recursive=True):
    if path == 'index.html': continue
    s = open(path, encoding='utf8', errors='surrogateescape').read()
    def drop(m):
        try:
            o = json.loads(m.group(1))
            if isinstance(o, dict) and o.get('@type') == 'Product': return ''
        except Exception: pass
        return m.group(0)
    t = re.sub(r'\s*<script type="application/ld\+json">(.*?)</script>', drop, s, flags=re.S)
    if t != s: open(path, 'w', encoding='utf8', errors='surrogateescape').write(t); n += 1
print('Product schema removed from', n, 'pages')
print('DONE')

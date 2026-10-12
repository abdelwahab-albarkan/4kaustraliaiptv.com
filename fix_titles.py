"""Repairs titles that an earlier pass cut off with '...' by trimming to a natural phrase boundary."""
import glob, html, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
DANGLING = re.compile(r'(?:\s+(?:&|and|for|in|to|of|the|via|a|vs|with|on|by|-|–|\|)|[,:;(\-–])+\s*$', re.I)

def clean(t):
    raw = html.unescape(t).rstrip()
    if not raw.endswith('...'): return None
    raw = raw[:-3].rstrip()
    if raw.count('(') > raw.count(')'):
        raw = raw[:raw.rfind('(')].rstrip()
    raw = DANGLING.sub('', raw).rstrip()
    if raw.endswith('IPTV Setup'): raw += ' Guide'
    return raw

n = 0
for path in glob.glob('**/*.html', recursive=True):
    s = open(path, encoding='utf8', errors='surrogateescape').read()
    m = re.search(r'<title>(.*?)</title>', s, re.S)
    if not m: continue
    new = clean(m.group(1).strip())
    if not new: continue
    esc = new.replace('&', '&amp;')
    old = m.group(1).strip()
    s = s.replace('<title>' + m.group(1) + '</title>', '<title>%s</title>' % esc, 1)
    s = s.replace('content="%s"' % old, 'content="%s"' % esc)
    open(path, 'w', encoding='utf8', errors='surrogateescape').write(s); n += 1
print('titles repaired:', n)
print('DONE')

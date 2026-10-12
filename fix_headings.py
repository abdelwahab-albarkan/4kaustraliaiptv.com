"""Keeps the heading outline in order: an h4 that directly follows an h2 becomes an h3 (same visual size)."""
import glob, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
TAG = re.compile(r'<(/?)h([1-6])(\s[^>]*)?>')
n = 0; pages = 0
for path in glob.glob('**/*.html', recursive=True):
    s = open(path, encoding='utf8', errors='surrogateescape').read()
    cut = s.find('<footer'); head, tail = (s[:cut], s[cut:]) if cut > 0 else (s, '')
    out = []; pos = 0; prev = 0; changed = 0; open_conv = False
    for m in TAG.finditer(head):
        closing, lvl, attrs = m.group(1), int(m.group(2)), m.group(3) or ''
        out.append(head[pos:m.start()]); pos = m.end()
        if not closing:
            if lvl == 4 and prev == 2:
                attrs2 = attrs
                if 'class="' in attrs2: attrs2 = attrs2.replace('class="', 'class="h4-style ', 1)
                else: attrs2 = ' class="h4-style"' + attrs2
                out.append('<h3%s>' % attrs2); open_conv = True; changed += 1; prev = 3
            else:
                out.append(m.group(0)); open_conv = False; prev = lvl
        else:
            if lvl == 4 and open_conv: out.append('</h3>'); open_conv = False
            else: out.append(m.group(0))
    out.append(head[pos:])
    if changed:
        open(path, 'w', encoding='utf8', errors='surrogateescape').write(''.join(out) + tail); n += changed; pages += 1
print('h4->h3 conversions:', n, 'on', pages, 'pages')
print('DONE')

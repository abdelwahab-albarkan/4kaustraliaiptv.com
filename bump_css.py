import glob, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
v = sys.argv[1]
n = 0
for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf8', errors='surrogateescape').read()
    t = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + v, s)
    if t != s:
        open(f, 'w', encoding='utf8', errors='surrogateescape').write(t); n += 1
print('css version', v, 'on', n, 'pages')

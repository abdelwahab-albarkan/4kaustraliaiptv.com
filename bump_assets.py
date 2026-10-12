import glob, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
css, js = sys.argv[1], sys.argv[2]
n = 0
for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf8', errors='surrogateescape').read()
    t = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + css, s)
    t = re.sub(r'(assets/js/app\.js)\?v=\d+', r'\1?v=' + js, t)
    if t != s:
        open(f, 'w', encoding='utf8', errors='surrogateescape').write(t); n += 1
print('assets css', css, 'js', js, 'on', n, 'pages')

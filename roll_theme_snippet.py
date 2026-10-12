"""Adds the theme-restore snippet to every page <head> (prevents a light flash for dark-theme visitors) and bumps asset versions."""
import glob, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SNIP = '<script>try{var t=localStorage.getItem("theme");if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>'
n = 0
for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf8', errors='surrogateescape').read()
    t = re.sub(r'style\.css\?v=\d+', 'style.css?v=42', s)
    t = re.sub(r'(assets/js/app\.js)\?v=\d+', r'\1?v=4', t)
    if 'localStorage.getItem("theme")' not in t:
        t = re.sub(r'(<meta charset="UTF-8"\s*/?>)', lambda m: m.group(1) + '\n' + SNIP, t, 1)
    if t != s:
        open(f, 'w', encoding='utf8', errors='surrogateescape').write(t); n += 1
print('updated', n)

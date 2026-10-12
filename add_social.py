"""Adds the brand's social profiles: footer icons on every page, a card on the contact page, a line on About, and Organization.sameAs."""
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SOCIAL = [
    ('Facebook', 'fa-facebook-f', 'https://www.facebook.com/profile.php?id=61591545360371'),
    ('Instagram', 'fa-instagram', 'https://www.instagram.com/streamb4tv/'),
    ('X', 'fa-x-twitter', 'https://x.com/streamb4t'),
    ('Discord', 'fa-discord', 'https://discord.gg/BFr5HSZfk'),
]
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)
icons = ''.join('<a href="%s" target="_blank" rel="noopener noreferrer me" aria-label="%s" title="%s"><i class="fa-brands %s"></i></a>' % (u, n, n, ic) for n, ic, u in SOCIAL)
ROW = '<div class="footer-social" aria-label="Social profiles">%s</div>' % icons

n = 0
for path in glob.glob('**/*.html', recursive=True):
    s = rd(path); o = s
    if 'footer-social' not in s and '<div class="footer-legal">' in s:
        s = s.replace('<div class="footer-legal">', ROW + '<div class="footer-legal">', 1)
    if path == 'contact.html' and 'Follow us' not in s:
        card = ('<div class="glass-card" style="padding:1.25rem; display:flex; align-items:center; gap:1rem; flex-wrap:wrap;">'
                '<div style="width:50px; height:50px; border-radius:50%%; background:#0f172a; display:flex; align-items:center; justify-content:center; font-size:1.3rem; color:#fff;"><i class="fa-solid fa-share-nodes"></i></div>'
                '<div style="flex:1; min-width:180px;"><h4 style="font-size:1.05rem; margin-bottom:0.4rem;">Follow us</h4>'
                '<div class="social-chips">%s</div></div></div>') % ''.join(
                    '<a href="%s" target="_blank" rel="noopener noreferrer me"><i class="fa-brands %s"></i> %s</a>' % (u, ic, nm) for nm, ic, u in SOCIAL)
        k = s.find('<div class="glass-card" style="padding:1.25rem; display:flex; align-items:center; gap:1rem;">\n              <div style="width:50px; height:50px; border-radius:50%; background:rgba(0,229,255,0.15)')
        if k < 0: k = s.find('AEST Working Hours')
        if k > 0:
            k = s.rfind('<div class="glass-card"', 0, k) if s[k:k + 22] != '<div class="glass-card' else k
            s = s[:k] + card + '\n\n            ' + s[k:]
    if path == 'about/index.html' and 'Follow us' not in s:
        p = '<h2>Follow us</h2><p>We post setup tips and updates on our social profiles: ' + ', '.join('<a href="%s" target="_blank" rel="noopener noreferrer me">%s</a>' % (u, nm) for nm, ic, u in SOCIAL) + '.</p>'
        k = s.find('<h2>Contact us</h2>')
        if k > 0: s = s[:k] + p + s[k:]
    if path == 'index.html' and '"sameAs"' not in s:
        s = s.replace('"logo": "https://4kaustraliaiptv.com/assets/og-au.png",', '"logo": "https://4kaustraliaiptv.com/assets/og-au.png",\n      "sameAs": %s,' % json.dumps([u for _, _, u in SOCIAL]), 1)
    if s != o: wr(path, s); n += 1
print('pages updated:', n)
print('DONE')

"""Replaces invented testimonials with a real support section, links legal pages from every footer."""
import glob, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)

# ---- 1. homepage: testimonials -> support
s = rd('index.html')
m = re.search(r'<section class="testimonials-section"[^>]*>', s)
if m and 'id="support"' not in s[m.start():m.start() + 400]:
    e = s.find('</section>', m.end()) + len('</section>')
    new = '''<section class="testimonials-section" id="support">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-headset"></i> Support</span>
        <h2 class="section-title">Real People Behind Every Message</h2>
        <p class="section-subtitle">Questions before or after you buy? Message us directly. We reply in the order we receive messages.</p>
      </div>
      <div class="criteria-grid">
        <a class="criteria" href="https://wa.me/212625218443?text=Hi%2C%20I%20have%20a%20question%20about%20IPTV" target="_blank" rel="noopener" data-cta="whatsapp" style="color:inherit; text-decoration:none;">
          <i class="fa-brands fa-whatsapp"></i><h4>WhatsApp</h4><p>The fastest way to get help with trials, plans and setup. +212 625 218 443</p>
        </a>
        <a class="criteria" href="mailto:support@4kaustraliaiptv.com" style="color:inherit; text-decoration:none;">
          <i class="fa-solid fa-envelope"></i><h4>Email</h4><p>Prefer email? Send details and screenshots to support@4kaustraliaiptv.com</p>
        </a>
        <a class="criteria" href="#setup" style="color:inherit; text-decoration:none;">
          <i class="fa-solid fa-book-open"></i><h4>Setup guides</h4><p>Step-by-step help for Fire TV Stick, Android TV, Apple TV, Samsung, LG, phones and PCs.</p>
        </a>
      </div>
      <div style="display:flex; flex-wrap:wrap; gap:.75rem; justify-content:center; margin-top:2rem;">
        <button class="btn btn-gold btn-lg" data-open-modal="trial" data-cta="trial"><i class="fa-solid fa-play"></i> Start Free 24H Trial</button>
        <a class="btn btn-secondary btn-lg" href="about/index.html"><i class="fa-solid fa-circle-info"></i> About us</a>
      </div>
      <p style="text-align:center; font-size:.88rem; color:var(--text-dim); margin-top:1.25rem;">We only publish reviews from customers who have used the service. Have feedback? Send it on WhatsApp.</p>
    </div>
  </section>'''
    s = s[:m.start()] + new + s[e:]
s = re.sub(r'<div class="trust-item"><i class="fa-solid fa-users"></i> <span>12,000\+ Active AU Resellers</span></div>',
           '<div class="trust-item"><i class="fa-solid fa-gift"></i> <span>Free 24H Trial, No Card</span></div>', s)
wr('index.html', s)
print('homepage updated; testimonials left:', len(re.findall(r'testimonial-card', s)))

# ---- 2. legal links in every footer
LEGAL = [('about', 'About'), ('privacy-policy', 'Privacy Policy'), ('terms-of-service', 'Terms of Service'), ('refund-policy', 'Refund Policy')]
n = 0
for path in glob.glob('**/*.html', recursive=True):
    t = rd(path)
    if 'footer-legal' in t or '<footer' not in t: continue
    prefix = '../' * (path.replace(os.sep, '/').count('/'))
    links = ''.join('<a href="%s%s/index.html">%s</a>' % (prefix, slug, name) for slug, name in LEGAL)
    block = '<div class="footer-legal">%s</div>' % links
    fi = t.find('<footer'); fe = t.find('</footer>', fi)
    foot = t[fi:fe]
    c = foot.find('&copy;')
    if c < 0: continue
    close = re.search(r'</(div|p)>', foot[c:])
    pos = fi + c + close.end()
    t = t[:pos] + block + t[pos:]
    wr(path, t); n += 1
print('footers with legal links:', n)
print('DONE')

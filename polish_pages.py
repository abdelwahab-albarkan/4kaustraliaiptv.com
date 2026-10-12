"""Site-wide polish: shorter nav labels, logo-based payment row, no emoji, lighter font request, theme colour."""
import glob, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

LABELS = [
    ('Aussie Providers', 'Providers'),
    ('AU Providers', 'Providers'),
    ('Reseller Panel <i class="fa-solid fa-chevron-down"', 'Reseller <i class="fa-solid fa-chevron-down"'),
    ('Reseller Guide</a>', 'Reseller</a>'),
    ('Sports &amp; Channels</a>', 'Channels</a>'),
    ('Sports & Channels</a>', 'Channels</a>'),
    ('Aussie Sports</a>', 'Sports</a>'),
    ('Pricing (AUD)</a>', 'Pricing</a>'),
    ('Setup Guides</a>', 'Setup</a>'),
    ('2,000+ Directory</a>', 'Directory</a>'),
]
NAV_ONLY = re.compile(r'(<a [^>]*class="nav-link[^"]*"[^>]*>.*?</a>)', re.S)

PAY_OLD = re.compile(
    r'<div style="display:flex; flex-wrap:wrap; gap:0\.4rem; margin-bottom:1rem;">\s*'
    r'<span class="badge badge-glow-gold">PayID</span>.*?<span class="badge badge-glow-gold">Crypto</span>\s*</div>', re.S)

def pay_block(prefix):
    img = lambda n, alt: '<img src="%spublic/images/%s" alt="%s" loading="lazy" height="28">' % (prefix, n, alt)
    return ('<div class="pay-logos" style="margin-bottom:1rem;">'
            '<span class="pay-chip">PayID</span>'
            + img('visa-logo.webp', 'Visa') + img('mastercard-logo.webp', 'Mastercard')
            + img('apple-pay-logo.webp', 'Apple Pay') + img('paypal-logo.webp', 'PayPal')
            + img('google-pay-logo.webp', 'Google Pay') + img('crypto-logo.webp', 'Crypto') + '</div>')

stats = dict(pages=0, nav=0, pay=0, emoji=0)
for path in glob.glob('**/*.html', recursive=True):
    rel = path.replace(os.sep, '/')
    prefix = '../' * rel.count('/')
    s = open(path, encoding='utf8', errors='surrogateescape').read(); o = s
    # nav labels, only inside nav-link anchors
    def fix_nav(m):
        t = m.group(1)
        for a, b in LABELS: t = t.replace(a, b)
        return t
    s = NAV_ONLY.sub(fix_nav, s)
    # payment logos
    s, n = PAY_OLD.subn(lambda m: pay_block(prefix), s); stats['pay'] += n
    # emoji -> consistent icons
    s = s.replace('🔥 ', '<i class="fa-solid fa-fire" style="color:#f59e0b;"></i> ').replace('🔥', '<i class="fa-solid fa-fire" style="color:#f59e0b;"></i>')
    s = re.sub('\U0001F1E6\U0001F1FA\\s?', '<i class="fa-solid fa-earth-oceania" style="color:var(--primary);"></i> ', s)
    # theme colour + fonts
    s = s.replace('<meta name="theme-color" content="#0a0614" />', '<meta name="theme-color" content="#0f172a" />')
    s = s.replace('&family=Outfit:wght@400;500;600;700;800;900', '').replace('family=Inter:wght@300;400;500;600;700;800', 'family=Inter:wght@400;500;600;700;800')
    if s != o:
        open(path, 'w', encoding='utf8', errors='surrogateescape').write(s); stats['pages'] += 1
print(stats)

"""Homepage conversion + SEO pass: sports mosaic, device gallery, CTA bands, 'Best IPTV Australia' section,
extra FAQ, WhatsApp order buttons on pricing cards, keyword-focused hero. Idempotent."""
import re, urllib.parse, sys
sys.stdout.reconfigure(encoding='utf8')
p = 'index.html'
s = open(p, encoding='utf8', errors='surrogateescape').read()
if 'id="best-iptv-australia"' in s:
    raise SystemExit('already applied')

WA = 'https://wa.me/212625218443?text='
def wa(msg): return WA + urllib.parse.quote(msg)
IMG = 'public/images/'

# ---------------------------------------------------------------- CTA band
def cta(title, text, wa_msg, img=None, cls=''):
    media = ('<div class="cta-media"><img src="%s%s" alt="" loading="lazy" decoding="async" width="900" height="600"></div>' % (IMG, img)) if img else ''
    return '''
  <section class="cta-band %s" aria-label="Get started">
    <div class="container">
      <div class="cta-inner">
        <div class="cta-copy">
          <h2>%s</h2>
          <p>%s</p>
          <div class="cta-actions">
            <button class="btn btn-gold btn-lg" data-open-modal="trial" data-cta="trial"><i class="fa-solid fa-play"></i> Start Free 24H Trial</button>
            <a class="btn btn-whatsapp btn-lg" data-cta="whatsapp" href="%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp</a>
          </div>
          <p class="cta-note"><i class="fa-solid fa-circle-check"></i> No credit card for the trial &nbsp;&middot;&nbsp; <i class="fa-solid fa-circle-check"></i> Replies on WhatsApp and support@4kaustraliaiptv.com</p>
        </div>
        %s
      </div>
    </div>
  </section>
''' % (cls, title, text, wa(wa_msg), media)

CTA1 = cta('Try IPTV Australia free for 24 hours',
           'Test live sport, channel quality and your NBN connection on your own TV before you pay anything.',
           'Hi, I would like a free 24-hour IPTV trial in Australia', 'home/streaming-device-remote.webp')
CTA2 = cta('Ready to watch? Pick a plan or ask us first',
           'Not sure which IPTV subscription fits your TV and internet? Message us your device and we will point you to the right plan.',
           'Hi, I need help choosing an IPTV subscription plan', 'support-team.webp', 'cta-dark')
CTA3 = cta('Setup stuck? We will walk you through it',
           'Send us a screenshot of your device or app and we will help you get your IPTV player working.',
           'Hi, I need help setting up IPTV on my device', 'iptv/devices/iptv-apple-tv.webp')
CTA4 = cta('Join Australians watching AFL, NRL and cricket in 4K',
           'Start with the free trial, then choose a 3, 6 or 12-month IPTV subscription in AUD.',
           'Hi, I want to start an IPTV subscription in Australia', 'home/family-watching-tv.webp', 'cta-dark')

# ---------------------------------------------------------------- sports mosaic
SPORTS = [
    ('packimages2/5403.webp', 'NRL &amp; State of Origin', 'sports/nrl-live-stream-iptv'),
    ('playing-rules-scaled-1.webp', 'AFL Premiership', 'sports/afl-live-stream-iptv'),
    ('cricket-ashes.webp', 'Cricket &amp; The Ashes', 'sports/cricket-australia-the-ashes-iptv'),
    ('formula-1-aus.webp', 'Formula 1 &amp; Supercars', 'sports/formula-1-australian-gp-iptv'),
    ('ufc-boxing-main-event.webp', 'UFC &amp; Boxing PPV', 'sports/ufc-ppv-main-event-australia-iptv'),
    ('premier-league-soccer.webp', 'Premier League', 'sports/premier-league-optus-sport-alternative'),
    ('nbl-basketball.webp', 'NBA &amp; Basketball', 'sports/nba-basketball-australia-iptv'),
    ('fussball-streaming.webp', 'A-League &amp; Soccer', 'sports/a-league-soccer-iptv-australia'),
]
tiles = ''.join('''
        <a class="mosaic-tile" href="%s/index.html">
          <img src="%s%s" alt="%s live on IPTV in Australia" loading="lazy" decoding="async" width="800" height="600">
          <span class="mosaic-label"><strong>%s</strong><em>Watch live <i class="fa-solid fa-arrow-right"></i></em></span>
        </a>''' % (href, IMG, img, label, label) for img, label, href in SPORTS)
MOSAIC = '''
  <section class="section-padding-lg" style="background:var(--bg-main);" id="live-sport-gallery">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-tower-broadcast"></i> Live Sport</span>
        <h2 class="section-title">Every Aussie Sport on One IPTV Subscription</h2>
        <p class="section-subtitle">From the AFL and NRL to cricket, F1, UFC and the Premier League. Choose a sport to see channels, schedules and how to watch.</p>
      </div>
      <div class="mosaic-grid">%s
      </div>
      <div style="text-align:center; margin-top:2rem;"><a class="btn btn-primary btn-lg" href="channels.html"><i class="fa-solid fa-futbol"></i> See all sports channels</a></div>
    </div>
  </section>
''' % tiles

# ---------------------------------------------------------------- device gallery
DEV = [
    ('iptv/devices/iptv-fire-stick.webp', 'Amazon Fire TV Stick', 'devices/iptv-on-amazon-firestick-australia'),
    ('iptv/devices/iptv-apple-tv.webp', 'Apple TV 4K', 'devices/iptv-on-apple-tv-tvos-australia'),
    ('iptv/devices/iptv-samsung-tv-einrichtung.webp', 'Samsung Smart TV', 'devices/iptv-on-samsung-smart-tv-tizen-australia'),
    ('iptv/devices/iptv-lg-tv-einrichtung.webp', 'LG webOS TV', 'devices/iptv-on-lg-smart-tv-webos-australia'),
    ('iptv/devices/iptv-android-tv.webp', 'Android TV &amp; Google TV', 'devices/iptv-on-android-tv-box-australia'),
    ('iptv/devices/iptv-android-handy.webp', 'Android phone', 'devices/tivimate-iptv-player-australia-setup'),
    ('iptv/devices/iptv-iphone-ipad.webp', 'iPhone &amp; iPad', 'devices/iptv-smarters-pro-australia-guide'),
    ('iptv/devices/iptv-windows-mac.webp', 'Windows &amp; Mac', 'devices/windows-mac-pc-iptv-player-australia'),
]
dtiles = ''.join('''
        <a class="mosaic-tile mosaic-tile--device" href="%s/index.html">
          <img src="%s%s" alt="IPTV on %s" loading="lazy" decoding="async" width="800" height="600">
          <span class="mosaic-label"><strong>%s</strong><em>Setup guide <i class="fa-solid fa-arrow-right"></i></em></span>
        </a>''' % (href, IMG, img, label, label) for img, label, href in DEV)
DEVICES = '''
  <section class="section-padding-lg" style="background:var(--bg-secondary);" id="every-screen">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-tv"></i> Works on Every Screen</span>
        <h2 class="section-title">IPTV on Your TV, Phone, Tablet and PC</h2>
        <p class="section-subtitle">One IPTV subscription, every device in the house. Pick your device for a step-by-step setup guide.</p>
      </div>
      <div class="mosaic-grid">%s
      </div>
    </div>
  </section>
''' % dtiles

# ---------------------------------------------------------------- SEO section
def faq_link(href, text): return '<a href="%s">%s</a>' % (href, text)
BEST = '''
  <section class="section-padding-lg" style="background:var(--bg-secondary);" id="best-iptv-australia">
    <div class="container">
      <div class="media-split">
        <div>
          <span class="badge badge-glow-green" style="margin-bottom:0.75rem;"><i class="fa-solid fa-award"></i> Buyer&rsquo;s Guide 2026</span>
          <h2 class="section-title" style="margin-top:0;">Best IPTV Australia 2026: How to Choose a Top-Rated IPTV Subscription</h2>
          <p style="line-height:1.8; margin-bottom:1rem;">
            If you are searching for the <strong>best IPTV Australia</strong> has to offer, start with what matters at home: a stable picture on your NBN plan, the Australian sport you actually watch, and an IPTV player that works on your TV. A good <strong>IPTV subscription</strong> in Australia should let you test it first, show clear AUD pricing and give you a real person to talk to when something goes wrong.
          </p>
          <p style="line-height:1.8; margin-bottom:1.5rem;">
            Use this page as a shortcut: compare <a href="providers.html">IPTV providers Australia</a>, read the <a href="#iptv-box-australia">IPTV box guide</a>, pick an <a href="#iptv-player-apps">IPTV player</a>, then start a <a href="#free-trial">free IPTV trial</a> to see how it performs on your own connection.
          </p>
          <div style="display:flex; flex-wrap:wrap; gap:0.75rem;">
            <button class="btn btn-gold btn-lg" data-open-modal="trial" data-cta="trial"><i class="fa-solid fa-play"></i> Get a Free IPTV Trial</button>
            <a class="btn btn-whatsapp btn-lg" data-cta="whatsapp" href="%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Ask on WhatsApp</a>
          </div>
        </div>
        <figure class="media-figure"><img src="public/images/home/living-room-hero.webp" alt="Smart TV in an Australian living room streaming IPTV" width="1200" height="800" loading="lazy" decoding="async"></figure>
      </div>

      <h3 style="margin-bottom:1.25rem;">What makes an IPTV service &ldquo;top rated&rdquo;?</h3>
      <div class="criteria-grid">
        <div class="criteria"><i class="fa-solid fa-signal"></i><h4>Stable on Australian NBN</h4><p>Servers close to Sydney and Melbourne, and a stream that holds up on Telstra, Optus, TPG and Aussie Broadband at peak time.</p></div>
        <div class="criteria"><i class="fa-solid fa-futbol"></i><h4>The sport you watch</h4><p>AFL, NRL, cricket, F1, UFC and soccer, with a programme guide that shows the right Australian time zone.</p></div>
        <div class="criteria"><i class="fa-solid fa-tv"></i><h4>Works with your device</h4><p>Fire TV Stick, Android TV box, Apple TV, Samsung, LG, phone and PC, with an easy IPTV player.</p></div>
        <div class="criteria"><i class="fa-solid fa-gift"></i><h4>A real free trial</h4><p>Try before you pay. A short IPTV free trial is the fairest way to compare services.</p></div>
        <div class="criteria"><i class="fa-solid fa-dollar-sign"></i><h4>Clear AUD pricing</h4><p>Simple 3, 6 and 12-month plans in Australian dollars, with no hidden extras.</p></div>
        <div class="criteria"><i class="fa-solid fa-headset"></i><h4>Support that replies</h4><p>Help by WhatsApp and email when you need it, not just a ticket form.</p></div>
      </div>

      <div class="glass-card" style="margin-top:2rem; display:flex; gap:1rem; align-items:flex-start;">
        <i class="fa-solid fa-scale-balanced" style="color:var(--primary); font-size:1.3rem; margin-top:.2rem;"></i>
        <p style="font-size:0.95rem; line-height:1.75; margin:0;"><strong>Choose legal, licensed content.</strong> Before you subscribe to any IPTV service, check that it has the rights to the channels it sells. Read our <a href="guides/is-iptv-legal-in-australia-2026-guide/index.html">guide to IPTV legality in Australia</a>, and compare options on the <a href="providers.html">IPTV providers page</a>.</p>
      </div>

      <div class="chip-row">
        <span>Popular searches:</span>
        <a href="cities/sydney/index.html">IPTV Sydney</a>
        <a href="cities/melbourne/index.html">IPTV Melbourne</a>
        <a href="cities/brisbane/index.html">IPTV Brisbane</a>
        <a href="cities/perth/index.html">IPTV Perth</a>
        <a href="cities/adelaide/index.html">IPTV Adelaide</a>
        <a href="comparisons/foxtel-alternative-iptv-australia/index.html">Foxtel alternative</a>
        <a href="comparisons/kayo-sports-alternative-iptv-australia/index.html">Kayo alternative</a>
        <a href="devices/iptv-on-amazon-firestick-australia/index.html">IPTV on Firestick</a>
      </div>
    </div>
  </section>
''' % wa('Hi, I am looking for the best IPTV in Australia. Can you help me choose?')

# ---------------------------------------------------------------- extra FAQ
NEW_FAQ = [
    ('What is the best IPTV in Australia?', 'The best IPTV in Australia is the one that stays stable on your own NBN connection, carries the Australian sport you watch, works with your TV or IPTV box, and lets you test it first. Start with a free IPTV trial, check live sport at peak time, then compare plans in AUD.'),
    ('How do I get an IPTV free trial in Australia?', 'Tap Start Free 24H Trial, tell us your device and email, or message us on WhatsApp. You will get trial login details to add to an IPTV player such as TiviMate, IPTV Smarters Pro or IBO Player. No credit card is needed for the trial.'),
    ('Which IPTV box or player should I use?', 'For a Fire TV Stick or Android TV box, TiviMate is a popular IPTV player. On Samsung and LG TVs, IBO Player is common. On iPhone, iPad and PC, IPTV Smarters Pro is easy to set up. See our IPTV box and player guides on this page.'),
    ('How much does an IPTV subscription cost in Australia?', 'Plans on this page are priced in Australian dollars for 3, 6 and 12 months. Check the pricing section for current prices, or message us on WhatsApp for help choosing.'),
]
faq_html = ''
for i, (q, a) in enumerate(NEW_FAQ):
    faq_html += '''
        <div class="faq-item" data-category="payment">
          <div class="faq-question">
            <h3><i class="fa-solid fa-circle-question" style="color:var(--primary);"></i> %s</h3>
            <div class="faq-toggle-icon"><i class="fa-solid fa-plus"></i></div>
          </div>
          <div class="faq-answer"><div class="faq-answer-inner">%s</div></div>
        </div>''' % (q, a)
import json
faq_ld = '<script type="application/ld+json">\n' + json.dumps({
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in NEW_FAQ]},
    indent=2, ensure_ascii=False) + '\n</script>\n'

# ---------------------------------------------------------------- apply
def insert_before(marker_regex, html, count=1):
    global s
    m = re.search(marker_regex, s)
    assert m, marker_regex
    s = s[:m.start()] + html + s[m.start():]
def insert_after_section(sec_id, html):
    global s
    j = s.find('id="%s"' % sec_id); assert j > 0, sec_id
    e = s.find('</section>', j) + len('</section>')
    s = s[:e] + '\n' + html + s[e:]

# trust bar -> CTA 1, then sports mosaic after channels
insert_after_section_trust = re.search(r'<section class="trust-bar-section">', s)
j = s.find('</section>', insert_after_section_trust.start()) + len('</section>')
s = s[:j] + '\n' + CTA1 + s[j:]
insert_after_section('channels', MOSAIC)
insert_after_section('pricing', BEST)
insert_after_section('setup', CTA3)
insert_after_section('iptv-player-apps', DEVICES)
insert_after_section('providers', CTA2)
# CTA 4 before the FAQ section, final CTA before the footer
m = re.search(r'<!--[^>]*FAQ[^>]*-->\s*<section class="faq-section"', s) or re.search(r'<section class="faq-section"', s)
s = s[:m.start()] + CTA4 + '\n' + s[m.start():]
s = s.replace('</footer>', '</footer>', 1)

# extra FAQ items at the end of the accordion + schema
acc = s.find('<div class="faq-accordion">'); assert acc > 0
depth = 0; i = acc
for m in re.finditer(r'<div\b|</div>', s[acc:]):
    depth += 1 if m.group(0) == '<div' else -1
    if depth == 0: i = acc + m.start(); break
s = s[:i] + faq_html + '\n      ' + s[i:]
s = s.replace('</head>', '  ' + faq_ld + '</head>', 1)

# hero: keyword H1, trial-first buttons
s = re.sub(r'<h1 class="hero-title">.*?</h1>',
           '<h1 class="hero-title">\n            Best IPTV Australia: <span class="gradient-text">IPTV Subscription &amp; Reseller Panel</span> with 4K Live Sports\n          </h1>', s, 1, flags=re.S)
hero_ctas = re.search(r'<div class="hero-ctas">.*?</div>', s, re.S)
new_ctas = '''<div class="hero-ctas">
            <button class="btn btn-gold btn-xl" data-open-modal="trial" data-cta="trial">
              <i class="fa-solid fa-play"></i> Start Free 24H Trial
            </button>
            <a href="%s" target="_blank" rel="noopener" class="btn btn-whatsapp btn-xl" data-cta="whatsapp">
              <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp
            </a>
            <button class="btn btn-secondary btn-xl" data-open-modal="reseller">
              <i class="fa-solid fa-rocket"></i> Reseller Panel (AUD)
            </button>
          </div>''' % wa('Hi, I am interested in IPTV Australia')
s = s[:hero_ctas.start()] + new_ctas + s[hero_ctas.end():]

# meta description: lead with the main keywords
s = re.sub(r'<meta name="description" content="[^"]*" />',
           '<meta name="description" content="Best IPTV Australia: premium IPTV subscription in AUD with AFL, NRL, cricket and 4K live sport. Compare IPTV providers, pick an IPTV box or player, and start a free IPTV trial. Reseller panel available. Support by WhatsApp and email." />', s, 1)

# pricing cards: WhatsApp order button under each plan
def add_order(m):
    block = m.group(0)
    name = re.search(r'class="plan-name"[^>]*>(.*?)<', block, re.S)
    nm = re.sub(r'\s+', ' ', name.group(1)).strip() if name else 'a plan'
    link = ('\n            <a class="btn btn-whatsapp btn-sm btn-block" data-cta="whatsapp" style="margin-top:.6rem;" href="%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Order on WhatsApp</a>'
            % wa('Hi, I want the %s IPTV plan' % nm))
    i = block.rfind('</button>')
    return block if i < 0 or 'Order on WhatsApp' in block else block[:i + 9] + link + block[i + 9:]
pj = s.find('id="pricing"'); pe = s.find('</section>', pj)
seg = s[pj:pe]
seg = re.sub(r'<div class="pricing-card[^"]*"[^>]*>.*?(?=<div class="pricing-card|\s*</div>\s*</div>\s*$)', add_order, seg, flags=re.S)
s = s[:pj] + seg + s[pe:]

open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)
print('applied; cta bands:', s.count('class="cta-band'), ' order buttons:', s.count('Order on WhatsApp'))

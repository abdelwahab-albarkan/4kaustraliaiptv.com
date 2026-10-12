"""Replaces the consumer plans with the new 3 / 6 / 12 month offers (1-4 accounts) and updates related copy."""
import glob, os, re, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)

PRICES = {3: [39.99, 59.99, 79.99, 99.99], 6: [56.99, 84.99, 109.99, 134.99], 12: [79.99, 119.99, 149.99, 179.99]}
DESC = {3: 'Season pass', 6: 'Half-year plan', 12: 'Best long-term value'}
FEATS = ['Live TV, sports and on-demand', 'Works on Fire TV, Android, Apple, Samsung, LG and PC', 'Free 24-hour trial before you buy', 'Support on WhatsApp and email']
WA = 'https://wa.me/212625218443?text='

def money(v): return '%.2f' % v
def msg(months, acct, price):
    return WA + urllib.parse.quote('Hi, I want the %d months IPTV plan with %d account%s ($%s)' % (months, acct, '' if acct == 1 else 's', money(price)))

def card(months):
    price = PRICES[months][0]
    base = PRICES[3][0] / 3
    permonth = price / months
    save = round((1 - permonth / base) * 100)
    pop = months == 12
    return '''
        <div class="pricing-card%s" data-months="%d">
          %s
          <div>
            <div class="plan-header">
              <div class="plan-name">%d Months</div>
              <div class="plan-desc">%s</div>
            </div>
            <div class="plan-price-wrap">
              <span class="currency-sym">$</span>
              <span class="price-big" data-price>%s</span>
              <span class="price-period">AUD for %d months</span>
            </div>
            <div class="price-meta"><span data-permonth>$%s / month</span> <span class="save-pill" data-save%s>Save %d%%</span></div>
            <ul class="plan-features-list">
              <li><i class="fa-solid fa-check"></i> <span data-accounts>1 account included</span></li>
              %s
            </ul>
          </div>
          <a class="btn btn-whatsapp btn-block" data-cta="whatsapp" data-order href="%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Order on WhatsApp</a>
          <button class="btn btn-outline btn-block" style="margin-top:.6rem;" data-open-modal="trial" data-cta="trial"><i class="fa-solid fa-play"></i> Try free for 24H first</button>
        </div>''' % (' popular' if pop else '', months, '<div class="pricing-badge-popular">Best Value</div>' if pop else '',
                     months, DESC[months], money(price), months, money(permonth), '' if months != 3 else ' hidden', save,
                     ''.join('<li><i class="fa-solid fa-check"></i> %s</li>' % f for f in FEATS), msg(months, 1, price))

NEW = '''<div id="consumerPricingGrid" class="pricing-consumer" style="display:grid;">
        <div class="account-select" role="radiogroup" aria-label="Number of accounts">
          <span class="account-select-label">How many accounts?</span>
          <div class="account-pills">
            <button type="button" class="acct-btn active" data-acct="1" role="radio" aria-checked="true">1 Account</button>
            <button type="button" class="acct-btn" data-acct="2" role="radio" aria-checked="false">2 Accounts</button>
            <button type="button" class="acct-btn" data-acct="3" role="radio" aria-checked="false">3 Accounts</button>
            <button type="button" class="acct-btn" data-acct="4" role="radio" aria-checked="false">4 Accounts</button>
          </div>
        </div>
        <div class="pricing-cards-grid cols-3">%s
        </div>
        <p class="acct-note"><i class="fa-solid fa-circle-info"></i> Prices in AUD. More accounts cost less per account. Not sure? <a href="#free-trial">Start with the free 24-hour trial</a>.</p>
      </div>''' % ''.join(card(m) for m in (3, 6, 12))

s = rd('index.html')
if 'data-acct="1"' not in s:
    m = re.search(r'<div class="pricing-cards-grid" id="consumerPricingGrid">', s)
    assert m
    depth = 0; end = None
    for t in re.finditer(r'<div\b|</div>', s[m.start():]):
        depth += 1 if t.group(0) == '<div' else -1
        if depth == 0: end = m.start() + t.end(); break
    s = s[:m.start()] + NEW + s[end:]

PHR = [('1, 3, 6 and 12-month', '3, 6 and 12-month'), ('1, 3, 6 and 12 months', '3, 6 and 12 months'), ('1, 3, 6 or 12-month', '3, 6 or 12-month'),
       ('1, 3, 6 or 12 months', '3, 6 or 12 months'), ('Plans in AUD from 1 to 12 months', 'Plans in AUD from 3 to 12 months'),
       ('monthly, quarterly, six-month and yearly plans', '3, 6 and 12-month plans')]
changed = 0
for f in ['index.html', 'best-iptv-australia/index.html', 'iptv-free-trial-australia/index.html', 'iptv-box-australia/index.html',
          'iptv-player-australia/index.html', 'build_landing_pages.py', 'add_conversion_sections.py']:
    t = s if f == 'index.html' else rd(f)
    u = t
    for a, b in PHR: u = u.replace(a, b)
    u = u.replace('Simple monthly, quarterly, six-month and yearly plans in Australian dollars', 'Simple 3, 6 and 12-month plans in Australian dollars, with 1 to 4 accounts')
    if f == 'index.html': s = u
    elif u != t: wr(f, u)
    if u != t: changed += 1
# structured data on the homepage: consumer 39.99-179.99 plus reseller packs up to 1100
s = s.replace('"lowPrice": "15.00",\n      "highPrice": "1100.00",\n      "offerCount": "8"', '"lowPrice": "39.99",\n      "highPrice": "1100.00",\n      "offerCount": "16"')
wr('index.html', s)
print('copy files updated:', changed)

n = 0
for path in glob.glob('**/*.html', recursive=True):
    if path == 'index.html': continue
    t = rd(path)
    u = t.replace('"lowPrice": "15.00"', '"lowPrice": "39.99"').replace('"highPrice": "110.00"', '"highPrice": "179.99"').replace('"offerCount": "4"', '"offerCount": "12"')
    if u != t: wr(path, u); n += 1
print('schema updated on pages:', n)
print('DONE')

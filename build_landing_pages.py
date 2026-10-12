"""Builds 4 keyword landing pages (best IPTV Australia, IPTV box, IPTV player, IPTV free trial) from the site's
existing page shell, then adds them to the sitemap. Safe to re-run: pages are overwritten, sitemap entries are not duplicated."""
import html as H, json, os, re, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://4kaustraliaiptv.com'
WA = 'https://wa.me/212625218443?text='
def wa(m): return WA + urllib.parse.quote(m)
IMG = '../public/images/'

shell = open('devices/iptv-on-amazon-firestick-australia/index.html', encoding='utf8').read()
i_body = shell.find('<body'); i_head_end = shell.find('</header>') + len('</header>'); i_foot = shell.find('<footer')
TOP = shell[i_body:i_head_end].replace('../../', '../')
FOOT = shell[i_foot:].replace('../../', '../')
TOP = TOP.replace('class="nav-link active"', 'class="nav-link"')

def e(t): return H.escape(t, quote=False)

# ------------------------------------------------------------------ reusable blocks
def hero(badge, h1, intro, img, alt, bullets):
    lis = ''.join('<li><i class="fa-solid fa-circle-check"></i> %s</li>' % b for b in bullets)
    return '''
  <section class="hero-section" style="padding:3.5rem 0 3rem;">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="hero-badges-row">
            <span class="badge badge-glow-gold"><i class="fa-solid fa-crown"></i> %s</span>
            <span class="badge badge-glow-green"><i class="fa-solid fa-dollar-sign"></i> AUD pricing</span>
            <span class="badge badge-glow-cyan"><i class="fa-solid fa-signal"></i> Built for Australian NBN</span>
          </div>
          <h1 class="hero-title">%s</h1>
          <p class="hero-description">%s</p>
          <div class="hero-ctas">
            <button class="btn btn-gold btn-xl" data-open-modal="trial" data-cta="trial"><i class="fa-solid fa-play"></i> Start Free 24H Trial</button>
            <a class="btn btn-whatsapp btn-xl" data-cta="whatsapp" href="%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp</a>
          </div>
        </div>
        <div>
          <div class="hero-portal-card">
            <figure class="hero-visual"><img src="%s" alt="%s" width="1200" height="675" loading="eager" decoding="async"></figure>
            <ul class="portal-features-list" style="margin-top:1.25rem;">%s</ul>
          </div>
        </div>
      </div>
    </div>
  </section>''' % (badge, h1, intro, wa('Hi, I found you on ' + h1.split(':')[0] + '. I would like a free IPTV trial'), img, alt, lis)

def section(title, body, bg='var(--bg-main)', sid=''):
    return '''
  <section style="padding:4.5rem 0; background:%s;"%s>
    <div class="container">
      <div class="prose-block">
        <h2 class="section-title" style="margin-top:0;">%s</h2>
        %s
      </div>
    </div>
  </section>''' % (bg, ' id="%s"' % sid if sid else '', title, body)

def cards(items, cols=3):
    return '<div class="criteria-grid" style="grid-template-columns:repeat(%d,1fr);">%s</div>' % (cols, ''.join(
        '<div class="criteria"><i class="fa-solid %s"></i><h4>%s</h4><p>%s</p></div>' % (ic, t, d) for ic, t, d in items))

def table(head, rows):
    th = ''.join('<th>%s</th>' % h for h in head)
    tr = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows)
    return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tr)

def steps(items):
    return '<ol class="steps-list">%s</ol>' % ''.join('<li><span class="step-number">%d</span><div><h4>%s</h4><p>%s</p></div></li>' % (i + 1, t, d) for i, (t, d) in enumerate(items))

def faq(items):
    return '<div class="faq-accordion" style="margin-top:1rem;">%s</div>' % ''.join(
        '<div class="faq-item"><div class="faq-question"><h3>%s</h3><div class="faq-toggle-icon"><i class="fa-solid fa-plus"></i></div></div><div class="faq-answer"><div class="faq-answer-inner">%s</div></div></div>' % (q, a) for q, a in items)

def cta(title, text, msg):
    return '''
  <section class="cta-band cta-dark" aria-label="Get started">
    <div class="container"><div class="cta-inner" style="grid-template-columns:1fr;">
      <div class="cta-copy" style="text-align:center; margin:0 auto;">
        <h2>%s</h2><p style="margin-left:auto;margin-right:auto;">%s</p>
        <div class="cta-actions" style="justify-content:center;">
          <button class="btn btn-gold btn-lg" data-open-modal="trial" data-cta="trial"><i class="fa-solid fa-play"></i> Start Free 24H Trial</button>
          <a class="btn btn-whatsapp btn-lg" data-cta="whatsapp" href="%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp</a>
        </div>
        <p class="cta-note"><i class="fa-solid fa-circle-check"></i> No credit card for the trial &nbsp;&middot;&nbsp; support@4kaustraliaiptv.com</p>
      </div>
    </div></div>
  </section>''' % (title, text, wa(msg))

def related(slug):
    links = [('best-iptv-australia', 'Best IPTV Australia', 'fa-award'), ('iptv-box-australia', 'IPTV Box Australia', 'fa-box'),
             ('iptv-player-australia', 'IPTV Player Apps', 'fa-circle-play'), ('iptv-free-trial-australia', 'IPTV Free Trial', 'fa-gift')]
    chips = ''.join('<a href="../%s/index.html"><i class="fa-solid %s"></i> %s</a>' % (s, ic, t) for s, t, ic in [(a, b, c) for a, b, c in links] if s != slug)
    more = ('<a href="../providers.html">IPTV Providers</a><a href="../channels.html">Sports &amp; Channels</a><a href="../index.html#pricing">Pricing (AUD)</a>'
            '<a href="../cities/sydney/index.html">IPTV Sydney</a><a href="../cities/melbourne/index.html">IPTV Melbourne</a><a href="../cities/brisbane/index.html">IPTV Brisbane</a>'
            '<a href="../guides/is-iptv-legal-in-australia-2026-guide/index.html">Is IPTV legal?</a>')
    return '''
  <section style="padding:3rem 0; background:var(--bg-secondary);">
    <div class="container"><div class="chip-row" style="margin-top:0;"><span>Keep reading:</span>%s%s</div></div>
  </section>''' % (chips, more)

def crumbs(name):
    return '''
  <div style="background:var(--bg-secondary); border-bottom:1px solid var(--border-color); padding:0.6rem 0;">
    <div class="container"><nav aria-label="Breadcrumbs" style="display:flex; align-items:center;">
      <a href="../index.html" style="color:var(--text-muted); font-size:0.85rem;">Home</a> <span style="color:var(--text-dim); margin:0 0.4rem;">/</span> <span style="font-size:0.85rem; font-weight:600;">%s</span>
    </nav></div>
  </div>''' % name

def head(title, desc, slug, name, faq_items, img):
    url = '%s/%s/' % (SITE, slug)
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + '/'},
        {"@type": "ListItem", "position": 2, "name": name, "item": url}]}
    fq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": H.unescape(re.sub('<[^>]+>', '', q)), "acceptedAnswer": {"@type": "Answer", "text": H.unescape(re.sub('<[^>]+>', '', a))}} for q, a in faq_items]}
    wp = {"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc, "url": url, "inLanguage": "en-AU",
          "isPartOf": {"@type": "WebSite", "name": "IPTV Australia", "url": SITE + '/'}}
    ld = ''.join('<script type="application/ld+json">\n%s\n</script>\n' % json.dumps(x, indent=2, ensure_ascii=False) for x in (bc, fq, wp))
    return '''<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
<meta name="theme-color" content="#0f172a" />
<title>%s</title>
<meta name="description" content="%s" />
<link rel="canonical" href="%s" />
<link rel="alternate" hreflang="en-AU" href="%s" />
<link rel="alternate" hreflang="x-default" href="%s" />
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
<meta property="og:title" content="%s" />
<meta property="og:description" content="%s" />
<meta property="og:type" content="article" />
<meta property="og:locale" content="en_AU" />
<meta property="og:url" content="%s" />
<meta property="og:image" content="%s/assets/og-au.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="%s/assets/og-au.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
<link rel="stylesheet" href="../assets/css/style.css?v=23" />
%s</head>
''' % (e(title), e(desc), url, url, url, e(title), e(desc), url, SITE, SITE, ld)

# ------------------------------------------------------------------ page content
PAGES = {}

# ---- 1. best-iptv-australia
faq1 = [
    ('What is the best IPTV in Australia?', 'There is no single best IPTV for everyone. The best IPTV in Australia is the one that stays stable on your own NBN connection, carries the Australian sport you watch, works with your TV or IPTV box, and lets you test it before paying. Start a free IPTV trial and compare on your own internet.'),
    ('How do I choose an IPTV subscription in Australia?', 'Check four things: a free trial, clear AUD pricing, device support for your TV or box, and a support channel that replies. Then watch live sport at peak time during the trial before choosing a 3, 6 or 12-month IPTV subscription.'),
    ('Do I need a special IPTV box?', 'No. A Fire TV Stick, Android TV box, Apple TV, Samsung or LG smart TV, phone or PC can all run an IPTV player. A dedicated box can feel faster and supports a wired connection. See our IPTV box guide for the options.'),
    ('Is IPTV legal in Australia?', 'IPTV technology is legal, but the content must be properly licensed. Before subscribing, check that a service has the rights to the channels it offers. Read our guide to IPTV legality in Australia for the basics.'),
    ('How much does IPTV cost in Australia?', 'Prices are listed in Australian dollars for 3, 6 and 12-month plans on the pricing section of our homepage. Longer plans usually cost less per month.'),
]
b1 = (
    '<p>Searching for the <strong>best IPTV Australia</strong> has to offer usually ends in a long list of services that all promise the same thing. This guide cuts through that. It explains what actually separates a good <strong>IPTV subscription</strong> from a frustrating one, how to test a service on your own NBN connection, and which setup works on your TV.</p>'
    + '<h3>The six things that make an IPTV service top rated</h3>'
    + cards([('fa-signal', 'Stability on NBN', 'A stream that holds up on Telstra, Optus, TPG and Aussie Broadband during Friday and Saturday night sport, not just at 10am.'),
             ('fa-futbol', 'Your sport and channels', 'AFL, NRL, cricket, F1, UFC and soccer, plus the free-to-air channels you watch, with a guide in the Australian time zone.'),
             ('fa-tv', 'Device support', 'An app or setup for your Fire TV Stick, Android TV box, Apple TV, Samsung, LG, phone or PC.'),
             ('fa-gift', 'A real free trial', 'A short trial you can use on your own TV and internet before you pay anything.'),
             ('fa-dollar-sign', 'Clear AUD pricing', 'Simple 3, 6 and 12-month plans in Australian dollars.'),
             ('fa-headset', 'Support that replies', 'Help on WhatsApp and email when you get stuck on setup.')])
    + '<h3 style="margin-top:2rem;">How to test an IPTV service in 24 hours</h3>'
    + steps([('Request the trial', 'Use the free trial button on this page. You only need your device type and an email address.'),
             ('Install an IPTV player', 'Add the login details to TiviMate, IPTV Smarters Pro or IBO Player. See the <a href="../iptv-player-australia/index.html">IPTV player guide</a>.'),
             ('Test at peak time', 'Watch a live AFL or NRL match, flick between channels, and check the programme guide on a Friday or Saturday night.'),
             ('Check your own connection', 'If a stream stutters, try a wired connection or a different DNS before blaming the service. See our <a href="../guides/how-to-fix-iptv-buffering-australia/index.html">buffering guide</a>.')])
    + '<h3 style="margin-top:2rem;">IPTV compared with pay TV and sports apps</h3>'
    + table(['', 'IPTV subscription', 'Pay TV / sports apps'],
            [['Where you watch', 'Any device with an IPTV player', 'Set-top box or the provider app'],
             ['Contract', 'Usually prepaid 1 to 12 months', 'Often a lock-in contract'],
             ['Try before you buy', 'Free trial from many services', 'Rarely'],
             ['Licensing', 'Varies by service, so check it', 'Fully licensed']])
    + '<p style="margin-top:1.25rem;"><strong>Choose licensed content.</strong> Before subscribing to any IPTV service, make sure it has the rights to the channels it sells. Compare options on the <a href="../providers.html">IPTV providers page</a>.</p>'
    + '<h2 class="section-title" style="margin-top:2.5rem;">IPTV questions Australians ask</h2>' + faq(faq1))
PAGES['best-iptv-australia'] = dict(
    name='Best IPTV Australia', title='Best IPTV Australia 2026: Top-Rated IPTV Subscription Guide',
    desc='Looking for the best IPTV Australia? Learn how to pick a top-rated IPTV subscription, test it with a free trial on your NBN, and set it up on your TV or IPTV box.',
    hero=hero('Buyer’s Guide 2026', 'Best IPTV Australia: Top-Rated IPTV Subscription Guide',
              'How to choose an IPTV service that works on your NBN, carries the sport you watch and sets up in minutes on your TV. Test it free for 24 hours first.',
              IMG + 'home/living-room-hero.webp', 'Smart TV in an Australian living room',
              ['Free 24-hour trial before you pay', 'Plans in AUD from 3 to 12 months', 'Fire TV, Android TV, Apple TV, Samsung and LG', 'WhatsApp and email support']),
    body=section('How to pick the best IPTV in Australia', b1), faq=faq1,
    cta=cta('Test the best IPTV Australia has to offer, free', 'Start a 24-hour trial on your own TV and NBN connection.', 'Hi, I want to test IPTV in Australia with a free trial'))

# ---- 2. iptv-box-australia
faq2 = [
    ('What is the best IPTV box in Australia?', 'For performance, the Nvidia Shield TV Pro is the strongest Android TV box. For value, an Android TV box such as the Xiaomi Mi Box S works well. For a simple IPTV-first experience, look at Formuler or MAG boxes. A Fire TV Stick 4K is the cheapest way to start.'),
    ('Do I need an IPTV box if I have a smart TV?', 'No. Many Samsung, LG and Android smart TVs can run an IPTV player directly. A box helps if your TV is old or slow, or if you want a wired network connection.'),
    ('Is an IPTV box better than a Fire Stick?', 'A dedicated box usually has faster menus, more storage and an Ethernet port. A Fire TV Stick 4K is cheaper and good enough for one TV on stable Wi-Fi.'),
    ('Which IPTV player works on an Android TV box?', 'TiviMate and IPTV Smarters Pro are the most popular IPTV players on Android TV boxes. See the IPTV player guide.'),
    ('Can I use an IPTV box with a free trial?', 'Yes. Any IPTV box that can install an IPTV player can use a free trial. Start a trial and add the login details to your player.'),
]
b2 = (
    '<p>An <strong>IPTV box</strong> is a small streaming device that plugs into your TV and runs an IPTV player. The right <strong>IPTV box in Australia</strong> depends on your TV, your internet and your budget. This guide compares the main options so you can choose in a few minutes.</p>'
    + '<h3>IPTV boxes compared</h3>'
    + table(['Device', 'Best for', 'Strengths', 'Watch out for'],
            [['<strong>Nvidia Shield TV Pro</strong>', 'Best performance', 'Fast, handles 4K and large playlists, long software support', 'Highest price'],
             ['<strong>Android TV box</strong> (e.g. Xiaomi Mi Box S)', 'Best value', 'Cheap, runs TiviMate and Smarters Pro well', 'Avoid unbranded boxes with no updates'],
             ['<strong>Formuler Z series</strong>', 'IPTV-first experience', 'Simple remote and menus, built for IPTV', 'Uses its own app (MyTVOnline)'],
             ['<strong>MAG 524 / 540</strong>', 'Portal-style IPTV', 'Dedicated IPTV hardware, reliable', 'Setup uses a portal URL'],
             ['<strong>Fire TV Stick 4K</strong>', 'Cheapest start', 'Low price, easy app install', 'Less storage and no Ethernet on the stick'],
             ['<strong>Apple TV 4K</strong>', 'Apple households', 'Smooth and reliable, great picture', 'Fewer IPTV apps']])
    + '<h3 style="margin-top:2rem;">What to look for before you buy</h3>'
    + cards([('fa-display', '4K output', 'HDMI 2.0 or newer and HDR support if your TV has it.'),
             ('fa-network-wired', 'Ethernet port', 'A wired connection avoids Wi-Fi drop-outs on busy NBN evenings.'),
             ('fa-memory', 'Memory and storage', 'At least 2 GB RAM and 16 GB storage for a smooth IPTV player.'),
             ('fa-store', 'Official app store', 'Choose a box with Google Play or Amazon Appstore and regular updates.'),
             ('fa-shield-halved', 'Local warranty', 'Buy from an Australian retailer so you get Australian consumer protection.'),
             ('fa-plug', 'Power and HDMI', 'Check that your TV has a free HDMI port that supports your box.')])
    + '<h3 style="margin-top:2rem;">Set up your IPTV box in 4 steps</h3>'
    + steps([('Connect and update', 'Plug the box into HDMI and power, connect to your network (use Ethernet if you can) and install system updates.'),
             ('Install an IPTV player', 'Add TiviMate or IPTV Smarters Pro from the app store. See the <a href="../iptv-player-australia/index.html">IPTV player guide</a>.'),
             ('Add your login', 'Enter the server URL, username and password from your trial or subscription.'),
             ('Test and tune', 'Watch live sport, set favourites and load the programme guide. If you see buffering, read the <a href="../guides/how-to-fix-iptv-buffering-australia/index.html">buffering guide</a>.')])
    + '<p style="margin-top:1.25rem;">Step-by-step guides: <a href="../devices/nvidia-shield-pro-4k-iptv-australia/index.html">Nvidia Shield</a>, <a href="../devices/iptv-on-android-tv-box-australia/index.html">Android TV box</a>, <a href="../devices/formuler-z-mol3-iptv-australia/index.html">Formuler</a>, <a href="../devices/mag-box-stalker-portal-australia/index.html">MAG box</a>, <a href="../devices/iptv-on-amazon-firestick-australia/index.html">Fire TV Stick</a>.</p>'
    + '<h2 class="section-title" style="margin-top:2.5rem;">IPTV box questions</h2>' + faq(faq2))
PAGES['iptv-box-australia'] = dict(
    name='IPTV Box Australia', title='Best IPTV Box Australia: Shield, Android TV, Formuler and MAG',
    desc='Choosing an IPTV box in Australia? Compare Nvidia Shield, Android TV boxes, Formuler, MAG and Fire Stick, with a buying checklist and setup guide.',
    hero=hero('IPTV Box Guide', 'Best IPTV Box Australia: Which One Should You Buy?',
              'Compare the Nvidia Shield, Android TV boxes, Formuler, MAG and Fire TV Stick, then set yours up and test it with a free IPTV trial.',
              IMG + 'iptv/devices/iptv-apple-tv.webp', 'IPTV box and remote next to a TV',
              ['Clear comparison of the popular IPTV boxes', 'Buying checklist for Australian homes', 'Step-by-step setup guides', 'Test any box with a free trial']),
    body=section('IPTV box comparison and buying guide', b2), faq=faq2,
    cta=cta('Already have a box? Test IPTV on it free', 'Request a 24-hour trial and add the login details to your IPTV player.', 'Hi, I have an IPTV box and want a free trial'))

# ---- 3. iptv-player-australia
faq3 = [
    ('What is the best IPTV player in Australia?', 'TiviMate is a favourite on Fire TV Stick and Android TV boxes. IPTV Smarters Pro is the most compatible across phones, tablets and PCs. IBO Player is common on Samsung and LG smart TVs.'),
    ('Does an IPTV player include channels?', 'No. An IPTV player is only the app. You add the login details or playlist from your IPTV provider to see channels.'),
    ('What is the difference between M3U and Xtream Codes?', 'An M3U playlist is a single link to your channel list. Xtream Codes uses a server URL, username and password and also loads the programme guide and movies more neatly. Most players support both.'),
    ('Why are my channels buffering in my IPTV player?', 'Buffering is often your network. Try a wired connection, restart the router, or change DNS. If a single channel fails, try another. Read our IPTV buffering guide for a step-by-step fix.'),
    ('Can I use the free trial with any IPTV player?', 'Yes. Start a free trial and enter the details in TiviMate, IPTV Smarters Pro, IBO Player or another supported player.'),
]
b3 = (
    '<p>An <strong>IPTV player</strong> is the app that plays your channels. It does not come with channels: you add the login details from your IPTV provider. Picking the right <strong>IPTV player app in Australia</strong> depends on your device, so here is what to use where.</p>'
    + '<h3>IPTV players compared</h3>'
    + table(['Player', 'Best on', 'Why people use it', 'Guide'],
            [['<strong>TiviMate</strong>', 'Fire TV, Android TV', 'Clean guide-style layout, favourites, recording in premium', '<a href="../devices/tivimate-iptv-player-australia-setup/index.html">Setup</a>'],
             ['<strong>IPTV Smarters Pro</strong>', 'Android, iPhone, iPad, PC', 'Free, works almost everywhere, simple login', '<a href="../devices/iptv-smarters-pro-australia-guide/index.html">Setup</a>'],
             ['<strong>IBO Player</strong>', 'Samsung, LG smart TVs', 'Works where you cannot sideload apps', '<a href="../devices/ibo-player-australia-activation/index.html">Activation</a>'],
             ['<strong>Smart STB / Hot Player</strong>', 'Smart TVs', 'Simple smart TV alternatives', '<a href="../devices/iptv-on-samsung-smart-tv-tizen-australia/index.html">Samsung TV</a>'],
             ['<strong>Kodi (IPTV Simple Client)</strong>', 'PC, Android, Fire TV', 'Highly customisable media centre', '<a href="../devices/kodi-iptv-simple-client-australia/index.html">Kodi setup</a>'],
             ['<strong>VLC</strong>', 'Windows, Mac', 'Quick test of an M3U link', '<a href="../devices/windows-mac-pc-iptv-player-australia/index.html">PC guide</a>']])
    + '<h3 style="margin-top:2rem;">Which IPTV player should you pick?</h3>'
    + cards([('fa-fire', 'Fire TV Stick or Android TV box', 'Start with TiviMate for the best TV experience.'),
             ('fa-tv', 'Samsung or LG smart TV', 'Use IBO Player or another smart TV player from the TV app store.'),
             ('fa-mobile-screen', 'Phone, tablet or PC', 'IPTV Smarters Pro is the simplest cross-platform choice.')], 3)
    + '<h3 style="margin-top:2rem;">Add your IPTV login in 3 steps</h3>'
    + steps([('Install the player', 'Download the IPTV player from your device app store.'),
             ('Choose the login type', 'Pick Xtream Codes (server URL, username, password) or paste an M3U link.'),
             ('Load channels and the guide', 'Wait for the playlist and programme guide (EPG) to load, then add your favourites.')])
    + '<h2 class="section-title" style="margin-top:2.5rem;">IPTV player questions</h2>' + faq(faq3))
PAGES['iptv-player-australia'] = dict(
    name='IPTV Player Australia', title='Best IPTV Player App Australia: TiviMate, Smarters Pro and IBO',
    desc='Which IPTV player app should you use in Australia? Compare TiviMate, IPTV Smarters Pro, IBO Player and Kodi, with setup guides for Fire TV, Android, Apple, Samsung and LG.',
    hero=hero('IPTV Player Guide', 'Best IPTV Player App for Australia',
              'Compare TiviMate, IPTV Smarters Pro, IBO Player and more. Pick the right IPTV player for your TV, phone or PC and add your login in minutes.',
              IMG + 'iptv/devices/iptv-android-tv.webp', 'Android TV running an IPTV player app',
              ['Player picks for Fire TV, Android, Apple, Samsung and LG', 'M3U and Xtream Codes explained', 'Step-by-step setup guides', 'Test any player with a free trial']),
    body=section('IPTV player apps compared', b3), faq=faq3,
    cta=cta('Pick a player, then test it free', 'Request a 24-hour trial and add the login to your IPTV player.', 'Hi, I picked an IPTV player and want a free trial'))

# ---- 4. iptv-free-trial-australia
faq4 = [
    ('How do I get an IPTV free trial in Australia?', 'Tap the Start Free 24H Trial button, tell us your device and email, or message us on WhatsApp. You will get login details to add to an IPTV player such as TiviMate, IPTV Smarters Pro or IBO Player.'),
    ('Do I need a credit card for the trial?', 'No. The free trial does not need a credit card.'),
    ('How long is the IPTV free trial?', 'The trial lasts 24 hours so you can test live sport at peak time and different channels on your own connection.'),
    ('What should I test during an IPTV trial?', 'Watch live sport on a Friday or Saturday night, change channels quickly, check the programme guide, and try a few movies in 4K if your connection allows.'),
    ('What if the trial buffers?', 'Try a wired connection, restart your router or change DNS. If it still buffers, message us on WhatsApp with your device and internet provider.'),
]
b4 = (
    '<p>The easiest way to choose an IPTV service is to try it on your own TV and internet. An <strong>IPTV free trial in Australia</strong> shows you real channel quality, how fast channels change and whether the stream holds up on your NBN plan, before you spend anything.</p>'
    + '<h3>How the 24-hour IPTV free trial works</h3>'
    + steps([('Request your trial', 'Use the button on this page and share your device and email. It takes about a minute.'),
             ('Add the login to a player', 'Open TiviMate, IPTV Smarters Pro or IBO Player and enter the details. See the <a href="../iptv-player-australia/index.html">player guide</a>.'),
             ('Test what matters to you', 'Watch live AFL or NRL, news and a movie. Try both Wi-Fi and a wired connection if you can.'),
             ('Decide with confidence', 'If it works well, choose a 3, 6 or 12-month plan in AUD on the <a href="../index.html#pricing">pricing section</a>.')])
    + '<h3 style="margin-top:2rem;">Your trial checklist</h3>'
    + cards([('fa-futbol', 'Live sport at peak time', 'Friday and Saturday night is the real test.'),
             ('fa-bolt', 'Channel change speed', 'Flick between channels and see how quickly they load.'),
             ('fa-calendar-days', 'Programme guide', 'Check the EPG matches the Australian time zone.'),
             ('fa-film', 'Movies and series', 'Open a few titles and check the picture quality.'),
             ('fa-wifi', 'Your own network', 'Compare Wi-Fi and Ethernet on the same stream.'),
             ('fa-headset', 'Support response', 'Send a question and see how quickly you get a reply.')])
    + '<h3 style="margin-top:2rem;">Red flags when choosing an IPTV service</h3>'
    + '<ul class="check-list"><li>No trial and no way to test before paying.</li><li>Unclear pricing or prices not shown in AUD.</li><li>No support contact other than a form.</li><li>No information about which devices and players are supported.</li></ul>'
    + '<p><strong>Choose licensed content.</strong> Make sure any IPTV service has the rights to the channels it offers. See our <a href="../guides/is-iptv-legal-in-australia-2026-guide/index.html">IPTV legality guide</a>.</p>'
    + '<h2 class="section-title" style="margin-top:2.5rem;">IPTV free trial questions</h2>' + faq(faq4))
PAGES['iptv-free-trial-australia'] = dict(
    name='IPTV Free Trial Australia', title='IPTV Free Trial Australia: 24-Hour Test on Your Own TV',
    desc='Get an IPTV free trial in Australia. Test live sport, channels and your NBN connection for 24 hours before you pay. No credit card needed.',
    hero=hero('Free 24H Trial', 'IPTV Free Trial Australia: Test It on Your Own TV',
              'Try IPTV free for 24 hours on your own TV and NBN connection. No credit card. Add the login to your IPTV player and decide with confidence.',
              IMG + 'home/streaming-device-remote.webp', 'Streaming box and remote beside a TV',
              ['No credit card needed', 'Works with TiviMate, Smarters Pro and IBO Player', 'Test live sport at peak time', 'WhatsApp and email help']),
    body=section('How the IPTV free trial works', b4), faq=faq4,
    cta=cta('Start your free IPTV trial now', 'It takes about a minute. Test it on your own TV and internet.', 'Hi, I want a free IPTV trial'))

# ------------------------------------------------------------------ write pages
for slug, p in PAGES.items():
    os.makedirs(slug, exist_ok=True)
    page = (head(p['title'], p['desc'], slug, p['name'], p['faq'], None) + TOP + crumbs(p['name']) + p['hero'] + p['body'] + p['cta'] + related(slug) + '\n  ' + FOOT)
    open(os.path.join(slug, 'index.html'), 'w', encoding='utf8').write(page)
    print('wrote', slug, len(page) // 1024, 'KB')

# sitemap
sm = open('sitemap-core.xml', encoding='utf8').read()
for slug in PAGES:
    loc = '%s/%s/' % (SITE, slug)
    if loc not in sm:
        sm = sm.replace('</urlset>', '  <url>\n    <loc>%s</loc>\n    <lastmod>2026-10-11</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n  </url>\n</urlset>' % loc)
open('sitemap-core.xml', 'w', encoding='utf8').write(sm)
print('DONE')

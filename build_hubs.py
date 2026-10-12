"""Builds one hub page per content section (devices, sports, guides, comparisons, ISPs, languages, cities).
Hubs give the site a clear structure: Home > Hub > Page, with every page reachable in two clicks."""
import glob, html as H, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import site_shell as S

KEY_CITIES = ['sydney', 'melbourne', 'brisbane', 'perth', 'adelaide', 'canberra', 'hobart', 'darwin', 'gold-coast', 'newcastle']

def meta(path):
    s = open(path, encoding='utf8', errors='ignore').read()
    t = re.search(r'<title>(.*?)</title>', s, re.S); t = H.unescape(t.group(1).strip()) if t else ''
    d = re.search(r'name="description" content="([^"]*)"', s); d = H.unescape(d.group(1)) if d else ''
    h = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S); h = re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', h.group(1)))).strip() if h else t
    return t.split(' | ')[0], h, d, 'noindex' in s

HUBS = [
 dict(slug='devices', name='Devices', icon='fa-tv', badge='Setup Guides', h1='IPTV Setup Guides for Every Device in Australia',
      title='IPTV Setup Guides for Fire Stick, Android TV, Apple TV, LG',
      desc='Step-by-step IPTV setup guides for Fire TV Stick, Android TV box, Apple TV, Samsung, LG, Nvidia Shield, MAG, Formuler, phones and PC in Australia.',
      intro=['Getting IPTV running is mostly about picking the right player app for your device. Choose your device below for a step-by-step guide, from installing the app to adding your login and loading the programme guide.',
             'Not sure which device to buy? Read the <a href="../iptv-box-australia/index.html">IPTV box guide</a>, or compare apps in the <a href="../iptv-player-australia/index.html">IPTV player guide</a>. You can test any setup with a <a href="../iptv-free-trial-australia/index.html">free 24-hour trial</a>.'],
      pages=lambda: sorted(glob.glob('devices/*/index.html'))),
 dict(slug='sports', name='Sports', icon='fa-futbol', badge='Live Sport', h1='Watch Australian Sport on IPTV: AFL, NRL, Cricket and More',
      title='Australian Sport on IPTV: AFL, NRL, Cricket, F1 and UFC',
      desc='Guides to watching AFL, NRL, cricket, F1, UFC, rugby, tennis and soccer on IPTV in Australia, with channel notes and tips for a stable stream on NBN.',
      intro=['Live sport is where a weak connection shows first. Each guide below covers one sport: what to watch, when it is on and how to get a stable stream on your NBN plan.',
             'Test your setup during a real match with the <a href="../iptv-free-trial-australia/index.html">free 24-hour trial</a>, and see our <a href="../guides/how-to-fix-iptv-buffering-australia/index.html">buffering guide</a> if a stream stutters.'],
      pages=lambda: sorted(p for p in glob.glob('sports/*/index.html'))),
 dict(slug='guides', name='Guides', icon='fa-book-open', badge='How-To Guides', h1='IPTV Guides for Australia: Buffering, VPN, Payments and More',
      title='IPTV Guides Australia: Buffering, VPN, Legal and Setup',
      desc='Practical IPTV guides for Australians: fix buffering, choose a VPN, understand legality, pay with PayID, set DNS and read the programme guide.',
      intro=['Short, practical guides for the questions Australians ask most about IPTV: speed and buffering, DNS, payments, legality and how playlists work.'],
      pages=lambda: sorted(glob.glob('guides/*/index.html'))),
 dict(slug='comparisons', name='Comparisons', icon='fa-scale-balanced', badge='Compare', h1='IPTV vs Foxtel, Kayo, Binge and Other Services',
      title='IPTV vs Foxtel, Kayo, Binge, Stan Sport, Optus Sport and Fetch',
      desc='Compare IPTV with Foxtel, Kayo, Binge, Stan Sport, Optus Sport, Fetch and Sky Sports in Australia: what you get, how you watch and what to check first.',
      intro=['Thinking about switching from pay TV or a sports app? These comparisons explain the differences in plain language so you can decide with the facts.',
             'Whatever you choose, make sure the service has the rights to the content it sells. Read the <a href="../guides/is-iptv-legal-in-australia-2026-guide/index.html">IPTV legality guide</a>.'],
      pages=lambda: sorted(glob.glob('comparisons/*/index.html'))),
 dict(slug='isps', name='Internet Providers', icon='fa-network-wired', badge='NBN and ISPs', h1='IPTV on Telstra, Optus, TPG, Aussie Broadband and Starlink',
      title='IPTV on Telstra, Optus, TPG, Aussie Broadband and Starlink NBN',
      desc='How to get a stable IPTV stream on Telstra, Optus, TPG, Aussie Broadband and Starlink: DNS, Wi-Fi, wired connections and peak-time tips.',
      intro=['Your internet provider and home network matter as much as the IPTV service. These guides cover the common fixes for each major Australian provider.',
             'Need to know how fast your plan should be? Try the <a href="../tools/iptv-bandwidth-calculator/index.html">IPTV bandwidth calculator</a>.'],
      pages=lambda: sorted(glob.glob('isps/*/index.html'))),
 dict(slug='languages', name='Languages', icon='fa-language', badge='Multicultural TV', h1='Multicultural and Language TV on IPTV in Australia',
      title='Arabic, Indian, Greek, Italian, Chinese TV on IPTV Australia',
      desc='Guides to watching Arabic, Hindi, Punjabi, Tamil, Greek, Italian, Chinese, Vietnamese and Filipino TV channels on IPTV in Australia.',
      intro=['Australia is home to many communities who want TV from home. These guides explain how to find and watch channels in your language on IPTV.'],
      pages=lambda: sorted(glob.glob('languages/*/index.html'))),
]

def card(href, title, desc, icon):
    d = desc if len(desc) <= 130 else desc[:127].rsplit(' ', 1)[0] + '...'
    return ('<a class="hub-card" href="%s"><i class="fa-solid %s"></i><h3>%s</h3><p>%s</p><span>Read more <i class="fa-solid fa-arrow-right"></i></span></a>'
            % (href, icon, S.e(title), S.e(d)))

built = []
for h in HUBS:
    items = []
    for p in h['pages']():
        p = p.replace(os.sep, '/')
        t, h1, d, ni = meta(p)
        if ni: continue
        slug = p.split('/')[1]
        items.append((slug, t, d))
    cards = ''.join(card('%s/index.html' % slug, t, d, h['icon']) for slug, t, d in items)
    ld = [S.breadcrumb_ld([('Home', S.SITE + '/'), (h['name'], '%s/%s/' % (S.SITE, h['slug']))]),
          {"@context": "https://schema.org", "@type": "CollectionPage", "name": h['h1'], "description": h['desc'], "url": '%s/%s/' % (S.SITE, h['slug']), "inLanguage": "en-AU",
           "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [
               {"@type": "ListItem", "position": i + 1, "url": '%s/%s/%s/' % (S.SITE, h['slug'], s_), "name": t} for i, (s_, t, d) in enumerate(items)]}}]
    body = (S.page_hero(h['badge'], h['h1'], h['intro'][0])
            + '<section style="padding:1rem 0 4rem; background:var(--bg-main);"><div class="container"><div class="prose-block" style="max-width:900px;">%s</div>'
              '<div class="hub-grid" style="margin-top:2rem;">%s</div></div></section>' % (''.join('<p style="line-height:1.8;">%s</p>' % x for x in h['intro'][1:]), cards)
            + S.cta_band('Test IPTV on your own device, free', 'Request a 24-hour trial and try the guide for your device.', 'Hi, I read your %s guides and want a free trial' % h['name'].lower()))
    html = S.assemble(1, S.head(h['title'], h['desc'], h['slug'] + '/', 1, ld), S.crumbs([(h['name'], None)], 1), body)
    S.write(h['slug'], html)
    S.add_to_sitemap(h['slug'] + '/', '0.7')
    built.append((h['slug'], len(items)))

# cities hub: ten key cities up front, every other city listed in a collapsed block (those pages stay noindex)
keys = []
for c in KEY_CITIES:
    p = 'cities/%s/index.html' % c
    if os.path.exists(p):
        t, h1, d, ni = meta(p)
        keys.append((c, c.replace('-', ' ').title(), d))
others = []
for p in sorted(glob.glob('cities/*/index.html')):
    p = p.replace(os.sep, '/')
    c = p.split('/')[1]
    if c in KEY_CITIES: continue
    others.append('<a href="%s/index.html">%s</a>' % (c, c.replace('-', ' ').title()))
cards = ''.join(card('%s/index.html' % c, 'IPTV %s' % n, d, 'fa-location-dot') for c, n, d in keys)
ld = [S.breadcrumb_ld([('Home', S.SITE + '/'), ('Cities', S.SITE + '/cities/')]),
      {"@context": "https://schema.org", "@type": "CollectionPage", "name": "IPTV by Australian City", "url": S.SITE + '/cities/', "inLanguage": "en-AU",
       "mainEntity": {"@type": "ItemList", "numberOfItems": len(keys), "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": '%s/cities/%s/' % (S.SITE, c), "name": 'IPTV ' + n} for i, (c, n, d) in enumerate(keys)]}}]
body = (S.page_hero('Cities', 'IPTV in Australian Cities: Sydney, Melbourne, Brisbane, Perth and More',
                    'Local guides for watching live sport and TV in Australia\'s biggest cities, with notes on local teams and how to get a stable stream on your home internet.')
        + '<section style="padding:1rem 0 4rem; background:var(--bg-main);"><div class="container"><div class="hub-grid" style="margin-top:1rem;">%s</div>'
          '<details class="more-details" style="margin-top:2.5rem;"><summary><span>Show all other towns and cities</span></summary><div class="chip-row" style="margin-top:1rem;">%s</div></details></div></section>' % (cards, ''.join(others))
        + S.cta_band('Try IPTV where you live, free', 'Request a 24-hour trial and test it on your own internet.', 'Hi, I want a free IPTV trial'))
S.write('cities', S.assemble(1, S.head('IPTV in Australian Cities: Sydney, Melbourne, Brisbane, Perth',
        'Local IPTV guides for Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra, Hobart, Darwin, Gold Coast and Newcastle, with local sport notes and setup tips.',
        'cities/', 1, ld), S.crumbs([('Cities', None)], 1), body))
S.add_to_sitemap('cities/', '0.7')
built.append(('cities', len(keys)))
print('hubs built:', built)
print('DONE')

"""Audit fixes, part 2: unique content for language pages, contextual internal links, structured data and content for the root pages."""
import glob, html as H, json, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://4kaustraliaiptv.com'
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)
def ul(xs): return '<ul class="check-ok">' + ''.join('<li>%s</li>' % x for x in xs) + '</ul>'
def steps(xs): return '<ol class="steps-list">' + ''.join('<li><span class="step-number">%d</span><div><h4>%s</h4><p>%s</p></div></li>' % (i + 1, a, b) for i, (a, b) in enumerate(xs)) + '</ol>'
def table(h, rows): return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (''.join('<th>%s</th>' % x for x in h), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows))
def block(cls, body): return '\n  <section class="%s" style="padding:3.5rem 0; background:var(--bg-main);"><div class="container"><article class="prose-block legal">%s</article></div></section>\n' % (cls, body)
def before_footer(s, html, prefer_related=True):
    k = s.find('<section class="related-section"') if prefer_related else -1
    if k < 0: k = s.find('<section class="cta-band')
    if k < 0: k = s.find('<footer')
    return s[:k] + html + s[k:]
stats = {}
def bump(k): stats[k] = stats.get(k, 0) + 1

# ================================================================= A. languages: community-specific content
LANG = {
 'arabic-lebanese-iptv-australia': ('Arabic and Lebanese TV', 'Arabic is one of the larger community languages in Australia, with strong communities in Sydney and Melbourne. Viewers often ask for the MBC group, Rotana, Al Jazeera and Lebanese channels such as LBC and MTV Lebanon.',
   ['Ask whether the service lists your dialect’s main channels, not only Gulf channels.', 'Ramadan drama series are watched heavily, so test the weeks around Ramadan.', 'Beirut is 8 to 9 hours behind Sydney, so live news from home arrives in the Australian evening or morning.'], 'Arabic and Lebanese'),
 'chinese-mandarin-cantonese-iptv-australia': ('Mandarin and Cantonese TV', 'Mandarin and Cantonese are among the most spoken languages other than English in Australia. Common requests include CCTV, Phoenix TV and TVB from Hong Kong, plus Chinese movies and series.',
   ['Check subtitles: Simplified Chinese, Traditional Chinese or English.', 'Beijing and Hong Kong are 2 to 3 hours behind Sydney, so live evening shows air in your late evening.', 'Lunar New Year galas draw big audiences, so test your setup before the event.'], 'Mandarin and Cantonese'),
 'filipino-tagalog-tv-iptv-australia': ('Filipino TV', 'Filipino viewers in Australia usually look for TFC, GMA Pinoy TV and Philippine teleseryes, news and variety shows.',
   ['Philippine time is 2 to 3 hours behind Sydney.', 'Check whether teleseryes are available on demand as well as live.', 'Basketball and boxing fans should check sport channels separately.'], 'Filipino'),
 'greek-tv-channels-iptv-australia': ('Greek TV', 'Greek-speaking communities, especially in Melbourne and Adelaide, often look for ERT, Mega and Antenna, plus Greek news, drama and football.',
   ['Athens is 8 to 9 hours behind Sydney, so check your guide time zone.', 'Greek Orthodox Easter coverage is watched widely.', 'Football fans should check which Greek league games are included.'], 'Greek'),
 'indian-hindi-tv-channels-iptv-australia': ('Hindi and Indian TV', 'Hindi and wider Indian TV is popular across Sydney, Melbourne and Perth. Viewers often ask for Star Plus, Zee TV, Sony and Colors, plus news and Bollywood movies.',
   ['India is 5.5 hours behind Sydney in daylight saving time, so prime-time shows air in the Australian night.', 'Cricket fans should check which tournaments, such as the IPL, are included. The IPL usually runs from March to May.', 'Festival programming around Diwali is popular.'], 'Hindi'),
 'italian-tv-channels-iptv-australia': ('Italian TV', 'Italian communities in Melbourne, Sydney and Adelaide often look for Rai Italia, Mediaset channels, Italian news and Serie A football.',
   ['Rome is 9 to 10 hours behind Sydney, so evening shows air in the Australian morning.', 'The Sanremo music festival in February is a highlight for many viewers.', 'Football fans should check Serie A rights separately.'], 'Italian'),
 'punjabi-tv-channels-iptv-australia': ('Punjabi TV', 'Punjabi TV is growing quickly with Australia’s Punjabi-speaking communities. Viewers look for Punjabi news, music, drama and religious programming, including PTC Punjabi and Zee Punjabi.',
   ['India is 5.5 hours behind Sydney during daylight saving time.', 'Kabaddi and Punjabi music channels are popular, so check they are listed.', 'Baisakhi and Gurpurab programming is watched widely.'], 'Punjabi'),
 'tamil-telugu-iptv-australia': ('Tamil and Telugu TV', 'Tamil and Telugu viewers commonly look for Sun TV, Star Vijay, Zee Tamil, Gemini TV and Telugu entertainment and movie channels.',
   ['Check that both Tamil and Telugu channels are listed, as some services carry only one.', 'India is 5.5 hours behind Sydney in daylight saving time.', 'Cricket fans should check which IPL coverage is available.'], 'Tamil and Telugu'),
 'vietnamese-tv-channels-iptv-australia': ('Vietnamese TV', 'Vietnamese-speaking communities, notably in Melbourne and Sydney, often look for VTV4, SBTN and Vietnamese news, music and drama.',
   ['Vietnam is 4 hours behind Sydney during daylight saving time.', 'Tet (Lunar New Year) programming is a highlight.', 'Check for Vietnamese subtitles on movies and series.'], 'Vietnamese'),
}
for slug, (name, intro, checks, short) in LANG.items():
    p = 'languages/%s/index.html' % slug
    if not os.path.exists(p): continue
    s = rd(p)
    if 'lang-specific' in s: continue
    body = ('<h2>%s on IPTV in Australia</h2><p>%s</p><h3>What to check before you subscribe</h3>%s<p>Channel line-ups change, so always confirm the channels you want in the service’s list and test them during the free trial.</p>') % (name, intro, ul(checks))
    s = before_footer(s, block('content-pass lang-specific', body)); wr(p, s); bump('languages')

# ================================================================= B. contextual links
CITIES = [('sydney', 'Sydney'), ('melbourne', 'Melbourne'), ('brisbane', 'Brisbane'), ('perth', 'Perth'), ('adelaide', 'Adelaide'), ('canberra', 'Canberra'), ('hobart', 'Hobart'), ('darwin', 'Darwin'), ('gold-coast', 'Gold Coast'), ('newcastle', 'Newcastle')]
def city_chips(kind, label, depth=1):
    pre = '../' * depth
    return ('<section style="padding:2.5rem 0; background:var(--bg-secondary);"><div class="container"><div class="chip-row" style="margin-top:0;"><span>%s</span>%s</div></div></section>\n'
            % (label, ''.join('<a href="%scities/%s/%s/index.html">%s</a>' % (pre, c, kind, n) for c, n in CITIES)))
for p, kind, label in (('iptv-free-trial-australia/index.html', 'free-trial', 'Free trial by city:'), ('best-iptv-australia/index.html', 'best-iptv', 'Best IPTV by city:'), ('sports/index.html', 'sports-channels', 'Sport on IPTV by city:')):
    s = rd(p)
    if label in s: continue
    extra = city_chips(kind, label)
    if p.startswith('best-iptv'): extra += city_chips('subscription', 'IPTV subscription by city:')
    k = s.find('<section class="cta-band')
    s = s[:k] + extra + s[k:]; wr(p, s); bump('pillar-to-city links')
for c, n in CITIES:
    kinds = [('best-iptv', 'Best IPTV in %s'), ('subscription', 'IPTV subscription in %s'), ('free-trial', 'Free trial in %s'), ('sports-channels', 'Sport on IPTV in %s')]
    for kind, _ in kinds:
        p = 'cities/%s/%s/index.html' % (c, kind)
        if not os.path.exists(p): continue
        s = rd(p)
        if 'More for %s' % n in s: continue
        links = ''.join('<a href="../%s/index.html">%s</a>' % (k2, t % n) for k2, t in kinds if k2 != kind) + '<a href="../index.html">All %s guides</a>' % n
        blk = '<section class="related-section" style="padding:2.5rem 0; background:var(--bg-secondary);"><div class="container"><div class="chip-row" style="margin-top:0;"><span>More for %s:</span>%s</div></div></section>\n' % (n, links)
        k = s.find('<footer'); s = s[:k] + blk + s[k:]; wr(p, s); bump('city sibling links')
# homepage: reseller and setup sections link to their own pages
s = rd('index.html')
for sid, text in (('calculator', '<p style="margin-top:.75rem;"><a href="reseller.html">How the reseller panel works</a> &middot; <a href="guides/how-to-start-iptv-reseller-business-australia/index.html">Start an IPTV reseller business: the guide</a></p>'),
                  ('setup', '<p style="margin-top:.75rem;"><a href="setup.html">Setup overview for every device</a> &middot; <a href="devices/index.html">All device guides</a></p>')):
    j = s.find('id="%s"' % sid); e = s.find('</section>', j); k = s.find('</p>', s.find('section-subtitle', j)) + 4
    if j > 0 and 0 < k < e and text not in s: s = s[:k] + text + s[k:]; bump('homepage links')
wr('index.html', s)
# privacy policy linked from where data is collected; reseller guide + devices hub link to their commercial/setup pages
for p, marker, add in (('contact.html', '</form>', '<p style="font-size:.85rem; color:var(--text-dim); margin-top:1rem;">We use your details only to reply. Read our <a href="privacy-policy/index.html">Privacy Policy</a>.</p>'),
                       ('terms-of-service/index.html', '<h2>Changes and contact</h2>', '<h2>Your information</h2><p>How we handle your details is explained in our <a href="../privacy-policy/index.html">Privacy Policy</a>.</p>'),
                       ('about/index.html', '<h2>Contact us</h2>', '<p>Read our <a href="../privacy-policy/index.html">Privacy Policy</a>, <a href="../terms-of-service/index.html">Terms of Service</a> and <a href="../refund-policy/index.html">Refund Policy</a>.</p>'),
                       ('guides/how-to-start-iptv-reseller-business-australia/index.html', '<h2>Frequently asked questions</h2>', '<p>Ready to compare credit packs? See the <a href="../../reseller.html">reseller panel page</a> and the <a href="../../index.html#calculator">profit calculator</a>.</p>'),
                       ('devices/index.html', '<div class="hub-grid"', '')):
    if not os.path.exists(p) or not add: continue
    s = rd(p)
    if add in s: continue
    if marker == '</form>':
        k = s.find(marker)
        if k > 0: s = s[:k + len(marker)] + add + s[k + len(marker):]; wr(p, s); bump('privacy/contextual links')
    else:
        k = s.find(marker)
        if k > 0: s = s[:k] + add + s[k:]; wr(p, s); bump('privacy/contextual links')

# ================================================================= C. root pages
ROOT = {
 'providers.html': ('Providers', 'Compare IPTV Providers in Australia'),
 'channels.html': ('Channels', 'IPTV Channels and Sports in Australia'),
 'setup.html': ('Setup', 'IPTV Setup Guides'),
 'reseller.html': ('Reseller', 'IPTV Reseller Panel'),
 'contact.html': ('Contact', 'Contact'),
 'directory/index.html': ('Directory', 'Directory'),
}
for p, (name, _) in ROOT.items():
    s = rd(p)
    t = H.unescape((re.search(r'<title>(.*?)</title>', s, re.S) or [0, ''])[1].strip()); d = H.unescape((re.search(r'name="description" content="([^"]*)"', s) or [0, ''])[1])
    url = SITE + '/' + p[:-10] if p.endswith('/index.html') else SITE + '/' + p
    add = ''
    if 'BreadcrumbList' not in s:
        add += '<script type="application/ld+json">\n%s\n</script>\n' % json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + '/'}, {"@type": "ListItem", "position": 2, "name": name, "item": url}]}, indent=2)
    if 'og:title' not in s:
        add += ('<meta property="og:title" content="%s" />\n<meta property="og:description" content="%s" />\n<meta property="og:type" content="website" />\n<meta property="og:locale" content="en_AU" />\n'
                '<meta property="og:url" content="%s" />\n<meta property="og:image" content="%s/assets/og-au.png" />\n<meta name="twitter:card" content="summary_large_image" />\n<meta name="twitter:image" content="%s/assets/og-au.png" />\n') % (H.escape(t), H.escape(d), url, SITE, SITE)
    if add: s = s.replace('</head>', add + '</head>', 1); wr(p, s); bump('root structured data/og')

CONTENT = {
 'providers.html': block('content-pass', '<h2>How to compare IPTV providers in Australia</h2><p>Provider lists are only a starting point. What matters is how a service behaves on your own internet at the times you watch. Use these checks to compare any two providers fairly.</p>'
   + ul(['<strong>Rights and licensing:</strong> does the service say where its channels come from? Read our <a href="guides/is-iptv-legal-in-australia-2026-guide/index.html">legality guide</a>.', '<strong>A free trial:</strong> you should be able to test before paying.', '<strong>Stability on your NBN:</strong> test during live sport on a Friday or Saturday night.', '<strong>Channels and sport:</strong> check your must-have channels are listed.', '<strong>Devices and apps:</strong> confirm it works with your <a href="iptv-player-australia/index.html">IPTV player</a> and <a href="iptv-box-australia/index.html">box</a>.', '<strong>Clear pricing and support:</strong> prices in AUD and a way to reach a person.'])
   + '<h3>A fair test in four steps</h3>' + steps([('Use the same device', 'Test every provider on the same TV or box.'), ('Use the same connection', 'Prefer a cable to rule out Wi-Fi.'), ('Test the same match', 'Watch the same live event on each.'), ('Write down what you saw', 'Note start time, picture, freezes and how fast support replied.')])
   + '<p>Start with our <a href="iptv-free-trial-australia/index.html">free 24-hour trial</a>, or read the <a href="best-iptv-australia/index.html">best IPTV Australia guide</a> and the <a href="comparisons/index.html">comparisons</a>.</p>'),
 'channels.html': block('content-pass', '<h2>How to check a channel line-up before you subscribe</h2><p>A long channel number does not tell you whether your channels are there. Check the line-up for the channels you actually watch.</p>'
   + steps([('List your must-haves', 'Free-to-air, news, kids and the sport you follow.'), ('Ask for the channel list', 'A service should be able to tell you what is included.'), ('Test during a live event', 'Watch a match or news bulletin, not just a movie.'), ('Check the guide', 'Open the programme guide and confirm times match your time zone.')])
   + '<h2>When Australian sport is on</h2>' + table(['Competition', 'Typical season'], [['Australian Open tennis', 'January'], ['Super Rugby Pacific', 'February to June'], ['AFL', 'March to September'], ['NRL', 'March to October'], ['Formula 1 Australian Grand Prix', 'March'], ['Summer cricket', 'December to February'], ['A-League Men', 'October to May']])
   + '<p>See the <a href="sports/index.html">sports guides</a>, the <a href="guides/iptv-epg-guide-explained-australia/index.html">EPG guide</a> and the <a href="iptv-free-trial-australia/index.html">free trial</a>.</p>'),
 'reseller.html': block('content-pass', '<h2>Before you start an IPTV reselling business</h2><p>Reselling IPTV can be a side business, but it comes with responsibilities. Think through these points before you buy credits.</p>'
   + ul(['<strong>Licensing:</strong> make sure the supply you resell has the rights to its content. You are responsible for what you sell. See the <a href="guides/is-iptv-legal-in-australia-2026-guide/index.html">legality guide</a>.', '<strong>Support time:</strong> customers will message you about setup and buffering. Our <a href="devices/index.html">device guides</a> can help.', '<strong>Pricing:</strong> work out your margin with the <a href="index.html#calculator">profit calculator</a>.', '<strong>Terms and refunds:</strong> publish clear terms and a refund policy, like ours: <a href="refund-policy/index.html">Refund Policy</a>.', '<strong>Trials:</strong> a short trial helps customers decide and reduces refund requests.'])
   + '<p>Questions? <a href="contact.html">Contact us</a> or read the <a href="guides/how-to-start-iptv-reseller-business-australia/index.html">reseller business guide</a>.</p>'),
}
for p, html in CONTENT.items():
    s = rd(p)
    if 'content-pass' in s: continue
    k = s.find('<footer'); s = s[:k] + html + s[k:]; wr(p, s); bump('root content')
# tools hub
p = 'tools/index.html'; s = rd(p)
if 'content-pass' not in s:
    html = block('content-pass', '<h2>Why we built these tools</h2><p>Most IPTV problems come from the home network, not the service. A quick calculation shows whether your plan has enough speed for the screens in your house, and a guide to DNS and EPG settings fixes the next most common issues.</p>' + ul(['<a href="iptv-bandwidth-calculator/index.html">IPTV bandwidth calculator</a>: Mbps and NBN plan for your household.', '<a href="../guides/how-much-internet-speed-for-iptv-australia/index.html">Internet speed guide</a>: what each stream needs.', '<a href="../guides/best-dns-for-iptv-australia/index.html">Best DNS for IPTV</a>: how to change it.']))
    k = s.find('<footer'); s = s[:k] + html + s[k:]; wr(p, s); bump('tools hub content')
print(stats)
print('DONE')

"""Builds the bandwidth calculator (a shareable tool) and three new in-depth guides."""
import html as H, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import site_shell as S

def cards(items, cols=3):
    return '<div class="criteria-grid" style="grid-template-columns:repeat(%d,1fr);">%s</div>' % (cols, ''.join(
        '<div class="criteria"><i class="fa-solid %s"></i><h4>%s</h4><p>%s</p></div>' % x for x in items))
def table(head, rows):
    return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
        ''.join('<th>%s</th>' % h for h in head), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows))
def steps(items):
    return '<ol class="steps-list">%s</ol>' % ''.join('<li><span class="step-number">%d</span><div><h4>%s</h4><p>%s</p></div></li>' % (i + 1, t, d) for i, (t, d) in enumerate(items))
def faq(items):
    return '<div class="faq-accordion" style="margin-top:1rem;">%s</div>' % ''.join(
        '<div class="faq-item"><div class="faq-question"><h3>%s</h3><div class="faq-toggle-icon"><i class="fa-solid fa-plus"></i></div></div><div class="faq-answer"><div class="faq-answer-inner">%s</div></div></div>' % x for x in items)
def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": H.unescape(re.sub('<[^>]+>', '', q)), "acceptedAnswer": {"@type": "Answer", "text": H.unescape(re.sub('<[^>]+>', '', a))}} for q, a in items]}
def share(url, text):
    import urllib.parse as u
    q = u.quote(url, safe=''); t = u.quote(text, safe='')
    return ('<div class="share-row"><span>Share this page:</span>'
            '<a href="https://wa.me/?text=%s%%20%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> WhatsApp</a>'
            '<a href="https://www.facebook.com/sharer/sharer.php?u=%s" target="_blank" rel="noopener"><i class="fa-brands fa-facebook"></i> Facebook</a>'
            '<a href="https://twitter.com/intent/tweet?url=%s&amp;text=%s" target="_blank" rel="noopener"><i class="fa-brands fa-x-twitter"></i> X</a>'
            '<button type="button" data-copy-link="%s"><i class="fa-solid fa-link"></i> Copy link</button></div>') % (t, q, q, q, t, url)
def article(title, desc, path):
    return {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "inLanguage": "en-AU",
            "datePublished": S.TODAY, "dateModified": S.TODAY, "mainEntityOfPage": '%s/%s' % (S.SITE, path),
            "author": {"@type": "Organization", "name": S.BIZ, "url": S.SITE + '/'},
            "publisher": {"@type": "Organization", "name": S.BIZ, "url": S.SITE + '/', "logo": {"@type": "ImageObject", "url": S.SITE + '/assets/og-au.png'}}}
def related(links):
    return ('<section style="padding:3rem 0; background:var(--bg-secondary);"><div class="container"><div class="chip-row" style="margin-top:0;"><span>Related:</span>%s</div></div></section>'
            % ''.join('<a href="%s">%s</a>' % x for x in links))

def guide_page(path, depth, hub, hub_href, title, h1, desc, lead, body, faqs, rel):
    url = '%s/%s' % (S.SITE, path)
    ld = [S.breadcrumb_ld([('Home', S.SITE + '/'), (hub, '%s/%s' % (S.SITE, hub_href)), (h1, url)]), article(title, desc, path), faq_ld(faqs)]
    main = ('<main>' + S.page_hero('Guide', h1, lead)
            + '<section style="padding:1rem 0 4rem; background:var(--bg-main);"><div class="container"><article class="prose-block legal">%s<h2>Frequently asked questions</h2>%s%s</article></div></section>' % (body, faq(faqs), share(url, h1))
            + S.cta_band('Test it on your own connection, free', 'Request a 24-hour IPTV trial and see how it runs on your NBN.', 'Hi, I read your guide: %s. I want a free trial' % h1)
            + related(rel) + '</main>')
    html = S.assemble(depth, S.head(title, desc, path, depth, ld, 'article'), S.crumbs([(hub, hub_href), (h1, None)], depth), main)
    S.write(path.rstrip('/'), html)

# ================================================================= 1. internet speed guide
faq1 = [('How fast does my internet need to be for IPTV?', 'Plan on about 8 Mbps for each Full HD stream and about 25 Mbps for each 4K stream, then add 25% headroom for other devices. One 4K TV on its own is comfortable on an NBN 50 plan; a busy household with several screens is better on NBN 100 or higher.'),
        ('Is Wi-Fi good enough for IPTV?', 'Often yes on a strong 5 GHz signal close to the router, but a wired Ethernet connection is more reliable, especially for live sport at peak time.'),
        ('Why does IPTV buffer in the evening?', 'Evenings are when most households stream at once, so your home network and your internet provider are busiest. Check your provider’s typical evening speed and try a wired connection.'),
        ('Does a faster NBN plan fix buffering?', 'Only if speed was the problem. Buffering is also caused by weak Wi-Fi, an overloaded router or a slow DNS. Test with a wired connection first.')]
b1 = ('<p>The most common reason IPTV stutters is not the service. It is the home internet. This guide shows what speed you actually need and how to check that your connection delivers it when it matters.</p>'
      '<h2>How much speed does one stream need?</h2>'
      + table(['Quality', 'Typical speed per stream', 'Good for'], [['Standard (SD)', 'about 3 Mbps', 'Phones, older TVs'], ['HD (720p)', 'about 5 Mbps', 'Small TVs, tablets'], ['Full HD (1080p)', 'about 8 Mbps', 'Most TVs and live sport'], ['4K (UHD)', 'about 25 Mbps', 'Large 4K TVs']])
      + '<p>These are planning figures. Real streams vary with the channel and how busy the scene is, so keep some spare capacity. Use the <a href="../../tools/iptv-bandwidth-calculator/index.html">IPTV bandwidth calculator</a> to add up your own household.</p>'
      '<h2>Which NBN plan do you need?</h2>'
      + table(['NBN plan', 'Comfortable for'], [['NBN 25', 'One Full HD stream with light use'], ['NBN 50', 'One 4K stream, or two Full HD streams'], ['NBN 100', 'A busy household with a 4K stream plus other devices'], ['NBN 250 and above', 'Several 4K screens at once, heavy downloads']])
      + '<p>Check your internet provider’s <strong>typical evening speed</strong>. Providers publish it for each plan, and it is a better guide than the headline speed.</p>'
      '<h2>5 ways to get a steadier stream</h2>'
      + steps([('Use a cable for the main TV', 'Plug your IPTV box or TV into the router with an Ethernet cable. It removes Wi-Fi interference completely.'),
               ('Improve your Wi-Fi if you cannot use a cable', 'Use the 5 GHz band, sit the router in the open and keep it away from microwaves and thick walls.'),
               ('Restart the router', 'A weekly restart clears many odd problems on home routers.'),
               ('Check what else is using the internet', 'Large downloads, game updates and cloud backups can starve a stream. Pause them during live sport.'),
               ('Try a different DNS', 'A faster DNS can speed up channel loading. See the <a href="../best-dns-for-iptv-australia/index.html">DNS guide</a>.')])
      + '<p>Still stuck? Read the <a href="../how-to-fix-iptv-buffering-australia/index.html">full buffering guide</a>.</p>')
guide_page('guides/how-much-internet-speed-for-iptv-australia/', 2, 'Guides', 'guides/index.html',
           'How Much Internet Speed Do You Need for IPTV in Australia?', 'How Much Internet Speed Do You Need for IPTV?',
           'How many Mbps does IPTV need? See the speed per stream for SD, HD, Full HD and 4K, which NBN plan to choose and 5 ways to stop buffering.',
           'IPTV needs less bandwidth than most people think, but it needs it to be steady. Here is the speed to plan for and how to check your home setup.', b1, faq1,
           [('../../tools/iptv-bandwidth-calculator/index.html', 'Bandwidth calculator'), ('../best-dns-for-iptv-australia/index.html', 'Best DNS for IPTV'), ('../../iptv-box-australia/index.html', 'IPTV box guide'), ('../../iptv-free-trial-australia/index.html', 'Free trial')])
S.add_to_sitemap('guides/how-much-internet-speed-for-iptv-australia/', '0.7')

# ================================================================= 2. DNS guide
faq2 = [('Which DNS is best for IPTV?', 'Cloudflare (1.1.1.1), Google (8.8.8.8) and Quad9 (9.9.9.9) are reliable public DNS services. The best one for you is the one that responds fastest on your connection, so test two or three.'),
        ('Will changing DNS make my IPTV faster?', 'It can make channels start loading faster and fix some lookup problems. It does not raise your internet speed, so it will not fix a connection that is simply too slow.'),
        ('Should I change DNS on the router or the device?', 'Changing it on the router covers every device in the house. Changing it on one device is useful for testing.'),
        ('Is it safe to change DNS?', 'Yes. You can switch back to your provider’s DNS at any time by choosing automatic settings.')]
b2 = ('<p>DNS is the internet’s address book. Your device asks a DNS server where to find a website or stream, so a slow or unreliable DNS can make channels take longer to start. Changing it is free and takes a few minutes.</p>'
      '<h2>Popular public DNS servers</h2>'
      + table(['Provider', 'Primary', 'Secondary'], [['Cloudflare', '1.1.1.1', '1.0.0.1'], ['Google', '8.8.8.8', '8.8.4.4'], ['Quad9', '9.9.9.9', '149.112.112.112']])
      + '<h2>How to change DNS</h2>'
      + steps([('On your router (best)', 'Open your router’s settings page, find the internet or WAN settings, and enter the primary and secondary DNS. Save and restart. Every device now uses it.'),
               ('On an Android TV or Fire TV', 'Open Wi-Fi settings, choose your network, then change IP settings to static and enter the DNS. Wired connections use the router DNS.'),
               ('On Windows', 'Open Network settings, choose your adapter, edit the IPv4 properties and enter the DNS servers.'),
               ('On iPhone or iPad', 'Open Wi-Fi settings, tap the network, choose Configure DNS and enter the servers manually.')])
      + '<h2>Check that it helped</h2><p>Open a few channels before and after the change. If channels start faster and stay stable, keep it. If not, switch back to automatic and look at your <a href="../how-much-internet-speed-for-iptv-australia/index.html">internet speed</a> and Wi-Fi next.</p>')
guide_page('guides/best-dns-for-iptv-australia/', 2, 'Guides', 'guides/index.html',
           'Best DNS for IPTV in Australia: Cloudflare, Google and Quad9', 'Best DNS for IPTV in Australia',
           'Which DNS is best for IPTV in Australia? Compare Cloudflare, Google and Quad9 and learn how to change DNS on your router, TV box, Windows or iPhone.',
           'A faster DNS can help channels start quicker and fix some connection problems. Here are the best public DNS options and exactly how to switch.', b2, faq2,
           [('../how-much-internet-speed-for-iptv-australia/index.html', 'Internet speed for IPTV'), ('../how-to-fix-iptv-buffering-australia/index.html', 'Fix buffering'), ('../../iptv-player-australia/index.html', 'IPTV player guide'), ('../../iptv-free-trial-australia/index.html', 'Free trial')])
S.add_to_sitemap('guides/best-dns-for-iptv-australia/', '0.7')

# ================================================================= 3. EPG guide
faq3 = [('What is an EPG in IPTV?', 'EPG stands for Electronic Programme Guide. It is the on-screen TV guide that shows what is on now and next for each channel.'),
        ('Why is my IPTV guide empty?', 'The most common causes are a guide that has not finished loading, an EPG source that is not linked in your player, or a wrong time zone. Refresh the playlist and the guide, then check your player’s EPG settings.'),
        ('Why are the guide times wrong?', 'The guide and your device must use the same time zone. Australia has several (AEST/AEDT, ACST/ACDT and AWST) and daylight saving changes the offset for some states.'),
        ('What is XMLTV?', 'XMLTV is a common file format for TV guide data. Many IPTV players can load an XMLTV link to fill the guide.')]
b3 = ('<p>The programme guide, or EPG, turns a long list of channels into a TV guide you can browse. When it works you barely notice it. When it is empty or out by an hour it is one of the most common IPTV complaints, and it is usually easy to fix.</p>'
      '<h2>How the guide gets into your player</h2><p>Your IPTV player loads two things: the channel list and the guide data. Some services include the guide automatically with an Xtream Codes login. Others give you a separate XMLTV link to paste into your player’s EPG settings.</p>'
      '<h2>Fix an empty or missing guide</h2>'
      + steps([('Refresh the playlist and guide', 'In your player, find the refresh or update option for the playlist and EPG, then wait a few minutes for it to finish.'),
               ('Check the EPG source', 'Make sure an EPG or XMLTV link is set if your service gives you one. Paste it exactly with no spaces.'),
               ('Match channels to the guide', 'Some players let you map a channel to its guide listing. Do this for channels that still show no information.'),
               ('Restart the app', 'Close the player fully and reopen it. On a TV box, restart the box.')])
      + '<h2>Fix guide times that are wrong</h2>'
      + table(['Where you are', 'Time zone'], [['NSW, VIC, ACT, TAS, QLD', 'AEST (AEDT in summer, except QLD)'], ['SA and NT', 'ACST (ACDT in summer for SA)'], ['WA', 'AWST (no daylight saving)']])
      + '<p>Set the time zone in your device and in the player’s settings. Many players also have a manual EPG time shift option to adjust the guide by one or more hours.</p>'
      '<p>If you are choosing an app, our <a href="../../iptv-player-australia/index.html">IPTV player guide</a> compares how each one handles the guide.</p>')
guide_page('guides/iptv-epg-guide-explained-australia/', 2, 'Guides', 'guides/index.html',
           'IPTV EPG Guide Explained: Fix an Empty or Wrong TV Guide', 'IPTV EPG Explained: Fix an Empty or Wrong TV Guide',
           'What is an IPTV EPG, why is the TV guide empty or out by an hour, and how to fix it. Covers XMLTV, Australian time zones and player settings.',
           'The EPG is your IPTV TV guide. Here is how it works and how to fix it when it is empty, missing channels or showing the wrong times.', b3, faq3,
           [('../../iptv-player-australia/index.html', 'IPTV player guide'), ('../best-dns-for-iptv-australia/index.html', 'Best DNS for IPTV'), ('../m3u-playlist-url-xtream-codes-api-australia/index.html', 'M3U and Xtream Codes'), ('../../iptv-free-trial-australia/index.html', 'Free trial')])
S.add_to_sitemap('guides/iptv-epg-guide-explained-australia/', '0.7')

# ================================================================= 4. bandwidth calculator (tool)
faq4 = [('How accurate is the calculator?', 'It gives a planning estimate using typical speeds per stream (SD 3, HD 5, Full HD 8, 4K 25 Mbps) plus the headroom you choose. Real streams vary, so treat it as a guide.'),
        ('Why does it add headroom?', 'Other devices in your home also use the internet, and a stream needs spare capacity to stay smooth at peak times.'),
        ('Which NBN plan should I pick?', 'Choose the plan whose typical evening speed is above the number the calculator shows. Check the typical evening speed your provider publishes.')]
tool_body = '''
<section style="padding:1rem 0 4rem; background:var(--bg-main);"><div class="container"><div class="prose-block" style="max-width:900px;">
<div class="glass-card bw-card" id="bwTool">
  <h2 class="section-title" style="font-size:1.4rem; margin-top:0;">How many screens will stream at once?</h2>
  <div class="bw-grid">
    <label>SD streams <small>about 3 Mbps each</small><input type="number" min="0" max="20" value="0" data-q="3" inputmode="numeric"></label>
    <label>HD streams <small>about 5 Mbps each</small><input type="number" min="0" max="20" value="1" data-q="5" inputmode="numeric"></label>
    <label>Full HD streams <small>about 8 Mbps each</small><input type="number" min="0" max="20" value="1" data-q="8" inputmode="numeric"></label>
    <label>4K streams <small>about 25 Mbps each</small><input type="number" min="0" max="20" value="0" data-q="25" inputmode="numeric"></label>
  </div>
  <label class="bw-head">Spare capacity for other devices
    <select id="bwHead"><option value="1.1">Light home use (+10%%)</option><option value="1.25" selected>Normal home use (+25%%)</option><option value="1.5">Busy household (+50%%)</option></select></label>
  <div class="bw-result" aria-live="polite">
    <div><span>You need about</span><strong id="bwMbps">0</strong><em>Mbps</em></div>
    <div><span>Suggested NBN plan</span><strong id="bwPlan">NBN 25</strong><em id="bwNote"></em></div>
  </div>
</div>
<h2>How it works</h2>
<p>Add the streams you expect at the same time, choose how much spare capacity your household needs and the calculator adds it up. It then picks the smallest common NBN plan that covers the total. Always check your provider\’s typical evening speed, because that is what you get when you are actually watching.</p>
<h2>Frequently asked questions</h2>%s
%s
</div></div></section>
<script>
(function(){
  var tool=document.getElementById('bwTool'); if(!tool) return;
  var inputs=tool.querySelectorAll('input[data-q]'), head=document.getElementById('bwHead');
  var plans=[[25,'NBN 25'],[50,'NBN 50'],[100,'NBN 100'],[250,'NBN 250'],[1000,'NBN 1000']];
  function calc(){
    var total=0; inputs.forEach(function(i){var n=Math.max(0,Math.min(20,parseInt(i.value,10)||0)); total+=n*parseFloat(i.dataset.q);});
    var need=Math.ceil(total*parseFloat(head.value));
    document.getElementById('bwMbps').textContent=need;
    var plan=plans.find(function(p){return p[0]>=need;})||plans[plans.length-1];
    document.getElementById('bwPlan').textContent=need===0?'-':plan[1];
    document.getElementById('bwNote').textContent=need===0?'Add at least one stream':(need>1000?'Consider a wired multi-gig setup':'Pick a plan with a typical evening speed above '+need+' Mbps');
  }
  inputs.forEach(function(i){i.addEventListener('input',calc);}); head.addEventListener('change',calc); calc();
})();
</script>
''' % (faq(faq4), share(S.SITE + '/tools/iptv-bandwidth-calculator/', 'IPTV bandwidth calculator for Australia'))
tool_path = 'tools/iptv-bandwidth-calculator/'
tool_url = S.SITE + '/' + tool_path
tool_ld = [S.breadcrumb_ld([('Home', S.SITE + '/'), ('Tools', S.SITE + '/tools/'), ('IPTV Bandwidth Calculator', tool_url)]),
           {"@context": "https://schema.org", "@type": "WebApplication", "name": "IPTV Bandwidth Calculator", "url": tool_url, "applicationCategory": "UtilitiesApplication",
            "operatingSystem": "Any", "browserRequirements": "Requires JavaScript", "inLanguage": "en-AU", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "AUD"}},
           faq_ld(faq4)]
tool_html = S.assemble(2, S.head('IPTV Bandwidth Calculator: How Many Mbps and Which NBN Plan?', 'Free IPTV bandwidth calculator. Add your SD, HD, Full HD and 4K streams to see how many Mbps you need and which NBN plan to choose in Australia.', tool_path, 2, tool_ld),
                       S.crumbs([('Tools', 'tools/index.html'), ('IPTV Bandwidth Calculator', None)], 2),
                       '<main>' + S.page_hero('Free Tool', 'IPTV Bandwidth Calculator: How Many Mbps Do You Need?', 'Add up the streams in your home and see the internet speed you need and the NBN plan that fits.') + tool_body
                       + S.cta_band('Know your speed? Now test IPTV on it', 'Request a free 24-hour trial and watch live sport on your own connection.', 'Hi, I used your bandwidth calculator and want a free trial')
                       + related([('../../guides/how-much-internet-speed-for-iptv-australia/index.html', 'Internet speed guide'), ('../../guides/best-dns-for-iptv-australia/index.html', 'Best DNS for IPTV'), ('../../guides/how-to-fix-iptv-buffering-australia/index.html', 'Fix buffering')]) + '</main>')
S.write(tool_path.rstrip('/'), tool_html)
S.add_to_sitemap(tool_path, '0.8')

# tools hub
hub_ld = [S.breadcrumb_ld([('Home', S.SITE + '/'), ('Tools', S.SITE + '/tools/')]),
          {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Free IPTV Tools", "url": S.SITE + '/tools/', "inLanguage": "en-AU"}]
hub_body = ('<main>' + S.page_hero('Free Tools', 'Free IPTV Tools for Australians', 'Simple tools that take the guesswork out of setting up IPTV at home.')
            + '<section style="padding:1rem 0 4rem; background:var(--bg-main);"><div class="container"><div class="hub-grid" style="margin-top:1rem;">'
              '<a class="hub-card" href="iptv-bandwidth-calculator/index.html"><i class="fa-solid fa-gauge-high"></i><h3>IPTV Bandwidth Calculator</h3><p>Add up your streams to see the Mbps you need and which NBN plan fits.</p><span>Open tool <i class="fa-solid fa-arrow-right"></i></span></a>'
              '</div></div></section></main>')
S.write('tools', S.assemble(1, S.head('Free IPTV Tools: Bandwidth Calculator and More', 'Free tools for Australians setting up IPTV, starting with an IPTV bandwidth calculator that shows the Mbps and NBN plan you need.', 'tools/', 1, hub_ld), S.crumbs([('Tools', None)], 1), hub_body))
S.add_to_sitemap('tools/', '0.6')
print('content built')
print('DONE')

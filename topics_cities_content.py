"""Topics + cities content pass.
Topics: keep 19 genuinely useful pages (unique copy), noindex the rest. Cities: richer, distinct content on 4 local page types per key city,
noindex the two low-value types (reseller-panel, firestick-setup)."""
import glob, html as H, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://4kaustraliaiptv.com'
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)
def ul(xs): return '<ul class="check-ok">' + ''.join('<li>%s</li>' % x for x in xs) + '</ul>'
def steps(xs): return '<ol class="steps-list">' + ''.join('<li><span class="step-number">%d</span><div><h4>%s</h4><p>%s</p></div></li>' % (i + 1, a, b) for i, (a, b) in enumerate(xs)) + '</ol>'
def table(head, rows): return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (''.join('<th>%s</th>' % h for h in head), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows))
def sec(h, *parts): return '<h2>%s</h2>' % h + ''.join(p if p.startswith('<') else '<p>%s</p>' % p for p in parts)
HERO_P = re.compile(r'(<p class="hero-description"[^>]*>)(.*?)(</p>)', re.S)
def block(body): return '<section class="content-pass" style="padding:3.5rem 0; background:var(--bg-main);"><div class="container"><article class="prose-block legal">%s</article></div></section>' % body
def inject(s, body):
    k = s.find('hero-section'); e = s.find('</section>', k)
    return s[:e + 10] + '\n  ' + block(body) + s[e + 10:]
def set_meta(s, title=None, h1=None, desc=None, opening=None):
    if title:
        s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % H.escape(title, quote=False), s, 1, flags=re.S)
        s = re.sub(r'(property="og:title" content=")[^"]*(")', lambda m: m.group(1) + H.escape(title) + m.group(2), s, 1)
    if desc:
        s = re.sub(r'(name="description" content=")[^"]*(")', lambda m: m.group(1) + H.escape(desc) + m.group(2), s, 1)
        s = re.sub(r'(property="og:description" content=")[^"]*(")', lambda m: m.group(1) + H.escape(desc) + m.group(2), s, 1)
    if h1: s = re.sub(r'(<h1[^>]*>)(.*?)(</h1>)', lambda m: m.group(1) + H.escape(h1, quote=False) + m.group(3), s, 1, flags=re.S)
    if opening: s = HERO_P.sub(lambda m: m.group(1) + opening + m.group(3), s, 1)
    return s
def noindex(s):
    if 'noindex' in s: return s, False
    s = re.sub(r'\s*<meta name="robots"[^>]*>', '', s)
    return s.replace('</head>', '  <meta name="robots" content="noindex, follow" />\n</head>', 1), True
LINKS = '<p>Next steps: <a href="../../iptv-free-trial-australia/index.html">start a free 24-hour trial</a>, compare apps in the <a href="../../iptv-player-australia/index.html">IPTV player guide</a>, or read the <a href="../../best-iptv-australia/index.html">best IPTV Australia guide</a>.</p>'

# ================================================================ TOPICS (19 kept)
T = {
 'iptv': ('What Is IPTV? How It Works in Australia', 'What Is IPTV and How Does It Work?', 'IPTV delivers TV over the internet instead of an aerial. Learn how IPTV works in Australia, what you need to watch it and how it differs from streaming apps.',
  'IPTV, short for Internet Protocol Television, delivers TV channels over your internet connection instead of an aerial or satellite dish. You watch it in a player app on a smart TV, streaming box, phone or computer.',
  sec('How IPTV works', ul(['A service sends channels and on-demand video as internet streams.', 'You add a login or playlist link to an IPTV player app.', 'The app shows a channel list and programme guide (EPG).', 'Your home internet carries the stream, so connection quality matters.'])) +
  sec('What you need', ul(['An internet connection (about 8 Mbps per Full HD stream and 25 Mbps for 4K).', 'A device that can run a player: Fire TV Stick, Android TV box, Apple TV, Samsung or LG TV, phone or PC.', 'A service with the channels you want and the rights to show them.'])) +
  sec('IPTV compared with streaming apps', 'Streaming apps such as Netflix keep everything inside one app. IPTV uses a separate player app, so one player can show many kinds of content, and you choose the player that suits your device. Always check that a service is licensed to supply what it sells.') + LINKS),
 'iptv-for-australia': ('IPTV for Australia: How to Choose and Set Up', 'IPTV for Australia: How to Choose and Set Up', 'How to choose IPTV in Australia: what to check before you subscribe, the speed you need, which devices work and how to test a service with a free trial.',
  'To use IPTV in Australia, you need a service with the channels you want, an IPTV player app on your device and an internet connection fast enough for your streams, about 25 Mbps for one 4K stream.',
  sec('Choosing a service', ul(['Check it carries the sport and channels you actually watch.', 'Look for clear pricing in AUD and a short free trial.', 'Make sure support replies on WhatsApp or email.', 'Confirm the service has the rights to its content.'])) +
  sec('Setting up in four steps', steps([('Pick a device', 'A Fire TV Stick, Android TV box or Apple TV is a good start.'), ('Install a player', 'TiviMate and IPTV Smarters Pro are popular.'), ('Add your login', 'Use Xtream Codes or an M3U link.'), ('Test at peak time', 'Watch a live match on a Friday or Saturday night.')])) + LINKS),
 'au-iptv': ('AU IPTV: Watching Australian TV and Sport Online', 'AU IPTV: Watching Australian TV and Sport Online', 'Australian IPTV explained: time zones and guide times, sport seasons, free-to-air channels and the internet speed you need on NBN.',
  'AU IPTV means watching Australian TV and sport through an IPTV service. The details that matter here are your time zone, the sport seasons you follow and a stable NBN connection.',
  sec('Australian time zones', table(['Region', 'Time zone'], [['NSW, VIC, ACT, TAS', 'AEST, AEDT in summer'], ['QLD', 'AEST all year'], ['SA, NT', 'ACST, ACDT in summer for SA'], ['WA', 'AWST']]) + '<p>Set the right time zone in your device and your player so the programme guide lines up. See the <a href="../../guides/iptv-epg-guide-explained-australia/index.html">EPG guide</a>.</p>') +
  sec('Sport seasons to plan around', table(['Competition', 'Typical season'], [['AFL', 'March to September'], ['NRL', 'March to October'], ['Cricket (BBL, Tests)', 'December to February, summer Tests'], ['A-League Men', 'October to May']])) +
  sec('Internet', 'Check your plan’s typical evening speed and use a cable for the main TV. The <a href="../../tools/iptv-bandwidth-calculator/index.html">bandwidth calculator</a> shows what you need.') + LINKS),
 'amazon-firestick': ('Amazon Fire TV Stick for IPTV: Which Model to Buy', 'Amazon Fire TV Stick for IPTV: Which Model?', 'Which Amazon Fire TV Stick is best for IPTV? Compare Fire TV Stick Lite, 4K and 4K Max and the Fire TV Cube for speed, Wi-Fi and storage.',
  'For IPTV, the Fire TV Stick 4K Max is the best Fire TV Stick because it is faster and has newer Wi-Fi. The cheaper Fire TV Stick Lite or standard stick also works for one TV on a strong connection.',
  sec('Fire TV models compared', table(['Model', 'Good for', 'Note'], [['Fire TV Stick Lite', 'Budget, one TV', 'Simpler remote'], ['Fire TV Stick 4K', 'Most homes', '4K and HDR support'], ['Fire TV Stick 4K Max', 'Best stick for IPTV', 'Faster, newer Wi-Fi'], ['Fire TV Cube', 'Heavy use, smart home', 'Most powerful']])) +
  sec('Tips', ul(['Use an Ethernet adapter if your Wi-Fi is weak.', 'Keep the stick updated from Settings.', 'Clear app cache if channels load slowly.'])) +
  '<p>Setup steps are in the <a href="../../devices/iptv-on-amazon-firestick-australia/index.html">Fire TV Stick IPTV guide</a>.</p>' + LINKS),
 'firestick-4k-max': ('Fire TV Stick 4K Max for IPTV: Setup and Tips', 'Fire TV Stick 4K Max for IPTV: Setup and Tips', 'Set up IPTV on the Fire TV Stick 4K Max: install a player, use Ethernet or 5 GHz Wi-Fi and tune the stick for a smooth live stream.',
  'The Fire TV Stick 4K Max runs IPTV well: install a player such as TiviMate or IPTV Smarters Pro, add your login and, for the steadiest stream, connect it with an Ethernet adapter or use 5 GHz Wi-Fi.',
  sec('Quick setup', steps([('Update', 'Install the latest Fire OS update.'), ('Install a player', 'Use the Amazon Appstore or Downloader.'), ('Add your login', 'Choose Xtream Codes or M3U.'), ('Pick Wi-Fi or Ethernet', 'An Ethernet adapter gives the most reliable live sport.')])) +
  sec('Make it run smoothly', ul(['Free storage by removing apps you do not use.', 'Turn off app auto-updates during live sport.', 'Restart the stick weekly.'])) +
  '<p>Full guide: <a href="../../devices/iptv-on-amazon-firestick-australia/index.html">IPTV on Fire TV Stick</a>.</p>' + LINKS),
 'android-tv-box': ('Android TV Box for IPTV: What to Look For', 'Android TV Box for IPTV: What to Look For', 'Choosing an Android TV box for IPTV in Australia: RAM, storage, Ethernet, 4K output and official Google certification, with a setup guide.',
  'An Android TV box for IPTV should have at least 2 GB of RAM, 16 GB of storage, 4K output and an Ethernet port. Choose a Google-certified box so apps and updates keep working.',
  sec('Buying checklist', ul(['Google Play certification, not a generic Android box.', '2 GB RAM or more and 16 GB storage.', 'HDMI 2.0 or newer for 4K.', 'Ethernet port or fast dual-band Wi-Fi.', 'Local warranty from an Australian retailer.'])) +
  sec('Popular choices', table(['Type', 'Example', 'Best for'], [['Premium', 'Nvidia Shield TV Pro', 'Best performance'], ['Value', 'Xiaomi Mi Box S', 'One TV, low cost'], ['IPTV-first', 'Formuler Z series', 'Simple IPTV experience']])) +
  '<p>See the <a href="../../iptv-box-australia/index.html">IPTV box buying guide</a> and the <a href="../../devices/iptv-on-android-tv-box-australia/index.html">Android TV box setup guide</a>.</p>' + LINKS),
 'tv-box': ('TV Box for IPTV: Android, Apple, Fire TV and More', 'TV Box for IPTV: Which Type Should You Buy?', 'Which TV box is best for IPTV? Compare Android TV boxes, Apple TV, Fire TV and Google TV for speed, apps and ease of use in Australia.',
  'The best TV box for IPTV depends on your TV and budget: an Android TV box offers the most IPTV apps, Apple TV is the smoothest, and a Fire TV Stick is the cheapest way to start.',
  sec('Compared', table(['Box', 'IPTV apps', 'Ease of use'], [['Android / Google TV box', 'Many', 'Good'], ['Apple TV 4K', 'Fewer', 'Very good'], ['Fire TV Stick', 'Many', 'Good'], ['Chromecast with Google TV', 'Many', 'Good']])) +
  sec('How to decide', ul(['Pick Apple TV if you already use Apple devices.', 'Pick Android TV or Shield for the most choice.', 'Pick a Fire TV Stick for the lowest cost.'])) + '<p>Read the <a href="../../iptv-box-australia/index.html">full IPTV box guide</a>.</p>' + LINKS),
 'apple-tv-4k': ('Apple TV 4K for IPTV: Is It a Good Choice?', 'Apple TV 4K for IPTV: Is It a Good Choice?', 'Is Apple TV 4K good for IPTV? Pros and cons, which IPTV apps work on tvOS and a quick setup guide for Australian viewers.',
  'Apple TV 4K is a smooth, reliable box for IPTV, but it has fewer IPTV apps than Android. Install an IPTV player from the App Store, add your login and use Ethernet for live sport.',
  sec('Pros and cons', table(['Pros', 'Cons'], [['Fast, smooth interface', 'Fewer IPTV apps than Android'], ['Excellent picture quality', 'Higher price'], ['Ethernet on the 4K model', 'No sideloading']])) +
  sec('Setup', steps([('Open the App Store', 'Search for an IPTV player.'), ('Add your playlist', 'Enter your M3U link or Xtream login.'), ('Add the guide', 'Use an XMLTV link if one is supplied.')])) +
  '<p>Full guide: <a href="../../devices/iptv-on-apple-tv-tvos-australia/index.html">IPTV on Apple TV</a>.</p>' + LINKS),
 'chromecast-with-google-tv': ('Chromecast with Google TV for IPTV: Pros and Cons', 'Chromecast with Google TV for IPTV', 'Is Chromecast with Google TV good for IPTV? Pros and cons, the apps to use and how to get a steadier stream with Ethernet.',
  'Chromecast with Google TV works well for IPTV because it runs Android apps. Install TiviMate or IPTV Smarters Pro from the Play Store and, for live sport, use the Ethernet adapter.',
  sec('Pros and cons', table(['Pros', 'Cons'], [['Runs Android IPTV apps', 'No Ethernet port on the dongle'], ['4K HDR support', 'Limited storage'], ['Small and affordable', 'Can slow down with many apps']])) +
  '<p>Use the Google TV home screen, not casting, to run IPTV apps. Setup steps: <a href="../../devices/chromecast-with-google-tv-iptv-australia/index.html">Chromecast guide</a>.</p>' + LINKS),
 'google-tv-streamer': ('Google TV Streamer for IPTV: What to Know', 'Google TV Streamer for IPTV', 'Google TV Streamer and IPTV: how it compares with Chromecast with Google TV, which apps work and how to set up a steady stream.',
  'The Google TV Streamer is Google’s newer streaming box and runs Android TV apps, so you can install an IPTV player from the Play Store. It has an Ethernet port for a steadier stream.',
  sec('Why use it for IPTV', ul(['Runs IPTV players such as TiviMate and IPTV Smarters Pro.', 'Ethernet port for stable live sport.', 'Supports 4K and HDR.'])) +
  sec('Setup', 'Install a player from the Play Store, add your login and load the guide. The steps match the <a href="../../devices/chromecast-with-google-tv-iptv-australia/index.html">Chromecast with Google TV guide</a>.') + LINKS),
 'streaming-devices': ('Streaming Devices for IPTV Compared', 'Streaming Devices for IPTV Compared', 'Compare streaming devices for IPTV in Australia: Fire TV Stick, Android TV box, Apple TV, Chromecast with Google TV and Nvidia Shield.',
  'The best streaming device for IPTV is the one that runs your player app smoothly: Nvidia Shield for performance, an Android TV box for value, Apple TV for simplicity and a Fire TV Stick for budget.',
  sec('Side by side', table(['Device', 'Strength', 'Watch out for'], [['Nvidia Shield TV Pro', 'Most powerful', 'Price'], ['Android TV box', 'Good value', 'Choose a certified box'], ['Apple TV 4K', 'Smooth and reliable', 'Fewer IPTV apps'], ['Fire TV Stick 4K Max', 'Cheap and capable', 'No built-in Ethernet'], ['Chromecast with Google TV', 'Compact', 'No Ethernet port']])) +
  '<p>Read the <a href="../../iptv-box-australia/index.html">IPTV box guide</a> for detail.</p>' + LINKS),
 'sports-streaming': ('Sports Streaming in Australia: Getting a Stable Stream', 'Sports Streaming in Australia: Getting a Stable Stream', 'How to get a stable sports stream in Australia: internet speed, wired connections, DNS and testing at peak time.',
  'To get a stable live sports stream in Australia, use a wired connection, make sure your plan has the speed for your quality setting and test during a real match, not just at off-peak times.',
  sec('A reliable setup', ul(['Wired Ethernet to the main TV.', 'Enough speed: about 8 Mbps for Full HD, 25 Mbps for 4K.', 'Try Cloudflare or Google DNS.', 'Pause large downloads during the game.'])) +
  '<p>Calculate what you need with the <a href="../../tools/iptv-bandwidth-calculator/index.html">bandwidth calculator</a> and read the <a href="../../guides/how-to-fix-iptv-buffering-australia/index.html">buffering guide</a>.</p>' + LINKS),
 'cricket-live-streaming': ('Cricket Live Streaming in Australia: Setup and Tips', 'Cricket Live Streaming in Australia', 'How to watch cricket live online in Australia: seasons, how to avoid buffering and the best setup for the Big Bash, Tests and Sheffield Shield.',
  'To watch cricket live online in Australia, use a service that is licensed for the competition, a wired or strong 5 GHz connection and a quick test before the first ball.',
  sec('Cricket calendar', table(['Competition', 'Typical time'], [['Big Bash League', 'December to February'], ['Summer Test series', 'December to January'], ['Sheffield Shield', 'October to March']])) +
  sec('Tips for long matches', ul(['Cricket runs for hours, so use a cable or a stable network.', 'Keep your device charged and updated.', 'Stream delay can be 30 seconds or more behind the ground, so avoid spoilers.'])) + LINKS),
 'f1-live-stream': ('F1 Live Stream in Australia: Race Weekend Setup', 'F1 Live Stream in Australia', 'How to set up an F1 live stream in Australia: race weekend schedule, time zones and a stable connection for Albert Park and overseas races.',
  'F1 races overseas often start at night or in the early morning in Australia, so check the local start time, set up your device the day before and test your connection for the stream.',
  sec('Race weekend format', ul(['Practice sessions on Friday.', 'Qualifying on Saturday.', 'The race on Sunday.', 'The Australian Grand Prix is held at Albert Park in Melbourne, usually in March.'])) +
  sec('Setup tips', ul(['Use a wired connection for 4K.', 'Check your guide times use the right time zone.', 'Restart your player before the race.'])) + LINKS),
 'afl-stream': ('AFL Live Stream: How to Get a Stable Stream', 'AFL Live Stream: How to Get a Stable Stream', 'How to set up an AFL live stream in Australia: season dates, match day tips, devices and avoiding buffering during finals.',
  'To stream AFL live without buffering, use a wired connection, check your plan has the speed for your quality setting and test your setup during a real match before the finals.',
  sec('AFL season at a glance', ul(['Home and away season from March to August.', 'Finals in September, ending with the Grand Final.', 'Matches run Thursday to Sunday.'])) +
  sec('Match day checklist', ul(['Restart your device an hour before the bounce.', 'Close other apps and downloads.', 'Open the guide to check the channel in advance.'])) + LINKS),
 'streaming-for-ufc': ('Streaming UFC in Australia: Time Zones and Setup', 'Streaming UFC in Australia', 'How to watch UFC events in Australia: why events start early in the morning, how to prepare your device and what to check about licensing.',
  'UFC events are usually held in the United States, so they often air on Sunday morning in Australia. Check the local start time, set your device up the night before and make sure your service is licensed for the event.',
  sec('Be ready', ul(['Check main card and prelim times in your time zone.', 'Test your stream the night before.', 'Use a wired connection for a stable pay-per-view stream.'])) + LINKS),
 'basketball-streaming-nba': ('Streaming NBA and NBL Basketball in Australia', 'Streaming NBA and NBL Basketball in Australia', 'How to watch NBA and NBL basketball online in Australia: seasons, time zones and a stable setup for game day.',
  'NBA games are played in North America, so many tip off in the Australian morning or afternoon. The Australian NBL runs from about October to March. Check the local time and test your stream.',
  sec('Seasons', table(['League', 'Typical season'], [['NBA', 'October to April, then playoffs'], ['NBL', 'October to March']])) +
  sec('Tips', ul(['Use the player guide to set reminders.', 'Prefer a wired connection for 4K.', 'Check that a service is licensed for the league.'])) + LINKS),
 'best-streaming-service-australia': ('How to Choose a Streaming Service in Australia', 'How to Choose a Streaming Service in Australia', 'How to choose the best streaming service in Australia: what you watch, cost over 12 months, devices and licensing.',
  'The best streaming service in Australia is the one that carries what you actually watch at a total cost you are happy with. Start by listing your shows and sport, then compare cost over 12 months.',
  sec('A simple method', steps([('List what you watch', 'Shows, sport and news you cannot miss.'), ('Count your devices', 'Check each service runs on your TV and phone.'), ('Compare 12-month cost', 'Add up cost for the year, not just a month.'), ('Test before you commit', 'Use free trials where offered.')])) + LINKS),
 'sport-streaming-services': ('Sport Streaming Services in Australia: How to Choose', 'Sport Streaming Services in Australia', 'How to choose a sport streaming service in Australia: match the service to your sport, check devices and compare licensed apps with IPTV.',
  'To choose a sport streaming service in Australia, start with the sport you follow, then check which service shows it, which devices it runs on and what it costs over a year.',
  sec('What to compare', ul(['Which competitions are included.', 'Device support and how many screens at once.', 'Price over 12 months.', 'Free trial availability.'])) + '<p>See the <a href="../../comparisons/index.html">comparisons hub</a> for licensed services side by side with IPTV.</p>' + LINKS),
}

# ================================================================ CITIES
CITY = {
 'sydney': ('Sydney', 'NSW', 'the Sydney Swans and GWS Giants (AFL), the Sydney Roosters, South Sydney Rabbitohs and Parramatta Eels (NRL) and Sydney FC (A-League)', 'the SCG and Sydney’s NRL grounds', 'State of Origin nights and Friday night football', ['AFL', 'NRL', 'A-League', 'Cricket (Sydney Test, BBL)', 'Rugby union']),
 'melbourne': ('Melbourne', 'VIC', 'Collingwood, Richmond, Carlton, Essendon and Hawthorn (AFL), Melbourne Storm (NRL) and Melbourne City and Victory (A-League)', 'the MCG', 'AFL finals, the Boxing Day Test, the Australian Open and the Spring Racing Carnival', ['AFL', 'Cricket (Boxing Day Test, BBL)', 'Tennis (Australian Open)', 'A-League', 'Formula 1 (Albert Park)']),
 'brisbane': ('Brisbane', 'QLD', 'the Brisbane Lions (AFL), the Brisbane Broncos (NRL) and Brisbane Roar (A-League)', 'the Gabba and Suncorp Stadium', 'State of Origin and summer cricket at the Gabba', ['NRL', 'AFL', 'Cricket (Gabba Test, BBL)', 'A-League', 'State of Origin']),
 'perth': ('Perth', 'WA', 'West Coast Eagles and Fremantle (AFL), the Perth Scorchers (Big Bash) and Perth Glory (A-League)', 'Optus Stadium', 'AFL games and summer cricket at Optus Stadium', ['AFL', 'Cricket (BBL, Tests)', 'A-League', 'Rugby union']),
 'adelaide': ('Adelaide', 'SA', 'Adelaide Crows and Port Adelaide (AFL), the Adelaide Strikers (Big Bash) and Adelaide United (A-League)', 'Adelaide Oval', 'Showdown matches and Test cricket at Adelaide Oval', ['AFL', 'Cricket (Adelaide Test, BBL)', 'A-League', 'Supercars']),
 'canberra': ('Canberra', 'ACT', 'the Canberra Raiders (NRL) and the ACT Brumbies (Super Rugby Pacific)', 'Manuka Oval and the Canberra Stadium', 'Raiders home games and Brumbies matches', ['NRL', 'Super Rugby Pacific', 'Cricket (Prime Minister’s XI)', 'AFL']),
 'hobart': ('Hobart', 'TAS', 'the Hobart Hurricanes (Big Bash), with AFL and NRL followed closely across Tasmania', 'Bellerive Oval', 'summer cricket and the Hobart International tennis', ['AFL', 'Cricket (BBL)', 'Tennis (Hobart International)', 'NRL']),
 'darwin': ('Darwin', 'NT', 'AFL, NRL and Supercars events followed across the Top End', 'Marrara Oval', 'AFL Top End fixtures and Supercars weekends', ['AFL', 'NRL', 'Supercars', 'Cricket']),
 'gold-coast': ('Gold Coast', 'QLD', 'the Gold Coast Suns (AFL) and the Gold Coast Titans (NRL)', 'Carrara Stadium', 'Suns and Titans home games', ['AFL', 'NRL', 'Cricket', 'Surf and Commonwealth sport events']),
 'newcastle': ('Newcastle', 'NSW', 'the Newcastle Knights (NRL) and the Newcastle Jets (A-League)', 'Newcastle’s home stadium', 'Knights home games and Jets match days', ['NRL', 'A-League', 'AFL', 'Cricket']),
}
SEASON = {'AFL': 'March to September', 'NRL': 'March to October', 'A-League': 'October to May', 'Super Rugby Pacific': 'February to June', 'Rugby union': 'varies by competition', 'State of Origin': 'May to July',
          'Cricket': 'summer, December to February', 'Supercars': 'March to November', 'Tennis': 'January (Australian Open)'}
def season_of(label):
    for k, v in SEASON.items():
        if label.startswith(k): return v
    return 'varies'
def pages(city, typ):
    return 'cities/%s/%s/index.html' % (city, typ)
GUIDE = '<p>More help: <a href="../../../guides/how-much-internet-speed-for-iptv-australia/index.html">how much internet speed you need</a>, <a href="../../../guides/best-dns-for-iptv-australia/index.html">the best DNS for IPTV</a> and <a href="../../../iptv-player-australia/index.html">IPTV player apps</a>.</p>'

def city_body(typ, c):
    name, st, teams, grounds, big, comps = CITY[c]
    if typ == 'best-iptv':
        o = 'The best IPTV in %s is one that stays stable on your home internet during live sport, works on your TV or box and lets you test it free first. Use the checklist below, then start a 24-hour trial.' % name
        b = (sec('What matters for IPTV in %s' % name, ul(['<strong>Your connection.</strong> NBN technology differs from street to street across %s (fibre, fixed wireless, satellite). Check your address on the NBN Co website and your provider’s typical evening speed.' % name,
                                                          '<strong>Local sport.</strong> Viewers here follow %s. Check the service carries your competitions.' % teams,
                                                          '<strong>Devices.</strong> Fire TV Stick, Android TV box, Apple TV, Samsung and LG TVs all work with the right player.',
                                                          '<strong>A free trial.</strong> Test it at peak time before you pay.',
                                                          '<strong>Support.</strong> Look for help on WhatsApp or email.'])) +
             sec('Try it on a %s match day' % name, 'Test your trial during %s. That shows how the stream behaves when many households are online.' % big) + GUIDE)
    elif typ == 'subscription':
        o = 'To buy an IPTV subscription in %s, choose a 3, 6 or 12-month plan, pick 1 to 4 accounts and order on WhatsApp. Start with the free 24-hour trial if you want to test it first.' % name
        b = (sec('IPTV subscription plans in %s' % name, table(['Plan', '1 account', 'Per month'], [['3 months', '$39.99', '$13.33'], ['6 months', '$56.99', '$9.50'], ['12 months', '$79.99', '$6.67']]) + '<p>Prices in AUD. Plans with 2, 3 and 4 accounts are on the <a href="../../../index.html#pricing">pricing section</a>.</p>') +
             sec('How to order from %s' % name, steps([('Pick your plan', 'Choose the length and the number of accounts.'), ('Message us', 'Tap Order on WhatsApp and send your device type.'), ('Add the login to a player', 'Use TiviMate, IPTV Smarters Pro or IBO Player.')])) +
             sec('A tip for %s homes' % name, 'If several people in your household watch at once, choose more accounts and check your internet plan has the speed. The <a href="../../../tools/iptv-bandwidth-calculator/index.html">bandwidth calculator</a> shows what you need.') + GUIDE)
    elif typ == 'free-trial':
        o = 'To get an IPTV free trial in %s, request the 24-hour trial, add the login to a player app and test live sport and your home internet. No credit card is needed.' % name
        b = (sec('Your %s trial checklist' % name, ul(['Watch a live match at peak time, for example %s.' % big, 'Change channels quickly and check how fast they load.', 'Open the programme guide and confirm the times match %s time.' % name, 'Compare Wi-Fi and a cable on the same stream.'])) +
             sec('How to start', steps([('Request the trial', 'Use the Start Free 24H Trial button or message us on WhatsApp.'), ('Install a player', 'See the <a href="../../../iptv-player-australia/index.html">player guide</a>.'), ('Add your login and test', 'Try the checklist above.')])) +
             sec('If it buffers in %s' % name, 'Try a wired connection, restart your router and change DNS. Our <a href="../../../guides/how-to-fix-iptv-buffering-australia/index.html">buffering guide</a> walks through every step.'))
    elif typ == 'sports-channels':
        o = 'To watch sport in %s on IPTV, check that the service carries your competitions (%s) and test it during a live match with the free trial.' % (name, ', '.join(comps[:3]))
        rows = [[k, season_of(k)] for k in comps]
        b = (sec('%s sport calendar' % name, table(['Competition', 'Typical season'], rows)) +
             sec('Local teams and grounds', 'Viewers in %s follow %s, with big days at %s. Match times differ by competition, so set up your guide in the right time zone.' % (name, teams, grounds)) +
             sec('Get a steady live stream', ul(['Use a wired connection for the main TV.', 'Restart your player before kick-off.', 'Check that your plan has the speed for your quality setting.'])) + GUIDE)
    return o, b

stats = dict(topics_kept=0, topics_noindex=0, cities_content=0, cities_noindex=0, hubs=0)
gone = set()
# ---- topics
for f in glob.glob('topic/*/index.html'):
    slug = f.replace(os.sep, '/').split('/')[1]
    s = rd(f)
    if slug in T:
        if 'content-pass' in s: continue
        title, h1, desc, opening, body = T[slug]
        s = set_meta(s, title, h1, desc, opening)
        s = inject(s, body)
        wr(f, s); stats['topics_kept'] += 1
    else:
        s2, ch = noindex(s)
        if ch: wr(f, s2); stats['topics_noindex'] += 1; gone.add('%s/topic/%s/' % (SITE, slug))
# ---- cities
for c in CITY:
    for typ in ('best-iptv', 'subscription', 'free-trial', 'sports-channels'):
        f = pages(c, typ)
        if not os.path.exists(f): continue
        s = rd(f)
        if 'content-pass' in s: continue
        o, b = city_body(typ, c)
        s = set_meta(s, opening=o)
        s = inject(s, b)
        wr(f, s); stats['cities_content'] += 1
    for typ in ('reseller-panel', 'firestick-setup'):
        f = pages(c, typ)
        if os.path.exists(f):
            s = rd(f); s2, ch = noindex(s)
            if ch: wr(f, s2); stats['cities_noindex'] += 1; gone.add('%s/cities/%s/%s/' % (SITE, c, typ))
# ---- sitemaps
for sm in glob.glob('sitemap-*.xml'):
    x = rd(sm)
    y = re.sub(r'\s*<url>\s*<loc>(.*?)</loc>.*?</url>', lambda m: '' if m.group(1) in gone else m.group(0), x, flags=re.S)
    if y != x: wr(sm, y)
# ---- directory topics card: only the pages that stay indexable
d = rd('directory/index.html')
m = re.search(r'<div class="glass-card" id="topics".*?</div>\s*</div>', d, re.S)
if m:
    items = ''.join('<a href="../topic/%s/index.html" class="nav-link" style="padding:0.4rem 0.6rem; font-size:0.88rem;"><i class="fa-solid fa-arrow-right" style="font-size:0.7rem; color:var(--primary);"></i> %s</a>' % (k, v[1]) for k, v in sorted(T.items()))
    new = ('<div class="glass-card" id="topics" style="margin-bottom:2.5rem;"><h2 style="font-size:1.6rem; margin-bottom:1.25rem;"><i class="fa-solid fa-hashtag" style="color:var(--primary); margin-right:0.5rem;"></i> Popular Topics</h2>'
           '<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:0.75rem;">%s</div></div>') % items
    d = d[:m.start()] + new + d[m.end():]
    wr('directory/index.html', d)
print(stats)
print('DONE')

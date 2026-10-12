"""Content pass: gives device, comparison, ISP and language pages a direct-answer opening and a unique, accurate how-to section."""
import html as H, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def ul(xs): return '<ul class="check-ok">' + ''.join('<li>%s</li>' % x for x in xs) + '</ul>'
def steps(xs): return '<ol class="steps-list">' + ''.join('<li><span class="step-number">%d</span><div><h4>%s</h4><p>%s</p></div></li>' % (i + 1, a, b) for i, (a, b) in enumerate(xs)) + '</ol>'
def faqs(xs): return ''.join('<h3>%s</h3><p>%s</p>' % x for x in xs)

# ============================================================ DEVICES
D = {
 'iptv-on-amazon-firestick-australia': dict(
  open='To watch IPTV on a Fire TV Stick, install an IPTV player app such as IPTV Smarters Pro or TiviMate, enter the login details from your service, and wait for the channels and guide to load. The whole setup takes about 10 minutes.',
  need=['A Fire TV Stick (Lite, HD, 4K or 4K Max) or Fire TV Cube', 'A Wi-Fi connection, or an Ethernet adapter for the most stable stream', 'Your IPTV login: server URL, username and password, or an M3U link'],
  steps=[('Find an IPTV player', 'Search for a player in the Amazon Appstore. If your preferred app is not listed, install the Downloader app and sideload it from the developer website.'),
         ('Allow installs if you sideload', 'In Settings, open My Fire TV, Developer options, and allow Downloader to install unknown apps.'),
         ('Sign in', 'Open the player and choose Xtream Codes login or M3U URL, then paste the details exactly, with no spaces.'),
         ('Load the guide', 'Wait for the channel list and programme guide to finish loading before you start watching.'),
         ('Add favourites', 'Mark the channels you watch most so they appear first.')],
  tips=['Use an Ethernet adapter on a Fire TV Stick 4K Max or Cube if your Wi-Fi is weak.', 'Clear the player cache from Settings, Applications if channels load slowly.', 'Restart the stick once a week to keep menus quick.'],
  prob=[('The app will not install', 'Check that unknown apps are allowed for Downloader and that the stick has free storage.'), ('Channels buffer', 'Try a wired connection, then see the buffering guide.'), ('The guide is empty', 'Refresh the playlist and check the player EPG settings.')]),
 'iptv-on-android-tv-box-australia': dict(
  open='To use IPTV on an Android TV box, install an IPTV player from the Google Play Store, add your login details and load the playlist. Boxes with 2 GB RAM or more and an Ethernet port give the smoothest picture.',
  need=['An Android TV or Google TV box (for example Xiaomi Mi Box S or Nvidia Shield)', 'A Google account to use the Play Store', 'Your IPTV login details'],
  steps=[('Open the Play Store', 'Search for TiviMate or IPTV Smarters Pro and install it.'), ('Open the app and add a playlist', 'Choose Xtream Codes or M3U and enter your details.'), ('Wait for the first load', 'The first import of channels and guide can take a few minutes.'), ('Set a default player for streams', 'Leave it on the built-in player unless a channel will not play.'), ('Save your favourites', 'Group channels into favourites for faster browsing.')],
  tips=['Use Ethernet where you can.', 'Keep the box software updated from Settings.', 'Avoid very cheap unbranded boxes that never receive updates.'],
  prob=[('The Play Store app is missing', 'Make sure the box is certified and signed in to Google.'), ('Menus are slow', 'Clear storage in Settings, Apps and remove apps you do not use.'), ('Streams stutter on Wi-Fi', 'Move to 5 GHz or connect a cable.')]),
 'iptv-on-apple-tv-tvos-australia': dict(
  open='On an Apple TV 4K, install an IPTV player from the App Store, such as iPlayTV or IPTVX, then add your M3U or Xtream login. Apple TV is smooth and reliable, though it has fewer IPTV apps than Android.',
  need=['An Apple TV HD or Apple TV 4K running a recent tvOS', 'An Apple ID signed in to the App Store', 'Your IPTV login details'],
  steps=[('Open the App Store', 'Search for an IPTV player that supports tvOS.'), ('Install and open it', 'Choose the option to add a playlist.'), ('Enter your details', 'Type the M3U link or Xtream details. Pairing from your iPhone can save typing.'), ('Add the guide', 'If your service provides an XMLTV link, add it in the app settings.'), ('Check the picture settings', 'Turn on match frame rate and dynamic range in Apple TV settings for sport.')],
  tips=['Use Ethernet on Apple TV 4K for the steadiest stream.', 'Use the Remote app on iPhone to type long URLs.', 'Restart the device if the app stops loading.'],
  prob=[('The app cannot find my playlist', 'Check the link for typos and make sure it starts with https.'), ('Sound is out of sync', 'Use Settings, Video and Audio, Wireless Audio Sync.'), ('Channels do not load', 'Refresh the playlist inside the app.')]),
 'iptv-on-samsung-smart-tv-tizen-australia': dict(
  open='On a Samsung smart TV, install an IPTV player such as IBO Player or Smart IPTV from the Samsung app store, then add your playlist. You cannot sideload apps on most Samsung TVs, so choose a player available in Smart Hub.',
  need=['A Samsung smart TV running Tizen (most models from 2016 onwards)', 'An internet connection on the TV', 'Your IPTV login or playlist link'],
  steps=[('Open Smart Hub', 'Go to Apps and search for an IPTV player.'), ('Install and open the player', 'Note the device ID and key or code it shows.'), ('Add your playlist', 'Use the player website or the on-screen option to upload your M3U link or Xtream login.'), ('Restart the app', 'Close and reopen it so the playlist loads.'), ('Set your favourites', 'Group your channels for quick access.')],
  tips=['A wired connection helps if the TV Wi-Fi is weak.', 'Keep the TV software up to date.', 'If the app is missing, check that the TV region is set to Australia.'],
  prob=[('The playlist will not load', 'Check the activation details and the playlist link.'), ('The app crashes', 'Update the TV and reinstall the app.'), ('Pictures look soft', 'Check that the channel is HD or 4K and your connection is fast enough.')]),
 'iptv-on-lg-smart-tv-webos-australia': dict(
  open='On an LG smart TV, install an IPTV player such as IBO Player or Smart IPTV from the LG Content Store, then add your playlist using the player website or your login. LG webOS does not allow sideloading, so use an app listed in the store.',
  need=['An LG TV running webOS', 'An internet connection on the TV', 'Your IPTV login or playlist link'],
  steps=[('Open the LG Content Store', 'Search for an IPTV player and install it.'), ('Open the player', 'Note any device ID or activation code shown on screen.'), ('Add your playlist', 'Upload the M3U link or Xtream login through the player website.'), ('Reload the app', 'Restart the app to load channels and the guide.'), ('Pin the app', 'Move it to the first row of the home screen.')],
  tips=['Turn on the Game or Filmmaker picture mode only if you want less processing.', 'Use Ethernet if your Wi-Fi is weak.', 'Update webOS from Settings, General.'],
  prob=[('App not in the store', 'Check the TV region and webOS version.'), ('Channels freeze', 'Try another channel, then restart the TV.'), ('Guide shows wrong times', 'Set the correct time zone in the TV and the app.')]),
 'tivimate-iptv-player-australia-setup': dict(
  open='TiviMate is an IPTV player for Android TV, Google TV and Fire TV. To set it up, install the app, choose Add playlist, enter your Xtream Codes or M3U details and wait for the guide to load.',
  need=['An Android TV, Google TV or Fire TV device', 'The TiviMate app', 'Your IPTV login details'],
  steps=[('Install TiviMate', 'Use the Google Play Store or Amazon Appstore, or sideload where needed.'), ('Add a playlist', 'Select Xtream Codes, M3U or Stalker, then enter your details.'), ('Import the guide', 'Choose the EPG source your service provides, or use the Xtream guide.'), ('Tidy your channels', 'Hide unused groups and add favourites.'), ('Consider Premium', 'Premium adds features such as multiple playlists and recording.')],
  tips=['Set the programme guide update time to overnight.', 'Use the multi-view feature on a 4K box for sport.', 'Back up your settings in the app.'],
  prob=[('Guide missing', 'Refresh the EPG and check the time zone.'), ('Playlist will not add', 'Check the server URL for typing errors.'), ('Playback stutters', 'Try the external player option or a wired connection.')]),
 'iptv-smarters-pro-australia-guide': dict(
  open='IPTV Smarters Pro is a free IPTV player for Android, iPhone, iPad, Fire TV, Windows and Mac. To use it, open the app, choose Login with Xtream Codes API, then enter your username, password and server URL.',
  need=['A device that can run IPTV Smarters Pro', 'Your username, password and server URL', 'A stable internet connection'],
  steps=[('Install the app', 'Download it from your device app store, or from the official website for Windows and Mac.'), ('Choose Xtream Codes', 'Select Login with Xtream Codes API.'), ('Enter your details', 'Give the connection a name, then add username, password and URL.'), ('Wait for the import', 'Channels, movies and series load into separate sections.'), ('Open Live TV', 'Pick a category and start watching.')],
  tips=['Use the built-in player first.', 'Set parental controls from the settings menu.', 'Restart the app after changing the playlist.'],
  prob=[('Login fails', 'Check the URL has no trailing spaces and begins with http or https.'), ('No guide', 'Refresh EPG in the app settings.'), ('Black screen', 'Switch to another player in settings.')]),
 'ibo-player-australia-activation': dict(
  open='IBO Player is an IPTV player for smart TVs. After installing it, the app shows a device ID and key; you use those on the player website to link your playlist, then restart the app to see your channels.',
  need=['A smart TV or Android device with IBO Player', 'The device ID and key shown in the app', 'Your playlist link or Xtream details'],
  steps=[('Install IBO Player', 'Find it in your TV app store.'), ('Note the device ID and key', 'They appear on the first screen.'), ('Open the player website', 'Enter the device ID and key to sign in.'), ('Add your playlist', 'Paste your M3U link or Xtream login and save.'), ('Restart the app', 'Close and reopen the app on the TV.')],
  tips=['Take a photo of the device ID.', 'Keep one playlist per device while you test.', 'Make sure the TV clock and region are correct.'],
  prob=[('Playlist does not appear', 'Restart the app and check the key.'), ('Activation page rejects the code', 'Retype the ID and key carefully.'), ('Channels load slowly', 'Reduce the playlist size or use a wired connection.')]),
 'nvidia-shield-pro-4k-iptv-australia': dict(
  open='The Nvidia Shield TV Pro is the most powerful Android TV box for IPTV. Install TiviMate or IPTV Smarters Pro from the Google Play Store, add your login and use the Ethernet port for the most stable stream.',
  need=['An Nvidia Shield TV or Shield TV Pro', 'A Google account', 'Your IPTV login details'],
  steps=[('Connect and update', 'Plug in HDMI, power and Ethernet, then install updates.'), ('Install a player', 'Use the Play Store to install TiviMate or IPTV Smarters Pro.'), ('Add your login', 'Enter Xtream Codes or M3U details.'), ('Turn on upscaling', 'Use the Shield AI upscaling setting for HD channels on a 4K TV.'), ('Set up favourites', 'Save the channels you use most.')],
  tips=['The Shield handles large playlists well.', 'Turn on automatic frame rate matching for sport.', 'Keep it ventilated.'],
  prob=[('Remote is not responding', 'Replace batteries and re-pair the remote.'), ('App crashes', 'Clear its cache and reinstall.'), ('HDR looks off', 'Check HDMI mode in Shield display settings.')]),
 'chromecast-with-google-tv-iptv-australia': dict(
  open='Chromecast with Google TV runs Android apps, so you install an IPTV player such as TiviMate or IPTV Smarters Pro from the Play Store and add your login. For the steadiest stream, use the Ethernet adapter for Chromecast with Google TV.',
  need=['A Chromecast with Google TV (4K or HD)', 'A Google account', 'Your IPTV login details'],
  steps=[('Open the Apps tab', 'Search for an IPTV player and install it.'), ('Add your playlist', 'Enter your Xtream or M3U details.'), ('Load the guide', 'Wait for the EPG to finish importing.'), ('Choose favourites', 'Save them for fast access.'), ('Check Wi-Fi', 'Use the 5 GHz band or an Ethernet adapter.')],
  tips=['Free up storage by removing unused apps.', 'Restart the dongle from Settings, System, Restart.', 'Do not use the regular Chromecast casting mode for IPTV; use an app.'],
  prob=[('Remote voice is slow', 'Check your Wi-Fi.'), ('Streams buffer', 'Try a wired adapter.'), ('Apps are missing', 'Check the Google TV region.')]),
 'formuler-z-mol3-iptv-australia': dict(
  open='Formuler Z boxes are Android-based IPTV boxes that use the MyTVOnline 3 app. To set up, open MyTVOnline, add a portal using your Xtream, M3U or Stalker details and let it load your channels.',
  need=['A Formuler Z box (for example Z11 Pro Max)', 'The MyTVOnline 3 app (built in)', 'Your portal, M3U or Xtream details'],
  steps=[('Open MyTVOnline', 'Start the app from the home screen.'), ('Add a portal', 'Choose Xtream, M3U or Stalker and enter the details.'), ('Name the portal', 'Give it a short name to find later.'), ('Wait for channels', 'Let it import the list and guide.'), ('Customise the layout', 'Set favourites and hide unused groups.')],
  tips=['Use Ethernet for best results.', 'Keep the box updated.', 'Back up the portal list.'],
  prob=[('Portal will not add', 'Check the URL and credentials.'), ('Guide not showing', 'Refresh the portal and check time settings.'), ('Remote not pairing', 'Re-pair it in settings.')]),
 'mag-box-stalker-portal-australia': dict(
  open='MAG boxes use a portal URL rather than a username and password. Enter the portal address in the box settings under Servers, then give your provider the MAC address printed on the back so your account can be linked.',
  need=['A MAG box (for example MAG 524 or 540)', 'The portal URL from your IPTV service', 'The MAC address on the back of the box'],
  steps=[('Connect the box', 'Plug in HDMI, network and power.'), ('Open Settings', 'Choose Servers, then Portals.'), ('Enter the portal URL', 'Type the address exactly as given.'), ('Share the MAC address', 'Your service links the account to that MAC.'), ('Restart the box', 'It will load your channel list.')],
  tips=['Write the MAC address down before you mount the box.', 'Use a cable for the network connection.', 'Reset the portal if you change service.'],
  prob=[('The portal does not load', 'Check the URL and that the MAC is registered.'), ('Channels missing', 'Restart the box and reload the portal.'), ('Remote not working', 'Replace batteries or re-pair.')]),
 'kodi-iptv-simple-client-australia': dict(
  open='Kodi can play IPTV through the PVR IPTV Simple Client add-on. Install the add-on, enter your M3U link and optional XMLTV guide link in its settings, then enable it to see Live TV in the main menu.',
  need=['Kodi installed on your device', 'The PVR IPTV Simple Client add-on', 'Your M3U link and an XMLTV link if you have one'],
  steps=[('Install the add-on', 'Go to Add-ons, Install from repository, PVR clients, PVR IPTV Simple Client.'), ('Open its settings', 'Choose Configure and set the General tab.'), ('Add your M3U link', 'Select Remote path and paste your URL.'), ('Add the guide', 'Use the EPG settings tab and paste the XMLTV URL.'), ('Enable it', 'Restart Kodi so the TV menu appears.')],
  tips=['Use the cache settings for slow networks.', 'Keep Kodi on a stable release.', 'Back up your add-on settings.'],
  prob=[('No channels', 'Check the M3U link and restart Kodi.'), ('Wrong programme times', 'Set the time offset in the EPG settings.'), ('Add-on will not enable', 'Reinstall it.')]),
 'windows-mac-pc-iptv-player-australia': dict(
  open='On a Windows PC or Mac you can watch IPTV with VLC, Kodi or IPTV Smarters Pro. The quickest test is VLC: open Media, Open Network Stream and paste your M3U link.',
  need=['A Windows or Mac computer', 'VLC, Kodi or IPTV Smarters Pro', 'Your M3U link or Xtream login'],
  steps=[('Install a player', 'Download VLC, Kodi or IPTV Smarters Pro from the official site.'), ('Open your playlist', 'In VLC use Media, Open Network Stream. In Smarters, choose Xtream Codes.'), ('Pick a channel', 'Select a channel from the list.'), ('Use full screen', 'Press F or double click to go full screen.'), ('Connect to the TV', 'Use an HDMI cable or cast the screen if you want it on a large TV.')],
  tips=['Close heavy apps while streaming.', 'Use a cable on a laptop for sport.', 'Keep drivers up to date for smooth video.'],
  prob=[('VLC shows a black screen', 'Try Tools, Preferences, Input, hardware decoding off.'), ('Stream stops', 'Check Wi-Fi and try another channel.'), ('No sound', 'Check the output device.')]),
}
# ============================================================ COMPARISONS
C = {
 'foxtel-alternative-iptv-australia': dict(open='Foxtel is a licensed pay-TV and streaming service. An IPTV subscription is a different way to watch: you add a service to a player app on your own device. Compare price, contract, devices and, most importantly, whether the service has the rights to the channels it sells.',
   rows=[['Contract', 'Often a minimum term', 'Usually prepaid 3 to 12 months'], ['Where you watch', 'Foxtel box or app', 'Any device with an IPTV player'], ['Try before you buy', 'Rarely', 'Free trial offered here'], ['Content licensing', 'Licensed by Foxtel', 'Check each service']]),
 'kayo-sports-alternative-iptv-australia': dict(open='Kayo Sports is a licensed sports streaming app. An IPTV subscription works through a player app instead. Compare the sports you follow, the devices in your home and the cost per month, and always check licensing.',
   rows=[['Best for', 'Sport-only app', 'Live TV, sport and on-demand in one player'], ['Devices', 'Kayo app on supported devices', 'Fire TV, Android, Apple, Samsung, LG, PC'], ['Cost', 'Monthly subscription', 'Prepaid plans from 3 months'], ['Content licensing', 'Licensed by Kayo', 'Check each service']]),
 'binge-alternative-iptv-australia': dict(open='Binge is a licensed streaming service for TV series and movies. An IPTV subscription is a player-based service that can include live TV and on-demand. Compare what you watch, the devices you use and how you pay.',
   rows=[['Main use', 'Series and movies on demand', 'Live TV plus on-demand'], ['Devices', 'Binge app', 'Any IPTV player device'], ['Payment', 'Monthly', 'Prepaid 3 to 12 months'], ['Content licensing', 'Licensed by Binge', 'Check each service']]),
 'optus-sport-alternative-iptv-australia': dict(open='Optus Sport is a licensed streaming service known for football, including the Premier League. An IPTV subscription uses a player app instead. Compare the leagues you follow, your devices and whether the content is properly licensed.',
   rows=[['Main use', 'Football and soccer', 'Live TV including sport'], ['Devices', 'Optus Sport app', 'Any IPTV player device'], ['Payment', 'Monthly', 'Prepaid 3 to 12 months'], ['Content licensing', 'Licensed by Optus Sport', 'Check each service']]),
 'fetch-tv-alternative-iptv-australia': dict(open='Fetch is a licensed set-top box and app service. An IPTV subscription works through a player on your own box or TV. Compare the hardware you need, what you pay each month and the channels you watch.',
   rows=[['Hardware', 'Fetch box', 'Your own TV, box or phone'], ['Contract', 'Plans vary', 'Prepaid 3 to 12 months'], ['Setup', 'Provider installs or ships a box', 'Install a player app'], ['Content licensing', 'Licensed by Fetch', 'Check each service']]),
 'sky-sports-uk-australia-iptv': dict(open='Sky Sports is a UK sports channel group that is not sold directly in Australia. Australians usually watch Premier League and other UK sport through local licensed services. Check which service holds the rights for the competition you follow.',
   rows=[['Where it is sold', 'United Kingdom', 'Depends on the service'], ['Premier League in Australia', 'Held by a local licensed broadcaster', 'Check each service'], ['Devices', 'Sky app in the UK', 'Any IPTV player device'], ['Content licensing', 'Licensed by Sky in the UK', 'Check each service']]),
 'stan-sport-alternative-iptv-australia': dict(open='Stan Sport is a licensed add-on for Stan with rugby, tennis and other sport. An IPTV subscription uses a player app. Compare the sports you watch and your devices, and always check licensing.',
   rows=[['Main use', 'Rugby, tennis, football and more', 'Live TV including sport'], ['Devices', 'Stan app', 'Any IPTV player device'], ['Payment', 'Monthly add-on', 'Prepaid 3 to 12 months'], ['Content licensing', 'Licensed by Stan', 'Check each service']]),
}
# ============================================================ ISPs and languages (short direct answers)
ISP = {
 'telstra-nbn-iptv-anti-freeze-guide': 'To stop IPTV freezing on a Telstra NBN connection, use a wired connection, check Telstra’s typical evening speed for your plan and try a public DNS such as Cloudflare or Google.',
 'optus-broadband-iptv-optimization': 'To get a steady IPTV stream on Optus broadband, use the 5 GHz Wi-Fi band or a cable, restart the modem weekly and check the Optus typical evening speed for your plan.',
 'tpg-internet-iptv-anti-buffering-guide': 'To reduce IPTV buffering on TPG, connect by cable where possible, check the typical evening speed for your plan and try a different DNS.',
 'aussie-broadband-iptv-speed-guide': 'Aussie Broadband publishes typical evening speeds for each plan. Pick a plan above your needs from the IPTV bandwidth calculator, use a wired connection for the main TV and keep Wi-Fi on 5 GHz.',
 'starlink-australia-satellite-iptv-guide': 'IPTV works over Starlink, but latency and weather can cause short drop-outs. Use a wired connection from the router, avoid peak congestion and give the player a larger buffer if it has the option.',
}
LANG = {
 'arabic-lebanese-iptv-australia': 'To watch Arabic and Lebanese TV in Australia, choose an IPTV service that lists the channels you want, such as MBC and Shahid content, then add it to a player app on your TV.',
 'chinese-mandarin-cantonese-iptv-australia': 'To watch Mandarin and Cantonese TV in Australia, choose an IPTV service that lists the Chinese-language channels you want and add it to a player app on your TV or phone.',
 'filipino-tagalog-tv-iptv-australia': 'To watch Filipino TV in Australia, check which channels you want, such as TFC and GMA Pinoy, then pick an IPTV service that carries them and add it to a player app.',
 'greek-tv-channels-iptv-australia': 'To watch Greek TV in Australia, check that the IPTV service carries channels such as ERT, Mega and Antenna, then add it to a player app on your TV.',
 'indian-hindi-tv-channels-iptv-australia': 'To watch Hindi and Indian TV in Australia, check that an IPTV service carries channels such as Star and Zee, then add it to a player app on your TV or phone.',
 'italian-tv-channels-iptv-australia': 'To watch Italian TV in Australia, check that the IPTV service carries channels such as Rai and Mediaset, then add it to a player app on your TV.',
 'punjabi-tv-channels-iptv-australia': 'To watch Punjabi TV in Australia, choose an IPTV service that lists the Punjabi channels you follow and add it to a player app on your TV or phone.',
 'tamil-telugu-iptv-australia': 'To watch Tamil and Telugu TV in Australia, choose an IPTV service that lists the channels you want and add it to a player app on your TV or phone.',
 'vietnamese-tv-channels-iptv-australia': 'To watch Vietnamese TV in Australia, choose an IPTV service that lists the Vietnamese channels you follow and add it to a player app on your TV or phone.',
}
LANG_EXTRA = ('<h2>How to get started</h2>' + steps([('List the channels you want', 'Write down your must-have channels and any sport or news you follow.'), ('Test with a free trial', 'Use the free 24-hour trial to check that those channels are included and play well.'), ('Add the login to a player', 'Use TiviMate, IPTV Smarters Pro or IBO Player. See the <a href="../../iptv-player-australia/index.html">player guide</a>.'), ('Check licensing', 'Make sure the service has the rights to the channels it sells.')]))

def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)
HERO_P = re.compile(r'(<p class="hero-description"[^>]*>)(.*?)(</p>)', re.S)

def put_open(s, text):
    m = HERO_P.search(s)
    if not m: return s, False
    return s[:m.start()] + m.group(1) + text + m.group(3) + s[m.end():], True

def insert_block(s, block):
    k = s.find('<!-- Deep Content Section -->')
    if k < 0:
        m = re.search(r'</section>', s[s.find('hero-section'):]); k = s.find('hero-section') + m.end() if m else -1
    if k < 0: return s, False
    return s[:k] + block + '\n  ' + s[k:], True

n = dict(devices=0, comparisons=0, isps=0, languages=0)
for slug, c in D.items():
    p = 'devices/%s/index.html' % slug; s = rd(p)
    if 'content-pass' in s: continue
    s, a = put_open(s, c['open'])
    body = ('<h2>What you need</h2>' + ul(c['need']) + '<h2>Setup in 5 steps</h2>' + steps(c['steps']) + '<h2>Tips</h2>' + ul(c['tips']) + '<h2>Common problems</h2>' + faqs(c['prob'])
            + '<p>Not sure which app to choose? Compare them in the <a href="../../iptv-player-australia/index.html">IPTV player guide</a>, or test your setup with a <a href="../../iptv-free-trial-australia/index.html">free 24-hour trial</a>.</p>')
    s, b = insert_block(s, '<section class="content-pass" style="padding:3.5rem 0; background:var(--bg-main);"><div class="container"><article class="prose-block legal">%s</article></div></section>' % body)
    if a and b: wr(p, s); n['devices'] += 1
for slug, c in C.items():
    p = 'comparisons/%s/index.html' % slug
    if not os.path.exists(p): continue
    s = rd(p)
    if 'content-pass' in s: continue
    s, a = put_open(s, c['open'])
    tbl = '<div class="table-wrap"><table><thead><tr><th></th><th>Licensed service</th><th>IPTV subscription</th></tr></thead><tbody>%s</tbody></table></div>' % ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % x for x in r) for r in c['rows'])
    body = ('<h2>At a glance</h2>' + tbl + '<h2>How to decide</h2>' + ul(['List the sports and channels you actually watch.', 'Count the devices and TVs in your home.', 'Compare the cost over 12 months, not just one month.', 'Test an IPTV service with a free trial before you commit.', 'Choose a service that has the rights to its content.'])
            + '<p>Read the <a href="../../guides/is-iptv-legal-in-australia-2026-guide/index.html">IPTV legality guide</a> and the <a href="../../best-iptv-australia/index.html">best IPTV Australia guide</a> before you decide.</p>')
    s, b = insert_block(s, '<section class="content-pass" style="padding:3.5rem 0; background:var(--bg-main);"><div class="container"><article class="prose-block legal">%s</article></div></section>' % body)
    if a and b: wr(p, s); n['comparisons'] += 1
for kind, data in (('isps', ISP), ('languages', LANG)):
    for slug, text in data.items():
        p = '%s/%s/index.html' % (kind, slug)
        if not os.path.exists(p): continue
        s = rd(p)
        if 'content-pass' in s: continue
        s, a = put_open(s, text)
        extra = LANG_EXTRA if kind == 'languages' else ('<h2>Quick checks</h2>' + ul(['Use an Ethernet cable for the main TV.', 'Restart your modem once a week.', 'Try a public DNS from the <a href="../../guides/best-dns-for-iptv-australia/index.html">DNS guide</a>.', 'Work out the speed you need with the <a href="../../tools/iptv-bandwidth-calculator/index.html">bandwidth calculator</a>.']))
        s, b = insert_block(s, '<section class="content-pass" style="padding:3.5rem 0; background:var(--bg-main);"><div class="container"><article class="prose-block legal">%s</article></div></section>' % extra)
        if a and b: wr(p, s); n[kind] += 1
print(n)

# homepage: direct answer in the intro and keyword in the title
s = rd('index.html')
if 'Best IPTV Australia means' not in s:
    s = re.sub(r'(<p class="hero-description"[^>]*>\s*)', r'\1The best IPTV Australia has to offer is the service that runs smoothly on your own NBN connection, carries the sport you watch and lets you test it first. ', s, 1)
    s = s.replace('<title>IPTV Australia | Best IPTV Subscription &amp; Reseller Panel 2026</title>', '<title>Best IPTV Australia 2026 | IPTV Subscription &amp; Reseller Panel</title>')
    s = s.replace('content="IPTV Australia | Best IPTV Subscription &amp; Reseller Panel 2026"', 'content="Best IPTV Australia 2026 | IPTV Subscription &amp; Reseller Panel"')
    wr('index.html', s)
print('homepage intro and title updated')
print('DONE')

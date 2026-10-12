"""Adds 3 homepage sections: Free Trial, Best IPTV Box Australia, IPTV Player apps."""
p = 'index.html'
s = open(p, encoding='utf8', errors='surrogateescape').read()
if 'id="free-trial"' in s:
    raise SystemExit('already added')

TRIAL = '''
  <!-- ==================== FREE TRIAL ==================== -->
  <section class="section-padding-lg" style="background:var(--bg-main);" id="free-trial">
    <div class="container">
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:center;">
        <div>
          <span class="badge badge-glow-green" style="margin-bottom:0.75rem;"><i class="fa-solid fa-gift"></i> No Credit Card Needed</span>
          <h2 class="section-title" style="margin-top:0;">Free IPTV Trial Australia &mdash; Test It on Your Own TV First</h2>
          <p style="line-height:1.75; margin-bottom:1.25rem;">
            The best way to choose an IPTV service is to try it on your own internet connection. A free IPTV trial in Australia lets you check live channel quality, how fast channels change, and whether the stream holds up on your Telstra, Optus, TPG or Aussie Broadband NBN plan before you pay anything.
          </p>
          <ol style="list-style:none; display:flex; flex-direction:column; gap:0.9rem; margin-bottom:1.75rem; padding:0;">
            <li style="display:flex; gap:0.85rem; align-items:flex-start;"><span class="step-number" style="flex-shrink:0;">1</span><span><strong>Request your trial.</strong> Tell us your device and email. It takes under a minute.</span></li>
            <li style="display:flex; gap:0.85rem; align-items:flex-start;"><span class="step-number" style="flex-shrink:0;">2</span><span><strong>Install an app.</strong> Add the login details to TiviMate, IPTV Smarters Pro or IBO Player (see the player guide below).</span></li>
            <li style="display:flex; gap:0.85rem; align-items:flex-start;"><span class="step-number" style="flex-shrink:0;">3</span><span><strong>Test what matters to you.</strong> Try a live AFL or NRL match, evening news, and a 4K movie. Then decide.</span></li>
          </ol>
          <div style="display:flex; flex-wrap:wrap; gap:0.75rem;">
            <button class="btn btn-primary btn-lg" data-open-modal="trial"><i class="fa-solid fa-play"></i> Request Free 24H Trial</button>
            <a href="https://wa.me/61400000000?text=Hi%2C%20I%20would%20like%20a%20free%20IPTV%20trial%20in%20Australia" target="_blank" rel="noopener" class="btn btn-whatsapp btn-lg"><i class="fa-brands fa-whatsapp"></i> Ask on WhatsApp</a>
          </div>
        </div>
        <div>
          <figure class="media-figure" style="margin-bottom:1.25rem;">
            <img src="public/images/home/streaming-device-remote.webp" alt="Streaming box and remote next to a TV, ready for an IPTV trial" width="1200" height="800" loading="lazy" decoding="async" />
          </figure>
          <div class="glass-card" style="padding:1.5rem;">
            <h3 style="font-size:1.05rem; margin-bottom:0.75rem;"><i class="fa-solid fa-list-check" style="color:var(--primary); margin-right:0.4rem;"></i> What to check during your trial</h3>
            <ul style="list-style:none; display:flex; flex-direction:column; gap:0.55rem; font-size:0.92rem; color:var(--text-muted); padding:0;">
              <li><i class="fa-solid fa-check" style="color:var(--aus-green); margin-right:0.5rem;"></i> Live sport at peak time (Friday and Saturday nights)</li>
              <li><i class="fa-solid fa-check" style="color:var(--aus-green); margin-right:0.5rem;"></i> Channel switching speed and picture stability</li>
              <li><i class="fa-solid fa-check" style="color:var(--aus-green); margin-right:0.5rem;"></i> Programme guide (EPG) accuracy for your time zone</li>
              <li><i class="fa-solid fa-check" style="color:var(--aus-green); margin-right:0.5rem;"></i> Movies and series library on your own device</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

BOX = '''
  <!-- ==================== BEST IPTV BOX AUSTRALIA ==================== -->
  <section class="section-padding-lg" style="background:var(--bg-main);" id="iptv-box-australia">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-box"></i> Hardware Buying Guide</span>
        <h2 class="section-title">Best IPTV Box Australia: Which One Should You Buy?</h2>
        <p class="section-subtitle">An IPTV box is a small streaming device that plugs into your TV and runs the player app. The right choice depends on your TV, your budget and how many rooms you want to cover.</p>
      </div>
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.5rem; margin-bottom:2.5rem;">
        <div class="glass-card" style="text-align:center;">
          <div style="height:120px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;"><img src="public/images/devices/products/nvidia-shield.webp" alt="Nvidia Shield TV Pro IPTV box" style="max-height:110px; max-width:100%; object-fit:contain;" loading="lazy" /></div>
          <span class="badge badge-glow-gold" style="margin-bottom:0.6rem;">Best performance</span>
          <h3 style="font-size:1.2rem; margin-bottom:0.5rem;">Nvidia Shield TV Pro</h3>
          <p style="font-size:0.92rem; line-height:1.65;">The most powerful Android TV box. Handles 4K, large playlists and fast channel changes without slowing down. Costs more, but it stays smooth for years.</p>
          <a href="devices/nvidia-shield-pro-4k-iptv-australia/index.html" style="font-weight:700; font-size:0.88rem;">Shield setup guide &rarr;</a>
        </div>
        <div class="glass-card" style="text-align:center;">
          <div style="height:120px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;"><img src="public/images/devices/products/android-tv-box.webp" alt="Android TV box for IPTV in Australia" style="max-height:110px; max-width:100%; object-fit:contain;" loading="lazy" /></div>
          <span class="badge badge-glow-green" style="margin-bottom:0.6rem;">Best value</span>
          <h3 style="font-size:1.2rem; margin-bottom:0.5rem;">Android TV Box</h3>
          <p style="font-size:0.92rem; line-height:1.65;">Affordable boxes such as the Xiaomi Mi Box S run TiviMate and IPTV Smarters well. A good first IPTV box for one TV. Look for 4K output, 2 GB RAM or more, and Ethernet.</p>
          <a href="devices/iptv-on-android-tv-box-australia/index.html" style="font-weight:700; font-size:0.88rem;">Android TV box guide &rarr;</a>
        </div>
        <div class="glass-card" style="text-align:center;">
          <div style="height:120px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;"><img src="public/images/devices/products/formuler-box.webp" alt="Formuler Z IPTV box" style="max-height:110px; max-width:100%; object-fit:contain;" loading="lazy" /></div>
          <span class="badge badge-glow-cyan" style="margin-bottom:0.6rem;">Built for IPTV</span>
          <h3 style="font-size:1.2rem; margin-bottom:0.5rem;">Formuler Z / MAG Box</h3>
          <p style="font-size:0.92rem; line-height:1.65;">Boxes designed specifically for IPTV with a remote that is simple for the whole family. Formuler runs MyTVOnline; MAG boxes use a portal URL.</p>
          <a href="devices/formuler-z-mol3-iptv-australia/index.html" style="font-weight:700; font-size:0.88rem;">Formuler guide &rarr;</a>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
        <div class="glass-card">
          <h3 style="font-size:1.1rem; margin-bottom:0.75rem;"><i class="fa-solid fa-scale-balanced" style="color:var(--primary); margin-right:0.4rem;"></i> Box or Fire Stick?</h3>
          <p style="font-size:0.92rem; line-height:1.7;">An Amazon Fire TV Stick is the cheapest way to start and works with all the main players. A dedicated box costs more but usually gives faster menus, more storage and a wired network port, which helps on busy NBN evenings. If you only use one TV and a stable Wi-Fi connection, a Fire Stick 4K is enough.</p>
          <a href="devices/iptv-on-amazon-firestick-australia/index.html" style="font-weight:700; font-size:0.88rem;">Fire TV Stick guide &rarr;</a>
        </div>
        <div class="glass-card">
          <h3 style="font-size:1.1rem; margin-bottom:0.75rem;"><i class="fa-solid fa-list-check" style="color:var(--primary); margin-right:0.4rem;"></i> Checklist before you buy</h3>
          <ul style="list-style:none; display:flex; flex-direction:column; gap:0.5rem; font-size:0.92rem; color:var(--text-muted); padding:0;">
            <li><i class="fa-solid fa-check" style="color:var(--aus-green); margin-right:0.5rem;"></i> 4K output with HDMI 2.0 or newer</li>
            <li><i class="fa-solid fa-check" style="color:var(--aus-green); margin-right:0.5rem;"></i> Ethernet port or fast dual-band Wi-Fi</li>
            <li><i class="fa-solid fa-check" style="color:var(--aus-green); margin-right:0.5rem;"></i> At least 2 GB RAM and 16 GB storage</li>
            <li><i class="fa-solid fa-check" style="color:var(--aus-green); margin-right:0.5rem;"></i> Official Google or Amazon app store (avoid unbranded boxes with no updates)</li>
            <li><i class="fa-solid fa-check" style="color:var(--aus-green); margin-right:0.5rem;"></i> Australian warranty from a local retailer</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
'''

PLAYER = '''
  <!-- ==================== IPTV PLAYER APPS ==================== -->
  <section class="section-padding-lg" style="background:var(--bg-secondary);" id="iptv-player-apps">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-circle-play"></i> Player App Guide</span>
        <h2 class="section-title">Best IPTV Player App for Australia</h2>
        <p class="section-subtitle">An IPTV player is the app that plays your channels. It does not include any channels itself: you add the login details or playlist from your provider. Here is how the popular players compare.</p>
      </div>
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.5rem; margin-bottom:2.5rem;">
        <div class="glass-card">
          <div style="height:56px; display:flex; align-items:center; margin-bottom:1rem;"><img src="public/images/Tivimate-app-logo.webp" alt="TiviMate IPTV Player logo" style="max-height:52px; max-width:160px; object-fit:contain;" loading="lazy" /></div>
          <h3 style="font-size:1.2rem; margin-bottom:0.4rem;">TiviMate</h3>
          <span class="badge badge-glow-green" style="margin-bottom:0.75rem;">Best on Android TV &amp; Fire TV</span>
          <p style="font-size:0.92rem; line-height:1.65; margin-bottom:0.75rem;">A clean, fast guide-style interface with favourites, recording and multi-view in the premium version. A top pick for Fire Stick and Android TV boxes.</p>
          <a href="devices/tivimate-iptv-player-australia-setup/index.html" style="font-weight:700; font-size:0.88rem;">TiviMate setup &rarr;</a>
        </div>
        <div class="glass-card">
          <div style="height:56px; display:flex; align-items:center; margin-bottom:1rem;"><i class="fa-solid fa-circle-play" style="font-size:2.2rem; color:var(--primary);"></i></div>
          <h3 style="font-size:1.2rem; margin-bottom:0.4rem;">IPTV Smarters Pro</h3>
          <span class="badge badge-glow-cyan" style="margin-bottom:0.75rem;">Most compatible</span>
          <p style="font-size:0.92rem; line-height:1.65; margin-bottom:0.75rem;">Free, available on almost every platform: Android, iPhone, iPad, Fire TV, Windows and Mac. Simple login with a username, password and server URL.</p>
          <a href="devices/iptv-smarters-pro-australia-guide/index.html" style="font-weight:700; font-size:0.88rem;">Smarters Pro guide &rarr;</a>
        </div>
        <div class="glass-card">
          <div style="height:56px; display:flex; align-items:center; margin-bottom:1rem;"><img src="public/images/Ibo-Player-Pro-app-logo.webp" alt="IBO Player Pro logo" style="max-height:52px; max-width:160px; object-fit:contain;" loading="lazy" /></div>
          <h3 style="font-size:1.2rem; margin-bottom:0.4rem;">IBO Player</h3>
          <span class="badge badge-glow-gold" style="margin-bottom:0.75rem;">Best on Smart TVs</span>
          <p style="font-size:0.92rem; line-height:1.65; margin-bottom:0.75rem;">Popular on Samsung, LG and other smart TVs where you cannot sideload apps. You activate it with the device ID and MAC address shown on screen.</p>
          <a href="devices/ibo-player-australia-activation/index.html" style="font-weight:700; font-size:0.88rem;">IBO Player activation &rarr;</a>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.5rem; margin-bottom:2.5rem;">
        <div class="glass-card" style="padding:1.5rem;">
          <h4 style="margin-bottom:0.4rem;"><i class="fa-solid fa-tv" style="color:var(--primary); margin-right:0.4rem;"></i> Samsung &amp; LG smart TVs</h4>
          <p style="font-size:0.9rem; line-height:1.6;">Use IBO Player, Smart IPTV or Hot Player from the TV app store.</p>
          <a href="devices/iptv-on-samsung-smart-tv-tizen-australia/index.html" style="font-weight:700; font-size:0.85rem;">Samsung &rarr;</a> &nbsp; <a href="devices/iptv-on-lg-smart-tv-webos-australia/index.html" style="font-weight:700; font-size:0.85rem;">LG &rarr;</a>
        </div>
        <div class="glass-card" style="padding:1.5rem;">
          <h4 style="margin-bottom:0.4rem;"><i class="fa-brands fa-apple" style="color:var(--primary); margin-right:0.4rem;"></i> Apple TV, iPhone &amp; iPad</h4>
          <p style="font-size:0.9rem; line-height:1.6;">IPTV Smarters Pro and similar players are available on the App Store.</p>
          <a href="devices/iptv-on-apple-tv-tvos-australia/index.html" style="font-weight:700; font-size:0.85rem;">Apple TV guide &rarr;</a>
        </div>
        <div class="glass-card" style="padding:1.5rem;">
          <h4 style="margin-bottom:0.4rem;"><i class="fa-solid fa-laptop" style="color:var(--primary); margin-right:0.4rem;"></i> Windows &amp; Mac</h4>
          <p style="font-size:0.9rem; line-height:1.6;">Use VLC, Kodi with the IPTV Simple Client, or a desktop player app.</p>
          <a href="devices/windows-mac-pc-iptv-player-australia/index.html" style="font-weight:700; font-size:0.85rem;">PC guide &rarr;</a> &nbsp; <a href="devices/kodi-iptv-simple-client-australia/index.html" style="font-weight:700; font-size:0.85rem;">Kodi &rarr;</a>
        </div>
      </div>
      <div class="glass-card" style="background:#f8fafc;">
        <h3 style="font-size:1.1rem; margin-bottom:0.5rem;"><i class="fa-solid fa-circle-question" style="color:var(--primary); margin-right:0.4rem;"></i> Which one should I pick?</h3>
        <p style="font-size:0.95rem; line-height:1.75;">On a <strong>Fire Stick or Android TV box</strong>, start with TiviMate. On a <strong>Samsung or LG TV</strong>, use IBO Player. On an <strong>iPhone, iPad or PC</strong>, IPTV Smarters Pro is the simplest. All of them can be tested with a <a href="#free-trial">free IPTV trial</a> before you commit to a plan.</p>
      </div>
    </div>
  </section>
'''

marker = '<!-- ==================== 9. AUSTRALIAN ISP & DEVICE SETUP GUIDES'
i = s.find(marker)
assert i > 0, 'marker missing'
s = s[:i] + TRIAL.lstrip('\n') + '\n  ' + s[i:]
j = s.find('id="hardware-gallery"')
e = s.find('</section>', j) + len('</section>')
s = s[:e] + '\n' + BOX + PLAYER + s[e:]
open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)
print('added')

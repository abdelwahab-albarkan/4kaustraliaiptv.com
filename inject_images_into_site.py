import os, re

index_path = r"c:\Users\clanm\OneDrive\Desktop\australiatv\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

print(f"Loaded index.html: {len(html)} chars")

# =========================================================================
# 1. HERO SECTION: ADD DASHBOARD MOCKUP PREVIEW IN HERO VISUAL & DEVICE STRIP
# =========================================================================
hero_device_strip_html = """
          <!-- Floating Hardware Logos Strip -->
          <div style="margin-top:2.5rem; padding-top:1.5rem; border-top:1px solid var(--border-color);">
            <div style="font-size:0.82rem; color:var(--text-dim); text-transform:uppercase; letter-spacing:1px; margin-bottom:0.85rem; font-weight:700;">
              <i class="fa-solid fa-circle-check" style="color:var(--aus-green); margin-right:0.35rem;"></i> Compatible With All Australian Streaming Hardware & TVs:
            </div>
            <div style="display:flex; align-items:center; gap:1.25rem; flex-wrap:wrap;">
              <div style="display:flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.04); padding:0.4rem 0.8rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
                <img src="images/firestick.webp" alt="Firestick 4K" style="height:26px; object-fit:contain;" />
                <span style="font-size:0.8rem; color:#fff; font-weight:600;">Fire TV</span>
              </div>
              <div style="display:flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.04); padding:0.4rem 0.8rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
                <img src="images/appletv.webp" alt="Apple TV 4K" style="height:26px; object-fit:contain;" />
                <span style="font-size:0.8rem; color:#fff; font-weight:600;">Apple TV</span>
              </div>
              <div style="display:flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.04); padding:0.4rem 0.8rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
                <img src="images/samsungsmarttv.webp" alt="Samsung Smart TV" style="height:26px; object-fit:contain;" />
                <span style="font-size:0.8rem; color:#fff; font-weight:600;">Samsung</span>
              </div>
              <div style="display:flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.04); padding:0.4rem 0.8rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
                <img src="images/LG TV (webOS).webp" alt="LG webOS TV" style="height:26px; object-fit:contain;" />
                <span style="font-size:0.8rem; color:#fff; font-weight:600;">LG webOS</span>
              </div>
              <div style="display:flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.04); padding:0.4rem 0.8rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
                <img src="images/Android TV.webp" alt="Android TV" style="height:26px; object-fit:contain;" />
                <span style="font-size:0.8rem; color:#fff; font-weight:600;">Android TV</span>
              </div>
              <div style="display:flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.04); padding:0.4rem 0.8rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
                <img src="images/nvidiashield.webp" alt="Nvidia Shield" style="height:26px; object-fit:contain;" />
                <span style="font-size:0.8rem; color:#fff; font-weight:600;">Nvidia Shield</span>
              </div>
              <div style="display:flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.04); padding:0.4rem 0.8rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
                <img src="images/Formuler.webp" alt="Formuler Z11" style="height:26px; object-fit:contain;" />
                <span style="font-size:0.8rem; color:#fff; font-weight:600;">Formuler</span>
              </div>
            </div>
          </div>
"""

# Inject hero device strip right after hero-stats-strip
if "hero_device_strip_html" not in html and '<div class="hero-stats-strip">' in html:
    pattern = re.compile(r'(<div class="hero-stats-strip">.*?</div>\s*</div>)', re.DOTALL)
    html = pattern.sub(r'\1\n' + hero_device_strip_html, html, count=1)
    print("Injected Hero device strip!")

# Enhance Hero Portal Card with real TV dashboard preview
hero_dashboard_card_img = """
            <!-- 4K Dashboard Screen Preview -->
            <div style="position:relative; border-radius:var(--radius-md); overflow:hidden; margin-bottom:1.25rem; border:1px solid var(--border-highlight); box-shadow:0 8px 24px rgba(0,0,0,0.6);">
              <img src="images/apps-dashboard.webp" alt="4K IPTV Australia TV Guide & EPG Interface" style="width:100%; height:180px; object-fit:cover; display:block;" />
              <div style="position:absolute; top:8px; right:8px; background:rgba(10,6,20,0.85); backdrop-filter:blur(8px); padding:0.25rem 0.6rem; border-radius:var(--radius-sm); font-size:0.75rem; color:var(--aus-gold); font-weight:700; border:1px solid var(--border-gold);">
                <i class="fa-solid fa-satellite-dish"></i> 4K 60FPS Live
              </div>
              <div style="position:absolute; bottom:8px; left:8px; background:rgba(10,6,20,0.85); backdrop-filter:blur(8px); padding:0.25rem 0.6rem; border-radius:var(--radius-sm); font-size:0.72rem; color:var(--secondary); font-weight:600; border:1px solid var(--border-color);">
                <i class="fa-solid fa-football"></i> Fox Footy 504 • Optus 1 • Stan 4K
              </div>
            </div>
"""
if "4K Dashboard Screen Preview" not in html and '<div class="portal-card-header">' in html:
    html = html.replace('<div class="portal-card-header">', hero_dashboard_card_img + '\n            <div class="portal-card-header">', 1)
    print("Injected Hero dashboard card image!")

# =========================================================================
# 2. SPORTS SECTION: INJECT REAL HIGH RESOLUTION ACTION BANNERS
# =========================================================================
# AFL Card
if 'alt="AFL Melbourne Stadium"' not in html and '<div class="sport-card gold-theme">' in html:
    html = html.replace(
        '<div class="sport-card gold-theme">\n          <div>',
        '<div class="sport-card gold-theme">\n          <div>\n            <div style="position:relative; border-radius:var(--radius-sm); overflow:hidden; margin-bottom:1rem; border:1px solid var(--border-gold);"><img src="images/afl-nrl-stadium.webp" alt="AFL Melbourne Stadium" style="width:100%; height:150px; object-fit:cover; display:block;" /><div style="position:absolute; bottom:6px; left:8px; background:rgba(0,0,0,0.8); padding:0.2rem 0.5rem; border-radius:4px; font-size:0.72rem; color:var(--aus-gold); font-weight:700;">MCG • Fox Footy 504 4K</div></div>',
        1
    )
    print("Injected AFL image!")

# NRL Card
if 'alt="NRL Stadium Action"' not in html and '<div class="sport-card">\n          <div>\n            <div class="sport-icon-header">\n              <div class="sport-badge-icon">\n                <i class="fa-solid fa-shield"></i>' in html:
    html = html.replace(
        '<div class="sport-card">\n          <div>\n            <div class="sport-icon-header">\n              <div class="sport-badge-icon">\n                <i class="fa-solid fa-shield"></i>',
        '<div class="sport-card">\n          <div>\n            <div style="position:relative; border-radius:var(--radius-sm); overflow:hidden; margin-bottom:1rem; border:1px solid var(--border-color);"><img src="images/packimages2/lucid-origin_Epic_night_football_scene_from_low_angle_a_player_striking_the_ball_under_bright-0.webp" alt="NRL Stadium Action" style="width:100%; height:150px; object-fit:cover; display:block;" /><div style="position:absolute; bottom:6px; left:8px; background:rgba(0,0,0,0.8); padding:0.2rem 0.5rem; border-radius:4px; font-size:0.72rem; color:var(--primary); font-weight:700;">Fox League 502 • State of Origin</div></div>\n            <div class="sport-icon-header">\n              <div class="sport-badge-icon">\n                <i class="fa-solid fa-shield"></i>',
        1
    )
    print("Injected NRL image!")

# Cricket Card
if 'alt="Cricket Australia The Ashes"' not in html and '<div class="sport-card">\n          <div>\n            <div class="sport-icon-header">\n              <div class="sport-badge-icon">\n                <i class="fa-solid fa-baseball-bat-ball"></i>' in html:
    html = html.replace(
        '<div class="sport-card">\n          <div>\n            <div class="sport-icon-header">\n              <div class="sport-badge-icon">\n                <i class="fa-solid fa-baseball-bat-ball"></i>',
        '<div class="sport-card">\n          <div>\n            <div style="position:relative; border-radius:var(--radius-sm); overflow:hidden; margin-bottom:1rem; border:1px solid var(--border-color);"><img src="images/cricket-ashes.webp" alt="Cricket Australia The Ashes" style="width:100%; height:150px; object-fit:cover; display:block;" /><div style="position:absolute; bottom:6px; left:8px; background:rgba(0,0,0,0.8); padding:0.2rem 0.5rem; border-radius:4px; font-size:0.72rem; color:var(--aus-green); font-weight:700;">Fox Cricket 501 • BBL • The Ashes</div></div>\n            <div class="sport-icon-header">\n              <div class="sport-badge-icon">\n                <i class="fa-solid fa-baseball-bat-ball"></i>',
        1
    )
    print("Injected Cricket image!")

# =========================================================================
# 3. TOP PROVIDERS: INJECT DASHBOARD AND STREAMING SCREENS
# =========================================================================
# Trex provider card
if 'alt="Trex IPTV AU 4K Screen"' not in html and '<div class="provider-card featured-gold" id="provider-trex">' in html:
    html = html.replace(
        '<div class="provider-card featured-gold" id="provider-trex">\n          <div class="provider-top-ribbon">',
        '<div class="provider-card featured-gold" id="provider-trex">\n          <div class="provider-top-ribbon">',
        1
    )
    # Add image before provider-desc
    html = html.replace(
        '<p class="provider-desc">The undisputed king of sports in Australia.',
        '<div style="margin:0.75rem 0; border-radius:var(--radius-sm); overflow:hidden; border:1px solid var(--border-gold);"><img src="images/apps-dashboard.webp" alt="Trex IPTV AU 4K Screen" style="width:100%; height:130px; object-fit:cover; display:block;" /></div>\n            <p class="provider-desc">The undisputed king of sports in Australia.',
        1
    )
    print("Injected Trex provider image!")

# Ultra 8K provider card
if 'alt="Ultra 8K IPTV AU Quality Screen"' not in html and '<div class="provider-card featured-au" id="provider-ultra8k">' in html:
    html = html.replace(
        '<p class="provider-desc">Pristine picture quality engineered for OLED and QLED large screens.',
        '<div style="margin:0.75rem 0; border-radius:var(--radius-sm); overflow:hidden; border:1px solid var(--border-color);"><img src="images/quality-4k.webp" alt="Ultra 8K IPTV AU Quality Screen" style="width:100%; height:130px; object-fit:cover; display:block;" /></div>\n            <p class="provider-desc">Pristine picture quality engineered for OLED and QLED large screens.',
        1
    )
    print("Injected Ultra 8K provider image!")

# 8K IPTV Australia
if 'alt="8K IPTV Australia Home Cinema"' not in html and 'id="provider-8k"' in html:
    html = html.replace(
        '<p class="provider-desc">Optimized for home theatre setups with Dolby Digital 5.1.',
        '<div style="margin:0.75rem 0; border-radius:var(--radius-sm); overflow:hidden; border:1px solid var(--border-color);"><img src="images/home-cinema.webp" alt="8K IPTV Australia Home Cinema" style="width:100%; height:130px; object-fit:cover; display:block;" /></div>\n            <p class="provider-desc">Optimized for home theatre setups with Dolby Digital 5.1.',
        1
    )
    print("Injected 8K IPTV Australia image!")

# 5GLive AU
if 'alt="5GLive AU VOD Screen"' not in html and 'id="provider-5glive"' in html:
    html = html.replace(
        '<p class="provider-desc">Champion provider for multicultural communities across Sydney and Melbourne.',
        '<div style="margin:0.75rem 0; border-radius:var(--radius-sm); overflow:hidden; border:1px solid var(--border-color);"><img src="images/vod-dashboard.webp" alt="5GLive AU VOD Screen" style="width:100%; height:130px; object-fit:cover; display:block;" /></div>\n            <p class="provider-desc">Champion provider for multicultural communities across Sydney and Melbourne.',
        1
    )
    print("Injected 5GLive provider image!")

# =========================================================================
# 4. MASTER 20-DEVICE & APP GALLERY SECTION
# =========================================================================
master_device_gallery_html = """
  <!-- ==================== COMPREHENSIVE AUSTRALIAN DEVICE & HARDWARE GALLERY ==================== -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="hardware-gallery">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-tv"></i> Universal Hardware Support</span>
        <h2 class="section-title">Works Flawlessly Across Every Australian TV & Device</h2>
        <p class="section-subtitle">No proprietary hardware needed. Download our recommended apps on your existing smart television, streaming stick, tablet, phone, or console.</p>
      </div>

      <!-- 16 Key Devices Grid with Real Product PNGs/WebPs -->
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.5rem; margin-bottom:3rem;">
        <!-- 1. Firestick -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem; transition:transform 0.3s ease;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/firestick.webp" alt="Amazon Firestick 4K" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">Amazon Fire TV Stick</h4>
          <span class="badge badge-glow-gold" style="font-size:0.75rem; margin-bottom:0.6rem;">Fire OS 7/8</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">4K Max & Cube support. Install TiviMate or IPTV Smarters in 3 mins.</p>
          <a href="devices/iptv-on-amazon-firestick-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Firestick Guide →</a>
        </div>

        <!-- 2. Apple TV -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/appletv.webp" alt="Apple TV 4K" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">Apple TV 4K</h4>
          <span class="badge badge-glow-cyan" style="font-size:0.75rem; margin-bottom:0.6rem;">tvOS 16/17/18</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">iPlayTV & IPTVX with Dolby Vision & Siri Remote navigation.</p>
          <a href="devices/iptv-on-apple-tv-tvos-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Apple TV Guide →</a>
        </div>

        <!-- 3. Samsung Smart TV -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/samsungsmarttv.webp" alt="Samsung Smart TV" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">Samsung Tizen TV</h4>
          <span class="badge badge-glow-green" style="font-size:0.75rem; margin-bottom:0.6rem;">QLED / OLED</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">Native IBO Player & Smart IPTV in Samsung Apps Store.</p>
          <a href="devices/iptv-on-samsung-smart-tv-tizen-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Samsung Guide →</a>
        </div>

        <!-- 4. LG webOS TV -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/LG TV (webOS).webp" alt="LG webOS TV" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">LG webOS Smart TV</h4>
          <span class="badge badge-glow-cyan" style="font-size:0.75rem; margin-bottom:0.6rem;">webOS 5 - 24</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">LG OLED C & G series optimized with Magic Remote.</p>
          <a href="devices/iptv-on-lg-smart-tv-webos-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">LG TV Guide →</a>
        </div>

        <!-- 5. Android TV -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/Android TV.webp" alt="Android TV Box" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">Android TV / Box</h4>
          <span class="badge badge-glow-gold" style="font-size:0.75rem; margin-bottom:0.6rem;">Google TV 11+</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">Google Play Store apps with instant automatic EPG sync.</p>
          <a href="devices/iptv-on-android-tv-box-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Android TV Guide →</a>
        </div>

        <!-- 6. Nvidia Shield -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/nvidiashield.webp" alt="Nvidia Shield Pro" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">Nvidia Shield Pro</h4>
          <span class="badge badge-glow-green" style="font-size:0.75rem; margin-bottom:0.6rem;">AI 4K Upscaling</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">Highest processing power for 4K 60FPS sports broadcasts.</p>
          <a href="devices/iptv-on-android-tv-box-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Shield Guide →</a>
        </div>

        <!-- 7. Formuler Z11 -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/Formuler.webp" alt="Formuler Z11 Pro" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">Formuler Z11 Box</h4>
          <span class="badge badge-glow-cyan" style="font-size:0.75rem; margin-bottom:0.6rem;">MyTVOnline 3</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">Dedicated hardware with premium MOL3 PVR recording.</p>
          <a href="devices/iptv-on-formuler-mytvonline-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Formuler Guide →</a>
        </div>

        <!-- 8. Google Chromecast -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/chromecast.webp" alt="Google Chromecast 4K" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">Chromecast 4K</h4>
          <span class="badge badge-glow-gold" style="font-size:0.75rem; margin-bottom:0.6rem;">Google TV</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">Plug into any HDMI port for portable Australian 4K streaming.</p>
          <a href="devices/iptv-on-android-tv-box-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Chromecast Guide →</a>
        </div>

        <!-- 9. Sony Google TV -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/Sony TV (Google TV).webp" alt="Sony Bravia TV" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">Sony Bravia TV</h4>
          <span class="badge badge-glow-cyan" style="font-size:0.75rem; margin-bottom:0.6rem;">XR Processor</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">Integrated Google TV interface with direct Play Store installs.</p>
          <a href="devices/iptv-on-android-tv-box-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Sony TV Guide →</a>
        </div>

        <!-- 10. TCL & Hisense TV -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/Hisense TV.webp" alt="Hisense VIDAA TV" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">Hisense & TCL</h4>
          <span class="badge badge-glow-green" style="font-size:0.75rem; margin-bottom:0.6rem;">VIDAA & Android</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">Australia's most popular budget 4K screens fully compatible.</p>
          <a href="devices/iptv-on-samsung-smart-tv-tizen-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Hisense Guide →</a>
        </div>

        <!-- 11. Apple iPad & Tablets -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/iPad.webp" alt="Apple iPad" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">iPad & Fire Tablet</h4>
          <span class="badge badge-glow-cyan" style="font-size:0.75rem; margin-bottom:0.6rem;">iPadOS / Android</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">Watch live footy and cricket anywhere in Australia on the go.</p>
          <a href="devices/iptv-on-apple-tv-tvos-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">iPad Guide →</a>
        </div>

        <!-- 12. iPhone & Android Smartphones -->
        <div class="glass-card" style="text-align:center; padding:2rem 1.25rem;">
          <div style="height:90px; display:flex; align-items:center; justify-content:center; margin-bottom:1rem;">
            <img src="images/iphone17.webp" alt="Apple iPhone" style="max-height:85px; max-width:100%; object-fit:contain;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;">iPhone & Galaxy</h4>
          <span class="badge badge-glow-gold" style="font-size:0.75rem; margin-bottom:0.6rem;">iOS & Android</span>
          <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.5;">Cast directly to your television via AirPlay or Chromecast.</p>
          <a href="devices/iptv-on-apple-tv-tvos-australia/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Mobile Guide →</a>
        </div>
      </div>

      <!-- Top IPTV Streaming Apps Showcase Strip -->
      <div class="glass-card" style="border-color:var(--border-mauve); padding:2rem 2.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem;">
          <div>
            <h3 style="color:#fff; font-size:1.35rem; margin:0;"><i class="fa-solid fa-shapes" style="color:var(--primary); margin-right:0.5rem;"></i> Top IPTV Applications Supported</h3>
            <p style="color:var(--text-muted); font-size:0.88rem; margin:0;">Download directly on your TV or media player:</p>
          </div>
          <span class="badge badge-glow-gold">Instant Xtream Codes & M3U</span>
        </div>

        <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:1.25rem; text-align:center;">
          <div style="background:rgba(0,0,0,0.35); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <img src="images/Tivimate-app-logo.webp" alt="TiviMate Player" style="height:48px; object-fit:contain; margin-bottom:0.5rem;" />
            <h5 style="color:#fff; font-size:0.95rem; margin-bottom:0.2rem;">TiviMate</h5>
            <span style="font-size:0.75rem; color:var(--aus-gold);">#1 Android / Firestick</span>
          </div>

          <div style="background:rgba(0,0,0,0.35); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <img src="images/Ibo-Player-Pro-app-logo.webp" alt="IBO Player Pro" style="height:48px; object-fit:contain; margin-bottom:0.5rem;" />
            <h5 style="color:#fff; font-size:0.95rem; margin-bottom:0.2rem;">IBO Player Pro</h5>
            <span style="font-size:0.75rem; color:var(--primary);">#1 Samsung & LG</span>
          </div>

          <div style="background:rgba(0,0,0,0.35); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <img src="images/Smart-IPTV-app-logo.webp" alt="Smart IPTV SIPTV" style="height:48px; object-fit:contain; margin-bottom:0.5rem;" />
            <h5 style="color:#fff; font-size:0.95rem; margin-bottom:0.2rem;">Smart IPTV</h5>
            <span style="font-size:0.75rem; color:var(--secondary);">MAC Address Active</span>
          </div>

          <div style="background:rgba(0,0,0,0.35); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <img src="images/Hot-Player-app-logo.webp" alt="Hot Player" style="height:48px; object-fit:contain; margin-bottom:0.5rem;" />
            <h5 style="color:#fff; font-size:0.95rem; margin-bottom:0.2rem;">Hot Player</h5>
            <span style="font-size:0.75rem; color:var(--aus-green);">Multi-Screen UI</span>
          </div>

          <div style="background:rgba(0,0,0,0.35); padding:1rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <img src="images/Smart-STB-app-logo.webp" alt="Smart STB" style="height:48px; object-fit:contain; margin-bottom:0.5rem;" />
            <h5 style="color:#fff; font-size:0.95rem; margin-bottom:0.2rem;">Smart STB</h5>
            <span style="font-size:0.75rem; color:var(--primary);">Stalker Emulation</span>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# Insert master hardware gallery before Section 10 Testimonials
if 'id="hardware-gallery"' not in html:
    html = html.replace('<!-- ==================== 10. TESTIMONIALS (SYDNEY, MELBOURNE, BRISBANE, PERTH) ==================== -->', master_device_gallery_html + '\n  <!-- ==================== 10. TESTIMONIALS (SYDNEY, MELBOURNE, BRISBANE, PERTH) ==================== -->', 1)
    print("Injected Master Device Gallery!")

# =========================================================================
# 5. TESTIMONIALS: REPLACE DUMMY INITIALS WITH REAL CUSTOMER AVATARS
# =========================================================================
html = html.replace(
    '<div class="reviewer-avatar">MR</div>',
    '<img src="images/revriw/avatars/avatar-1.webp" alt="Marcus Reynolds" style="width:48px; height:48px; border-radius:50%; object-fit:cover; border:2px solid var(--primary);" />',
    1
)
html = html.replace(
    '<div class="reviewer-avatar">DL</div>',
    '<img src="images/revriw/avatars/avatar-2.webp" alt="David Lawson" style="width:48px; height:48px; border-radius:50%; object-fit:cover; border:2px solid var(--aus-gold);" />',
    1
)
html = html.replace(
    '<div class="reviewer-avatar">SK</div>',
    '<img src="images/revriw/avatars/avatar-3.webp" alt="Sanjay Kumar" style="width:48px; height:48px; border-radius:50%; object-fit:cover; border:2px solid var(--secondary);" />',
    1
)
print("Updated Testimonial Avatars!")

# =========================================================================
# 6. PAYMENTS & CHECKOUT HUB: REPLACE TEXT BADGES WITH REAL PAYMENT LOGOS
# =========================================================================
payment_logos_strip = """
          <div style="display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap; margin-bottom:1.25rem;">
            <div style="background:#fff; padding:0.3rem 0.6rem; border-radius:4px; display:flex; align-items:center; height:32px;"><img src="images/visa-logo.webp" alt="Visa" style="height:18px; object-fit:contain;" /></div>
            <div style="background:#fff; padding:0.3rem 0.6rem; border-radius:4px; display:flex; align-items:center; height:32px;"><img src="images/mastercard-logo.webp" alt="Mastercard" style="height:20px; object-fit:contain;" /></div>
            <div style="background:#000; padding:0.3rem 0.6rem; border-radius:4px; display:flex; align-items:center; height:32px; border:1px solid #333;"><img src="images/apple-pay-logo.webp" alt="Apple Pay" style="height:18px; object-fit:contain;" /></div>
            <div style="background:#fff; padding:0.3rem 0.6rem; border-radius:4px; display:flex; align-items:center; height:32px;"><img src="images/google-pay-logo.webp" alt="Google Pay" style="height:18px; object-fit:contain;" /></div>
            <div style="background:#fff; padding:0.3rem 0.6rem; border-radius:4px; display:flex; align-items:center; height:32px;"><img src="images/paypal-logo.webp" alt="PayPal" style="height:18px; object-fit:contain;" /></div>
            <div style="background:rgba(255,255,255,0.08); padding:0.3rem 0.6rem; border-radius:4px; display:flex; align-items:center; height:32px; gap:0.3rem; border:1px solid var(--border-gold);"><img src="images/crypto-logo.webp" alt="Crypto" style="height:20px; object-fit:contain;" /><span style="font-size:0.75rem; color:var(--aus-gold); font-weight:700;">Crypto BTC</span></div>
          </div>
"""

# Replace text payment badges in footer
footer_old_badges = """<div style="display:flex; flex-wrap:wrap; gap:0.4rem; margin-bottom:1.25rem;">
            <span class="badge badge-glow-gold">PayID</span>
            <span class="badge badge-glow-cyan">Visa / MC</span>
            <span class="badge badge-glow-green">Apple Pay</span>
            <span class="badge badge-glow-cyan">PayPal</span>
            <span class="badge badge-glow-gold">Crypto</span>
          </div>"""

if footer_old_badges in html:
    html = html.replace(footer_old_badges, payment_logos_strip, 1)
    print("Injected real payment logos in footer!")

# =========================================================================
# 7. INJECT INFOGRAPHIC IN FOXTEL & KAYO COMPARISON
# =========================================================================
infographic_html = """
        <div style="margin-bottom:2.5rem; text-align:center;">
          <div style="position:relative; border-radius:var(--radius-md); overflow:hidden; border:1px solid var(--border-gold); display:inline-block; max-width:100%; box-shadow:0 10px 30px rgba(0,0,0,0.5);">
            <img src="images/cable-vs-iptv.webp" alt="IPTV vs Foxtel Cable Comparison Infographic" style="width:100%; max-height:360px; object-fit:cover; display:block;" />
            <div style="position:absolute; bottom:12px; left:16px; background:rgba(10,6,20,0.9); padding:0.4rem 1rem; border-radius:var(--radius-sm); border:1px solid var(--border-gold);">
              <span style="color:var(--aus-gold); font-weight:800; font-size:1.05rem;">Save $3,332 AUD/Year</span> • 50,000+ Channels vs Foxtel Cable
            </div>
          </div>
        </div>
"""
if 'alt="IPTV vs Foxtel Cable Comparison Infographic"' not in html and '<div class="glass-card" style="margin-bottom:2.5rem; border-color:var(--border-gold);">' in html:
    html = html.replace(
        '<div class="glass-card" style="margin-bottom:2.5rem; border-color:var(--border-gold);">',
        infographic_html + '\n      <div class="glass-card" style="margin-bottom:2.5rem; border-color:var(--border-gold);">',
        1
    )
    print("Injected Cable vs IPTV infographic!")

# =========================================================================
# 8. INJECT REAL SUPPORT TEAM & PAYMENT PHOTO IN PAYID HUB
# =========================================================================
if 'alt="Australian 24/7 WhatsApp IPTV Support Team"' not in html and '<div style="background:rgba(0,0,0,0.5); padding:2rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">' in html:
    html = html.replace(
        '<div style="background:rgba(0,0,0,0.5); padding:2rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">',
        '<div style="background:rgba(0,0,0,0.5); padding:2rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">\n            <div style="margin-bottom:1.5rem; border-radius:var(--radius-md); overflow:hidden; border:1px solid var(--border-color);"><img src="images/support-team.webp" alt="Australian 24/7 WhatsApp IPTV Support Team" style="width:100%; height:150px; object-fit:cover; display:block;" /></div>',
        1
    )
    print("Injected Support Team photo in PayID hub!")

# Save updated index.html
with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"SUCCESS: Injected all images into index.html! New size: {len(html)} chars")

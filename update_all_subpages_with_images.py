import os, re

base_dir = r"c:\Users\clanm\OneDrive\Desktop\australiatv"

# =========================================================================
# 1. UPGRADE SETUP.HTML
# =========================================================================
setup_path = os.path.join(base_dir, "setup.html")
if os.path.exists(setup_path):
    with open(setup_path, "r", encoding="utf-8") as f:
        s_html = f.read()

    device_showcase = """
      <!-- Comprehensive Hardware & App Showcase -->
      <div style="margin-bottom:3.5rem;">
        <h3 style="font-size:1.6rem; color:#fff; text-align:center; margin-bottom:1.5rem;"><i class="fa-solid fa-tv" style="color:var(--primary); margin-right:0.5rem;"></i> Supported Australian Hardware (Select Your Device)</h3>
        
        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.5rem; margin-bottom:2.5rem;">
          <div class="glass-card" style="text-align:center; padding:1.75rem 1rem;">
            <div style="height:80px; display:flex; align-items:center; justify-content:center; margin-bottom:0.75rem;">
              <img src="images/firestick.webp" alt="Firestick 4K" style="max-height:75px; object-fit:contain;" />
            </div>
            <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.3rem;">Amazon Fire TV Stick</h4>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Fire TV Stick 4K, 4K Max & Cube. Supports TiviMate & IPTV Smarters.</p>
            <a href="devices/iptv-on-amazon-firestick-australia/index.html" class="btn btn-primary btn-sm btn-block">Firestick Guide →</a>
          </div>

          <div class="glass-card" style="text-align:center; padding:1.75rem 1rem;">
            <div style="height:80px; display:flex; align-items:center; justify-content:center; margin-bottom:0.75rem;">
              <img src="images/samsungsmarttv.webp" alt="Samsung Smart TV" style="max-height:75px; object-fit:contain;" />
            </div>
            <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.3rem;">Samsung Smart TV</h4>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Tizen OS (2018-2026). Install IBO Player directly from Samsung Apps.</p>
            <a href="devices/iptv-on-samsung-smart-tv-tizen-australia/index.html" class="btn btn-primary btn-sm btn-block">Samsung Guide →</a>
          </div>

          <div class="glass-card" style="text-align:center; padding:1.75rem 1rem;">
            <div style="height:80px; display:flex; align-items:center; justify-content:center; margin-bottom:0.75rem;">
              <img src="images/LG TV (webOS).webp" alt="LG webOS TV" style="max-height:75px; object-fit:contain;" />
            </div>
            <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.3rem;">LG webOS OLED TV</h4>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">webOS 5.0 - 24. Install IBO Player or Smart IPTV with Magic Remote.</p>
            <a href="devices/iptv-on-lg-smart-tv-webos-australia/index.html" class="btn btn-primary btn-sm btn-block">LG TV Guide →</a>
          </div>

          <div class="glass-card" style="text-align:center; padding:1.75rem 1rem;">
            <div style="height:80px; display:flex; align-items:center; justify-content:center; margin-bottom:0.75rem;">
              <img src="images/appletv.webp" alt="Apple TV 4K" style="max-height:75px; object-fit:contain;" />
            </div>
            <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.3rem;">Apple TV 4K & iOS</h4>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">tvOS 16/17/18. Stream with iPlayTV, IPTVX, or UHF Player in Dolby Vision.</p>
            <a href="devices/iptv-on-apple-tv-tvos-australia/index.html" class="btn btn-primary btn-sm btn-block">Apple TV Guide →</a>
          </div>

          <div class="glass-card" style="text-align:center; padding:1.75rem 1rem;">
            <div style="height:80px; display:flex; align-items:center; justify-content:center; margin-bottom:0.75rem;">
              <img src="images/Android TV.webp" alt="Android TV" style="max-height:75px; object-fit:contain;" />
            </div>
            <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.3rem;">Android TV & Google TV</h4>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Chromecast, Sony Bravia, TCL, Hisense with TiviMate & full EPG sync.</p>
            <a href="devices/iptv-on-android-tv-box-australia/index.html" class="btn btn-primary btn-sm btn-block">Android TV Guide →</a>
          </div>

          <div class="glass-card" style="text-align:center; padding:1.75rem 1rem;">
            <div style="height:80px; display:flex; align-items:center; justify-content:center; margin-bottom:0.75rem;">
              <img src="images/Formuler.webp" alt="Formuler Z11" style="max-height:75px; object-fit:contain;" />
            </div>
            <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.3rem;">Formuler Z11 Pro Max</h4>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Dedicated IPTV hardware with MyTVOnline 3 portal and DVR recording.</p>
            <a href="devices/iptv-on-formuler-mytvonline-australia/index.html" class="btn btn-primary btn-sm btn-block">Formuler Guide →</a>
          </div>

          <div class="glass-card" style="text-align:center; padding:1.75rem 1rem;">
            <div style="height:80px; display:flex; align-items:center; justify-content:center; margin-bottom:0.75rem;">
              <img src="images/nvidiashield.webp" alt="Nvidia Shield" style="max-height:75px; object-fit:contain;" />
            </div>
            <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.3rem;">Nvidia Shield Pro</h4>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Tegra X1+ powerhouse with AI 4K upscaling for footy and live sports.</p>
            <a href="devices/iptv-on-android-tv-box-australia/index.html" class="btn btn-primary btn-sm btn-block">Shield Guide →</a>
          </div>

          <div class="glass-card" style="text-align:center; padding:1.75rem 1rem;">
            <div style="height:80px; display:flex; align-items:center; justify-content:center; margin-bottom:0.75rem;">
              <img src="images/chromecast.webp" alt="Chromecast 4K" style="max-height:75px; object-fit:contain;" />
            </div>
            <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.3rem;">Chromecast with Google TV</h4>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Plug into any HDMI port with Voice Remote and Google Play Store.</p>
            <a href="devices/iptv-on-android-tv-box-australia/index.html" class="btn btn-primary btn-sm btn-block">Chromecast Guide →</a>
          </div>
        </div>

        <!-- Recommended Apps Row -->
        <div class="glass-card" style="padding:1.75rem; border-color:var(--border-mauve);">
          <h4 style="color:#fff; font-size:1.2rem; margin-bottom:1rem; text-align:center;"><i class="fa-solid fa-shapes" style="color:var(--secondary); margin-right:0.4rem;"></i> Recommended Streaming Apps</h4>
          <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:1rem; text-align:center;">
            <div style="background:rgba(0,0,0,0.3); padding:0.85rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
              <img src="images/Tivimate-app-logo.webp" alt="TiviMate" style="height:40px; object-fit:contain; margin-bottom:0.35rem;" />
              <div style="color:#fff; font-size:0.85rem; font-weight:700;">TiviMate</div>
              <span style="font-size:0.72rem; color:var(--aus-gold);">#1 Choice Android</span>
            </div>
            <div style="background:rgba(0,0,0,0.3); padding:0.85rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
              <img src="images/Ibo-Player-Pro-app-logo.webp" alt="IBO Player" style="height:40px; object-fit:contain; margin-bottom:0.35rem;" />
              <div style="color:#fff; font-size:0.85rem; font-weight:700;">IBO Player Pro</div>
              <span style="font-size:0.72rem; color:var(--primary);">#1 Choice Samsung/LG</span>
            </div>
            <div style="background:rgba(0,0,0,0.3); padding:0.85rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
              <img src="images/Smart-IPTV-app-logo.webp" alt="Smart IPTV" style="height:40px; object-fit:contain; margin-bottom:0.35rem;" />
              <div style="color:#fff; font-size:0.85rem; font-weight:700;">Smart IPTV</div>
              <span style="font-size:0.72rem; color:var(--secondary);">MAC Address Active</span>
            </div>
            <div style="background:rgba(0,0,0,0.3); padding:0.85rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
              <img src="images/Hot-Player-app-logo.webp" alt="Hot Player" style="height:40px; object-fit:contain; margin-bottom:0.35rem;" />
              <div style="color:#fff; font-size:0.85rem; font-weight:700;">Hot Player</div>
              <span style="font-size:0.72rem; color:var(--aus-green);">Multi-Screen</span>
            </div>
            <div style="background:rgba(0,0,0,0.3); padding:0.85rem; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
              <img src="images/Smart-STB-app-logo.webp" alt="Smart STB" style="height:40px; object-fit:contain; margin-bottom:0.35rem;" />
              <div style="color:#fff; font-size:0.85rem; font-weight:700;">Smart STB</div>
              <span style="font-size:0.72rem; color:var(--primary);">Portal Emulation</span>
            </div>
          </div>
        </div>
      </div>
"""
    if "Supported Australian Hardware" not in s_html:
        s_html = s_html.replace('<!-- Detailed DNS Optimization Guide -->', device_showcase + '\n      <!-- Detailed DNS Optimization Guide -->', 1)
        with open(setup_path, "w", encoding="utf-8") as f:
            f.write(s_html)
        print("Updated setup.html with devices and app showcase!")

# =========================================================================
# 2. UPGRADE CHANNELS.HTML
# =========================================================================
channels_path = os.path.join(base_dir, "channels.html")
if os.path.exists(channels_path):
    with open(channels_path, "r", encoding="utf-8") as f:
        c_html = f.read()

    sports_visuals = """
      <!-- Australian Sports Stadium & Broadcast Showcase -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem; margin-bottom:3rem;">
        <div class="glass-card" style="border-color:var(--border-gold);">
          <div style="position:relative; border-radius:var(--radius-sm); overflow:hidden; margin-bottom:1rem; border:1px solid var(--border-gold);">
            <img src="images/afl-nrl-stadium.webp" alt="AFL MCG Stadium" style="width:100%; height:160px; object-fit:cover; display:block;" />
            <div style="position:absolute; bottom:6px; left:8px; background:rgba(0,0,0,0.8); padding:0.2rem 0.6rem; border-radius:4px; font-size:0.75rem; color:var(--aus-gold); font-weight:700;">
              Fox Footy 504 4K • 7HD
            </div>
          </div>
          <h3 style="color:#fff; font-size:1.25rem; margin-bottom:0.5rem;"><i class="fa-solid fa-football" style="color:var(--aus-gold); margin-right:0.4rem;"></i> AFL Premiership & Grand Final</h3>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">All 9 matches each round live and commercial-free in true 4K 60FPS from the MCG, Marvel Stadium, Adelaide Oval, and Optus Stadium.</p>
          <a href="sports/afl-live-stream-iptv/index.html" class="btn btn-gold btn-sm btn-block">AFL 4K Hub →</a>
        </div>

        <div class="glass-card" style="border-color:var(--border-mauve);">
          <div style="position:relative; border-radius:var(--radius-sm); overflow:hidden; margin-bottom:1rem; border:1px solid var(--border-color);">
            <img src="images/packimages2/lucid-origin_Epic_night_football_scene_from_low_angle_a_player_striking_the_ball_under_bright-0.webp" alt="NRL Stadium Action" style="width:100%; height:160px; object-fit:cover; display:block;" />
            <div style="position:absolute; bottom:6px; left:8px; background:rgba(0,0,0,0.8); padding:0.2rem 0.6rem; border-radius:4px; font-size:0.75rem; color:var(--primary); font-weight:700;">
              Fox League 502 4K • 9HD
            </div>
          </div>
          <h3 style="color:#fff; font-size:1.25rem; margin-bottom:0.5rem;"><i class="fa-solid fa-shield-halved" style="color:var(--primary); margin-right:0.4rem;"></i> NRL Telstra & State of Origin</h3>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">Every tackle live: Thursday Night, Super Saturday, Sunday Ticket, Magic Round Brisbane, and State of Origin I-III in Ultra HD.</p>
          <a href="sports/nrl-live-stream-iptv/index.html" class="btn btn-primary btn-sm btn-block">NRL 4K Hub →</a>
        </div>

        <div class="glass-card">
          <div style="position:relative; border-radius:var(--radius-sm); overflow:hidden; margin-bottom:1rem; border:1px solid var(--border-color);">
            <img src="images/cricket-ashes.webp" alt="Cricket Australia" style="width:100%; height:160px; object-fit:cover; display:block;" />
            <div style="position:absolute; bottom:6px; left:8px; background:rgba(0,0,0,0.8); padding:0.2rem 0.6rem; border-radius:4px; font-size:0.75rem; color:var(--aus-green); font-weight:700;">
              Fox Cricket 501 • BBL • Ashes
            </div>
          </div>
          <h3 style="color:#fff; font-size:1.25rem; margin-bottom:0.5rem;"><i class="fa-solid fa-baseball-bat-ball" style="color:var(--secondary); margin-right:0.4rem;"></i> Cricket Australia & The Ashes</h3>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">Boxing Day Test MCG, New Year's Test SCG, Border-Gavaskar Trophy, and every BBL & WBBL Big Bash match in crisp 4K.</p>
          <a href="sports/cricket-australia-live-iptv/index.html" class="btn btn-outline btn-sm btn-block">Cricket Hub →</a>
        </div>
      </div>

      <!-- EPL, F1, Combat Sports Row -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem; margin-bottom:3rem;">
        <div class="glass-card">
          <div style="position:relative; border-radius:var(--radius-sm); overflow:hidden; margin-bottom:0.75rem;">
            <img src="images/premier-league-soccer.webp" alt="Premier League Football" style="width:100%; height:130px; object-fit:cover; display:block;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;"><i class="fa-solid fa-futbol" style="color:var(--secondary); margin-right:0.4rem;"></i> English Premier League</h4>
          <p style="font-size:0.82rem; color:var(--text-muted);">All 380 games via Optus Sport 1-6 & TNT Sports UK 4K with no Australian buffering.</p>
        </div>

        <div class="glass-card">
          <div style="position:relative; border-radius:var(--radius-sm); overflow:hidden; margin-bottom:0.75rem;">
            <img src="images/formula-1-aus.webp" alt="Formula 1 Australian GP" style="width:100%; height:130px; object-fit:cover; display:block;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;"><i class="fa-solid fa-flag-checkered" style="color:var(--aus-gold); margin-right:0.4rem;"></i> Formula 1 & Bathurst 1000</h4>
          <p style="font-size:0.82rem; color:var(--text-muted);">Australian Grand Prix Albert Park Melbourne in 4K 50FPS + Supercars Repco Bathurst 1000.</p>
        </div>

        <div class="glass-card">
          <div style="position:relative; border-radius:var(--radius-sm); overflow:hidden; margin-bottom:0.75rem;">
            <img src="images/ufc-boxing-main-event.webp" alt="UFC PPV Main Event" style="width:100%; height:130px; object-fit:cover; display:block;" />
          </div>
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.35rem;"><i class="fa-solid fa-hand-back-fist" style="color:var(--primary); margin-right:0.4rem;"></i> UFC & Boxing PPV Main Event</h4>
          <p style="font-size:0.82rem; color:var(--text-muted);">All numbered UFC cards and world title fights included free on dedicated Main Event channels.</p>
        </div>
      </div>
"""
    if "Australian Sports Stadium & Broadcast Showcase" not in c_html:
        # Insert before the channel table
        c_html = c_html.replace('<div class="glass-card" style="margin-bottom:3rem;">', sports_visuals + '\n      <div class="glass-card" style="margin-bottom:3rem;">', 1)
        with open(channels_path, "w", encoding="utf-8") as f:
            f.write(c_html)
        print("Updated channels.html with sports action images!")

# =========================================================================
# 3. UPGRADE RESELLER.HTML
# =========================================================================
reseller_path = os.path.join(base_dir, "reseller.html")
if os.path.exists(reseller_path):
    with open(reseller_path, "r", encoding="utf-8") as f:
        r_html = f.read()

    reseller_visuals = """
      <!-- Reseller Dashboard Preview Banner -->
      <div style="margin-bottom:3.5rem; text-align:center;">
        <div style="position:relative; border-radius:var(--radius-md); overflow:hidden; border:1px solid var(--border-gold); display:inline-block; max-width:100%; box-shadow:0 12px 35px rgba(0,0,0,0.6);">
          <img src="images/apps-dashboard.webp" alt="Xtream UI Reseller Dashboard Interface" style="width:100%; max-height:360px; object-fit:cover; display:block;" />
          <div style="position:absolute; bottom:12px; left:16px; background:rgba(10,6,20,0.9); padding:0.4rem 1.2rem; border-radius:var(--radius-sm); border:1px solid var(--border-gold);">
            <span style="color:var(--aus-gold); font-weight:800; font-size:1.05rem;">Xtream UI & ZapX Panel</span> • Manage Australian Clients & Sub-Resellers in AUD
          </div>
        </div>
      </div>
"""
    if "Xtream UI Reseller Dashboard Interface" not in r_html:
        r_html = r_html.replace('<div class="glass-card" style="margin-bottom:3rem; border-color:var(--border-gold);">', reseller_visuals + '\n      <div class="glass-card" style="margin-bottom:3rem; border-color:var(--border-gold);">', 1)
        with open(reseller_path, "w", encoding="utf-8") as f:
            f.write(r_html)
        print("Updated reseller.html with dashboard banner!")

print("All subpages updated with rich visuals successfully!")

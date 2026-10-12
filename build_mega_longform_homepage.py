import os, sys, re, json, html

BASE_DIR = r"c:\Users\clanm\OneDrive\Desktop\australiatv"
index_path = os.path.join(BASE_DIR, "index.html")

from seo_engine_init import (
    cities_list, sports_list, devices_list, competitors_list,
    isps_list, languages_list, guides_list, parsed_kws
)
from seo_page_renderer import slugify

print("Crafting Ultra Long-Form Australian IPTV Powerhouse Homepage...")

# Read existing index.html
with open(index_path, "r", encoding="utf-8") as f:
    existing_html = f.read()

# Generate city link pills
city_pills = []
for c, s, _ in cities_list:
    c_slug = slugify(c)
    city_pills.append(f'<a href="cities/{c_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-location-dot" style="color:var(--primary); font-size:0.75rem;"></i> {c}, {s}</a>')
city_pills_html = '\n'.join(city_pills)

# Generate sports link pills
sports_pills = []
for s_slug, s_title, _, s_name, _ in sports_list:
    sports_pills.append(f'<a href="sports/{s_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-play" style="color:var(--aus-gold); font-size:0.75rem;"></i> {s_name}</a>')
sports_pills_html = '\n'.join(sports_pills)

# Generate devices link pills
devices_pills = []
for d_slug, d_title, _, d_name, _ in devices_list:
    devices_pills.append(f'<a href="devices/{d_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-tv" style="color:var(--secondary); font-size:0.75rem;"></i> {d_name}</a>')
devices_pills_html = '\n'.join(devices_pills)

# Generate competitor comparison pills
comp_pills = []
for c_slug, c_title, _, c_name, _ in competitors_list:
    comp_pills.append(f'<a href="comparisons/{c_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-scale-balanced" style="color:var(--primary); font-size:0.75rem;"></i> {c_name}</a>')
comp_pills_html = '\n'.join(comp_pills)

# Generate languages pills
lang_pills = []
for l_slug, l_title, _, l_name, _ in languages_list:
    lang_pills.append(f'<a href="languages/{l_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-globe-oceania" style="color:var(--aus-gold); font-size:0.75rem;"></i> {l_name} TV</a>')
lang_pills_html = '\n'.join(lang_pills)

# Generate top search volume pills
top_kws = sorted([p for p in parsed_kws if len(p['keyword']) > 3], key=lambda x: x['volume'], reverse=True)[:80]
top_kw_pills = []
for k in top_kws:
    slug = slugify(k['keyword'])
    top_kw_pills.append(f'<a href="topic/{slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-bolt" style="color:var(--primary); font-size:0.72rem;"></i> {k["keyword"].title()} <span style="color:var(--text-dim);">({k["volume"]:,}/mo)</span></a>')
top_kw_pills_html = '\n'.join(top_kw_pills)

# Build the Mega Long-Form Content Extension
mega_extension_html = f"""
  <!-- ==================== ULTRA LONG-FORM AUSTRALIAN IPTV AUTHORITY & CONVERSION SUITE ==================== -->
  
  <!-- SECTION A: COMPLETE AUSTRALIAN FREE-TO-AIR & PAY-TV CHANNEL DIRECTORY -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5rem 0;" id="aussie-channel-guide">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-tv"></i> Complete Australian TV Lineup</span>
        <h2 class="section-title">50,000+ Channels Including Every Australian Free-to-Air & Pay-TV Network</h2>
        <p class="section-subtitle">Stream local Sydney, Melbourne, Brisbane, Perth, and Adelaide broadcast feeds with 7-day electronic program guide (EPG) and catch-up TV.</p>
      </div>

      <div class="glass-card" style="margin-bottom:3rem;">
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.92rem;">
            <thead>
              <tr style="border-bottom:2px solid var(--border-color); color:var(--primary);">
                <th style="padding:1rem;">Channel Category</th>
                <th style="padding:1rem;">Included Australian Channels</th>
                <th style="padding:1rem;">Resolution</th>
                <th style="padding:1rem;">EPG Guide</th>
                <th style="padding:1rem;">Catch-Up TV</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">
                  <i class="fa-solid fa-football" style="color:var(--aus-gold); margin-right:0.4rem;"></i> Premium Australian Sports
                </td>
                <td style="padding:1.1rem;">Fox Footy 504, Fox League 502, Fox Cricket 501, Fox Sports 503/505/506, Stan Sport 1-4, Optus Sport 1-6, Main Event PPV, ESPN 1 & 2 HD, beIN Sports 1-3</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">4K UHD & 1080p 60FPS</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> 7 Days Active</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> 7 Days DVR</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">
                  <i class="fa-solid fa-tower-broadcast" style="color:var(--primary); margin-right:0.4rem;"></i> Free-To-Air (FTA) HD Feeds
                </td>
                <td style="padding:1.1rem;">Channel 7 HD (7mate, 7two, 7flix), Channel 9 HD (9Gem, 9Go!, 9Life), Channel 10 HD (10Bold, 10Peach), ABC HD, ABC Kids, ABC News 24, SBS ONE HD, SBS VICELAND, NITV</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">1080p Full HD</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> 7 Days Active</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> 7 Days DVR</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">
                  <i class="fa-solid fa-film" style="color:var(--secondary); margin-right:0.4rem;"></i> Foxtel Drama & Entertainment
                </td>
                <td style="padding:1.1rem;">Showcase 4K (HBO Dramas), Fox8 HD (WWE & Sitcoms), Arena, LifeStyle, Discovery AU, History AU, Crime + Investigation, BBC UKTV, MTV Australia, National Geographic</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">4K UHD & 1080p</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> 7 Days Active</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> 7 Days DVR</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">
                  <i class="fa-solid fa-clapperboard" style="color:var(--primary); margin-right:0.4rem;"></i> 24/7 Aussie Movie Channels
                </td>
                <td style="padding:1.1rem;">Foxtel Movies Premiere, Movies Action, Movies Comedy, Movies Family, Movies Thriller, Movies Greats, Stan & Binge 4K on-demand cinema feeds</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">4K UHD HDR</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> 7 Days Active</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> On-Demand</td>
              </tr>
              <tr>
                <td style="padding:1.1rem; font-weight:700; color:#fff;">
                  <i class="fa-solid fa-globe" style="color:var(--aus-gold); margin-right:0.4rem;"></i> International & Expat Channels
                </td>
                <td style="padding:1.1rem;">UK BBC & Sky Sports, USA NBC/CBS/FOX/ESPN, New Zealand Sky Sport 1-9, Indian Star/Zee/Sony, Arabic MBC/Shahid, Greek ERT/ANT1, Italian Rai/Mediaset</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">4K & 1080p</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> Global EPG</td>
                <td style="padding:1.1rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> 14 Days</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION B: AFL & NRL 4K STREAMING DEEP-DIVE -->
  <section class="section-padding-lg" style="background:var(--bg-main); padding: 5rem 0;" id="aussie-footy-hub">
    <div class="container">
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:center;">
        <div>
          <span class="badge badge-glow-gold" style="margin-bottom:0.75rem;"><i class="fa-solid fa-football"></i> Unrivalled Australian Sports</span>
          <h2 style="font-size:2.2rem; color:#fff; line-height:1.2; margin-bottom:1.25rem;">Watch Every AFL & NRL Round Live in True 4K 60FPS Without Blackouts</h2>
          <p style="color:var(--text-muted); line-height:1.75; font-size:1rem; margin-bottom:1.25rem;">
            Forget 720p compressed streams, delayed live feeds, or frustrating regional blackouts. Our dedicated Australian sports server network streams directly from high-bitrate stadium broadcast lines.
          </p>
          <ul style="list-style:none; display:flex; flex-direction:column; gap:0.75rem; color:var(--text-muted); font-size:0.95rem; margin-bottom:2rem;">
            <li><i class="fa-solid fa-circle-check" style="color:var(--aus-gold); margin-right:0.5rem;"></i> <strong>AFL Premiership:</strong> All 9 weekly matches live on Fox Footy 504 and Channel 7HD through to the MCG Grand Final.</li>
            <li><i class="fa-solid fa-circle-check" style="color:var(--primary); margin-right:0.5rem;"></i> <strong>NRL Telstra Premiership:</strong> Thursday Night Footy, Friday doubleheaders, Super Saturday, Sunday NRL, and State of Origin I-III.</li>
            <li><i class="fa-solid fa-circle-check" style="color:var(--secondary); margin-right:0.5rem;"></i> <strong>Cricket Australia & The Ashes:</strong> Border-Gavaskar Trophy, Test matches, ODI, and BBL Big Bash League.</li>
            <li><i class="fa-solid fa-circle-check" style="color:var(--primary); margin-right:0.5rem;"></i> <strong>UFC & Boxing Main Event PPVs:</strong> Full numbered UFC cards and international boxing included free.</li>
          </ul>

          <div style="display:flex; gap:1rem; flex-wrap:wrap;">
            <button class="btn btn-gold btn-lg" data-open-modal="trial"><i class="fa-solid fa-play"></i> Watch Footy Free Trial</button>
            <a href="sports/afl-live-stream-iptv/index.html" class="btn btn-outline btn-lg"><i class="fa-solid fa-football"></i> AFL Hub</a>
            <a href="sports/nrl-live-stream-iptv/index.html" class="btn btn-outline btn-lg"><i class="fa-solid fa-shield"></i> NRL Hub</a>
          </div>
        </div>

        <div class="glass-card" style="padding:2.5rem; border-color:var(--border-gold);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; border-bottom:1px solid var(--border-color); padding-bottom:1rem;">
            <h3 style="font-size:1.3rem; color:#fff; margin:0;"><i class="fa-solid fa-satellite-dish" style="color:var(--aus-gold); margin-right:0.5rem;"></i> 2026 Sports Broadcast Spec</h3>
            <span class="badge badge-glow-gold">4K 60FPS</span>
          </div>

          <div style="display:flex; flex-direction:column; gap:1.25rem;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="color:var(--text-muted); font-size:0.95rem;">Video Frame Rate</span>
              <strong style="color:#fff; font-family:var(--font-mono);">60 Frames Per Second</strong>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="color:var(--text-muted); font-size:0.95rem;">Video Bitrate</span>
              <strong style="color:var(--secondary); font-family:var(--font-mono);">25 Mbps - 40 Mbps (Uncompressed)</strong>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="color:var(--text-muted); font-size:0.95rem;">Audio Commentary</span>
              <strong style="color:#fff; font-family:var(--font-mono);">Dolby Digital 5.1 Surround</strong>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="color:var(--text-muted); font-size:0.95rem;">Stream Delay</span>
              <strong style="color:var(--primary); font-family:var(--font-mono);">&lt; 3 Seconds from Satellite</strong>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="color:var(--text-muted); font-size:0.95rem;">Australian CDN Latency</span>
              <strong style="color:var(--aus-gold); font-family:var(--font-mono);">Sydney 8ms | Melbourne 12ms</strong>
            </div>
          </div>

          <div style="margin-top:2rem; padding:1rem; background:rgba(0,0,0,0.35); border-radius:var(--radius-md); text-align:center;">
            <p style="font-size:0.85rem; color:var(--text-dim); margin:0;">
              <i class="fa-solid fa-circle-check" style="color:var(--secondary);"></i> Compatible with TiviMate, IPTV Smarters Pro, Apple TV, and Firestick 4K.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION C: 15+ AUSTRALIAN IPTV PROVIDERS BENCHMARK MATRIX -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5rem 0;" id="provider-dossiers">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-list-check"></i> Benchmark Directory</span>
        <h2 class="section-title">Tested & Audited Australian IPTV Providers (2026 Ratings)</h2>
        <p class="section-subtitle">We rigorously evaluate streaming stability, local Australian CDN peering, VOD library depth, and reseller panel wholesale rates across all top services.</p>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem;">
        <!-- Card 1 -->
        <div class="glass-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
              <h3 style="font-size:1.35rem; color:#fff; margin:0;"><i class="fa-solid fa-dragon" style="color:var(--aus-gold); margin-right:0.4rem;"></i> Trex IPTV AU</h3>
              <span class="badge badge-glow-gold">4.95/5 #1</span>
            </div>
            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
              #1 rated for Australian sports. Features 51,000+ channels, 200,000+ VOD titles, dedicated AFL 4K channels, Fox League, and Stan Sport with 8ms Sydney server latency.
            </p>
            <ul style="list-style:none; font-size:0.82rem; color:var(--text-dim); display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.25rem;">
              <li>• Retail Price: <strong>$16 AUD / month</strong></li>
              <li>• Wholesale Credit: <strong>$4.50 AUD / credit</strong></li>
              <li>• Anti-Freeze: <strong>v9.4 Built-in</strong></li>
            </ul>
          </div>
          <button class="btn btn-gold btn-sm btn-block" data-open-modal="trial">Get Trex AU Trial</button>
        </div>

        <!-- Card 2 -->
        <div class="glass-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
              <h3 style="font-size:1.35rem; color:#fff; margin:0;"><i class="fa-solid fa-gem" style="color:var(--primary); margin-right:0.4rem;"></i> Ultra 8K IPTV AU</h3>
              <span class="badge badge-glow-cyan">4.90/5</span>
            </div>
            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
              Pristine picture quality engineered for OLED and QLED large screens. High-bitrate 8K & 4K 60FPS feeds of Fox Sports, ESPN, and latest cinema blockbusters.
            </p>
            <ul style="list-style:none; font-size:0.82rem; color:var(--text-dim); display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.25rem;">
              <li>• Retail Price: <strong>$18 AUD / month</strong></li>
              <li>• Wholesale Credit: <strong>$5.00 AUD / credit</strong></li>
              <li>• Multi-Screen: <strong>Up to 4 devices</strong></li>
            </ul>
          </div>
          <button class="btn btn-primary btn-sm btn-block" data-open-modal="trial">Get Ultra 8K Trial</button>
        </div>

        <!-- Card 3 -->
        <div class="glass-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
              <h3 style="font-size:1.35rem; color:#fff; margin:0;"><i class="fa-solid fa-globe-oceania" style="color:var(--secondary); margin-right:0.4rem;"></i> 5GLive Australia</h3>
              <span class="badge badge-glow-green">4.85/5</span>
            </div>
            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
              Champion provider for multicultural communities across Sydney and Melbourne. Largest Indian (Hindi/Tamil/Punjabi), Arabic, Greek, and Italian channel selection in Australia.
            </p>
            <ul style="list-style:none; font-size:0.82rem; color:var(--text-dim); display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.25rem;">
              <li>• Retail Price: <strong>$15 AUD / month</strong></li>
              <li>• Wholesale Credit: <strong>$4.00 AUD / credit</strong></li>
              <li>• Cricket IPL: <strong>All Feeds 4K</strong></li>
            </ul>
          </div>
          <button class="btn btn-primary btn-sm btn-block" data-open-modal="trial">Get 5GLive AU Trial</button>
        </div>

        <!-- Card 4 -->
        <div class="glass-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
              <h3 style="font-size:1.35rem; color:#fff; margin:0;"><i class="fa-solid fa-microchip" style="color:var(--primary); margin-right:0.4rem;"></i> Smarter8K AU</h3>
              <span class="badge badge-glow-cyan">4.75/5</span>
            </div>
            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
              App-optimized streaming platform tailored for Firestick and Smart TV apps. 45,000+ live channels with automated EPG synchronization and instant channel zap.
            </p>
            <ul style="list-style:none; font-size:0.82rem; color:var(--text-dim); display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.25rem;">
              <li>• Retail Price: <strong>$15 AUD / month</strong></li>
              <li>• Wholesale Credit: <strong>$3.80 AUD / credit</strong></li>
              <li>• NBN Peering: <strong>Brisbane & Sydney</strong></li>
            </ul>
          </div>
          <button class="btn btn-outline btn-sm btn-block" data-open-modal="trial">Get Smarter8K Trial</button>
        </div>

        <!-- Card 5 -->
        <div class="glass-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
              <h3 style="font-size:1.35rem; color:#fff; margin:0;"><i class="fa-solid fa-network-wired" style="color:var(--aus-gold); margin-right:0.4rem;"></i> MegaOTT AU</h3>
              <span class="badge badge-glow-gold">4.70/5</span>
            </div>
            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
              Complete OTT streaming solution with dedicated Android and TV apps, 150,000+ VOD titles, and a 7-day money-back guarantee. Reliable Australian reseller infrastructure.
            </p>
            <ul style="list-style:none; font-size:0.82rem; color:var(--text-dim); display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.25rem;">
              <li>• Retail Price: <strong>$14 AUD / month</strong></li>
              <li>• Wholesale Credit: <strong>$3.50 AUD / credit</strong></li>
              <li>• Guarantee: <strong>7-Day Money-Back</strong></li>
            </ul>
          </div>
          <button class="btn btn-outline btn-sm btn-block" data-open-modal="trial">Get MegaOTT Trial</button>
        </div>

        <!-- Card 6 -->
        <div class="glass-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
              <h3 style="font-size:1.35rem; color:#fff; margin:0;"><i class="fa-solid fa-shield-halved" style="color:var(--secondary); margin-right:0.4rem;"></i> Cyber IPTV AU</h3>
              <span class="badge badge-glow-green">4.80/5</span>
            </div>
            <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
              Engineered for maximum security and privacy on Australian broadband networks. Built-in VPN compatibility, 110+ secure servers, and military-grade anti-freeze technology.
            </p>
            <ul style="list-style:none; font-size:0.82rem; color:var(--text-dim); display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.25rem;">
              <li>• Retail Price: <strong>$15 AUD / month</strong></li>
              <li>• Wholesale Credit: <strong>$3.80 AUD / credit</strong></li>
              <li>• VPN Friendly: <strong>100% Compatible</strong></li>
            </ul>
          </div>
          <button class="btn btn-outline btn-sm btn-block" data-open-modal="trial">Get Cyber AU Trial</button>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION D: AUSTRALIAN GEOGRAPHIC & CITIES COVERAGE ENCYCLOPEDIA -->
  <section class="section-padding-lg" style="background:var(--bg-main); padding: 5rem 0;" id="australian-cities-encyclopedia">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-map-location-dot"></i> Nationwide Australian Footprint</span>
        <h2 class="section-title">Serving All Australian States, Capital Cities & Regional Towns</h2>
        <p class="section-subtitle">Local CDN nodes ensure buffer-free 4K sports streaming whether you live in downtown Sydney, Melbourne, Brisbane, Perth, or regional Australia.</p>
      </div>

      <div class="glass-card" style="margin-bottom:2.5rem;">
        <h3 style="font-size:1.3rem; margin-bottom:1rem; color:#fff;"><i class="fa-solid fa-location-dot" style="color:var(--primary); margin-right:0.5rem;"></i> Browse All Australian City Hubs:</h3>
        <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
          {city_pills_html}
        </div>
      </div>

      <!-- State by State Breakdown Grid -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.5rem;">
        <div class="glass-card">
          <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:0.6rem;"><i class="fa-solid fa-building"></i> New South Wales (NSW)</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:0.75rem;">
            Sydney CBD, Western Sydney (Parramatta, Penrith, Blacktown), Eastern Suburbs (Bondi, Coogee), Northern Beaches (Manly), Cronulla, Newcastle, Wollongong, Central Coast, and Albury.
          </p>
          <a href="cities/sydney/index.html" style="font-size:0.85rem; color:var(--primary); font-weight:700;">Explore NSW IPTV Hubs →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:var(--aus-gold); font-size:1.15rem; margin-bottom:0.6rem;"><i class="fa-solid fa-building"></i> Victoria (VIC)</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:0.75rem;">
            Melbourne CBD, St Kilda, Richmond, South Yarra, Footscray, Dandenong, Frankston, Werribee, Geelong, Ballarat, Bendigo, Shepparton, Mildura, and Warrnambool.
          </p>
          <a href="cities/melbourne/index.html" style="font-size:0.85rem; color:var(--aus-gold); font-weight:700;">Explore VIC IPTV Hubs →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:var(--secondary); font-size:1.15rem; margin-bottom:0.6rem;"><i class="fa-solid fa-building"></i> Queensland (QLD)</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:0.75rem;">
            Brisbane CBD, Fortitude Valley, Chermside, Gold Coast (Surfers Paradise, Broadbeach, Robina), Sunshine Coast (Maroochydore, Noosa), Townsville, Cairns, Mackay, and Rockhampton.
          </p>
          <a href="cities/brisbane/index.html" style="font-size:0.85rem; color:var(--secondary); font-weight:700;">Explore QLD IPTV Hubs →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION E: STEP-BY-STEP DEVICE SETUP CENTER -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5rem 0;" id="device-setup-center">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-wrench"></i> Easy Setup Guides</span>
        <h2 class="section-title">How to Install IPTV in Under 5 Minutes on Any Device</h2>
        <p class="section-subtitle">Select your device below to view our verified Australian step-by-step installation tutorials.</p>
      </div>

      <div class="glass-card" style="margin-bottom:2.5rem;">
        <h3 style="font-size:1.3rem; margin-bottom:1rem; color:#fff;"><i class="fa-solid fa-tv" style="color:var(--primary); margin-right:0.5rem;"></i> Select Your Streaming Hardware:</h3>
        <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
          {devices_pills_html}
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem;">
        <div class="glass-card">
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.75rem;"><i class="fa-brands fa-amazon" style="color:var(--aus-gold); margin-right:0.4rem;"></i> Amazon Firestick 4K Max</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
            1. Install Downloader from Fire TV Store.<br/>
            2. Enable 'Install Unknown Apps'.<br/>
            3. Download TiviMate or IPTV Smarters Pro.<br/>
            4. Enter Xtream Codes and stream in 4K!
          </p>
          <a href="devices/iptv-on-amazon-firestick-australia/index.html" style="color:var(--primary); font-size:0.85rem; font-weight:700;">Read Full Firestick Guide →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.75rem;"><i class="fa-solid fa-tv" style="color:var(--primary); margin-right:0.4rem;"></i> Samsung & LG Smart TVs</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
            1. Open Samsung Apps or LG Content Store.<br/>
            2. Search and download IBO Player or Smart IPTV.<br/>
            3. Note your Device ID and Key.<br/>
            4. Activate M3U playlist or send to our WhatsApp desk!
          </p>
          <a href="devices/iptv-on-samsung-smart-tv-tizen-australia/index.html" style="color:var(--primary); font-size:0.85rem; font-weight:700;">Read Smart TV Guide →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:#fff; font-size:1.15rem; margin-bottom:0.75rem;"><i class="fa-brands fa-apple" style="color:var(--secondary); margin-right:0.4rem;"></i> Apple TV 4K & iOS</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
            1. Open App Store on Apple TV.<br/>
            2. Install iPlayTV, UHF Player, or IPTVX.<br/>
            3. Add Playlist via Xtream Codes API.<br/>
            4. Automatic EPG TV guide sync!
          </p>
          <a href="devices/iptv-on-apple-tv-tvos-australia/index.html" style="color:var(--primary); font-size:0.85rem; font-weight:700;">Read Apple TV Guide →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION F: AUSTRALIAN BROADBAND & NBN DNS ANTI-THROTTLING PROTOCOL -->
  <section class="section-padding-lg" style="background:var(--bg-main); padding: 5rem 0;" id="nbn-dns-hub">
    <div class="container">
      <div class="glass-card" style="border-color:var(--border-gold);">
        <span class="badge badge-glow-gold" style="margin-bottom:0.75rem;"><i class="fa-solid fa-shield-virus"></i> NBN Network Optimization</span>
        <h2 style="font-size:2rem; color:#fff; margin-bottom:1rem;">Eliminating ISP Video Throttling on Telstra, Optus & TPG Broadband</h2>
        <div style="color:var(--text-muted); line-height:1.8; font-size:0.95rem; margin-bottom:1.5rem;">
          <p style="margin-bottom:1rem;">
            During peak Australian evening sports hours (Friday night footy, Saturday AFL/NRL, Sunday evening Premier League), major Australian retail service providers (RSPs)—notably <strong>Telstra, Optus, TPG, iiNet, and Vodafone</strong>—manage CVC network congestion by aggressively throttling transparent DNS lookups on video streaming packets.
          </p>
          <p style="margin-bottom:1.5rem;">
            By switching your device or modem DNS from your ISP default to <strong>Cloudflare Anycast (1.1.1.1)</strong> or <strong>Google Public DNS (8.8.8.8)</strong>, you completely bypass ISP transparent proxy caching. DNS queries are resolved directly via Sydney and Melbourne edge nodes with sub-5ms response times, eliminating video stuttering and buffering.
          </p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:1.5rem; background:rgba(0,0,0,0.4); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
          <div>
            <h4 style="color:var(--primary); margin-bottom:0.4rem;"><i class="fa-solid fa-cloud"></i> Cloudflare Fast DNS (Sydney / Melbourne)</h4>
            <p style="font-size:0.9rem; color:#fff; font-family:var(--font-mono); margin-bottom:0.4rem;">Primary DNS: 1.1.1.1 | Secondary DNS: 1.0.0.1</p>
            <span style="font-size:0.82rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> Recommended for all metro Sydney, Melbourne, Brisbane & Perth NBN users.</span>
          </div>
          <div>
            <h4 style="color:var(--aus-gold); margin-bottom:0.4rem;"><i class="fa-brands fa-google"></i> Google Anycast DNS (Regional & Starlink)</h4>
            <p style="font-size:0.9rem; color:#fff; font-family:var(--font-mono); margin-bottom:0.4rem;">Primary DNS: 8.8.8.8 | Secondary DNS: 8.8.4.4</p>
            <span style="font-size:0.82rem; color:var(--secondary);"><i class="fa-solid fa-check"></i> Recommended for regional WA, regional QLD, NSW country, and Starlink users.</span>
          </div>
        </div>

        <div style="margin-top:1.5rem;">
          <a href="guides/how-to-fix-iptv-buffering-australia/index.html" class="btn btn-primary btn-lg"><i class="fa-solid fa-wrench"></i> View Step-by-Step DNS Guide</a>
          <a href="isps/telstra-nbn-iptv-anti-freeze-guide/index.html" class="btn btn-outline btn-lg" style="margin-left:0.75rem;"><i class="fa-solid fa-network-wired"></i> Telstra NBN Guide</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION G: MULTICULTURAL EXPAT TELEVISION IN AUSTRALIA -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5rem 0;" id="multicultural-tv-hub">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-globe-oceania"></i> Australian Multicultural TV</span>
        <h2 class="section-title">Stay Connected to Home with 65+ International Language Packs</h2>
        <p class="section-subtitle">Extensive channel packages for Indian, Arabic, Greek, Italian, Vietnamese, Filipino, and Chinese communities across Sydney, Melbourne, Brisbane, and Perth.</p>
      </div>

      <div class="glass-card" style="margin-bottom:2.5rem;">
        <h3 style="font-size:1.3rem; margin-bottom:1rem; color:#fff;"><i class="fa-solid fa-language" style="color:var(--aus-gold); margin-right:0.5rem;"></i> Featured International Communities:</h3>
        <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
          {lang_pills_html}
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.25rem;">
        <div class="glass-card">
          <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.5rem;">🇮🇳 Indian & Hindi TV</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">Star Plus, Zee TV, Sony, Colors, Aaj Tak, NDTV, Star Sports Hindi, IPL live in 4K.</p>
          <a href="languages/indian-hindi-tv-channels-iptv-australia/index.html" style="font-size:0.82rem; color:var(--primary); font-weight:700;">Explore Indian TV →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.5rem;">🇱🇧 Arabic & Lebanese TV</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">MBC 1-4, Shahid VIP, MTV Lebanon, LBCI, Al Jadeed, beIN Sports Arabic 4K.</p>
          <a href="languages/arabic-lebanese-iptv-australia/index.html" style="font-size:0.82rem; color:var(--aus-gold); font-weight:700;">Explore Arabic TV →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.5rem;">🇬🇷 Greek TV Australia</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">ERT World, Mega Cosmos, ANT1 Pacific, Alpha TV, Star International, Greek Super League.</p>
          <a href="languages/greek-tv-channels-iptv-australia/index.html" style="font-size:0.82rem; color:var(--secondary); font-weight:700;">Explore Greek TV →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:#fff; font-size:1.1rem; margin-bottom:0.5rem;">🇮🇹 Italian TV Australia</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">Rai 1, Rai 2, Rai 3, Mediaset Canale 5, Italia 1, Sky Sport Serie A live.</p>
          <a href="languages/italian-tv-channels-iptv-australia/index.html" style="font-size:0.82rem; color:var(--primary); font-weight:700;">Explore Italian TV →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION H: MASTER AUSTRALIAN KEYWORDS DIRECTORY INDEX (97,000+ DATASET) -->
  <section class="section-padding-lg" style="background:var(--bg-main); padding: 5rem 0;" id="mega-keyword-index">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-database"></i> Search Engine Index</span>
        <h2 class="section-title">Australian IPTV Streaming & Reseller Directory Index</h2>
        <p class="section-subtitle">Search terms and topics indexed from our comprehensive 97,000+ Australian keyword dataset.</p>
      </div>

      <div class="glass-card" style="margin-bottom:3rem;">
        <h3 style="font-size:1.3rem; margin-bottom:1rem; color:#fff;"><i class="fa-solid fa-magnifying-glass" style="color:var(--primary); margin-right:0.5rem;"></i> Indexed Australian Search Clusters:</h3>
        <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
          {top_kw_pills_html}
        </div>
      </div>

      <div style="text-align:center;">
        <a href="directory/index.html" class="btn btn-primary btn-xl"><i class="fa-solid fa-compass"></i> Open Full 2,000+ Page Programmatic Directory</a>
      </div>
    </div>
  </section>
"""

# Inject before the existing seo-knowledge-hub section or before footer
if '<section class="section-padding-lg" style="background:var(--bg-main); border-top:1px solid var(--border-color); padding: 5rem 0;" id="australia-iptv-master-guide">' in existing_html:
    # Replace existing master guide section with the comprehensive version
    pattern = re.compile(r'<section class="section-padding-lg" style="background:var\(--bg-main\); border-top:1px solid var\(--border-color\); padding: 5rem 0;" id="australia-iptv-master-guide">.*?</section>', re.DOTALL)
    updated_html = pattern.sub(mega_extension_html.strip(), existing_html)
else:
    # Insert before the footer
    updated_html = existing_html.replace("<!-- ==================== 12. FOOTER ==================== -->", mega_extension_html + "\n  <!-- ==================== 12. FOOTER ==================== -->")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(updated_html)

print("SUCCESS: Homepage index.html has been expanded into an ultra-long, keyword-dense, high-converting masterpiece!")

import os, sys, re, json, html
from seo_engine_init import (
    cities_list, sports_list, devices_list, competitors_list,
    isps_list, languages_list, guides_list, parsed_kws
)
from seo_page_renderer import slugify

BASE_DIR = r"c:\Users\clanm\OneDrive\Desktop\australiatv"
index_path = os.path.join(BASE_DIR, "index.html")

print("Crafting Ultra Long-Form Australian IPTV Powerhouse Homepage with Mega Expansion...")

# Build rich keyword pills from parsed_kws
top_kws = sorted([p for p in parsed_kws if len(p['keyword']) > 3], key=lambda x: x['volume'], reverse=True)

# Group top keywords by categories for the keyword cloud
iptv_cluster = [k for k in top_kws if 'iptv' in k['keyword'].lower()][:40]
sports_cluster = [k for k in top_kws if any(s in k['keyword'].lower() for s in ['foxtel', 'kayo', 'afl', 'nrl', 'cricket', 'sport', 'premier league'])][:40]
isp_cluster = [k for k in top_kws if any(s in k['keyword'].lower() for s in ['telstra', 'optus', 'tpg', 'speed', 'internet', 'nbn'])][:30]
device_cluster = [k for k in top_kws if any(s in k['keyword'].lower() for s in ['firestick', 'tv', 'apple', 'box', 'player', 'samsung'])][:30]
general_cluster = [k for k in top_kws if k not in iptv_cluster and k not in sports_cluster and k not in isp_cluster and k not in device_cluster][:50]

def make_pill(k, icon, color):
    slug = slugify(k['keyword'])
    return f'<a href="topic/{slug}/index.html" class="sport-tag" style="margin:0.22rem; font-size:0.83rem; display:inline-flex; align-items:center; gap:0.35rem;"><i class="fa-solid {icon}" style="color:{color}; font-size:0.75rem;"></i> {k["keyword"].title()} <span style="color:var(--text-dim); font-size:0.75rem;">({k["volume"]:,}/mo)</span></a>'

iptv_pills_html = '\n'.join([make_pill(k, 'fa-bolt', 'var(--primary)') for k in iptv_cluster])
sports_pills_html = '\n'.join([make_pill(k, 'fa-football', 'var(--aus-gold)') for k in sports_cluster])
isp_pills_html = '\n'.join([make_pill(k, 'fa-network-wired', 'var(--secondary)') for k in isp_cluster])
device_pills_html = '\n'.join([make_pill(k, 'fa-tv', 'var(--primary)') for k in device_cluster])
general_pills_html = '\n'.join([make_pill(k, 'fa-magnifying-glass', 'var(--text-muted)') for k in general_cluster])

# City pills for all 76 Australian cities
city_pills = []
for c, s, _ in cities_list:
    c_slug = slugify(c)
    city_pills.append(f'<a href="cities/{c_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-location-dot" style="color:var(--primary); font-size:0.75rem;"></i> {c}, {s}</a>')
city_pills_html = '\n'.join(city_pills)

# Sports pills
sports_pills = []
for s_slug, s_title, _, s_name, _ in sports_list:
    sports_pills.append(f'<a href="sports/{s_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-play" style="color:var(--aus-gold); font-size:0.75rem;"></i> {s_name}</a>')
sports_pills_html = '\n'.join(sports_pills)

# Devices pills
devices_pills = []
for d_slug, d_title, _, d_name, _ in devices_list:
    devices_pills.append(f'<a href="devices/{d_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-tv" style="color:var(--secondary); font-size:0.75rem;"></i> {d_name}</a>')
devices_pills_html = '\n'.join(devices_pills)

# Languages pills
lang_pills = []
for l_slug, l_title, _, l_name, _ in languages_list:
    lang_pills.append(f'<a href="languages/{l_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-globe-oceania" style="color:var(--aus-gold); font-size:0.75rem;"></i> {l_name} TV</a>')
lang_pills_html = '\n'.join(lang_pills)

# Comparisons pills
comp_pills = []
for c_slug, c_title, _, c_name, _ in competitors_list:
    comp_pills.append(f'<a href="comparisons/{c_slug}/index.html" class="sport-tag" style="margin:0.2rem; font-size:0.82rem;"><i class="fa-solid fa-scale-balanced" style="color:var(--primary); font-size:0.75rem;"></i> {c_name}</a>')
comp_pills_html = '\n'.join(comp_pills)

# Complete Mega Long-Form HTML Injection
mega_body = f"""
  <!-- ==================== 13. ULTIMATE AUSTRALIAN IPTV AUTHORITY & CONVERSION SUITE ==================== -->
  
  <!-- SECTION 1: FOXTEL & KAYO VS IPTV AUSTRALIA PRICE COMPARISON TABLE (SAVE $3,332 AUD/YR) -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="foxtel-kayo-comparison">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-calculator"></i> Huge Household Savings</span>
        <h2 class="section-title">Foxtel & Kayo vs Australia IPTV: Save Over $3,332 AUD Every Year</h2>
        <p class="section-subtitle">See why over 140,000 Australian households have cut the pay-TV cord and switched to all-inclusive 4K IPTV streaming.</p>
      </div>

      <div class="glass-card" style="margin-bottom:2.5rem; border-color:var(--border-gold);">
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.95rem;">
            <thead>
              <tr style="border-bottom:2px solid var(--border-color); color:var(--text-main);">
                <th style="padding:1.2rem; font-size:1.05rem;">Features & Channels</th>
                <th style="padding:1.2rem; color:#ef4444; font-size:1.05rem;"><i class="fa-solid fa-xmark"></i> Traditional Subscriptions</th>
                <th style="padding:1.2rem; color:var(--secondary); font-size:1.05rem;"><i class="fa-solid fa-check-double"></i> Australia IPTV Service</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">Live Australian TV Channels</td>
                <td style="padding:1.1rem; color:var(--text-muted);">Limited to ~90 Foxtel cable channels</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">50,000+ Live Channels Worldwide + All AU FTA & Foxtel</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">AFL, NRL & Cricket Australia</td>
                <td style="padding:1.1rem; color:var(--text-muted);">$35 AUD / month (Kayo) or $100+ Foxtel Sports</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">Included 4K 60FPS (Fox Footy 504, Fox League 502, 7HD, 9HD)</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">English Premier League & Champions League</td>
                <td style="padding:1.1rem; color:var(--text-muted);">$24.99 AUD / month (Optus Sport) + $27 AUD Stan Sport</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">Included (Optus Sport 1-6, Stan Sport 1-4, Sky Sports UK 4K)</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">UFC Numbered Cards & Boxing PPVs</td>
                <td style="padding:1.1rem; color:var(--text-muted);">$59.95 AUD per Main Event Pay-Per-View</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">Included Free of Charge on 4 Dedicated Main Event Channels</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">On-Demand Movies & TV Series (VOD)</td>
                <td style="padding:1.1rem; color:var(--text-muted);">Requires Netflix ($22.99), Disney+ ($17.99), Binge ($18)</td>
                <td style="padding:1.1rem; color:var(--secondary); font-weight:700;">200,000+ VOD Titles in 4K HDR Updated Daily</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1.1rem; font-weight:700; color:#fff;">Contract & Equipment Lock-in</td>
                <td style="padding:1.1rem; color:#ef4444;">12-24 Month Contracts, $150 installation, set-top box fees</td>
                <td style="padding:1.1rem; color:var(--aus-green); font-weight:700;">No Lock-in Contract, Works on Your Existing Smart TV/Firestick</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color); background:rgba(192, 132, 252, 0.08);">
                <td style="padding:1.25rem; font-weight:800; font-size:1.1rem; color:#fff;">Total Cost Per Year (AUD)</td>
                <td style="padding:1.25rem; color:#ef4444; font-weight:800; font-size:1.15rem; font-family:var(--font-mono);">$3,442.00 AUD / year</td>
                <td style="padding:1.25rem; color:var(--aus-gold); font-weight:800; font-size:1.35rem; font-family:var(--font-mono);">$110.00 AUD / year</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="margin-top:2rem; padding:1.5rem; background:rgba(0,0,0,0.4); border-radius:var(--radius-md); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1.5rem;">
          <div>
            <h4 style="color:#fff; font-size:1.2rem; margin-bottom:0.35rem;"><i class="fa-solid fa-piggy-bank" style="color:var(--aus-gold); margin-right:0.5rem;"></i> Total Net Household Savings: <strong>$3,332 AUD / year</strong></h4>
            <p style="color:var(--text-muted); font-size:0.9rem; margin:0;">Pay with Australian PayID, Visa/Mastercard, or Crypto with instant activation in 60 seconds.</p>
          </div>
          <div style="display:flex; gap:1rem;">
            <button class="btn btn-gold btn-lg" data-open-modal="trial"><i class="fa-solid fa-play"></i> Start 24-Hour Free Trial</button>
            <a href="#pricing" class="btn btn-primary btn-lg"><i class="fa-solid fa-bolt"></i> Order Annual Plan ($110 AUD)</a>
          </div>
        </div>
      </div>

      <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center;">
        {comp_pills_html}
      </div>
    </div>
  </section>

  <!-- SECTION 2: WHOLESALE IPTV RESELLER ACADEMY & PANEL PORTAL -->
  <section class="section-padding-lg" style="background:var(--bg-main); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="wholesale-reseller-academy">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-briefcase"></i> High Profit Margins</span>
        <h2 class="section-title">Start Your Own IPTV Reseller Business in Australia</h2>
        <p class="section-subtitle">Earn $3,000 to $15,000 AUD per month supplying friends, family, and local clients with premium 4K Australian streaming television.</p>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem; margin-bottom:3rem; align-items:center;">
        <div>
          <h3 style="font-size:1.8rem; color:#fff; margin-bottom:1.2rem; line-height:1.3;">
            How the Australian IPTV Reseller Credit System Works
          </h3>
          <p style="color:var(--text-muted); line-height:1.8; margin-bottom:1rem; font-size:0.96rem;">
            When you purchase an IPTV Reseller Panel from us, you receive a master web dashboard (Xtream UI / ZapX) pre-loaded with wholesale credits. There is <strong>zero technical skill required</strong> and credits never expire until you activate them.
          </p>
          <ul style="list-style:none; display:flex; flex-direction:column; gap:0.85rem; color:var(--text-muted); font-size:0.93rem; margin-bottom:2rem;">
            <li><i class="fa-solid fa-circle-check" style="color:var(--secondary); margin-right:0.5rem;"></i> <strong>Wholesale Cost:</strong> 1 Credit = 1 Full Year Subscription for just $2.20 to $4.50 AUD.</li>
            <li><i class="fa-solid fa-circle-check" style="color:var(--aus-gold); margin-right:0.5rem;"></i> <strong>Retail Sale Price:</strong> Sell 1 Year for $90 to $140 AUD to Australian retail clients.</li>
            <li><i class="fa-solid fa-circle-check" style="color:var(--primary); margin-right:0.5rem;"></i> <strong>Net Profit Margin:</strong> Pocket over 800% profit ($85 to $135 AUD pure margin per client!).</li>
            <li><i class="fa-solid fa-circle-check" style="color:var(--secondary); margin-right:0.5rem;"></i> <strong>Unlimited Free Trials:</strong> Generate 24-hour test accounts instantly for your prospects with 1 click.</li>
            <li><i class="fa-solid fa-circle-check" style="color:var(--aus-gold); margin-right:0.5rem;"></i> <strong>Custom Branding & DNS:</strong> Connect your own domain and DNS so clients see your private brand.</li>
          </ul>

          <div style="display:flex; gap:1rem; flex-wrap:wrap;">
            <button class="btn btn-primary btn-lg" data-open-modal="reseller"><i class="fa-solid fa-rocket"></i> Open Reseller Account Now</button>
            <a href="#calculator" class="btn btn-outline btn-lg"><i class="fa-solid fa-calculator"></i> Calculate Your Net Profit</a>
          </div>
        </div>

        <div class="glass-card" style="padding:2.5rem; border-color:var(--border-mauve);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; border-bottom:1px solid var(--border-color); padding-bottom:1rem;">
            <h4 style="font-size:1.3rem; color:#fff; margin:0;"><i class="fa-solid fa-chart-line" style="color:var(--secondary); margin-right:0.5rem;"></i> Monthly Reseller Profit Projections</h4>
            <span class="badge badge-glow-gold">AUD Dollars</span>
          </div>

          <div style="display:flex; flex-direction:column; gap:1.25rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:0.75rem; border-bottom:1px dashed var(--border-color);">
              <div>
                <strong style="color:#fff; font-size:1.05rem;">20 Retail Clients</strong>
                <div style="font-size:0.8rem; color:var(--text-dim);">Wholesale Cost: $70 AUD</div>
              </div>
              <div style="text-align:right;">
                <span style="color:var(--secondary); font-size:1.2rem; font-weight:800; font-family:var(--font-mono);">$2,130 AUD</span>
                <div style="font-size:0.75rem; color:var(--aus-green);">Pure Net Profit</div>
              </div>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:0.75rem; border-bottom:1px dashed var(--border-color);">
              <div>
                <strong style="color:#fff; font-size:1.05rem;">50 Retail Clients</strong>
                <div style="font-size:0.8rem; color:var(--text-dim);">Wholesale Cost: $175 AUD</div>
              </div>
              <div style="text-align:right;">
                <span style="color:var(--secondary); font-size:1.2rem; font-weight:800; font-family:var(--font-mono);">$5,325 AUD</span>
                <div style="font-size:0.75rem; color:var(--aus-green);">Pure Net Profit</div>
              </div>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:0.75rem; border-bottom:1px dashed var(--border-color);">
              <div>
                <strong style="color:#fff; font-size:1.05rem;">100 Retail Clients</strong>
                <div style="font-size:0.8rem; color:var(--text-dim);">Wholesale Cost: $350 AUD</div>
              </div>
              <div style="text-align:right;">
                <span style="color:var(--aus-gold); font-size:1.3rem; font-weight:800; font-family:var(--font-mono);">$10,650 AUD</span>
                <div style="font-size:0.75rem; color:var(--aus-green);">Pure Net Profit</div>
              </div>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center;">
              <div>
                <strong style="color:#fff; font-size:1.05rem;">250 Retail Clients</strong>
                <div style="font-size:0.8rem; color:var(--text-dim);">Wholesale Cost: $875 AUD</div>
              </div>
              <div style="text-align:right;">
                <span style="color:var(--aus-gold); font-size:1.45rem; font-weight:800; font-family:var(--font-mono);">$26,625 AUD</span>
                <div style="font-size:0.75rem; color:var(--aus-green);">Pure Net Profit</div>
              </div>
            </div>
          </div>

          <div style="margin-top:1.5rem; padding:1rem; background:rgba(0,0,0,0.3); border-radius:var(--radius-md); text-align:center;">
            <p style="font-size:0.85rem; color:var(--text-muted); margin:0;">
              <i class="fa-solid fa-lock" style="color:var(--primary);"></i> Instant Wholesale Panel Activation via PayID, Visa/Mastercard, or Crypto.
            </p>
          </div>
        </div>
      </div>

      <!-- Reseller Tools Feature Grid -->
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.5rem;">
        <div class="glass-card">
          <div style="font-size:2rem; color:var(--primary); margin-bottom:1rem;"><i class="fa-solid fa-gauge-high"></i></div>
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;">Xtream UI & ZapX Panel</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">Full intuitive web management dashboard accessible on desktop, tablet, and smartphone.</p>
        </div>

        <div class="glass-card">
          <div style="font-size:2rem; color:var(--aus-gold); margin-bottom:1rem;"><i class="fa-solid fa-user-plus"></i></div>
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;">Sub-Reseller Creation</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">Build a network of sub-resellers beneath you and sell credits in bulk for passive recurring income.</p>
        </div>

        <div class="glass-card">
          <div style="font-size:2rem; color:var(--secondary); margin-bottom:1rem;"><i class="fa-solid fa-fingerprint"></i></div>
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;">Custom DNS & Branding</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">Point your private domain name so your customers see only your brand name, logo, and portal URL.</p>
        </div>

        <div class="glass-card">
          <div style="font-size:2rem; color:var(--aus-green); margin-bottom:1rem;"><i class="fa-solid fa-headset"></i></div>
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;">24/7 Priority Australian Desk</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6;">Direct WhatsApp and Telegram access to senior server engineers during peak AEST sporting hours.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: 2026 AUSTRALIAN SPORTS BROADCAST CALENDAR & FIXTURES MATRIX -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="aussie-sports-calendar">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-calendar-days"></i> 2026 Live Broadcast Fixtures</span>
        <h2 class="section-title">Never Miss an Australian Sporting Event in 4K 60FPS</h2>
        <p class="section-subtitle">Stadium-grade feeds directly relayed to Australian edge nodes with zero regional blackout restrictions.</p>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem; margin-bottom:2.5rem;">
        <!-- Sports Card 1: AFL -->
        <div class="glass-card" style="border-color:var(--border-gold);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
            <h3 style="font-size:1.35rem; color:#fff; margin:0;"><i class="fa-solid fa-football" style="color:var(--aus-gold); margin-right:0.4rem;"></i> AFL Premiership</h3>
            <span class="badge badge-glow-gold">4K 60FPS</span>
          </div>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1.25rem;">
            Every single match of all 24 home & away rounds plus the finals series and the 100,000-seat MCG Grand Final. Dual Fox Footy and Channel 7HD feeds with no regional blackouts.
          </p>
          <ul style="list-style:none; font-size:0.82rem; color:var(--text-dim); display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.5rem;">
            <li>• <strong>Broadcast Feeds:</strong> Fox Footy 504 HD/4K, 7mate, Channel 7HD</li>
            <li>• <strong>Key Fixtures:</strong> Anzac Day MCG, Dreamtime at the 'G, AFL Grand Final</li>
            <li>• <strong>Commentary:</strong> Dolby 5.1 stadium audio with local Fox expert commentary</li>
          </ul>
          <a href="sports/afl-live-stream-iptv/index.html" class="btn btn-gold btn-sm btn-block">Open AFL 4K Hub →</a>
        </div>

        <!-- Sports Card 2: NRL -->
        <div class="glass-card" style="border-color:var(--border-mauve);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
            <h3 style="font-size:1.35rem; color:#fff; margin:0;"><i class="fa-solid fa-shield-halved" style="color:var(--primary); margin-right:0.4rem;"></i> NRL Telstra Premiership</h3>
            <span class="badge badge-glow-cyan">4K 60FPS</span>
          </div>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1.25rem;">
            Complete rugby league coverage: Thursday Night Footy, Super Saturday, Sunday Ticket, Brisbane Magic Round, State of Origin I-III, and the Accor Stadium Grand Final.
          </p>
          <ul style="list-style:none; font-size:0.82rem; color:var(--text-dim); display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.5rem;">
            <li>• <strong>Broadcast Feeds:</strong> Fox League 502 HD/4K, 9Gem, Channel 9HD</li>
            <li>• <strong>State of Origin:</strong> Game 1 (Sydney), Game 2 (Perth), Game 3 (Brisbane)</li>
            <li>• <strong>NRLW:</strong> All women's premiership rounds and finals included live</li>
          </ul>
          <a href="sports/nrl-live-stream-iptv/index.html" class="btn btn-primary btn-sm btn-block">Open NRL 4K Hub →</a>
        </div>

        <!-- Sports Card 3: Cricket Australia -->
        <div class="glass-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
            <h3 style="font-size:1.35rem; color:#fff; margin:0;"><i class="fa-solid fa-baseball-bat-ball" style="color:var(--secondary); margin-right:0.4rem;"></i> Cricket Australia & Ashes</h3>
            <span class="badge badge-glow-green">Full HD / 4K</span>
          </div>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1.25rem;">
            Uninterrupted summer of cricket: Border-Gavaskar Trophy, The Ashes Test series, Boxing Day Test MCG, New Year's Test SCG, and every BBL & WBBL Big Bash clash.
          </p>
          <ul style="list-style:none; font-size:0.82rem; color:var(--text-dim); display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.5rem;">
            <li>• <strong>Broadcast Feeds:</strong> Fox Cricket 501 HD/4K, Channel 7HD, Sky Sports Cricket</li>
            <li>• <strong>BBL Coverage:</strong> All 44 matches from Gabba to Optus Stadium Perth</li>
            <li>• <strong>Global Tournaments:</strong> ICC T20 World Cup, IPL in 4K with Hindi commentary</li>
          </ul>
          <a href="sports/cricket-australia-live-iptv/index.html" class="btn btn-outline btn-sm btn-block">Open Cricket Hub →</a>
        </div>
      </div>

      <!-- Sports Sub-Row: EPL, F1, Combat Sports -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem; margin-bottom:2.5rem;">
        <div class="glass-card">
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-solid fa-futbol" style="color:var(--secondary); margin-right:0.4rem;"></i> Premier League & UEFA 4K</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">All 380 EPL games live via Optus Sport 1-6 & TNT Sports UK 4K. Zero compression artifacts during Saturday night kickoffs.</p>
          <a href="sports/epl-english-premier-league-iptv-australia/index.html" style="font-size:0.82rem; color:var(--secondary); font-weight:700;">View EPL Hub →</a>
        </div>

        <div class="glass-card">
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-solid fa-flag-checkered" style="color:var(--aus-gold); margin-right:0.4rem;"></i> Formula 1 & Bathurst 1000</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">Australian Grand Prix at Albert Park Melbourne in 4K 50FPS + Supercars Championship Mount Panorama Bathurst 1000 endurance race.</p>
          <a href="sports/formula-1-australian-grand-prix-iptv/index.html" style="font-size:0.82rem; color:var(--aus-gold); font-weight:700;">View Motorsport Hub →</a>
        </div>

        <div class="glass-card">
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-solid fa-hand-back-fist" style="color:var(--primary); margin-right:0.4rem;"></i> UFC & Boxing Main Event PPVs</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">All numbered UFC cards and world title boxing bouts included free on 4 dedicated Main Event feeds without $59.95 PPV charges.</p>
          <a href="sports/ufc-ppv-main-event-iptv-australia/index.html" style="font-size:0.82rem; color:var(--primary); font-weight:700;">View Combat Sports Hub →</a>
        </div>
      </div>

      <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center;">
        {sports_pills_html}
      </div>
    </div>
  </section>

  <!-- SECTION 4: NBN & 5G ISP SPEED, BUFFERING & LATENCY BENCHMARK MATRIX -->
  <section class="section-padding-lg" style="background:var(--bg-main); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="nbn-speed-guide">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-gauge"></i> NBN Peering Architecture</span>
        <h2 class="section-title">Engineered Specifically for Australian NBN & 5G Broadband</h2>
        <p class="section-subtitle">Local Equinix SY1 (Sydney), NextDC M2 (Melbourne), and B1 (Brisbane) data center points of presence eliminate overseas buffering.</p>
      </div>

      <div class="glass-card" style="margin-bottom:2.5rem;">
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.92rem;">
            <thead>
              <tr style="border-bottom:2px solid var(--border-color); color:var(--primary);">
                <th style="padding:1rem;">NBN Speed Tier</th>
                <th style="padding:1rem;">Typical Evening Speed</th>
                <th style="padding:1rem;">IPTV Streaming Capacity</th>
                <th style="padding:1rem;">Recommended Video Profile</th>
                <th style="padding:1rem;">Server Latency</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1rem; font-weight:700; color:#fff;">NBN 25 (Basic II)</td>
                <td style="padding:1rem;">20 - 25 Mbps</td>
                <td style="padding:1rem;">1x Stream at 1080p FHD</td>
                <td style="padding:1rem; color:var(--text-muted);">1080p 50FPS (H.264 / HEVC)</td>
                <td style="padding:1rem; color:var(--secondary); font-family:var(--font-mono);">12ms - 18ms</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1rem; font-weight:700; color:#fff;">NBN 50 (Standard Plus)</td>
                <td style="padding:1rem;">45 - 50 Mbps</td>
                <td style="padding:1rem;">2x Concurrent 4K UHD Streams</td>
                <td style="padding:1rem; color:var(--secondary); font-weight:700;">4K UHD 60FPS (HEVC 25 Mbps)</td>
                <td style="padding:1rem; color:var(--secondary); font-family:var(--font-mono);">8ms - 12ms</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1rem; font-weight:700; color:#fff;">NBN 100 (Premium)</td>
                <td style="padding:1rem;">90 - 100 Mbps</td>
                <td style="padding:1rem;">4x Concurrent 4K UHD Streams</td>
                <td style="padding:1rem; color:var(--secondary); font-weight:700;">True 4K UHD & 8K Cinema</td>
                <td style="padding:1rem; color:var(--aus-green); font-family:var(--font-mono);">&lt; 8ms Direct Peer</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1rem; font-weight:700; color:#fff;">NBN 250 / 1000 (Superfast)</td>
                <td style="padding:1rem;">230 - 850 Mbps</td>
                <td style="padding:1rem;">Whole-home unlimited 4K & multi-room</td>
                <td style="padding:1rem; color:var(--aus-gold); font-weight:700;">Uncompressed Master 4K 60FPS</td>
                <td style="padding:1rem; color:var(--aus-green); font-family:var(--font-mono);">&lt; 5ms Equinix IX</td>
              </tr>
              <tr>
                <td style="padding:1rem; font-weight:700; color:#fff;">Telstra / Optus 5G Home</td>
                <td style="padding:1rem;">150 - 350 Mbps</td>
                <td style="padding:1rem;">3x Concurrent 4K Streams</td>
                <td style="padding:1rem; color:var(--secondary);">4K 60FPS with Cloudflare DNS</td>
                <td style="padding:1rem; color:var(--secondary); font-family:var(--font-mono);">15ms - 22ms</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- ISP Guides Cards -->
      <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:1.25rem;">
        <div class="glass-card" style="text-align:center; padding:1.5rem 1rem;">
          <h4 style="font-size:1.05rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-solid fa-tower-cell" style="color:var(--primary);"></i> Telstra NBN</h4>
          <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Bypass transparent DNS proxy on Telstra Smart Modem Gen 2/3.</p>
          <a href="isps/telstra-nbn-iptv-anti-freeze-guide/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Read Telstra Guide →</a>
        </div>

        <div class="glass-card" style="text-align:center; padding:1.5rem 1rem;">
          <h4 style="font-size:1.05rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-solid fa-signal" style="color:var(--aus-gold);"></i> Optus NBN & 5G</h4>
          <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Fix evening sports stuttering on Optus Ultra WiFi routers.</p>
          <a href="isps/optus-nbn-iptv-streaming-setup/index.html" style="font-size:0.8rem; color:var(--aus-gold); font-weight:700;">Read Optus Guide →</a>
        </div>

        <div class="glass-card" style="text-align:center; padding:1.5rem 1rem;">
          <h4 style="font-size:1.05rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-solid fa-bolt" style="color:var(--secondary);"></i> TPG / iiNet</h4>
          <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">DNS setup for TP-Link Archer VR1600v modems on TPG & Vodafone.</p>
          <a href="isps/tpg-telecom-iptv-configuration/index.html" style="font-size:0.8rem; color:var(--secondary); font-weight:700;">Read TPG Guide →</a>
        </div>

        <div class="glass-card" style="text-align:center; padding:1.5rem 1rem;">
          <h4 style="font-size:1.05rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-solid fa-satellite" style="color:var(--primary);"></i> Aussie Broadband</h4>
          <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Direct CVC peering with lowest Australian packet loss metrics.</p>
          <a href="isps/aussie-broadband-iptv-optimization/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Read ABB Guide →</a>
        </div>

        <div class="glass-card" style="text-align:center; padding:1.5rem 1rem;">
          <h4 style="font-size:1.05rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-solid fa-satellite-dish" style="color:var(--aus-green);"></i> Starlink Australia</h4>
          <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem;">Low-orbit satellite streaming in regional WA, QLD, and bush NSW.</p>
          <a href="isps/starlink-satellite-iptv-regional-australia/index.html" style="font-size:0.8rem; color:var(--aus-green); font-weight:700;">Read Starlink Guide →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: MASTER HARDWARE & APP COMPATIBILITY MATRIX -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="hardware-matrix">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-microchip"></i> Hardware Compatibility</span>
        <h2 class="section-title">Tested Across All Australian Smart TVs & Streaming Boxes</h2>
        <p class="section-subtitle">Install in under 5 minutes without technicians or extra hardware purchases.</p>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem; margin-bottom:2.5rem;">
        <div class="glass-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
            <h4 style="font-size:1.25rem; color:#fff; margin:0;"><i class="fa-brands fa-amazon" style="color:var(--aus-gold); margin-right:0.4rem;"></i> Amazon Fire TV Stick</h4>
            <span class="badge badge-glow-gold">Top Recommended</span>
          </div>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
            Works flawlessly with <strong>Firestick 4K, 4K Max, and Fire TV Cube</strong>. Install TiviMate or IPTV Smarters Pro via Downloader in 3 simple steps.
          </p>
          <div style="font-size:0.82rem; color:var(--text-dim); margin-bottom:1rem;">
            Recommended App: <strong>TiviMate Premium / IPTV Smarters</strong>
          </div>
          <a href="devices/iptv-on-amazon-firestick-australia/index.html" class="btn btn-outline btn-sm btn-block">Firestick Guide →</a>
        </div>

        <div class="glass-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
            <h4 style="font-size:1.25rem; color:#fff; margin:0;"><i class="fa-solid fa-tv" style="color:var(--primary); margin-right:0.4rem;"></i> Samsung Tizen Smart TVs</h4>
            <span class="badge badge-glow-cyan">Direct App Store</span>
          </div>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
            Native compatibility with all 2018-2026 Samsung QLED, Neo QLED, OLED, and Crystal UHD screens. Download IBO Player or Smart IPTV directly from Samsung Apps.
          </p>
          <div style="font-size:0.82rem; color:var(--text-dim); margin-bottom:1rem;">
            Recommended App: <strong>IBO Player Pro / Smart IPTV</strong>
          </div>
          <a href="devices/iptv-on-samsung-smart-tv-tizen-australia/index.html" class="btn btn-outline btn-sm btn-block">Samsung TV Guide →</a>
        </div>

        <div class="glass-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
            <h4 style="font-size:1.25rem; color:#fff; margin:0;"><i class="fa-solid fa-display" style="color:var(--secondary); margin-right:0.4rem;"></i> LG webOS Smart TVs</h4>
            <span class="badge badge-glow-green">Direct App Store</span>
          </div>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">
            Engineered for LG OLED C-Series, G-Series, QNED, and NanoCell televisions running webOS 4.0 through webOS 24. Activate within 2 minutes via MAC or M3U playlist.
          </p>
          <div style="font-size:0.82rem; color:var(--text-dim); margin-bottom:1rem;">
            Recommended App: <strong>IBO Player / Room IPTV / IPTV Smarters</strong>
          </div>
          <a href="devices/iptv-on-lg-smart-tv-webos-australia/index.html" class="btn btn-outline btn-sm btn-block">LG webOS Guide →</a>
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem; margin-bottom:2.5rem;">
        <div class="glass-card">
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-brands fa-apple" style="color:var(--primary); margin-right:0.4rem;"></i> Apple TV 4K & iPhone / iPad</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">Premium tvOS experience with iPlayTV, IPTVX, UHF Player, and Smarters Player Lite with Siri Remote scrubbing and Dolby Vision.</p>
          <a href="devices/iptv-on-apple-tv-tvos-australia/index.html" style="font-size:0.82rem; color:var(--primary); font-weight:700;">View Apple TV Setup →</a>
        </div>

        <div class="glass-card">
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-brands fa-android" style="color:var(--aus-green); margin-right:0.4rem;"></i> Android TV & Google TV Box</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">Chromecast with Google TV, Nvidia Shield Pro, Sony Bravia, TCL, and Hisense Android TVs with TiviMate & automated EPG.</p>
          <a href="devices/iptv-on-android-tv-box-australia/index.html" style="font-size:0.82rem; color:var(--aus-green); font-weight:700;">View Android TV Setup →</a>
        </div>

        <div class="glass-card">
          <h4 style="font-size:1.15rem; color:#fff; margin-bottom:0.5rem;"><i class="fa-solid fa-box" style="color:var(--aus-gold); margin-right:0.4rem;"></i> Formuler Z11 & MAG Set-Top Boxes</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:0.75rem;">MyTVOnline 3 (MOL3) portal and Stalker middleware support for Formuler Z11 Pro Max, MAG 520/540, and BuzzTV dedicated boxes.</p>
          <a href="devices/iptv-on-formuler-mytvonline-australia/index.html" style="font-size:0.82rem; color:var(--aus-gold); font-weight:700;">View Formuler Guide →</a>
        </div>
      </div>

      <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center;">
        {devices_pills_html}
      </div>
    </div>
  </section>

  <!-- SECTION 6: AUSTRALIAN METROPOLITAN & REGIONAL COVERAGE ATLAS -->
  <section class="section-padding-lg" style="background:var(--bg-main); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="australian-suburbs-atlas">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-map"></i> Comprehensive Australian Atlas</span>
        <h2 class="section-title">Local Australian IPTV Streaming for 76+ Cities & Regions</h2>
        <p class="section-subtitle">Find your city or suburb below to access localized electronic program guides and nearby CDN ping benchmarks.</p>
      </div>

      <div class="glass-card" style="margin-bottom:2.5rem;">
        <h3 style="font-size:1.3rem; margin-bottom:1rem; color:#fff;"><i class="fa-solid fa-location-dot" style="color:var(--primary); margin-right:0.5rem;"></i> Select Your Australian City:</h3>
        <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
          {city_pills_html}
        </div>
      </div>

      <!-- State by State Breakdown Grid -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.5rem;">
        <div class="glass-card">
          <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:0.6rem;"><i class="fa-solid fa-building"></i> Greater Sydney & NSW</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:0.75rem;">
            Sydney CBD, Western Sydney (Parramatta, Penrith, Blacktown, Liverpool, Campbelltown), Eastern Suburbs (Bondi, Coogee), Northern Beaches (Manly, Dee Why), Sutherland Shire (Cronulla), Newcastle, Wollongong, Central Coast, and Albury.
          </p>
          <a href="cities/sydney/index.html" style="font-size:0.85rem; color:var(--primary); font-weight:700;">Explore NSW IPTV Hubs →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:var(--aus-gold); font-size:1.15rem; margin-bottom:0.6rem;"><i class="fa-solid fa-building"></i> Greater Melbourne & VIC</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:0.75rem;">
            Melbourne CBD, St Kilda, Richmond, South Yarra, Footscray, Brunswick, Carlton, Dandenong, Frankston, Werribee, Geelong, Ballarat, Bendigo, Shepparton, Mildura, and Warrnambool.
          </p>
          <a href="cities/melbourne/index.html" style="font-size:0.85rem; color:var(--aus-gold); font-weight:700;">Explore VIC IPTV Hubs →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:var(--secondary); font-size:1.15rem; margin-bottom:0.6rem;"><i class="fa-solid fa-building"></i> Queensland (QLD)</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:0.75rem;">
            Brisbane CBD, Fortitude Valley, Chermside, Gold Coast (Surfers Paradise, Broadbeach, Robina), Sunshine Coast (Maroochydore, Noosa), Townsville, Cairns, Mackay, Rockhampton, and Toowoomba.
          </p>
          <a href="cities/brisbane/index.html" style="font-size:0.85rem; color:var(--secondary); font-weight:700;">Explore QLD IPTV Hubs →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:var(--aus-green); font-size:1.15rem; margin-bottom:0.6rem;"><i class="fa-solid fa-building"></i> Western Australia (WA)</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:0.75rem;">
            Perth CBD, Northbridge, Fremantle, Joondalup, Scarborough, Mandurah, Bunbury, Kalgoorlie, Geraldton, and Albany with direct low-latency Perth IX peering.
          </p>
          <a href="cities/perth/index.html" style="font-size:0.85rem; color:var(--aus-green); font-weight:700;">Explore WA IPTV Hubs →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:var(--primary); font-size:1.15rem; margin-bottom:0.6rem;"><i class="fa-solid fa-building"></i> South Australia (SA)</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:0.75rem;">
            Adelaide CBD, North Adelaide, Norwood, Glenelg, Port Adelaide, Marion, Salisbury, Elizabeth, Mount Gambier, and Whyalla with 10ms Adelaide server response.
          </p>
          <a href="cities/adelaide/index.html" style="font-size:0.85rem; color:var(--primary); font-weight:700;">Explore SA IPTV Hubs →</a>
        </div>

        <div class="glass-card">
          <h4 style="color:var(--aus-gold); font-size:1.15rem; margin-bottom:0.6rem;"><i class="fa-solid fa-building"></i> ACT, TAS & NT</h4>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6; margin-bottom:0.75rem;">
            Canberra (Civic, Belconnen, Tuggeranong, Gungahlin), Hobart, Launceston, Devonport, Darwin, Palmerston, and Alice Springs with full regional NBN & 4G/5G tuning.
          </p>
          <a href="cities/canberra/index.html" style="font-size:0.85rem; color:var(--aus-gold); font-weight:700;">Explore Regional Hubs →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 7: PAYID & AUSTRALIAN PAYMENT CHECKOUT GUARANTEE -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="payid-checkout-hub">
    <div class="container">
      <div class="glass-card" style="border-color:var(--border-gold); padding:3.5rem 2.5rem;">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:center;">
          <div>
            <span class="badge badge-glow-gold" style="margin-bottom:0.75rem;"><i class="fa-solid fa-shield-check"></i> 100% Safe Australian Payments</span>
            <h2 style="font-size:2.2rem; color:#fff; line-height:1.2; margin-bottom:1.25rem;">Pay Securely via Australian PayID / Osko or Credit Card</h2>
            <p style="color:var(--text-muted); line-height:1.8; font-size:0.96rem; margin-bottom:1.5rem;">
              We support convenient, instant Australian payment methods. No overseas international transaction surcharges or bank conversion penalties.
            </p>
            <div style="display:flex; flex-direction:column; gap:1rem; margin-bottom:2rem;">
              <div style="display:flex; gap:1rem; align-items:flex-start;">
                <div style="font-size:1.5rem; color:var(--aus-gold);"><i class="fa-solid fa-bolt"></i></div>
                <div>
                  <h4 style="color:#fff; font-size:1.05rem; margin-bottom:0.2rem;">Instant PayID / Osko Bank Transfer</h4>
                  <p style="color:var(--text-dim); font-size:0.88rem; margin:0;">Supported by Commonwealth Bank, NAB, ANZ, Westpac, Bendigo Bank, ING, and Macquarie. Zero payment fees.</p>
                </div>
              </div>

              <div style="display:flex; gap:1rem; align-items:flex-start;">
                <div style="font-size:1.5rem; color:var(--primary);"><i class="fa-solid fa-credit-card"></i></div>
                <div>
                  <h4 style="color:#fff; font-size:1.05rem; margin-bottom:0.2rem;">Visa & Mastercard (256-Bit SSL)</h4>
                  <p style="color:var(--text-dim); font-size:0.88rem; margin:0;">Encrypted 3D-Secure checkout processed with instantaneous confirmation.</p>
                </div>
              </div>

              <div style="display:flex; gap:1rem; align-items:flex-start;">
                <div style="font-size:1.5rem; color:var(--secondary);"><i class="fa-brands fa-bitcoin"></i></div>
                <div>
                  <h4 style="color:#fff; font-size:1.05rem; margin-bottom:0.2rem;">Cryptocurrency (BTC, USDT, ETH)</h4>
                  <p style="color:var(--text-dim); font-size:0.88rem; margin:0;">Total anonymity and privacy with 10% bonus wholesale credits on crypto orders.</p>
                </div>
              </div>
            </div>

            <div style="display:flex; gap:1rem;">
              <button class="btn btn-gold btn-lg" data-open-modal="trial"><i class="fa-solid fa-play"></i> Try 24H Free First</button>
              <a href="#pricing" class="btn btn-primary btn-lg"><i class="fa-solid fa-cart-shopping"></i> View AUD Plans</a>
            </div>
          </div>

          <div style="background:rgba(0,0,0,0.5); padding:2rem; border-radius:var(--radius-lg); border:1px solid var(--border-color);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; border-bottom:1px solid var(--border-color); padding-bottom:1rem;">
              <h4 style="font-size:1.25rem; color:#fff; margin:0;"><i class="fa-solid fa-clock" style="color:var(--aus-green); margin-right:0.5rem;"></i> 60-Second Setup Workflow</h4>
              <span class="badge badge-glow-green">Automated</span>
            </div>

            <div style="display:flex; flex-direction:column; gap:1.25rem; font-size:0.92rem;">
              <div style="display:flex; gap:1rem;">
                <span style="background:var(--primary); color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; flex-shrink:0;">1</span>
                <div>
                  <strong style="color:#fff;">Choose Plan or Reseller Package</strong>
                  <p style="color:var(--text-muted); font-size:0.82rem; margin:0;">Select 1-Month, 6-Month, 12-Month, or wholesale credits.</p>
                </div>
              </div>

              <div style="display:flex; gap:1rem;">
                <span style="background:var(--primary); color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; flex-shrink:0;">2</span>
                <div>
                  <strong style="color:#fff;">Complete Payment in AUD</strong>
                  <p style="color:var(--text-muted); font-size:0.82rem; margin:0;">Pay securely with PayID or Card in Australian Dollars.</p>
                </div>
              </div>

              <div style="display:flex; gap:1rem;">
                <span style="background:var(--primary); color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; flex-shrink:0;">3</span>
                <div>
                  <strong style="color:#fff;">Instant Delivery via Email & WhatsApp</strong>
                  <p style="color:var(--text-muted); font-size:0.82rem; margin:0;">Receive M3U URL, Xtream Codes login, and step-by-step setup guide within 60 seconds.</p>
                </div>
              </div>

              <div style="display:flex; gap:1rem;">
                <span style="background:var(--aus-green); color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; flex-shrink:0;"><i class="fa-solid fa-check" style="font-size:0.75rem;"></i></span>
                <div>
                  <strong style="color:var(--aus-green);">Stream 50,000+ Channels & Sports in 4K</strong>
                  <p style="color:var(--text-muted); font-size:0.82rem; margin:0;">Enjoy footy, cricket, movies, and world television buffer-free!</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 8: AUSTRALIAN LEGAL, ACMA & PRIVACY MANIFESTO -->
  <section class="section-padding-lg" style="background:var(--bg-main); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="aussie-legal-guide">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-gavel"></i> Legal & Regulatory Context</span>
        <h2 class="section-title">Is IPTV Legal in Australia? Everything You Need to Know</h2>
        <p class="section-subtitle">Understanding Australian copyright regulations, ACMA ISP guidelines, and consumer privacy protections.</p>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:2.5rem; margin-bottom:2.5rem;">
        <div class="glass-card">
          <h3 style="font-size:1.35rem; color:#fff; margin-bottom:1rem;"><i class="fa-solid fa-circle-info" style="color:var(--primary); margin-right:0.5rem;"></i> Australian Telecommunications Context</h3>
          <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.75; margin-bottom:1rem;">
            IPTV (Internet Protocol Television) technology itself is 100% legal in Australia. Thousands of Australian businesses, hotels, and universities utilize IPTV protocol infrastructure daily.
          </p>
          <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.75; margin-bottom:1rem;">
            Under the Australian Telecommunications Act and Copyright Amendment (Online Infringement) legislation, the Australian Communications and Media Authority (ACMA) coordinates with major Internet Service Providers (Telstra, Optus, TPG) to place DNS blocks on select unlicensed domains.
          </p>
          <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.75; margin:0;">
            Our network architecture employs dynamic Anycast CDN routing and private secure domain nodes, preventing ISP DNS redirection from disrupting your home viewing experience.
          </p>
        </div>

        <div class="glass-card">
          <h3 style="font-size:1.35rem; color:#fff; margin-bottom:1rem;"><i class="fa-solid fa-shield-virus" style="color:var(--aus-gold); margin-right:0.5rem;"></i> Should You Use a VPN in Australia?</h3>
          <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.75; margin-bottom:1rem;">
            While our Australian servers connect directly with sub-10ms response times without requiring a VPN, using a reputable VPN (such as <strong>Surfshark, NordVPN, or ExpressVPN</strong>) offers two distinct advantages for Australian viewers:
          </p>
          <ul style="list-style:none; display:flex; flex-direction:column; gap:0.75rem; font-size:0.9rem; color:var(--text-muted); margin-bottom:1.5rem;">
            <li><i class="fa-solid fa-circle-check" style="color:var(--aus-gold); margin-right:0.5rem;"></i> <strong>Bypasses ISP Traffic Throttling:</strong> Prevents Telstra and Optus algorithms from selectively deprioritizing video traffic during Friday and Saturday night peak sports hours.</li>
            <li><i class="fa-solid fa-circle-check" style="color:var(--primary); margin-right:0.5rem;"></i> <strong>Complete Data Privacy:</strong> Encrypts your IP address under Australian Mandatory Data Retention laws.</li>
          </ul>
          <a href="guides/is-iptv-legal-in-australia-2026/index.html" class="btn btn-outline btn-block">Read Full Australian Legal Guide →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 9: THE ULTIMATE AUSTRALIAN KEYWORD & SEARCH CLUSTER DIRECTORY (97,000+ DATASET) -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5.5rem 0;" id="mega-search-directory">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-magnifying-glass-chart"></i> Master Keyword Index</span>
        <h2 class="section-title">Explore Australia's Largest IPTV Search & Topic Knowledge Base</h2>
        <p class="section-subtitle">Indexed terms from over 97,461 real Australian search engine queries across Semrush and Ahrefs databases.</p>
      </div>

      <!-- Cluster 1: Top IPTV Australia Queries -->
      <div class="glass-card" style="margin-bottom:2rem;">
        <h3 style="font-size:1.25rem; color:#fff; margin-bottom:0.75rem; display:flex; align-items:center; gap:0.5rem;">
          <i class="fa-solid fa-tv" style="color:var(--primary);"></i> Top Australian IPTV Search Queries
        </h3>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">High-intent subscription and trial search terms queried by Australian cord-cutters:</p>
        <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
          {iptv_pills_html}
        </div>
      </div>

      <!-- Cluster 2: Australian Footy, Cricket & Sports Queries -->
      <div class="glass-card" style="margin-bottom:2rem;">
        <h3 style="font-size:1.25rem; color:#fff; margin-bottom:0.75rem; display:flex; align-items:center; gap:0.5rem;">
          <i class="fa-solid fa-football" style="color:var(--aus-gold);"></i> Australian Sports & Footy Search Queries
        </h3>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">AFL, NRL, Cricket Australia, Kayo, Foxtel and Premier League search clusters:</p>
        <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
          {sports_pills_html}
        </div>
      </div>

      <!-- Cluster 3: Australian Broadband, NBN & Speed Queries -->
      <div class="glass-card" style="margin-bottom:2rem;">
        <h3 style="font-size:1.25rem; color:#fff; margin-bottom:0.75rem; display:flex; align-items:center; gap:0.5rem;">
          <i class="fa-solid fa-network-wired" style="color:var(--secondary);"></i> NBN Speed & Broadband Optimization Terms
        </h3>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">Telstra, Optus, TPG speed test, latency and ISP router configuration queries:</p>
        <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
          {isp_pills_html}
        </div>
      </div>

      <!-- Cluster 4: Streaming Devices & Player Queries -->
      <div class="glass-card" style="margin-bottom:2.5rem;">
        <h3 style="font-size:1.25rem; color:#fff; margin-bottom:0.75rem; display:flex; align-items:center; gap:0.5rem;">
          <i class="fa-solid fa-microchip" style="color:var(--primary);"></i> Streaming Devices & Player Hardware Searches
        </h3>
        <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">Firestick 4K, TiviMate, Samsung TV, LG webOS, Apple TV, and Android hardware queries:</p>
        <div style="display:flex; flex-wrap:wrap; gap:0.35rem;">
          {device_pills_html}
        </div>
      </div>

      <div style="text-align:center; padding:2rem 0;">
        <a href="directory/index.html" class="btn btn-primary btn-xl" style="padding:1.1rem 2.5rem; font-size:1.1rem;">
          <i class="fa-solid fa-compass" style="margin-right:0.5rem;"></i> Browse All 2,081 Programmatic Australian SEO Directory Pages
        </a>
      </div>
    </div>
  </section>
"""

# Read existing index.html
with open(index_path, "r", encoding="utf-8") as f:
    existing_html = f.read()

# Replace or inject mega body cleanly before the footer
footer_marker = "<!-- ==================== 12. FOOTER ==================== -->"
if footer_marker in existing_html:
    # Check if section 13 was previously appended, replace it or insert
    if "<!-- ==================== 13. ULTIMATE AUSTRALIAN IPTV AUTHORITY & CONVERSION SUITE ==================== -->" in existing_html:
        pattern = re.compile(r'<!-- ==================== 13\. ULTIMATE AUSTRALIAN IPTV AUTHORITY & CONVERSION SUITE ==================== -->.*?(?=<!-- ==================== 12\. FOOTER ==================== -->)', re.DOTALL)
        updated_html = pattern.sub(mega_body.strip() + "\n  ", existing_html)
    else:
        updated_html = existing_html.replace(footer_marker, mega_body.strip() + "\n\n  " + footer_marker)
else:
    # If marker changed, replace </body>
    updated_html = existing_html.replace("</body>", mega_body.strip() + "\n</body>")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(updated_html)

print(f"SUCCESS: Injected Ultimate Mega Long-Form Suite! New index.html size: {len(updated_html)} characters.")

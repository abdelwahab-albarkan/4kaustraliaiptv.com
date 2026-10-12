import os, html, re

BASE_DIR = r"c:\Users\clanm\OneDrive\Desktop\australiatv"
index_path = os.path.join(BASE_DIR, "index.html")

print("Generating ultra-rich, keyword-packed homepage for Australia IPTV...")

from seo_engine_init import (
    cities_list, sports_list, devices_list, competitors_list,
    isps_list, languages_list, guides_list, parsed_kws
)
from seo_page_renderer import slugify

# Extract top 100 keywords from parsed_kws sorted by volume
top_kws = []
seen = set()
for p in parsed_kws:
    kw = p["keyword"].strip()
    if kw.lower() not in seen and len(kw) > 2:
        seen.add(kw.lower())
        top_kws.append(p)

top_kws = sorted(top_kws, key=lambda x: x["volume"], reverse=True)[:100]

# Build Mega Keyword Cloud HTML
cloud_pills = []
for k in top_kws[:60]:
    kw = k["keyword"]
    vol = k["volume"]
    slug = slugify(kw)
    cloud_pills.append(f'<a href="topic/{slug}/index.html" class="sport-tag" style="margin:0.25rem; font-size:0.85rem;"><i class="fa-solid fa-bolt" style="color:var(--primary); font-size:0.75rem;"></i> {kw.title()} <small style="color:var(--text-dim);">({vol:,}/mo)</small></a>')

mega_cloud_html = '\n'.join(cloud_pills)

# Comprehensive Semantic SEO Content Blocks
deep_seo_html = f"""
  <!-- ==================== MEGA AUSTRALIAN SEO KEYWORD & KNOWLEDGE POWERHOUSE ==================== -->
  <section class="section-padding-lg" style="background:var(--bg-main); border-top:1px solid var(--border-color); padding: 5rem 0;" id="australia-iptv-master-guide">
    <div class="container">
      
      <!-- Top Mega Search Keyword Cloud -->
      <div class="glass-card" style="margin-bottom:3.5rem; border-color:var(--border-highlight);">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; margin-bottom:1.5rem;">
          <div>
            <span class="badge badge-glow-gold" style="margin-bottom:0.5rem;"><i class="fa-solid fa-chart-line"></i> High-Volume Australian Search Trends 2026</span>
            <h2 style="font-size:1.6rem; color:#fff; margin:0;">Popular Australian IPTV & Streaming Searches</h2>
          </div>
          <span class="badge badge-glow-cyan">97,000+ Keyword Index</span>
        </div>
        <p style="font-size:0.92rem; color:var(--text-muted); margin-bottom:1.5rem;">
          Browse high-demand live sports, device setups, cable alternatives, and location-based streaming queries searched by Australian viewers:
        </p>
        <div style="display:flex; flex-wrap:wrap; gap:0.4rem;">
          {mega_cloud_html}
        </div>
      </div>

      <!-- Section 1: The Definitive Guide to IPTV in Australia -->
      <div class="glass-card" style="margin-bottom:3.5rem;">
        <span class="badge badge-glow-cyan" style="margin-bottom:0.75rem;"><i class="fa-solid fa-book-open"></i> Australian Streaming Authority</span>
        <h2 style="font-size:2rem; color:#fff; margin-bottom:1.25rem;">Why IPTV Australia is the #1 Entertainment Choice in 2026</h2>
        
        <div style="color:var(--text-muted); line-height:1.8; font-size:0.98rem;">
          <p style="margin-bottom:1.25rem;">
            As Australian households face rising living costs and skyrocketing pay-TV subscriptions exceeding <strong>$1,200 to $1,800 AUD per year</strong> across fragmented platforms (Foxtel, Kayo Sports, Stan Sport, Optus Sport, Binge, Netflix, and Paramount+), <strong>IPTV Australia</strong> has emerged as the definitive all-in-one entertainment solution. By consolidating <strong>50,000+ live television channels</strong>, complete Australian sports leagues in 4K 60FPS, and over <strong>160,000+ on-demand movies and series</strong> into a single high-speed subscription for only <strong>$15 AUD per month (or $110 AUD per year)</strong>, viewers across New South Wales, Victoria, Queensland, Western Australia, South Australia, Tasmania, ACT, and the Northern Territory enjoy unmatched value.
          </p>

          <p style="margin-bottom:1.25rem;">
            Unlike traditional satellite or legacy cable requiring expensive proprietary set-top boxes, contracts, and installation technician call-outs, modern <strong>Australian IPTV</strong> functions over standard high-speed broadband (NBN 25, NBN 50, NBN 100, NBN 250, NBN 1000, and 5G Home Wireless). Using industry-standard protocols such as <strong>M3U Plus playlists</strong> and <strong>Xtream Codes API</strong>, customers can stream on existing hardware including Amazon Firestick 4K Max, Samsung Smart TVs (Tizen OS), LG Smart TVs (webOS), Apple TV 4K, Android TV / Google TV (Chromecast 4K, Nvidia Shield), iPhones, iPads, Android smartphones, and Windows/Mac PCs.
          </p>
        </div>

        <!-- 4 Key Advantages Grid -->
        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.25rem; margin-top:2rem;">
          <div style="background:rgba(0,0,0,0.4); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <div style="font-size:1.6rem; color:var(--primary); margin-bottom:0.5rem;"><i class="fa-solid fa-bolt"></i></div>
            <h4 style="color:#fff; font-size:1.05rem; margin-bottom:0.3rem;">Zero ISP Buffering</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">Local CDN edge peering in Sydney and Melbourne delivers sub-15ms response times across all Australian NBN providers.</p>
          </div>
          <div style="background:rgba(0,0,0,0.4); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <div style="font-size:1.6rem; color:var(--aus-gold); margin-bottom:0.5rem;"><i class="fa-solid fa-trophy"></i></div>
            <h4 style="color:#fff; font-size:1.05rem; margin-bottom:0.3rem;">All Sports & PPVs</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">Fox Footy, Fox League, Optus Sport, Stan Sport, and all UFC/Boxing Main Event PPVs included with zero extra fees.</p>
          </div>
          <div style="background:rgba(0,0,0,0.4); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <div style="font-size:1.6rem; color:var(--secondary); margin-bottom:0.5rem;"><i class="fa-solid fa-calendar-days"></i></div>
            <h4 style="color:#fff; font-size:1.05rem; margin-bottom:0.3rem;">7-Day EPG Guide</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">Full Australian Electronic Program Guide (EPG) with automatic syncing for local Free-to-Air and Foxtel channels.</p>
          </div>
          <div style="background:rgba(0,0,0,0.4); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <div style="font-size:1.6rem; color:var(--primary); margin-bottom:0.5rem;"><i class="fa-solid fa-credit-card"></i></div>
            <h4 style="color:#fff; font-size:1.05rem; margin-bottom:0.3rem;">PayID in AUD</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">Pay instantly in Australian Dollars using PayID, Osko, Apple Pay, Visa/Mastercard, or Crypto with instant automated setup.</p>
          </div>
        </div>
      </div>

      <!-- Section 2: Australian Cable & Pay-TV Price Comparison Table -->
      <div class="glass-card" style="margin-bottom:3.5rem;">
        <span class="badge badge-glow-gold" style="margin-bottom:0.75rem;"><i class="fa-solid fa-scale-balanced"></i> Australian Cost Comparison</span>
        <h2 style="font-size:1.8rem; color:#fff; margin-bottom:1rem;">Australian Pay-TV vs. IPTV Cost Breakdown (AUD)</h2>
        <p style="color:var(--text-muted); font-size:0.95rem; margin-bottom:1.5rem;">
          Compare the typical monthly and annual expenditure of maintaining separate Australian streaming subscriptions versus our all-in-one 4K IPTV service:
        </p>

        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.92rem;">
            <thead>
              <tr style="border-bottom:2px solid var(--border-color); color:var(--primary);">
                <th style="padding:1rem;">Streaming Service</th>
                <th style="padding:1rem;">Monthly Cost (AUD)</th>
                <th style="padding:1rem;">Annual Cost (AUD)</th>
                <th style="padding:1rem;">Channel & Content Limitations</th>
                <th style="padding:1rem;">Included in IPTV Australia?</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1rem; font-weight:700;">Foxtel Platinum Plus / iQ5</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$140.00 AUD</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$1,680.00 AUD</td>
                <td style="padding:1rem; color:var(--text-dim);">Requires iQ box, lock-in contract, extra fees for multi-room</td>
                <td style="padding:1rem; color:var(--secondary); font-weight:700;"><i class="fa-solid fa-check"></i> YES (All Channels 4K)</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1rem; font-weight:700;">Kayo Sports (Basic / Premium)</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$35.00 AUD</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$420.00 AUD</td>
                <td style="padding:1rem; color:var(--text-dim);">Sports only, 2 screens max, frequent price hikes</td>
                <td style="padding:1rem; color:var(--secondary); font-weight:700;"><i class="fa-solid fa-check"></i> YES (Fox Sports 4K)</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1rem; font-weight:700;">Stan + Stan Sport Add-on</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$27.00 AUD</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$324.00 AUD</td>
                <td style="padding:1rem; color:var(--text-dim);">Requires base Stan plan + mandatory sport surcharge</td>
                <td style="padding:1rem; color:var(--secondary); font-weight:700;"><i class="fa-solid fa-check"></i> YES (Stan Sport 1-4 4K)</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1rem; font-weight:700;">Optus Sport (Non-Optus Users)</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$24.99 AUD</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$299.88 AUD</td>
                <td style="padding:1rem; color:var(--text-dim);">EPL and La Liga only, limited VOD</td>
                <td style="padding:1rem; color:var(--secondary); font-weight:700;"><i class="fa-solid fa-check"></i> YES (Optus Sport 1-6 HD)</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border-color);">
                <td style="padding:1rem; font-weight:700;">Main Event PPVs (Boxing/UFC)</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$60 - $80 / event</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">$720.00+ AUD</td>
                <td style="padding:1rem; color:var(--text-dim);">Pay-per-view fees charged on top of existing subscriptions</td>
                <td style="padding:1rem; color:var(--secondary); font-weight:700;"><i class="fa-solid fa-check"></i> YES (All PPVs Free)</td>
              </tr>
              <tr style="border-bottom:2px solid var(--primary); background:rgba(192,132,252,0.06);">
                <td style="padding:1rem; font-weight:800; color:var(--primary); font-size:1.05rem;">Combined Pay-TV Package</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:800; font-size:1.05rem;">$286.99 AUD / mo</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:800; font-size:1.1rem;">$3,443.88 AUD / yr</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">5+ separate apps, complex billing</td>
                <td style="padding:1rem; color:#f43f5e; font-weight:700;">Expensive & Fragmented</td>
              </tr>
              <tr style="background:rgba(217,70,239,0.12); border:1px solid var(--border-highlight);">
                <td style="padding:1.2rem; font-weight:800; color:#fff; font-size:1.15rem;">
                  <i class="fa-solid fa-crown" style="color:var(--aus-gold); margin-right:0.4rem;"></i> IPTV Australia Complete 4K Pass
                </td>
                <td style="padding:1.2rem; color:var(--secondary); font-weight:800; font-size:1.2rem;">$15.00 AUD / mo</td>
                <td style="padding:1.2rem; color:var(--aus-gold); font-weight:800; font-size:1.25rem;">$110.00 AUD / yr</td>
                <td style="padding:1.2rem; color:#fff; font-weight:600;">50,000+ Channels, 160K VOD, All Sports, PPV Free</td>
                <td style="padding:1.2rem; color:var(--secondary); font-weight:800; font-size:1.1rem;">
                  <span class="badge badge-glow-gold">SAVE $3,333 AUD / YEAR</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Section 3: Australian Sports & Broadcasting Guide -->
      <div class="glass-card" style="margin-bottom:3.5rem;">
        <span class="badge badge-glow-cyan" style="margin-bottom:0.75rem;"><i class="fa-solid fa-football"></i> Complete Australian Sports Hub</span>
        <h2 style="font-size:1.8rem; color:#fff; margin-bottom:1rem;">Australian Live Sports Broadcast Schedule (4K 60FPS)</h2>
        <p style="color:var(--text-muted); font-size:0.95rem; margin-bottom:1.5rem;">
          Never miss a kickoff, bounce, bowl, or green flag. Our streaming infrastructure provides uncompressed 60FPS sports feeds with multi-audio commentary:
        </p>

        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.5rem;">
          <!-- AFL Column -->
          <div style="background:rgba(0,0,0,0.35); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <h4 style="color:var(--aus-gold); font-size:1.1rem; margin-bottom:0.6rem;"><i class="fa-solid fa-football"></i> AFL Premiership & Finals</h4>
            <ul style="list-style:none; display:flex; flex-direction:column; gap:0.4rem; font-size:0.88rem; color:var(--text-muted);">
              <li>• <strong>Fox Footy 504 HD/4K:</strong> 24/7 AFL news & games</li>
              <li>• <strong>Channel 7 HD (7mate):</strong> Friday Night Footy & Finals</li>
              <li>• <strong>AFL Grand Final:</strong> MCG Live stream in 4K HDR</li>
              <li>• <strong>AFLW & VFL/SANFL/WAFL:</strong> State leagues live</li>
              <li>• <a href="sports/afl-live-stream-iptv/index.html" style="color:var(--primary); font-weight:700;">View AFL Stream Guide →</a></li>
            </ul>
          </div>

          <!-- NRL Column -->
          <div style="background:rgba(0,0,0,0.35); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <h4 style="color:var(--primary); font-size:1.1rem; margin-bottom:0.6rem;"><i class="fa-solid fa-shield"></i> NRL & State of Origin</h4>
            <ul style="list-style:none; display:flex; flex-direction:column; gap:0.4rem; font-size:0.88rem; color:var(--text-muted);">
              <li>• <strong>Fox League 502 HD/4K:</strong> All NRL rounds live</li>
              <li>• <strong>Channel 9HD & 9Now:</strong> Thursday & Sunday NRL</li>
              <li>• <strong>State of Origin 4K:</strong> Game 1, 2, and 3 live</li>
              <li>• <strong>NRL Grand Final & NRLW:</strong> Complete finals series</li>
              <li>• <a href="sports/nrl-live-stream-iptv/index.html" style="color:var(--primary); font-weight:700;">View NRL Stream Guide →</a></li>
            </ul>
          </div>

          <!-- Cricket & Global Column -->
          <div style="background:rgba(0,0,0,0.35); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <h4 style="color:var(--secondary); font-size:1.1rem; margin-bottom:0.6rem;"><i class="fa-solid fa-baseball-bat-ball"></i> Cricket, Rugby & F1</h4>
            <ul style="list-style:none; display:flex; flex-direction:column; gap:0.4rem; font-size:0.88rem; color:var(--text-muted);">
              <li>• <strong>Fox Cricket 501 4K:</strong> The Ashes, Test matches & BBL</li>
              <li>• <strong>Stan Sport 4K:</strong> Super Rugby Pacific & UEFA CL</li>
              <li>• <strong>Optus Sport 1-6:</strong> Premier League 380 games</li>
              <li>• <strong>Formula 1 4K:</strong> Melbourne GP, Qualifying & Races</li>
              <li>• <a href="sports/cricket-australia-the-ashes-iptv/index.html" style="color:var(--primary); font-weight:700;">View Cricket Guide →</a></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Section 4: Australian City & Regional Low-Latency Server Nodes -->
      <div class="glass-card" style="margin-bottom:3.5rem;">
        <span class="badge badge-glow-mauve" style="margin-bottom:0.75rem;"><i class="fa-solid fa-server"></i> Local Edge Infrastructure</span>
        <h2 style="font-size:1.8rem; color:#fff; margin-bottom:1rem;">Australian High-Speed Server Network (Sub-15ms Latency)</h2>
        <p style="color:var(--text-muted); font-size:0.95rem; margin-bottom:1.5rem;">
          We host dedicated high-throughput streaming nodes directly inside Australian data centers to ensure zero packet loss and instantaneous channel switching:
        </p>

        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.25rem;">
          <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
              <h4 style="color:#fff; font-size:1rem;">Sydney (NSW)</h4>
              <span class="badge badge-glow-cyan" style="font-size:0.7rem;">8ms Ping</span>
            </div>
            <p style="font-size:0.82rem; color:var(--text-dim); margin-bottom:0.6rem;">Equinix SYD & NextDC S1/S2 edge peering covering Sydney CBD, Parramatta, Penrith, Bondi, and Newcastle.</p>
            <a href="cities/sydney/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Explore Sydney Hub →</a>
          </div>

          <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
              <h4 style="color:#fff; font-size:1rem;">Melbourne (VIC)</h4>
              <span class="badge badge-glow-gold" style="font-size:0.7rem;">12ms Ping</span>
            </div>
            <p style="font-size:0.82rem; color:var(--text-dim); margin-bottom:0.6rem;">NextDC M1/M2 nodes serving Greater Melbourne, Geelong, Ballarat, Bendigo, St Kilda, and Frankston.</p>
            <a href="cities/melbourne/index.html" style="font-size:0.8rem; color:var(--aus-gold); font-weight:700;">Explore Melbourne Hub →</a>
          </div>

          <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
              <h4 style="color:#fff; font-size:1rem;">Brisbane (QLD)</h4>
              <span class="badge badge-glow-green" style="font-size:0.7rem;">14ms Ping</span>
            </div>
            <p style="font-size:0.82rem; color:var(--text-dim); margin-bottom:0.6rem;">NextDC B1/B2 serving Brisbane, Gold Coast, Sunshine Coast, Toowoomba, Townsville, and Cairns.</p>
            <a href="cities/brisbane/index.html" style="font-size:0.8rem; color:var(--secondary); font-weight:700;">Explore Brisbane Hub →</a>
          </div>

          <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
              <h4 style="color:#fff; font-size:1rem;">Perth (WA)</h4>
              <span class="badge badge-glow-cyan" style="font-size:0.7rem;">22ms Ping</span>
            </div>
            <p style="font-size:0.82rem; color:var(--text-dim); margin-bottom:0.6rem;">NextDC P1 node delivering uninterrupted Western Australian AFL and sports feeds to Perth & Fremantle.</p>
            <a href="cities/perth/index.html" style="font-size:0.8rem; color:var(--primary); font-weight:700;">Explore Perth Hub →</a>
          </div>
        </div>
      </div>

      <!-- Section 5: Australian IPTV Reseller & Wholesale Program (AUD) -->
      <div class="glass-card" style="margin-bottom:3.5rem; border-color:var(--border-gold);">
        <span class="badge badge-glow-gold" style="margin-bottom:0.75rem;"><i class="fa-solid fa-store"></i> Australian Reseller Opportunities</span>
        <h2 style="font-size:1.8rem; color:#fff; margin-bottom:1rem;">Start an IPTV Reseller Business in Australia (Earn $3,000 - $10,000+ AUD / Month)</h2>
        <div style="color:var(--text-muted); line-height:1.8; font-size:0.95rem;">
          <p style="margin-bottom:1.25rem;">
            The IPTV reselling model in Australia represents one of the most profitable online business opportunities in 2026. By purchasing <strong>wholesale credits in AUD</strong> at low rates (<strong>$2.20 to $4.50 AUD per credit</strong>), resellers sell 1-month, 3-month, 6-month, and 12-month passes to Australian customers at standard market rates of <strong>$15 to $25 AUD per month</strong>.
          </p>
          <p style="margin-bottom:1.5rem;">
            With a customer base of just <strong>100 active Australian subscribers</strong>, your monthly revenue reaches <strong>$2,000 AUD</strong> against a wholesale cost of only <strong>$450 AUD</strong>—generating <strong>$1,550 AUD net profit every single month ($18,600 AUD annually)</strong>. Reseller credits never expire, and our dashboard includes an automated 24-hour trial generator to convert Aussie prospects on the spot.
          </p>
        </div>

        <div style="display:flex; gap:1rem; flex-wrap:wrap;">
          <a href="reseller.html" class="btn btn-gold btn-lg"><i class="fa-solid fa-graduation-cap"></i> Read Complete Reseller Guide</a>
          <button class="btn btn-primary btn-lg" data-open-modal="reseller"><i class="fa-solid fa-rocket"></i> Apply for Reseller Panel</button>
          <a href="https://wa.me/61400000000?text=Hi%20I%20want%20Australian%20IPTV%20Reseller%20Panel%20Information" target="_blank" class="btn btn-whatsapp btn-lg"><i class="fa-brands fa-whatsapp"></i> Chat with Aussie Reseller Manager</a>
        </div>
      </div>

      <!-- Section 6: Australian IPTV Glossary of Terms -->
      <div class="glass-card">
        <span class="badge badge-glow-cyan" style="margin-bottom:0.75rem;"><i class="fa-solid fa-book"></i> Streaming Terminology</span>
        <h2 style="font-size:1.6rem; color:#fff; margin-bottom:1.25rem;">Australian IPTV Glossary & Technical Concepts</h2>
        
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.25rem;">
          <div style="background:rgba(0,0,0,0.3); padding:1rem; border-radius:var(--radius-sm);">
            <h4 style="color:var(--primary); font-size:0.95rem; margin-bottom:0.3rem;">M3U / M3U8 Playlist</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">A plain-text playlist file containing live stream URL endpoints for media players like VLC, TiviMate, and IPTV Smarters.</p>
          </div>
          <div style="background:rgba(0,0,0,0.3); padding:1rem; border-radius:var(--radius-sm);">
            <h4 style="color:var(--aus-gold); font-size:0.95rem; margin-bottom:0.3rem;">Xtream Codes API</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">A standardized login protocol consisting of a Server URL, Username, and Password that organizes Live TV, Movies, and Series.</p>
          </div>
          <div style="background:rgba(0,0,0,0.3); padding:1rem; border-radius:var(--radius-sm);">
            <h4 style="color:var(--secondary); font-size:0.95rem; margin-bottom:0.3rem;">Electronic Program Guide (EPG)</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">An interactive digital TV schedule providing Australian viewers with 7-day upcoming show listings and channel descriptions.</p>
          </div>
          <div style="background:rgba(0,0,0,0.3); padding:1rem; border-radius:var(--radius-sm);">
            <h4 style="color:var(--primary); font-size:0.95rem; margin-bottom:0.3rem;">Anti-Freeze Technology v9.4</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">Proprietary load-balancing algorithms that dynamically reroute video packets around congested Australian ISP peering nodes.</p>
          </div>
          <div style="background:rgba(0,0,0,0.3); padding:1rem; border-radius:var(--radius-sm);">
            <h4 style="color:var(--aus-gold); font-size:0.95rem; margin-bottom:0.3rem;">Cloudflare 1.1.1.1 DNS</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">A ultra-fast privacy-focused DNS resolver that bypasses Telstra and Optus transparent proxies for instant channel loading.</p>
          </div>
          <div style="background:rgba(0,0,0,0.3); padding:1rem; border-radius:var(--radius-sm);">
            <h4 style="color:var(--secondary); font-size:0.95rem; margin-bottom:0.3rem;">PayID & Osko Transfer</h4>
            <p style="font-size:0.82rem; color:var(--text-dim); margin:0;">Australian real-time interbank payment system enabling instant settlement in AUD with Commonwealth, ANZ, NAB, and Westpac.</p>
          </div>
        </div>
      </div>

    </div>
  </section>
"""

# Replace the existing seo-knowledge-hub section in index.html with the supercharged version
with open(index_path, "r", encoding="utf-8") as f:
    current_html = f.read()

# Replace or add before footer
if '<section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5rem 0;" id="seo-knowledge-hub">' in current_html:
    pattern = re.compile(r'<section class="section-padding-lg" style="background:var\(--bg-secondary\); border-top:1px solid var\(--border-color\); padding: 5rem 0;" id="seo-knowledge-hub">.*?</section>', re.DOTALL)
    new_html = pattern.sub(deep_seo_html.strip(), current_html)
else:
    new_html = current_html.replace("<!-- ==================== 12. FOOTER ==================== -->", deep_seo_html + "\n  <!-- ==================== 12. FOOTER ==================== -->")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("SUCCESS: index.html has been supercharged with comprehensive Australian search keywords and authority SEO sections!")

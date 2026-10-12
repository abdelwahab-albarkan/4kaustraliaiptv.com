import os, re

BASE_DIR = r"c:\Users\clanm\OneDrive\Desktop\australiatv"
index_path = os.path.join(BASE_DIR, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Build the rich SEO section to insert before footer
seo_section = """
  <!-- ==================== 11.5 MEGA AUSTRALIAN SEO RESEARCH LIBRARY & DIRECTORY (2,000+ PAGES) ==================== -->
  <section class="section-padding-lg" style="background:var(--bg-secondary); border-top:1px solid var(--border-color); padding: 5rem 0;" id="seo-knowledge-hub">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-layer-group"></i> 2,000+ Page Australian Knowledge Library</span>
        <h2 class="section-title">The Definitive Australian IPTV & Reseller Research Hub 2026</h2>
        <p class="section-subtitle">Comprehensive coverage of Australian streaming infrastructure, location-based city hubs, 4K sports schedules, device installation wizards, and Telstra/Optus NBN anti-throttling protocols.</p>
      </div>

      <!-- 8-Card Knowledge Grid -->
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.5rem; margin-bottom:3.5rem;">
        <div class="glass-card" style="padding:1.5rem;">
          <div style="font-size:1.8rem; color:var(--primary); margin-bottom:0.6rem;"><i class="fa-solid fa-city"></i></div>
          <h3 style="font-size:1.15rem; margin-bottom:0.4rem;">800+ City Hubs</h3>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">Dedicated low-latency servers across Sydney, Melbourne, Brisbane, Perth, Adelaide & Gold Coast.</p>
          <a href="directory/index.html#cities" style="font-size:0.85rem; font-weight:700; color:var(--primary);">Explore City Hubs →</a>
        </div>

        <div class="glass-card" style="padding:1.5rem;">
          <div style="font-size:1.8rem; color:var(--aus-gold); margin-bottom:0.6rem;"><i class="fa-solid fa-football"></i></div>
          <h3 style="font-size:1.15rem; margin-bottom:0.4rem;">Aussie Sports 4K</h3>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">AFL Premiership, NRL Telstra, State of Origin, The Ashes Cricket, F1 & UFC PPV in 4K UHD.</p>
          <a href="directory/index.html#sports" style="font-size:0.85rem; font-weight:700; color:var(--aus-gold);">Browse 4K Sports →</a>
        </div>

        <div class="glass-card" style="padding:1.5rem;">
          <div style="font-size:1.8rem; color:var(--secondary); margin-bottom:0.6rem;"><i class="fa-solid fa-mobile-screen"></i></div>
          <h3 style="font-size:1.15rem; margin-bottom:0.4rem;">Device Wizards</h3>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">5-minute installation guides for Firestick 4K, Samsung/LG Smart TVs, TiviMate & Apple TV.</p>
          <a href="directory/index.html#devices" style="font-size:0.85rem; font-weight:700; color:var(--secondary);">View Setup Guides →</a>
        </div>

        <div class="glass-card" style="padding:1.5rem;">
          <div style="font-size:1.8rem; color:var(--primary); margin-bottom:0.6rem;"><i class="fa-solid fa-coins"></i></div>
          <h3 style="font-size:1.15rem; margin-bottom:0.4rem;">Reseller Academy</h3>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">Wholesale AUD credits ($2.20-$4.50), white-label panels, and Australian marketing guides.</p>
          <a href="reseller.html" style="font-size:0.85rem; font-weight:700; color:var(--primary);">Reseller Portal →</a>
        </div>
      </div>

      <!-- High-Volume Australian Search Keyword Clusters -->
      <div class="glass-card" style="padding:2.5rem; margin-bottom:3rem;">
        <h3 style="font-size:1.4rem; margin-bottom:1.25rem; color:#fff;"><i class="fa-solid fa-magnifying-glass" style="color:var(--primary); margin-right:0.5rem;"></i> High-Intent Australian Search Clusters</h3>
        <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">
          Our streaming infrastructure is engineered to serve the most demanded television and sports broadcasts across Australia:
        </p>

        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem;">
          <div>
            <h4 style="color:var(--primary); font-size:1rem; margin-bottom:0.6rem;"><i class="fa-solid fa-trophy"></i> Australian Sports & Footy</h4>
            <ul style="list-style:none; display:flex; flex-direction:column; gap:0.4rem; font-size:0.88rem; color:var(--text-muted);">
              <li>• <a href="sports/afl-live-stream-iptv/index.html">AFL Live Stream & Fox Footy 504 HD</a></li>
              <li>• <a href="sports/nrl-live-stream-iptv/index.html">NRL Telstra Premiership & Fox League 502</a></li>
              <li>• <a href="sports/state-of-origin-4k-iptv/index.html">State of Origin Game I, II & III in 4K UHD</a></li>
              <li>• <a href="sports/cricket-australia-the-ashes-iptv/index.html">Cricket Australia, The Ashes & BBL</a></li>
              <li>• <a href="sports/premier-league-optus-sport-alternative/index.html">Premier League (Optus Sport Alternative)</a></li>
              <li>• <a href="sports/super-rugby-pacific-iptv/index.html">Super Rugby Pacific (Stan Sport 4K)</a></li>
              <li>• <a href="sports/formula-1-australian-gp-iptv/index.html">Formula 1 Australian Grand Prix Melbourne</a></li>
              <li>• <a href="sports/ufc-ppv-main-event-australia-iptv/index.html">UFC PPV Main Event 4K Australia</a></li>
            </ul>
          </div>

          <div>
            <h4 style="color:var(--aus-gold); font-size:1rem; margin-bottom:0.6rem;"><i class="fa-solid fa-tv"></i> Pay-TV & Streaming Alternatives</h4>
            <ul style="list-style:none; display:flex; flex-direction:column; gap:0.4rem; font-size:0.88rem; color:var(--text-muted);">
              <li>• <a href="comparisons/foxtel-alternative-iptv-australia/index.html">Best Foxtel Alternative in Australia</a></li>
              <li>• <a href="comparisons/kayo-sports-alternative-iptv-australia/index.html">Kayo Sports Alternative in 4K UHD</a></li>
              <li>• <a href="comparisons/stan-sport-alternative-iptv-australia/index.html">Stan Sport Alternative in Australia</a></li>
              <li>• <a href="comparisons/optus-sport-alternative-iptv-australia/index.html">Optus Sport Alternative with 4K EPL</a></li>
              <li>• <a href="comparisons/binge-alternative-iptv-australia/index.html">Binge Alternative (160,000+ VOD Movies)</a></li>
              <li>• <a href="comparisons/fetch-tv-alternative-iptv-australia/index.html">Fetch TV Ultimate Channel Packs</a></li>
              <li>• <a href="providers.html">Compare 15+ Australian IPTV Providers</a></li>
            </ul>
          </div>

          <div>
            <h4 style="color:var(--secondary); font-size:1rem; margin-bottom:0.6rem;"><i class="fa-solid fa-location-dot"></i> Australian Capital Cities & Regions</h4>
            <ul style="list-style:none; display:flex; flex-direction:column; gap:0.4rem; font-size:0.88rem; color:var(--text-muted);">
              <li>• <a href="cities/sydney/index.html">IPTV Sydney & Greater Western Sydney (NSW)</a></li>
              <li>• <a href="cities/melbourne/index.html">IPTV Melbourne & St Kilda / Richmond (VIC)</a></li>
              <li>• <a href="cities/brisbane/index.html">IPTV Brisbane & Gold Coast / Logan (QLD)</a></li>
              <li>• <a href="cities/perth/index.html">IPTV Perth & Fremantle / Joondalup (WA)</a></li>
              <li>• <a href="cities/adelaide/index.html">IPTV Adelaide & Glenelg / Marion (SA)</a></li>
              <li>• <a href="cities/canberra/index.html">IPTV Canberra & ACT Region</a></li>
              <li>• <a href="cities/hobart/index.html">IPTV Hobart & Launceston (TAS)</a></li>
              <li>• <a href="directory/index.html">Browse All 2,000+ Australian Pages</a></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- State & Regional Network Hubs -->
      <div class="glass-card" style="padding:2rem;">
        <h3 style="font-size:1.3rem; margin-bottom:1rem; color:#fff;"><i class="fa-solid fa-earth-oceania" style="color:var(--primary); margin-right:0.5rem;"></i> Australian Broadband & ISP Optimization Directory</h3>
        <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:1.25rem;">
          Tested for 0% buffering across all Australian NBN tiers (NBN 25, NBN 50, NBN 100, NBN 250, and 5G Home Wireless):
        </p>
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem;">
          <a href="isps/telstra-nbn-iptv-anti-freeze-guide/index.html" class="sport-tag"><i class="fa-solid fa-network-wired"></i> Telstra NBN Anti-Freeze</a>
          <a href="isps/optus-broadband-iptv-optimization/index.html" class="sport-tag"><i class="fa-solid fa-network-wired"></i> Optus Broadband DNS Fix</a>
          <a href="isps/tpg-internet-iptv-anti-buffering-guide/index.html" class="sport-tag"><i class="fa-solid fa-network-wired"></i> TPG NBN Bypass</a>
          <a href="isps/aussie-broadband-iptv-speed-guide/index.html" class="sport-tag"><i class="fa-solid fa-network-wired"></i> Aussie Broadband 8ms Peering</a>
          <a href="isps/starlink-australia-satellite-iptv-guide/index.html" class="sport-tag"><i class="fa-solid fa-satellite"></i> Starlink Satellite Australia</a>
          <a href="guides/is-iptv-legal-in-australia-2026-guide/index.html" class="sport-tag"><i class="fa-solid fa-scale-balanced"></i> Australian IPTV Legal Guide</a>
          <a href="guides/how-to-fix-iptv-buffering-australia/index.html" class="sport-tag"><i class="fa-solid fa-wrench"></i> Fix IPTV Buffering in Australia</a>
          <a href="guides/best-vpn-for-iptv-australia-2026/index.html" class="sport-tag"><i class="fa-solid fa-shield-halved"></i> Best VPN for Australia IPTV</a>
        </div>
      </div>
    </div>
  </section>
"""

# Insert before footer
if "<!-- ==================== 12. FOOTER ==================== -->" in html_content:
    new_html = html_content.replace("<!-- ==================== 12. FOOTER ==================== -->", seo_section + "\n  <!-- ==================== 12. FOOTER ==================== -->")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Enriched index.html with 2000+ Page SEO Knowledge Hub successfully!")
else:
    print("Could not find footer anchor in index.html")

import os

providers_path = r"c:\Users\clanm\OneDrive\Desktop\australiatv\providers.html"

with open(providers_path, "r", encoding="utf-8") as f:
    p_html = f.read()

provider_visuals = """
      <!-- Provider Infographic Banner -->
      <div style="margin-bottom:3rem; text-align:center;">
        <div style="position:relative; border-radius:var(--radius-md); overflow:hidden; border:1px solid var(--border-gold); display:inline-block; max-width:100%; box-shadow:0 12px 35px rgba(0,0,0,0.6);">
          <img src="images/provider-comparison.webp" alt="Australian IPTV Providers Comparison 2026" style="width:100%; max-height:360px; object-fit:cover; display:block;" />
          <div style="position:absolute; bottom:12px; left:16px; background:rgba(10,6,20,0.9); padding:0.4rem 1.2rem; border-radius:var(--radius-sm); border:1px solid var(--border-gold);">
            <span style="color:var(--aus-gold); font-weight:800; font-size:1.05rem;">2026 Vetted & Benchmarked</span> • Sydney & Melbourne Peering
          </div>
        </div>
      </div>

      <!-- Visual Provider Cards Grid -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.75rem; margin-bottom:3.5rem;">
        <div class="glass-card" style="border-color:var(--border-gold);">
          <div style="border-radius:var(--radius-sm); overflow:hidden; margin-bottom:1rem; border:1px solid var(--border-gold);">
            <img src="images/apps-dashboard.webp" alt="Trex IPTV AU" style="width:100%; height:140px; object-fit:cover; display:block;" />
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <h3 style="color:#fff; font-size:1.25rem; margin:0;"><i class="fa-solid fa-dragon" style="color:var(--aus-gold); margin-right:0.35rem;"></i> Trex IPTV AU</h3>
            <span class="badge badge-glow-gold">4.95/5 #1</span>
          </div>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">Top-rated for AFL, NRL, and Australian local channels with 8ms Sydney latency.</p>
          <a href="index.html#trial" class="btn btn-gold btn-sm btn-block">Get Free Trex Trial</a>
        </div>

        <div class="glass-card">
          <div style="border-radius:var(--radius-sm); overflow:hidden; margin-bottom:1rem; border:1px solid var(--border-color);">
            <img src="images/quality-4k.webp" alt="Ultra 8K IPTV AU" style="width:100%; height:140px; object-fit:cover; display:block;" />
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <h3 style="color:#fff; font-size:1.25rem; margin:0;"><i class="fa-solid fa-gem" style="color:var(--primary); margin-right:0.35rem;"></i> Ultra 8K IPTV</h3>
            <span class="badge badge-glow-cyan">4.90/5</span>
          </div>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">Pristine 8K/4K uncompressed stadium feeds engineered for OLED screens.</p>
          <a href="index.html#trial" class="btn btn-primary btn-sm btn-block">Get Ultra 8K Trial</a>
        </div>

        <div class="glass-card">
          <div style="border-radius:var(--radius-sm); overflow:hidden; margin-bottom:1rem; border:1px solid var(--border-color);">
            <img src="images/vod-dashboard.webp" alt="5GLive AU" style="width:100%; height:140px; object-fit:cover; display:block;" />
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <h3 style="color:#fff; font-size:1.25rem; margin:0;"><i class="fa-solid fa-globe-oceania" style="color:var(--secondary); margin-right:0.35rem;"></i> 5GLive Australia</h3>
            <span class="badge badge-glow-green">4.85/5</span>
          </div>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;">Leader for multicultural TV: Hindi, Arabic, Greek, Italian + 4K IPL cricket.</p>
          <a href="index.html#trial" class="btn btn-primary btn-sm btn-block">Get 5GLive Trial</a>
        </div>
      </div>
"""

if "Provider Infographic Banner" not in p_html:
    p_html = p_html.replace('<!-- Comparison Matrix -->', provider_visuals + '\n      <!-- Comparison Matrix -->', 1)
    with open(providers_path, "w", encoding="utf-8") as f:
        f.write(p_html)
    print("Updated providers.html with infographic and cards!")

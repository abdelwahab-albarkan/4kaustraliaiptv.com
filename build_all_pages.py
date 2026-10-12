import os, sys, re, json, html
from collections import defaultdict
from seo_engine_init import (
    cities_list, sports_list, devices_list, competitors_list,
    isps_list, languages_list, guides_list, parsed_kws
)
from seo_page_renderer import render_seo_page, slugify

BASE_DIR = r"c:\Users\clanm\OneDrive\Desktop\australiatv"
SITE_URL = "https://4kaustraliaiptv.com"

generated_urls = []

print("Starting generation of 2000+ Australian SEO pages...")

def write_page(rel_dir, fname, content, canonical_path):
    target_dir = os.path.join(BASE_DIR, rel_dir)
    os.makedirs(target_dir, exist_ok=True)
    file_path = os.path.join(target_dir, fname)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    clean_url = f"{SITE_URL}/{canonical_path.lstrip('/')}"
    generated_urls.append((clean_url, rel_dir))

# -------------------------------------------------------------
# 1. GENERATE CITY & SUBURB PAGES (800+ PAGES)
# -------------------------------------------------------------
city_angles = [
    ("best-iptv", "Best IPTV {city} 2026 | #1 4K Australian Streaming", "Best IPTV in {city}, {state} (2026 Updated)", "Compare and stream the top rated IPTV service in {city} with 50,000+ live channels, AFL, NRL and 4K movies on local {city} low-latency servers.", "Best Rated in {city}"),
    ("subscription", "IPTV Subscription {city} {state} | Instant M3U & Xtream Codes", "Premium IPTV Subscription in {city}", "Get instant IPTV subscription in {city}, {state} with AUD pricing, PayID activation, and zero buffering on Telstra and Optus NBN.", "Instant {city} Activation"),
    ("free-trial", "IPTV Free Trial {city} | 24-Hour 4K Sports Access", "24-Hour Free IPTV Trial in {city}, {state}", "Test all Australian live sports, AFL, NRL, and 160,000+ VOD movies in {city} with our 100% free 24h trial. No credit card needed.", "Free 24H Trial {city}"),
    ("sports-channels", "Watch AFL & NRL IPTV in {city} | Fox Sports & Stan 4K", "Live Sports & Footy IPTV in {city}, {state}", "Stream every AFL, NRL, Cricket, and Premier League match live in 4K UHD in {city} with uncompressed 60FPS high-bitrate feeds.", "Live Sports {city}"),
    ("firestick-setup", "How to Setup IPTV on Firestick in {city} {state}", "Firestick 4K IPTV Installation Guide for {city}", "Step-by-step tutorial to install IPTV Smarters and TiviMate on Amazon Firestick 4K in {city} with local anti-buffering settings.", "{city} Setup Guide"),
    ("reseller-panel", "IPTV Reseller Panel {city} {state} | Wholesale AUD Credits", "Start an IPTV Reseller Business in {city}", "Launch your branded IPTV reseller business in {city}, {state}. Wholesale credits from $2.20 AUD, white-label panel, and 400% profit margins.", "{city} Reseller Hub")
]

for city, state, suburbs in cities_list:
    city_slug = slugify(city)
    
    # Generate main city hub
    main_title = f"IPTV {city} {state} | Best IPTV Service & Reseller in {city} 2026"
    main_desc = f"Looking for the best IPTV in {city}, {state}? Stream 50,000+ channels, AFL, NRL, Cricket and 4K movies with 8ms low latency in {city}. Free 24h trial."
    main_h1 = f"IPTV {city}, {state} - #1 4K Streaming & Reseller Panel"
    main_h2 = f"Ultra-fast IPTV service optimized for {city} and surrounding suburbs ({suburbs}). Stream AFL, NRL, Fox Sports, Stan Sport and 160,000+ VOD movies on Telstra, Optus & Aussie Broadband NBN."
    
    content_html = f"""
    <div class="glass-card" style="margin-bottom:2.5rem;">
      <h2 style="font-size:1.8rem; margin-bottom:1rem; color:#fff;">Why Viewers in {city}, {state} Choose IPTV Australia</h2>
      <p style="color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">
        Residents across <strong>{city} ({suburbs})</strong> are cutting the cord on traditional $100+/month cable bills. Our dedicated Australian servers provide crystal-clear 4K and Full HD streams with <strong>under 15ms latency</strong> directly into {state} homes. Whether you are watching Friday night footy at home or managing an IPTV reseller business in {city}, our platform guarantees 99.98% uptime and zero buffering.
      </p>
      
      <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:1.5rem; margin-top:2rem;">
        <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
          <h4 style="color:var(--primary); margin-bottom:0.4rem;"><i class="fa-solid fa-tv"></i> Local {city} Channels</h4>
          <p style="font-size:0.88rem; color:var(--text-dim);">Channel 7 HD, 9HD, 10HD, ABC, SBS, Fox Footy, Fox League, and 50,000+ global channels.</p>
        </div>
        <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
          <h4 style="color:var(--aus-gold); margin-bottom:0.4rem;"><i class="fa-solid fa-server"></i> {state} Low Ping</h4>
          <p style="font-size:0.88rem; color:var(--text-dim);">Dedicated Sydney & Melbourne CDN nodes ensuring 8ms - 15ms ping times across {city}.</p>
        </div>
        <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
          <h4 style="color:var(--secondary); margin-bottom:0.4rem;"><i class="fa-solid fa-credit-card"></i> AUD & PayID</h4>
          <p style="font-size:0.88rem; color:var(--text-dim);">Direct Australian banking with PayID, Osko, Apple Pay, and Visa/Mastercard.</p>
        </div>
      </div>
    </div>

    <!-- Suburbs Grid -->
    <div class="glass-card">
      <h3 style="font-size:1.4rem; margin-bottom:1rem;">Coverage Areas in {city} & Greater {state}</h3>
      <p style="font-size:0.95rem; color:var(--text-muted); margin-bottom:1.25rem;">
        We provide high-speed streaming infrastructure across all suburbs of {city}:
      </p>
      <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
        {' '.join([f'<span class="sport-tag">{sub.strip()}</span>' for sub in suburbs.split(',')])}
      </div>
    </div>
    """

    faq_city = [
        (f"How fast is IPTV in {city}, {state}?", f"Our servers deliver under 15ms latency across {city} using high-speed Australian CDN nodes. Standard 25Mbps NBN or 5G home internet is more than enough for 4K streaming."),
        (f"Can I watch AFL & NRL live in {city}?", f"Yes! You get full access to Fox Footy 504 HD, Fox League 502 HD, Channel 7HD, and 9HD with zero blackouts in {city}."),
        (f"How do I get an IPTV free trial in {city}?", f"Click 'Free 24H Trial' anywhere on this page, enter your email and device type, and your M3U and Xtream codes will be generated instantly."),
        (f"Can I become an IPTV reseller in {city}?", f"Yes! You can purchase wholesale reseller credits in AUD (starting from $2.20 AUD/credit) and resell subscriptions to customers in {city} and across Australia.")
    ]

    # Render main city page
    html_out = render_seo_page(
        title=main_title,
        meta_desc=main_desc,
        h1=main_h1,
        h2=main_h2,
        badge_text=f"{city} #1 IPTV",
        category_name="Cities",
        category_url="directory/index.html#cities",
        canonical_url=f"{SITE_URL}/cities/{city_slug}/",
        content_html=content_html,
        faq_list=faq_city,
        rel_path_to_root="../../",
        breadcrumbs=[("Home", "../../index.html"), ("Cities", "../../directory/index.html#cities"), (f"{city}, {state}", "")]
    )
    write_page(f"cities/{city_slug}", "index.html", html_out, f"/cities/{city_slug}/")

    # Render 6 intent angles per city
    for a_slug, a_title_tpl, a_h1_tpl, a_desc_tpl, a_badge_tpl in city_angles:
        sub_title = a_title_tpl.format(city=city, state=state)
        sub_desc = a_desc_tpl.format(city=city, state=state)
        sub_h1 = a_h1_tpl.format(city=city, state=state)
        sub_h2 = f"Optimized for viewers and resellers in {city}, {state} ({suburbs}). Stream in 4K UHD with Telstra and Optus NBN anti-buffering protection."
        sub_badge = a_badge_tpl.format(city=city, state=state)

        sub_content = f"""
        <div class="glass-card">
          <h2 style="font-size:1.6rem; margin-bottom:1rem;">{sub_h1}</h2>
          <p style="color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">
            {sub_desc}
          </p>
          <div style="background:rgba(0,0,0,0.3); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color); margin-top:1.5rem;">
            <h4 style="color:var(--primary); margin-bottom:0.5rem;"><i class="fa-solid fa-circle-check"></i> {city} Quick Features</h4>
            <ul style="list-style:none; display:flex; flex-direction:column; gap:0.5rem; font-size:0.9rem; color:var(--text-muted);">
              <li>• Compatible with Amazon Firestick, Samsung TV, LG TV, Android TV and Apple TV in {city}</li>
              <li>• AFL, NRL, Cricket, F1 and Premier League in 4K 60FPS</li>
              <li>• Instant PayID, Credit Card & Apple Pay activation in AUD</li>
              <li>• Local 24/7 Aussie support on WhatsApp and Telegram</li>
            </ul>
          </div>
        </div>
        """

        sub_html = render_seo_page(
            title=sub_title,
            meta_desc=sub_desc,
            h1=sub_h1,
            h2=sub_h2,
            badge_text=sub_badge,
            category_name=city,
            category_url=f"cities/{city_slug}/index.html",
            canonical_url=f"{SITE_URL}/cities/{city_slug}/{a_slug}/",
            content_html=sub_content,
            faq_list=faq_city,
            rel_path_to_root="../../../",
            breadcrumbs=[("Home", "../../../index.html"), ("Cities", "../../../directory/index.html#cities"), (city, f"../index.html"), (a_slug.replace("-", " ").title(), "")]
        )
        write_page(f"cities/{city_slug}/{a_slug}", "index.html", sub_html, f"/cities/{city_slug}/{a_slug}/")

# -------------------------------------------------------------
# 2. GENERATE SPORTS & LIVE EVENTS PAGES (250+ PAGES)
# -------------------------------------------------------------
sports_angles = [
    ("4k-live-stream", "Watch {name} 4K Live Stream in Australia | Zero Buffering", "Watch {name} in 4K Live Stream", "Stream every moment of {name} in crystal-clear 4K 60FPS with dedicated Australian sports feeds.", "4K Live Stream"),
    ("without-foxtel", "How to Watch {name} Without Foxtel in Australia (Save $1000+)", "Watch {name} Without Foxtel or Kayo", "Ditch expensive cable subscriptions and watch full {name} coverage for only $15 AUD/month.", "No Foxtel Required"),
    ("free-trial", "Free Trial for {name} Live Stream | 24-Hour Pass", "{name} 24-Hour Free Streaming Pass", "Test our high-bitrate live feeds for {name} with a 100% free 24h pass on your TV or Firestick.", "24H Free Pass"),
    ("fixtures-schedule", "{name} 2026 TV Schedule & Australian Channel List", "{name} 2026 TV Guide & Broadcast Channels", "Complete fixture broadcast guide for {name} across Fox Sports, Channel 7, Channel 9, and Stan Sport.", "Broadcast Guide")
]

for s_slug, s_title, s_chans, s_name, s_desc in sports_list:
    main_title = f"{s_title} | IPTV Australia 2026"
    main_desc = f"Watch {s_name} live in 4K Ultra HD in Australia. {s_desc} Channels: {s_chans}."
    main_h1 = s_title
    main_h2 = f"Stream {s_name} live on your TV, Firestick, or phone in 4K 60FPS. Dedicated channels: {s_chans}. Zero buffering on Australian NBN."

    content_html = f"""
    <div class="glass-card" style="margin-bottom:2rem;">
      <h2 style="font-size:1.8rem; margin-bottom:1rem;">Complete {s_name} Broadcast Coverage in Australia</h2>
      <p style="color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">
        {s_desc}
      </p>
      
      <div style="background:rgba(0,0,0,0.35); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
        <h4 style="color:var(--primary); margin-bottom:0.75rem;"><i class="fa-solid fa-satellite-dish"></i> Included Channels for {s_name}:</h4>
        <p style="color:#fff; font-size:1rem; font-weight:600; margin-bottom:1rem;">{s_chans}</p>
        <p style="font-size:0.88rem; color:var(--text-dim); margin:0;">All matches and PPV events are broadcast in 4K UHD and Full HD 60FPS with zero extra pay-per-view fees.</p>
      </div>
    </div>
    """

    faq_sport = [
        (f"What channels broadcast {s_name}?", f"Our service includes {s_chans} with full HD and 4K resolution."),
        (f"Can I watch {s_name} on my Firestick or Smart TV?", f"Yes! Setup takes under 5 minutes on Amazon Firestick, Samsung TV, LG TV, Apple TV, and Android TV."),
        (f"Will there be blackouts or buffering during {s_name}?", f"No. We use dedicated anti-freeze CDN edge servers located in Sydney and Melbourne that bypass ISP throttling completely.")
    ]

    html_out = render_seo_page(
        title=main_title,
        meta_desc=main_desc,
        h1=main_h1,
        h2=main_h2,
        badge_text="4K Sports AU",
        category_name="Sports",
        category_url="directory/index.html#sports",
        canonical_url=f"{SITE_URL}/sports/{s_slug}/",
        content_html=content_html,
        faq_list=faq_sport,
        rel_path_to_root="../../",
        breadcrumbs=[("Home", "../../index.html"), ("Sports", "../../directory/index.html#sports"), (s_name, "")]
    )
    write_page(f"sports/{s_slug}", "index.html", html_out, f"/sports/{s_slug}/")

    # Sub angles for sports
    for a_slug, a_title_tpl, a_h1_tpl, a_desc_tpl, a_badge in sports_angles:
        sub_title = a_title_tpl.format(name=s_name)
        sub_desc = a_desc_tpl.format(name=s_name)
        sub_h1 = a_h1_tpl.format(name=s_name)

        sub_html = render_seo_page(
            title=f"{sub_title} | IPTV Australia",
            meta_desc=sub_desc,
            h1=sub_h1,
            h2=f"High-bitrate uncompressed feeds for {s_name}. Channels: {s_chans}.",
            badge_text=a_badge,
            category_name=s_name,
            category_url=f"sports/{s_slug}/index.html",
            canonical_url=f"{SITE_URL}/sports/{s_slug}/{a_slug}/",
            content_html=content_html,
            faq_list=faq_sport,
            rel_path_to_root="../../../",
            breadcrumbs=[("Home", "../../../index.html"), ("Sports", "../../../directory/index.html#sports"), (s_name, f"../index.html"), (a_badge, "")]
        )
        write_page(f"sports/{s_slug}/{a_slug}", "index.html", sub_html, f"/sports/{s_slug}/{a_slug}/")

# -------------------------------------------------------------
# 3. GENERATE DEVICES & APPS PAGES (150+ PAGES)
# -------------------------------------------------------------
for d_slug, d_title, d_apps, d_name, d_desc in devices_list:
    main_title = f"{d_title} IPTV Setup Guide Australia 2026"
    main_desc = f"{d_desc} Recommended apps: {d_apps}."
    main_h1 = f"How to Setup IPTV on {d_name} in Australia"
    main_h2 = f"Complete installation guide for {d_name}. Stream AFL, NRL, and 160,000+ VOD movies in 4K UHD using {d_apps}."

    content_html = f"""
    <div class="glass-card" style="margin-bottom:2rem;">
      <h2 style="font-size:1.7rem; margin-bottom:1rem;">{d_name} IPTV Installation Steps</h2>
      <p style="color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">{d_desc}</p>
      
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1.25rem;">
        <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
          <span class="step-number" style="position:static; margin-bottom:0.5rem;">1</span>
          <h4>Download App</h4>
          <p style="font-size:0.85rem; color:var(--text-dim);">Install one of the recommended apps: <strong>{d_apps}</strong>.</p>
        </div>
        <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
          <span class="step-number" style="position:static; margin-bottom:0.5rem;">2</span>
          <h4>Enter Credentials</h4>
          <p style="font-size:0.85rem; color:var(--text-dim);">Input your Server Portal URL, Username and Password from your trial email.</p>
        </div>
        <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
          <span class="step-number" style="position:static; margin-bottom:0.5rem;">3</span>
          <h4>Stream in 4K</h4>
          <p style="font-size:0.85rem; color:var(--text-dim);">Enjoy 50,000+ live channels and full Australian EPG TV guide automatically synced.</p>
        </div>
      </div>
    </div>
    """

    faq_device = [
        (f"What is the best IPTV app for {d_name} in Australia?", f"We recommend {d_apps} for the smoothest 60FPS playback and 7-day EPG guide support."),
        (f"Do I need a VPN when using {d_name} in Australia?", f"A VPN is not mandatory because our servers feature anti-ISP throttling, but Cloudflare 1.1.1.1 DNS is recommended on Telstra and Optus.")
    ]

    html_out = render_seo_page(
        title=main_title,
        meta_desc=main_desc,
        h1=main_h1,
        h2=main_h2,
        badge_text=f"{d_name} Guide",
        category_name="Devices",
        category_url="directory/index.html#devices",
        canonical_url=f"{SITE_URL}/devices/{d_slug}/",
        content_html=content_html,
        faq_list=faq_device,
        rel_path_to_root="../../",
        breadcrumbs=[("Home", "../../index.html"), ("Devices", "../../directory/index.html#devices"), (d_name, "")]
    )
    write_page(f"devices/{d_slug}", "index.html", html_out, f"/devices/{d_slug}/")

# -------------------------------------------------------------
# 4. GENERATE COMPARISONS & ALTERNATIVES (100+ PAGES)
# -------------------------------------------------------------
for c_slug, c_title, c_features, c_name, c_desc in competitors_list:
    main_title = f"{c_title} 2026 | Cut The Cord"
    main_desc = f"{c_desc} Feature comparison: {c_features}."
    main_h1 = c_title
    main_h2 = c_desc

    content_html = f"""
    <div class="glass-card">
      <h2 style="font-size:1.7rem; margin-bottom:1rem;">How IPTV Compares to {c_name} in Australia</h2>
      <p style="color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">{c_desc}</p>
      
      <div style="overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.92rem;">
          <thead>
            <tr style="border-bottom:2px solid var(--border-color); color:var(--primary);">
              <th style="padding:1rem;">Feature</th>
              <th style="padding:1rem;">IPTV Australia</th>
              <th style="padding:1rem;">{c_name}</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border-color);">
              <td style="padding:1rem; font-weight:700;">Monthly Price</td>
              <td style="padding:1rem; color:var(--secondary); font-weight:700;">$15 AUD / month</td>
              <td style="padding:1rem; color:#f43f5e;">$25 - $120+ AUD / month</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border-color);">
              <td style="padding:1rem; font-weight:700;">Live Channels</td>
              <td style="padding:1rem; color:var(--secondary); font-weight:700;">50,000+ Channels</td>
              <td style="padding:1rem;">Limited to 50 - 150 channels</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border-color);">
              <td style="padding:1rem; font-weight:700;">PPV Events (UFC & Boxing)</td>
              <td style="padding:1rem; color:var(--secondary); font-weight:700;">Included FREE</td>
              <td style="padding:1rem; color:#f43f5e;">Extra $60 - $80 per event</td>
            </tr>
            <tr>
              <td style="padding:1rem; font-weight:700;">Lock-in Contract</td>
              <td style="padding:1rem; color:var(--secondary); font-weight:700;">Zero Contract (Cancel Anytime)</td>
              <td style="padding:1rem;">12-24 Month Contracts</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """

    faq_comp = [
        (f"Is IPTV cheaper than {c_name} in Australia?", f"Yes. Standard {c_name} subscriptions cost $300 to $1,400+ per year. IPTV Australia gives you all sports, movies, and live channels for only $110 AUD/year."),
        (f"Can I cancel my {c_name} subscription and switch to IPTV?", f"Yes! You can test our free 24-hour trial to verify picture quality before making the switch.")
    ]

    html_out = render_seo_page(
        title=main_title,
        meta_desc=main_desc,
        h1=main_h1,
        h2=main_h2,
        badge_text="Save $1000+/yr",
        category_name="Comparisons",
        category_url="directory/index.html#comparisons",
        canonical_url=f"{SITE_URL}/comparisons/{c_slug}/",
        content_html=content_html,
        faq_list=faq_comp,
        rel_path_to_root="../../",
        breadcrumbs=[("Home", "../../index.html"), ("Comparisons", "../../directory/index.html#comparisons"), (c_name, "")]
    )
    write_page(f"comparisons/{c_slug}", "index.html", html_out, f"/comparisons/{c_slug}/")

# -------------------------------------------------------------
# 5. GENERATE ISPS, LANGUAGES & TECHNICAL GUIDES (200+ PAGES)
# -------------------------------------------------------------
for i_slug, i_title, i_settings, i_name, i_desc in isps_list:
    main_title = f"{i_title} 2026"
    main_desc = f"{i_desc} Recommended settings: {i_settings}."
    main_h1 = i_title
    main_h2 = i_desc

    content_html = f"""
    <div class="glass-card">
      <h2 style="font-size:1.7rem; margin-bottom:1rem;">{i_name} IPTV Optimization Settings</h2>
      <p style="color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">{i_desc}</p>
      <div style="background:rgba(0,0,0,0.35); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
        <h4 style="color:var(--primary); margin-bottom:0.5rem;"><i class="fa-solid fa-network-wired"></i> Key Configuration:</h4>
        <p style="color:#fff; font-size:0.95rem;">{i_settings}</p>
      </div>
    </div>
    """

    faq_isp = [
        (f"Does {i_name} block IPTV in Australia?", f"No, but {i_name} may apply transparent DNS filtering during peak sports hours. Setting DNS to 1.1.1.1 solves this completely.")
    ]

    html_out = render_seo_page(
        title=main_title,
        meta_desc=main_desc,
        h1=main_h1,
        h2=main_h2,
        badge_text="NBN Guide",
        category_name="ISPs",
        category_url="directory/index.html#isps",
        canonical_url=f"{SITE_URL}/isps/{i_slug}/",
        content_html=content_html,
        faq_list=faq_isp,
        rel_path_to_root="../../",
        breadcrumbs=[("Home", "../../index.html"), ("ISPs", "../../directory/index.html#isps"), (i_name, "")]
    )
    write_page(f"isps/{i_slug}", "index.html", html_out, f"/isps/{i_slug}/")

for l_slug, l_title, l_channels, l_name, l_desc in languages_list:
    main_title = f"{l_title} 2026"
    main_desc = f"{l_desc} Top channels: {l_channels}."
    main_h1 = l_title
    main_h2 = l_desc

    content_html = f"""
    <div class="glass-card">
      <h2 style="font-size:1.7rem; margin-bottom:1rem;">{l_name} Television in Australia</h2>
      <p style="color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">{l_desc}</p>
      <div style="background:rgba(0,0,0,0.35); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
        <h4 style="color:var(--primary); margin-bottom:0.5rem;"><i class="fa-solid fa-tv"></i> Featured Channels:</h4>
        <p style="color:#fff; font-size:0.95rem;">{l_channels}</p>
      </div>
    </div>
    """

    faq_lang = [
        (f"Can I watch {l_name} channels in Australia live?", f"Yes! You get direct high-definition streams with 7-day catch-up TV and extensive on-demand movies.")
    ]

    html_out = render_seo_page(
        title=main_title,
        meta_desc=main_desc,
        h1=main_h1,
        h2=main_h2,
        badge_text="Multicultural TV",
        category_name="Languages",
        category_url="directory/index.html#languages",
        canonical_url=f"{SITE_URL}/languages/{l_slug}/",
        content_html=content_html,
        faq_list=faq_lang,
        rel_path_to_root="../../",
        breadcrumbs=[("Home", "../../index.html"), ("Languages", "../../directory/index.html#languages"), (l_name, "")]
    )
    write_page(f"languages/{l_slug}", "index.html", html_out, f"/languages/{l_slug}/")

for g_slug, g_title, g_topics, g_name, g_desc in guides_list:
    main_title = f"{g_title} | IPTV Australia"
    main_desc = f"{g_desc} Key topics: {g_topics}."
    main_h1 = g_title
    main_h2 = g_desc

    content_html = f"""
    <div class="glass-card">
      <h2 style="font-size:1.7rem; margin-bottom:1rem;">{g_name} - Comprehensive Breakdown</h2>
      <p style="color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">{g_desc}</p>
      <div style="background:rgba(0,0,0,0.35); padding:1.5rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
        <h4 style="color:var(--primary); margin-bottom:0.5rem;"><i class="fa-solid fa-book-open"></i> Key Information Covered:</h4>
        <p style="color:#fff; font-size:0.95rem;">{g_topics}</p>
      </div>
    </div>
    """

    faq_guide = [
        (f"How do I apply this guide in Australia?", f"Follow the step-by-step instructions or message our 24/7 Australian WhatsApp support desk for direct assistance.")
    ]

    html_out = render_seo_page(
        title=main_title,
        meta_desc=main_desc,
        h1=main_h1,
        h2=main_h2,
        badge_text="Aussie Guide",
        category_name="Guides",
        category_url="directory/index.html#guides",
        canonical_url=f"{SITE_URL}/guides/{g_slug}/",
        content_html=content_html,
        faq_list=faq_guide,
        rel_path_to_root="../../",
        breadcrumbs=[("Home", "../../index.html"), ("Guides", "../../directory/index.html#guides"), (g_name, "")]
    )
    write_page(f"guides/{g_slug}", "index.html", html_out, f"/guides/{g_slug}/")

print(f"Primary programmatic pages generated. Total URLs: {len(generated_urls)}")

# -------------------------------------------------------------
# 6. GENERATE KEYWORD CLUSTERS FROM PARSED 97K DATASET (REACHING 2000+ PAGES)
# -------------------------------------------------------------
print("Generating targeted programmatic long-tail pages from Australian dataset...")

# Generate targeted localized search terms
target_intents = [
    ("best-iptv-subscription", "Best IPTV Subscription {kw} | 4K Channels 2026", "Best IPTV Subscription for {kw}"),
    ("cheap-iptv-channels", "Cheap IPTV {kw} | AFL, NRL & Foxtel Channels", "Affordable IPTV Streaming for {kw}"),
    ("iptv-free-trial-pass", "IPTV Free Trial {kw} | 24 Hours No Card", "24-Hour Free IPTV Trial for {kw}"),
    ("how-to-watch-live", "How to Watch {kw} Online in Australia (2026 Guide)", "Live Streaming Guide for {kw}")
]

# Pick high-value terms from dataset
dataset_terms = []
for p in parsed_kws:
    kw_raw = p["keyword"]
    # Filter for relevant Australian streaming keywords
    if any(term in kw_raw.lower() for term in ["iptv", "tv", "afl", "nrl", "cricket", "firestick", "smart tv", "stream", "foxtel", "kayo", "stan", "optus", "sydney", "melbourne", "brisbane", "perth", "adelaide"]):
        if len(kw_raw) > 3 and not kw_raw.isdigit():
            dataset_terms.append((kw_raw, p["volume"]))

# Deduplicate
seen_terms = set()
unique_terms = []
for kw, vol in dataset_terms:
    slug = slugify(kw)
    if slug not in seen_terms and len(slug) > 3:
        seen_terms.add(slug)
        unique_terms.append((kw, vol, slug))

print(f"Identified {len(unique_terms)} high-value Australian search terms.")

# Scale up to 2000+ total pages
for kw, vol, k_slug in unique_terms[:1400]:
    kw_title = kw.title()
    title = f"{kw_title} Australia 2026 | IPTV Reseller Panel & 4K Streaming"
    desc = f"Search guide and streaming portal for {kw_title} in Australia. Access 50,000+ live channels, AFL, NRL, and 160,000+ 4K movies with Sydney & Melbourne CDN edge servers."
    h1 = f"{kw_title} in Australia"
    h2 = f"Stream {kw_title} in 4K Ultra HD on your Smart TV, Firestick, or phone. Telstra & Optus NBN anti-freeze servers with local Australian support."

    content_html = f"""
    <div class="glass-card">
      <h2 style="font-size:1.7rem; margin-bottom:1rem;">{kw_title} - Australian Streaming Overview</h2>
      <p style="color:var(--text-muted); line-height:1.7; margin-bottom:1.5rem;">
        Searching for <strong>{kw_title}</strong> in Australia? IPTV Australia connects you with over 50,000 live channels, AFL Premiership, NRL Telstra season, Super Rugby, Cricket Australia, and 160,000+ on-demand movies.
      </p>
      <div style="background:rgba(0,0,0,0.35); padding:1.25rem; border-radius:var(--radius-md); border:1px solid var(--border-color);">
        <h4 style="color:var(--primary); margin-bottom:0.5rem;"><i class="fa-solid fa-bolt"></i> Instant Australian Access:</h4>
        <p style="font-size:0.9rem; color:var(--text-dim); margin:0;">
          Compatible with Amazon Firestick 4K, Samsung Smart TV, LG TV, TiviMate, Apple TV, and Android TV with instant PayID activation in AUD.
        </p>
      </div>
    </div>
    """

    faq_kw = [
        (f"How can I stream {kw_title} in Australia?", f"You can stream {kw_title} using our 24-hour free trial or monthly/yearly pass with instant setup on your TV or Firestick."),
        (f"Can I resell IPTV for {kw_title} in Australia?", f"Yes! Our Australian reseller panel allows you to sell subscriptions under your own brand with wholesale credits starting from $2.20 AUD.")
    ]

    html_out = render_seo_page(
        title=title,
        meta_desc=desc,
        h1=h1,
        h2=h2,
        badge_text="Australia 2026",
        category_name="Search Directory",
        category_url="directory/index.html",
        canonical_url=f"{SITE_URL}/topic/{k_slug}/",
        content_html=content_html,
        faq_list=faq_kw,
        rel_path_to_root="../../",
        breadcrumbs=[("Home", "../../index.html"), ("Directory", "../../directory/index.html"), (kw_title, "")]
    )
    write_page(f"topic/{k_slug}", "index.html", html_out, f"/topic/{k_slug}/")

print(f"Total Generated Programmatic Pages: {len(generated_urls)}")

# -------------------------------------------------------------
# 7. GENERATE COMPLETE MULTI-PART XML SITEMAPS & ROBOTS.TXT
# -------------------------------------------------------------
print("Building XML Sitemaps and robots.txt...")

sitemap_groups = defaultdict(list)
for u, rel_dir in generated_urls:
    if rel_dir.startswith("cities"):
        sitemap_groups["cities"].append(u)
    elif rel_dir.startswith("sports"):
        sitemap_groups["sports"].append(u)
    elif rel_dir.startswith("devices"):
        sitemap_groups["devices"].append(u)
    elif rel_dir.startswith("comparisons"):
        sitemap_groups["comparisons"].append(u)
    elif rel_dir.startswith("isps"):
        sitemap_groups["isps"].append(u)
    elif rel_dir.startswith("languages"):
        sitemap_groups["languages"].append(u)
    elif rel_dir.startswith("guides"):
        sitemap_groups["guides"].append(u)
    else:
        sitemap_groups["topics"].append(u)

# Core URLs
core_urls = [
    f"{SITE_URL}/",
    f"{SITE_URL}/reseller.html",
    f"{SITE_URL}/providers.html",
    f"{SITE_URL}/channels.html",
    f"{SITE_URL}/setup.html",
    f"{SITE_URL}/contact.html",
    f"{SITE_URL}/directory/index.html"
]

def make_sitemap_xml(url_list, priority="0.8"):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in url_list:
        xml += '  <url>\n'
        xml += f'    <loc>{html.escape(u)}</loc>\n'
        xml += '    <lastmod>2026-10-10</lastmod>\n'
        xml += '    <changefreq>weekly</changefreq>\n'
        xml += f'    <priority>{priority}</priority>\n'
        xml += '  </url>\n'
    xml += '</urlset>\n'
    return xml

# Write individual sitemaps
with open(os.path.join(BASE_DIR, "sitemap-core.xml"), "w", encoding="utf-8") as f:
    f.write(make_sitemap_xml(core_urls, "1.0"))

for group_name, urls in sitemap_groups.items():
    sitemap_file = f"sitemap-{group_name}.xml"
    with open(os.path.join(BASE_DIR, sitemap_file), "w", encoding="utf-8") as f:
        f.write(make_sitemap_xml(urls, "0.8"))

# Write Master sitemap index
master_sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
master_sitemap += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
master_sitemap += f'  <sitemap><loc>{SITE_URL}/sitemap-core.xml</loc><lastmod>2026-10-10</lastmod></sitemap>\n'
for group_name in sitemap_groups.keys():
    master_sitemap += f'  <sitemap><loc>{SITE_URL}/sitemap-{group_name}.xml</loc><lastmod>2026-10-10</lastmod></sitemap>\n'
master_sitemap += '</sitemapindex>\n'

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(master_sitemap)

# Write robots.txt
robots_txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)

# -------------------------------------------------------------
# 8. GENERATE INTERACTIVE DIRECTORY BROWSER (/directory/index.html)
# -------------------------------------------------------------
print("Building interactive directory hub (/directory/index.html)...")

dir_html = f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <meta name="theme-color" content="#0a0614" />
  <title>Australian IPTV Complete Research & Location Directory (2,000+ Pages) 2026</title>
  <meta name="description" content="Browse our complete 2,000+ page Australian IPTV research library. Locations, Australian sports in 4K, device setup tutorials, competitor alternatives, and reseller guides." />
  <link rel="stylesheet" href="../assets/css/style.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
</head>
<body>
  <div class="bg-glow-orb bg-orb-1"></div>
  <div class="bg-glow-orb bg-orb-2"></div>
  <div class="bg-grid-overlay"></div>

  <header class="site-header">
    <div class="container header-inner">
      <a href="../index.html" class="site-logo">
        <div class="logo-badge"><i class="fa-solid fa-earth-oceania"></i></div>
        <div class="logo-text">
          <span class="logo-brand">IPTV<span>AUSTRALIA</span></span>
          <span class="logo-sub">2000+ Page Directory</span>
        </div>
      </a>
      <nav class="main-nav">
        <a href="../index.html" class="nav-link"><i class="fa-solid fa-house"></i> Home</a>
        <a href="../reseller.html" class="nav-link"><i class="fa-solid fa-store"></i> Reseller Guide</a>
        <a href="../providers.html" class="nav-link"><i class="fa-solid fa-tv"></i> AU Providers</a>
        <a href="../channels.html" class="nav-link"><i class="fa-solid fa-futbol"></i> Aussie Sports</a>
        <a href="../setup.html" class="nav-link"><i class="fa-solid fa-wrench"></i> Setup Guides</a>
        <a href="index.html" class="nav-link active"><i class="fa-solid fa-compass"></i> Directory</a>
      </nav>
      <div class="header-actions">
        <a href="../index.html#trial" class="btn btn-gold btn-sm"><i class="fa-solid fa-play"></i> Free 24H Trial</a>
      </div>
    </div>
  </header>

  <section class="hero-section" style="padding:4rem 0 6rem;">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-gold"><i class="fa-solid fa-layer-group"></i> 2,000+ Page Knowledge Hub</span>
        <h1 class="hero-title" style="font-size:3rem;">Complete Australian IPTV <span class="gradient-text">Research Directory</span></h1>
        <p class="section-subtitle">Explore location-based IPTV hubs, 4K sports schedules, device installation wizards, and Australian broadband anti-buffering protocols.</p>
      </div>

      <!-- Quick Category Links Grid -->
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1.5rem; margin-bottom:3.5rem;">
        <a href="#cities" class="glass-card" style="text-align:center; padding:1.75rem; text-decoration:none;">
          <div style="font-size:2rem; color:var(--primary); margin-bottom:0.75rem;"><i class="fa-solid fa-location-dot"></i></div>
          <h3 style="font-size:1.2rem; color:#fff;">Cities & Suburbs</h3>
          <p style="font-size:0.85rem; margin:0;">800+ Location Pages</p>
        </a>
        <a href="#sports" class="glass-card" style="text-align:center; padding:1.75rem; text-decoration:none;">
          <div style="font-size:2rem; color:var(--aus-gold); margin-bottom:0.75rem;"><i class="fa-solid fa-futbol"></i></div>
          <h3 style="font-size:1.2rem; color:#fff;">Live 4K Sports</h3>
          <p style="font-size:0.85rem; margin:0;">AFL, NRL, Cricket & F1</p>
        </a>
        <a href="#devices" class="glass-card" style="text-align:center; padding:1.75rem; text-decoration:none;">
          <div style="font-size:2rem; color:var(--secondary); margin-bottom:0.75rem;"><i class="fa-solid fa-tv"></i></div>
          <h3 style="font-size:1.2rem; color:#fff;">Devices & Apps</h3>
          <p style="font-size:0.85rem; margin:0;">Firestick, Smart TV, TiviMate</p>
        </a>
        <a href="#comparisons" class="glass-card" style="text-align:center; padding:1.75rem; text-decoration:none;">
          <div style="font-size:2rem; color:var(--primary); margin-bottom:0.75rem;"><i class="fa-solid fa-scale-balanced"></i></div>
          <h3 style="font-size:1.2rem; color:#fff;">Foxtel & Kayo</h3>
          <p style="font-size:0.85rem; margin:0;">Save $1000+/year</p>
        </a>
      </div>

      <!-- Section: Cities -->
      <div class="glass-card" id="cities" style="margin-bottom:2.5rem;">
        <h2 style="font-size:1.6rem; margin-bottom:1.25rem; color:#fff;"><i class="fa-solid fa-location-dot" style="color:var(--primary); margin-right:0.5rem;"></i> Australian Cities & Regional Hubs</h2>
        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:0.75rem;">
          {' '.join([f'<a href="../cities/{slugify(c)}/index.html" class="nav-link" style="padding:0.4rem 0.6rem; font-size:0.88rem;"><i class="fa-solid fa-chevron-right" style="font-size:0.7rem;"></i> {c}, {s}</a>' for c, s, _ in cities_list])}
        </div>
      </div>

      <!-- Section: Sports -->
      <div class="glass-card" id="sports" style="margin-bottom:2.5rem;">
        <h2 style="font-size:1.6rem; margin-bottom:1.25rem; color:#fff;"><i class="fa-solid fa-futbol" style="color:var(--aus-gold); margin-right:0.5rem;"></i> Australian Sports in 4K UHD</h2>
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:0.75rem;">
          {' '.join([f'<a href="../sports/{s_slug}/index.html" class="nav-link" style="padding:0.4rem 0.6rem; font-size:0.88rem;"><i class="fa-solid fa-play" style="font-size:0.7rem; color:var(--aus-gold);"></i> {s_name}</a>' for s_slug, _, _, s_name, _ in sports_list])}
        </div>
      </div>

      <!-- Section: Devices -->
      <div class="glass-card" id="devices" style="margin-bottom:2.5rem;">
        <h2 style="font-size:1.6rem; margin-bottom:1.25rem; color:#fff;"><i class="fa-solid fa-tv" style="color:var(--secondary); margin-right:0.5rem;"></i> Device Installation Wizards</h2>
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:0.75rem;">
          {' '.join([f'<a href="../devices/{d_slug}/index.html" class="nav-link" style="padding:0.4rem 0.6rem; font-size:0.88rem;"><i class="fa-solid fa-wrench" style="font-size:0.7rem; color:var(--secondary);"></i> {d_name}</a>' for d_slug, _, _, d_name, _ in devices_list])}
        </div>
      </div>

      <!-- Section: Comparisons -->
      <div class="glass-card" id="comparisons">
        <h2 style="font-size:1.6rem; margin-bottom:1.25rem; color:#fff;"><i class="fa-solid fa-scale-balanced" style="color:var(--primary); margin-right:0.5rem;"></i> Foxtel, Kayo & Competitor Alternatives</h2>
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:0.75rem;">
          {' '.join([f'<a href="../comparisons/{c_slug}/index.html" class="nav-link" style="padding:0.4rem 0.6rem; font-size:0.88rem;"><i class="fa-solid fa-arrow-right-arrow-left" style="font-size:0.7rem; color:var(--primary);"></i> {c_name}</a>' for c_slug, _, _, c_name, _ in competitors_list])}
        </div>
      </div>
    </div>
  </section>

  <footer class="site-footer">
    <div class="container" style="text-align:center;">
      <p>&copy; 2026 IPTV Australia Reseller Panel. 2,000+ Page Programmatic SEO Directory.</p>
    </div>
  </footer>
</body>
</html>
"""

os.makedirs(os.path.join(BASE_DIR, "directory"), exist_ok=True)
with open(os.path.join(BASE_DIR, "directory", "index.html"), "w", encoding="utf-8") as f:
    f.write(dir_html)

print("\nSUCCESS: Generated 2,000+ Australian SEO pages, Sitemaps, and Directory Hub!")

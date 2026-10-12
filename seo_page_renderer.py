import os, sys, re, json, glob, html

BASE_DIR = r"c:\Users\clanm\OneDrive\Desktop\australiatv"
SITE_URL = "https://4kaustraliaiptv.com"

from seo_engine_init import (
    cities_list, sports_list, devices_list, competitors_list,
    isps_list, languages_list, guides_list, parsed_kws
)

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

# Template generator for programmatic SEO pages
def render_seo_page(
    title,
    meta_desc,
    h1,
    h2,
    badge_text,
    category_name,
    category_url,
    canonical_url,
    content_html,
    faq_list,
    rel_path_to_root="../../",
    breadcrumbs=None
):
    if breadcrumbs is None:
        breadcrumbs = [
            ("Home", f"{rel_path_to_root}index.html"),
            (category_name, f"{rel_path_to_root}{category_url}"),
            (h1, "")
        ]

    # Schema JSON-LD Breadcrumb
    bc_items = []
    for idx, (b_name, b_url) in enumerate(breadcrumbs, 1):
        full_url = f"{SITE_URL}/{b_url.lstrip('./')}" if b_url else canonical_url
        bc_items.append({
            "@type": "ListItem",
            "position": idx,
            "name": b_name,
            "item": full_url
        })
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": bc_items
    }

    # Schema FAQ
    faq_schema_items = []
    for q, a in faq_list:
        faq_schema_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schema_items
    }

    # Product Schema
    product_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": h1,
        "description": meta_desc,
        "image": f"{SITE_URL}/assets/og-au.png",
        "brand": {
            "@type": "Brand",
            "name": "IPTV Australia Reseller Panel"
        },
        "offers": {
            "@type": "AggregateOffer",
            "priceCurrency": "AUD",
            "lowPrice": "15.00",
            "highPrice": "110.00",
            "offerCount": "4"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.94",
            "reviewCount": "2480"
        }
    }

    # Breadcrumbs HTML
    bc_html = ' <span style="color:var(--text-dim); margin:0 0.4rem;">/</span> '.join([
        f'<a href="{url}" style="color:var(--text-muted); font-size:0.85rem;">{name}</a>' if url else f'<span style="color:var(--primary); font-size:0.85rem;">{name}</span>'
        for name, url in breadcrumbs
    ])

    # FAQ HTML
    faq_html_blocks = ""
    for idx, (q, a) in enumerate(faq_list):
        faq_html_blocks += f"""
        <div class="faq-item" data-category="general">
          <div class="faq-question">
            <h3><i class="fa-solid fa-circle-question" style="color:var(--primary);"></i> {html.escape(q)}</h3>
            <div class="faq-toggle-icon"><i class="fa-solid fa-plus"></i></div>
          </div>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              {a}
            </div>
          </div>
        </div>
        """

    page_html = f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <meta name="theme-color" content="#0a0614" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(meta_desc)}" />
  <link rel="canonical" href="{canonical_url}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />

  <!-- Open Graph -->
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(meta_desc)}" />
  <meta property="og:type" content="article" />
  <meta property="og:locale" content="en_AU" />
  <meta property="og:url" content="{canonical_url}" />

  <!-- Fonts & Stylesheet -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <link rel="stylesheet" href="{rel_path_to_root}assets/css/style.css" />

  <!-- Schema.org Structured Data -->
  <script type="application/ld+json">
  {json.dumps(breadcrumb_schema, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(faq_schema, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(product_schema, indent=2)}
  </script>
</head>

<body>
  <div class="bg-glow-orb bg-orb-1"></div>
  <div class="bg-glow-orb bg-orb-2"></div>
  <div class="bg-grid-overlay"></div>

  <!-- Announcement Bar -->
  <div class="announcement-bar">
    <div class="container announcement-inner">
      <div class="announcement-ticker">
        <span class="ticker-tag"><i class="fa-solid fa-bolt"></i> 2026 Aussie Special</span>
        <span>🇦🇺 <strong>Australia Exclusive:</strong> 24H Free AFL, NRL & Foxtel 4K Trial | Telstra & Optus NBN Anti-Freeze</span>
      </div>
      <div class="announcement-meta">
        <span class="aus-time-pill">
          <span class="live-indicator"></span>
          <span id="ausLiveClock">Sydney/Melb: Online</span>
        </span>
        <button class="btn btn-sm btn-gold" data-open-modal="trial">
          <i class="fa-solid fa-play"></i> Free 24H Trial
        </button>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="{rel_path_to_root}index.html" class="site-logo">
        <div class="logo-badge"><i class="fa-solid fa-earth-oceania"></i></div>
        <div class="logo-text">
          <span class="logo-brand">IPTV<span>AUSTRALIA</span></span>
          <span class="logo-sub">#1 Network 2026</span>
        </div>
      </a>
      <nav class="main-nav">
        <a href="{rel_path_to_root}index.html" class="nav-link"><i class="fa-solid fa-house"></i> Home</a>
        <a href="{rel_path_to_root}reseller.html" class="nav-link"><i class="fa-solid fa-store"></i> Reseller Guide</a>
        <a href="{rel_path_to_root}providers.html" class="nav-link"><i class="fa-solid fa-tv"></i> AU Providers</a>
        <a href="{rel_path_to_root}channels.html" class="nav-link"><i class="fa-solid fa-futbol"></i> Aussie Sports</a>
        <a href="{rel_path_to_root}setup.html" class="nav-link"><i class="fa-solid fa-wrench"></i> Setup Guides</a>
        <a href="{rel_path_to_root}directory/index.html" class="nav-link"><i class="fa-solid fa-compass"></i> Directory</a>
      </nav>
      <div class="header-actions">
        <button class="btn btn-outline btn-sm" data-open-modal="trial"><i class="fa-solid fa-play"></i> Free Trial</button>
        <button class="btn btn-primary btn-sm" data-open-modal="reseller"><i class="fa-solid fa-store"></i> Reseller Panel</button>
      </div>
    </div>
  </header>

  <!-- Breadcrumbs Bar -->
  <div style="background:rgba(18,11,34,0.6); border-bottom:1px solid var(--border-color); padding:0.6rem 0;">
    <div class="container">
      <nav aria-label="Breadcrumbs" style="display:flex; align-items:center;">
        {bc_html}
      </nav>
    </div>
  </div>

  <!-- Main Hero Section -->
  <section class="hero-section" style="padding: 3.5rem 0 3rem;">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="hero-badges-row">
            <span class="badge badge-glow-gold"><i class="fa-solid fa-crown"></i> {badge_text}</span>
            <span class="badge badge-glow-mauve"><i class="fa-solid fa-signal"></i> 100% NBN Anti-Freeze</span>
            <span class="badge badge-glow-green"><i class="fa-solid fa-dollar-sign"></i> AUD Accepted</span>
          </div>

          <h1 class="hero-title" style="font-size:2.85rem; line-height:1.15; margin-bottom:1.25rem;">
            {h1}
          </h1>

          <p class="hero-description" style="font-size:1.1rem; line-height:1.7;">
            {h2}
          </p>

          <div class="hero-ctas">
            <button class="btn btn-gold btn-lg" data-open-modal="trial">
              <i class="fa-solid fa-play"></i> Start 24H Free Aussie Trial
            </button>
            <button class="btn btn-primary btn-lg" data-open-modal="reseller">
              <i class="fa-solid fa-rocket"></i> Get Reseller Panel Access
            </button>
            <a href="https://wa.me/61400000000?text=Hi%2C%20I%20am%20interested%20in%20{h1.replace(' ', '%20')}" target="_blank" class="btn btn-whatsapp btn-lg">
              <i class="fa-brands fa-whatsapp"></i> Aussie WhatsApp Desk
            </a>
          </div>
        </div>

        <!-- Portal Info Card -->
        <div>
          <div class="hero-portal-card">
            <div class="portal-card-header">
              <div>
                <h3 style="font-size:1.2rem;">🇦🇺 Australian Server Edge</h3>
                <span style="font-size:0.8rem; color:var(--text-dim);">Sydney & Melbourne Ultra Low Latency</span>
              </div>
              <div class="portal-status-pill">
                <span class="live-indicator"></span> 0% Buffering
              </div>
            </div>

            <div class="portal-server-ping">
              <div class="server-loc"><i class="fa-solid fa-server" style="color:var(--primary);"></i> <span>Sydney (SYD-01)</span></div>
              <div class="ping-val">8ms • 10Gbps</div>
            </div>
            <div class="portal-server-ping" style="margin-top:-0.5rem;">
              <div class="server-loc"><i class="fa-solid fa-server" style="color:var(--aus-gold);"></i> <span>Melbourne (MEL-02)</span></div>
              <div class="ping-val">12ms • 10Gbps</div>
            </div>

            <ul class="portal-features-list">
              <li><i class="fa-solid fa-circle-check"></i> <strong>50,000+ Live Channels:</strong> AFL, NRL, Fox Sports, Stan Sport, Optus.</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>160,000+ 4K Movies & VOD:</strong> Stan, Binge, Netflix & HBO style library.</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Aussie Payment Methods:</strong> PayID, Visa/MC, Apple Pay, PayPal & Crypto.</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Instant 5-Minute Setup:</strong> Firestick 4K, Smart TV, TiviMate, Apple TV.</li>
            </ul>

            <button class="btn btn-primary btn-block btn-lg" data-open-modal="trial">
              <i class="fa-solid fa-bolt"></i> Generate Instant Free Trial
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Deep Content Section -->
  <section style="padding: 4rem 0; background: var(--bg-secondary);">
    <div class="container">
      {content_html}
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="faq-section" style="padding: 5rem 0;">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-glow-cyan"><i class="fa-solid fa-circle-question"></i> Help & FAQs</span>
        <h2 class="section-title">Frequently Asked Questions</h2>
        <p class="section-subtitle">Common questions from Australian customers and resellers regarding pricing, device compatibility, and NBN speed requirements.</p>
      </div>

      <div class="faq-accordion">
        {faq_html_blocks}
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <a href="{rel_path_to_root}index.html" class="site-logo" style="margin-bottom:1rem;">
            <div class="logo-badge"><i class="fa-solid fa-earth-oceania"></i></div>
            <div class="logo-text">
              <span class="logo-brand">IPTV<span>AUSTRALIA</span></span>
              <span class="logo-sub">#1 Network 2026</span>
            </div>
          </a>
          <p style="font-size:0.88rem;">Australia's leading IPTV subscription and reseller panel infrastructure with local CDN servers in Sydney, Melbourne, Brisbane & Perth.</p>
        </div>
        <div class="footer-col">
          <h4><i class="fa-solid fa-compass"></i> Quick Links</h4>
          <ul class="footer-links-list">
            <li><a href="{rel_path_to_root}index.html">Home</a></li>
            <li><a href="{rel_path_to_root}reseller.html">Reseller Guide</a></li>
            <li><a href="{rel_path_to_root}providers.html">Top AU Providers</a></li>
            <li><a href="{rel_path_to_root}channels.html">Aussie Sports</a></li>
            <li><a href="{rel_path_to_root}setup.html">Setup Guides</a></li>
            <li><a href="{rel_path_to_root}directory/index.html">Directory Index</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4><i class="fa-solid fa-futbol"></i> Australian Sports</h4>
          <ul class="footer-links-list">
            <li><a href="{rel_path_to_root}sports/afl-live-stream-iptv/index.html">AFL Premiership 4K</a></li>
            <li><a href="{rel_path_to_root}sports/nrl-live-stream-iptv/index.html">NRL Telstra Season</a></li>
            <li><a href="{rel_path_to_root}sports/cricket-australia-the-ashes-iptv/index.html">The Ashes & BBL</a></li>
            <li><a href="{rel_path_to_root}sports/formula-1-australian-gp-iptv/index.html">Formula 1 Aus GP</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4><i class="fa-solid fa-location-dot"></i> Top Cities</h4>
          <ul class="footer-links-list">
            <li><a href="{rel_path_to_root}cities/sydney/index.html">Sydney IPTV</a></li>
            <li><a href="{rel_path_to_root}cities/melbourne/index.html">Melbourne IPTV</a></li>
            <li><a href="{rel_path_to_root}cities/brisbane/index.html">Brisbane IPTV</a></li>
            <li><a href="{rel_path_to_root}cities/perth/index.html">Perth IPTV</a></li>
            <li><a href="{rel_path_to_root}cities/adelaide/index.html">Adelaide IPTV</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4><i class="fa-solid fa-lock"></i> AUD Payments</h4>
          <div style="display:flex; flex-wrap:wrap; gap:0.4rem; margin-bottom:1rem;">
            <span class="badge badge-glow-gold">PayID</span>
            <span class="badge badge-glow-cyan">Visa / MC</span>
            <span class="badge badge-glow-green">Apple Pay</span>
            <span class="badge badge-glow-cyan">PayPal</span>
            <span class="badge badge-glow-gold">Crypto</span>
          </div>
          <button class="btn btn-gold btn-sm btn-block" data-open-modal="trial">Get Free 24H Trial</button>
        </div>
      </div>
      <div class="footer-bottom-bar">
        <div>&copy; 2026 IPTV Australia Reseller Panel. All rights reserved.</div>
      </div>
    </div>
  </footer>

  <!-- Modals -->
  <div class="modal-overlay" id="trialModal">
    <div class="modal-dialog">
      <button class="modal-close-btn"><i class="fa-solid fa-times"></i></button>
      <div style="text-align:center; margin-bottom:1.5rem;">
        <span class="badge badge-glow-gold" style="margin-bottom:0.5rem;">100% Free • No Card</span>
        <h3 style="font-size:1.5rem;">24-Hour Free Australian Trial</h3>
        <p style="font-size:0.9rem;">Instant access to AFL, NRL, Fox Sports, Stan Sport, Optus, and 160,000+ 4K movies.</p>
      </div>
      <form id="trialForm">
        <div class="form-group"><label>Your Name:</label><input type="text" class="form-control" placeholder="e.g. Liam Smith" required /></div>
        <div class="form-group"><label>Email Address:</label><input type="email" class="form-control" placeholder="name@example.com.au" required /></div>
        <div class="form-group"><label>Device:</label><select class="form-control"><option>Amazon Firestick 4K</option><option>Samsung / LG Smart TV</option><option>Android TV / Google TV / TiviMate</option><option>Apple TV</option><option>iPhone / Android</option><option>PC / Mac</option></select></div>
        <button type="submit" class="btn btn-gold btn-block btn-lg" style="margin-top:1.25rem;"><i class="fa-solid fa-play"></i> Send Free Trial Credentials</button>
      </form>
    </div>
  </div>

  <div class="modal-overlay" id="resellerModal">
    <div class="modal-dialog">
      <button class="modal-close-btn"><i class="fa-solid fa-times"></i></button>
      <div style="text-align:center; margin-bottom:1.5rem;">
        <span class="badge badge-glow-cyan" style="margin-bottom:0.5rem;">Aussie Reseller Portal</span>
        <h3 style="font-size:1.5rem;">Apply for Reseller Panel</h3>
        <p style="font-size:0.9rem;">Wholesale credits from $2.20 AUD. White-label dashboard and unlimited trial generator.</p>
      </div>
      <form id="resellerForm">
        <div class="form-group"><label>Name / Brand:</label><input type="text" class="form-control" placeholder="e.g. Sydney IPTV Stream" required /></div>
        <div class="form-group"><label>Email:</label><input type="email" class="form-control" placeholder="contact@domain.com.au" required /></div>
        <div class="form-group"><label>WhatsApp / Mobile:</label><input type="tel" class="form-control" placeholder="+61 400 123 456" required /></div>
        <div class="form-group"><label>Initial Credits Package:</label><select class="form-control"><option>50 Credits ($180 AUD)</option><option selected>100 Credits ($320 AUD)</option><option>250 Credits ($650 AUD)</option><option>500 Credits ($1,100 AUD)</option></select></div>
        <button type="submit" class="btn btn-primary btn-block btn-lg" style="margin-top:1.25rem;"><i class="fa-solid fa-rocket"></i> Submit Application</button>
      </form>
    </div>
  </div>

  <script src="{rel_path_to_root}assets/js/app.js"></script>
</body>
</html>
"""
    return page_html

print("Page renderer ready.")

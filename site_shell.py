"""Shared page shell (head, header, footer, breadcrumbs, small components) for pages built by the helper scripts."""
import html as H, json, os, re, urllib.parse

SITE = 'https://4kaustraliaiptv.com'
BIZ = '4K Australia IPTV'
EMAIL = 'support@4kaustraliaiptv.com'
WA = 'https://wa.me/212625218443?text='
CSS_V = '29'
TODAY = '2026-10-11'

_root = os.path.dirname(os.path.abspath(__file__))
_shell = open(os.path.join(_root, 'devices/iptv-on-amazon-firestick-australia/index.html'), encoding='utf8').read()
_top = _shell[_shell.find('<body'):_shell.find('</header>') + 9]
_foot = _shell[_shell.find('<footer'):]


def wa(msg): return WA + urllib.parse.quote(msg)
def e(t): return H.escape(t, quote=False)
def ea(t): return H.escape(t, quote=True)


def shell_parts(depth):
    """header+footer with relative links valid for a page `depth` folders below the site root."""
    pre = '../' * depth
    top = _top.replace('../../', pre).replace('class="nav-link active"', 'class="nav-link"')
    foot = _foot.replace('../../', pre)
    return top, foot


def head(title, desc, path, depth, jsonld=(), og_type='website'):
    """path: URL path without domain, e.g. 'devices/' or ''."""
    url = '%s/%s' % (SITE, path)
    pre = '../' * depth
    ld = ''.join('<script type="application/ld+json">\n%s\n</script>\n' % json.dumps(x, indent=2, ensure_ascii=False) for x in jsonld)
    return '''<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
<meta name="theme-color" content="#0f172a" />
<title>%s</title>
<meta name="description" content="%s" />
<link rel="canonical" href="%s" />
<link rel="alternate" hreflang="en-AU" href="%s" />
<link rel="alternate" hreflang="x-default" href="%s" />
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
<meta property="og:title" content="%s" />
<meta property="og:description" content="%s" />
<meta property="og:type" content="%s" />
<meta property="og:locale" content="en_AU" />
<meta property="og:url" content="%s" />
<meta property="og:image" content="%s/assets/og-au.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="%s/assets/og-au.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
<link rel="stylesheet" href="%sassets/css/style.css?v=%s" />
%s</head>
''' % (e(title), ea(desc), url, url, url, e(title), ea(desc), og_type, url, SITE, SITE, pre, CSS_V, ld)


def crumbs(items, depth):
    """items: list of (name, href-or-None) after Home."""
    pre = '../' * depth
    parts = ['<a href="%sindex.html" style="color:var(--text-muted); font-size:0.85rem;">Home</a>' % pre]
    for name, href in items:
        sep = '<span style="color:var(--text-dim); margin:0 0.4rem;">/</span>'
        if href: parts.append(sep + '<a href="%s%s" style="color:var(--text-muted); font-size:0.85rem;">%s</a>' % (pre, href, name))
        else: parts.append(sep + '<span style="font-size:0.85rem; font-weight:600;">%s</span>' % name)
    return ('<div style="background:var(--bg-secondary); border-bottom:1px solid var(--border-color); padding:0.6rem 0;"><div class="container">'
            '<nav aria-label="Breadcrumbs" style="display:flex; align-items:center; flex-wrap:wrap;">%s</nav></div></div>' % ''.join(parts))


def breadcrumb_ld(items):
    """items: list of (name, url) including Home first."""
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def page_hero(badge, h1, lead):
    return ('<section style="padding:3.5rem 0 1rem; background:var(--bg-main);"><div class="container"><div class="prose-block" style="max-width:900px;">'
            '<span class="badge badge-glow-cyan">%s</span><h1 class="hero-title" style="margin:1rem 0 1rem; font-size:clamp(2rem,4vw,2.75rem);">%s</h1>'
            '<p class="legal-lead" style="font-size:1.1rem; color:var(--text-muted); line-height:1.75;">%s</p></div></div></section>' % (badge, h1, lead))


def cta_band(title, text, msg, dark=True):
    return '''
  <section class="cta-band%s" aria-label="Get started">
    <div class="container"><div class="cta-inner" style="grid-template-columns:1fr;">
      <div class="cta-copy" style="text-align:center; margin:0 auto;">
        <h2>%s</h2><p style="margin-left:auto;margin-right:auto;">%s</p>
        <div class="cta-actions" style="justify-content:center;">
          <button class="btn btn-gold btn-lg" data-open-modal="trial" data-cta="trial"><i class="fa-solid fa-play"></i> Start Free 24H Trial</button>
          <a class="btn btn-whatsapp btn-lg" data-cta="whatsapp" href="%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp</a>
        </div>
      </div>
    </div></div>
  </section>''' % (' cta-dark' if dark else '', title, text, wa(msg))


def assemble(depth, head_html, crumb_html, body_html):
    top, foot = shell_parts(depth)
    return head_html + top + crumb_html + body_html + '\n  ' + foot


def write(path_dir, html):
    os.makedirs(os.path.join(_root, path_dir), exist_ok=True)
    with open(os.path.join(_root, path_dir, 'index.html'), 'w', encoding='utf8') as f: f.write(html)


def add_to_sitemap(path, priority='0.8', freq='weekly', file='sitemap-core.xml'):
    p = os.path.join(_root, file)
    sm = open(p, encoding='utf8').read()
    loc = '%s/%s' % (SITE, path)
    if '<loc>%s</loc>' % loc not in sm:
        sm = sm.replace('</urlset>', '  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>\n</urlset>' % (loc, TODAY, freq, priority))
        open(p, 'w', encoding='utf8').write(sm)

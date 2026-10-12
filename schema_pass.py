"""Structured data pass: complete FAQPage on the homepage, HowTo on step-by-step pages, Article on guides/comparisons/landing pages,
AboutPage and ContactPage, plus share rows on the landing pages. Only describes content that is visible on the page."""
import glob, html as H, json, os, re, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://4kaustraliaiptv.com'
TODAY = '2026-10-11'
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)
def txt(x): return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', x))).strip()
def ld(obj): return '  <script type="application/ld+json">\n%s\n  </script>\n' % json.dumps(obj, indent=2, ensure_ascii=False)
def url_for(rel): return SITE + '/' + ('' if rel == 'index.html' else (rel[:-10] if rel.endswith('/index.html') else rel))

def meta(s):
    t = re.search(r'<title>(.*?)</title>', s, re.S); t = H.unescape(t.group(1).strip()) if t else ''
    d = re.search(r'name="description" content="([^"]*)"', s); d = H.unescape(d.group(1)) if d else ''
    h = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S); h = txt(h.group(1)) if h else t
    return t, d, h

def article(t, d, h, url):
    return {"@context": "https://schema.org", "@type": "Article", "headline": h[:110], "description": d, "inLanguage": "en-AU", "datePublished": TODAY, "dateModified": TODAY,
            "mainEntityOfPage": url, "author": {"@type": "Organization", "name": "4K Australia IPTV", "url": SITE + '/'},
            "publisher": {"@type": "Organization", "name": "4K Australia IPTV", "url": SITE + '/', "logo": {"@type": "ImageObject", "url": SITE + '/assets/og-au.png'}}}

def howto(h, steps, url):
    return {"@context": "https://schema.org", "@type": "HowTo", "name": h, "inLanguage": "en-AU", "url": url,
            "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate(steps)]}

def steps_from(s):
    out = [(txt(a), txt(b)) for a, b in re.findall(r'<li><span class="step-number">\d+</span><div><h4>(.*?)</h4><p>(.*?)</p></div></li>', s, re.S)]
    if out: return out
    return [(txt(a), txt(b)) for a, b in re.findall(r'step-number[^>]*>\d+</span>\s*<h4>(.*?)</h4>\s*<p[^>]*>(.*?)</p>', s, re.S)]

stats = dict(faq=0, howto=0, article=0, about=0, contact=0, share=0)
for path in glob.glob('**/*.html', recursive=True):
    rel = path.replace(os.sep, '/'); parts = rel.split('/')
    s = rd(path); o = s
    if 'noindex' in s: continue
    t, d, h = meta(s); url = url_for(rel)
    add = ''
    # homepage FAQPage: every visible Q&A
    if rel == 'index.html':
        qa = []
        for m in re.finditer(r'<div class="faq-item"[^>]*>.*?<h3>(.*?)</h3>.*?<div class="faq-answer-inner">(.*?)</div>', s, re.S):
            qa.append((txt(m.group(1)), txt(m.group(2))))
        # drop the earlier partial FAQPage block, then add the full one
        s = re.sub(r'\s*<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage".*?</script>', '', s, flags=re.S)
        if qa:
            add += ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}); stats['faq'] += 1
    isguide = parts[0] in ('guides', 'comparisons') and len(parts) == 3
    island = rel in ('best-iptv-australia/index.html', 'iptv-box-australia/index.html', 'iptv-player-australia/index.html', 'iptv-free-trial-australia/index.html')
    isdevice = parts[0] == 'devices' and len(parts) == 3
    if '"@type": "Article"' not in s and (isguide or island):
        add += ld(article(t, d, h, url)); stats['article'] += 1
    if '"@type": "HowTo"' not in s and (isguide or island or isdevice):
        st = steps_from(s)
        if len(st) >= 3:
            add += ld(howto(h, st, url)); stats['howto'] += 1
    if rel == 'about/index.html' and 'AboutPage' not in s:
        add += ld({"@context": "https://schema.org", "@type": "AboutPage", "name": t, "url": url, "inLanguage": "en-AU", "about": {"@type": "Organization", "name": "4K Australia IPTV", "url": SITE + '/'}}); stats['about'] += 1
    if rel == 'contact.html' and 'ContactPage' not in s:
        add += ld({"@context": "https://schema.org", "@type": "ContactPage", "name": t, "url": url, "inLanguage": "en-AU",
                   "mainEntity": {"@type": "Organization", "name": "4K Australia IPTV", "email": "support@4kaustraliaiptv.com", "telephone": "+212625218443", "url": SITE + '/'}}); stats['contact'] += 1
    if add: s = s.replace('</head>', add + '</head>', 1)
    # share row on the landing pages
    if island and 'share-row' not in s:
        q = urllib.parse.quote(url, safe=''); tx = urllib.parse.quote(h, safe='')
        row = ('<section style="padding:0 0 3rem; background:var(--bg-main);"><div class="container"><div class="prose-block"><div class="share-row"><span>Share this page:</span>'
               '<a href="https://wa.me/?text=%s%%20%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> WhatsApp</a>'
               '<a href="https://www.facebook.com/sharer/sharer.php?u=%s" target="_blank" rel="noopener"><i class="fa-brands fa-facebook"></i> Facebook</a>'
               '<a href="https://twitter.com/intent/tweet?url=%s&amp;text=%s" target="_blank" rel="noopener"><i class="fa-brands fa-x-twitter"></i> X</a>'
               '<button type="button" data-copy-link="%s"><i class="fa-solid fa-link"></i> Copy link</button></div></div></div></section>\n') % (tx, q, q, q, tx, url)
        k = s.find('<section class="cta-band')
        if k > 0: s = s[:k] + row + s[k:]; stats['share'] += 1
    if s != o: wr(path, s)
print(stats)
print('DONE')

"""Builds About, Privacy Policy, Terms of Service and Refund Policy pages from the site shell."""
import html as H, json, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://4kaustraliaiptv.com'
BIZ = '4K Australia IPTV'
EMAIL = 'support@4kaustraliaiptv.com'
WA_NUM = '+212 625 218 443'
WA_URL = 'https://wa.me/212625218443'
UPDATED = '11 October 2026'

shell = open('devices/iptv-on-amazon-firestick-australia/index.html', encoding='utf8').read()
TOP = shell[shell.find('<body'):shell.find('</header>') + 9].replace('../../', '../').replace('class="nav-link active"', 'class="nav-link"')
FOOT = shell[shell.find('<footer'):].replace('../../', '../')
def e(t): return H.escape(t, quote=False)

def head(title, desc, slug, name):
    url = '%s/%s/' % (SITE, slug)
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + '/'},
        {"@type": "ListItem", "position": 2, "name": name, "item": url}]}
    ld = '<script type="application/ld+json">\n%s\n</script>\n' % json.dumps(bc, indent=2)
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
<meta name="robots" content="index, follow" />
<meta property="og:title" content="%s" />
<meta property="og:description" content="%s" />
<meta property="og:type" content="website" />
<meta property="og:locale" content="en_AU" />
<meta property="og:url" content="%s" />
<meta property="og:image" content="%s/assets/og-au.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="%s/assets/og-au.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
<link rel="stylesheet" href="../assets/css/style.css?v=24" />
%s</head>
''' % (e(title), e(desc), url, url, url, e(title), e(desc), url, SITE, SITE, ld)

def page(slug, name, title, desc, h1, lead, body):
    crumbs = ('<div style="background:var(--bg-secondary); border-bottom:1px solid var(--border-color); padding:0.6rem 0;"><div class="container"><nav aria-label="Breadcrumbs" style="display:flex; align-items:center;">'
              '<a href="../index.html" style="color:var(--text-muted); font-size:0.85rem;">Home</a> <span style="color:var(--text-dim); margin:0 0.4rem;">/</span> <span style="font-size:0.85rem; font-weight:600;">%s</span></nav></div></div>' % name)
    main = ('<main><section style="padding:3.5rem 0 5rem; background:var(--bg-main);"><div class="container"><article class="prose-block legal">'
            '<span class="badge badge-glow-cyan"><i class="fa-solid fa-file-lines"></i> Last updated: %s</span>'
            '<h1 class="hero-title" style="margin:1rem 0 1rem; font-size:clamp(2rem,4vw,2.75rem);">%s</h1><p class="legal-lead">%s</p>%s'
            '</article></div></section></main>') % (UPDATED, h1, lead, body)
    out = head(title, desc, slug, name) + TOP + crumbs + main + '\n  ' + FOOT
    os.makedirs(slug, exist_ok=True)
    open(os.path.join(slug, 'index.html'), 'w', encoding='utf8').write(out)
    print('wrote', slug, len(out) // 1024, 'KB')

def sec(title, *items):
    parts = ''
    for it in items:
        parts += it if it.startswith('<') else '<p>%s</p>' % it
    return '<h2>%s</h2>%s' % (title, parts)
def ul(*xs): return '<ul>' + ''.join('<li>%s</li>' % x for x in xs) + '</ul>'
CONTACT = 'Email <a href="mailto:%s">%s</a> or message us on WhatsApp at <a href="%s" target="_blank" rel="noopener">%s</a>.' % (EMAIL, EMAIL, WA_URL, WA_NUM)

# ------------------------------------------------------------------ About
page('about', 'About', 'About %s | IPTV Subscriptions and Setup Guides' % BIZ,
     '%s helps Australians choose, set up and test IPTV. Read what we do, how our free trial works and how to reach our support team.' % BIZ,
     'About %s' % BIZ,
     '%s is an IPTV information and subscription service for viewers in Australia. We publish setup guides, device and player comparisons, and offer a free 24-hour trial so you can test the service on your own TV and internet before you pay.' % BIZ,
     sec('What we do', ul('<strong>IPTV subscriptions</strong> in Australian dollars, with 1, 3, 6 and 12-month plans.',
                          '<strong>A free 24-hour trial</strong> with no credit card, so you can test live channels on your own connection.',
                          '<strong>Setup guides</strong> for Fire TV Stick, Android TV boxes, Apple TV, Samsung and LG TVs, phones and PCs.',
                          '<strong>A reseller panel</strong> for people who want to offer IPTV to their own customers.'))
     + sec('How we work', 'We aim to explain things plainly: what an IPTV box or player does, how to test a service, and what to check before you pay. Our guides are written for people watching in Australia on NBN and mobile connections.')
     + sec('Using IPTV responsibly', 'IPTV technology is legal, but content must be properly licensed. Please use any IPTV service lawfully and in line with copyright rules where you live. Our <a href="../guides/is-iptv-legal-in-australia-2026-guide/index.html">IPTV legality guide</a> explains the basics.')
     + sec('Contact us', CONTACT + ' We reply to messages in the order we receive them.')
     + '<p><a class="btn btn-gold btn-lg" href="../iptv-free-trial-australia/index.html" data-cta="trial"><i class="fa-solid fa-play"></i> Start a free trial</a></p>')

# ------------------------------------------------------------------ Privacy
page('privacy-policy', 'Privacy Policy', 'Privacy Policy | %s' % BIZ,
     'How %s collects, uses and protects your personal information, including cookies, analytics and your rights to access or delete your data.' % BIZ,
     'Privacy Policy',
     'This policy explains what personal information %s collects when you use 4kaustraliaiptv.com, request a free trial, buy a plan or contact us, and how we use it.' % BIZ,
     sec('Information we collect', ul('<strong>Details you give us:</strong> your name, email address, WhatsApp or phone number, device type and the messages you send us.',
                                      '<strong>Order information:</strong> the plan you choose and the payment reference you send us. We do not store full card numbers on this website.',
                                      '<strong>Usage data:</strong> pages visited, device and browser type, and approximate location, collected through analytics if enabled.'))
     + sec('How we use it', ul('To create your free trial or subscription and send your login details.',
                               'To answer support questions by email or WhatsApp.',
                               'To improve our guides and website, and to understand which pages are useful.',
                               'To meet legal and tax obligations and prevent misuse of our service.'))
     + sec('Cookies and analytics', 'We save a small amount of data in your browser to remember your choices, such as the light or dark theme and your cookie choice. Analytics cookies (Google Analytics) are only set if you press Accept in the cookie banner, and they are not loaded if your browser sends a Do Not Track signal. You can change your choice at any time with the Cookie settings link in the footer, or clear cookies in your browser settings.')
     + sec('Third-party services', 'This website loads fonts from Google Fonts and icons from the cdnjs content network. When you click a WhatsApp link, your message is handled by WhatsApp under its own privacy policy. Payment providers handle your payment details under their own policies.')
     + sec('Sharing your information', 'We do not sell your personal information. We share it only with service providers who help us operate the service (for example email, messaging and payment providers), or when the law requires it.')
     + sec('Keeping your information', 'We keep your information only as long as needed for your subscription, support and legal obligations, then delete or anonymise it.')
     + sec('Your choices', 'You can ask to access, correct or delete the personal information we hold about you, or to stop receiving messages from us. ' + CONTACT)
     + sec('Changes to this policy', 'We may update this policy from time to time. The date at the top of this page shows when it was last changed.'))

# ------------------------------------------------------------------ Terms
page('terms-of-service', 'Terms of Service', 'Terms of Service | %s' % BIZ,
     'The terms for using %s: our IPTV subscriptions, free trial, acceptable use, payments, availability and how to contact us.' % BIZ,
     'Terms of Service',
     'These terms apply when you use 4kaustraliaiptv.com or buy a subscription or trial from %s. By using the website or service you agree to them.' % BIZ,
     sec('The service', 'We provide IPTV subscriptions and a reseller panel, plus guides and tools for setting up IPTV on your own devices. Plans, prices in Australian dollars and features are shown on our website and may change.')
     + sec('Free trial', 'The free trial lasts 24 hours and does not need a credit card. We may limit trials to one per person or household to prevent misuse.')
     + sec('Your account', ul('Keep your login details private. You are responsible for activity on your account.',
                              'Your subscription is for personal use on the number of devices stated in your plan, unless you buy a reseller plan.',
                              'Resellers are responsible for their own customers and for following these terms.'))
     + sec('Acceptable use', ul('Use the service lawfully and only for personal viewing, and follow copyright and broadcasting laws where you live.',
                                'Do not share, resell or publish login details, unless you hold a reseller plan.',
                                'Do not attempt to disrupt, copy or reverse-engineer the service.'),
           'We may suspend or end an account that breaks these terms.')
     + sec('Payments and renewals', 'You pay the price shown for your plan, in Australian dollars unless stated otherwise. Subscriptions do not renew unless we tell you otherwise before you pay. Refunds are covered by our <a href="../refund-policy/index.html">Refund Policy</a>.')
     + sec('Availability', 'Streaming depends on your internet connection, device and the content providers we rely on. We work to keep the service available but cannot guarantee uninterrupted access.')
     + sec('Liability', 'To the extent the law allows, we are not liable for indirect or consequential loss. Nothing in these terms limits any rights you have under Australian Consumer Law.')
     + sec('Changes and contact', 'We may update these terms and will change the date above when we do. ' + CONTACT))

# ------------------------------------------------------------------ Refund
page('refund-policy', 'Refund Policy', 'Refund Policy | %s' % BIZ,
     'Refund policy for %s: 7-day refund if your IPTV service does not work on your device and we cannot fix it. How to request a refund.' % BIZ,
     'Refund Policy',
     'We want you to be happy with your IPTV service. Start with the free 24-hour trial, which costs nothing, so you can check it works on your own TV and internet before you buy.',
     sec('7-day refund', 'If your subscription does not work on your device and we cannot fix the problem within 7 days of your purchase, you can ask for a refund of the plan you bought.')
     + sec('How to ask for a refund', ul('Contact us within 7 days of your purchase. ' + CONTACT,
                                          'Tell us your name, the email or number you used, the plan, your device and what is not working.',
                                          'Give us a chance to fix it first. Most issues are solved with a setup change on your device or network.'))
     + sec('When we may not refund', ul('The problem is caused by your internet connection or device and the service works elsewhere.',
                                        'You asked for a refund after the 7-day period.',
                                        'The account was used in breach of our <a href="../terms-of-service/index.html">Terms of Service</a>.',
                                        'You have used the free trial or previous refunds repeatedly to avoid paying.'))
     + sec('Reseller credits', 'Reseller credits that have already been used to create customer accounts cannot be refunded. Unused credits can be reviewed on request within 7 days of purchase.')
     + sec('Refund timing', 'Approved refunds are sent back using the same method you paid with where possible. Timing depends on your payment provider.')
     + sec('Your consumer rights', 'This policy does not limit any rights you have under Australian Consumer Law.'))

# sitemap
sm = open('sitemap-core.xml', encoding='utf8').read()
for slug in ('about', 'privacy-policy', 'terms-of-service', 'refund-policy'):
    loc = '%s/%s/' % (SITE, slug)
    if loc not in sm:
        sm = sm.replace('</urlset>', '  <url>\n    <loc>%s</loc>\n    <lastmod>2026-10-11</lastmod>\n    <changefreq>yearly</changefreq>\n    <priority>0.4</priority>\n  </url>\n</urlset>' % loc)
open('sitemap-core.xml', 'w', encoding='utf8').write(sm)
print('DONE')

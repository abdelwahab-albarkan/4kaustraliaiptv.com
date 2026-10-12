"""Adds a category-appropriate hero image to every generated page and cleans leftover purple inline colours."""
import glob, os, re, zlib

BASE = os.path.dirname(os.path.abspath(__file__))
I = 'public/images/'

CITY_POOL = ['home/living-room-hero', 'home/family-watching-tv', 'home/smart-tv-living-room', 'home/tv-phone-tablet', 'family-tv', 'home/streaming-device-remote']
TOPIC_POOL = ['home/smart-tv-living-room', 'home/tv-phone-tablet', 'home-cinema', 'iptv-entertainment-dashboard', 'home/living-room-hero', 'google-tv-dashboard', 'family-tv', 'quality-4k']

def pick(pool, slug):
    return pool[zlib.crc32(slug.encode()) % len(pool)]

def sport_img(slug):
    s = slug
    if re.search(r'afl|nrl|origin|rugby', s): return 'afl-nrl-stadium'
    if re.search(r'cricket|bbl|big-bash|ashes', s): return 'cricket-ashes'
    if re.search(r'formula|bathurst|supercars', s): return 'formula-1-aus'
    if re.search(r'soccer|league|matildas|socceroos|champions', s): return 'premier-league-soccer'
    if re.search(r'ufc|boxing', s): return 'ufc-boxing-main-event'
    if re.search(r'nba|basket', s): return 'nbl-basketball'
    return 'iptv-sport-streaming'

def device_img(slug):
    s = slug
    if 'firestick' in s or 'fire' in s: return 'iptv-fire-tv-stick'
    if 'apple' in s: return 'iptv-apple-tv-4k'
    if 'samsung' in s: return 'iptv-samsung-tv-setup'
    if 'lg' in s: return 'iptv-lg-smart-tv'
    if 'chromecast' in s or 'google' in s: return 'google-tv-dashboard'
    if 'android' in s or 'shield' in s: return 'iptv-android-tv-setup'
    if 'windows' in s or 'pc' in s: return 'iptv-windows-pc'
    if 'kodi' in s: return 'iptv-macbook-pro'
    if 'mag' in s or 'formuler' in s: return 'home/streaming-device-remote'
    return 'apps-dashboard'

GUIDE = {'payid': 'safe-payment', 'vpn': 'vpn-shield', 'buffering': 'zero-buffer', 'reseller-business': 'provider-comparison',
         'pricing': 'provider-comparison', 'm3u': 'iptv/setup/iptv-m3u', 'legal': 'wie-funktioniert-iptv'}
CITY_SUB = {'firestick-setup': 'iptv-fire-tv-stick', 'free-trial': 'home/streaming-device-remote', 'reseller-panel': 'apps-dashboard',
            'sports-channels': 'afl-nrl-stadium', 'subscription': 'family-tv', 'best-iptv': None}

def choose(parts):
    sec = parts[0]
    slug = parts[1] if len(parts) > 1 else ''
    if sec == 'cities':
        if len(parts) > 2 and CITY_SUB.get(parts[2]): return CITY_SUB[parts[2]]
        return pick(CITY_POOL, slug)
    if sec == 'sports': return sport_img(slug)
    if sec == 'devices': return device_img(slug)
    if sec == 'guides':
        for k, v in GUIDE.items():
            if k in slug: return v
        return 'wie-funktioniert-iptv'
    if sec == 'comparisons': return 'cable-vs-iptv'
    if sec == 'isps': return 'anti-freeze-tech'
    if sec == 'languages': return pick(['home/tv-phone-tablet', 'family-tv', 'home/family-watching-tv'], slug)
    if sec == 'topic': return pick(TOPIC_POOL, slug)
    if sec == 'directory': return 'quality-4k'
    return None

def alt_text(html, name):
    m = re.search(r'<h1[^>]*>\s*(.*?)\s*</h1>', html, re.S)
    t = re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else name
    return re.sub(r'\s+', ' ', t).replace('"', '&quot;')

n = 0
for path in glob.glob(os.path.join(BASE, '**', '*.html'), recursive=True):
    rel = os.path.relpath(path, BASE).replace(os.sep, '/')
    parts = rel.split('/')
    if len(parts) < 2: continue
    html = open(path, encoding='utf8', errors='surrogateescape').read()
    orig = html
    html = html.replace('rgba(18,11,34,0.6)', 'var(--bg-secondary)')
    name = choose(parts[:-1])
    if name and 'class="hero-portal-card">' in html and 'hero-visual' not in html:
        depth = len(parts) - 1
        img = '../' * depth + I + name + '.webp'
        fig = ('<figure class="hero-visual"><img src="%s" alt="%s" width="1200" height="750" loading="eager" decoding="async"></figure>\n            '
               % (img, alt_text(html, name)))
        html = html.replace('class="hero-portal-card">', 'class="hero-portal-card">\n            ' + fig, 1)
    if html != orig:
        open(path, 'w', encoding='utf8', errors='surrogateescape').write(html); n += 1
print('updated', n)

"""Removes invented or unverifiable claims: fake activity popups, latency/uptime numbers, '0% buffering', 24/7 staffing,
the unverified Telegram channel. Replaces them with statements that are true for the business today."""
import glob, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def rd(p): return open(p, encoding='utf8', errors='surrogateescape').read()
def wr(p, s): open(p, 'w', encoding='utf8', errors='surrogateescape').write(s)

def drop_block(s, start_re):
    """Remove an element that starts at start_re, balancing nested divs."""
    m = re.search(start_re, s)
    if not m: return s, 0
    depth = 0
    for t in re.finditer(r'<div\b|</div>', s[m.start():]):
        depth += 1 if t.group(0) == '<div' else -1
        if depth == 0:
            return s[:m.start()] + s[m.start() + t.end():], 1
    return s, 0

PING = re.compile(r'<div class="portal-server-ping"[^>]*>\s*<div class="server-loc">.*?</div>\s*<div class="ping-val">.*?</div>\s*</div>', re.S)
ROWS = [
    '<div class="portal-server-ping"><div class="server-loc"><i class="fa-solid fa-gift" style="color:var(--primary);"></i> <span>Free 24-hour trial</span></div><div class="ping-val">No card needed</div></div>',
    '<div class="portal-server-ping"><div class="server-loc"><i class="fa-solid fa-headset" style="color:var(--primary);"></i> <span>Support</span></div><div class="ping-val">WhatsApp + email</div></div>',
]
TEXT = [
    # announcement bar and pills
    (re.compile(r'0% Buffering on Telstra, Optus (?:&amp;|&) TPG NBN'), 'Test it on Telstra, Optus &amp; TPG NBN'),
    (re.compile(r'(<div class="portal-status-pill">\s*<span class="live-indicator"></span>\s*)0% (?:Buffering|Freezing)'), r'\1Free trial'),
    (re.compile(r'Sydney (?:&amp;|&) Melbourne Ultra Low Latency'), 'Streaming for Australian viewers'),
    (re.compile(r'(Sydney|Melbourne)? ?Australia Gateway'), 'Built for Australia'),
    (re.compile(r'Australian Server Edge'), 'Built for Australia'),
    # uptime guarantees and absolute buffering promises
    (re.compile(r'99\.98%</span>\s*<span class="stat-label">NBN Uptime SLA'), '24H</span>\n              <span class="stat-label">Free Trial'),
    (re.compile(r'our platform guarantees 99\.98% uptime and zero buffering', re.I), 'we aim for smooth, reliable streaming'),
    (re.compile(r'zero buffering', re.I), lambda m: 'Smooth streaming' if m.group(0)[0].isupper() else 'smooth streaming'),
    # 24/7 staffing and Telegram claims
    (re.compile(r'Local 24/7 Aussie support on WhatsApp and Telegram'), 'Support on WhatsApp and email'),
    (re.compile(r'24/7 Australian WhatsApp support desk'), 'WhatsApp support'),
    (re.compile(r'24/7 Aussie support desk'), 'support team'),
    (re.compile(r'24/7 Aussie Local Time Support'), 'WhatsApp and Email Support'),
    (re.compile(r'24/7 Aussie Support'), 'WhatsApp &amp; Email Support'),
    (re.compile(r'24/7 Australian IPTV support desk'), 'Australian IPTV support team'),
    (re.compile(r'VIP 24/7 Aussie Telegram Hotline'), 'WhatsApp Support Line'),
    (re.compile(r'24/7 Priority Australian Desk'), 'Priority Support Desk'),
    (re.compile(r'Support Hours: <strong>24/7 AEST Time</strong>'), 'Support: <strong>WhatsApp &amp; email</strong>'),
    (re.compile(r'our Melbourne and Sydney support engineers are ready 24/7'), 'our team is available on WhatsApp and email'),
    (re.compile(r'Australian 24/7 WhatsApp IPTV Support Team'), 'WhatsApp IPTV support team'),
]
TG_FAB = re.compile(r'<a [^>]*href="https://t\.me/iptvaustralia_official"[^>]*class="fab-btn fab-telegram"[^>]*>.*?</a>\s*', re.S)
TG_CARD = re.compile(r'<a href="https://t\.me/iptvaustralia_official".*?</a>\s*', re.S)

stats = dict(files=0, toast=0, ping=0, telegram=0)
for path in glob.glob('**/*.html', recursive=True):
    s = rd(path); o = s
    s, n = drop_block(s, r'<!-- Live Activity Toast -->\s*<div class="live-toast"'); stats['toast'] += n
    if n == 0:
        s, n = drop_block(s, r'<div class="live-toast"'); stats['toast'] += n
    it = iter(ROWS)
    s, k = PING.subn(lambda m: next(it, ''), s); stats['ping'] += 1 if k else 0
    for rx, rep in TEXT: s = rx.sub(rep, s)
    s, a = TG_FAB.subn('', s)
    s, b = TG_CARD.subn('', s) if 'contact.html' in path.replace(os.sep, '/') else (s, 0)
    stats['telegram'] += 1 if (a or b) else 0
    if s != o: wr(path, s); stats['files'] += 1
print(stats)
print('DONE')

"""Shows the real WhatsApp number and support email in every footer; fixes HTML that leaked into alert() text."""
import glob, os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

WA = 'https://wa.me/212625218443'
MAIL = 'support@4kaustraliaiptv.com'
BLOCK = ('<div class="footer-contact-block" style="margin-top:1rem;">'
         '<a class="footer-contact-item" href="%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp" style="color:#25D366; font-size:1.2rem;"></i><span>WhatsApp: <strong>+212 625 218 443</strong></span></a>'
         '<a class="footer-contact-item" href="mailto:%s"><i class="fa-solid fa-envelope" style="color:#93c5fd; font-size:1.1rem;"></i><span>Email: <strong>%s</strong></span></a>'
         '</div>') % (WA, MAIL, MAIL)
LINE = ('<p style="margin-top:.75rem;"><a href="%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> +212 625 218 443</a>'
        ' &nbsp;&middot;&nbsp; <a href="mailto:%s"><i class="fa-solid fa-envelope"></i> %s</a></p>') % (WA, MAIL, MAIL)

OLD_WA_ITEM = re.compile(r'<div class="footer-contact-item">\s*<i class="fa-brands fa-whatsapp"[^>]*></i>\s*<span>WhatsApp: <strong>Aussie Live Desk</strong></span>\s*</div>')
GEN_BRAND = re.compile(r'(<p style="font-size:0\.88rem;">Australia\'s leading IPTV subscription and reseller panel infrastructure[^<]*</p>)')
MIN_FOOT = re.compile(r'(<footer class="site-footer">\s*<div class="container" style="text-align:center;">\s*<p>[^<]*</p>)')

stats = dict(pages=0, footer=0, alert=0)
for path in glob.glob('**/*.html', recursive=True):
    s = open(path, encoding='utf8', errors='surrogateescape').read(); o = s
    if 'footer-contact-item' in s and '4kaustraliaiptv.com' in s: continue
    # stray icon markup inside JS alert()/toast strings
    s, n = re.subn(r"(alert\(')<i class=\"[^\"]*\"[^>]*></i>\s*", r'\1', s); stats['alert'] += n
    if OLD_WA_ITEM.search(s):                                   # homepage footer
        item = BLOCK.replace('<div class="footer-contact-block" style="margin-top:1rem;">', '').rsplit('</div>', 1)[0]
        s = OLD_WA_ITEM.sub(lambda m: item, s, 1); stats['footer'] += 1
    elif GEN_BRAND.search(s):                                   # generated pages
        s = GEN_BRAND.sub(lambda m: m.group(1) + '\n        ' + BLOCK, s, 1); stats['footer'] += 1
    elif MIN_FOOT.search(s):                                    # slim footers
        s = MIN_FOOT.sub(lambda m: m.group(1) + '\n    ' + LINE, s, 1); stats['footer'] += 1
    if s != o:
        open(path, 'w', encoding='utf8', errors='surrogateescape').write(s); stats['pages'] += 1
print(stats)
print('DONE')

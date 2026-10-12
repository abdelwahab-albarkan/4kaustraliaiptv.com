import re
p='index.html'
s=open(p,encoding='utf8',errors='surrogateescape').read()
M={'aussie-channel-guide':('home/smart-tv-living-room.webp','Australian live TV channel guide on a smart TV'),
'aussie-footy-hub':('afl-nrl-stadium.webp','AFL and NRL live in 4K'),
'provider-dossiers':('provider-comparison.webp','Australian IPTV provider comparison'),
'australian-cities-encyclopedia':('home/living-room-hero.webp','IPTV across Australian cities'),
'device-setup-center':('home/tv-phone-tablet.webp','IPTV on TV, phone and tablet'),
'nbn-dns-hub':('anti-freeze-tech.webp','NBN anti-freeze streaming technology'),
'multicultural-tv-hub':('home/family-watching-tv.webp','Multicultural family watching TV'),
'foxtel-kayo-comparison':('cable-vs-iptv.webp','IPTV compared with Foxtel and Kayo'),
'wholesale-reseller-academy':('apps-dashboard.webp','Reseller panel dashboard'),
'aussie-sports-calendar':('cricket-ashes.webp','Australian sports calendar'),
'nbn-speed-guide':('zero-buffer.webp','Buffer-free streaming on NBN'),
'hardware-matrix':('devices/devices-collection.jpg','Compatible streaming hardware'),
'payid-checkout-hub':('safe-payment.webp','Secure PayID and card payments'),
'aussie-legal-guide':('wie-funktioniert-iptv.webp','How IPTV works'),
}
n=0
for sid,(img,alt) in M.items():
    m=re.search(r'(<section[^>]*id="%s"[^>]*>\s*<div class="container">)'%sid,s)
    if not m: print('miss',sid); continue
    end=s.find('</section>',m.end())
    if 'page-banner' in s[m.end():end]: continue
    fig='\n      <div class="page-banner"><img src="public/images/%s" alt="%s" width="1600" height="610" loading="lazy" decoding="async"></div>'%(img,alt)
    s=s[:m.end()]+fig+s[m.end():]; n+=1
open(p,'w',encoding='utf8',errors='surrogateescape').write(s); print(n)

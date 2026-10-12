import re
p='index.html'
s=open(p,encoding='utf8',errors='surrogateescape').read()
LABEL={'australian-cities-encyclopedia':'Show all cities & suburbs','mega-keyword-index':'Show all indexed search topics','australian-suburbs-atlas':'Show the full suburbs atlas','mega-search-directory':'Show the full topic directory'}
n=0
for sid,label in LABEL.items():
    j=s.find('id="%s"'%sid); e=s.find('</section>',j)
    sec=s[j:e]
    if 'more-details' in sec: continue
    h=sec.find('class="section-header')
    if h<0: print('nohdr',sid); continue
    hend=sec.find('</div>',h)+6
    t=sec.rfind('<div style="text-align:center')
    if t<hend: print('nocta',sid); continue
    new=sec[:hend]+'\n      <details class="more-details"><summary><span>%s</span></summary>\n'%label+sec[hend:t]+'      </details>\n      '+sec[t:]
    s=s[:j]+new+s[e:]; n+=1
open(p,'w',encoding='utf8',errors='surrogateescape').write(s); print(n)

import csv, re, sqlite3, itertools

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

rows = []
def add(kw, category, page_type, intent, city=""):
    rows.append(dict(keyword=kw, category=category, page_type=page_type,
                     intent=intent, city=city, slug=slug(kw),
                     title=kw.title() + " | Updated 2026"))

# ---- 1. Core / head terms
for kw in ["iptv australia", "best iptv australia", "iptv subscription australia",
           "iptv australia free trial", "buy iptv australia", "cheap iptv australia",
           "iptv australia reviews", "iptv australia legal", "iptv australia price",
           "iptv providers australia", "iptv service australia", "premium iptv australia",
           "iptv australia 4k", "iptv australia no buffering", "iptv australia reseller",
           "iptv australia m3u", "iptv australia epg", "iptv australia 12 months",
           "iptv australia monthly", "iptv australia yearly plan"]:
    add(kw, "core", "landing", "transactional")

# ---- 2. City pages
cities = """Sydney Melbourne Brisbane Perth Adelaide Gold Coast Canberra Newcastle Wollongong
Sunshine Coast Hobart Geelong Townsville Cairns Darwin Toowoomba Ballarat Bendigo Launceston
Mackay Rockhampton Bunbury Bundaberg Coffs Harbour Wagga Wagga Hervey Bay Mildura Shepparton
Port Macquarie Gladstone Tamworth Orange Dubbo Geraldton Albury Warrnambool Nowra Bathurst
Lismore Kalgoorlie Alice Springs Mandurah Penrith Parramatta Blacktown Liverpool Campbelltown
Frankston Dandenong Werribee Ipswich Logan Redcliffe Caboolture Joondalup Rockingham Armadale
Salisbury Elizabeth Glenelg Burwood Chatswood Bondi Manly Cronulla St Kilda Footscray Richmond
Southbank Fremantle Surfers Paradise Noosa Byron Bay Hobart CBD Palmerston""".split("\n")
cities = [c for line in cities for c in re.split(r"\s{1}(?=[A-Z])", line)]
# re-join multiword names manually
multi = ["Gold Coast","Sunshine Coast","Coffs Harbour","Wagga Wagga","Hervey Bay","Port Macquarie",
         "Alice Springs","Surfers Paradise","Byron Bay","St Kilda"]
txt = " ".join(cities)
for m in multi:
    txt = txt.replace(m, m.replace(" ", "_"))
cities = [c.replace("_", " ") for c in txt.split()]
cities = list(dict.fromkeys(cities))
city_tpl = ["iptv {c}", "best iptv {c}", "iptv subscription {c}", "iptv free trial {c}",
            "cheap iptv {c}", "iptv box {c}", "buy iptv {c}", "iptv provider {c}",
            "iptv installation {c}", "iptv firestick {c}", "iptv sports channels {c}",
            "iptv reviews {c}"]
for c in cities:
    for t in city_tpl:
        add(t.format(c=c.lower()), "city", "local", "transactional", c)

# ---- 3. Devices
devices = ["firestick","fire tv","android tv","smart tv","samsung tv","lg tv","apple tv","iphone",
           "ipad","android phone","mag box","nvidia shield","roku","kodi","windows pc","mac",
           "chromecast","xbox","playstation","formuler","tivimate","smarters pro","ibo player","vlc"]
dev_tpl = ["iptv on {d} australia", "how to install iptv on {d}", "best iptv app for {d} australia",
           "iptv {d} setup guide australia", "iptv not working on {d}", "best iptv for {d} australia"]
for d in devices:
    for t in dev_tpl:
        add(t.format(d=d), "device", "guide", "informational")

# ---- 4. Sports
sports = ["AFL","NRL","A-League","Big Bash","cricket","Premier League","UFC","F1","rugby union",
          "Super Rugby","NBA","Australian Open tennis","Melbourne Cup","Bathurst 1000","State of Origin",
          "Ashes","Champions League","boxing PPV","MotoGP","Socceroos","Matildas","NFL","golf"]
sp_tpl = ["watch {s} iptv australia", "{s} live stream iptv", "best iptv for {s} australia",
          "{s} iptv free trial australia", "how to watch {s} without foxtel"]
for s in sports:
    for t in sp_tpl:
        add(t.format(s=s), "sports", "content", "transactional")

# ---- 5. Channels / competitor alternatives
chans = ["Foxtel","Kayo Sports","Stan Sport","Binge","Optus Sport","Fetch TV","Sky Sports","BT Sport",
         "beIN Sports","ESPN","Channel 7","Channel 9","Channel 10","ABC iview","SBS On Demand","Netflix",
         "Disney Plus","Paramount Plus","Amazon Prime Video","DAZN","Hayu","Showtime"]
ch_tpl = ["{x} alternative iptv australia", "iptv with {x} australia", "cheaper than {x} australia"]
for x in chans:
    for t in ch_tpl:
        add(t.format(x=x.lower()), "competitor", "comparison", "commercial")

# ---- 6. Expat / language
langs = ["arabic","indian","hindi","punjabi","tamil","urdu","greek","italian","chinese","mandarin",
         "cantonese","vietnamese","filipino","turkish","persian","polish","russian","korean","japanese",
         "british","irish","south african","serbian","croatian","lebanese","maltese","spanish",
         "portuguese","french","german","dutch","nepali","sri lankan","bangladeshi","african"]
l_tpl = ["{l} iptv australia", "{l} channels iptv australia", "best {l} iptv subscription australia",
         "{l} tv channels in australia online"]
for l in langs:
    for t in l_tpl:
        add(t.format(l=l), "language", "content", "transactional")

# ---- 7. ISP / NBN
isps = ["telstra","optus","tpg","aussie broadband","iinet","vodafone","superloop","belong","dodo","exetel","mate","starlink"]
isp_tpl = ["iptv buffering on {i}", "best iptv for {i} nbn", "iptv speed requirements {i}",
           "iptv blocked {i}", "does {i} block iptv"]
for i in isps:
    for t in isp_tpl:
        add(t.format(i=i), "isp", "guide", "informational")

# ---- 8. Informational / FAQ
faq = ["what is iptv","is iptv legal in australia","how does iptv work","iptv vs foxtel",
       "iptv vs streaming services","iptv vs cable","how much does iptv cost in australia",
       "what internet speed do i need for iptv","how to fix iptv buffering","best vpn for iptv australia",
       "do i need a vpn for iptv","what is m3u playlist","what is xtream codes","what is epg in iptv",
       "best iptv player app","iptv catch up tv","iptv multi room","iptv multiple devices",
       "iptv 4k vs hd","iptv trial how it works","how to cancel iptv subscription","iptv payment methods australia",
       "iptv refund policy","iptv anti freeze technology","iptv server locations","iptv for restaurants and pubs australia",
       "iptv for hotels australia","iptv for caravan and rv australia","iptv for overseas australians",
       "iptv setup service australia","best router for iptv","iptv ethernet vs wifi","iptv on two tvs"]
for q in faq:
    add(q, "faq", "article", "informational")

# ---- 9. State pages
states = ["new south wales","victoria","queensland","western australia","south australia","tasmania",
          "northern territory","act"]
st_tpl = ["iptv {s}","best iptv {s}","iptv subscription {s}","iptv free trial {s}",
          "cheap iptv {s}","iptv sports {s}","iptv providers {s}","iptv reviews {s}"]
for s in states:
    for t in st_tpl:
        add(t.format(s=s), "state", "local", "transactional", s)

# ---- dedupe
seen, out = set(), []
for r in rows:
    if r["keyword"] in seen:
        continue
    seen.add(r["keyword"]); out.append(r)

fields = ["keyword","category","page_type","intent","city","slug","title"]
with open("keywords.csv","w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out)

con = sqlite3.connect("keywords.db")
con.execute("DROP TABLE IF EXISTS keywords")
con.execute("""CREATE TABLE keywords(id INTEGER PRIMARY KEY, keyword TEXT UNIQUE, category TEXT,
  page_type TEXT, intent TEXT, city TEXT, slug TEXT, title TEXT,
  volume INTEGER, kd INTEGER, cpc REAL, position INTEGER, published INTEGER DEFAULT 0)""")
con.executemany("INSERT INTO keywords(keyword,category,page_type,intent,city,slug,title) VALUES(?,?,?,?,?,?,?)",
                [(r["keyword"],r["category"],r["page_type"],r["intent"],r["city"],r["slug"],r["title"]) for r in out])
con.commit()
print("total keywords:", len(out))
for cat, n in con.execute("SELECT category, COUNT(*) FROM keywords GROUP BY category ORDER BY 2 DESC"):
    print(f"  {cat:12} {n}")

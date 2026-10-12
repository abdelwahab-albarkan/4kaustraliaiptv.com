import os, sys, re, json, glob, csv
from collections import defaultdict

print("Starting Australian IPTV SEO Engine (2000+ Pages Builder)...")

BASE_DIR = r"c:\Users\clanm\OneDrive\Desktop\australiatv"
DATA_DIR = os.path.join(BASE_DIR, "dataaustralia")

# 1. Load parsed keywords
parsed_kws = []
txt_path = os.path.join(BASE_DIR, "all_parsed_keywords.txt")
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 4:
                try:
                    vol = int(parts[0])
                    kd = int(parts[1]) if parts[1].isdigit() else 0
                    intent = parts[2]
                    kw = parts[3]
                    src = parts[4] if len(parts) > 4 else ""
                    parsed_kws.append({
                        "keyword": kw,
                        "volume": vol,
                        "kd": kd,
                        "intent": intent,
                        "source": src
                    })
                except Exception:
                    pass

print(f"Loaded {len(parsed_kws)} parsed keywords from dataset.")

# Categorize keywords
cities_list = [
    # NSW
    ("Sydney", "NSW", "Sydney CBD, Parramatta, Penrith, Blacktown, Bondi, Manly, Chatswood, Cronulla, Liverpool, Campbelltown, Burwood, Castle Hill"),
    ("Newcastle", "NSW", "Newcastle East, Merewether, Charlestown, Hamilton, Wallsend, Maitland"),
    ("Central Coast", "NSW", "Gosford, Terrigal, Woy Woy, The Entrance, Wyong, Erina"),
    ("Wollongong", "NSW", "Wollongong CBD, Fairy Meadow, Thirroul, Shellharbour, Kiama, Dapto"),
    ("Parramatta", "NSW", "Western Sydney, Westmead, Harris Park, Granville, Rosehill"),
    ("Penrith", "NSW", "St Marys, Kingswood, Glenmore Park, Blue Mountains foothills"),
    ("Blacktown", "NSW", "Mount Druitt, Seven Hills, Rooty Hill, Doonside, Quakers Hill"),
    ("Bondi", "NSW", "Bondi Beach, Bondi Junction, Waverley, Tamarama, Bronte"),
    ("Manly", "NSW", "Northern Beaches, Dee Why, Brookvale, Mona Vale, Freshwater"),
    ("Albury", "NSW", "Albury-Wodonga, Lavington, Thurgoona, Murray River"),
    ("Wagga Wagga", "NSW", "Riverina, Kooringal, Turvey Park, Lake Albert, Estella"),
    ("Port Macquarie", "NSW", "Mid North Coast, Lighthouse Beach, Flynns Beach, Wauchope"),
    ("Tamworth", "NSW", "New England, Country Music Capital, South Tamworth, Oxley Vale"),
    ("Orange", "NSW", "Central West, Calare, Bletchington, Bowen, Orange CBD"),
    ("Dubbo", "NSW", "Orana region, West Dubbo, South Dubbo, Delroy Park"),
    ("Bathurst", "NSW", "Mount Panorama, Kelso, West Bathurst, Mitchell"),
    ("Coffs Harbour", "NSW", "Park Beach, Sawtell, Toormina, Korora, Woolgoolga"),
    ("Lismore", "NSW", "Northern Rivers, Goonellabah, South Lismore, Ballina"),
    ("Byron Bay", "NSW", "Suffolk Park, Brunswick Heads, Lennox Head, Mullumbimby"),
    ("Nowra", "NSW", "Shoalhaven, Bomaderry, Culburra Beach, Jervis Bay"),

    # VIC
    ("Melbourne", "VIC", "Melbourne CBD, Southbank, Docklands, St Kilda, Richmond, South Yarra, Carlton, Brunswick"),
    ("Geelong", "VIC", "Geelong West, Belmont, Newtown, Highton, Waurn Ponds, Torquay, Bellarine"),
    ("Ballarat", "VIC", "Ballarat Central, Wendouree, Alfredton, Sebastopol, Mount Helen"),
    ("Bendigo", "VIC", "Bendigo CBD, Strathdale, Kangaroo Flat, Golden Square, Kennington"),
    ("Shepparton", "VIC", "Goulburn Valley, Mooroopna, Kialla, Shepparton North"),
    ("Mildura", "VIC", "Sunraysia, Irymple, Red Cliffs, Merbein, Murray Valley"),
    ("Warrnambool", "VIC", "Great Ocean Road, Dennington, East Warrnambool, Allansford"),
    ("Frankston", "VIC", "Mornington Peninsula, Seaford, Karingal, Mount Eliza"),
    ("Dandenong", "VIC", "South East Melbourne, Noble Park, Springvale, Keysborough"),
    ("Werribee", "VIC", "Point Cook, Hoppers Crossing, Tarneit, Wyndham Vale"),
    ("St Kilda", "VIC", "Port Phillip, Elwood, Balaclava, Albert Park"),
    ("Footscray", "VIC", "Western Melbourne, Yarraville, Seddon, Maribyrnong"),
    ("Richmond", "VIC", "MCG precinct, Cremorne, Abbotsford, Burnley"),
    ("Traralgon", "VIC", "Latrobe Valley, Morwell, Moe, Gippsland"),
    ("Wodonga", "VIC", "Murray border, West Wodonga, Birallee Park"),

    # QLD
    ("Brisbane", "QLD", "Brisbane CBD, Fortitude Valley, South Brisbane, West End, Chermside, Carindale, Indooroopilly"),
    ("Gold Coast", "QLD", "Surfers Paradise, Broadbeach, Southport, Burleigh Heads, Robina, Coomera, Coolangatta"),
    ("Sunshine Coast", "QLD", "Maroochydore, Mooloolaba, Caloundra, Noosa Heads, Buderim, Coolum Beach"),
    ("Townsville", "QLD", "North Queensland, Castle Hill, Aitkenvale, Annandale, Thuringowa"),
    ("Cairns", "QLD", "Far North Queensland, Cairns CBD, Palm Cove, Smithfield, Redlynch, Trinity Beach"),
    ("Toowoomba", "QLD", "Darling Downs, East Toowoomba, Rangeville, Kearneys Spring"),
    ("Mackay", "QLD", "Central Coast QLD, Mackay CBD, North Mackay, Andergrove, Northern Beaches"),
    ("Rockhampton", "QLD", "Capricornia, Frenchville, Norman Gardens, Berserker, Gracemere"),
    ("Bundaberg", "QLD", "Wide Bay, Bargara, Svensson Heights, Walkervale"),
    ("Hervey Bay", "QLD", "Fraser Coast, Urraween, Torquay, Scarness, Pialba"),
    ("Gladstone", "QLD", "Central QLD, Clinton, Kin Kora, Tannum Sands, Boyne Island"),
    ("Ipswich", "QLD", "Greater Brisbane, Brassall, Booval, Springfield, Ripley"),
    ("Logan", "QLD", "Logan Central, Springwood, Browns Plains, Shailer Park"),
    ("Surfers Paradise", "QLD", "Cavill Avenue, Main Beach, Chevron Island, Isle of Capri"),
    ("Noosa", "QLD", "Noosa Heads, Noosaville, Tewantin, Sunshine Beach"),

    # WA
    ("Perth", "WA", "Perth CBD, Northbridge, Fremantle, Joondalup, Scarborough, Subiaco, Victoria Park, Mandurah"),
    ("Fremantle", "WA", "South Fremantle, East Fremantle, North Fremantle, Cottesloe"),
    ("Joondalup", "WA", "Northern Suburbs, Hillarys, Wanneroo, Clarkson, Ocean Reef"),
    ("Mandurah", "WA", "Peel region, Halls Head, Meadow Springs, Falcon, Silver Sands"),
    ("Bunbury", "WA", "South West WA, Eaton, Australind, Dalyellup, Carey Park"),
    ("Geraldton", "WA", "Mid West, Geraldton CBD, Bluff Point, Wandina, Strathalbyn"),
    ("Kalgoorlie", "WA", "Goldfields, Kalgoorlie-Boulder, Hannans, South Kalgoorlie"),
    ("Albany", "WA", "Great Southern, Middleton Beach, Spencer Park, Lockyer"),
    ("Rockingham", "WA", "Safety Bay, Baldivis, Waikiki, Secret Harbour"),
    ("Armadale", "WA", "South East Perth, Kelmscott, Seville Grove, Byford"),

    # SA
    ("Adelaide", "SA", "Adelaide CBD, North Adelaide, Glenelg, Norwood, Marion, Mawson Lakes, Port Adelaide"),
    ("Glenelg", "SA", "Holdfast Bay, Somerton Park, Brighton, West Beach"),
    ("Salisbury", "SA", "Northern Adelaide, Parafield, Mawson Lakes, Paralowie"),
    ("Elizabeth", "SA", "Playford, Elizabeth South, Munno Para, Blakeview"),
    ("Mount Gambier", "SA", "Blue Lake, Suttontown, Worrolong, Mount Gambier East"),
    ("Whyalla", "SA", "Eyre Peninsula, Whyalla Norrie, Whyalla Playford, Whyalla Stuart"),
    ("Port Lincoln", "SA", "Boston Bay, Kirton Point, Port Lincoln CBD"),
    ("Victor Harbor", "SA", "Fleurieu Peninsula, Encounter Bay, McCracken, Hayborough"),

    # TAS
    ("Hobart", "TAS", "Hobart CBD, Sandy Bay, Battery Point, North Hobart, Glenorchy, Kingston"),
    ("Launceston", "TAS", "Tamar Valley, East Launceston, Mowbray, Riverside, Kings Meadows"),
    ("Devonport", "TAS", "North West TAS, East Devonport, Miandetta, Spreyton"),
    ("Burnie", "TAS", "Upper Burnie, Cooee, Parklands, Montello"),

    # ACT & NT
    ("Canberra", "ACT", "Canberra CBD, Civic, Belconnen, Gungahlin, Tuggeranong, Woden Valley, Kingston, Manuka"),
    ("Darwin", "NT", "Darwin CBD, Palmerston, Casuarina, Nightcliff, Stuart Park, Fannie Bay"),
    ("Alice Springs", "NT", "Red Centre, East Side, Gillen, Braitling, Desert Springs"),
    ("Palmerston", "NT", "Rosebery, Durack, Bakewell, Driver, Gray")
]

# Sports List
sports_list = [
    ("afl-live-stream-iptv", "AFL Premiership & Finals 4K Live Stream", "Fox Footy 504 HD, Channel 7HD, Kayo Alternative, AFL Grand Final MCG 4K 60FPS", "AFL Footy", "Every AFL round, Friday Night Footy, Super Saturday, Sunday Sunday matches, AFLW and Grand Final without blackout delays."),
    ("nrl-live-stream-iptv", "NRL Telstra Premiership & Finals 4K", "Fox League 502 HD, Channel 9HD, 9Now, NRL Finals, NRL Grand Final", "NRL Rugby League", "All NRL matches live, Thursday Night Footy, Friday Night double header, Super Saturday and Sunday NRL live."),
    ("state-of-origin-4k-iptv", "State of Origin Game 1, 2 & 3 in 4K UHD", "Channel 9HD, 9Now 4K, Fox League Pre-Game, Queensland Maroons vs NSW Blues", "State of Origin", "Stream the biggest rugby league rivalry in Australia in uncompressed 4K with multi-camera angles."),
    ("cricket-australia-the-ashes-iptv", "Cricket Australia & The Ashes 4K Live", "Fox Cricket 501 HD, Channel 7 Cricket, Kayo Cricket, BBL Big Bash League, Test Series", "Cricket Australia", "The Ashes, Border-Gavaskar Trophy, Australia vs India, Pakistan, England, BBL Big Bash League and ODI World Cup."),
    ("big-bash-league-bbl-iptv", "Big Bash League (BBL & WBBL) Live Stream", "Fox Cricket 501, 7plus HD, BBL Finals, Melbourne Stars, Sydney Sixers, Brisbane Heat", "Big Bash League", "Every T20 Big Bash match live with zero buffering and instant ball-by-ball HD playback."),
    ("premier-league-optus-sport-alternative", "English Premier League 4K (Optus Sport Alternative)", "Optus Sport 1-6 HD, Sky Sports Premier League, TNT Sports UK, NBC Sports 4K", "Premier League EPL", "All 380 EPL games live with English commentary, pre-match analysis, and full match replay."),
    ("champions-league-stan-sport-iptv", "UEFA Champions League & Europa League in 4K", "Stan Sport 4K, TNT Sports UHD, beIN Sports UEFA, UEFA Super Cup", "UEFA Champions League", "Every UCL group stage and knockout match live in 4K resolution on Australian NBN connections."),
    ("super-rugby-pacific-iptv", "Super Rugby Pacific & Wallabies Rugby", "Stan Sport 1-4, Fox Sports Rugby, Six Nations, The Rugby Championship, Bledisloe Cup", "Super Rugby & Wallabies", "Cheer for the Reds, Brumbies, Waratahs, Force, and Rebels plus all Wallabies test matches."),
    ("formula-1-australian-gp-iptv", "Formula 1 Australian Grand Prix (Melbourne Albert Park) 4K", "Fox Sports 506 HD, Sky Sports F1 4K, F1 TV Pro feeds, 4K On-Board Cameras", "Formula 1 Motorsport", "Practice, Qualifying, Sprint Races and Sunday Grand Prix for all 24 races in 4K 60FPS."),
    ("bathurst-1000-supercars-iptv", "Bathurst 1000 Supercars Mount Panorama Live", "Fox Sports 506, Channel 7HD, Supercars Championship, Gold Coast 500", "Bathurst 1000 Supercars", "The Great Race at Mount Panorama live from start to finish with multi-screen telemetry."),
    ("melbourne-cup-live-stream-iptv", "Melbourne Cup & Spring Racing Carnival 4K", "Racing.com, Channel 9HD, Sky Racing 1 & 2, The Everest, Caulfield Cup, Cox Plate", "Melbourne Cup Horse Racing", "The race that stops a nation live with expert tips, parade ring audio and HD photo finish."),
    ("ufc-ppv-main-event-australia-iptv", "UFC Numbered PPVs & Fight Night 4K (Main Event)", "Main Event PPV, ESPN HD, Sony Ten 4K, TNT Sports Box Office, UFC Fight Pass", "UFC & MMA PPV", "All numbered UFC PPVs included with zero extra $60-$80 pay-per-view fees in Australia."),
    ("boxing-ppv-main-event-iptv", "World Title Boxing PPV Live Stream Australia", "Main Event 4K, DAZN Boxing, Sky Sports Box Office, TNT Sports Box Office", "Boxing PPV", "Tim Tszyu, Tyson Fury, Canelo Alvarez, Anthony Joshua and all Australian title fights."),
    ("a-league-soccer-iptv-australia", "A-League Men & Women Live Stream Australia", "Paramount+ Sport, Channel 10HD, 10Bold, A-League Finals Series", "A-League Football", "All Melbourne Victory, Sydney FC, Brisbane Roar, Western United and A-League matches."),
    ("nba-basketball-australia-iptv", "NBA Basketball Live & NBA Finals 4K Australia", "ESPN 1 & 2 HD, NBA TV 4K, TNT NBA, ABC Sports, NBA Playoffs & Finals", "NBA Basketball", "Follow Australian NBA stars Josh Giddey, Ben Simmons, Dyson Daniels, Kyrie Irving and all 82 games."),
    ("australian-open-tennis-4k-iptv", "Australian Open Tennis Melbourne Park 4K", "Channel 9HD, Stan Sport Tennis 4K, Eurosport 1 & 2 4K, Wimbledon, Roland Garros, US Open", "Australian Open Tennis", "Rod Laver Arena, Margaret Court, and John Cain Arena all-court live feeds in pristine 4K HDR."),
    ("socceroos-world-cup-qualifiers-iptv", "Socceroos World Cup Qualifiers & Asian Cup", "Channel 10HD, Paramount+ Sport, AFC Asian Qualifiers 4K, beIN Sports Asia", "Socceroos Football", "Support the Australian national football team in their World Cup qualifying journey."),
    ("matildas-live-stream-iptv", "Matildas National Women's Football Live", "Channel 10HD, Paramount+, FIFA Women's Champions, Olympic Football", "Matildas Football", "Watch Sam Kerr and the Matildas live across all international friendlies and tournaments."),
    ("pga-golf-the-masters-australia-iptv", "PGA Tour Golf, The Masters & The Open 4K", "Fox Sports 503, Golf Channel 4K, Sky Sports Golf, Australian PGA Championship", "PGA Tour Golf", "All 4 majors, Australian Open Golf, LIV Golf tournaments in Adelaide with featured groups."),
    ("nfl-super-bowl-australia-iptv", "NFL American Football & Super Bowl in Australia", "ESPN HD, 7mate, NFL RedZone HD, DAZN NFL Game Pass, Super Bowl 4K", "NFL Football", "Sunday NFL RedZone, Monday Night Football, Thanksgiving games and the Super Bowl.")
]

# Devices List
devices_list = [
    ("iptv-on-amazon-firestick-australia", "Amazon Firestick 4K Max & Fire TV Cube", "Downloader App, IPTV Smarters Pro, TiviMate APK, Smart IPTV", "Firestick", "Complete guide to installing, configuring and optimizing 4K IPTV on Amazon Fire TV Stick in Australia."),
    ("iptv-on-samsung-smart-tv-tizen-australia", "Samsung Smart TV (Tizen OS 2018-2026)", "IBO Player, IPTV Smarters, Smart IPTV, Nanomid, Flix IPTV", "Samsung Smart TV", "How to install IPTV player apps on Samsung Tizen OS without needing extra TV boxes."),
    ("iptv-on-lg-smart-tv-webos-australia", "LG Smart TV (webOS 4.0 - 24)", "IBO Player Pro, Smart IPTV, IPTV Smarters Pro, SS IPTV", "LG Smart TV", "Stream AFL, NRL, and 4K movies directly from the LG Content Store with quick activation."),
    ("tivimate-iptv-player-australia-setup", "TiviMate IPTV Player (Android TV / Google TV)", "TiviMate Premium APK, Xtream Codes API, EPG TV Guide Sync, Multi-Screen", "TiviMate Player", "The #1 highest-rated IPTV player app for Australian users. 7-day Aussie EPG guide and instant channel switching."),
    ("iptv-smarters-pro-australia-guide", "IPTV Smarters Pro App (Firestick, Android, iOS, Windows)", "Xtream Codes API, M3U Playlist, Catch-Up TV, Master Search", "IPTV Smarters Pro", "Complete step-by-step setup guide for IPTV Smarters Pro with Australian server portal links."),
    ("iptv-on-apple-tv-tvos-australia", "Apple TV 4K & tvOS Devices", "iPlayTV, GSE Smart IPTV, IPTVX, UHF Player, Smarters Player Lite", "Apple TV 4K", "High-performance Apple TV 4K setup with buttery-smooth 60FPS sports playback."),
    ("iptv-on-android-tv-box-australia", "Android TV Box & Google TV (Chromecast 4K, Shield)", "Chromecast with Google TV, Nvidia Shield Pro, Xiaomi Mi Box, Mecool", "Android TV Box", "The ultimate guide for Google TV and Android streaming boxes with Telstra/Optus NBN optimization."),
    ("ibo-player-australia-activation", "IBO Player Pro App (Smart TVs & Fire TV)", "MAC Address activation, Device Key upload, M3U Playlist integration", "IBO Player", "Fast activation guide for IBO Player on Samsung, LG, Hisense, and Sony TVs."),
    ("formuler-z-mol3-iptv-australia", "Formuler Z11 Pro Max & MYTVOnline 3", "MYTVOnline 3 (MOL3), Dedicated Remote, Advanced PVR Recording", "Formuler Z Box", "Hardware-accelerated IPTV receiver with custom Electronic Program Guide and instant recording."),
    ("mag-box-stalker-portal-australia", "MAG Box 524 / 540 (Infomir Stalker Portal)", "MAC Address registration, Stalker Portal URL, Inner Portal Settings", "MAG Box", "Classic MAG box setup with stable Stalker middleware integration for Australian viewers."),
    ("chromecast-with-google-tv-iptv-australia", "Chromecast with Google TV 4K Setup", "Google Play Store, TiviMate, Downloader, Cloudflare 1.1.1.1 DNS", "Chromecast 4K", "Turn any TV with an HDMI port into a 4K Australian streaming powerhouse."),
    ("nvidia-shield-pro-4k-iptv-australia", "Nvidia Shield TV Pro 4K AI-Upscaling", "AI-Enhanced 4K Upscaling, Dolby Atmos, Gigabit Ethernet, TiviMate", "Nvidia Shield Pro", "The absolute highest fidelity streaming hardware for 8K and 4K sports in Australia."),
    ("kodi-iptv-simple-client-australia", "Kodi IPTV Simple Client & Addons", "PVR IPTV Simple Client, EPG XMLTV URL, M3U8 Playlist", "Kodi Player", "How to configure PVR IPTV Simple Client inside Kodi 21 Omega on PC, Mac, and Linux."),
    ("windows-mac-pc-iptv-player-australia", "Windows PC, Mac & Laptop IPTV Streaming", "VLC Media Player, IPTV Smarters PC, MyIPTV Player, SFVIP Player", "PC & Mac", "Watch Australian TV on your work laptop, MacBook, or Windows desktop computer.")
]

# Competitors & Alternatives List
competitors_list = [
    ("foxtel-alternative-iptv-australia", "Best Foxtel Alternative in Australia (Save $1,200/Year)", "Foxtel iQ5, Foxtel Now, Showcase, Fox8, Fox Sports AU, BoxSets", "Foxtel Alternative", "Why thousands of Australians are ditching Foxtel $100+/mo bills for $15/mo IPTV with identical 4K channels."),
    ("kayo-sports-alternative-iptv-australia", "Kayo Sports Alternative (All Fox Sports in 4K UHD)", "Fox Footy, Fox League, Fox Cricket, Fox Sports 503-507, ESPN, beIN", "Kayo Alternative", "Watch all Australian sports without Kayo price hikes, concurrent stream limits, or 720p compression."),
    ("stan-sport-alternative-iptv-australia", "Stan Sport Alternative (Super Rugby & Champions League)", "Stan Sport 1-4 4K, UEFA Champions League, UEFA Europa League, Wimbledon", "Stan Sport Alternative", "Get all Stan Sport premium events included directly without paying $27+/month on top of base plans."),
    ("optus-sport-alternative-iptv-australia", "Optus Sport Alternative (Premier League & La Liga 4K)", "Optus Sport 1-6 HD, EPL Live Streams, La Liga, J-League, WSL", "Optus Sport Alternative", "Never miss an Arsenal, Liverpool, Man City or Chelsea match with buffer-free English commentary."),
    ("binge-alternative-iptv-australia", "Binge Australia Alternative (160,000+ VOD Movies & Series)", "HBO Max, Warner Bros, House of the Dragon, Succession, White Lotus", "Binge Alternative", "Access the entire HBO, Warner, and Australian drama library on-demand in 4K with English subtitles."),
    ("fetch-tv-alternative-iptv-australia", "Fetch TV Alternative (Ultimate Channel Packs Included)", "Fetch Mini, Fetch Mighty, Movie Box, Variety Pack, Knowledge Pack", "Fetch TV Alternative", "Upgrade from restrictive Fetch TV subscription tiers to unrestricted 50,000+ live global channels."),
    ("sky-sports-uk-australia-iptv", "Sky Sports UK in Australia (Main Event, Premier League, F1)", "Sky Sports Main Event, Sky Sports Football, Sky Sports F1, Sky Sports Cricket", "Sky Sports UK", "Watch British sports coverage live from the UK with authentic UK studio commentary in Australia.")
]

# ISPs List
isps_list = [
    ("telstra-nbn-iptv-anti-freeze-guide", "Telstra NBN & 5G Home Internet IPTV Setup", "Telstra Smart Modem, Cloudflare 1.1.1.1 DNS, Telstra Throttling Fix", "Telstra NBN", "How to optimize Telstra NBN 50, 100, and 250 plans to eliminate prime-time footy buffering."),
    ("optus-broadband-iptv-optimization", "Optus NBN & Optus 5G Home Broadband Setup", "Optus Ultra WiFi Modem, DNS Configuration, Optus Sport Bypass", "Optus NBN", "Fix Optus transparent DNS proxy issues and stream uninterrupted 4K sports on Optus broadband."),
    ("tpg-internet-iptv-anti-buffering-guide", "TPG NBN & Vodafone Home Wireless IPTV Guide", "TPG VR1600v, Static DNS, TPG ISP Throttling Bypass", "TPG NBN", "Ensure lightning-fast channel switching on TPG, Vodafone, and iiNet broadband connections."),
    ("aussie-broadband-iptv-speed-guide", "Aussie Broadband NBN Fast Track Setup", "Aussie Broadband CVC Graphs, Local Sydney/Melb peering, Sub-10ms ping", "Aussie Broadband", "The cleanest, fastest NBN provider in Australia paired with local Australian IPTV CDN nodes."),
    ("starlink-australia-satellite-iptv-guide", "Starlink Satellite Internet IPTV in Regional Australia", "Starlink Gen 2/3 Router, Bypass Mode, Low-Earth Orbit Satellite Latency", "Starlink Australia", "How regional and rural Australian properties stream 4K IPTV flawlessly over Starlink satellite.")
]

# Languages List
languages_list = [
    ("indian-hindi-tv-channels-iptv-australia", "Indian & Hindi IPTV Channels in Australia (Star, Zee, Sony)", "Star Plus, Zee TV, Sony SAB, Colors, Aaj Tak, NDTV, Star Gold 4K", "Indian & Hindi", "The #1 Indian IPTV service in Sydney, Melbourne, Brisbane & Perth with 1,500+ Indian live channels."),
    ("punjabi-tv-channels-iptv-australia", "Punjabi IPTV Channels in Australia (PTC, Zee Punjabi)", "PTC Punjabi, Zee Punjabi, Chardikla Time TV, 9X Tashan, Punjabi Movies", "Punjabi TV", "Dedicated Punjabi channels, Gurbani live streams, and latest Punjabi cinema VOD."),
    ("tamil-telugu-iptv-australia", "Tamil & Telugu IPTV Channels Australia (Sun TV, Star Maa)", "Sun TV, Star Vijay, KTV, Zee Tamil, Star Maa, ETV Telugu, Zee Telugu", "Tamil & Telugu", "South Indian entertainment, regional news, and Kollywood/Tollywood movie releases."),
    ("arabic-lebanese-iptv-australia", "Arabic & Lebanese IPTV Channels Australia (MBC, Shahid, beIN)", "MBC 1-4, Shahid VIP, MTV Lebanon, LBCI, Al Jadeed, beIN Sports Arabic", "Arabic & Lebanese", "Over 2,000 Arabic channels covering Lebanon, Egypt, Syria, Iraq, UAE, and Jordan."),
    ("greek-tv-channels-iptv-australia", "Greek TV Channels in Australia (ERT, Mega, Antenna, Alpha)", "ERT World, Mega Cosmos, ANT1 Pacific, Alpha TV, Star International, Skai", "Greek TV", "Watch live news from Athens, Greek football Super League, and classic Greek cinema."),
    ("italian-tv-channels-iptv-australia", "Italian TV Channels in Australia (Rai, Mediaset, Sky Italia)", "Rai 1, Rai 2, Rai 3, Canale 5, Italia 1, Rete 4, Sky Sport Serie A", "Italian TV", "Live Italian television, Serie A football, Sanremo music festival and TG1 news in Australia."),
    ("vietnamese-tv-channels-iptv-australia", "Vietnamese IPTV Channels Australia (VTV, HTV, THVL)", "VTV1-VTV9, HTV7, THVL1, SCTV, Vietnamese movies and Paris By Night", "Vietnamese TV", "Popular Vietnamese channels and variety shows for Melbourne and Sydney Vietnamese communities."),
    ("filipino-tagalog-tv-iptv-australia", "Filipino IPTV Channels Australia (TFC, GMA Pinoy, Kapamilya)", "GMA Pinoy TV, GMA Life TV, Kapamilya Channel, Cinema One, TV5 Kapatid", "Filipino TV", "Teleseryes, PBA basketball, Eat Bulaga, and ABS-CBN/GMA news live in Australia."),
    ("chinese-mandarin-cantonese-iptv-australia", "Chinese (Mandarin & Cantonese) IPTV Channels Australia", "CCTV 1-15, TVB Jade, Phoenix TV, Hunan TV, Zhejiang TV, Now TV HK", "Chinese TV", "Hong Kong TVB, mainland Chinese CCTV/satellite networks, and Taiwanese drama channels.")
]

# Guides List
guides_list = [
    ("is-iptv-legal-in-australia-2026-guide", "Is IPTV Legal in Australia? (2026 Legal & Privacy Breakdown)", "ACMA Regulations, Copyright Act 1968, Personal Streaming Rights, VPN Use", "IPTV Legal Guide", "Everything you need to know about Australian ACMA regulations, ISP copyright policies, and safe streaming."),
    ("how-to-start-iptv-reseller-business-australia", "How to Start an IPTV Reseller Business in Australia (Step-by-Step)", "Wholesale Credits AUD, Customer Acquisition, Pricing Strategy, PayID Setup", "Start Reseller Business", "A complete roadmap to earning $3,000 - $10,000 AUD monthly reselling IPTV in Sydney, Melbourne and Brisbane."),
    ("iptv-reseller-panel-pricing-credits-aud", "IPTV Reseller Panel Pricing & Wholesale Credits in AUD", "50 Credits ($180 AUD), 100 Credits ($320 AUD), Sub-Resellers, Profit Margins", "Reseller Pricing AUD", "Transparent breakdown of wholesale credit costs, profit margins, and sub-reseller tree management."),
    ("how-to-fix-iptv-buffering-australia", "How to Fix IPTV Buffering in Australia (Ultimate 7-Step Guide)", "NBN DNS Fix, ISP Throttling Bypass, Buffer Size Cache, 5GHz Wi-Fi vs Ethernet", "Fix Buffering Guide", "Eliminate stuttering and freezing during live AFL and NRL matches with verified network adjustments."),
    ("best-vpn-for-iptv-australia-2026", "Best VPN for IPTV in Australia (ExpressVPN, NordVPN, Surfshark)", "Anti-ISP Throttling, Dedicated Australian Servers, WireGuard Protocol", "Best VPN Guide", "Why using a fast Australian VPN server ensures 100% privacy and bypasses ISP prime-time bandwidth caps."),
    ("m3u-playlist-url-xtream-codes-api-australia", "M3U Playlist URL & Xtream Codes API Guide for Australia", "M3U Plus, Xtream Codes Server URL, Username & Password, EPG XMLTV Link", "M3U & Xtream API", "How to use your M3U link and Xtream codes on any IPTV player app with automatic EPG sync."),
    ("australian-payid-bank-transfer-iptv-payments", "How to Pay for IPTV via PayID & Osko Direct Transfer in Australia", "PayID Email/Phone, Instant Settlement, Zero Surcharge, Commonwealth, ANZ, NAB, Westpac", "PayID Payments AUD", "Pay securely in Australian Dollars using your banking app with instant automatic activation.")
]

print(f"Categories defined: {len(cities_list)} Cities, {len(sports_list)} Sports, {len(devices_list)} Devices, {len(competitors_list)} Competitors, {len(isps_list)} ISPs, {len(languages_list)} Languages, {len(guides_list)} Guides.")

print("SEO Engine initialization complete.")

import os, shutil

IMG_DIR = r"c:\Users\clanm\OneDrive\Desktop\australiatv\public\images"

aliases = {
    'visa-logo.webp': [f for f in os.listdir(IMG_DIR) if 'visa' in f.lower()][0],
    'mastercard-logo.webp': 'Mastercard-logo.svg.webp',
    'apple-pay-logo.webp': 'Apple_Pay_logo.svg.webp',
    'google-pay-logo.webp': '6124998.webp',
    'paypal-logo.webp': 'Paypal_2014_logo.webp',
    'crypto-logo.webp': '360_F_242832348_HvNHaiEu6tAlklMGTSYgjS20RV2jjeKq.webp',
    'afl-nrl-stadium.webp': 'packimages2/lucid-origin_Dramatic_wide_night_photo_of_a_packed_football_stadium_floodlights_green_pitch_p-0.webp',
    'cricket-ashes.webp': 'cricket-iptv-australia-sports.webp',
    'formula-1-aus.webp': 'packimages2/lucid-origin_Formula-style_open-wheel_racing_car_at_night_on_a_city_circuit_motion_blur_neon_-0.webp',
    'ufc-boxing-main-event.webp': 'packimages2/lucid-origin_Fighter_in_a_boxing_ring_seen_from_behind_glove_raised_arena_lights_and_smoke_cr-0.webp',
    'premier-league-soccer.webp': 'fussball-streaming.webp',
    'nbl-basketball.webp': 'packimages2/lucid-origin_Basketball_arena_a_player_in_generic_plain_jersey_dunking_dramatic_spotlights_a_-0.webp',
    'living-room-tv.webp': 'home/living-room-hero.webp',
    'family-tv.webp': 'iptv-familie-fernsehen.webp',
    'apps-dashboard.webp': 'beste-iptv-apps-dashboard.webp',
    'vod-dashboard.webp': 'iptv-entertainment-dashboard.webp',
    'google-tv-dashboard.webp': 'iptv-google-tv-dashboard.webp',
    'quality-4k.webp': 'iptv-4k-qualitaet.webp',
    'server-infra.webp': 'iptv-server-infrastruktur.webp',
    'anti-freeze-tech.webp': 'iptv-streaming-technologie.webp',
    'zero-buffer.webp': 'iptv-ohne-buffering-illustration.webp',
    'support-team.webp': 'iptv-support-team.webp',
    'safe-payment.webp': 'iptv-sichere-zahlung.webp',
    'cable-vs-iptv.webp': 'iptv-vs-kabel-infografik.webp',
    'provider-comparison.webp': 'iptv-anbieter-vergleich-2026.webp',
    'vpn-shield.webp': 'iptv-vpn-schutz.webp',
    'home-cinema.webp': 'iptv-heimkino.webp'
}

for dest, src in aliases.items():
    src_path = os.path.join(IMG_DIR, src)
    dest_path = os.path.join(IMG_DIR, dest)
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dest_path)
        print(f"Created alias: {dest} -> {src}")
    else:
        print(f"NOT FOUND: {src}")

print("Image aliases setup complete!")

import os, glob

BASE_DIR = r"c:\Users\clanm\OneDrive\Desktop\australiatv"

all_html = glob.glob(os.path.join(BASE_DIR, "**", "*.html"), recursive=True)
sitemaps = glob.glob(os.path.join(BASE_DIR, "sitemap*.xml"))
robots = os.path.exists(os.path.join(BASE_DIR, "robots.txt"))

print(f"Total HTML files generated: {len(all_html)}")
print(f"Total Sitemaps: {len(sitemaps)}")
for sm in sitemaps:
    size = os.path.getsize(sm)
    with open(sm, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"  - {os.path.basename(sm)}: {len(lines)} lines ({size} bytes)")

print(f"robots.txt exists: {robots}")

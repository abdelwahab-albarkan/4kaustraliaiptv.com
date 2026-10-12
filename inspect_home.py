import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\'][^>]*>', content)
h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
print("SECTIONS FOUND:")
for s in sections:
    print("- Section ID:", s)

print("\nH2 HEADINGS FOUND (" + str(len(h2s)) + "):")
for h in h2s:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    print("- H2:", clean)

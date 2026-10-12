with open('all_parsed_keywords.txt', 'r', encoding='utf-8', errors='ignore') as f:
    kws = []
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) >= 4:
            try:
                kws.append({
                    'volume': int(parts[0]),
                    'kd': int(parts[1]) if parts[1].isdigit() else 0,
                    'intent': parts[2],
                    'keyword': parts[3],
                    'src': parts[4] if len(parts) > 4 else ''
                })
            except:
                pass

print(f"Total parsed keywords: {len(kws)}")

sorted_kws = sorted(kws, key=lambda x: x['volume'], reverse=True)
print("\nTop 40 Keywords by Search Volume in Australia:")
for k in sorted_kws[:40]:
    print(f"- {k['keyword']} (Vol: {k['volume']:,}, KD: {k['kd']})")

iptv_kws = [k for k in sorted_kws if 'iptv' in k['keyword'].lower()]
print(f"\nTotal keywords containing 'iptv': {len(iptv_kws)}")
print("\nTop 30 IPTV-specific keywords:")
for k in iptv_kws[:30]:
    print(f"- {k['keyword']} (Vol: {k['volume']:,}, KD: {k['kd']})")

reseller_kws = [k for k in sorted_kws if 'reseller' in k['keyword'].lower() or 'panel' in k['keyword'].lower() or 'credit' in k['keyword'].lower()]
print(f"\nTotal keywords containing 'reseller' or 'panel': {len(reseller_kws)}")
print("\nTop 20 Reseller keywords:")
for k in reseller_kws[:20]:
    print(f"- {k['keyword']} (Vol: {k['volume']:,}, KD: {k['kd']})")

sports_kws = [k for k in sorted_kws if any(s in k['keyword'].lower() for s in ['foxtel', 'kayo', 'afl', 'nrl', 'optus sport', 'stan sport', 'cricket'])]
print(f"\nTotal Australian Sports/Competitor keywords: {len(sports_kws)}")
print("\nTop 30 Australian Sports keywords:")
for k in sports_kws[:30]:
    print(f"- {k['keyword']} (Vol: {k['volume']:,}, KD: {k['kd']})")

import os, glob, csv, re
from collections import defaultdict

data_dir = r"c:\Users\clanm\OneDrive\Desktop\australiatv\dataaustralia"
csv_files = glob.glob(os.path.join(data_dir, "*.csv"))

all_keywords = {}

for fpath in csv_files:
    fname = os.path.basename(fpath)
    try:
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.reader(f)
            header = None
            for row in reader:
                if not row or len(row) < 2:
                    continue
                # identify header
                row_lower = [c.strip().lower() for c in row]
                if not header:
                    if any("keyword" in c for c in row_lower):
                        header = row_lower
                        continue
                if header:
                    kw = ""
                    vol = 0
                    kd = 0
                    intent = ""
                    
                    for idx, col in enumerate(header):
                        if idx >= len(row):
                            continue
                        val = row[idx].strip()
                        if col == "keyword":
                            kw = val
                        elif "volume" in col or "search volume" in col:
                            v_clean = val.replace(",", "").replace(" ", "")
                            if v_clean.isdigit():
                                vol = int(v_clean)
                            elif v_clean.replace('.', '', 1).isdigit():
                                vol = int(float(v_clean))
                        elif "difficulty" in col or "kd" in col:
                            kd_clean = val.replace(",", "").strip()
                            if kd_clean.isdigit():
                                kd = int(kd_clean)
                        elif "intent" in col:
                            intent = val
                    
                    if kw and len(kw) >= 2 and not kw.isdigit():
                        kw_norm = kw.lower().strip()
                        if kw_norm not in all_keywords or vol > all_keywords[kw_norm]['volume']:
                            all_keywords[kw_norm] = {
                                'keyword': kw.strip(),
                                'volume': vol,
                                'kd': kd,
                                'intent': intent,
                                'source': fname
                            }
    except Exception as e:
        print(f"Error parsing {fname}: {e}")

print(f"Total unique parsed keywords from 67 CSVs: {len(all_keywords)}")

# Sort by volume
sorted_kws = sorted(all_keywords.values(), key=lambda x: x['volume'], reverse=True)

print("\n--- TOP 50 HIGHEST VOLUME KEYWORDS ---")
for idx, k in enumerate(sorted_kws[:50], 1):
    print(f"{idx:2d}. Vol: {k['volume']:7d} | KD: {k['kd']:2d} | {k['keyword']} ({k['source']})")

with open(r"c:\Users\clanm\OneDrive\Desktop\australiatv\all_parsed_keywords.txt", "w", encoding="utf-8") as out:
    for k in sorted_kws:
        out.write(f"{k['volume']}\t{k['kd']}\t{k['intent']}\t{k['keyword']}\t{k['source']}\n")

print("\nFull parsed keywords saved to all_parsed_keywords.txt")

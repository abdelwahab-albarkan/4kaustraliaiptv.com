import os, glob, csv, re
from collections import defaultdict

data_dir = r"c:\Users\clanm\OneDrive\Desktop\australiatv\dataaustralia"
csv_files = glob.glob(os.path.join(data_dir, "*.csv"))

print(f"Found {len(csv_files)} CSV files in {data_dir}")

keywords_dict = {}

for fpath in csv_files:
    fname = os.path.basename(fpath)
    try:
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.reader(f)
            header = None
            for row in reader:
                if not row or len(row) < 2:
                    continue
                # find header line
                first_cell = row[0].strip().lower()
                if "keyword" in first_cell and not header:
                    header = [c.strip().lower() for c in row]
                    continue
                if header:
                    # extract keyword and volume
                    try:
                        kw_idx = 0
                        vol_idx = 1
                        for i, h in enumerate(header):
                            if "keyword" in h:
                                kw_idx = i
                            elif "volume" in h or "search volume" in h:
                                vol_idx = i
                        kw = row[kw_idx].strip()
                        if not kw or len(kw) < 2:
                            continue
                        vol_str = row[vol_idx].replace(",", "").strip() if len(row) > vol_idx else "0"
                        vol = int(float(vol_str)) if vol_str.replace('.', '', 1).isdigit() else 0
                        
                        kw_clean = kw.lower()
                        if kw_clean not in keywords_dict or vol > keywords_dict[kw_clean]['volume']:
                            keywords_dict[kw_clean] = {
                                'keyword': kw,
                                'volume': vol,
                                'source': fname
                            }
                    except Exception as e:
                        pass
    except Exception as e:
        print(f"Error reading {fname}: {e}")

print(f"Total unique keywords extracted: {len(keywords_dict)}")

# Sort by volume
sorted_kws = sorted(keywords_dict.values(), key=lambda x: x['volume'], reverse=True)

print("\n--- TOP 30 HIGHEST VOLUME KEYWORDS ---")
for k in sorted_kws[:30]:
    print(f"{k['volume']:8d} | {k['keyword']} (source: {k['source']})")

with open(r"c:\Users\clanm\OneDrive\Desktop\australiatv\extracted_summary.txt", "w", encoding="utf-8") as out:
    out.write(f"Total extracted keywords: {len(keywords_dict)}\n\n")
    for k in sorted_kws:
        out.write(f"{k['volume']}\t{k['keyword']}\t{k['source']}\n")

print("\nSummary saved to extracted_summary.txt")

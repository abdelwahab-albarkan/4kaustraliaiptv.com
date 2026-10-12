import os

all_images = {}
for root, dirs, files in os.walk('public/images'):
    rel = os.path.relpath(root, 'public/images').replace('\\', '/')
    for f in files:
        if f.lower().endswith(('.webp', '.png', '.jpg', '.jpeg', '.svg')):
            ext = os.path.splitext(f)[1]
            full_path = os.path.join(root, f)
            size = os.path.getsize(full_path)
            all_images[f"{rel}/{f}" if rel != '.' else f] = size

print(f"Total images found: {len(all_images)}")
print("\n--- ROOT IMAGES ---")
for k in sorted([k for k in all_images if '/' not in k]):
    print(f"- {k} ({all_images[k]:,} bytes)")

print("\n--- SUBFOLDER IMAGES ---")
for k in sorted([k for k in all_images if '/' in k]):
    print(f"- {k} ({all_images[k]:,} bytes)")

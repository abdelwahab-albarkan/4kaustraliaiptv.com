# 4K Australia IPTV (4kaustraliaiptv.com)

Static HTML website. No framework and no build step needed to host it: upload the folder as it is.

- Pages: about 2,100 HTML files. 158 are indexable and listed in `sitemap.xml`; the rest are `noindex, follow`.
- Shared files: `assets/css/style.css`, `assets/js/app.js` (the `?v=` number in every page is bumped with `py bump_assets.py <css> <js>`).
- Sitemaps: `sitemap.xml` (index) and `sitemap-*.xml`. `robots.txt` points to it.
- Contact: WhatsApp +212625218443, support@4kaustraliaiptv.com.
- Analytics: set `GA_MEASUREMENT_ID` in `assets/js/app.js`. It loads only after the visitor accepts cookies.
- IndexNow: upload `817b9ca250bfeb6b52ffe4e750a08a61.txt` to the root, then run `node index-now.js`.
- Local preview: `py -m http.server 8099`.
- The `*.py` files are the scripts that generated and audited the pages. They are not part of the website. Reports: `SEO-AUDIT-REPORT.md`, `SEO-REPORT.md`, `BACKLINK-PLAN.md`.

Host settings to add (not possible from files): force HTTPS and 301 `www` to the non-www domain.

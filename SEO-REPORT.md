# SEO report (generated)

## 1. Site settings report
| Setting | Current value | Status | Recommended fix |
|---|---|---|---|
| robots.txt | Allow all + sitemap line | ✅ |  |
| XML sitemap | 385 URLs in 9 files | ✅ |  |
| Canonical domain | All canonicals use https://4kaustraliaiptv.com | ✅ |  |
| Language / locale | lang="en-AU", og:locale en_AU | ✅ |  |
| Hreflang | en-AU + x-default (self) | ✅ |  |
| Open Graph + Twitter card | On every page | ✅ |  |
| Organization + WebSite schema | Homepage only | ✅ |  |
| Favicon | None declared | ⚠️ | Add a favicon (32x32 PNG + SVG). |
| Custom 404 page | None | ⚠️ | Add 404.html with search links (host must serve it). |
| Google Search Console | No verification tag; domain property needs DNS | ⚠️ | Add the Domain property (DNS TXT) and submit sitemap.xml. |
| Analytics | GA4 ID is empty | ⚠️ | Paste Measurement ID into assets/js/app.js. |
| www / HTTPS redirects | Server-side, cannot be checked from files | ⚠️ | 301 www to non-www and force HTTPS at the host. |
| Pretty URLs | Folder URLs with trailing slash | ✅ |  |

**Top 5 fixes:** 1) Search Console + sitemap, 2) GA4 ID, 3) www/HTTPS 301, 4) favicon, 5) 404 page.

## 2. SEO audit
- Indexable pages: 386 of 2101. Indexable titles/descriptions are unique and in range.
- Biggest risks: templated near-duplicate pages (topics, cities) and a very large homepage.
- Strong: 0 broken links, 0 orphans, schema valid on every page.

| Issue | Priority | Affected pages | Fix |
|---|---|---|---|
| Thin content (<300 words) | High | 8 | Expand or noindex; top: about/index.html, channels.html, contact.html |
| Meta description over 160 chars | Medium | 0 | Trim |
| Title under 30 chars | Low | 48 | Add the keyword and a benefit |
| Heading level skipped (e.g. H2 to H4) | Low | 385 | Fix the heading order |
| More than 12 H2 on one page | Medium | 1 | Split index.html |
| Images without alt | High | 0 | Add alt text |
| Images without width/height (layout shift) | Medium | 382 | Add dimensions |
| HTML over 150 KB | High | 1 | Homepage ~330 KB: move sections to their own pages |
| http:// links (mixed content) | Medium | 0 | Use https |

Next steps: 1) split the homepage, 2) write unique copy for the top 20 topic pages and 10 city pages, 3) add favicon/404, 4) connect Search Console and GA4.

## 3. On-page: index.html (focus: best iptv australia)
| Element | Current status | Problem / fix |
|---|---|---|
| Focus keyword "best iptv australia" in title | No | Add keyword |
| Keyword in H1 | Yes |  |
| Keyword in first 100 words | No | Mention it in the opening paragraph |
| Keyword in URL | No | Optional |
| Title length | 61 chars |  |
| Description length | 95 chars |  |
| Word count | 9147 |  |
| H1 count | 1 |  |
| H2 count | 36 | Too many, split page |
| Internal / external links | 380 / 26 |  |
| Images with alt | 78 of 78 |  |

## 3. On-page: best-iptv-australia/index.html (focus: best iptv australia)
| Element | Current status | Problem / fix |
|---|---|---|
| Focus keyword "best iptv australia" in title | Yes |  |
| Keyword in H1 | Yes |  |
| Keyword in first 100 words | No | Mention it in the opening paragraph |
| Keyword in URL | Yes | Optional |
| Title length | 59 chars |  |
| Description length | 158 chars |  |
| Word count | 915 |  |
| H1 count | 1 |  |
| H2 count | 3 |  |
| Internal / external links | 41 / 6 |  |
| Images with alt | 7 of 7 |  |

## 4. Pages whose title/H1/first paragraph do not contain their own main phrase
Pages checked: guides, devices, comparisons, languages, ISPs, sports. Mismatches: 6
| Page | Suggested focus keyword |
|---|---|
| comparisons/index.html | comparisons iptv australia |
| devices/index.html | devices iptv australia |
| guides/australian-payid-bank-transfer-iptv-payments/index.html | australian payid bank transfer iptv australia |
| isps/index.html | isps iptv australia |
| languages/index.html | languages iptv australia |
| sports/index.html | sports iptv australia |

## 5. Schema checklist
**index.html** found: Product, Organization, WebSite, FAQPage
- ❌ missing, add BreadcrumbList
- ✅ FAQPage matches visible questions (9 in schema / 9 on page)
- ✅ Organization has logo + contactPoint
- ⚠️ Organization has no sameAs. Add real social profile URLs when you have them.
- ⚠️ Product/AggregateOffer lists a price range only. Add one Offer per plan if you want price rich results.
**best-iptv-australia/index.html** found: BreadcrumbList, FAQPage, WebPage, Article, HowTo
- ✅ BreadcrumbList
- ✅ FAQPage matches visible questions (5 in schema / 5 on page)
- ✅ HowTo / Article present
**devices/iptv-on-amazon-firestick-australia/index.html** found: BreadcrumbList, FAQPage, HowTo
- ✅ BreadcrumbList
- ✅ FAQPage matches visible questions (2 in schema / 2 on page)
- ✅ HowTo / Article present
**tools/iptv-bandwidth-calculator/index.html** found: BreadcrumbList, WebApplication, FAQPage
- ✅ BreadcrumbList
- ✅ FAQPage matches visible questions (3 in schema / 3 on page)

## 6. Recommended schema by section
| Section | Pages (indexable) | Current schema | Recommended |
|---|---|---|---|
| about | 1 | BreadcrumbList, AboutPage | keep |
| best-iptv-australia | 1 | BreadcrumbList, FAQPage, WebPage, Article | keep |
| cities | 71 | BreadcrumbList, FAQPage, CollectionPage | WebPage + BreadcrumbList + FAQPage |
| comparisons | 8 | BreadcrumbList, FAQPage, Article, CollectionPage | Article + FAQPage |
| devices | 15 | BreadcrumbList, FAQPage, HowTo, CollectionPage | HowTo + FAQPage |
| directory | 1 |  | keep |
| guides | 11 | BreadcrumbList, FAQPage, Article, HowTo | Article + HowTo + FAQPage |
| iptv-box-australia | 1 | BreadcrumbList, FAQPage, WebPage, Article | keep |
| iptv-free-trial-australia | 1 | BreadcrumbList, FAQPage, WebPage, Article | keep |
| iptv-player-australia | 1 | BreadcrumbList, FAQPage, WebPage, Article | keep |
| isps | 6 | BreadcrumbList, FAQPage, CollectionPage | Article + HowTo |
| languages | 10 | BreadcrumbList, FAQPage, CollectionPage | Article |
| privacy-policy | 1 | BreadcrumbList | keep |
| refund-policy | 1 | BreadcrumbList | keep |
| root | 6 | ContactPage, Product, Organization, WebSite | keep |
| sports | 21 | BreadcrumbList, FAQPage, CollectionPage | WebPage + BreadcrumbList |
| terms-of-service | 1 | BreadcrumbList | keep |
| tools | 2 | BreadcrumbList, CollectionPage, WebApplication, FAQPage | keep |
| topic | 227 | BreadcrumbList, FAQPage | WebPage + BreadcrumbList (FAQPage only if answers are unique) |

## 7. Link analysis: index.html
Summary: 380 internal, 26 external links, 0 broken.
| External domain | Count | Type | Issue |
|---|---|---|---|
| wa.me | 18 | External | None |
| 4kdeutsch.com | 1 | External | Sister site: keep few and relevant |
| 4kanbieteriptv.de | 1 | External | Sister site: keep few and relevant |
| germanystreamtv.com | 1 | External | Sister site: keep few and relevant |
| streamgermany4k.com | 1 | External | Sister site: keep few and relevant |
| 4kiptvfr.com | 1 | External | Sister site: keep few and relevant |
| 4kspaintv.com | 1 | External | Sister site: keep few and relevant |
| ukstream4k.com | 1 | External | Sister site: keep few and relevant |
| 4ksubscriptioniptv.com | 1 | External | Sister site: keep few and relevant |

## 8. Indexable pages with the fewest internal links pointing to them
| Page | Inbound internal links | Suggested pages to link from |
|---|---|---|
| cities/adelaide/best-iptv/index.html | 1 | cities/index.html, cities/adelaide/firestick-setup/index.html |
| cities/adelaide/firestick-setup/index.html | 1 | cities/index.html, cities/adelaide/best-iptv/index.html |
| cities/adelaide/free-trial/index.html | 1 | cities/index.html, cities/adelaide/best-iptv/index.html |
| cities/adelaide/reseller-panel/index.html | 1 | cities/index.html, cities/adelaide/best-iptv/index.html |
| cities/adelaide/sports-channels/index.html | 1 | cities/index.html, cities/adelaide/best-iptv/index.html |
| cities/adelaide/subscription/index.html | 1 | cities/index.html, cities/adelaide/best-iptv/index.html |
| cities/brisbane/best-iptv/index.html | 1 | cities/index.html, cities/adelaide/index.html |
| cities/brisbane/firestick-setup/index.html | 1 | cities/index.html, cities/adelaide/index.html |
| cities/brisbane/free-trial/index.html | 1 | cities/index.html, cities/adelaide/index.html |
| cities/brisbane/reseller-panel/index.html | 1 | cities/index.html, cities/adelaide/index.html |
| cities/brisbane/sports-channels/index.html | 1 | cities/index.html, cities/adelaide/index.html |
| cities/brisbane/subscription/index.html | 1 | cities/index.html, cities/adelaide/index.html |

## 9. Suggested internal links for best-iptv-australia/
| Anchor text | Link to | Where to place |
|---|---|---|
| IPTV bandwidth calculator | tools/iptv-bandwidth-calculator/ | In "How to test an IPTV service", step 4 |
| how much internet speed you need | guides/how-much-internet-speed-for-iptv-australia/ | Criteria card "Stability on NBN" |
| change your DNS | guides/best-dns-for-iptv-australia/ | Under the buffering tip |
| fix an empty TV guide | guides/iptv-epg-guide-explained-australia/ | FAQ about programme guides |
| Foxtel alternative | comparisons/foxtel-alternative-iptv-australia/ | Comparison table intro |
| IPTV on Samsung and LG TVs | devices/iptv-on-samsung-smart-tv-tizen-australia/ | Device criteria card |

## 10. Does the first paragraph answer the question? (main content pages)
| Page | Direct answer at top | Note |
|---|---|---|
| comparisons/binge-alternative-iptv-australia/index.html | No | First paragraph 15 words: Access the entire HBO, Warner, and Australian drama library on-demand ... |
| comparisons/fetch-tv-alternative-iptv-australia/index.html | No | First paragraph 13 words: Upgrade from restrictive Fetch TV subscription tiers to unrestricted 5... |
| comparisons/kayo-sports-alternative-iptv-australia/index.html | No | First paragraph 14 words: Watch all Australian sports without Kayo price hikes, concurrent strea... |
| comparisons/optus-sport-alternative-iptv-australia/index.html | No | First paragraph 14 words: Never miss an Arsenal, Liverpool, Man City or Chelsea match with buffe... |
| comparisons/sky-sports-uk-australia-iptv/index.html | No | First paragraph 15 words: Watch British sports coverage live from the UK with authentic UK studi... |
| devices/chromecast-with-google-tv-iptv-australia/index.html | No | First paragraph 25 words: Complete installation guide for Chromecast 4K. Stream AFL, NRL, and 16... |
| devices/formuler-z-mol3-iptv-australia/index.html | No | First paragraph 26 words: Complete installation guide for Formuler Z Box. Stream AFL, NRL, and 1... |
| devices/ibo-player-australia-activation/index.html | No | First paragraph 26 words: Complete installation guide for IBO Player. Stream AFL, NRL, and 160,0... |
| devices/iptv-on-amazon-firestick-australia/index.html | No | First paragraph 25 words: Complete installation guide for Firestick. Stream AFL, NRL, and 160,00... |
| devices/iptv-on-android-tv-box-australia/index.html | No | First paragraph 29 words: Complete installation guide for Android TV Box. Stream AFL, NRL, and 1... |
| devices/iptv-on-apple-tv-tvos-australia/index.html | No | First paragraph 28 words: Complete installation guide for Apple TV 4K. Stream AFL, NRL, and 160,... |
| devices/iptv-on-lg-smart-tv-webos-australia/index.html | No | First paragraph 28 words: Complete installation guide for LG Smart TV. Stream AFL, NRL, and 160,... |
Result: 13 pages have a short direct opening, 41 need one.

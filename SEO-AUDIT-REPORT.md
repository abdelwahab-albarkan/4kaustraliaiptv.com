# SEO, indexing and content audit: 4kaustraliaiptv.com (12 Oct 2026)

Scope: static HTML site (no framework, so no TypeScript, lint, build or middleware). Validation was done with scripts that read every page and with HTTP requests against a local server.
Not available: Google Search Console data. Causes below are inferred from the site, not read from GSC. Send a GSC export (Pages report, both "not indexed" lists) to confirm them.

## 1. Why Google probably refuses to index pages (root causes, most likely first)
| # | Cause | Evidence in the files | Severity |
|---|---|---|---|
| 1 | Thousands of near-identical template pages submitted at once | 1,400 topic pages (47-73% shared text), 533 city pages (same template, only the place name changed), 100 sports sub-pages | Critical |
| 2 | Pages with no relation to what the site is good at | 1,380 topic pages about Samsung TV sizes, Apple TV shows, Netflix/Stan/Kayo subscriptions, remotes, internet providers, and piracy-site names | Critical |
| 3 | Unverifiable claims and fake social proof (trust signals) | fake testimonials, invented "activated" pop-ups, "8ms / under 15ms latency", "99.98% uptime", "#1" labels, "12,000+ resellers", Product schema with a fake rating on every page | High |
| 4 | New domain, no external links | 0 known backlinks; sister sites linked only from 2 pages | High |
| 5 | Thin or generic copy on important pages | device/comparison/ISP/language intros were boilerplate ("Complete installation guide for ..."); commercial root pages under 300 words | High |
| 6 | Missing trust pages | no About, Privacy, Terms or Refund (added 11 Oct) | Medium |
| 7 | Very heavy homepage (330 KB, 9,000 words, 36 H2) | index.html | Medium |
| 8 | Keyword conflict between homepage and guide | both used "Best IPTV Australia" in title and H1 | Medium |
| 9 | Technical SEO | clean: canonicals, sitemap, hreflang, robots, JSON-LD, 0 broken links | OK |

"Discovered, not indexed" is typical when Google finds a very large number of low-value URLs in a sitemap on a new domain: it postpones crawling them. "Crawled, not indexed" is typical for templated or thin pages. Both patterns match causes 1, 2 and 5.

## 2. What was changed (this session and earlier)
### Index scope (not done to improve GSC numbers: each group has a content reason)
| Group | Count | Decision | Reason |
|---|---|---|---|
| Topic pages about other brands, TV sizes, remotes, other services' subscriptions, internet providers, piracy-site names | 1,381 | D: noindex,follow | No relation to the business, duplicate template, some target unlicensed streaming sites |
| 19 topic pages about IPTV, devices and sport streaming | 19 | A: keep + improved | Real search intent, rewritten with unique copy |
| Small-town city pages | 482 | D: noindex,follow | Doorway-style template; only the place name differs |
| 10 city hubs + 40 local pages (best IPTV, subscription, free trial, sport) | 50 | A: keep + improved | Local intent, local teams and seasons added |
| Firestick-setup and reseller-panel city pages | 20 | D | Same content as /devices/ and /reseller.html |
| Sports "without-foxtel" and "fixtures" sub-pages | 80 | D for now, improve later | Template copy; intent is real, so write unique copy for the 5 biggest sports and re-index |
| Everything else (home, pillars, hubs, guides, devices, comparisons, ISPs, languages, tools, legal) | 139 | B/A keep | |

### Fixes by problem
| Problem | Fix | Files |
|---|---|---|
| Homepage and /best-iptv-australia/ competed for the same phrase | Homepage now targets "IPTV Australia: Subscription, Free Trial and Reseller Panel"; the guide owns "best IPTV Australia" | index.html (title, meta, H1, intro) |
| Premier League page duplicated the Optus Sport comparison | Premier League page re-pointed to kick-off times and setup; comparison keeps the "alternative" intent | sports/premier-league-optus-sport-alternative/index.html |
| Unsupported numbers and superlatives | Removed latency, uptime, "#1", "100% anti-freeze", filler phrases | all 2,102 pages |
| Boilerplate openings, no direct answer | Direct-answer intro + unique how-to blocks | 14 devices, 7 comparisons, 5 ISPs, 9 languages, 19 topics, 40 city pages |
| Language pages 54-68% identical | Community-specific copy (channels people ask for, time zones, events) | 9 pages under /languages/ |
| Thin commercial pages | Added buying criteria, channel checks, reseller checklist | providers.html, channels.html, reseller.html, tools/index.html |
| No structure above pages | 8 hub pages, breadcrumbs pointing to hubs | /devices/ /sports/ /guides/ /comparisons/ /isps/ /languages/ /cities/ /tools/ |
| Weak internal links | related blocks (292 pages), city siblings, pillar-to-city chips, privacy/reseller/setup contextual links | many |
| Missing BreadcrumbList / og tags on 6 root pages | Added | providers, channels, setup, reseller, contact, directory |
| Heading order (h2 to h4, h1 to h3) | 2,127 headings fixed, hero card title is no longer a heading | all pages |
| Titles outside 30-62 characters | 4 hub titles shortened | build_hubs.py + 4 hubs |
| No favicon, no 404 page | favicon.svg, favicon-48.png, apple-touch-icon.png, 404.html (noindex) | all pages, 404.html |
| Product schema on every page (misleading) | Removed everywhere except the homepage | 2,074 pages |
| Sitemap listed 2,000+ URLs | Now only the 158 indexable pages | sitemap-*.xml |
| Domain | iptvaustralia.app replaced by 4kaustraliaiptv.com in canonicals, hreflang, og, schema, sitemaps, robots.txt | all |

## 3. Pages intentionally left unchanged
* Canonicals, hreflang (single language, self-referencing en-AU + x-default), robots.txt, JSON-LD validity: all correct.
* Legal pages (About, Privacy, Terms, Refund): left indexable; they build trust and cost nothing.
* /directory/: kept indexable as a link hub; thin text is acceptable for a navigation page.
* Contact page (under 300 words): it is a utility page.
* chromecast vs android-tv-box device guides (62% token overlap in titles): different devices, different intent.

## 4. Cannibalisation decisions
| Pair | Decision |
|---|---|
| Homepage vs best-iptv-australia | Differentiate (done) |
| comparisons/optus-sport-alternative vs sports/premier-league | Differentiate (done) |
| topic/amazon-firestick vs topic/firestick-4k-max vs devices/iptv-on-amazon-firestick | Keep all three: model comparison, model setup tips, general setup. Watch in GSC; if they swap rankings, merge the two topic pages into the device guide |
| topic/tv-box vs topic/streaming-devices vs iptv-box-australia | Candidate for C (merge into iptv-box-australia) if GSC shows overlap. Not merged automatically |
| 10 city free-trial pages vs iptv-free-trial-australia | Keep: local intent vs generic intent, cross-linked |

## 5. Internal linking
* Indexable pages with 0 contextual inbound links: 0 (was 373 orphans on 10 Oct).
* Indexable pages with 2 or fewer: 76 (mostly the 40 city pages and 19 topic pages; each now has several links from hubs, siblings and pillar pages).
* Commercial pages: iptv-free-trial-australia 55 contextual links, best-iptv-australia 41, iptv-player-australia 100, iptv-box-australia 20, calculator 21.

## 6. Request indexing in Search Console (priority order, about 10 per day)
1. https://4kaustraliaiptv.com/
2. /iptv-free-trial-australia/
3. /best-iptv-australia/
4. /iptv-box-australia/
5. /iptv-player-australia/
6. /tools/iptv-bandwidth-calculator/
7. /devices/ then /guides/ then /sports/ then /cities/ then /comparisons/
8. The 3 new guides and the Firestick, Android TV and Apple TV device guides
9. /cities/sydney/ and /cities/melbourne/
Everything else follows through the sitemap: submit https://4kaustraliaiptv.com/sitemap.xml (158 URLs).

## 7. Do not request indexing for
Any noindex page (1,944 pages incl. 404.html), the legal pages (optional), /directory/, and old topic or small-city URLs.

## 8. Checks run (static site: no TypeScript, lint or build step exists)
| Check | Result |
|---|---|
| Canonicals (self, HTTPS, correct host, no noindex targets, no duplicates) | Pass, 0 problems (404.html has none on purpose) |
| robots.txt and meta robots | Pass; no accidental noindex on indexable pages; no server config files in the repo, so X-Robots-Tag cannot be set from here |
| Sitemap (158 URLs) | Pass; equals indexable pages; unique; HTTPS; every URL returns 200 on the local server |
| Redirect chains, www, HTTPS | Cannot be tested from files. Configure on the host: 301 www to non-www, force HTTPS |
| hreflang | Pass (self-referencing only, matches canonical) |
| JSON-LD | 0 invalid; FAQ counts match visible FAQs; breadcrumbs match page URLs |
| Titles / descriptions / H1 (indexable) | 0 duplicates, 0 out of range, 0 missing |
| Internal links | 0 broken across 2,102 pages |
| Headings | 23 indexable pages still skip a level (low) |
| Content | 2 indexable pages under 300 words (contact, tools hub) |
| Filler phrases | 6 pages, 1 occurrence each (low) |

## 9. What still depends on you
* Search Console (Domain property + sitemap) and GA4 ID.
* 301 from www and HTTPS at the host; upload this folder (the live site may still be an older version).
* Real reviews, real backlinks (see BACKLINK-PLAN.md), and confirmation of any remaining service claims (50,000+ channels, local CDN nodes, provider names).
* Write unique copy for the 5 biggest sports sub-pages, then remove noindex from them.

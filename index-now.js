// IndexNow submitter for https://4kaustraliaiptv.com (Bing, Yandex, Seznam, Naver via api.indexnow.org).
// Needs Node 18+ (built-in fetch), no npm packages.
//
// Usage:
//   node index-now.js                      -> reads the LIVE sitemap index and all child sitemaps, submits every URL
//   node index-now.js --local              -> reads the sitemap-*.xml files in this folder instead (use before uploading is finished)
//   node index-now.js https://4kaustraliaiptv.com/ https://4kaustraliaiptv.com/best-iptv-australia/   -> only these URLs
//
// The key file 817b9ca250bfeb6b52ffe4e750a08a61.txt (same name as the key, content = the key) must be
// uploaded to the site root so that https://4kaustraliaiptv.com/817b9ca250bfeb6b52ffe4e750a08a61.txt opens.

const fs = require('fs');
const path = require('path');

const HOST = '4kaustraliaiptv.com';
const SITE_URL = 'https://' + HOST;
const SITEMAP_URL = SITE_URL + '/sitemap.xml';
const INDEXNOW_KEY = '817b9ca250bfeb6b52ffe4e750a08a61';
const KEY_LOCATION = SITE_URL + '/' + INDEXNOW_KEY + '.txt';
const ENGINES = ['https://api.indexnow.org/indexnow', 'https://www.bing.com/indexnow', 'https://yandex.com/indexnow'];
const BATCH = 1000;
const UA = 'Mozilla/5.0 (compatible; IndexNowSubmitter/1.0; +' + SITE_URL + ')';

const locs = (xml) => [...xml.matchAll(/<loc>\s*([^<\s]+)\s*<\/loc>/g)].map((m) => m[1].trim());

async function getText(url) {
  const r = await fetch(url, { headers: { 'User-Agent': UA, Accept: 'application/xml, text/xml, */*' }, signal: AbortSignal.timeout(15000) });
  if (!r.ok) throw new Error(url + ' returned HTTP ' + r.status);
  return r.text();
}

async function urlsFromSitemaps(local) {
  const read = async (u) => {
    if (!local) return getText(u);
    return fs.readFileSync(path.join(__dirname, new URL(u).pathname.replace(/^\//, '')), 'utf8');
  };
  const root = await read(SITEMAP_URL);
  const out = new Set();
  if (/<sitemapindex/i.test(root)) {
    for (const child of locs(root)) {
      console.log('  reading ' + child);
      locs(await read(child)).forEach((u) => out.add(u));
    }
  } else {
    locs(root).forEach((u) => out.add(u));
  }
  return [...out].filter((u) => new URL(u).hostname === HOST);
}

async function submit(urls) {
  console.log('\nSubmitting ' + urls.length + ' URL(s) to ' + ENGINES.length + ' engines...');
  for (let i = 0; i < urls.length; i += BATCH) {
    const batch = urls.slice(i, i + BATCH);
    for (const engine of ENGINES) {
      try {
        const r = await fetch(engine, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json; charset=utf-8' },
          body: JSON.stringify({ host: HOST, key: INDEXNOW_KEY, keyLocation: KEY_LOCATION, urlList: batch }),
        });
        const note = { 200: 'OK', 202: 'accepted (key will be checked)', 400: 'bad request', 403: 'key not valid / key file not found', 422: 'URLs do not match host', 429: 'too many requests' }[r.status] || '';
        console.log((r.status === 200 || r.status === 202 ? 'OK   ' : 'WARN ') + engine + ' -> ' + r.status + ' ' + note);
      } catch (e) {
        console.log('ERR  ' + engine + ' -> ' + e.message);
      }
    }
  }
}

(async () => {
  try {
    const args = process.argv.slice(2);
    const local = args.includes('--local');
    const specific = args.filter((a) => a.startsWith('http'));
    let urls;
    if (specific.length) {
      urls = specific.filter((u) => new URL(u).hostname === HOST);
      console.log(urls.length + ' specific URL(s) given.');
    } else {
      console.log('Reading ' + (local ? 'local' : 'live') + ' sitemap: ' + SITEMAP_URL);
      urls = await urlsFromSitemaps(local);
      console.log('Found ' + urls.length + ' URLs.');
    }
    if (!urls.length) throw new Error('No URLs to submit.');
    if (!local) {
      try {
        const k = (await getText(KEY_LOCATION)).trim();
        if (k !== INDEXNOW_KEY) console.log('WARN key file is online but its content does not match the key.');
      } catch (e) {
        console.log('WARN key file not reachable at ' + KEY_LOCATION + ' (upload it first, otherwise engines return 403).');
      }
    }
    await submit(urls);
    console.log('\nDone. IndexNow only notifies Bing/Yandex/Seznam/Naver. Google still needs Search Console.');
  } catch (e) {
    console.error('Fatal: ' + e.message);
    process.exit(1);
  }
})();

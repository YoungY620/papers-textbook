// Internal-link audit for a built mdBook site.
//
// Render checks catch pages that fail to load; they do not catch a page whose
// links point somewhere that does not exist. mdBook resolves `[x](y.md)`
// relative to the chapter file, so moving a chapter between directories (or
// moving a page that chapters link to) silently breaks links. This walks the
// built output and resolves every local href/src against the files on disk.
//
//   node check-links.mjs <site-dir> [--base /papers-textbook]
import { readdirSync, statSync, readFileSync, existsSync } from 'node:fs';
import { join, relative, dirname, resolve, normalize } from 'node:path';

const siteDir = process.argv[2];
const baseIdx = process.argv.indexOf('--base');
const base = baseIdx > -1 ? process.argv[baseIdx + 1].replace(/\/$/, '') : '';
if (!siteDir) {
  console.error('usage: node check-links.mjs <site-dir> [--base <url-path>]');
  process.exit(2);
}

function walk(dir, out = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (name.endsWith('.html')) out.push(p);
  }
  return out;
}

const SKIP = /^(https?:|mailto:|data:|javascript:|#|\/\/)/;
const broken = [];
let checked = 0;

for (const file of walk(siteDir)) {
  const html = readFileSync(file, 'utf8');
  const rel = relative(siteDir, file);
  const re = /(?:href|src)="([^"]+)"/g;
  let m;
  while ((m = re.exec(html)) !== null) {
    let href = m[1];
    if (SKIP.test(href)) continue;
    // strip query/hash and mdBook's highlight parameter
    href = href.split('#')[0].split('?')[0];
    if (!href) continue;
    let target;
    if (href.startsWith('/')) {
      // absolute path: only meaningful if it lives under our base
      const stripped = base && href.startsWith(base) ? href.slice(base.length) : href;
      target = join(siteDir, stripped);
    } else {
      target = resolve(dirname(file), href);
    }
    checked += 1;
    if (!existsSync(target) && !existsSync(join(target, 'index.html'))) {
      broken.push({ page: rel, href: m[1] });
    }
  }
}

const byTarget = {};
for (const b of broken) {
  byTarget[b.href] = byTarget[b.href] || [];
  byTarget[b.href].push(b.page);
}

console.log(
  JSON.stringify(
    {
      pages: walk(siteDir).length,
      checked,
      broken: broken.length,
      targets: Object.entries(byTarget).map(([href, pages]) => ({
        href,
        count: pages.length,
        example: pages.slice(0, 3),
      })),
    },
    null,
    2,
  ),
);
process.exit(broken.length === 0 ? 0 : 1);

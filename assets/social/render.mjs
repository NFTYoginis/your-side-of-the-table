// Render docs/og-image.png from og-1200x630.html.
//
//   node assets/social/render.mjs
//
// Needs puppeteer available on the machine. The HTML is the source of truth — change wording
// there and re-render; never hand-edit the PNG.

import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
import puppeteer from 'puppeteer';

const here = dirname(fileURLToPath(import.meta.url));
const src = resolve(here, 'og-1200x630.html');
const out = resolve(here, '..', '..', 'docs', 'og-image.png');

const browser = await puppeteer.launch({ headless: 'new' });
const page = await browser.newPage();
await page.setViewport({ width: 1200, height: 630, deviceScaleFactor: 1 });
await page.goto('file://' + src, { waitUntil: 'load' });
await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 1200, height: 630 } });
await browser.close();

console.log('wrote', out);

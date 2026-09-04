// Measures text contrast off the RENDERED PIXELS, not off the CSS.
//
// A ground that is "flat colour with a photograph washed into it" has no single
// background colour, so a token-vs-token contrast check is meaningless: the
// answer changes across the section depending on what is in the picture behind
// each paragraph. This captures the section, samples every pixel inside each
// text element's box that is NOT part of a glyph, and reports the WORST patch.
//
// Usage: node shots/contrast.mjs <file> <sectionSelector> <textSelector>
import { spawn } from 'node:child_process';
import { rmSync, writeFileSync, readFileSync, unlinkSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url)), REPO = resolve(HERE, '..');
const CHROME = process.env.CHROME || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep = ms => new Promise(r => setTimeout(r, ms));

const [file, secSel, txtSel] = process.argv.slice(2);
const port = 9000 + Math.floor(Math.random() * 4000);
const profile = `${process.env.TEMP}/ps-k-${port}`;
const ch = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
  '--allow-file-access-from-files', `--user-data-dir=${profile}`,
  `--remote-debugging-port=${port}`, '--window-size=1440,940', 'about:blank'], { stdio: 'ignore' });

let list;
for (let i = 0; i < 45; i++) { try { list = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); break } catch { await sleep(200) } }
const ws = new WebSocket(list.find(t => t.type === 'page').webSocketDebuggerUrl);
let id = 0; const pend = new Map();
ws.addEventListener('message', e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m.result); pend.delete(m.id) } });
await new Promise(r => ws.addEventListener('open', r));
const send = (m, p = {}) => new Promise(res => { const n = ++id; pend.set(n, res); ws.send(JSON.stringify({ id: n, method: m, params: p })) });
await send('Page.enable'); await send('Runtime.enable');
await send('Page.navigate', { url: pathToFileURL(resolve(REPO, file)).href });
await sleep(3500);

// scroll the section to the top of the viewport, kill the reveal transforms
await send('Runtime.evaluate', {
  expression: `document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'));
    document.querySelector(${JSON.stringify(secSel)}).scrollIntoView({block:'start'});`
});
await sleep(1400);

const boxes = JSON.parse((await send('Runtime.evaluate', {
  returnByValue: true, expression:
    `JSON.stringify([...document.querySelectorAll(${JSON.stringify(txtSel)})].map(e=>{
      const r=e.getBoundingClientRect(), cs=getComputedStyle(e);
      return {t:e.textContent.trim().slice(0,34),color:cs.color,
        x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)};
    }).filter(b=>b.y>=0 && b.y+b.h<=940 && b.w>4 && b.h>4))`
})).result.value);

const shot = await send('Page.captureScreenshot', { format: 'png' });
const png = Buffer.from(shot.data, 'base64');
writeFileSync(resolve(HERE, '_k.png'), png);

// decode with the browser itself rather than pulling in a PNG library
const b64 = png.toString('base64');
const pixels = JSON.parse((await send('Runtime.evaluate', {
  awaitPromise: true, returnByValue: true, expression: `
  (async()=>{
    const img=new Image();
    img.src='data:image/png;base64,${b64}';
    await img.decode();
    const c=document.createElement('canvas');c.width=img.width;c.height=img.height;
    const g=c.getContext('2d');g.drawImage(img,0,0);
    const boxes=${JSON.stringify(boxes)};
    const out=boxes.map(b=>{
      const d=g.getImageData(b.x,b.y,b.w,b.h).data;
      const lum=[];
      for(let i=0;i<d.length;i+=4){
        const f=v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)};
        lum.push(0.2126*f(d[i])+0.7152*f(d[i+1])+0.0722*f(d[i+2]));
      }
      lum.sort((a,z)=>a-z);
      // glyphs are the DARK tail on a light ground. The background is the bulk,
      // so take a low percentile of the light half as the worst background patch.
      const bg = lum[Math.floor(lum.length*0.62)];
      return {...b, bgLum:bg};
    });
    return JSON.stringify(out);
  })()` })).result.value);

function lumOf(css) {
  const m = css.match(/[\d.]+/g).map(Number);
  const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4) };
  return 0.2126 * f(m[0]) + 0.7152 * f(m[1]) + 0.0722 * f(m[2]);
}

console.log(`${file}  ${secSel}`);
let worst = 99;
for (const b of pixels) {
  const tl = lumOf(b.color);
  const ratio = (Math.max(tl, b.bgLum) + 0.05) / (Math.min(tl, b.bgLum) + 0.05);
  worst = Math.min(worst, ratio);
  const flag = ratio >= 4.5 ? 'ok  ' : ratio >= 3 ? 'LOW ' : 'FAIL';
  console.log(`  ${flag} ${ratio.toFixed(2)}:1  ${b.color.padEnd(20)} "${b.t}"`);
}
console.log(`  worst ${worst.toFixed(2)}:1  ${worst >= 4.5 ? 'passes AA for body text' : 'UNDER AA'}`);

try { unlinkSync(resolve(HERE, '_k.png')) } catch {}
try { ws.close() } catch {}
ch.kill();
spawn('taskkill', ['/PID', String(ch.pid), '/T', '/F'], { stdio: 'ignore' });
await sleep(400);
try { rmSync(profile, { recursive: true, force: true, maxRetries: 5, retryDelay: 200 }) } catch {}
process.exit(worst >= 4.5 ? 0 : 1);

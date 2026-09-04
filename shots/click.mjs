// Real clicks on the pieces the wireframe pass added, because a filter that
// looks right in the source and does nothing in the browser is worse than no
// filter. Dispatches actual mouse events at real coordinates, then reads the
// resulting layout back off the rendered page.
//
//   direction 1  the job index filter, every tab
//   direction 1  the FAQ accordion, open and close
//   direction 3  the FAQ accordion in its two column form
import { spawn } from 'node:child_process';
import { rmSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url)), REPO = resolve(HERE, '..');
const CHROME = process.env.CHROME || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const port = 9000 + Math.floor(Math.random() * 4000);
const profile = `${process.env.TEMP}/ps-c-${port}`;
const ch = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
  '--allow-file-access-from-files', `--user-data-dir=${profile}`,
  `--remote-debugging-port=${port}`, '--window-size=1440,940', 'about:blank'], { stdio: 'ignore' });

let list;
for (let i = 0; i < 45; i++) { try { list = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); break } catch { await sleep(200) } }
const ws = new WebSocket(list.find(t => t.type === 'page').webSocketDebuggerUrl);
let id = 0; const pend = new Map();
ws.addEventListener('message', e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m.result ?? m); pend.delete(m.id) } });
await new Promise(r => ws.addEventListener('open', r));
const send = (m, p = {}) => new Promise(res => { const n = ++id; pend.set(n, res); ws.send(JSON.stringify({ id: n, method: m, params: p })) });
await send('Page.enable'); await send('Runtime.enable');

const evalq = async expr => JSON.parse((await send('Runtime.evaluate', { returnByValue: true, expression: expr })).result.value);

async function clickSel(sel, nth = 0) {
  await send('Runtime.evaluate', { expression: `document.querySelectorAll(${JSON.stringify(sel)})[${nth}].scrollIntoView({block:'center'})` });
  // The reveal transition moves elements 34px for 900ms after they enter, so a
  // rect measured too early points the click at where the target used to be.
  // This cost four false failures before the wait went up.
  await sleep(1300);
  const { x, y } = await evalq(`(()=>{const r=document.querySelectorAll(${JSON.stringify(sel)})[${nth}].getBoundingClientRect();
    return JSON.stringify({x:Math.round(r.x+r.width/2),y:Math.round(r.y+Math.min(r.height/2,20))})})()`);
  for (const type of ['mousePressed', 'mouseReleased'])
    await send('Input.dispatchMouseEvent', { type, x, y, button: 'left', clickCount: 1, buttons: 1 });
  await sleep(700);
}

const fails = [];
const check = (name, ok, got) => { console.log(`${ok ? '  ok  ' : '  FAIL'} ${name}${ok ? '' : `   got ${got}`}`); if (!ok) fails.push(name) };

// ── direction 1: the job index filter ─────────────────────────────────────
await send('Page.navigate', { url: pathToFileURL(resolve(REPO, 'direction-1-pressure.html')).href });
await sleep(3000);
console.log('direction 1, job index filter');

const shown = () => evalq(`(()=>{const t=[...document.querySelectorAll('#gal .tile')];
  return JSON.stringify({vis:t.filter(e=>e.offsetParent!==null).length,
    on:document.querySelector('.tab.on').dataset.cat,
    filt:document.getElementById('gal').classList.contains('filt'),
    spans:[...new Set(t.filter(e=>e.offsetParent!==null).map(e=>getComputedStyle(e).gridColumn))]})})()`);

let st = await shown();
check('starts on Everything, all 10 tiles, bento spans intact', st.vis === 10 && st.on === 'all' && !st.filt && st.spans.length > 1, JSON.stringify(st));

for (const [nth, cat, n] of [[1, 'interior', 2], [2, 'doors', 4], [3, 'exterior', 4]]) {
  await clickSel('.tab', nth);
  st = await shown();
  check(`${cat}: ${n} tiles, even spans`, st.vis === n && st.on === cat && st.filt && st.spans.length === 1, JSON.stringify(st));
}
await clickSel('.tab', 0);
st = await shown();
check('back to Everything restores the bento', st.vis === 10 && !st.filt && st.spans.length > 1, JSON.stringify(st));

// ── direction 1: the FAQ accordion ────────────────────────────────────────
console.log('direction 1, FAQ accordion');
const faq = () => evalq(`(()=>{const q=[...document.querySelectorAll('.q')];
  return JSON.stringify({open:q.filter(e=>e.open).length,
    h:q.map(e=>Math.round(e.getBoundingClientRect().height))})})()`);
let f0 = await faq();
await clickSel('.q summary', 2);
let f1 = await faq();
check('a closed question opens and grows', f1.open === f0.open + 1 && f1.h[2] > f0.h[2], `${JSON.stringify(f0)} -> ${JSON.stringify(f1)}`);
await clickSel('.q summary', 2);
let f2 = await faq();
check('and closes again', f2.open === f0.open && f2.h[2] === f0.h[2], JSON.stringify(f2));

// ── direction 3: the two column FAQ ───────────────────────────────────────
await send('Page.navigate', { url: pathToFileURL(resolve(REPO, 'direction-3-spec-sheet.html')).href });
await sleep(3000);
console.log('direction 3, two column FAQ');
const cols = await evalq(`(()=>{const c=[...document.querySelectorAll('.faq-cols>div')];
  return JSON.stringify(c.map(d=>Math.round(d.getBoundingClientRect().x)))})()`);
check('questions really are in two columns', cols.length === 2 && cols[1] - cols[0] > 300, JSON.stringify(cols));
f0 = await faq();
await clickSel('.q summary', 5);
f1 = await faq();
check('a question in the right column opens', f1.open === f0.open + 1 && f1.h[5] > f0.h[5], `${JSON.stringify(f0)} -> ${JSON.stringify(f1)}`);

console.log(fails.length ? `\n${fails.length} FAILED` : '\nall interaction checks pass');
try { ws.close() } catch {}
ch.kill();
spawn('taskkill', ['/PID', String(ch.pid), '/T', '/F'], { stdio: 'ignore' });
await sleep(400);
try { rmSync(profile, { recursive: true, force: true, maxRetries: 5, retryDelay: 200 }) } catch {}
process.exit(fails.length ? 1 : 0);

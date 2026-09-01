// Focused check: do the Instagram bays end up filled (embed) or filled
// (poster fallback)? Either is acceptable — an EMPTY bay is not.
import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const HERE=dirname(fileURLToPath(import.meta.url)), REPO=resolve(HERE,'..');
const CHROME=process.env.CHROME||'C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const file=process.argv[2], out=process.argv[3];
const port=9000+Math.floor(Math.random()*4000);
const ch=spawn(CHROME,['--headless=new','--disable-gpu','--hide-scrollbars','--mute-audio',
  '--allow-file-access-from-files',`--user-data-dir=${process.env.TEMP}/ps-r-${port}`,
  `--remote-debugging-port=${port}`,'--window-size=1440,940','about:blank'],{stdio:'ignore'});
let list;
for(let i=0;i<45;i++){try{list=await(await fetch(`http://127.0.0.1:${port}/json/list`)).json();break}catch{await sleep(200)}}
const ws=new WebSocket(list.find(t=>t.type==='page').webSocketDebuggerUrl);
let id=0;const pend=new Map();
ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id&&pend.has(m.id)){pend.get(m.id)(m.result??m);pend.delete(m.id)}});
await new Promise(r=>ws.addEventListener('open',r));
const send=(m,p={})=>new Promise(res=>{const n=++id;pend.set(n,res);ws.send(JSON.stringify({id:n,method:m,params:p}))});
await send('Page.enable');await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride',{width:1440,height:940,deviceScaleFactor:1,mobile:false});
await send('Page.navigate',{url:pathToFileURL(resolve(REPO,file)).href});
await sleep(3000);
// scroll the reel section into view so the IntersectionObserver fires
await send('Runtime.evaluate',{expression:`document.getElementById('reels').scrollIntoView()`});
await sleep(14000);
const r=await send('Runtime.evaluate',{returnByValue:true,expression:`JSON.stringify(
  [...document.querySelectorAll('.screen[data-reel]')].map(s=>{
    const f=s.querySelector('iframe'), fb=s.querySelector('.fallback');
    return {live:s.classList.contains('live'), iframeH:f?Math.round(f.getBoundingClientRect().height):null,
            fallbackVisible: fb?getComputedStyle(fb).display!=='none':false,
            screenH:Math.round(s.getBoundingClientRect().height)};
  }))`});
console.log(file); console.log(r.result.value);
await send('Runtime.evaluate',{expression:`document.getElementById('reels').scrollIntoView()`});
await sleep(900);
const shot=await send('Page.captureScreenshot',{format:'png'});
writeFileSync(resolve(HERE,out),Buffer.from(shot.data,'base64'));
ws.close();ch.kill();spawn('taskkill',['/PID',String(ch.pid),'/T','/F'],{stdio:'ignore'});
process.exit(0);

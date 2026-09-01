import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
const HERE=dirname(fileURLToPath(import.meta.url));
const CHROME=process.env.CHROME||'C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const url=process.argv[2], out=process.argv[3];
const port=9000+Math.floor(Math.random()*4000);
const ch=spawn(CHROME,['--headless=new','--disable-gpu','--hide-scrollbars','--mute-audio',
  `--user-data-dir=${process.env.TEMP}/ps-live-${port}`,`--remote-debugging-port=${port}`,
  '--window-size=1440,940','about:blank'],{stdio:'ignore'});
let list;
for(let i=0;i<45;i++){try{list=await(await fetch(`http://127.0.0.1:${port}/json/list`)).json();break}catch{await sleep(200)}}
const ws=new WebSocket(list.find(t=>t.type==='page').webSocketDebuggerUrl);
let id=0;const pend=new Map();
ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id&&pend.has(m.id)){pend.get(m.id)(m.result??m);pend.delete(m.id)}});
await new Promise(r=>ws.addEventListener('open',r));
const send=(m,p={})=>new Promise(res=>{const n=++id;pend.set(n,res);ws.send(JSON.stringify({id:n,method:m,params:p}))});
await send('Page.enable');await send('Runtime.enable');
await send('Page.navigate',{url});
await sleep(6500);
const r=await send('Runtime.evaluate',{returnByValue:true,expression:`(()=>{
  const imgs=[...document.images];
  return JSON.stringify({title:document.title,h1:(document.querySelector('h1')||{}).innerText||'',
    imgs:imgs.length, broken:imgs.filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.getAttribute('src')),
    scrollW:document.documentElement.scrollWidth, clientW:document.documentElement.clientWidth,
    h1font:getComputedStyle(document.querySelector('h1')).fontFamily.split(',')[0],
    iframes:document.querySelectorAll('iframe').length})})()`});
console.log(url.replace('https://lumen-marketing.github.io/pane-solutions-designs/','› '), r.result.value);
const shot=await send('Page.captureScreenshot',{format:'png'});
writeFileSync(resolve(HERE,out),Buffer.from(shot.data,'base64'));
ws.close();ch.kill();spawn('taskkill',['/PID',String(ch.pid),'/T','/F'],{stdio:'ignore'});
process.exit(0);

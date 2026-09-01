import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const HERE=dirname(fileURLToPath(import.meta.url)), REPO=resolve(HERE,'..');
const CHROME=process.env.CHROME||'C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const port=9000+Math.floor(Math.random()*4000);
const ch=spawn(CHROME,['--headless=new','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files',
 `--user-data-dir=${process.env.TEMP}/ps-h-${port}`,`--remote-debugging-port=${port}`,
 '--window-size=1440,940','about:blank'],{stdio:'ignore'});
let list;for(let i=0;i<45;i++){try{list=await(await fetch(`http://127.0.0.1:${port}/json/list`)).json();break}catch{await sleep(200)}}
const ws=new WebSocket(list.find(t=>t.type==='page').webSocketDebuggerUrl);
let id=0;const pend=new Map();
ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id&&pend.has(m.id)){pend.get(m.id)(m.result??m);pend.delete(m.id)}});
await new Promise(r=>ws.addEventListener('open',r));
const send=(m,p={})=>new Promise(res=>{const n=++id;pend.set(n,res);ws.send(JSON.stringify({id:n,method:m,params:p}))});
await send('Page.enable');await send('Runtime.enable');await send('Input.setIgnoreInputEvents',{ignore:false});
const TOUCH=process.env.TOUCH==='1';
await send('Emulation.setDeviceMetricsOverride',{width:TOUCH?390:1440,height:940,deviceScaleFactor:1,mobile:TOUCH});
if(TOUCH){await send('Emulation.setTouchEmulationEnabled',{enabled:true,maxTouchPoints:5});
  await send('Emulation.setEmulatedMedia',{features:[{name:'hover',value:'none'},{name:'pointer',value:'coarse'}]});}
await send('Page.navigate',{url:pathToFileURL(resolve(REPO,'direction-3-spec-sheet.html')).href});
await sleep(3200);
// bring the sash into view, then hover pane 3
await send('Runtime.evaluate',{expression:`document.querySelector('.sash').scrollIntoView({block:'center'})`});
await sleep(900);
if(!TOUCH){
  const box=await send('Runtime.evaluate',{returnByValue:true,expression:
   `(()=>{const r=document.querySelectorAll('.lite')[2].getBoundingClientRect();
     return JSON.stringify({x:Math.round(r.x+r.width/2),y:Math.round(r.y+r.height/2)})})()`});
  const {x,y}=JSON.parse(box.result.value);
  await send('Input.dispatchMouseEvent',{type:'mouseMoved',x,y,buttons:0});
}
await sleep(1100);
const st=await send('Runtime.evaluate',{returnByValue:true,expression:
 `JSON.stringify([...document.querySelectorAll('.lite')].map((l,i)=>({
    i:i+1, filter:getComputedStyle(l.querySelector('img')).filter.slice(0,34),
    grime:+getComputedStyle(l,'::before').opacity,
    cap:getComputedStyle(l.querySelector('figcaption')).translate})))`});
console.log(st.result.value);
const shot=await send('Page.captureScreenshot',{format:'png'});
writeFileSync(resolve(HERE,TOUCH?'touch.png':'hover.png'),Buffer.from(shot.data,'base64'));
ws.close();ch.kill();spawn('taskkill',['/PID',String(ch.pid),'/T','/F'],{stdio:'ignore'});
process.exit(0);

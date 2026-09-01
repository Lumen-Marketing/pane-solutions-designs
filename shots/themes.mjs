import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const HERE=dirname(fileURLToPath(import.meta.url)), REPO=resolve(HERE,'..');
const CHROME=process.env.CHROME||'C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
// contrast helper runs IN the page so it reads real computed colours
const CHECK=`(()=>{
  function lum(c){const m=(String(c).match(/[\d.]+/g)||[]).map(Number);
    if(m.length<3)return null;
    const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};
    return .2126*f(m[0])+.7152*f(m[1])+.0722*f(m[2])}
  function ratio(a,b){const l1=lum(a),l2=lum(b);if(l1===null||l2===null)return null;
    return ((Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05)).toFixed(2)}
  function bgOf(el){let e=el;while(e){const b=getComputedStyle(e).backgroundColor;
    if(b&&b!=='rgba(0, 0, 0, 0)')return b;e=e.parentElement}return 'rgb(255,255,255)'}
  const sel=['h1','.h-sub','.dim span','.h-spec .v.cy','.h-spec .k','.seal .sm','.lbl','.btn s',
             '.btn-line','.shead h2','.note blockquote','.tk q','.irow .ti','.tb-num a','.hd .ti'];
  const out=[];
  sel.forEach(s=>{const el=document.querySelector(s);if(!el)return;
    const cs=getComputedStyle(el);
    const rr=ratio(cs.color,bgOf(el)); if(rr===null)return;
    out.push({sel:s,r:+rr,size:Math.round(parseFloat(cs.fontSize)),c:cs.color,b:bgOf(el)});});
  return JSON.stringify({theme:document.documentElement.getAttribute('data-theme')||'drafting',
    paper:getComputedStyle(document.body).backgroundColor, out});})()`;
const port=9000+Math.floor(Math.random()*4000);
const ch=spawn(CHROME,['--headless=new','--disable-gpu','--hide-scrollbars',
  '--allow-file-access-from-files',`--user-data-dir=${process.env.TEMP}/ps-th-${port}`,
  `--remote-debugging-port=${port}`,'--window-size=1440,940','about:blank'],{stdio:'ignore'});
let list;for(let i=0;i<45;i++){try{list=await(await fetch(`http://127.0.0.1:${port}/json/list`)).json();break}catch{await sleep(200)}}
const ws=new WebSocket(list.find(t=>t.type==='page').webSocketDebuggerUrl);
let id=0;const pend=new Map();
ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id&&pend.has(m.id)){pend.get(m.id)(m.result??m);pend.delete(m.id)}});
await new Promise(r=>ws.addEventListener('open',r));
const send=(m,p={})=>new Promise(res=>{const n=++id;pend.set(n,res);ws.send(JSON.stringify({id:n,method:m,params:p}))});
await send('Page.enable');await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride',{width:1440,height:940,deviceScaleFactor:1,mobile:false});
const base=pathToFileURL(resolve(REPO,'direction-3-spec-sheet.html')).href;
for(const t of ['drafting','blueprint','vellum']){
  await send('Page.navigate',{url:base+'?theme='+t});
  await sleep(3200);
  const r=await send('Runtime.evaluate',{expression:CHECK,returnByValue:true});
  if(!r.result||r.result.value===undefined){console.log('EVAL ERR',JSON.stringify(r).slice(0,700));process.exit(1)}
  const d=JSON.parse(r.result.value);
  const bad=d.out.filter(o=>o.r < (o.size>=24?3:4.5));
  console.log(`${t.padEnd(10)} paper=${d.paper}  ${bad.length?'FAIL '+bad.map(b=>b.sel+':'+b.r+'@'+b.size+'px').join(' | '):'all text passes contrast'}`);
  const s1=await send('Page.captureScreenshot',{format:'png'});
  writeFileSync(resolve(HERE,`t-${t}.png`),Buffer.from(s1.data,'base64'));
}
ws.close();ch.kill();spawn('taskkill',['/PID',String(ch.pid),'/T','/F'],{stdio:'ignore'});
process.exit(0);

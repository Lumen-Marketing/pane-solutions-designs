import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
const CHROME='C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const port=9000+Math.floor(Math.random()*4000);
const ch=spawn(CHROME,['--headless=new','--disable-gpu',`--user-data-dir=${process.env.TEMP}/cdp-${port}`,`--remote-debugging-port=${port}`,'--window-size=1280,1600','about:blank'],{stdio:'ignore'});
await sleep(2500);
const list=await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const ws=new WebSocket(list.find(x=>x.type==='page').webSocketDebuggerUrl);
let id=0;const pend=new Map();
ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id&&pend.has(m.id)){pend.get(m.id)(m.result);pend.delete(m.id);}});
await new Promise(r=>ws.addEventListener('open',r));
const send=(m,p={})=>new Promise(res=>{const n=++id;pend.set(n,res);ws.send(JSON.stringify({id:n,method:m,params:p}));});
await send('Page.enable');await send('Runtime.enable');
await send('Page.navigate',{url:'https://www.instagram.com/pane_solutions_llc/'});
await sleep(8000);
const r=await send('Runtime.evaluate',{expression:`JSON.stringify([...document.querySelectorAll('img')].map(i=>({s:i.currentSrc||i.src,w:i.naturalWidth,h:i.naturalHeight,alt:i.alt||''})))`,returnByValue:true});
const imgs=JSON.parse(r.result.value);
writeFileSync('grid.json',JSON.stringify(imgs,null,1));
const UA={'User-Agent':'Mozilla/5.0 Chrome/128.0','Referer':'https://www.instagram.com/'};
let n=0;
for(const im of imgs){
  const isProfile=/profile picture/i.test(im.alt);
  const isVideo=/^Video by/i.test(im.alt);
  if(!isProfile&&!isVideo) continue;
  // bump requested size in the signed url (stp param only affects rendition, signature still valid)
  const bigger=im.s.replace(/s150x150/,'s640x640');
  const tryUrls=[bigger,im.s];
  for(const u of tryUrls){
    const res=await fetch(u,{headers:UA});
    if(res.ok){const b=Buffer.from(await res.arrayBuffer());
      const name=isProfile?`LOGO-${im.w}.jpg`:`POSTER-${++n}-${im.w}x${im.h}.jpg`;
      writeFileSync(`raw/${name}`,b);console.log('ok',name,Math.round(b.length/1024)+'KB',u===bigger?'(upsized)':'(orig)');break;}
    else console.log('  '+res.status,u.slice(0,80));
  }
}
ws.close();ch.kill();process.exit(0);

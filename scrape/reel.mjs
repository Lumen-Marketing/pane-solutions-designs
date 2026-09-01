import { spawn } from 'node:child_process';
const CHROME='C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const url=process.argv[2];
const port=9000+Math.floor(Math.random()*4000);
const ch=spawn(CHROME,['--headless=new','--disable-gpu','--mute-audio',`--user-data-dir=${process.env.TEMP}/cdp-${port}`,`--remote-debugging-port=${port}`,'--window-size=500,900','about:blank'],{stdio:'ignore'});
await sleep(2500);
const list=await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const t=list.find(x=>x.type==='page');
const ws=new WebSocket(t.webSocketDebuggerUrl);
let id=0; const pend=new Map(); const hits=new Set();
ws.addEventListener('message',e=>{const m=JSON.parse(e.data);
  if(m.id&&pend.has(m.id)){pend.get(m.id)(m.result);pend.delete(m.id);}
  if(m.method==='Network.responseReceived'){const u=m.params.response.url; const mt=m.params.response.mimeType||'';
    if(/\.mp4|video\/|dash|\.m4v/.test(u+mt)) hits.add(mt+' :: '+u.slice(0,220));}
});
await new Promise(r=>ws.addEventListener('open',r));
const send=(method,params={})=>new Promise(res=>{const n=++id;pend.set(n,res);ws.send(JSON.stringify({id:n,method,params}));});
await send('Network.enable'); await send('Page.enable'); await send('Runtime.enable');
await send('Page.navigate',{url});
await sleep(9000);
const r=await send('Runtime.evaluate',{expression:`(()=>{const v=[...document.querySelectorAll('video')].map(v=>({src:v.currentSrc||v.src,poster:v.poster,ready:v.readyState}));
const og=[...document.querySelectorAll('meta')].map(m=>[m.getAttribute('property')||m.getAttribute('name'),m.content]).filter(x=>/video|image|description/i.test(x[0]||''));
return JSON.stringify({vids:v,og,text:document.body.innerText.slice(0,300)},null,1)})()`,returnByValue:true});
console.log('EVAL:', JSON.stringify(r).slice(0,2500));
console.log('\nNETWORK VIDEO HITS:'); [...hits].forEach(h=>console.log(' ',h));
ws.close(); ch.kill();
process.exit(0);

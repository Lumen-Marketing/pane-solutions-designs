import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
const CHROME='C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const CODES=['DGa2BgUpDQV','DGa18qGJxtX','DGa1zQ3JEVn','DGa1iIRpKyX','DGa1d1IJrZt','DGa1Q48pj9f','DGa1Ke4J0cY','DC4osCWRL3L','DC4otsoxbOD','DC4oAoixUgB','DC4nlEkxyKP','DC4nfRFRrEx'];
const port=9000+Math.floor(Math.random()*4000);
const ch=spawn(CHROME,['--headless=new','--disable-gpu','--mute-audio',`--user-data-dir=${process.env.TEMP}/cdp-${port}`,`--remote-debugging-port=${port}`,'--window-size=1400,1000','about:blank'],{stdio:'ignore'});
await sleep(2500);
const list=await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const ws=new WebSocket(list.find(x=>x.type==='page').webSocketDebuggerUrl);
let id=0;const pend=new Map();
ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id&&pend.has(m.id)){pend.get(m.id)(m.result);pend.delete(m.id);}});
await new Promise(r=>ws.addEventListener('open',r));
const send=(m,p={})=>new Promise(res=>{const n=++id;pend.set(n,res);ws.send(JSON.stringify({id:n,method:m,params:p}));});
await send('Page.enable');await send('Runtime.enable');
const all=[];
for(const c of CODES){
  await send('Page.navigate',{url:`https://www.instagram.com/p/${c}/`});
  await sleep(6000);
  const r=await send('Runtime.evaluate',{expression:`(()=>{
    const imgs=[...document.querySelectorAll('img')].filter(i=>/t51\.(75761|82787|2885)-15/.test(i.src)).map(i=>({src:i.currentSrc||i.src,w:i.naturalWidth,h:i.naturalHeight,alt:(i.alt||'').slice(0,120)}));
    const cap=(document.querySelector('meta[property="og:description"]')||{}).content||'';
    const isVid=/Video by|CLIPS/.test(JSON.stringify(imgs))||!!document.querySelector('svg[aria-label="Clip"]');
    return JSON.stringify({imgs,cap,isVid});})()`,returnByValue:true});
  let d={imgs:[],cap:''};try{d=JSON.parse(r.result.value);}catch(e){}
  console.log(c,'->',d.imgs.length,'imgs |',d.imgs.map(i=>i.w+'x'+i.h).join(','),'|',d.cap.slice(0,90));
  all.push({code:c,...d});
}
writeFileSync('posts.json',JSON.stringify(all,null,1));
ws.close();ch.kill();process.exit(0);

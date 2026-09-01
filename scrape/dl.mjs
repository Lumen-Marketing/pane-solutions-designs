import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
const posts=JSON.parse(readFileSync('posts.json','utf8'));
mkdirSync('raw',{recursive:true});
const seen=new Set();let n=0;const man=[];
for(const p of posts){
  const big=p.imgs.filter(i=>i.w>=1000);
  const use=big.length?big:p.imgs.filter(i=>i.w>=360&&i.h>=360).slice(0,1);
  for(const im of use){
    const key=(im.src.match(/\/([0-9]+_[0-9]+_[0-9]+_n\.jpg)/)||[])[1]||im.src.slice(-40);
    if(seen.has(key))continue;seen.add(key);
    const name=`${p.code}-${String(++n).padStart(2,'0')}-${im.w}x${im.h}.jpg`;
    const r=await fetch(im.src,{headers:{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0 Safari/537.36','Referer':'https://www.instagram.com/'}});
    if(!r.ok){console.log('FAIL',name,r.status);continue;}
    const b=Buffer.from(await r.arrayBuffer());
    writeFileSync(`raw/${name}`,b);
    man.push({file:name,code:p.code,w:im.w,h:im.h,kb:Math.round(b.length/1024)});
    console.log('ok',name,Math.round(b.length/1024)+'KB');
  }
}
writeFileSync('manifest.json',JSON.stringify(man,null,1));

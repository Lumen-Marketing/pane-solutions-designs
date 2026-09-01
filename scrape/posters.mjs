import {readFileSync,writeFileSync} from 'node:fs';
const posts=JSON.parse(readFileSync('posts.json','utf8'));
const reels=['DC4osCWRL3L','DC4oAoixUgB','DC4nlEkxyKP'];
for(const c of reels){
  const p=posts.find(x=>x.code===c);
  const im=p.imgs.filter(i=>i.w>=360).sort((a,b)=>b.w*b.h-a.w*a.h)[0];
  if(!im){console.log('none for',c);continue;}
  const r=await fetch(im.src,{headers:{'User-Agent':'Mozilla/5.0 Chrome/128.0','Referer':'https://www.instagram.com/'}});
  const b=Buffer.from(await r.arrayBuffer());
  writeFileSync(`raw/REEL-${c}-${im.w}x${im.h}.jpg`,b);
  console.log('poster',c,im.w+'x'+im.h,Math.round(b.length/1024)+'KB');
}

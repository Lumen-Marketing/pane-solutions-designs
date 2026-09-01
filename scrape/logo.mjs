import {writeFileSync} from 'node:fs';
const UA={'User-Agent':'Mozilla/5.0 Chrome/128.0','Referer':'https://www.instagram.com/'};
// profile pic: try progressively larger stp sizes
const base='https://scontent.cdninstagram.com/v/t51.2885-19/450667918_502359632297235_9207766297908880579_n.jpg';
for(const sz of ['s320x320','s640x640','s1080x1080','']){
  const u=sz?`${base}?stp=dst-jpg_${sz}&_nc_cat=100&ccb=7-5&_nc_sid=f7ccc5`:base;
  try{const r=await fetch(u,{headers:UA});
    if(r.ok){const b=Buffer.from(await r.arrayBuffer());writeFileSync(`raw/LOGO-${sz||'orig'}.jpg`,b);console.log('ok',sz||'orig',Math.round(b.length/1024)+'KB');}
    else console.log('fail',sz,r.status);}catch(e){console.log('err',sz,e.message);}
}
// correct reel posters seen on the grid
const posters={
 'DC4osCWRL3L':'https://scontent.cdninstagram.com/v/t51.75761-15/468303123_17869578843248778_707099630116274359_n.jpg?stp=dst-jpg_e35_s1080x1080_tt6&_nc_cat=109&ccb=7-5&_nc_sid=18de74',
 'DC4oAoixUgB':'https://scontent.cdninstagram.com/v/t51.75761-15/468500640_17869578192248778_5799357803848875314_n.jpg?stp=dst-jpg_e35_s1080x1080_tt6&_nc_cat=106&ccb=7-5&_nc_sid=18de74',
 'DC4nlEkxyKP':'https://scontent.cdninstagram.com/v/t51.75761-15/468499431_17869577745248778_2546947549789863495_n.jpg?stp=dst-jpg_e35_s1080x1080_tt6&_nc_cat=104&ccb=7-5&_nc_sid=18de74'};
for(const [c,u] of Object.entries(posters)){
  const r=await fetch(u,{headers:UA});
  if(!r.ok){console.log('poster fail',c,r.status);continue;}
  const b=Buffer.from(await r.arrayBuffer());writeFileSync(`raw/POSTER-${c}.jpg`,b);console.log('poster',c,Math.round(b.length/1024)+'KB');
}

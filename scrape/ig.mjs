import { withPage } from 'file:///C:/Users/tagal/quest-construction-designs/shots/cdp.mjs';

const target = process.argv[2] || 'https://www.instagram.com/pane_solutions_llc/';
await withPage(target, { width: 1280, height: 1600, wait: 7000, scroll: true }, async ({ evaluate }) => {
  const out = await evaluate(`(() => {
    const imgs = [...document.querySelectorAll('img')].map(i => ({s:i.currentSrc||i.src, w:i.naturalWidth, h:i.naturalHeight, alt:(i.alt||'').slice(0,140)}));
    const vids = [...document.querySelectorAll('video')].map(v => ({s:v.currentSrc||v.src, poster:v.poster}));
    const og = [...document.querySelectorAll('meta')].filter(m=>/og:|video/.test(m.getAttribute('property')||m.getAttribute('name')||'')).map(m=>({p:m.getAttribute('property')||m.getAttribute('name'), c:(m.content||'').slice(0,300)}));
    return JSON.stringify({title:document.title, bodyLen:document.body.innerText.length, snippet:document.body.innerText.slice(0,400), imgs, vids, og}, null, 1);
  })()`);
  console.log(out);
});

'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const root=path.resolve(__dirname,'..');
const home=fs.readFileSync(path.join(root,'index.html'),'utf8');
const card=fs.readFileSync(path.join(root,'carte/index.html'),'utf8');
const langs=['fr','en','es','pt','it','de','nl','ar'];
const expected='https://digiylyfe.com/acces-proprietaire.html';
function ownerLink(page){
 const m=page.match(/<a\s+[^>]*href="([^"]+)"[^>]*aria-label="Accès propriétaire BCHEIKH"[^>]*>/);
 assert.ok(m,'visible owner link must be a real anchor');
 const url=new URL(m[1].replaceAll('&amp;','&'));
 assert.equal(url.origin+url.pathname,expected);
 assert.equal(url.searchParams.get('fiche'),'bcheikh');
 assert.ok(['https://bcheikh.digiylyfe.com/','https://bcheikh.digiylyfe.com/carte/'].includes(url.searchParams.get('return')));
 assert.equal(url.searchParams.size,2,'only fiche and return; no tokens');
 return url;
}
test('BCHEIKH homepage: owner button and correct secure gateway',()=>{
 const url=ownerLink(home);
 assert.match(home,/<a class="owner-access-cta" data-i18n="ownerAccess"/);
 assert.match(home,/.owner-access-cta:focus-visible/);
 assert.equal(url.searchParams.get('return'),'https://bcheikh.digiylyfe.com/');
});
test('BCHEIKH living card: same gateway and return to card',()=>{
 const url=ownerLink(card);
 assert.match(card,/class="action wide owner-entry"/);
 assert.equal(url.searchParams.get('return'),'https://bcheikh.digiylyfe.com/carte/');
});
test('Eight-language owner labels remain available on both pages',()=>{
 const start=home.indexOf('const translations=');
 const end=home.indexOf('\n',start);
 assert.ok(start>=0);
 const json=home.slice(start+'const translations='.length,end).replace(/;\s*$/,'');
 const t=JSON.parse(json);
 for(const lang of langs){
  assert.ok(t[lang].ownerAccess?.length>5,'home '+lang);
  const rx=new RegExp(lang+':\\{back:\\'BCHEIKH\\',ownerAccess:\\'');
  assert.match(card,rx,'card '+lang);
 }
});
test('scripts parse; visitor links and PWA unchanged',()=>{
 const homeJs=home.match(/const translations=([^\n]+)/)?.[1];
 assert.ok(homeJs && homeJs.includes('ownerAccess'));
 const scripts=home.match(/<script\b[^>]*>([\s\S]*?)<\/script>/g)||[];
 for(const chunk of scripts){
  const code=chunk.replace(/^<script\b[^>]*>/,'').replace(/<\/script>$/,'');
  if(code.trim())new vm.Script(code);
 }
 const cardScripts=card.match(/<script\b[^>]*>([\s\S]*?)<\/script>/g)||[];
 for(const chunk of cardScripts){
  const code=chunk.replace(/^<script\b[^>]*>/,'').replace(/<\/script>$/,'');
  if(code.trim())new vm.Script(code);
 }
 assert.match(home,/https:\/\/wa\.me\/221786523129/);
 assert.match(home,/digiy-member-pwa-config/);
 assert.doesNotMatch(home+card,/service_role|sb_secret_|\bJWT\b|access_token=/i);
});

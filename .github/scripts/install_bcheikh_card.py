from pathlib import Path

p = Path('index.html')
h = p.read_text(encoding='utf-8')

old_grid = '''.business-card{
      display:grid;
      grid-template-columns:.92fr 1.08fr;
      gap:24px;'''
new_grid = '''.business-card{
      display:grid;
      grid-template-columns:1.12fr .88fr;
      gap:28px;'''
if old_grid not in h:
    raise SystemExit('Business-card grid not found')
h = h.replace(old_grid, new_grid, 1)

old_img = '.business-card img{width:min(100%,360px);margin:auto;border-radius:26px;border:1px solid var(--line);background:#0a0a0a}'
new_img = '.card-visual{display:flex;justify-content:center;align-items:center}.business-card img{width:min(100%,560px);margin:auto;border-radius:26px;border:1px solid var(--line);background:#0a0a0a;box-shadow:0 22px 64px rgba(0,0,0,.42)}'
if old_img not in h:
    raise SystemExit('Business-card image CSS not found')
h = h.replace(old_img, new_img, 1)

old_mobile = '''.hero,.business-card{grid-template-columns:1fr}
      .hero{padding-top:38px}'''
new_mobile = '''.hero,.business-card{grid-template-columns:1fr}
      .business-card img{width:min(100%,520px)}
      .hero{padding-top:38px}'''
if old_mobile not in h:
    raise SystemExit('Mobile business-card CSS not found')
h = h.replace(old_mobile, new_mobile, 1)

old_actions = '''<a class="btn btn-primary" data-i18n="openCard" href="carte-visite.webp" rel="noopener" target="_blank">Ouvrir la carte</a>
<a class="btn btn-secondary" data-i18n="download" download="" href="carte-visite.webp">Télécharger</a>'''
new_actions = '''<a class="btn btn-primary" data-i18n="openCard" href="carte-visite.webp" rel="noopener" target="_blank">Ouvrir la carte</a>
<button class="btn btn-secondary" id="shareCardButton" type="button">Partager la carte</button>
<a class="btn btn-secondary" data-i18n="download" download="BCHEIKH-carte-visite.webp" href="carte-visite.webp">Télécharger</a>'''
if old_actions not in h:
    raise SystemExit('Card action block not found')
h = h.replace(old_actions, new_actions, 1)

marker = '    shareShopButton.addEventListener("click",async()=>{'
share_js = r'''
    const shareCardButton=document.getElementById("shareCardButton");
    const cardShareLabels={fr:"Partager la carte",en:"Share the card",es:"Compartir la tarjeta",pt:"Partilhar o cartão",it:"Condividi la scheda",de:"Visitenkarte teilen",nl:"Deel het kaartje",ar:"مشاركة البطاقة"};
    const cardShareStatus={fr:"Carte prête à être partagée.",en:"Card ready to share.",es:"Tarjeta lista para compartir.",pt:"Cartão pronto para partilhar.",it:"Scheda pronta da condividere.",de:"Visitenkarte bereit zum Teilen.",nl:"Kaart klaar om te delen.",ar:"البطاقة جاهزة للمشاركة."};
    function currentCardLang(){
      const v=(document.getElementById("languageSelect")?.value||document.documentElement.lang||"fr").slice(0,2).toLowerCase();
      return cardShareLabels[v]?v:"fr";
    }
    function syncShareCardLabel(){
      if(shareCardButton) shareCardButton.textContent=cardShareLabels[currentCardLang()];
    }
    syncShareCardLabel();
    document.getElementById("languageSelect")?.addEventListener("change",()=>setTimeout(syncShareCardLabel,0));
    shareCardButton?.addEventListener("click",async()=>{
      const lang=currentCardLang();
      const cardUrl=new URL("carte-visite.webp",location.href).href;
      try{
        const response=await fetch(cardUrl,{cache:"no-store"});
        if(!response.ok) throw new Error("card-fetch");
        const blob=await response.blob();
        const file=new File([blob],"BCHEIKH-carte-visite.webp",{type:blob.type||"image/webp"});
        if(navigator.share && navigator.canShare && navigator.canShare({files:[file]})){
          await navigator.share({files:[file],title:"BCHEIKH",text:translations[lang]?.shareText||translations.fr.shareText});
        }else if(navigator.share){
          await navigator.share({title:"BCHEIKH",text:translations[lang]?.shareText||translations.fr.shareText,url:cardUrl});
        }else{
          await copyText(cardUrl,cardShareStatus[lang]);
          return;
        }
        setShareStatus(cardShareStatus[lang]);
      }catch(error){
        if(error && error.name==="AbortError") return;
        copyText(cardUrl,cardShareStatus[lang]);
      }
    });

'''
if marker not in h:
    raise SystemExit('Share shop marker not found')
h = h.replace(marker, share_js + marker, 1)

p.write_text(h, encoding='utf-8')

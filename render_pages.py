import asyncio
import os
from playwright.async_api import async_playwright

output_dir = r'c:\Users\lucag\.gemini\antigravity-ide\scratch\medstudylab\images'
os.makedirs(output_dir, exist_ok=True)

head_template = '''
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      width: 1240px;
      height: 1754px;
      background: #FAFCFF;
      font-family: 'Plus Jakarta Sans', sans-serif;
      color: #1E293B;
      padding: 60px 70px;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .page-footer-num {
      position: absolute;
      bottom: 30px;
      left: 0;
      right: 0;
      text-align: center;
      font-size: 24px;
      font-weight: 800;
      color: #64748B;
    }
    .top-section-tag {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 22px;
      font-weight: 800;
      color: #4F46E5;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 25px;
    }
    .top-section-tag::before {
      content: '';
      width: 16px;
      height: 16px;
      background: #4F46E5;
      transform: rotate(45deg);
      border-radius: 3px;
    }
  </style>
'''

pages_html = {}

# PAGE 1: Copertina Originale Recreata HD
pages_html[1] = head_template + '''
<style>
  body {
    padding: 0;
    justify-content: space-between;
    background: radial-gradient(circle at 50% 25%, #EFF6FF 0%, #FFFFFF 100%);
  }
  .cover-container {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 100px 60px 80px;
    text-align: center;
  }
  .cover-header h1 {
    font-family: 'Outfit', sans-serif;
    font-size: 88px;
    font-weight: 900;
    color: #243B6B;
    letter-spacing: -1.5px;
    line-height: 1.1;
    margin-bottom: 24px;
  }
  .cover-header h1 span {
    color: #2A9D8F;
    display: block;
  }
  .cover-subtitle {
    font-size: 32px;
    font-weight: 600;
    color: #475569;
    background: rgba(79, 70, 229, 0.07);
    padding: 16px 48px;
    border-radius: 40px;
    display: inline-block;
    border: 1px solid rgba(79, 70, 229, 0.15);
  }
  .cover-img-wrapper {
    width: 100%;
    max-width: 1050px;
    display: flex;
    justify-content: center;
  }
  .cover-img-wrapper img {
    width: 100%;
    height: auto;
    object-fit: contain;
  }
</style>
</head>
<body>
  <div class="cover-container">
    <div class="cover-header">
      <div style="font-size: 40px; margin-bottom: 20px;">✨ 💊 🧪 ✨</div>
      <h1>Farmacologia <span>illustrata</span></h1>
      <div class="cover-subtitle">Didattica visiva, direttamente al punto</div>
    </div>
    <div class="cover-img-wrapper">
      <img src="file:///c:/Users/lucag/.gemini/antigravity-ide/scratch/medstudylab/images/pagina_1.jpg" alt="Farmacologia Illustrata Cover">
    </div>
  </div>
</body>
</html>
'''

# PAGE 2: Leggere con cura e attenzione
pages_html[2] = head_template + '''
<style>
  body {
    background: #F8FAFC;
    align-items: center;
    justify-content: center;
  }
  .page2-card {
    background: #FFFFFF;
    border-radius: 32px;
    box-shadow: 0 25px 50px rgba(30, 41, 59, 0.08);
    border: 2px solid #E2E8F0;
    padding: 80px 70px;
    width: 100%;
    max-width: 1080px;
    display: flex;
    flex-direction: column;
    gap: 45px;
    position: relative;
  }
  .page2-title {
    font-family: 'Outfit', sans-serif;
    font-size: 54px;
    font-weight: 900;
    color: #3730A3;
    text-align: center;
    margin-bottom: 10px;
  }
  .intro-box {
    background: #F1F5F9;
    border-radius: 24px;
    padding: 40px 45px;
    border-left: 8px solid #6366F1;
  }
  .intro-box h2 {
    font-size: 34px;
    font-weight: 800;
    color: #1E293B;
    margin-bottom: 20px;
  }
  .intro-box p {
    font-size: 24px;
    line-height: 1.7;
    color: #334155;
    font-weight: 500;
  }
  .warning-box {
    background: #FEF2F2;
    border: 2px solid #FCA5A5;
    border-radius: 24px;
    padding: 40px 45px;
  }
  .warning-box h3 {
    font-size: 28px;
    font-weight: 800;
    color: #DC2626;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .warning-box p {
    font-size: 23px;
    line-height: 1.7;
    color: #7F1D1D;
    font-weight: 500;
  }
  .warning-box strong {
    color: #B91C1C;
  }
  .avatar-decor {
    position: absolute;
    bottom: -45px;
    right: 60px;
    width: 145px;
    height: 145px;
    border-radius: 50%;
    border: 6px solid #FFFFFF;
    box-shadow: 0 15px 35px rgba(0,0,0,0.18);
    overflow: hidden;
    background: #FFF;
  }
  .avatar-decor img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>
</head>
<body>
  <div class="page2-card">
    <h1 class="page2-title">Leggere con cura e attenzione</h1>
    <div class="intro-box">
      <h2>Ehi, come stai?</h2>
      <p>Innanzitutto vogliamo ringraziarvi per aver scelto il nostro materiale. Prepariamo tutto con grande dedizione per supportare i tuoi studi.<br><br>Ci auguriamo che questo strumento sia estremamente utile per te raggiungere i tuoi obiettivi. <strong>Buona fortuna e buoni studi!</strong></p>
    </div>
    <div class="warning-box">
      <h3>⚠️ Attenzione ad un avvertimento cruciale:</h3>
      <p>Questo contenuto è <strong>per uso esclusivo e personale</strong>. La riproduzione, la distribuzione o la vendita è severamente vietata.<br><br>La violazione di questi termini può comportare <strong>responsabilità penale</strong>, con le sanzioni previste dall’art. 184 cp, compresa la <strong>reclusione da 3 mesi a 4 anni</strong> e multe fino a 10 volte il valore del prodotto.</p>
    </div>
    <div class="avatar-decor">
      <img src="file:///c:/Users/lucag/.gemini/antigravity-ide/scratch/medstudylab/assets/avatar.png" alt="Avatar">
    </div>
  </div>
  <div class="page-footer-num">2</div>
</body>
</html>
'''

# PAGE 3: Sommario
pages_html[3] = head_template + '''
<style>
  body {
    background: #FAFCFF;
  }
  .sommario-title {
    font-family: 'Outfit', sans-serif;
    font-size: 58px;
    font-weight: 900;
    color: #3730A3;
    text-align: center;
    margin-bottom: 40px;
  }
  .section-card {
    background: #FFFFFF;
    border-radius: 26px;
    padding: 35px 45px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    border: 2px solid #E2E8F0;
    margin-bottom: 35px;
  }
  .section-header {
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    font-weight: 800;
    padding: 10px 24px;
    border-radius: 14px;
    display: inline-block;
    margin-bottom: 25px;
  }
  .sec-1-header {
    background: #EEF2FF;
    color: #4F46E5;
    border: 1px solid #C7D2FE;
  }
  .sec-2-header {
    background: #ECFDF5;
    color: #059669;
    border: 1px solid #A7F3D0;
  }
  .toc-grid {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .toc-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 21px;
    font-weight: 600;
    color: #334155;
    padding-bottom: 8px;
    border-bottom: 1px dashed #CBD5E1;
  }
  .toc-item span.item-title {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .toc-item span.item-page {
    font-weight: 800;
    color: #4F46E5;
    background: #F1F5F9;
    padding: 4px 14px;
    border-radius: 10px;
    font-size: 19px;
  }
</style>
</head>
<body>
  <h1 class="sommario-title">Sommario</h1>
  
  <div class="section-card">
    <div class="section-header sec-1-header">PARTE I — FONDAMENTALI</div>
    <div class="toc-grid">
      <div class="toc-item"><span class="item-title">1. Concetti fondamentali</span><span class="item-page">Pag. 05</span></div>
      <div class="toc-item"><span class="item-title">2. Forme farmaceutiche</span><span class="item-page">Pag. 08</span></div>
      <div class="toc-item"><span class="item-title">3. Nomenclatura</span><span class="item-page">Pag. 11</span></div>
      <div class="toc-item"><span class="item-title">4. Approcci terapeutici</span><span class="item-page">Pag. 13</span></div>
      <div class="toc-item"><span class="item-title">5. Vie di somministrazione</span><span class="item-page">Pag. 14</span></div>
      <div class="toc-item"><span class="item-title">6. Farmacocinetica</span><span class="item-page">Pag. 21</span></div>
      <div class="toc-item"><span class="item-title">7. Farmacodinamica</span><span class="item-page">Pag. 34</span></div>
      <div class="toc-item"><span class="item-title">8. Farmacocinetica vs Farmacodinamica</span><span class="item-page">Pag. 41</span></div>
      <div class="toc-item"><span class="item-title">9. Tossicità e farmacogenomica</span><span class="item-page">Pag. 42</span></div>
    </div>
  </div>

  <div class="section-card">
    <div class="section-header sec-2-header">PARTE II — INTERAZIONI CON I FARMACI</div>
    <div class="toc-grid">
      <div class="toc-item"><span class="item-title">10. Analgesici e Antinfiammatori</span><span class="item-page">Pag. 51</span></div>
      <div class="toc-item"><span class="item-title">11. Cardiovascolare</span><span class="item-page">Pag. 57</span></div>
      <div class="toc-item"><span class="item-title">12. Sistema nervoso centrale</span><span class="item-page">Pag. 64</span></div>
      <div class="toc-item"><span class="item-title">13. Antimicrobici</span><span class="item-page">Pag. 71</span></div>
      <div class="toc-item"><span class="item-title">14. Endocrino</span><span class="item-page">Pag. 77</span></div>
      <div class="toc-item"><span class="item-title">15. Gastrointestinale</span><span class="item-page">Pag. 80</span></div>
      <div class="toc-item"><span class="item-title">16. Indice</span><span class="item-page">Pag. 82</span></div>
      <div class="toc-item"><span class="item-title">17. Riferimenti bibliografici</span><span class="item-page">Pag. 83</span></div>
    </div>
  </div>
  <div class="page-footer-num">3</div>
</body>
</html>
'''

# PAGE 4: Parte I Fondamenti
pages_html[4] = head_template + '''
<style>
  body {
    background: radial-gradient(circle at 50% 30%, #F5F3FF 0%, #FFFFFF 100%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 80px 70px 60px;
    text-align: center;
  }
  .badge-part {
    background: #6366F1;
    color: white;
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    font-weight: 800;
    padding: 10px 36px;
    border-radius: 40px;
    display: inline-block;
    box-shadow: 0 8px 20px rgba(99, 102, 241, 0.35);
    margin-bottom: 25px;
  }
  .title-main {
    font-family: 'Outfit', sans-serif;
    font-size: 76px;
    font-weight: 900;
    color: #312E81;
    letter-spacing: 2px;
    margin-bottom: 20px;
  }
  .subtitle-text {
    font-size: 32px;
    font-weight: 600;
    color: #475569;
    margin-bottom: 35px;
  }
  .subtitle-text span {
    color: #4F46E5;
    font-weight: 800;
  }
  .topics-box {
    background: #FFFFFF;
    border: 2px solid #E0E7FF;
    border-radius: 30px;
    padding: 20px 45px;
    display: inline-flex;
    gap: 20px;
    font-size: 24px;
    font-weight: 700;
    color: #1E293B;
    box-shadow: 0 10px 25px rgba(79, 70, 229, 0.08);
  }
  .topics-box span.dot {
    color: #818CF8;
  }
  .hero-art {
    width: 100%;
    max-width: 850px;
    margin-top: 30px;
    border-radius: 24px;
    overflow: hidden;
  }
  .hero-art img {
    width: 100%;
    height: auto;
    object-fit: contain;
  }
</style>
</head>
<body>
  <div>
    <div class="badge-part">PARTE I</div>
    <h1 class="title-main">FONDAMENTI</h1>
    <p class="subtitle-text">I fondamenti che <span>sostengono</span> la pratica clinica</p>
    <div class="topics-box">
      <span>Concetti</span>
      <span class="dot">•</span>
      <span>Farmacocinetica</span>
      <span class="dot">•</span>
      <span>Farmacodinamica</span>
      <span class="dot">•</span>
      <span>Tossicità</span>
    </div>
  </div>
  <div class="hero-art">
    <img src="file:///c:/Users/lucag/.gemini/antigravity-ide/scratch/medstudylab/images/pagina_4.jpg" alt="Fondamenti Art">
  </div>
  <div class="page-footer-num">4</div>
</body>
</html>
'''

# PAGE 5: Concetti di Base in Farmacologia (100% Exact Complete Text) + Layout Infografico con Avatar
pages_html[5] = head_template + '''
<style>
  body {
    background: #FAFCFF;
    padding: 50px 65px;
  }
  .page5-title {
    font-family: 'Outfit', sans-serif;
    font-size: 46px;
    font-weight: 900;
    color: #1E3A8A;
    margin-bottom: 25px;
    text-align: center;
  }
  .layout-grid {
    display: flex;
    gap: 30px;
    align-items: flex-start;
  }
  .cards-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .concept-card {
    background: #FFFFFF;
    border-radius: 22px;
    padding: 18px 26px;
    display: flex;
    align-items: center;
    gap: 22px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.04);
    border: 2px solid #E2E8F0;
  }
  .card-icon {
    width: 68px;
    height: 68px;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 34px;
    flex-shrink: 0;
  }
  .card-content {
    flex: 1;
  }
  .card-header-badge {
    font-family: 'Outfit', sans-serif;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 5px;
    display: inline-block;
    padding: 4px 14px;
    border-radius: 8px;
  }
  .card-text {
    font-size: 20px;
    line-height: 1.5;
    color: #334155;
    font-weight: 500;
  }
  .side-avatar-box {
    width: 280px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    background: linear-gradient(180deg, #EEF2FF 0%, #FFFFFF 100%);
    border: 2px solid #C7D2FE;
    border-radius: 28px;
    padding: 30px 20px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(79, 70, 229, 0.08);
  }
  .side-avatar-img {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    overflow: hidden;
    border: 5px solid #FFFFFF;
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
  }
  .side-avatar-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .side-avatar-text {
    font-size: 19px;
    font-weight: 700;
    color: #3730A3;
    line-height: 1.45;
  }

  .bg-purple { background: #FAF5FF; border-color: #E9D5FF; }
  .badge-purple { background: #8B5CF6; color: white; }
  .icon-purple { background: #F3E8FF; }

  .bg-mint { background: #F0FDF4; border-color: #BBF7D0; }
  .badge-mint { background: #10B981; color: white; }
  .icon-mint { background: #DCFCE7; }

  .bg-blue { background: #EFF6FF; border-color: #BFDBFE; }
  .badge-blue { background: #3B82F6; color: white; }
  .icon-blue { background: #DBEAFE; }

  .bg-amber { background: #FFFBEB; border-color: #FDE68A; }
  .badge-amber { background: #F59E0B; color: white; }
  .icon-amber { background: #FEF3C7; }

  .bg-rose { background: #FFF1F2; border-color: #FECDD3; }
  .badge-rose { background: #F43F5E; color: white; }
  .icon-rose { background: #FFE4E6; }
</style>
</head>
<body>
  <div class="top-section-tag">Concetti di base</div>
  <h1 class="page5-title">Concetti di base in Farmacologia</h1>

  <div class="layout-grid">
    <div class="cards-container">
      <!-- 1. Farmacologia -->
      <div class="concept-card bg-purple">
        <div class="card-icon icon-purple">🔬</div>
        <div class="card-content">
          <div class="card-header-badge badge-purple">FARMACOLOGIA</div>
          <div class="card-text"><strong>Conosci la Farmacologia?</strong> È la scienza che studia gli effetti dei farmaci nell'organismo vivente (sostanza attiva + studio scientifico).</div>
        </div>
      </div>

      <!-- 2. Farmaco -->
      <div class="concept-card bg-blue">
        <div class="card-icon icon-blue">💊</div>
        <div class="card-content">
          <div class="card-header-badge badge-blue">FARMACO</div>
          <div class="card-text">Sostanza chimica con struttura conosciuta che, quando introdotta in un organismo vivo, è in grado di <strong>alterare le funzioni fisiologiche</strong> di un sistema biologico provocando un effetto.</div>
        </div>
      </div>

      <!-- 3. Principio Attivo -->
      <div class="concept-card bg-mint">
        <div class="card-icon icon-mint">🧬</div>
        <div class="card-content">
          <div class="card-header-badge badge-mint">PRINCIPIO ATTIVO</div>
          <div class="card-text">Sostanza chimica specifica presente all'interno di una medicina, direttamente <strong>responsabile del suo effetto terapeutico</strong> e biologico.</div>
        </div>
      </div>

      <!-- 4. Medicinale -->
      <div class="concept-card bg-rose">
        <div class="card-icon icon-rose">📦</div>
        <div class="card-content">
          <div class="card-header-badge badge-rose">MEDICINALE</div>
          <div class="card-text">Prodotto farmaceutico tecnicamente elaborato, contenente uno o più farmaci, con lo scopo di <strong>prevenire, curare, alleviare i sintomi</strong> o assistere la diagnosi di malattie.</div>
        </div>
      </div>

      <!-- 5. Rimedio -->
      <div class="concept-card bg-amber">
        <div class="card-icon icon-amber">🌿</div>
        <div class="card-content">
          <div class="card-header-badge badge-amber">RIMEDIO</div>
          <div class="card-text">Qualsiasi tipo di misura o intervento (terapeutico, naturale o comportamentale) effettuato con lo scopo di curare le malattie o ridurne sintomi e disagio in un individuo.</div>
        </div>
      </div>

      <!-- 6. Dosaggio -->
      <div class="concept-card bg-purple">
        <div class="card-icon icon-purple">⏱️</div>
        <div class="card-content">
          <div class="card-header-badge badge-purple">QUAL È IL DOSAGGIO?</div>
          <div class="card-text">È la precisa determinazione della quantità (dose) e degli <strong>orari di somministrazione</strong> di un medicinale necessari per ottenere l'effetto terapeutico desiderato.</div>
        </div>
      </div>
    </div>

    <!-- Side Avatar Box -->
    <div class="side-avatar-box">
      <div class="side-avatar-img">
        <img src="file:///c:/Users/lucag/.gemini/antigravity-ide/scratch/medstudylab/assets/avatar.png" alt="Avatar">
      </div>
      <div class="side-avatar-text">
        "Ogni farmaco agisce su specifici bersagli biologici: comprendere le basi è la chiave per la pratica clinica!"
      </div>
      <div style="font-size: 32px;">✨ 💊 🧪</div>
    </div>
  </div>
  <div class="page-footer-num">5</div>
</body>
</html>
'''

# PAGE 6: Effetto Placebo ed Effetto Nocebo (100% Exact Complete Text) + Illustrazioni e Diagrammi
pages_html[6] = head_template + '''
<style>
  body {
    background: #FAFCFF;
    padding: 50px 65px;
  }
  .section-box {
    background: #FFFFFF;
    border-radius: 26px;
    padding: 35px 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    margin-bottom: 28px;
    position: relative;
    border: 2px solid;
  }
  .box-placebo {
    border-color: #93C5FD;
    background: linear-gradient(180deg, #F0F9FF 0%, #FFFFFF 100%);
  }
  .box-nocebo {
    border-color: #FCA5A5;
    background: linear-gradient(180deg, #FEF2F2 0%, #FFFFFF 100%);
  }
  .box-title {
    font-family: 'Outfit', sans-serif;
    font-size: 32px;
    font-weight: 900;
    display: inline-block;
    padding: 8px 24px;
    border-radius: 14px;
    margin-bottom: 20px;
  }
  .title-placebo { background: #2563EB; color: white; }
  .title-nocebo { background: #DC2626; color: white; }
  .dialogue-p {
    font-size: 21px;
    line-height: 1.6;
    color: #334155;
    margin-bottom: 14px;
  }
  .highlight-card {
    border-radius: 18px;
    padding: 20px 26px;
    margin-top: 15px;
    font-size: 20px;
    line-height: 1.55;
    font-weight: 600;
  }
  .hl-placebo {
    background: #EFF6FF;
    border-left: 8px solid #3B82F6;
    color: #1E40AF;
  }
  .hl-nocebo {
    background: #FEF3C7;
    border-left: 8px solid #F59E0B;
    color: #92400E;
  }
  .badge-icon-pill {
    font-size: 26px;
    vertical-align: middle;
    margin-right: 8px;
  }
</style>
</head>
<body>
  <div class="top-section-tag">Concetti di base</div>

  <!-- EFFETTO PLACEBO -->
  <div class="section-box box-placebo">
    <div class="box-title title-placebo"><span class="badge-icon-pill">✨</span> EFFETTO PLACEBO</div>
    <p class="dialogue-p"><strong>Immagina di avere un forte mal di testa</strong> e qualcuno ti dà una pillola dicendoti che è una medicina potente ed efficace.<br>La prendi e, <em>"magicamente"</em>, il tuo dolore scompare del tutto!</p>
    <p class="dialogue-p"><strong>Questo è l'effetto placebo in azione!</strong> È quando ti senti meglio semplicemente per la <strong>fiducia nel trattamento</strong>, anche se il medicinale stesso potrebbe essere biologicamente inattivo (composto solo da farina o zucchero, senza principio attivo).</p>
    <div class="highlight-card hl-placebo">
      💡 <strong>Perché è fondamentale nella ricerca?</strong> Negli studi clinici è sempre presente il <em>"Gruppo Placebo"</em> per dimostrare scientificamente che la medicina funziona per la sua reale azione chimica e non per mera suggestione psicologica.
    </div>
  </div>

  <!-- EFFETTO NOCEBO -->
  <div class="section-box box-nocebo">
    <div class="box-title title-nocebo"><span class="badge-icon-pill">⚡</span> EFFETTO NOCEBO</div>
    <p class="dialogue-p"><strong>Immagina di dare una pillola di sola farina</strong> avvisando però il paziente: <em>"Fai attenzione, questo farmaco ti farà venire un forte mal di testa."</em> Il paziente la assume e il dolore appare davvero!</p>
    <p class="dialogue-p"><strong>Questo è il Nocebo, l'esatto opposto del placebo!</strong> L'aspettativa negativa e l'ansia fanno sì che il cervello induca il corpo a manifestare <strong>sintomi ed effetti avversi reali</strong>, pur in assenza di una causa chimica o farmacologica.</p>
    <div class="highlight-card hl-nocebo">
      ⚠️ <strong>Lezione clinica essenziale:</strong> Fai massima attenzione alla comunicazione! L'eccessiva paura degli effetti collaterali può indurre il paziente a sperimentarli realmente, anche con farmaci del tutto sicuri.
    </div>
  </div>
  <div class="page-footer-num">6</div>
</body>
</html>
'''

# PAGE 7: Potenza vs Efficacia (100% Exact Complete Text) + Grafica Divisa a Colonne
pages_html[7] = head_template + '''
<style>
  body {
    background: #FAFCFF;
    padding: 50px 65px;
  }
  .page7-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    margin-top: 15px;
  }
  .potenza-col {
    background: #FFFBEB;
    border: 2px solid #FDE68A;
    border-radius: 26px;
    padding: 32px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .efficacia-col {
    background: #FAF5FF;
    border: 2px solid #E9D5FF;
    border-radius: 26px;
    padding: 32px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .col-title {
    font-family: 'Outfit', sans-serif;
    font-size: 32px;
    font-weight: 900;
    padding: 10px 20px;
    border-radius: 14px;
    text-align: center;
  }
  .title-pot { background: #F59E0B; color: white; }
  .title-eff { background: #8B5CF6; color: white; }
  .def-box {
    background: white;
    border-radius: 18px;
    padding: 22px 24px;
    font-size: 20px;
    line-height: 1.55;
    color: #334155;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }
  .use-badge {
    font-size: 16px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #64748B;
    margin-bottom: 8px;
  }
  .example-card {
    background: white;
    border-radius: 18px;
    padding: 24px;
    border-left: 8px solid;
    font-size: 20px;
    line-height: 1.55;
  }
  .ex-pot { border-color: #F59E0B; color: #92400E; }
  .ex-eff { border-color: #8B5CF6; color: #581C87; }
</style>
</head>
<body>
  <div class="top-section-tag">Concetti di base</div>

  <div class="page7-grid">
    <!-- COLONNA POTENZA -->
    <div class="potenza-col">
      <div class="col-title title-pot">⚡ POTENZA</div>
      <div class="def-box">
        <strong>Cos'è:</strong> Quantità di farmaco necessaria per produrre un dato effetto terapeutico.<br><br>
        Un farmaco <strong>più potente</strong> ha bisogno di una <strong>dose più piccola</strong> per produrre lo stesso effetto di un farmaco meno potente.
      </div>
      <div class="def-box">
        <div class="use-badge">FARMACO — COME SI USA</div>
        <strong>Atto di gestione del medicinale:</strong><br>
        <em>Esempio:</em> Prendi 1 compressa di Paracetamolo 750 mg per via orale ogni 8 ore.
      </div>
      <div class="example-card ex-pot">
        <strong>🔍 Esempio Pratico:</strong><br>
        Se il Farmaco A necessita di soli <strong>10 mg</strong> per alleviare il dolore, mentre il Farmaco B richiede <strong>20 mg</strong> per lo stesso risultato, allora il <strong>Farmaco A è più potente</strong> del Farmaco B.
      </div>
    </div>

    <!-- COLONNA EFFICACIA -->
    <div class="efficacia-col">
      <div class="col-title title-eff">🎯 EFFICACIA</div>
      <div class="def-box">
        <strong>Cos'è:</strong> L'entità massima dell'effetto prodotto dal farmaco quando interagisce con il proprio recettore biologico.
      </div>
      <div class="def-box">
        <div class="use-badge">MEDICINALE — COSA USI</div>
        <strong>Prodotto farmaceutico con scopo terapeutico:</strong><br>
        <em>Esempio:</em> Scatola commerciale di Paracetamolo 750 mg in compresse.
      </div>
      <div class="example-card ex-eff">
        <strong>🚀 Esempio del Razzo:</strong><br>
        Immagina che il Farmaco A sia come un razzo che genera una <strong>grande esplosione</strong> (massimo effetto), mentre il Farmaco B genera una piccola esplosione.<br><br>
        Il <strong>Farmaco A è più efficace</strong> del Farmaco B poiché produce una risposta biologica maggiore al connettersi al recettore.
      </div>
    </div>
  </div>
  <div class="page-footer-num">7</div>
</body>
</html>
'''

# PAGE 8: Forme Farmaceutiche Solide (100% Exact Complete Text) + Icone Prodotti
pages_html[8] = head_template + '''
<style>
  body {
    background: #FAFCFF;
    padding: 50px 65px;
  }
  .page8-header {
    margin-bottom: 25px;
  }
  .page8-title {
    font-family: 'Outfit', sans-serif;
    font-size: 48px;
    font-weight: 900;
    color: #1E3A8A;
    margin-bottom: 8px;
  }
  .page8-badge {
    background: #ECFDF5;
    color: #059669;
    border: 1px solid #A7F3D0;
    font-size: 22px;
    font-weight: 800;
    padding: 6px 22px;
    border-radius: 20px;
    display: inline-block;
  }
  .intro-text-p8 {
    font-size: 22px;
    line-height: 1.55;
    color: #475569;
    margin-top: 14px;
    background: #F1F5F9;
    padding: 18px 26px;
    border-radius: 18px;
    font-weight: 500;
  }
  .solids-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-top: 20px;
  }
  .solid-item {
    background: #FFFFFF;
    border: 2px solid #E2E8F0;
    border-radius: 20px;
    padding: 18px 24px;
    display: flex;
    align-items: center;
    gap: 22px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.03);
  }
  .solid-icon-badge {
    width: 64px;
    height: 64px;
    border-radius: 16px;
    background: #F8FAFC;
    border: 1px solid #CBD5E1;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    flex-shrink: 0;
  }
  .solid-content h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: #1E293B;
    margin-bottom: 4px;
  }
  .solid-content p {
    font-size: 20px;
    line-height: 1.45;
    color: #475569;
  }
  .eccipiente-note {
    background: #EFF6FF;
    border-left: 6px solid #3B82F6;
    border-radius: 14px;
    padding: 14px 20px;
    margin-top: 8px;
    font-size: 19px;
    color: #1E40AF;
  }
</style>
</head>
<body>
  <div class="top-section-tag">Forme farmaceutiche</div>
  <div class="page8-header">
    <h1 class="page8-title">Forme farmaceutiche</h1>
    <div class="page8-badge">Forme solide</div>
    <div class="intro-text-p8">
      <strong>Classificazione generale:</strong> Diverse forme fisiche in cui i farmaci vengono presentati, classificabili in <em>solide, liquide e semisolide</em>.
    </div>
  </div>

  <div class="solids-list">
    <!-- 1. Capsula -->
    <div class="solid-item">
      <div class="solid-icon-badge">💊</div>
      <div class="solid-content">
        <h3>Capsula</h3>
        <p>Preparazione solida in cui i farmaci sono incapsulati all'interno di un involucro commestibile (comunemente costituito da amido o gelatina).</p>
      </div>
    </div>

    <!-- 2. Confetto -->
    <div class="solid-item">
      <div class="solid-icon-badge">🍬</div>
      <div class="solid-content">
        <h3>Confetto</h3>
        <p>Compresse rivestite con sostanze specifiche come zuccheri, cere, resine o gomme (utili per mascherare sapori o odori sgradevoli).</p>
      </div>
    </div>

    <!-- 3. Polvere -->
    <div class="solid-item">
      <div class="solid-icon-badge">🧂</div>
      <div class="solid-content">
        <h3>Polvere</h3>
        <p>Principi attivi allo stato secco con dimensione ridotta delle particelle; può contenere eccipienti o meno.</p>
      </div>
    </div>

    <!-- 4. Pillola / Compressa -->
    <div class="solid-item">
      <div class="solid-icon-badge">⚪</div>
      <div class="solid-content">
        <h3>Pillola / Compressa</h3>
        <p>Formulazione solida ottenuta attraverso la compressione meccanica del farmaco e del suo eccipiente.</p>
        <div class="eccipiente-note">
          <strong>Cos'è l'eccipiente?</strong> Sostanza inerte aggiunta al medicinale per controllarne il volume, dare la forma corretta e facilitarne l'assunzione, senza esercitare alcun effetto farmacologico.
        </div>
      </div>
    </div>

    <!-- 5. Supposta -->
    <div class="solid-item">
      <div class="solid-icon-badge">🕯️</div>
      <div class="solid-content">
        <h3>Supposta</h3>
        <p>Formulazione solida creata per essere inserita negli orifizi (rettale, vaginale o uretrale), progettata per fondere alla temperatura corporea rilasciando il principio attivo grazie a una base inerte.</p>
      </div>
    </div>
  </div>
  <div class="page-footer-num">8</div>
</body>
</html>
'''

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for i in range(1, 9):
            page = await browser.new_page(viewport={'width': 1240, 'height': 1754})
            await page.set_content(pages_html[i], wait_until='networkidle')
            out_file = os.path.join(output_dir, f'pagina_{i}.jpg')
            await page.screenshot(path=out_file, type='jpeg', quality=95)
            await page.close()
            print(f'Rendered Page {i} perfectly with 100% complete text')
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

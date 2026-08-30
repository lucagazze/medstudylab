# -*- coding: utf-8 -*-
"""Pagine 1-8."""
from common import A, shell, row, note, head, strip, k, flow, bullets, via, band

# ================================================================= pagina 1
P1 = shell(f"""
<div class="blob" style="width:250px;height:250px;background:var(--mint-s);left:-70px;top:300px"></div>
<div class="sq"   style="width:150px;height:150px;background:var(--lav-s);right:52px;top:392px;transform:rotate(-8deg)"></div>
<div class="blob" style="width:190px;height:190px;background:var(--sky-s);right:-50px;top:560px"></div>
<div class="sq"   style="width:120px;height:120px;background:var(--mint-s);left:96px;top:600px;transform:rotate(10deg)"></div>
<img class="deco" src="{A}/icon-molecule.png" style="width:120px;left:44px;top:392px;opacity:.85">
<img class="deco" src="{A}/icon-molecule.png" style="width:96px;right:56px;top:300px;opacity:.7;transform:scaleX(-1)">
<img class="deco" src="{A}/icon-capsule.png" style="width:80px;left:150px;top:280px;transform:rotate(-18deg)">
<img class="deco" src="{A}/icon-tablet.png"  style="width:70px;right:150px;top:610px;transform:rotate(12deg)">
<div class="cover">
  <div class="brandmark"><b></b>Studio Facile<b></b></div>
  <h1>Farmacologia<span>illustrata</span></h1>
  <div class="sub">Didattica visiva, direttamente al punto</div>
  <div class="avatar-big"><img src="{A}/avatar.png" alt=""></div>
  <img class="pile" src="{A}/cover-pile.png" alt="">
  <div class="chips">
    <span class="chip">Fondamenti</span>
    <span class="chip m">Farmacocinetica</span>
    <span class="chip s">Farmacodinamica</span>
    <span class="chip">Interazioni</span>
  </div>
</div>""")

# ================================================================= pagina 2
P2 = shell(f"""
<img class="deco" src="{A}/icon-blister.png" style="width:140px;right:24px;top:48px;opacity:.6">
<div class="body" style="display:flex;flex-direction:column;justify-content:space-between">
  <div>
    <div class="hd"><div class="eyebrow"><b></b>Prima di iniziare</div>
    <h1 class="title" style="margin-top:10px">Leggere con cura<br>e attenzione</h1></div>
    <div style="display:flex;align-items:center;gap:18px;margin-top:22px">
      <img src="{A}/icon-shield.png" style="width:110px">
      <div style="font-size:13.5px;font-weight:600;color:var(--ink-soft);line-height:1.5">
        Materiale protetto da diritto d'autore.<br>Licenza personale e non trasferibile.
      </div>
    </div>
  </div>
  <div class="card">
    <div class="hi">Ehi, come stai?</div>
    <p>Innanzitutto vogliamo ringraziarti per aver scelto il nostro materiale.
       Prepariamo tutto con grande dedizione per supportare i tuoi studi.</p>
    <p>Ci auguriamo che questo strumento sia estremamente utile per raggiungere
       i tuoi obiettivi. Buona fortuna e buono studio!</p>
    <div class="warn">
      <h3>Attenzione: avvertimento cruciale</h3>
      <p>Questo contenuto è per uso esclusivo e personale. La riproduzione, la
         distribuzione o la vendita è severamente vietata. La violazione di questi
         termini può comportare responsabilità penale, con le sanzioni previste
         dall'art. 184 c.p.: reclusione da 3 mesi a 4 anni e multe fino a 10 volte
         il valore del prodotto.</p>
    </div>
  </div>
  <div class="trio">
    <div class="t"><img src="{A}/icon-clipboard.png">
      <h4>Studia per blocchi</h4>
      <p>Ogni pagina è un concetto chiuso: leggi, osserva l'illustrazione, ripeti.</p></div>
    <div class="t"><img src="{A}/icon-magnifier.png">
      <h4>Solo l'essenziale</h4>
      <p>Definizioni ridotte al minimo indispensabile, senza giri di parole.</p></div>
    <div class="t"><img src="{A}/icon-book.png">
      <h4>Ripassa in fretta</h4>
      <p>Torna alle schede prima dell'esame: bastano pochi minuti.</p></div>
  </div>
</div>""", folio="2")

# ================================================================= pagina 3
TOC1 = [("1", "Concetti fondamentali", "05"), ("2", "Forme farmaceutiche", "08"),
        ("3", "Nomenclatura", "11"), ("4", "Approcci terapeutici", "13"),
        ("5", "Vie di somministrazione", "14"), ("6", "Farmacocinetica", "21"),
        ("7", "Farmacodinamica", "34"), ("8", "Farmacocinetica vs Farmacodinamica", "41"),
        ("9", "Tossicità e farmacogenomica", "42")]
TOC2 = [("10", "Analgesici e antinfiammatori", "51"), ("11", "Cardiovascolare", "57"),
        ("12", "Sistema nervoso centrale", "64"), ("13", "Antimicrobici", "71"),
        ("14", "Endocrino", "77"), ("15", "Gastrointestinale", "80"),
        ("16", "Indice", "82"), ("17", "Riferimenti bibliografici", "83")]


def toc(items):
    return "".join(f'<div class="li"><span class="n">{n}</span>'
                   f'<span class="t">{t}</span><span class="p">Pag. {p}</span></div>'
                   for n, t, p in items)


P3 = shell(f"""
<img class="deco" src="{A}/icon-molecule.png" style="width:112px;right:40px;top:42px;opacity:.55">
<div class="body">
  <div style="display:flex;align-items:center;gap:16px">
    <img src="{A}/icon-clipboard.png" style="width:92px">
    <div>
      <div class="hd"><div class="eyebrow"><b></b>Indice</div>
      <h1 class="title" style="font-size:40px;margin-top:6px">Sommario</h1></div>
    </div>
  </div>
  <div class="toc-part">Parte I — Fondamenti</div>
  <div class="toc">{toc(TOC1)}</div>
  <div class="toc-part">Parte II — Interazioni con i farmaci</div>
  <div class="toc">{toc(TOC2)}</div>
</div>""", folio="3")

# ================================================================= pagina 4
P4 = shell(f"""
<div class="blob" style="width:300px;height:300px;background:var(--lav-s);left:-100px;top:-70px"></div>
<div class="blob" style="width:240px;height:240px;background:var(--mint-s);right:-80px;bottom:30px"></div>
<img class="deco" src="{A}/icon-capsule.png" style="width:78px;left:96px;top:250px;transform:rotate(-20deg);opacity:.9">
<img class="deco" src="{A}/icon-molecule.png" style="width:96px;right:84px;top:214px;opacity:.6">
<img class="cutout" src="{A}/mascot-capsule.png" style="width:190px;right:60px;bottom:118px">
<div class="divider">
  <div class="badge">PARTE I</div>
  <h1>FONDAMENTI</h1>
  <div class="rule"></div>
  <div class="sub">I fondamenti che <b>sostengono</b> la pratica clinica</div>
  <div class="chips">
    <span class="chip">Concetti</span>
    <span class="chip m">Farmacocinetica</span>
    <span class="chip s">Farmacodinamica</span>
    <span class="chip">Tossicità</span>
  </div>
  <img class="art" src="{A}/icon-book.png" alt="">
  <div style="margin-top:10px;font-size:11.5px;font-weight:700;letter-spacing:2.4px;
              text-transform:uppercase;color:var(--ink-soft);opacity:.7">
    Capitoli 1 → 9 · pagine 5 – 50
  </div>
</div>""", folio="4")

# ================================================================= pagina 5
ROWS5 = [
    ("lav", "icon-microscope", "Farmacologia", False,
     "La scienza che studia gli effetti dei farmaci sull'organismo: origine, "
     "composizione, proprietà e meccanismo d'azione."),
    ("mint", "icon-bottles", "Farmaco", True,
     "Sostanza chimica che può alterare le funzioni fisiologiche di un sistema "
     "biologico. Introdotta in un organismo vivo, provoca un effetto biologico."),
    ("sky", "icon-molecule", "Principio attivo", True,
     "Sostanza chimica presente in un medicinale, responsabile del suo effetto "
     "terapeutico."),
    ("lav", "icon-blister", "Medicinale", True,
     "Prodotto farmaceutico tecnicamente elaborato, contenente uno o più farmaci, "
     "per prevenire, curare o alleviare i sintomi di una malattia."),
    ("mint", "icon-mortar", "Rimedio", False,
     "Qualsiasi misura adottata allo scopo di curare una malattia o di ridurne "
     "sintomi e disagio."),
    ("sky", "icon-beaker", "Dosaggio", False,
     "Determinazione della quantità e degli orari di somministrazione di un "
     "medicinale, per ottenere l'effetto terapeutico desiderato."),
]


def row(c, ic, t, narrow, p):
    n = " narrow" if narrow else ""
    return (f'<div class="row {c}{n}"><div class="disc"><img src="{A}/{ic}.png"></div>'
            f'<div class="txt"><h2>{t}</h2><p>{p}</p></div></div>')


P5 = shell(f"""
<img class="deco" src="{A}/icon-molecule.png" style="width:92px;right:26px;top:130px;opacity:.55">
<img class="deco" src="{A}/icon-capsule.png" style="width:66px;left:14px;top:430px;transform:rotate(-24deg);opacity:.8">
<img class="deco" src="{A}/icon-plant.png" style="width:70px;right:36px;bottom:44px;opacity:.9">
<img class="cutout" src="{A}/avatar-wave.png" style="width:214px;right:-4px;top:252px">
<div class="body">
  <div class="hd"><div class="eyebrow"><b></b>1 · Concetti fondamentali</div>
  <h1 class="title" style="font-size:33px;margin-top:6px">Concetti di base in
    <span class="p">Farmacologia</span></h1></div>
  <div class="rows">{"".join(row(*r) for r in ROWS5)}</div>
  <div class="note">
    <img src="{A}/icon-idea.png">
    <div>
      <h4>Da ricordare</h4>
      <p>Il <b>farmaco</b> è la sostanza; il <b>principio attivo</b> è ciò che produce
         l'effetto; il <b>medicinale</b> è il prodotto finito che lo contiene.</p>
    </div>
  </div>
</div>""", folio="5")

# ================================================================= pagina 6
P6 = shell(f"""
<img class="deco" src="{A}/icon-capsule.png" style="width:64px;right:34px;top:126px;transform:rotate(18deg);opacity:.85">
<img class="cutout" src="{A}/avatar-point.png" style="width:186px;right:-14px;bottom:36px;transform:scaleX(-1)">
<div class="body">
  <div class="hd"><div class="eyebrow"><b></b>1 · Concetti fondamentali</div>
  <h1 class="title" style="font-size:33px;margin-top:6px">Effetto
    <span class="p">placebo</span> e <span class="p">nocebo</span></h1></div>

  <div class="panel lav" style="margin-top:16px">
    <span class="tag p">Effetto placebo</span>
    <div class="steps">
      <div class="s"><span class="n">1</span><img src="{A}/icon-headache.png">
        <p>Hai mal di testa. Qualcuno ti dà una pillola dicendo che è un farmaco potente.</p></div>
      <div class="s"><span class="n">2</span><img src="{A}/icon-capsule.png">
        <p>La prendi e, «magicamente», il dolore scompare nel giro di poco.</p></div>
      <div class="s"><span class="n">3</span><img src="{A}/icon-polvere.png">
        <p>Ma quella pillola era solo farina e zucchero: nessun principio attivo.</p></div>
    </div>
    <div class="concl">Questo è l'<b>effetto placebo</b>: ti senti meglio per la fiducia
      nel trattamento, anche se il trattamento è biologicamente inattivo.</div>
    <div class="concl" style="background:var(--lav);margin-top:9px">
      <b>Perché è importante?</b> Negli studi clinici esiste sempre un «gruppo placebo»:
      serve a dimostrare che il medicinale funziona per azione chimica e non solo per
      effetto psicologico sul paziente.</div>
  </div>

  <div class="panel rose">
    <span class="tag r">Effetto nocebo</span>
    <div class="steps">
      <div class="s"><span class="n">1</span><img src="{A}/icon-tablet.png">
        <p>Dai una pillola di farina avvisando: «Attento, ti farà venire mal di testa».</p></div>
      <div class="s"><span class="n">2</span><img src="{A}/icon-headache.png">
        <p>Il paziente la prende e il dolore compare davvero, senza alcuna causa chimica.</p></div>
    </div>
    <div class="concl">È il <b>nocebo</b>, l'opposto del placebo: l'aspettativa negativa
      fa sì che il corpo produca sintomi reali.</div>
  </div>

  <div class="note">
    <img src="{A}/icon-warning.png">
    <div>
      <h4>Lezione</h4>
      <p>Attenzione a come comunichi gli effetti avversi: una paura eccessiva può
         indurre il paziente a percepirli, anche quando il medicinale è sicuro.</p>
    </div>
  </div>
</div>""", folio="6")

# ================================================================= pagina 7
P7 = shell(f"""
<img class="deco" src="{A}/icon-molecule.png" style="width:86px;left:26px;bottom:74px;opacity:.5">
<img class="cutout" src="{A}/mascot-capsule.png" style="width:150px;right:26px;bottom:30px">
<div class="body">
  <div class="hd"><div class="eyebrow"><b></b>1 · Concetti fondamentali</div>
  <h1 class="title" style="font-size:33px;margin-top:6px">Farmaco o medicinale?
    <span class="p">Potenza</span> ed <span class="p">efficacia</span></h1></div>

  <div class="grid2">
    <div class="k">
      <span class="tag s">Farmaco</span>
      <h4>È il principio attivo: la sostanza che agisce.</h4>
      <p><b>Come</b> si usa.</p>
      <div class="ex"><b>Esempio:</b> prendi 1 compressa di Paracetamolo 750 mg
        per via orale ogni 8 ore.</div>
      <img class="big" src="{A}/icon-taking.png">
    </div>
    <div class="k mint">
      <span class="tag m">Medicinale</span>
      <h4>È il prodotto farmaceutico finito, con scopo terapeutico.</h4>
      <p><b>Cosa</b> usi.</p>
      <div class="ex"><b>Esempio:</b> Paracetamolo 750 mg, compressa —
        la confezione che trovi in farmacia.</div>
      <img class="big" src="{A}/icon-medbox.png">
    </div>
  </div>

  <div class="grid2">
    <div class="k">
      <img class="ico" src="{A}/icon-dumbbell.png">
      <span class="tag p">Potenza</span>
      <p style="margin-top:12px">Quantità di farmaco necessaria per produrre un certo
        effetto. Più è potente, minore è la dose che serve.</p>
      <div class="ex"><b>Esempio:</b> se al farmaco A bastano 10 mg per togliere il
        dolore e al farmaco B ne servono 20 mg, il farmaco A è <b>più potente</b>.</div>
    </div>
    <div class="k sky">
      <img class="ico" src="{A}/icon-rocket.png">
      <span class="tag p">Efficacia</span>
      <p style="margin-top:12px">Quanto è grande l'effetto massimo che il farmaco
        produce quando interagisce con il recettore.</p>
      <div class="ex"><b>Esempio:</b> il farmaco A è un razzo che crea una grande
        esplosione, il farmaco B un razzo più piccolo: A è <b>più efficace</b>.</div>
    </div>
  </div>

  <div class="strip">
    <div class="b"><b>Farmaco</b>la sostanza che agisce — <i>come</i> si usa</div>
    <div class="sep"></div>
    <div class="b"><b>Medicinale</b>il prodotto in farmacia — <i>cosa</i> usi</div>
    <div class="sep"></div>
    <div class="b"><b>Dose</b>quanto ne serve per ottenere l'effetto</div>
  </div>

  <div class="note" style="padding-right:180px">
    <img src="{A}/icon-idea.png">
    <div>
      <h4>Non confonderli</h4>
      <p>La <b>potenza</b> riguarda la dose necessaria; l'<b>efficacia</b> riguarda
         l'effetto massimo raggiungibile. Un farmaco può essere potente ma poco efficace.</p>
    </div>
  </div>
</div>""", folio="7")

# ================================================================= pagina 8
ROWS8 = [
    ("lav", "icon-tablet", "Pillola",
     "Formulazione solida ottenuta per compressione del farmaco insieme al suo eccipiente."),
    ("mint", "icon-capsule", "Capsula",
     "Preparazione solida in cui i farmaci sono racchiusi in un involucro commestibile, "
     "di solito amido o gelatina."),
    ("sky", "icon-confetto", "Confetto",
     "Compresse rivestite con zuccheri, cere, resine o gomme, che mascherano sapore e odore."),
    ("lav", "icon-polvere", "Polvere",
     "Principi attivi allo stato secco, con particelle di dimensione ridotta; "
     "possono contenere eccipienti oppure no."),
    ("mint", "icon-supposta", "Supposta",
     "Pensata per essere inserita negli orifizi rettale, vaginale o uretrale: "
     "si scioglie alla temperatura corporea."),
]

P8 = shell(f"""
<img class="deco" src="{A}/icon-plant.png" style="width:80px;right:40px;top:58px;opacity:.9">
<div class="body">
  <div class="hd"><div class="eyebrow"><b></b>2 · Forme farmaceutiche</div>
  <h1 class="title" style="font-size:33px;margin-top:6px">Forme
    <span class="p">solide</span></h1></div>
  <div style="display:flex;align-items:center;gap:18px;margin-top:12px;
              background:var(--mint-s);border-radius:30px;padding:14px 22px">
    <img src="{A}/icon-bottles.png" style="width:82px">
    <div class="lead">Le <b>forme farmaceutiche</b> sono le diverse forme fisiche in cui
      un farmaco viene presentato. Si classificano in <b>solide</b>, <b>liquide</b> e
      <b>semisolide</b>: qui vediamo le prime.</div>
  </div>
  <div class="rows">{"".join(row(c, ic, t, False, p) for c, ic, t, p in ROWS8)}</div>
  <div class="strip" style="background:var(--lav-s)">
    <div class="b"><b>Solide</b>pillola, capsula, confetto, polvere, supposta</div>
    <div class="sep" style="background:var(--lav)"></div>
    <div class="b"><b>Liquide</b>sciroppi, soluzioni, sospensioni, gocce</div>
    <div class="sep" style="background:var(--lav)"></div>
    <div class="b"><b>Semisolide</b>creme, unguenti, gel, paste</div>
  </div>

  <div class="note">
    <img src="{A}/icon-idea.png">
    <div>
      <h4>Eccipiente</h4>
      <p>Sostanza inerte aggiunta al medicinale per controllarne volume e forma e
         facilitarne la somministrazione, senza esercitare effetti farmacologici propri.</p>
    </div>
  </div>
</div>""", folio="8")

PAGES = [P1, P2, P3, P4, P5, P6, P7, P8]

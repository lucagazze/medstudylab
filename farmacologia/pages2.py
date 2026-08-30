# -*- coding: utf-8 -*-
"""Pagine 9-18 — Forme liquide/semisolide, Nomenclatura, Approcci, Vie di somministrazione."""
from common import A, shell, row, note, head, strip, k, flow, bullets, via

# ================================================================= pagina 9
P9 = shell(f"""
<img class="deco" src="{A}/icon-molecule.png" style="width:86px;right:24px;top:120px;opacity:.5">
<div class="body">
  {head("2 · Forme farmaceutiche", 'Forme <span class="p">liquide</span>')}
  {row("sky", "icon-beaker", "Soluzione",
       "Formulazione chiara e omogenea (monofase), con il principio attivo "
       "completamente disciolto nel solvente. Può essere di due tipi:")}
  <div class="grid2" style="margin-top:11px">
    {k("Sciroppo", "s", "", "Soluzione di consistenza viscosa, ottenuta con un'alta "
       "concentrazione di zuccheri o di agenti addensanti.", "", "icon-syrup", "sky")}
    {k("Elisir", "s", "", "Soluzione idroalcolica (acqua + alcol), con viscosità "
       "inferiore allo sciroppo e sapore dolce.", "", "icon-elixir", "sky")}
  </div>
  {row("mint", "icon-suspension", "Sospensione",
       "Forma liquida in cui le particelle solide restano disperse (galleggianti), "
       "senza dissolversi nel liquido: è un sistema eterogeneo, va agitata prima dell'uso.")}
  {row("lav", "icon-emulsion", "Emulsione",
       "È composta da due liquidi che non si mescolano (immiscibili, come acqua e olio): "
       "uno è disperso in goccioline dentro l'altro.")}
  <div class="grid2" style="margin-top:11px">
    {k("Olio in acqua (O/A)", "p", "", "Le goccioline di olio sono disperse in una "
       "fase acquosa continua.")}
    {k("Acqua in olio (A/O)", "p", "", "Le goccioline d'acqua sono disperse in una "
       "fase oleosa continua.")}
  </div>
  {strip([("Fase interna", "è la fase dispersa: le goccioline"),
          ("Fase esterna", "è la fase continua che le avvolge"),
          ("Emulsionante", "l'agente che mantiene stabile la miscela")],
         "var(--lav-s)", "var(--lav)")}
</div>""", folio="9")

# ================================================================= pagina 10
P10 = shell(f"""
<img class="cutout" src="{A}/avatar-point.png" style="width:150px;right:20px;bottom:24px">
<div class="body">
  {head("2 · Forme farmaceutiche", 'Forme <span class="p">semisolide</span> e cerotto')}
  {row("mint", "icon-cream", "Crema",
       "Preparazione di consistenza semisolida composta da un'emulsione (contiene una "
       "fase acquosa e una oleosa), generalmente per applicazione esterna e topica.")}
  {row("lav", "icon-ointment", "Unguento",
       "Preparato per pelle o mucose, con una base in genere non acquosa (grassa, lipofila). "
       "Contiene principi attivi disciolti o dispersi in concentrazioni ridotte.")}
  {row("sky", "icon-gel", "Gel",
       "Forma semisolida composta da un agente gelificante (per esempio polimeri) che "
       "conferisce fermezza a una soluzione o dispersione colloidale.")}
  <div class="grid2" style="margin-top:11px">
    {k("Crema o unguento?", "m", "", "A differenza della crema, che contiene acqua, "
       "l'unguento è più oleoso e occlusivo.", "", "", "mint")}
    {k("Dispersione colloidale", "s", "", "È il sistema in cui particelle di dimensioni "
       "molto ridotte (tra 1 nm e 1 µm) sono distribuite uniformemente in un liquido, "
       "senza precipitare: è ciò che forma la struttura del gel.", "", "", "sky")}
  </div>
  <div class="panel lav" style="margin-top:13px">
    <span class="tag p">Cerotto transdermico</span>
    <div class="steps" style="padding-right:150px">
      <div class="s"><span class="n">1</span><img src="{A}/icon-patch.png">
        <p>Funziona come una «scorciatoia»: rilascia il farmaco attraverso la pelle
           (via percutanea), ma non serve a trattare la pelle stessa.</p></div>
      <div class="s"><span class="n">2</span><img src="{A}/icon-skin.png">
        <p>Il farmaco attraversa gli strati fino al derma e raggiunge il flusso
           sanguigno: da lì si diffonde in tutto il corpo (effetto sistemico).</p></div>
    </div>
    <div class="concl">La sua tecnologia consente un <b>rilascio costante e prolungato</b>:
      mantiene il livello del farmaco stabile nel sangue a lungo, senza oscillazioni.</div>
  </div>
</div>""", folio="10")

# ================================================================= pagina 11
P11 = shell(f"""
<img class="deco" src="{A}/icon-capsule.png" style="width:64px;left:22px;bottom:64px;transform:rotate(-20deg);opacity:.8">
<div class="body">
  {head("3 · Nomenclatura", 'Nomenclatura dei <span class="p">medicinali</span>')}
  <div class="klist">
    {k("Nome chimico", "p", "", "Descrive la struttura molecolare esatta della sostanza, "
       "seguendo le norme internazionali IUPAC. Di solito è complesso, lungo e poco "
       "pratico per l'uso di tutti i giorni.",
       "<b>Esempio:</b> <i>N-(4-idrossifenil)acetammide</i>", "icon-formula")}
    {k("Nome generico (DCI)", "m", "", "È il nome ufficiale del principio attivo, cioè "
       "della sostanza isolata. È universale — riconosciuto in tutto il mondo — e non "
       "appartiene a nessun produttore specifico: è il nome usato in scienza e medicina.",
       "<b>Esempio:</b> paracetamolo", "icon-box-generic", "mint")}
    {k("Nome commerciale", "s", "", "È il nome registrato — il marchio di fantasia — "
       "scelto dal laboratorio produttore per scopi di marketing e vendita esclusiva.",
       "<b>Esempio:</b> Tylenol®", "icon-box-brand", "sky")}
  </div>
  {note("icon-idea", "Lo stesso farmaco, tre nomi",
        "Paracetamolo (generico) e Tylenol® (commerciale) contengono la stessa molecola: "
        "cambia solo il nome con cui la chiami.")}
</div>""", folio="11")

# ================================================================= pagina 12
P12 = shell(f"""
<img class="cutout" src="{A}/mascot-capsule.png" style="width:132px;right:26px;bottom:26px">
<div class="body">
  {head("3 · Nomenclatura", 'Classificazione dei <span class="p">medicinali</span>')}
  {row("lav", "icon-box-brand", "Riferimento",
       "Prodotto innovativo registrato presso l'AIFA. È il primo sul mercato, con "
       "efficacia, sicurezza e qualità comprovate scientificamente: serve da riferimento "
       "per tutti gli altri. Ha un marchio e un nome commerciale.")}
  {row("mint", "icon-box-generic", "Generico",
       "Medicinale intercambiabile con quello di riferimento, prodotto dopo la scadenza "
       "del brevetto. Non ha un marchio proprio — usa il nome del principio attivo — "
       "e ha un costo ridotto.")}
  {row("sky", "icon-box-equivalent", "Simile (equivalente)",
       "Contiene lo stesso principio attivo e le stesse caratteristiche del riferimento "
       "(concentrazione, forma e posologia), ma si differenzia perché è identificato da "
       "un nome commerciale proprio.", True)}
  {strip([("Riferimento", "prodotto di marca · nome commerciale"),
          ("Generico", "nome del principio attivo · confezione con la «G»"),
          ("Equivalente", "prodotto di marca · nome commerciale proprio")],
         "var(--mint-s)", "var(--mint)")}
  {note("icon-idea", "Perché costa meno",
        "Il generico non deve ripetere tutta la ricerca clinica del riferimento: deve "
        "solo dimostrare di essere bioequivalente, e questo ne abbassa il prezzo.")}
</div>""", folio="12")

# ================================================================= pagina 13
P13 = shell(f"""
<img class="cutout" src="{A}/avatar-wave.png" style="width:170px;right:-8px;top:96px">
<div class="body">
  {head("4 · Approcci terapeutici", 'Approcci <span class="p">terapeutici</span>')}
  <div class="panel lav" style="margin-top:14px">
    <span class="tag p">Allopatia</span>
    <div class="concl" style="margin-top:12px;padding-right:170px">Dal greco, si basa sul principio della
      <b>guarigione attraverso gli opposti</b>. Usa farmaci progettati per causare
      sull'organismo effetti opposti ai sintomi della malattia: se il corpo si scalda
      con la febbre, il medicinale agisce per raffreddarlo.</div>
    <div class="steps" style="margin-top:11px">
      <div class="s"><img src="{A}/icon-thermometer.png">
        <p>Febbre → antipiretico: il farmaco abbassa la temperatura.</p></div>
      <div class="s"><img src="{A}/icon-blister.png">
        <p>Infiammazione → antinfiammatorio: blocca il processo in corso.</p></div>
      <div class="s"><img src="{A}/icon-bottles.png">
        <p>Infezione → antibiotico: contrasta l'agente che l'ha causata.</p></div>
    </div>
    <div class="concl" style="background:var(--lav);margin-top:11px">Proprio per questo
      meccanismo di contrasto diretto, la maggior parte delle classi riceve il prefisso
      «<b>anti-</b>»: agiscono bloccando o invertendo il processo patologico.</div>
  </div>
  <div class="grid2" style="margin-top:13px">
    {k("Omeopatia", "m", "", "Opera nella logica opposta: «il simile cura il simile». "
       "Utilizza sostanze diluite e dinamizzate che, nelle persone sane, causerebbero "
       "gli stessi sintomi della malattia.", "", "", "mint", "icon-dropper")}
    {k("Fitoterapia", "s", "", "Usa medicinali di origine esclusivamente vegetale.",
       "<b>Nota:</b> i principi attivi isolati (per esempio caffeina pura o morfina) "
       "non sono fitoterapici: serve l'estratto grezzo o la pianta trasformata.",
       "", "sky", "icon-mortar")}
  </div>
</div>""", folio="13")

# ================================================================= pagina 14
P14 = shell(f"""
<img class="cutout" src="{A}/avatar-point.png" style="width:142px;right:14px;top:118px">
<div class="body">
  {head("5 · Vie di somministrazione", 'Vie di <span class="p">somministrazione</span>')}
  <div class="card" style="margin-top:14px;padding:22px 28px 22px 26px">
    <p style="padding-right:150px">Sono i <b>metodi di introduzione dei farmaci nel corpo</b>.
      La scelta dipende dalla natura del farmaco (solubilità, pH), dalle condizioni del
      paziente (coscienza, vomito) e dall'<b>urgenza dell'effetto</b>.</p>
  </div>
  {via("Via orale (VO)", "lav",
       [("icon-mouth", "Bocca"), ("icon-stomach", "Stomaco"),
        ("icon-liver", "Fegato"), ("icon-blood", "Sangue")],
       "Ingestione per via orale con assorbimento nel tratto gastrointestinale. "
       "È considerata la via <b>più sicura ed economica</b>.",
       ["<b>Farmacocinetica:</b> subisce l'<b>effetto di primo passaggio</b> "
        "(metabolismo epatico), che può ridurre significativamente la quantità di "
        "farmaco che raggiunge il sangue, cioè la biodisponibilità.",
        "<b>Limiti:</b> richiede un paziente cosciente e collaborante; vomito, cibo e "
        "pH gastrico possono modificare l'assorbimento."])}
  <div>
    <div class="toc-part" style="margin-top:0">Le vie che vedremo</div>
    <div class="gal">
      <div class="g"><img src="{A}/icon-mouth.png"><span>Orale</span></div>
      <div class="g"><img src="{A}/icon-tongue.png"><span>Sublinguale</span></div>
      <div class="g"><img src="{A}/icon-supposta.png"><span>Rettale</span></div>
      <div class="g"><img src="{A}/icon-iv.png"><span>Parenterale</span></div>
      <div class="g"><img src="{A}/icon-inhaler.png"><span>Inalatoria</span></div>
      <div class="g"><img src="{A}/icon-nose.png"><span>Intranasale</span></div>
      <div class="g"><img src="{A}/icon-eye.png"><span>Oculare e otica</span></div>
      <div class="g"><img src="{A}/icon-spine.png"><span>Epidurale</span></div>
    </div>
  </div>
  {note("icon-idea", "Da ricordare",
        "Più una via evita il fegato, più il farmaco arriva «intatto» al sangue: è il "
        "motivo per cui la via orale è comoda ma non sempre la più efficiente.")}
</div>""", folio="14")

# ================================================================= pagina 15
P15 = shell(f"""
<div class="body">
  {head("5 · Vie di somministrazione", 'Via <span class="p">sublinguale</span> e <span class="p">rettale</span>')}
  {via("Via sublinguale (SL) e buccale", "lav",
       [("icon-tongue", "Sotto la lingua"), ("icon-bloodflow", "Vena cava"),
        ("icon-blood", "Sangue")],
       "Il farmaco è posizionato sotto la lingua o tra guancia e gengiva. La ricca "
       "vascolarizzazione locale consente l'<b>assorbimento diretto</b> nella vena cava.",
       ["<b>Vantaggio:</b> azione rapida e nessun metabolismo di primo passaggio "
        "epatico — il farmaco arriva al sangue «intatto»."])}
  {via("Via rettale", "rose",
       [("icon-supposta", "Supposta"), ("icon-stomach", "Mucosa rettale"),
        ("icon-blood", "Sangue")],
       "Introduzione di supposte o clisteri, con assorbimento attraverso la mucosa rettale.",
       ["<b>Farmacocinetica:</b> il farmaco raggiunge la circolazione sistemica evitando "
        "circa il <b>50% del metabolismo di primo passaggio</b> epatico.",
        "<b>Indicazione:</b> utile in pazienti incoscienti, con nausea o vomito, e nei "
        "bambini che non riescono a deglutire.",
        "<b>Attenzione:</b> l'assorbimento può essere irregolare e incompleto."])}
</div>""", folio="15")

# ================================================================= pagina 16
P16 = shell(f"""
<img class="cutout" src="{A}/mascot-capsule.png" style="width:118px;right:24px;bottom:22px">
<div class="body">
  {head("5 · Vie di somministrazione", 'Via <span class="p">parenterale</span> e <span class="p">inalatoria</span>')}
  <div class="panel lav" style="margin-top:14px">
    <span class="tag p">Via parenterale (IV, IM, SC)</span>
    <div class="steps">
      <div class="s"><img src="{A}/icon-iv.png">
        <p><b>Endovenosa (IV)</b><br>Biodisponibilità del 100%: nessun assorbimento,
           il farmaco entra direttamente nel sangue. È la via dell'emergenza.</p></div>
      <div class="s"><img src="{A}/icon-im.png">
        <p><b>Intramuscolare (IM)</b><br>Consente volumi moderati e veicoli oleosi,
           con effetto deposito.</p></div>
      <div class="s"><img src="{A}/icon-skin.png">
        <p><b>Sottocutanea (SC)</b><br>Assorbimento lento e continuo, per esempio
           l'insulina.</p></div>
    </div>
    <div class="concl">Sono <b>vie iniettabili</b>: rompono la barriera cutanea, quindi
      richiedono sterilità e personale addestrato.</div>
  </div>
  {via("Via inalatoria", "rose",
       [("icon-inhaler", "Aerosol"), ("icon-lungs", "Alveoli"), ("icon-blood", "Sangue")],
       "Somministrazione di gas o aerosol nelle vie aeree (polmoni).",
       ["<b>Meccanismo:</b> l'ampia superficie degli alveoli permette un assorbimento "
        "molto rapido.",
        "Ampiamente usata per <b>effetti locali</b> — broncodilatatori nell'asma — "
        "minimizzando gli effetti collaterali sul resto del corpo."])}
</div>""", folio="16")

# ================================================================= pagina 17
P17 = shell(f"""
<div class="body">
  {head("5 · Vie di somministrazione", 'Via <span class="p">intranasale</span> e <span class="p">topica</span>')}
  {via("Via intranasale", "lav",
       [("icon-nose", "Mucosa nasale"), ("icon-brain", "SNC vicino"),
        ("icon-blood", "Sangue")],
       "Applicazione alla mucosa nasale.",
       ["<b>Utilizzo:</b> generalmente per <b>azione locale</b> (decongestionanti).",
        "Può però essere usata per <b>effetti sistemici</b> — per esempio la "
        "desmopressina — grazie al rapido assorbimento e alla vicinanza al sistema "
        "nervoso centrale."])}
  {via("Via topica", "rose",
       [("icon-ointment", "Pomata"), ("icon-skin", "Pelle o mucosa"),
        ("icon-target", "Effetto locale")],
       "Applicazione diretta sulla pelle o sulle mucose.",
       ["<b>Obiettivo:</b> cerca quasi sempre un <b>effetto locale</b> — "
        "antinfiammatori, antibiotici, protettori.",
        "Ha un basso assorbimento sistemico, quindi riduce le reazioni avverse nel "
        "resto del corpo."])}
</div>""", folio="17")

# ================================================================= pagina 18
P18 = shell(f"""
<img class="cutout" src="{A}/avatar-wave.png" style="width:158px;right:-6px;bottom:30px">
<div class="body">
  {head("5 · Vie di somministrazione", 'Via <span class="p">oculare</span> e <span class="p">otica</span>')}
  {via("Via oculare (oftalmica)", "lav",
       [("icon-dropper", "Collirio"), ("icon-eye", "Sacco congiuntivale"),
        ("icon-clock", "Contatto breve")],
       "Applicazione al sacco congiuntivale.",
       ["<b>Cura:</b> il preparato deve essere sterile, isotonico e con un pH adeguato, "
        "per non irritare la cornea.",
        "Il <b>tempo di contatto è breve</b>, per via dell'ammiccamento e delle lacrime."])}
  {via("Via otica", "rose",
       [("icon-dropper", "Gocce"), ("icon-ear", "Condotto uditivo"),
        ("icon-thermometer", "A temperatura")],
       "Instillazione nel condotto uditivo esterno.",
       ["<b>Funzione:</b> trattamento locale dell'otite o rimozione del cerume.",
        "Il liquido <b>non deve essere freddo</b>, per evitare vertigini al paziente."])}
  {note("icon-warning", "Attenzione", "Colliri e gocce otiche non sono intercambiabili: "
        "un preparato per l'orecchio non è sterile come deve esserlo un collirio.",
        "padding-right:170px")}
</div>""", folio="18")

PAGES = [P9, P10, P11, P12, P13, P14, P15, P16, P17, P18]

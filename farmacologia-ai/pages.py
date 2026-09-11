# -*- coding: utf-8 -*-
"""
Prompt di ogni pagina di "Farmacologia Illustrata".

PAGES[n] = (slug, prompt).  La pagina n corrisponde alla pagina n del PDF
originale (src/testo-originale.txt e src/orig/oNN.png).

Il testo italiano e' riscritto in italiano corretto: l'originale e' una
traduzione automatica dal portoghese piena di errori. Significato invariato.
"""

STYLE = (
    "Educational infographic page from an Italian pharmacology study book, vertical A4 "
    "page, clean white background, NO watermark, no logo, no page border. Soft pastel "
    "palette of lavender purple, mint green, sky blue and soft peach; rounded pill-shaped "
    "cards; cute flat vector illustrations with thin dark outlines inside white circles; "
    "bold black uppercase headings in a geometric sans-serif, with one word in purple. "
    "Small floating pastel capsules, tablets and molecules as decoration. "
    "Modern, clean, generous spacing, nothing cropped at the edges. "
    "Full-bleed page: the white background reaches all four edges, there is NO coloured "
    "frame, border, outer margin or panel around the page content. "
    "Reproduce every Italian text EXACTLY as written, with correct accents and "
    "apostrophes, perfect spelling, no invented words. Every single word on the page is "
    "in Italian: no English words anywhere, not even as small labels inside the "
    "illustrations or diagrams."
)

CHAR = ("A friendly 3D cartoon young man with dark brown wavy hair, warm skin, big brown "
        "eyes, a wide smile and a white polo shirt, cut out with no frame")

MASCOT = ("a cute cartoon mascot made of a lavender and white capsule pill with big "
          "friendly eyes, tiny arms and tiny legs, cut out with no frame")

PAGES = {

1: ("cover", f"""Book cover, vertical A4, clean off-white background. At the top, small
purple letterspaced caps: 'STUDIO FACILE'. Below, a huge two-line title: 'Farmacologia'
in deep purple bold, and under it 'illustrata' in teal green bold. Under the title a grey
subtitle: 'Didattica visiva, direttamente al punto'. In the middle, a circular portrait
badge with a white ring containing {CHAR}, smiling at the viewer. At the bottom of the
page, a wide pile of pastel pharmacy products: medicine bottles, pill jars, blister packs,
a microscope, a mortar and pestle, an apothecary flask, loose capsules and tablets. Large
soft pastel geometric shapes (a mint circle, a lavender rounded square, a blue circle) in
the background behind the title area. At the very bottom four small pastel pill-shaped
chips with the words: 'Fondamenti', 'Farmacocinetica', 'Farmacodinamica', 'Interazioni'.
{STYLE}"""),

2: ("avviso", f"""Vertical A4 page. Top left small purple letterspaced caps:
'PRIMA DI INIZIARE'. Big bold black two-line title: 'LEGGERE CON CURA' and
'E ATTENZIONE'. Under the title, on the left a lavender shield illustration with an
exclamation mark and a small padlock; on the right two lines of dark grey bold text:
'Materiale protetto da diritto d'autore.' and 'Licenza personale e non trasferibile.'
Below, a big white rounded card with a soft shadow containing: a bold heading
'Ehi, come stai?' then the paragraph 'Innanzitutto vogliamo ringraziarti per aver scelto
il nostro materiale. Prepariamo tutto con grande dedizione per supportare i tuoi studi.'
then the paragraph 'Ci auguriamo che questo strumento sia estremamente utile per
raggiungere i tuoi obiettivi. Buona fortuna e buono studio!' and inside it a pink rounded
box with a dashed pink border, a dark pink bold heading 'ATTENZIONE: AVVERTIMENTO
CRUCIALE' and the text 'Questo contenuto e per uso esclusivo e personale. La riproduzione,
la distribuzione o la vendita e severamente vietata.' At the bottom three small pastel
cards side by side, each with a small illustration and a bold uppercase title and one
line of text: a clipboard with 'STUDIA PER BLOCCHI', a magnifying glass over pills with
'SOLO L'ESSENZIALE', an open book with a stethoscope with 'RIPASSA IN FRETTA'.
{STYLE}"""),

3: ("sommario", f"""Vertical A4 page. Top left a clipboard with a checklist illustration
next to small purple letterspaced caps 'INDICE' and a big bold black title 'SOMMARIO'.
Below, two groups of rows. First a small purple uppercase label 'PARTE I - FONDAMENTI',
then nine light lavender and mint rounded rows, each with a small white circle holding the
number, the chapter name on the left and the page on the right, in this exact order:
'1 Concetti fondamentali - Pag. 05', '2 Forme farmaceutiche - Pag. 08',
'3 Nomenclatura - Pag. 11', '4 Approcci terapeutici - Pag. 13',
'5 Vie di somministrazione - Pag. 14', '6 Farmacocinetica - Pag. 21',
'7 Farmacodinamica - Pag. 34', '8 Farmacocinetica vs Farmacodinamica - Pag. 41',
'9 Tossicita e farmacogenomica - Pag. 42'. Then a small purple uppercase label
'PARTE II - INTERAZIONI CON I FARMACI' and eight more rows:
'10 Analgesici e antinfiammatori - Pag. 51', '11 Cardiovascolare - Pag. 57',
'12 Sistema nervoso centrale - Pag. 64', '13 Antimicrobici - Pag. 71',
'14 Endocrino - Pag. 77', '15 Gastrointestinale - Pag. 80', '16 Indice - Pag. 82',
'17 Riferimenti bibliografici - Pag. 83'. A small pastel molecule illustration in the top
right corner. {STYLE}"""),

4: ("parte1", f"""Vertical A4 chapter divider page, mostly white with two big soft pastel
blobs (lavender top left, mint bottom right). In the centre: a purple pill-shaped badge
with white letterspaced text 'PARTE I'; under it a huge bold deep purple title
'FONDAMENTI'; a short lavender divider line; a grey sentence 'I fondamenti che sostengono
la pratica clinica' with the word 'sostengono' in purple; then four small pastel chips in
a row with the words 'Concetti', 'Farmacocinetica', 'Farmacodinamica', 'Tossicita'. Below
them, a cute illustration of an open book with a stethoscope on it and a capsule floating
above. On the right side, {MASCOT}, waving. {STYLE}"""),

5: ("concetti", f"""Vertical A4 page. Top left small purple letterspaced caps
'1 - CONCETTI FONDAMENTALI'. Big bold black title 'CONCETTI DI BASE IN' with
'FARMACOLOGIA' in purple. Below, six pastel rounded pill-shaped cards stacked vertically,
alternating lavender, mint green and light blue. Each card has a white circle on the left
with a cute flat illustration, and on the right a bold black uppercase title and one
paragraph of Italian text, exactly:
Card 1, microscope, 'FARMACOLOGIA': 'La scienza che studia gli effetti dei farmaci
sull'organismo: origine, composizione, proprieta e meccanismo d'azione.'
Card 2, three medicine bottles, 'FARMACO': 'Sostanza chimica che puo alterare le funzioni
fisiologiche di un sistema biologico.'
Card 3, a molecule, 'PRINCIPIO ATTIVO': 'Sostanza chimica presente in un medicinale,
responsabile del suo effetto terapeutico.'
Card 4, a blister pack of pills, 'MEDICINALE': 'Prodotto farmaceutico elaborato,
contenente uno o piu farmaci, per prevenire o curare una malattia.'
Card 5, a mortar and pestle with herbs, 'RIMEDIO': 'Qualsiasi misura adottata per curare
una malattia o ridurne i sintomi.'
Card 6, a measuring beaker with a dosing spoon, 'DOSAGGIO': 'Determinazione della
quantita e degli orari di somministrazione di un medicinale.'
On the right side, overlapping the cards, {CHAR}, waving with one hand raised.
{STYLE}"""),

6: ("placebo", f"""Vertical A4 page. Top left small purple letterspaced caps
'1 - CONCETTI FONDAMENTALI'. Big bold black title 'EFFETTO PLACEBO' with 'E NOCEBO'
in purple. The page is divided into two sections, each introduced by a wide pill-shaped
banner with white bold uppercase text.
First banner, lavender purple: 'EFFETTO PLACEBO'. Under it three small rounded cards in
a vertical flow connected by thin curved dotted arrows, each card with a small flat
illustration on the left:
card A, light lavender, a person with a headache holding their head: 'Immagina di avere
mal di testa e che qualcuno ti dia una pillola dicendo che è un medicinale potente. La
prendi e, come per magia, il dolore scompare.'
card B, white with a lavender dashed border, a pill cut in half showing flour and sugar:
'Ma se ti dicessi che quella pillola era solo farina e zucchero, senza alcun principio
attivo?'
card C, mint green, a smiling brain with a heart: 'Questo è l'effetto placebo in azione:
ti senti meglio solo per la fiducia nel trattamento, anche se la sostanza è
biologicamente inattiva.'
Then a soft peach rounded box with a bold dark heading 'PERCHÉ È IMPORTANTE?' and the
text: 'Negli studi clinici esiste il gruppo placebo per dimostrare che il medicinale
funziona per la sua azione chimica e non solo per l'aspettativa del paziente.'
Second banner, soft coral pink: 'EFFETTO NOCEBO'. Under it two small rounded cards:
card D, light blue, a hand offering a pill with a warning triangle: 'Immagina di dare una
pillola di farina avvertendo: attenzione, ti farà venire mal di testa. Il paziente la
prende e il dolore compare davvero.'
card E, light lavender, a head with dark storm clouds and lightning: 'Questo è il nocebo,
l'opposto del placebo. L'aspettativa negativa spinge il corpo a creare sintomi reali,
anche senza una causa chimica.'
At the bottom a wide mint green rounded card with a lightbulb icon, a bold heading
'LEZIONE' and the text: 'Attenzione a come si comunica. Una paura eccessiva degli effetti
avversi può indurre il paziente a percepirli, anche se il medicinale è sicuro.'
{STYLE}"""),

7: ("potenza", f"""Vertical A4 page. Top left small purple letterspaced caps
'1 - CONCETTI FONDAMENTALI'. Big bold black title 'POTENZA' with 'ED EFFICACIA' in
purple. Below, four rounded cards arranged in a two by two grid, each with a small
pill-shaped label at the top holding a white bold uppercase word, a short definition and
a small pastel example box with a bold word 'Esempio' at the start.
Top left card, light blue, label 'POSOLOGIA', with a small illustration of a clock next
to a tablet: 'Modo e tempi di somministrazione del medicinale.' and in the example box:
'Esempio: 1 compressa di Paracetamolo 750 mg per via orale ogni 8 ore.' and under it in
bold purple caps: 'COME si usa'.
Top right card, lavender purple, label 'POTENZA', with a small illustration of a dumbbell
next to a capsule: 'Quantità di farmaco necessaria per produrre un determinato effetto.
Un farmaco più potente richiede una dose più piccola per ottenere lo stesso effetto di un
farmaco meno potente.' and in the example box: 'Esempio: il farmaco A allevia il dolore con 10 mg,
il farmaco B ne richiede 20 mg. Il farmaco A è più potente.'
Bottom left card, mint green, label 'MEDICINALE', with a small illustration of a medicine
box next to a blister pack: 'Prodotto farmaceutico con finalità terapeutica.' and in the
example box: 'Esempio: Paracetamolo 750 mg, compressa.' and under it in bold purple caps:
'COSA si usa'.
Bottom right card, soft peach, label 'EFFICACIA', with a small illustration of a rocket
with a burst of light: 'Quanto è grande l'effetto massimo prodotto dal farmaco quando
interagisce con il recettore.' and in the example box: 'Esempio: il farmaco A è un razzo
che produce una grande esplosione, il farmaco B un razzo più piccolo con un'esplosione
minore. Il farmaco A è più efficace.'
{MASCOT} peeking from the bottom right corner of the page. {STYLE}"""),

8: ("forme-solide", f"""Vertical A4 page. Top left small purple letterspaced caps
'2 - FORME FARMACEUTICHE'. Big bold black title 'FORME' with 'SOLIDE' in purple.
Under the title a wide light mint rounded banner with centred dark green text: 'Le
diverse forme fisiche in cui i farmaci vengono presentati, classificabili in solide,
liquide e semisolide.'
Below, five rounded cards stacked vertically, alternating lavender, mint green and light
blue, each with a white circle on the left holding a cute flat illustration, and on the
right a bold black uppercase title and one paragraph, exactly:
Card 1, a red and white capsule, 'CAPSULA': 'Preparazione solida in cui i farmaci sono
racchiusi in un involucro commestibile, comunemente amido o gelatina.'
Card 2, a round coated sugar-glazed tablet, 'CONFETTO': 'Compressa rivestita con sostanze
come zuccheri, cere, resine e gomme, che mascherano sapore e odore.'
Card 3, a small mound of white powder with a scoop, 'POLVERE': 'Principi attivi allo
stato secco e con particelle di dimensioni ridotte, con o senza eccipienti.'
Card 4, a round scored tablet under a press, 'COMPRESSA': 'Formulazione solida ottenuta
mediante compressione del farmaco e dei suoi eccipienti.'
Card 5, a bullet-shaped suppository, 'SUPPOSTA': 'Preparazione destinata agli orifizi
rettale, vaginale o uretrale, progettata per sciogliersi alla temperatura corporea.'
At the bottom a soft peach rounded box with a dashed border, a small beaker illustration,
a bold heading 'CHE COS'È UN ECCIPIENTE?' and the text: 'Sostanza inerte aggiunta al
medicinale per dare volume e forma adeguata e facilitarne la somministrazione, senza
esercitare effetti farmacologici propri.' {STYLE}"""),

9: ("forme-liquide", f"""Vertical A4 page. Top left small purple letterspaced caps
'2 - FORME FARMACEUTICHE'. Big bold black title 'FORME' with 'LIQUIDE' in purple.
Below, four rounded cards stacked vertically, each with a white circle on the left
holding a cute flat illustration and on the right a bold black uppercase title and one
paragraph, exactly:
Card 1, light blue, a clear glass bottle with a dropper, 'SOLUZIONE': 'Formulazione
limpida e omogenea, monofase, con i principi attivi completamente disciolti nel
solvente.'
Card 2, lavender, a bottle of thick syrup with a dosing cup, 'SCIROPPO': 'Soluzione di
consistenza viscosa, preparata con un'alta concentrazione di zuccheri o di agenti
addensanti.'
Card 3, mint green, a small apothecary flask, 'ELISIR': 'Soluzione idroalcolica, acqua
più alcol, con viscosità inferiore allo sciroppo e sapore dolce.'
Card 4, soft peach, a bottle with floating solid particles and a shake icon,
'SOSPENSIONE': 'Forma liquida in cui particelle solide restano disperse, senza sciogliersi
nel liquido: un sistema eterogeneo.'
Under the cards a wide lavender rounded section with a bold black heading 'EMULSIONE' and
the text: 'È composta da due liquidi che non si mescolano, immiscibili come acqua e olio,
in cui uno è disperso in gocce dentro l'altro.' Inside it two small white cards side by
side, each with a simple diagram of a beaker with droplets: the left one titled
'OLIO IN ACQUA (O/A)' with gocce di olio disperse in acqua, the right one titled
'ACQUA IN OLIO (A/O)' with gocce di acqua disperse in olio. Under them three short lines
with small coloured dots: 'Fase interna: è la fase dispersa, le goccioline.',
'Fase esterna: è la fase continua che circonda le gocce.', 'Emulsionante: agente
utilizzato per mantenere stabile la miscela.' {STYLE}"""),

10: ("semisolide", f"""Vertical A4 page. Top left small purple letterspaced caps
'2 - FORME FARMACEUTICHE'. Big bold black title 'FORME SEMISOLIDE' with 'E CEROTTI' in
purple. Below, three rounded cards stacked vertically, each with a white circle on the
left holding a cute flat illustration and on the right a bold black uppercase title and
one paragraph, exactly:
Card 1, mint green, a jar of white cream, 'CREMA': 'Preparazione di consistenza
semisolida composta da un'emulsione con fase acquosa e fase oleosa, generalmente per
applicazione esterna e topica.'
Card 2, lavender, a squeezed tube of ointment, 'UNGUENTO': 'Preparato per pelle o mucose,
con base generalmente non acquosa, grassa e lipofila, che contiene principi attivi
disciolti o dispersi in basse concentrazioni.'
Card 3, light blue, a tube of transparent gel, 'GEL': 'Forma semisolida composta da un
agente gelificante, per esempio polimeri, che conferisce consistenza a una soluzione o a
una dispersione colloidale.'
Between card 2 and card 3 a small soft peach note with a dashed border and the text:
'A differenza della crema, che contiene acqua, l'unguento è più oleoso e occlusivo.'
Under the cards a white rounded box with a lavender border, a bold heading
'CHE COS'È LA DISPERSIONE COLLOIDALE?' and the text: 'Il sistema in cui particelle molto
piccole, tra 1 nm e 1 micrometro, sono distribuite uniformemente in un liquido senza
precipitare, formando la struttura del gel.'
At the bottom a wide mint green rounded section with a bold black heading
'CEROTTO TRANSDERMICO', a clear illustration of a square patch on an arm with three
arrows crossing the layers of the skin down to a blood vessel, and two short lines of
text: 'Il farmaco attraversa gli strati del derma fino al flusso sanguigno e si
distribuisce in tutto il corpo, con effetto sistemico.' and 'Il rilascio è costante e
prolungato: mantiene stabile il livello del farmaco nel sangue, senza oscillazioni.'
{STYLE}"""),

11: ("nomenclatura", f"""Vertical A4 page. Top left small purple letterspaced caps
'3 - NOMENCLATURA'. Big bold black title 'I NOMI DI UN' with 'MEDICINALE' in purple.
Below, three wide rounded cards stacked vertically, each split in two: on the left a bold
black uppercase title and one paragraph, on the right a small white box with a bold word
'Esempio:' and the example, exactly:
Card 1, light blue, title 'NOME CHIMICO': 'Descrive l'esatta struttura molecolare della
sostanza, secondo le norme internazionali IUPAC. Di solito è complesso, lungo e poco
pratico per l'uso quotidiano.' Example box: 'Esempio: N-(4-idrossifenil)acetammide' with
under it a simple drawn skeletal chemical structure of paracetamol.
Card 2, mint green, title 'NOME GENERICO (DCI)': 'È il nome ufficiale del principio
attivo, la sostanza isolata. È universale, riconosciuto in tutto il mondo, e non
appartiene a nessun produttore. È il nome usato in ambito scientifico e medico.' Example
box: 'Esempio: paracetamolo' with under it a plain white unbranded medicine box.
Card 3, lavender purple, title 'NOME COMMERCIALE': 'È il nome registrato, un marchio di
fantasia scelto dal laboratorio produttore per scopi di marketing e vendita esclusiva.'
Example box: 'Esempio: Tylenol' followed by a small registered trademark symbol, with
under it a colourful branded medicine box.
{MASCOT} standing at the bottom left, holding a small name tag. {STYLE}"""),

12: ("classificazione", f"""Vertical A4 page. Top left small purple letterspaced caps
'3 - NOMENCLATURA'. Big bold black title 'CLASSIFICAZIONE DEI' with 'MEDICINALI' in
purple. Below, three big rounded cards stacked vertically, each with a wide pill-shaped
label at the top holding a white bold uppercase word, a cute flat illustration of a
medicine box on the left and one paragraph of text on the right, exactly:
Card 1, lavender purple, label 'RIFERIMENTO', illustration of a branded medicine box with
a small gold star: 'Prodotto innovatore registrato presso l'AIFA. È il primo sul mercato,
con efficacia, sicurezza e qualità comprovate scientificamente, e fa da riferimento per
gli altri.'
Card 2, mint green, label 'GENERICO', illustration of a plain white medicine box with a
price tag: 'Medicinale intercambiabile con quello di riferimento, prodotto dopo la
scadenza del brevetto. Non ha un marchio proprio, usa il nome del principio attivo, e ha
un costo inferiore.'
Card 3, light blue, label 'SIMILE', illustration of a medicine box with a fancy brand
name: 'Contiene lo stesso principio attivo e le stesse caratteristiche del riferimento,
cioè concentrazione, forma e posologia, ma si distingue perché è identificato da un nome
commerciale proprio.'
On the right side, overlapping the cards, {CHAR}, pointing with one hand towards the
cards. {STYLE}"""),

13: ("approcci", f"""Vertical A4 page. Top left small purple letterspaced caps
'4 - APPROCCI TERAPEUTICI'. Big bold black title 'APPROCCI' with 'TERAPEUTICI' in purple.
Below, three rounded cards stacked vertically, each with a white circle on the left
holding a cute flat illustration and on the right a bold black uppercase title and one
paragraph, exactly:
Card 1, lavender purple, a thermometer next to a snowflake, 'ALLOPATIA': 'Dal greco, si
basa sul principio della guarigione attraverso gli opposti. Usa farmaci che provocano
nell'organismo effetti contrari ai sintomi della malattia: se il corpo si scalda con la
febbre, il medicinale agisce per raffreddarlo.'
Card 2, mint green, two identical small flasks facing each other, 'OMEOPATIA': 'Segue la
logica opposta: il simile cura il simile. Utilizza sostanze diluite e dinamizzate che, in
una persona sana, provocherebbero gli stessi sintomi della malattia da curare.'
Card 3, light blue, a leaf with a mortar and pestle, 'FITOTERAPIA': 'Utilizza medicinali
di origine esclusivamente vegetale.'
Under card 1 a small soft peach note with a dashed border: 'Per questo meccanismo di
contrasto diretto la maggior parte delle classi riceve il prefisso anti: antibiotici,
antipiretici e antinfiammatori, che bloccano o invertono il processo patologico.'
At the bottom a white rounded box with a lavender dashed border, a small warning icon, a
bold heading 'NOTA' and the text: 'I principi attivi isolati, per esempio la caffeina
pura o la morfina, non sono fitoterapici. Per esserlo, il prodotto deve contenere
l'estratto grezzo o la pianta lavorata.' {STYLE}"""),

14: ("vie-orale", f"""Vertical A4 page. Top left small purple letterspaced caps
'5 - VIE DI SOMMINISTRAZIONE'. Big bold black title 'VIE DI SOMMINISTRAZIONE' with
'DEI MEDICINALI' in purple. Under the title a wide light blue rounded card with a small
illustration of a human body silhouette surrounded by small icons of a mouth, an eye, an
ear, a nose, a lung and a syringe, and the text: 'Sono i metodi con cui i farmaci vengono
introdotti nell'organismo. La scelta dipende dalla natura del farmaco (solubilità, pH),
dalle condizioni del paziente (stato di coscienza, vomito) e dall'urgenza dell'effetto.'
Below, one wide lavender rounded section introduced by a purple pill-shaped banner with
white bold uppercase text 'VIA ORALE (VO)'. Inside the section, first a horizontal flow
of four cute flat illustrations joined by arrows, each with a small bold Italian
caption underneath reading exactly 'Bocca', 'Stomaco e intestino', 'Fegato',
'Sangue': an open mouth, a stomach with intestines, a liver, a red blood drop. Under the flow, the text: 'Ingestione per bocca,
con assorbimento nel tratto gastrointestinale. È considerata la via più sicura ed
economica.' Then a white rounded box with a bold heading 'FARMACOCINETICA' and the text:
'Subisce l'effetto di primo passaggio epatico, cioè il metabolismo nel fegato, che può
ridurre in modo significativo la quantità di farmaco che raggiunge il sangue, cioè la
biodisponibilità.'
On the right side of the header, {CHAR}, pointing towards the title. {STYLE}"""),

15: ("vie-sl-rettale", f"""Vertical A4 page. Top left small purple letterspaced caps
'5 - VIE DI SOMMINISTRAZIONE'. Big bold black title 'VIA SUBLINGUALE' with 'E RETTALE' in
purple. Below, two wide rounded sections stacked vertically, each introduced by a
pill-shaped banner with white bold uppercase text.
First section, mint green, banner 'VIA SUBLINGUALE E BUCCALE'. Inside: a cute flat
illustration of a tablet placed under a tongue, next to the text: 'Il farmaco viene posto
sotto la lingua o tra guancia e gengiva. La ricca vascolarizzazione locale permette
l'assorbimento diretto nella circolazione sistemica.' Then a white rounded box with a bold
heading 'VANTAGGIO' and the text: 'Azione rapida. Il farmaco non subisce il metabolismo di
primo passaggio epatico e arriva al sangue intatto.'
Second section, lavender purple, banner 'VIA RETTALE'. Inside: a cute flat illustration of
a suppository next to a rectal outline, and the text: 'Introduzione di supposte o clisteri,
con assorbimento attraverso la mucosa rettale.' Then two white rounded boxes: the first
with a bold heading 'FARMACOCINETICA' and the text: 'Il farmaco raggiunge la circolazione
sistemica evitando circa il 50% del metabolismo di primo passaggio epatico.'; the second
with a bold heading 'INDICAZIONE' and the text: 'Utile nei pazienti incoscienti, con nausea
o vomito, e nei bambini che non riescono a deglutire. L'assorbimento può essere irregolare
e incompleto.' {STYLE}"""),

16: ("vie-parenterale", f"""Vertical A4 page. Top left small purple letterspaced caps
'5 - VIE DI SOMMINISTRAZIONE'. Big bold black title 'VIA PARENTERALE' with 'E INALATORIA'
in purple. Below, two wide rounded sections stacked vertically, each introduced by a
pill-shaped banner with white bold uppercase text.
First section, light blue, banner 'VIA PARENTERALE (IV, IM, SC)'. Inside, the line: 'Vie
iniettabili: attraversano la barriera cutanea.' Then three small white rounded rows, each
with a tiny illustration of a syringe on the left, a bold black uppercase title and one
line of text: row 1 with a syringe entering a vein, 'ENDOVENOSA (IV)': 'Biodisponibilità
del 100%. Non c'è assorbimento: il farmaco arriva direttamente nel sangue. Si usa nelle
emergenze.'; row 2 with a syringe entering a muscle, 'INTRAMUSCOLARE (IM)': 'Consente
volumi moderati e veicoli oleosi, con effetto deposito.'; row 3 with a syringe entering a
skin fold, 'SOTTOCUTANEA (SC)': 'Assorbimento lento e continuo, per esempio l'insulina.'
Second section, mint green, banner 'VIA INALATORIA'. Inside: a horizontal flow of three
cute flat illustrations joined by arrows, an inhaler, a pair of lungs with alveoli, a red
blood drop. Under it the text: 'Somministrazione di gas o aerosol nelle vie aeree fino ai
polmoni.' Then a white rounded box with a bold heading 'MECCANISMO' and the text: 'L'ampia
superficie degli alveoli permette un assorbimento rapido. Molto usata per effetti locali,
come i broncodilatatori nell'asma, riducendo gli effetti collaterali sul resto del corpo.'
{STYLE}"""),

17: ("vie-nasale-topica", f"""Vertical A4 page. Top left small purple letterspaced caps
'5 - VIE DI SOMMINISTRAZIONE'. Big bold black title 'VIA INTRANASALE' with 'E TOPICA' in
purple. Below, two wide rounded sections stacked vertically, each introduced by a
pill-shaped banner with white bold uppercase text.
First section, lavender purple, banner 'VIA INTRANASALE'. Inside: a horizontal flow of
three cute flat illustrations joined by arrows, a nasal spray bottle, a nose in
cross-section, a brain. Under it the text: 'Applicazione sulla mucosa nasale.' Then a
white rounded box with a bold heading 'UTILIZZO' and the text: 'Generalmente per un'azione
locale, come i decongestionanti, ma può servire anche per effetti sistemici, per esempio
la desmopressina, grazie al rapido assorbimento e alla vicinanza al sistema nervoso
centrale.'
Second section, soft peach, banner 'VIA TOPICA'. Inside: a horizontal flow of three cute
flat illustrations joined by arrows, a tube of cream, a cross-section of skin with cream
on top, a target symbol. Under it the text: 'Applicazione diretta sulla pelle o sulle
mucose.' Then a white rounded box with a bold heading 'OBIETTIVO' and the text: 'Cerca
quasi sempre un effetto locale, con antinfiammatori, antibiotici o protettivi, e un basso
assorbimento sistemico, riducendo le reazioni avverse nel resto del corpo.'
{MASCOT} standing at the bottom right corner. {STYLE}"""),

18: ("vie-oculare-otica", f"""Vertical A4 page. Top left small purple letterspaced caps
'5 - VIE DI SOMMINISTRAZIONE'. Big bold black title 'VIA OCULARE' with 'E OTICA' in
purple. Below, two wide rounded sections stacked vertically, each introduced by a
pill-shaped banner with white bold uppercase text.
First section, light blue, banner 'VIA OCULARE (OFTALMICA)'. Inside: a cute flat
illustration of an eye with a dropper releasing a drop into the lower eyelid, next to the
text: 'Applicazione nel sacco congiuntivale.' Then a white rounded box with a bold heading
'ATTENZIONE' and the text: 'La preparazione deve essere sterile, isotonica e con un pH
adeguato per non irritare la cornea. Il tempo di contatto è breve a causa
dell'ammiccamento e della lacrimazione.'
Second section, mint green, banner 'VIA OTICA'. Inside: a cute flat illustration of an ear
with a dropper above it, next to the text: 'Instillazione nel condotto uditivo esterno.'
Then a white rounded box with a bold heading 'FUNZIONE' and the text: 'Trattamento locale
dell'otite o rimozione del cerume. Il liquido non deve essere freddo, per evitare vertigini
al paziente.' {STYLE}"""),

19: ("vie-spinale-id", f"""Vertical A4 page. Top left small purple letterspaced caps
'5 - VIE DI SOMMINISTRAZIONE'. Big bold black title 'VIA EPIDURALE,' with
'INTRATECALE E INTRADERMICA' in purple. Below, two wide rounded sections stacked
vertically, each introduced by a pill-shaped banner with white bold uppercase text.
First section, lavender purple, banner 'VIA EPIDURALE E INTRATECALE'. Inside: a clear
cross-section diagram of the lumbar spine with two needles, and four thin label lines with
small pastel tags reading exactly 'Midollo spinale', 'Vertebra', 'Spazio epidurale',
'Spazio subaracnoideo'. Under it the line: 'Vie di accesso al sistema nervoso centrale
attraverso la colonna vertebrale.' Then two white rounded boxes: the first with a bold
heading 'INTRATECALE' and the text: 'Il farmaco entra direttamente nel liquido
cerebrospinale, nello spazio subaracnoideo. Si usa quando serve un'azione rapida e in
trattamenti specifici, per esempio nella meningite.'; the second with a bold heading
'EPIDURALE' and the text: 'L'applicazione avviene nello spazio epidurale, all'esterno
della dura madre. Molto comune durante il parto, per un sollievo dal dolore prolungato
tramite catetere.'
Second section, soft peach, banner 'VIA INTRADERMICA (ID)'. Inside: a clear cross-section
diagram of the skin with a needle entering at a shallow angle and four small pastel label
tags reading exactly 'Epidermide', 'Derma', 'Tessuto sottocutaneo', 'Muscolo'. Under it
the line: 'Iniezione nel derma, lo strato superficiale, con formazione di una papula.'
Then a white rounded box with a bold heading 'UTILIZZO' and the text: 'Quasi
esclusivamente diagnostico, con test allergici e PPD, e per vaccini specifici come il BCG,
perché l'assorbimento è molto lento.' {STYLE}"""),

20: ("percorso-farmaco", f"""Vertical A4 page. Top left small purple letterspaced caps
'5 - VIE DI SOMMINISTRAZIONE'. Big bold black title 'IL PERCORSO' with 'DEL FARMACO' in
purple. Under the title three short stacked rounded cards: the first light blue: 
'L'assorbimento è il passaggio del farmaco dalla sede di somministrazione al plasma
sanguigno. È una tappa obbligata perché il medicinale raggiunga il suo bersaglio.'; the
second lavender: 'L'eccezione è la via endovenosa: il farmaco viene iniettato direttamente
nel flusso sanguigno, quindi l'assorbimento è completo e immediato, il 100%.'; the third
mint green: 'Nota: nei casi di effetto locale, come pomate e spray, l'obiettivo è agire sul
tessuto, senza bisogno di raggiungere il plasma.'
Below, occupying the lower two thirds of the page, a clean flow diagram on a white
background divided into three vertical columns by thin dividers, with a coloured header
strip above each column holding bold uppercase text: left column light blue
'SOMMINISTRAZIONE', centre column mint green 'ASSORBIMENTO E DISTRIBUZIONE', right column
soft peach 'ELIMINAZIONE'.
In the centre of the middle column a big green rounded oval with bold white text 'PLASMA'.
The left column is a vertical list of small light blue rounded tags reading exactly, from
top to bottom: 'Orale o rettale', 'Percutanea', 'Endovenosa', 'Intramuscolare',
'Intratecale', 'Inalazione'. Each tag has a thin orange arrow pointing right towards a
small peach tag in the middle column, reading in the same order: 'Intestino', 'Pelle',
then a direct arrow with no tag, 'Muscolo', 'Liquido cerebrospinale', 'Polmone'. All these
peach tags have arrows pointing to the central 'PLASMA' oval.
Above the PLASMA oval, a small peach tag 'Fegato' connected to it by an arrow labelled
'Sistema porta', with a further arrow up to a small tag 'Bile' and one to the right to a
tag 'Metaboliti'. Below the PLASMA oval, small peach tags 'Cervello', 'Placenta' and
'Feto' connected by arrows, and to the right of the oval a peach tag 'Ghiandole mammarie e
sudoripare'.
In the right column, small pastel tags reading exactly, from top to bottom: 'Urina',
'Feci', 'Latte e sudore', 'Aria espirata', each reached by an orange arrow from the middle
column.
Under the diagram, a small italic grey caption: 'Fonte: elaborazione propria, adattata da
Rang & Dale, Pharmacology, 8a ed.' {STYLE}"""),

21: ("farmacocinetica", f"""Vertical A4 page. Top left small purple letterspaced caps
'6 - FARMACOCINETICA'. Big bold black title 'FARMACO' with 'CINETICA' in purple, and under
it a small grey line: 'farmaco + movimento'. Below, a light blue rounded card with the
text: 'È l'area che studia il percorso e il destino del farmaco nell'organismo. In sintesi:
che cosa fa l'organismo al farmaco nel tempo.'
Next, a lavender rounded section with a bold black heading 'LE QUATTRO FASI: ADME' and four
small white rounded chips in a row, each with a tiny illustration and a bold label reading
exactly '1. Assorbimento', '2. Distribuzione', '3. Metabolismo', '4. Escrezione', and under
the third chip a small grey word in brackets: '(biotrasformazione)'.
Next, a mint green rounded section with a bold black heading 'ASSORBIMENTO' and the text:
'È il passaggio del farmaco dalla sede di somministrazione fino al flusso sanguigno, cioè
la circolazione sistemica.' Inside it a horizontal flow of three cute flat illustrations
joined by arrows with small labels under them reading exactly 'Somministrazione',
'Assorbimento', 'Circolazione sanguigna': a hand giving a tablet to a mouth, an intestinal
wall with molecules crossing it, a body silhouette with blood vessels.
Next, a soft peach rounded section with a bold black heading 'DA CHE COSA DIPENDE?' and
three short lines with small coloured dots: 'Via di somministrazione: la via endovenosa non
ha assorbimento.', 'Proprietà del farmaco: liposolubilità e dimensione della molecola.',
'Condizioni del sito: pH, flusso sanguigno e superficie di contatto.'
At the bottom a wide lavender rounded card with a bold black heading 'BIODISPONIBILITÀ' and
the text: 'È la frazione, in percentuale, della dose somministrata che raggiunge
immodificata la circolazione sistemica ed è disponibile per produrre l'effetto.'
{STYLE}"""),

22: ("assorbimento-1", f"""Vertical A4 page. Top left small purple letterspaced caps
'6 - FARMACOCINETICA'. Big bold black title 'MECCANISMI DI' with 'ASSORBIMENTO' in purple.
Under the title a light blue rounded card with the text: 'Per raggiungere la circolazione
il farmaco deve attraversare le membrane biologiche. Il trasporto dipende dalle proprietà
della molecola e non sempre richiede un dispendio di energia (ATP).'
Below, two wide rounded sections stacked vertically, each introduced by a pill-shaped
banner with white bold uppercase text.
First section, lavender purple, banner 'DIFFUSIONE PASSIVA'. Inside: the text 'È il
meccanismo più comune. Avviene a favore del gradiente di concentrazione: la molecola si
sposta dall'ambiente più concentrato a quello meno concentrato.' next to a clear diagram of
a cell membrane lipid bilayer with small round drug molecules crossing it downwards, and a
big triangle beside it, wide at the top and narrow at the bottom, with the label 'Più
concentrato' at the top and 'Meno concentrato' at the bottom. Then two short lines with
small coloured dots: 'Liposolubile: attraversa liberamente la matrice lipidica della
membrana.' and 'Idrosolubile: le molecole piccole passano attraverso i pori acquosi.'
Second section, mint green, banner 'DIFFUSIONE FACILITATA'. Inside: a clear diagram of a
membrane with a green carrier protein channel, small drug molecules binding to it and
being released on the other side, with exactly two small Italian labels inside the diagram, 'Farmaco' and
'Trasportatore', and no legend row or extra tags underneath it. Next to it the text: 'Avviene quando il farmaco è troppo grande o troppo
polare per passare da solo e ha bisogno di un passaggio dedicato.' Then two white rounded
boxes with short texts: 'La molecola entra nella cellula con l'aiuto di proteine
trasportatrici, situate in punti specifici della membrana. Il farmaco si lega alla
proteina, che cambia forma e rilascia la sostanza dentro la cellula.' and 'Pur usando un
aiuto non consuma energia, perché segue comunque il gradiente di concentrazione.'
{STYLE}"""),

23: ("assorbimento-2", f"""Vertical A4 page. Top left small purple letterspaced caps
'6 - FARMACOCINETICA'. Big bold black title 'TRASPORTO ATTIVO' with 'E PINOCITOSI' in
purple. Below, two wide rounded sections stacked vertically, each introduced by a
pill-shaped banner with white bold uppercase text.
First section, soft peach, banner 'TRASPORTO ATTIVO'. Inside: a clear diagram of a cell
membrane with an orange carrier protein pumping small drug molecules upwards against the
gradient, with the small Italian labels 'ATP' and 'ADP' next to the protein. Next to the
diagram three short lines with small coloured dots: 'A differenza della diffusione, questo
processo ha bisogno di energia per avvenire.', 'Sposta le molecole dall'ambiente meno
concentrato a quello più concentrato, cioè contro gradiente.', 'Richiede l'idrolisi
dell'ATP per attivare le proteine trasportatrici.' Then a white rounded box with the text:
'Le proteine sono specifiche: per essere trasportati, i farmaci devono avere una
somiglianza strutturale con le sostanze naturali dell'organismo, il cosiddetto mimetismo
molecolare.'
Second section, light blue, banner 'PINOCITOSI (ENDOCITOSI)'. Inside: a clear diagram of a
cell membrane wrapping around a big irregular green molecule labelled in Italian 'Farmaco
grande' and forming a vesicle inside the cell. Next to it the text: 'Meccanismo usato per
trasportare farmaci con molecole grandi, le macromolecole, che non passano attraverso pori
o canali.' Then two white rounded boxes with short texts: 'La membrana cellulare circonda
la molecola e si invagina verso l'interno.' and 'Il farmaco viene interiorizzato in una
piccola sacca, la vescicola, che viene poi rilasciata dentro la cellula.' {STYLE}"""),

24: ("fattori-assorbimento", f"""Vertical A4 page. Top left small purple letterspaced caps
'6 - FARMACOCINETICA'. Big bold black title 'FATTORI CHE INFLUENZANO' with 'L'ASSORBIMENTO'
in purple. Under the title a light blue rounded card with the text: 'La velocità e la
quantità di farmaco assorbito non dipendono solo dalla via di somministrazione, ma anche
dalle caratteristiche fisiologiche e chimico-fisiche del sito.'
Below, four rounded cards, each with a small pill-shaped label at the top holding a white
bold uppercase title, a small cute flat illustration and short lines of text.
Card 1, mint green, label 'FLUSSO SANGUIGNO', illustration of a blood vessel with a red
arrow: 'Il sangue funziona come un camion da trasporto: porta via il farmaco assorbito e
mantiene favorevole il gradiente di concentrazione.' plus two short bullet lines:
'L'intestino tenue è molto più vascolarizzato dello stomaco.' and 'Più flusso di sangue
significa assorbimento più rapido ed efficiente.'
Card 2, lavender purple, label 'AREA DI CONTATTO', illustration of intestinal villi:
'Più grande è l'area, maggiore è l'assorbimento.' plus two short bullet lines: 'Esempio:
l'intestino.' and 'Grazie ai microvilli la superficie di assorbimento dell'intestino è
circa 1000 volte maggiore di quella dello stomaco.'
Card 3, soft peach, label 'TEMPO DI CONTATTO', illustration of a clock: 'Il farmaco deve
restare abbastanza a lungo sulla superficie assorbente.' plus two short bullet lines:
'Transito accelerato, per esempio la diarrea: assorbimento incompleto.' and 'Svuotamento
gastrico lento: l'inizio dell'effetto ritarda.'
Card 4, light blue, label 'pH E IONIZZAZIONE', illustration of a pH colour strip and a
water drop: 'La maggior parte dei farmaci sono acidi o basi deboli e si trovano in
equilibrio tra due forme.' plus one line with a green check mark: 'Forma non ionizzata, non
polare: è liposolubile e attraversa facilmente le membrane.' and one line with a red cross:
'Forma ionizzata, polare: è idrosolubile, ma non attraversa bene le membrane.' Under them a
white rounded box with the bold text 'Per essere ben assorbito il farmaco deve trovarsi
prevalentemente nella forma NON ionizzata.' and two short lines: 'Acido in ambiente acido:
resta non ionizzato e si assorbe bene.' and 'Base in ambiente basico: resta non ionizzata e
si assorbe bene.' {STYLE}"""),

25: ("distribuzione", f"""Vertical A4 page. Top left small purple letterspaced caps
'6 - FARMACOCINETICA'. Big bold black title 'DISTRI' with 'BUZIONE' in purple. Under the
title a light blue rounded card with the text: 'Dopo l'assorbimento il farmaco lascia il
flusso sanguigno e viene trasportato nei liquidi interstiziale e intracellulare, cioè nei
tessuti.'
Below, two wide rounded sections stacked vertically, each introduced by a pill-shaped
banner with white bold uppercase text.
First section, mint green, banner '1. PERMEABILITÀ DEI CAPILLARI'. Inside the line: 'È la
capacità del farmaco di attraversare l'endotelio del vaso e cambia da organo a organo,
secondo l'anatomia del capillare.' Then two white rounded boxes side by side, each with a
small diagram of a capillary: the left one with a bold heading 'ALTA PERMEABILITÀ' and the
text 'Fegato e milza: hanno capillari fenestrati, con ampie aperture che lasciano passare
facilmente le sostanze.'; the right one with a bold heading 'BASSA PERMEABILITÀ' and the
text 'Cervello: ha la barriera ematoencefalica, con giunzioni serrate. Per entrare il
farmaco deve essere molto liposolubile o usare trasportatori specifici.'
Second section, lavender purple, banner '2. LEGAME CON LE PROTEINE PLASMATICHE'. Inside the
line: 'Nel sangue il farmaco si distribuisce in due forme, in equilibrio dinamico.' Then two
white rounded boxes: the first with a bold heading 'A) FRAZIONE LEGATA (DEPOSITO)' and the
text 'Il farmaco si lega alle proteine e resta intrappolato nel sangue: non attraversa le
membrane e non ha effetto farmacologico immediato. L'albumina lega soprattutto i farmaci
acidi, l'alfa-1-glicoproteina acida quelli basici.'; the second with a bold heading
'B) FRAZIONE LIBERA (ATTIVA)' and the text 'È l'unica che attraversa l'endotelio, raggiunge
il tessuto bersaglio ed esercita l'effetto terapeutico.' Under them a soft peach rounded
box with a bold heading 'EQUILIBRIO' and the text: 'Man mano che la forma libera passa dal
sangue ai tessuti, una parte si stacca dalle proteine per ricostituire la scorta di farmaco
libero nel plasma.'
On the right side of the page header, {CHAR}, smiling. {STYLE}"""),

26: ("volume-barriere", f"""Vertical A4 page. Top left small purple letterspaced caps
'6 - FARMACOCINETICA'. Big bold black title 'VOLUME DI DISTRIBUZIONE' with
'E BARRIERE' in purple. Below, two wide rounded sections stacked vertically, each
introduced by a pill-shaped banner with white bold uppercase text.
First section, light blue, banner 'VOLUME DI DISTRIBUZIONE APPARENTE (Vd)'. Inside the
text: 'È un parametro teorico che mette in relazione la quantità di farmaco presente nel
corpo con la sua concentrazione nel sangue.' Then a small white note with a lightbulb icon:
'Il Vd indica quanto al farmaco piace lasciare il sangue e diffondersi nei tessuti.' Then a
short line: 'Perché apparente? Perché il corpo non è un unico secchio: il valore calcolato
è ipotetico e serve a capire dove si concentra il farmaco.' Then two white rounded boxes
side by side: the left with a bold heading 'Vd BASSO' and the text 'Il farmaco resta
intrappolato nel sangue. In genere farmaci grandi, idrosolubili o molto legati alle
proteine plasmatiche, per esempio il warfarin.'; the right with a bold heading 'Vd ALTO'
and the text 'Il farmaco lascia il sangue e si accumula nei tessuti, come muscolo e grasso.
In genere farmaci piccoli e liposolubili, per esempio la clorochina.'
Second section, lavender purple, banner 'BARRIERE BIOLOGICHE'. Inside two white rounded
cards side by side, each with a small cute flat illustration at the top. Left card, a brain
with a brick wall in front of it, bold heading 'BARRIERA EMATOENCEFALICA (BEE)': 'Una difesa
formata da cellule endoteliali unite da giunzioni serrate. Impedisce l'ingresso di sostanze
nocive e polari nel sistema nervoso centrale. Passano solo i farmaci molto liposolubili o
quelli che usano trasportatori specifici. Il diazepam passa facilmente perché è
liposolubile, la penicillina passa male perché è idrosolubile.' Right card, a pregnant
belly with a filter symbol, bold heading 'BARRIERA PLACENTARE': 'Filtra il passaggio delle
sostanze dalla madre al feto, ma non è una barriera assoluta. Molti farmaci possono
attraversarla e causare teratogenicità, cioè malformazioni. La attraversano per diffusione
passiva i composti lipofili, non ionizzati e di basso peso molecolare, sotto i 1000 Dalton.'
{MASCOT} peeking from the bottom right corner. {STYLE}"""),

27: ("metabolizzazione", f"""Vertical A4 page. Top left small purple letterspaced caps
'6 - FARMACOCINETICA'. Big bold black title 'METABOLIZZAZIONE' with 'E ACCUMULO' in purple.
Below, four rounded cards stacked vertically, each with a small pill-shaped label at the
top holding a white bold uppercase title.
Card 1, mint green, label 'ACCUMULO DI FARMACI', with two small cute flat illustrations of
a fat cell and of a tooth with a bone: 'Alcuni tessuti funzionano come magazzini:
trattengono il farmaco e lo rilasciano lentamente nel sangue.' plus two short bullet lines:
'Tessuto adiposo: attira i farmaci liposolubili, come anestetici e benzodiazepine, e li
rilascia lentamente, prolungando l'effetto.' and 'Ossa e denti: farmaci come le
tetracicline, che si legano al calcio.'
Card 2, lavender purple, label 'METABOLIZZAZIONE', with a small illustration of a liver
next to a capsule and a water drop: 'Detta anche biotrasformazione, avviene soprattutto nel
fegato. L'organismo trasforma il farmaco, di solito liposolubile, in una sostanza più
polare e idrosolubile, facile da eliminare con i reni o con la bile.'
Card 3, light blue, label 'RISULTATI', with three short bullet lines: 'Inattivazione: il
farmaco attivo diventa inattivo. È il caso più comune.', 'Attivazione: una sostanza inattiva
viene convertita nella forma attiva, per esempio l'enalapril.', 'Tossicità: si generano
metaboliti tossici, per esempio con il paracetamolo.'
Card 4, soft peach, label 'METABOLISMO DI PRIMO PASSAGGIO', with the text: 'È il pedaggio
che il fegato fa pagare al farmaco prima di lasciarlo entrare nella circolazione sistemica.
Una parte della dose viene distrutta prima di raggiungere il sito d'azione e questo riduce
la biodisponibilità.' and next to it a simple flow diagram with red arrows and small
Italian tags: a tag 'Orale' with an arrow to a tag 'Circolazione portale', then to a liver
labelled 'Fegato', then to a tag 'Resto del corpo'; and a separate tag 'Via endovenosa' with
an arrow going straight to 'Resto del corpo'. Under the diagram two short lines: 'Via orale:
passa prima dal fegato, attraverso la vena porta, dove subisce il metabolismo.' and 'Via
endovenosa: entra direttamente nella circolazione sistemica, senza metabolismo iniziale.'
{STYLE}"""),

28: ("profarmaci", f"""Vertical A4 page. Top left small purple letterspaced caps
'6 - FARMACOCINETICA'. Big bold black title 'PROFARMACI' with 'E FASI DEL METABOLISMO' in
purple. Below, three wide rounded sections stacked vertically, each introduced by a
pill-shaped banner with white bold uppercase text.
First section, lavender purple, banner 'PROFARMACI'. Inside the text: 'Sono sostanze
somministrate in forma inattiva, che devono subire una biotrasformazione per acquisire le
loro proprietà farmacologiche attive.' Then a simple horizontal flow diagram with arrows
and small Italian labels under each step, reading exactly 'Profarmaco', 'Biotrasformazione',
'Farmaco attivo', 'Recettore', 'Effetto farmacologico'. Then a white rounded box with a bold
heading 'VANTAGGI' and the text: 'Migliorano assorbimento, stabilità e selettività di alcuni
farmaci e permettono di aggirare il metabolismo di primo passaggio, in modo che la
concentrazione ottimale di farmaco attivo raggiunga il sangue.'
Second section, mint green, banner 'FASE I: FUNZIONALIZZAZIONE'. Inside the text:
'L'obiettivo è trasformare i composti lipofili in strutture più idrosolubili, aggiungendo o
esponendo gruppi funzionali polari nella molecola, come -OH o -NH2.' Then a short line with
a coloured dot: 'Reazioni principali: ossidazione con il sistema P450, riduzione e idrolisi.'
Third section, light blue, banner 'FASE II: CONIUGAZIONE'. Inside the text: 'Se dopo la Fase
I il farmaco non è ancora abbastanza polare, subisce la coniugazione: una sostanza endogena
molto polare, come l'acido glucuronico, viene attaccata al farmaco.' Then a short line with
a coloured dot: 'Risultato: un prodotto molto idrosolubile, pronto per essere eliminato dai
reni o dalla bile.'
At the very bottom a small grey italic line: 'Schema delle Fasi I e II nella pagina
successiva.' {STYLE}"""),

29: ("fasi-fattori", f"""Vertical A4 page. Top left small purple letterspaced caps
'6 - FARMACOCINETICA'. Big bold black title 'FASI DEL METABOLISMO' with 'E FATTORI' in
purple. Under the title a wide white rounded card with a lavender border holding a clean
horizontal flow diagram: a small tag 'Farmaco' with an arrow to a big purple pill-shaped
box 'FASE I', with a small caption underneath reading 'Ossidazione, riduzione e idrolisi',
then an arrow to a big green pill-shaped box 'FASE II', then an arrow to a small tag
'Prodotti di coniugazione'. Above the row, a long curved arrow going from 'Farmaco' over
'FASE I' directly to 'FASE II', with a small peach label attached to it reading
'Scorciatoia: alcuni farmaci entrano direttamente nella Fase II'. Under the row two small
notes: 'Dopo la Fase I il farmaco può essere attivato, restare invariato o, più spesso,
essere inattivato.' and 'Il coniugato è di solito inattivo.'
Below, a bold black heading 'FATTORI CHE INFLUENZANO LA METABOLIZZAZIONE' and three rounded
cards stacked vertically, each with a small pill-shaped label at the top holding a white
bold uppercase title and a small cute flat illustration.
Card 1, mint green, label 'ETÀ', illustration of a baby and an elderly person: 'La velocità
di metabolizzazione è ridotta in due gruppi e richiede cautela.' plus two short bullet
lines: 'Anziani: per il declino della funzione del fegato e del flusso sanguigno.' and
'Neonati: per l'immaturità enzimatica del fegato, non ancora del tutto sviluppato.'
Card 2, soft peach, label 'MALATTIE DEL FEGATO', illustration of a liver with a warning
sign: 'Malattie come la cirrosi o l'epatite compromettono la funzione epatica e riducono
drasticamente il metabolismo.' plus one short bullet line: 'Azione clinica: è essenziale
aggiustare la dose per prevenire l'accumulo tossico del farmaco.'
Card 3, light blue, label 'TOLLERANZA', illustration of a liver with green up arrows:
'L'uso prolungato di alcuni farmaci può indurre il fegato ad aumentare la produzione di
enzimi metabolizzanti.' plus two short bullet lines: 'Conseguenza: l'eliminazione accelera,
la concentrazione nel sangue si riduce e l'effetto terapeutico cala.' and 'Soluzione: se non
è possibile cambiare farmaco, occorre aumentare la dose per mantenere lo stesso effetto.'
{STYLE}"""),


}

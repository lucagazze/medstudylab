# -*- coding: utf-8 -*-
"""
Genera le pagine del libro come immagini intere con Gemini (nano-banana).
Uso: python gen.py 1 2 3   (senza argomenti: tutte)
"""
import os, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
AVATAR = os.path.join(ROOT, "..", "farmacologia", "art", "avatar.png")

STYLE = (
    "Educational infographic page from an Italian pharmacology study book, vertical A4 "
    "page, clean white background, NO watermark, no logo, no page border. Soft pastel "
    "palette of lavender purple, mint green, sky blue and soft peach; rounded pill-shaped "
    "cards; cute flat vector illustrations with thin dark outlines inside white circles; "
    "bold black uppercase headings in a geometric sans-serif, with one word in purple. "
    "Small floating pastel capsules, tablets and molecules as decoration. "
    "Modern, clean, generous spacing, nothing cropped at the edges. "
    "Reproduce every Italian text EXACTLY as written, with correct accents and "
    "apostrophes, perfect spelling, no invented words."
)

CHAR = ("A friendly 3D cartoon young man with dark brown wavy hair, warm skin, big brown "
        "eyes, a wide smile and a white polo shirt, cut out with no frame")

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
above. On the right side, a friendly cartoon mascot made of a lavender and white capsule
pill with big eyes, tiny arms and legs, waving. {STYLE}"""),

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
}


import json, base64, urllib.request

KEY = open(r"C:/Users/lucag/.nano-banana/.env").read().split("=", 1)[1].strip()
URL = ("https://generativelanguage.googleapis.com/v1beta/models/"
       "gemini-3-pro-image-preview:generateContent?key=" + KEY)


def gen(n, suffix=""):
    slug, prompt = PAGES[n]
    body = {"contents": [{"parts": [{"text": " ".join(prompt.split())}]}],
            "generationConfig": {"imageConfig": {"aspectRatio": "3:4",
                                                 "imageSize": "2K"}}}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=600).read())
    for p in r["candidates"][0]["content"]["parts"]:
        if "inlineData" in p:
            out = os.path.join(ROOT, f"p{n:02d}{suffix}.jpg")
            open(out, "wb").write(base64.b64decode(p["inlineData"]["data"]))
            print("ok", os.path.basename(out), slug)
            return out
    print("FALLITA", n, r.get("candidates", [{}])[0].get("finishReason"))


if __name__ == "__main__":
    todo = [int(a) for a in sys.argv[1:]] or sorted(PAGES)
    for n in todo:
        gen(n)

# -*- coding: utf-8 -*-
"""
Builds nails.html — the «Nails Made Visual» kit (US).

Same shell as every other landing in this repo: head, CSS, carousels,
accordions and footer come out of ekg.html, so a CSS fix on the site
reaches this page by regenerating it.

WHO IT TALKS TO. A working nail tech, licensed or in school. Not a
dermatologist and not a client. The book says so on its own page 3, and
it is why the safety part is called «Safety and the Board» and not
«Hygiene».

WHAT IS AMERICAN ABOUT IT. Grit by number, e-file and bits, dip powder,
EPA-registered disinfectant with its contact time, and the scope line
drawn where the state board draws it — which differs from state to state
and the book says that out loud instead of pretending there is one rule.

THE TABLE OF CONTENTS IS NOT TYPED HERE. It is read from the book's own
struttura.py, so moving a chapter in the book moves it on the landing.

PRICE: $27 against an anchor of $91, the same shape as every other US kit
in this repo. IT IS NOT TAKEN FROM A LIVE CHECKOUT, because at the time
of writing the nails product does not exist in the store yet: the slug
below is the one it SHOULD get. Until Luca creates it, the button lands
on the phantom-slug fallback, which sells the dentistry kit. Render the
checkout before putting a campaign live — see the note in AVVISO.

Images are built by tools/assets_nails.py and already exist:
  mockups/nails/{hero,combo,bonus-1,bonus-2,questo,og}
  anteprime/nails_01..07.webp

  python tools/make_nails.py        -> checkout-propio/public/lp/nails/en (US, $27)
                                       servida en nails.studiofacilebook.com/en
"""
import html
import json
import os
import re
import shutil
import sys

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRO = r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Nails-US"
sys.path.insert(0, LIBRO)
import struttura as S  # noqa: E402

TITLE = "Nails Made Visual"
SLUG = "nails"                     # imágenes, item_id y content_ids: el producto es el mismo
REGION = (sys.argv[1] if len(sys.argv) > 1 else "us").lower()
UK = REGION == "uk"
PAGE_SLUG = SLUG
# Desde el 05/10/2026 la landing NO vive en medicalstudylab.com: landing,
# checkout, post-compra y descargas van en nails.studiofacilebook.com (un
# subdominio de un dominio viejo y verificado; studiofacilebook.academy, recién
# registrado, lo bloqueaban los antivirus). Este script escribe la página y
# copia sus imágenes en el checkout propio (public/lp/nails/en), que la sirve
# en /en. medicalstudylab.com/nails redirige ahí (vercel.json).
SUB_HOST = "https://nails.studiofacilebook.com"
LANG = "en"
LP_BASE = f"/lp/{SLUG}/{LANG}"
LP_DIR = os.path.join(r"C:\Users\lucag\Desktop\CLAUDE\APPS\APPS\checkout-propio\public",
                      "lp", SLUG, LANG)
URL = f"{SUB_HOST}/{LANG}"
IMG = f"{SUB_HOST}{LP_BASE}/mockups/{SLUG}"

# ---------------------------------------------------------------------------
# PREZZO E CHECKOUT: PRESI DAL CHECKOUT VERO, APERTO NEL BROWSER.
#
# Il prodotto nel checkout si chiama «Illustrated Dentistry Kit» e mostra
# US$ 27 con un valore d'ancora di US$ 91. Il nome e le due cifre sulla
# landing sono quelle: il compratore deve leggere lo stesso numero da
# entrambe le parti, altrimenti il clic sul bottone e' il punto in cui se
# ne accorge. Gli altri importi che il checkout mostra ($14,50 e $7,90)
# sono i bump e non stanno qui.
#
# UK: £19.99 lo fija Luca para la campaña UK. El valor de referencia guarda la
# misma proporción que en dólares (91 contra 27) y va en libras enteras (67).
if UK:
    CUR, CURRENCY, COUNTRY = "£", "GBP", "GB"
    PRICE_N, TOTAL_N = 19.99, 67
else:
    CUR, CURRENCY, COUNTRY = "$", "USD", "US"
    PRICE_N, TOTAL_N = 27, 91


def money(n):
    return f"{CUR}{int(n)}" if float(n) == int(n) else f"{CUR}{n:.2f}"


PRICE = money(PRICE_N)
TOTAL = money(TOTAL_N)
# Redondeado para abajo (67 - 19,99 = 47,01 → «£47»): nunca promete de más.
SAVINGS = money(int(TOTAL_N - PRICE_N))
# Desde el 05/10/2026 el kit se cobra en el checkout propio (algordigital),
# tienda Med Study Lab, con el producto, los 2 bonos y los 2 order bumps
# cargados y SOLO el pixel de uñas 4766627606900943 (+ API de Conversiones).
# El checkout va en el mismo subdominio que la landing, en /en/checkout
# (funnels.checkout_host + checkout_path): misma cookie del pixel de punta a
# punta. Cobra la cuenta de Stripe de Med Study Lab.
CHECKOUT_HOST = SUB_HOST
CHECKOUT = f"{SUB_HOST}/{LANG}/checkout"
KIT = "Nails Made Visual Kit"

# I tre valori di riga. Il checkout da' il totale (91) e il prezzo (27), non
# come il totale si divide fra i tre volumi. La divisione e' quella che Luca
# ha già scelto per lo STESSO kit in italiano (odontoiatria: 17,90 il bonus
# dei vassoi, 14,90 quello delle emergenze, il resto il volume principale),
# arrotondata al dollaro in modo che la somma faccia esattamente 91. Non
# sono numeri inventati e non sono prezzi di listino: se Luca vuole un'altra
# divisione, si cambiano qui e basta rigenerare.
VAL_B1_N, VAL_B2_N = (13, 11) if UK else (18, 15)
VAL_MAIN_N = TOTAL_N - VAL_B1_N - VAL_B2_N      # 58 en dólares, 43 en libras
VAL_MAIN, VAL_B1, VAL_B2 = money(VAL_MAIN_N), money(VAL_B1_N), money(VAL_B2_N)
assert VAL_MAIN_N + VAL_B1_N + VAL_B2_N == TOTAL_N

AVVISO = f"""<!--
  ===========================================================================
  Generated by tools/make_nails.py — DO NOT HAND-EDIT THIS FILE.
  Edit the script and run `python tools/make_nails.py`.

  Checkout: the own checkout (algordigital), store medstudylab, product
  «nails-made-visual» with 2 bonuses and 2 order bumps, pixel 4766627606900943.
  The checkout charges $27 / £19.99 by the buyer's country, same as here.
    checkout : {CHECKOUT}
    price    : {PRICE} · total value {TOTAL} · you save {SAVINGS}
  UTM and fbclid of the ad are carried into the checkout by the script at
  the end of the page, so each sale is attributed to its campaign.

  The per-book values ({VAL_MAIN} / {VAL_B1} / {VAL_B2}) are NOT list
  prices: the two bonus books have none. They are the split used for the
  same three volumes in the other kits, rounded to the dollar so they add
  up to {TOTAL} exactly. Change VAL_B1_N / VAL_B2_N in the script.

  robots is noindex, nofollow — same as anatomy.html, abg.html, dosage.html
  and ekg-ems.html. These are paid-traffic landings.
  ===========================================================================
-->
"""

# Un pixel por oferta (05/10/2026): el de uñas REEMPLAZA al principal de Med
# Study Lab (1369545011992472) que trae el head de ekg.html. El checkout propio
# carga solo el de uñas, así que landing y compra quedan en el mismo pixel y el
# principal no se ensucia con visitas de una oferta que nunca le compra.
MAIN_PIXEL = "1369545011992472"
PIXEL = "4766627606900943"

# Los nombres de la TAPA de cada PDF, que es lo que llega al comprador
# (05/10/2026: la landing decía «Tray Setups Made Visual» y «Chairside
# Emergencies Made Visual», y el libro de emergencias trae 11 situaciones,
# no 10 — faltaba la reacción al anestésico local; ver DentalEmerg-US).
B1 = "Before You Turn On the Lamp"
B2 = "What Do I Tell the Client"

PAGES = S.TOTALE                                   # 86
N_PARTS = len(S.PARTI)                             # 4
N_CHAP = sum(len(c) for *_r, c in S.PARTI)         # 43


# --- il sommario, calcolato dal libro ------------------------------------
def part_from(num):
    """La prima pagina di contenuto: il divisore piu' uno.

    Questo libro non ha un dizionario DIVISORI: i divisori sono pagine
    normali chiamate div_I, div_II... Si legge da li'."""
    return S.folio("div_" + num) + 1


def part_to(num):
    """L'ultima pagina dell'ultimo capitolo della parte."""
    return S.folio([c for n, _t, _s, c in S.PARTI if n == num][0][-1][1][-1])


# Le quattro tavole da staccare, col titolo che si legge in pagina.
CLOSING = [("Bits: the shape, the job and the safe speed", "tav_bits"),
           ("Grits, and what each one is for", "tav_grits"),
           ("When you do not work: the stop list", "tav_stop"),
           ("The station, set up the same way every time", "tav_spa")]

BLURB = {
    "I": "How a nail is actually built, how it grows and what happens to "
         "it: the plate, the matrix, the folds and what you can read "
         "through it &mdash; the part that decides what you can do on that "
         "hand before you touch it.",
    "II": "Files by grit, bits by shape, RPM and where the heat really "
          "comes from. Your station, your light and where your hands sit, "
          "so eight hours do not cost you your shoulders.",
    "III": "Hard gel, acrylic, builder, dip. Prep, apex, C-curve, the three "
           "zones and the five reasons it lifts: the geometry that decides "
           "whether a set holds for three weeks or comes back in five "
           "days.",
    "IV": "From the dirty tool to the sealed pouch, EPA-registered "
          "disinfectant and contact time, ventilation and dust &mdash; and "
          "the scope line your state board actually draws.",
}

# Le sette anteprime: pagine vere del libro. L'ordine alterna la forma —
# una tabella, una sezione, un gruppo di oggetti, un vassoio, una sequenza,
# una catena, una mappa. Sette variazioni della stessa cosa si scorrono
# senza fermarsi.
SAMPLES = [
    ("nails_01", "A nail is not a flat plate: the parts, drawn and named",
     1473),
    ("nails_02", "Bits: the shape tells you the job, the band tells you "
                 "the grit", 1473),
    ("nails_03", "The apex: the point that decides whether it holds",
     1473),
    ("nails_04", "The C-curve, and how you build one on a flat bed",
     1473),
    ("nails_05", "Why it lifts: the five causes, one drawing each", 1473),
    ("nails_06", "From the dirty tool to the sealed pouch", 1473),
    ("nails_07", "The French, and the smile line that carries it", 1473),
]

FAQ = [
    ("How will I receive the material?",
     f"Right after purchase you get an automatic email with all three books: "
     f"{TITLE}, {B1} and {B2}. They are high-resolution PDFs, ready to "
     f"download, print or read on any device."),
    ("Is this a one-time payment or a subscription?",
     f"One-time payment of {PRICE}. No installments, no recurring charges, "
     f"no surprises. You pay once and the material is yours forever."),
    ("Do I need experience, or can I start from zero?",
     "You can start from zero. Part I gives you the nail itself &mdash; the "
     "plate, the matrix, the folds and what you can read through it. If you "
     "have been doing sets for a year already, skip to Part III and use the "
     "four pull-out tables."),
    ("Is this a course, or does it certify me?",
     "Neither, and the book says so on its own rights page. It is "
     "illustrated study material. Licensing is your state board's, and so "
     "is the list of what you are allowed to do: the book points at that "
     "line instead of pretending there is one national rule."),
    ("I work with gel, not acrylic. Is half of it useless to me?",
     "No. The build part covers hard gel, acrylic, builder gel and dip, but "
     "the geometry underneath them is the same product to product: prep, "
     "apex, C-curve, the three zones and the five reasons it lifts. That is "
     "most of Part III, and it does not change with what is in the jar."),
    ("Does it cover nail art?",
     "Only the French and how color actually covers &mdash; two chapters. "
     "This is a book about why a set holds, not a design gallery. If what "
     "you want is art, this is not it."),
    ("Does the first bonus replace knowing when to send someone to a "
     "doctor?",
     "No, it is the opposite: it is eighteen pages that end in three words "
     "every time &mdash; work, work with care, do not work. It names no "
     "disease and diagnoses nothing. What it does is stop you before the "
     "lamp when the hand in front of you is not yours to work on."),
    ("Can I print the material?",
     "Yes, for personal use and without limits. The PDFs are high "
     "resolution, and the four pull-out tables are made to be printed and "
     "taped up at the station."),
]
CHECK_SVG = ('<span class="db-check"><svg viewBox="0 0 24 24">'
             '<polyline points="20 6 9 17 4 12"/></svg></span>')

DESCR = (f"The nail, the tools, the build and the board in {PAGES} "
         f"illustrated pages, one topic per page, plus 2 bonus books. "
         f"{PRICE}, 30-day guarantee.")


def head(tpl_head):
    h = tpl_head
    rep = [
        ("<title>Reading EKGs Made Visual: the illustrated guide on real "
         "tracings | Med Study Lab</title>",
         f"<title>{TITLE}: the easiest way to understand nails, fully "
         f"illustrated | Med Study Lab</title>"),
        ('content="Rhythm, arrhythmias, blocks, MI and electrolytes in 68 '
         'illustrated pages on real EKGs, plus 2 bonus books. $27, 30-day '
         'guarantee."', f'content="{DESCR}"'),
        ('<meta name="robots" content="index, follow">',
         '<meta name="robots" content="noindex, nofollow">'),
        ('  <link rel="alternate" hreflang="en" '
         'href="https://www.medicalstudylab.com/">\n', ''),
        ('href="https://www.medicalstudylab.com/ekg"', f'href="{URL}"'),
        ('content="https://www.medicalstudylab.com/ekg"', f'content="{URL}"'),
        ('content="Reading EKGs Made Visual | Med Study Lab"',
         f'content="{TITLE} | Med Study Lab"'),
        ('content="Read an EKG without panicking: an 8-step method on real '
         'tracings, explained with pictures."',
         'content="The easiest way to understand nails, fully illustrated: the nail, the tools, the build and the board, one topic per page."'),
        ("https://www.medicalstudylab.com/mockups/ekg/og.jpg", f"{IMG}/og.jpg"),
        ('content="Reading EKGs Made Visual — Med Study Lab"',
         f'content="{TITLE} — Med Study Lab"'),
        ('content="68 illustrated pages on real EKGs + 2 bonus books."',
         f'content="{PAGES} illustrated pages for the person beside the '
         f'chair + 2 bonus books."'),
    ]
    for a, b in rep:
        assert a in h, a[:70]
        h = h.replace(a, b)
    s = h.index('<script type="application/ld+json">')
    e = h.index("</script>", s) + len("</script>")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Product", "name": KIT,
         "brand": {"@type": "Brand", "name": "Med Study Lab"},
         "description": f"{PAGES} illustrated pages for working nail "
                        "technicians: the nail and what you can read "
                        "through it, files and bits and the heat they "
                        "make, the build from prep to apex to C-curve, "
                        "and the disinfection chain with the scope line "
                        "the state board draws. With two bonus books.",
         "image": f"{IMG}/hero.webp",
         "offers": {"@type": "Offer", "price": str(PRICE_N),
                    "priceCurrency": CURRENCY,
                    "availability": "https://schema.org/InStock",
                    "url": CHECKOUT,
                    "hasMerchantReturnPolicy": {
                        "@type": "MerchantReturnPolicy",
                        "returnPolicyCategory":
                            "https://schema.org/MerchantReturnFiniteReturnWindow",
                        "merchantReturnDays": 30,
                        "applicableCountry": COUNTRY}}},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": html.unescape(q),
             "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}}
            for q, a in FAQ]}]}
    h = (h[:s] + '<script type="application/ld+json">\n'
         + json.dumps(ld, ensure_ascii=False) + "\n  </script>" + h[e:])
    # init + noscript del pixel principal → el de uñas (ver MAIN_PIXEL)
    assert h.count(MAIN_PIXEL) == 2, h.count(MAIN_PIXEL)
    h = h.replace(MAIN_PIXEL, PIXEL)
    # L'avviso va DOPO <meta charset>, non in cima al file. Messo subito
    # dopo il doctype spingeva il charset oltre i primi 1024 byte, che e'
    # la finestra in cui il browser lo cerca: senza, la pagina si leggeva
    # in latin-1 e le cinque stelle dell'hero uscivano «â˜…â˜…â˜…».
    cs = '<meta charset="UTF-8">'
    j = h.index(cs) + len(cs) + 1
    return h[:j] + AVVISO + h[j:]


def body():
    acc = []
    for i, (num, name, _sub, chapters) in enumerate(S.PARTI, 1):
        items = "".join(f"<li>{t}</li>" for t, _k in chapters)
        acc.append(f'''        <div class="subject-item" data-open="false" role="listitem">
          <button class="subject-summary" type="button" aria-expanded="false" aria-controls="subj-content-{i}">
            <span class="subject-num" aria-hidden="true">{num}</span>
            <span class="subject-title">{name} <em style="font-style:normal;opacity:.6;font-weight:600">&middot; pp. {part_from(num)}-{part_to(num)}</em></span>
            <span class="subject-icon" aria-hidden="true"></span>
          </button>
          <div class="subject-content" id="subj-content-{i}" role="region">
            <div class="subject-content-inner"><ul class="subject-content-list">{items}</ul></div>
          </div>
        </div>''')
    end = "".join(f"<li>{t} &mdash; p. {S.folio(k)}</li>" for t, k in CLOSING)
    acc.append(f'''        <div class="subject-item" data-open="false" role="listitem">
          <button class="subject-summary" type="button" aria-expanded="false" aria-controls="subj-content-9">
            <span class="subject-num" aria-hidden="true">&middot;</span>
            <span class="subject-title">At the end: the pull-out tables <em style="font-style:normal;opacity:.6;font-weight:600">&middot; pp. {S.folio(CLOSING[0][1])}-{PAGES}</em></span>
            <span class="subject-icon" aria-hidden="true"></span>
          </button>
          <div class="subject-content" id="subj-content-9" role="region">
            <div class="subject-content-inner"><ul class="subject-content-list">{end}</ul></div>
          </div>
        </div>''')

    topics = []
    for num, name, _sub, _c in S.PARTI:
        topics.append(f'''        <div class="topic-item">
          <span class="topic-num">{num}</span>
          <div>
            <span class="topic-pages">pp. {part_from(num)}&ndash;{part_to(num)}</span>
            <h3>{name}</h3>
            <p>{BLURB[num]}</p>
          </div>
        </div>''')

    faq = []
    for i, (q, a) in enumerate(FAQ, 1):
        faq.append(f'''        <div class="faq-item">
          <button class="faq-question" aria-expanded="false" aria-controls="faq{i}">
            {q}
          </button>
          <div class="faq-answer" id="faq{i}" hidden>
            <p>{a}</p>
          </div>
        </div>''')

    sm = "\n".join(f'''          <article class="testimonial-item amostra-item" role="listitem">
            <img src="./anteprime/{f}.webp" alt="{alt}" width="1100" height="{hh}" loading="lazy" decoding="async">
          </article>''' for f, alt, hh in SAMPLES)

    # Le testimonianze sono quelle che il sito ha gia': non se ne inventa
    # nessuna per l'odontoiatria, e non se ne scrive una nuova.
    testi = "\n".join(
        f'          <article class="testimonial-item" role="listitem">'
        f'<img src="./depoimentos/testimonio-{i}.webp" alt="Feedback and '
        f'reviews from healthcare professionals using MedStudyLab" '
        f'width="1254" height="1254" loading="lazy" decoding="async">'
        f'</article>' for i in range(1, 14))

    ico_lock = ('<svg aria-hidden="true" focusable="false" class="lc" '
                'viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                'stroke-width="2" stroke-linecap="round" '
                'stroke-linejoin="round"><rect width="18" height="11" x="3" '
                'y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>'
                '</svg>')
    nav = lambda t, d, lab, pts: (
        f'<button type="button" class="carousel-nav" data-dir="{d}" '
        f'data-target="{t}" aria-label="{lab}"><svg viewBox="0 0 24 24" '
        f'fill="none" stroke="currentColor" stroke-width="2.4" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        f'<polyline points="{pts}"></polyline></svg></button>')
    P, N = "15 18 9 12 15 6", "9 18 15 12 9 6"

    # Il footer e' quello delle altre landing del sito, con una sola
    # differenza: fra i link c'e' un &middot;, e non il margin-left da 8px.
    # Con il margine i cinque link uscivano dalla pagina a 390 px e
    # comparivano le barre di scorrimento orizzontali — e' lo stesso
    # inciampo che avevano le landing di studiofacile.
    link = ('color: rgba(255,255,255,0.7); text-decoration: underline;')
    # Las políticas son las del checkout propio, en el mismo subdominio: dicen
    # lo mismo que el mail de entrega (garantía por problemas reales).
    legal = f"{SUB_HOST}/catalogo/medstudylab"
    footer_links = (f'<a href="{legal}/refund-policy" style="{link}">Refund Policy</a>'
                    f' &middot; <a href="{legal}/privacy" style="{link}">Privacy</a>'
                    f' &middot; <a href="{legal}/terms" style="{link}">Terms</a>'
                    f' &middot; <a href="{legal}/contact" style="{link}">Support</a>'
                    f' &middot; <a href="{legal}"'
                    f' style="{link}" target="_blank" rel="noopener">All '
                    f'products</a>')

    return f'''<body>

  <!-- OFFER BANNER -->
  <div class="promo" role="status" aria-live="off">
    <div class="promo-in">
      <span class="promo-txt">Launch Offer</span>
      <span class="promo-time">Valid until today, <span class="promo-clock" id="promoClock"></span></span>
    </div>
  </div>

  <!-- HERO -->
  <section class="hero">
    <div class="hero-content">
      <div class="hero-mockup">
        <img src="./mockups/{SLUG}/hero.webp" alt="{TITLE}, with {B1} and {B2} as bonus books"
             width="1200" height="886" loading="eager" fetchpriority="high" decoding="async">
      </div>
      <p class="hero-social">
        <span class="stars" aria-hidden="true">★★★★★</span>
        <span><strong>+11,978 students &amp; healthcare professionals</strong></span>
      </p>
      <h1>The Easiest Way to Understand Nails <mark>Explained Entirely with Drawings!</mark></h1>
      <p class="subheadline">From the nail in cross-section to the five reasons a set lifts: {PAGES} illustrated pages, one topic per page &mdash; written for the person holding the file, so you know why it holds instead of hoping it does.</p>
      <a href="#offer" id="cta-hero" class="btn-cta">I WANT TO UNDERSTAND NAILS WITH DRAWINGS</a>
      <p class="cta-small-print">
        {ico_lock} Digital book (PDF) · US edition · Secure checkout · Instant download · 30-day guarantee
      </p>
    </div>
  </section>

  <!-- STATS BAR -->
  <section class="stats-bar">
    <div class="container">
      <div class="stats-grid">
        <div class="stat-item">
          <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 10c.7-.7 1.69 0 2.5 0a2.5 2.5 0 1 0 0-5.5A2.5 2.5 0 1 0 14 2.5c0 .81.7 1.8 0 2.5l-9 9c-.7.7-1.69 0-2.5 0a2.5 2.5 0 0 0 0 5.5A2.5 2.5 0 1 0 10 21.5c0-.81-.7-1.8 0-2.5Z"/></svg></div>
          <strong>One topic per page</strong>
          <p>the drawing carries the logic, the text is the caption</p>
        </div>
        <div class="stat-item">
          <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg></div>
          <strong>{PAGES} illustrated pages</strong>
          <p>{N_PARTS} parts and {N_CHAP} chapters, from the nail to the board</p>
        </div>
        <div class="stat-item">
          <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg></div>
          <strong>Written for the US</strong>
          <p>grit by number, bits by shape, scope by state board</p>
        </div>
      </div>
    </div>
  </section>

  <!-- PREVIEWS -->
  <section class="section" aria-label="Sample pages">
    <div class="container">
      <h2 class="text-center">Here's What the Pages You'll Study Look Like</h2>
      <p class="text-center section-sub-p">One topic per page, the drawing that carries the logic and the text that captions it. Look inside:</p>

      <div class="testimonials-carousel-wrap" role="region" aria-label="Sample pages carousel">
        {nav("amostras-scroll", "prev", "Previous page", P)}
        {nav("amostras-scroll", "next", "Next page", N)}
        <div class="testimonials-scroll" id="amostras-scroll" role="list" data-no-autoplay>
{sm}
        </div>
        <div class="carousel-progress" aria-hidden="true"><div class="carousel-progress-inner" id="amostras-progress"></div></div>
        <div class="carousel-dots" id="amostras-dots" role="tablist" aria-label="Navigation"></div>
      </div>
    </div>
  </section>

  <!-- TESTIMONIALS -->
  <section class="section section-alt section-snug-top" aria-label="Reviews">
    <div class="container">
      <h2 class="text-center" style="margin-bottom: 32px;">What Over 11,978+ Students and Professionals Using MedStudyLab Have to Say:</h2>

      <div class="testimonials-carousel-wrap" role="region" aria-label="Reviews carousel">
        {nav("testimonials-scroll", "prev", "Previous review", P)}
        {nav("testimonials-scroll", "next", "Next review", N)}

        <div class="testimonials-scroll" id="testimonials-scroll" role="list">
{testi}
        </div>

        <div class="carousel-progress" aria-hidden="true">
          <div class="carousel-progress-inner" id="testimonials-progress"></div>
        </div>

        <div class="carousel-dots" id="testimonials-dots" role="tablist" aria-label="Reviews navigation"></div>
      </div>
    </div>
  </section>

  <!-- WHY IT IS DRAWN -->
  <section class="section section-alt section-snug-top">
    <div class="container">
      <h2 class="text-center">Why One Drawing Explains What Three Pages of Text Don't</h2>
      <div class="solution-content">
        <p class="text-center">Nail courses exist and many are good. The problem is not that the information is missing: it arrives as a video you watched once, and a week later almost none of it is left.</p>
        <p class="text-center">Here every topic sits on <strong>a single page, with the drawing doing the work</strong> and the text captioning it.</p>
        <div class="solution-image">
          <img src="./anteprime/nails_05.webp" alt="Why a set lifts: the five causes, each one drawn on the nail where it happens" width="1100" height="1473" loading="lazy" decoding="async">
        </div>
        <p class="text-center">This is the page on lifting. The five causes are drawn on the nail, each one where it actually happens. <strong>Looking at it answers, on its own, the question that costs you clients</strong>: why a set peels at the cuticle on one hand and at the free edge on another.</p>
        <p class="text-center">Because they are different failures with different fixes, and the place it separates is the one that tells you which. One drawing, and you don't forget it. That is what the book does for {N_CHAP} topics.</p>
        <p class="text-center" style="font-size: 22px; font-weight: 700; margin-top: 40px;">First you understand it. Only then does remembering it matter.</p>
      </div>
    </div>
  </section>

  <!-- COMPARISON -->
  <section class="comparison-section fade-in visible" aria-label="A list of names versus an illustrated page">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">The Difference Is Visual</span>
        <h2>Stop studying walls of text you forget in three days:</h2>
      </div>
      <div class="comparison-grid">
        <div class="comparison-card bad-card">
          <div class="comparison-label bad">ALL TEXT</div>
          <ul class="comparison-bullets bad-list">
            <li>Pages of prose to commit to memory</li>
            <li>No drawings, no context</li>
            <li>You still freeze in the operatory</li>
          </ul>
          <img src="./mockups/{SLUG}/questo.webp" alt="Pages of text to learn by heart" width="900" height="1190" loading="lazy" decoding="async">
        </div>
        <div class="comparison-card good-card">
          <div class="comparison-label good">THIS BOOK</div>
          <ul class="comparison-bullets good-list">
            <li>The same things, but drawn</li>
            <li>One topic per page, with its own logic</li>
            <li>You remember it because you understood it</li>
          </ul>
          <img src="./anteprime/nails_01.webp" alt="A nail is not a flat plate: the parts, drawn and named" width="1100" height="1473" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <!-- CONTENTS -->
  <section class="subjects-section fade-in visible" aria-label="Table of contents">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow eyebrow-inverse">Table of Contents</span>
        <h2>Take a Look at the {N_PARTS} Parts and {N_CHAP} Chapters</h2>
        <p class="subjects-subtitle">Sixteen pages on the nail itself, then the tools, the build and the board, plus four pull-out tables: {PAGES} pages, all illustrated</p>
      </div>
      <div class="subjects-accordion fade-in visible" role="list">
{chr(10).join(acc)}
      </div>
    </div>
  </section>

  <!-- SOLUTION -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">What If Every Topic Fit on a Single Page?</h2>
      <div class="solution-content">
        <p class="text-center">Picture this:</p>
        <p class="text-center">Instead of reading three pages of text on why a set lifts...</p>
        <p class="text-center">...you see the five causes drawn on the nail, <strong>each one where it actually happens</strong>. The same for the grits, the bits, the apex, the C-curve and the chain: one topic, one page, one drawing.</p>
        <div class="solution-image">
          <img src="./anteprime/nails_03.webp" alt="The apex: the point that decides whether a set holds or breaks" width="1100" height="1473" loading="lazy" decoding="async">
        </div>
        <p class="text-center">You stop <strong>memorizing and start understanding</strong>. And once you have seen why a lower block numbs half the face and an upper injection doesn't, you never have to remember it again.</p>
        <p class="text-center" style="font-size: 22px; font-weight: 700; margin-top: 40px;">That's exactly what {TITLE} is.</p>
        <p class="text-center">It isn't &ldquo;one more PDF&rdquo;. It's <strong>{N_PARTS} parts and {N_CHAP} illustrated chapters</strong>: the nail, the tools, the build and the board &mdash; and at the end, <strong>four tables made to be printed</strong>.</p>
        <p class="text-center">Because what the brain sees organized, <strong>it remembers</strong>.</p>
      </div>
    </div>
  </section>

  <!-- MODULES -->
  <section class="section">
    <div class="container">
      <h2 class="text-center">Here's What You Get With {TITLE}:</h2>
      <div style="margin: 20px auto 28px;">
        <img src="./mockups/{SLUG}/combo.webp" alt="{TITLE}: mockup with sample pages" width="1100" height="1620" loading="lazy" decoding="async" style="max-width: 480px; width: 100%; display: block; margin: 0 auto;">
      </div>
      <div class="topics-grid">
{chr(10).join(topics)}
      </div>
      <p class="text-center" style="font-size:15px;color:var(--text-light);max-width:760px;margin:0 auto;">
        At the end: <strong>four pull-out tables made to be printed</strong> &mdash; the three
        bits with their shape and safe speed, the grits with what each one is for, the stop list, and
        the whole infection control chain.
      </p>
      <div style="text-align: center; margin-top: 48px;">
        <a href="#offer" class="btn-cta">I WANT TO SEE THE FULL OFFER</a>
      </div>
    </div>
  </section>

  <!-- VALUE STACK -->
  <section class="value-section">
    <div class="container">
      <h2 class="text-center">But That's Not All: You Also Get 2 Bonus Books</h2>

      <div class="bonus-grid">
        <div class="bonus-item-with-image">
          <div class="bonus-mockup">
            <img src="./mockups/{SLUG}/bonus-1.webp" alt="{B1}, the bonus that stops you before the lamp" width="720" height="1000" loading="lazy" decoding="async">
          </div>
          <div class="bonus-text">
            <h3>BONUS 1: &ldquo;{B1}&rdquo;, the 18 situations that stop you</h3>
            <p class="value">Standalone value: {VAL_B1}</p>
            <p>20 pages, <strong>one situation per page</strong>, and every one of them ends in the same three words: work, work with care, do not work.</p>
            <p style="margin-top: 12px;">It names no disease and diagnoses nothing &mdash; that is not yours and it says so. It describes what is in front of you and tells you whether today is the day to work on that hand.</p>
          </div>
        </div>

        <div class="bonus-item-with-image">
          <div class="bonus-mockup">
            <img src="./mockups/{SLUG}/bonus-2.webp" alt="{B2}, the bonus with the 18 questions clients ask" width="720" height="1000" loading="lazy" decoding="async">
          </div>
          <div class="bonus-text">
            <h3>BONUS 2: &ldquo;{B2}&rdquo;, the 18 questions they ask</h3>
            <p class="value">Standalone value: {VAL_B2}</p>
            <p>20 pages of the eighteen questions clients actually ask: <strong>does gel ruin my nails, why does it lift, is this a fungus, can I do this pregnant, why is it so expensive</strong> &mdash; and, for each one, a sentence you can say out loud.</p>
            <p style="margin-top: 12px;">Every page has the same three bands in the same order: how you recognize it, what you do first, and what you never do. The role stays yours &mdash; recognize, call, assist.</p>
          </div>
        </div>
      </div>

      <!-- DECISION BOX -->
      <div class="decision-box" id="offer">
        <img src="./mockups/{SLUG}/hero.webp" alt="{TITLE} with the two bonus books" class="db-mockup" width="1200" height="886" loading="lazy" decoding="async">
        <h3 class="db-title">{KIT}: {TITLE} + 2 Bonus Books</h3>
        <ul class="db-checklist">
          <li>{CHECK_SVG}{TITLE}: {PAGES} illustrated pages<span class="db-price-val">{VAL_MAIN}</span></li>
          <li>{CHECK_SVG}Bonus 1: {B1}<span class="db-price-val">{VAL_B1}</span></li>
          <li>{CHECK_SVG}Bonus 2: {B2}<span class="db-price-val">{VAL_B2}</span></li>
          <li>{CHECK_SVG}High-resolution printable PDFs<span class="db-price-val">Included</span></li>
        </ul>
        <div class="db-anchoring">
          <p class="db-old-price">Total value: {TOTAL}</p>
          <p class="db-new-price-label">Today only:</p>
          <p class="db-new-price">{PRICE}</p>
          <span class="db-discount-badge">YOU SAVE {SAVINGS}</span>
        </div>
        <a href="{CHECKOUT}" data-checkout class="db-cta">YES, I WANT THE {KIT.upper()} FOR {PRICE}</a>
        <div class="db-trust">
          <span class="db-trust-item"><span class="db-trust-icon"><svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg></span>Secure purchase</span>
          <span class="db-trust-item"><span class="db-trust-icon"><svg viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1s3.1 1.39 3.1 3.1v2z"/></svg></span>Encrypted payment</span>
          <span class="db-trust-item"><span class="db-trust-icon"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></span>30-day guarantee</span>
        </div>
        <p class="db-small-print">Digital book (PDF), instant download. All 3 books arrive by email right after purchase. One-time payment, no installments or hidden fees.</p>
      </div>
    </div>
  </section>

  <!-- WHO IS IT FOR -->
  <section class="section">
    <div class="container">
      <h2 class="text-center">Is This Material Right for You?</h2>
      <div class="paraquem-grid">
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/persona-student.webp" alt="A student in a nail program" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>You're in nail school, or studying for the board</h3>
            <p>You have the textbooks, so information isn't what you're short of: seeing it is. Here every topic sits on one page, with the drawing carrying the logic and the text captioning it.</p>
          </div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/persona-professional.webp" alt="A nail technician working at the table" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>You're already doing sets, and nobody drew it for you</h3>
            <p>You file, you build, you cure. What you never got shown is what is underneath: where the apex belongs, why the C-curve is structure and not decoration, and why the same lift on two hands has two different causes.</p>
          </div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/persona-graduate.webp" alt="Someone newly licensed, working their first months" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>You just started in an office</h3>
            <p>You can do a set, but you cannot always say why one held and the next one didn't. You need the whole picture and the tables you can keep in front of you at the station.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- AUTHOR -->
  <section class="section author-section">
    <div class="container">
      <h2 class="text-center">Who's Behind Med Study Lab</h2>
      <div class="author-content">
        <div class="author-image">
          <img src="./Img-Leandro.webp" alt="Leandro Moretti - Pharmacist and founder of Med Study Lab" width="266" height="400" loading="lazy" decoding="async">
        </div>
        <div class="author-bio">
          <h3>Leandro Moretti</h3>
          <h4>Pharmacist · Founder of Med Study Lab</h4>
          <p>Pharmacist and founder of Med Study Lab, the series of illustrated books for healthcare: pharmacology, clinical handbooks, lab tests, EKGs, dosage calculations, clinical anatomy and now nails.</p>
          <p>The method is always the same: <strong>visual clarity and one topic per page</strong>, because what the brain sees organized, it remembers.</p>
          <p>For nails the decision was a different one: <strong>not to write one more course</strong>. Those already exist, and most of them show you what to do without ever showing you why. What doesn't exist is the book that draws the reason &mdash; and this is that book.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- RECAP -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">To Recap: Here's Everything You Get</h2>
      <ul class="recap-list">
        <li>{TITLE}: {PAGES} illustrated pages in {N_PARTS} parts &mdash; the nail and what you can read through it, files and bits and the heat they make, the build from prep to apex to C-curve, and the disinfection chain with the scope line your board draws</li>
        <li>Bonus 1: &ldquo;{B1}&rdquo;, 20 pages and 18 situations, one per page, each ending in work / work with care / do not work (value {VAL_B1})</li>
        <li>Bonus 2: &ldquo;{B2}&rdquo;, 20 pages and the 18 questions clients ask, each with a sentence you can say out loud (value {VAL_B2})</li>
        <li>Four pull-out tables made to be printed and taped up next to the sterilizer</li>
        <li>Delivery: all 3 books by email right after purchase</li>
        <li>30-day guarantee if anything is genuinely wrong with the books</li>
        <li>High-resolution PDFs: print them, annotate them, keep them in the operatory</li>
      </ul>
      <div class="price-recap">
        <p class="old-price">{TOTAL}</p>
        <p class="new-price">{PRICE}</p>
      </div>
      <div style="text-align: center;">
        <a href="#offer" class="btn-cta">I WANT TO SEE THE FULL OFFER</a>
      </div>
    </div>
  </section>

  <!-- GUARANTEE -->
  <section class="section">
    <div class="container">
      <div class="guarantee-box">
        <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg></div>
        <h3>30-Day Guarantee</h3>
        <p>You have 30 days to go through {TITLE} and the two bonus books.</p>
        <p>If something is genuinely wrong &mdash; a file won't open, or the content isn't what this page describes &mdash; write to us and tell us what happened: <strong>we fix it or refund you</strong>.</p>
        <p>Please note: these are <strong>digital books (PDF)</strong>, delivered by email. Nothing is shipped, so expecting a printed book or changing your mind after downloading are not grounds for a refund.</p>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">Frequently Asked Questions</h2>
      <div class="faq-container">
{chr(10).join(faq)}
      </div>
    </div>
  </section>

  <!-- FINAL CTA -->
  <section class="final-cta">
    <div class="container">
      <h2>One Last Thing Before You Decide...</h2>
      <p>At the table, you don't have to learn it by getting it wrong on a paying client first.</p>
      <p>You don't have to memorize fifty shapes without ever being told why they are shaped that way.</p>
      <p>And you certainly <strong>shouldn't find out why it lifts from the client who is telling you it lifted</strong>.</p>
      <p style="font-size: 22px; font-weight: 700; margin-top: 32px;">There's an easier way. And it's one click away.</p>
      <p>{N_PARTS} parts, {N_CHAP} illustrated chapters, four pull-out tables and two bonus books.</p>
      <p><strong>Now it's your turn.</strong></p>
      <div class="cta-summary">
        <ul>
          <li>One-time payment: {PRICE}</li>
          <li>Guarantee: 30 days</li>
          <li>Delivery: all 3 books right after purchase</li>
        </ul>
      </div>
      <a href="#offer" class="btn-cta">I WANT THE {KIT.upper()} FOR {PRICE}</a>
      <p class="cta-small-print" style="margin-top: 24px;">
        <svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/></svg> Digital book (PDF) · The books arrive by email within minutes
      </p>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container">
      <p>© 2026 Med Study Lab · All rights reserved · {footer_links}</p><p class="legal-entity" style="margin:12px 0 0;font-size:10.5px;line-height:1.7;letter-spacing:.12em;opacity:.5;">QUILLSTONE DIGITAL LLC<br>1057 NW 136TH AVE, MIAMI, FL 33182</p>
    <p style="margin:10px 0 0;font-size:11px;opacity:.55;">Illustrated study material for working nail technicians. It is not a license and it is not a course. What you are permitted to do is decided by your state board, and the rules differ from state to state. Nothing here is medical advice: where a nail shows something that is not yours to work on, the book says so and sends the client to a physician.</p>
    </div>
  </footer>
'''


def tail(tpl_tail):
    """Gli script dell'index, col prodotto e il prezzo di questa pagina.

    Il nome del prodotto nella misurazione e' quello del KIT, non del volume
    principale: in Meta e in GA4 deve corrispondere alla riga del checkout,
    altrimenti l'acquisto e la visita finiscono su due prodotti diversi."""
    t = tpl_tail
    rep = [('"item_id": "ekg", "item_name": "Reading EKGs Made Visual", '
            '"price": 27', f'"item_id": "{SLUG}", "item_name": "{KIT}", '
                           f'"price": {PRICE_N}'),
           ('"content_ids": ["ekg"], "content_name": "Reading EKGs Made '
            'Visual", "content_type": "product", "value": 27',
            f'"content_ids": ["{SLUG}"], "content_name": "{KIT}", '
            f'"content_type": "product", "value": {PRICE_N}')]
    for a, b in rep:
        assert a in t, a
        t = t.replace(a, b)
    t = t.replace("value: 27,", f"value: {PRICE_N},")
    if UK:
        t = t.replace('"currency": "USD"', '"currency": "GBP"').replace("currency: 'USD'", "currency: 'GBP'")
    return t


UTM_JS = """<script>
(function () {
  var q = new URLSearchParams(location.search), keep = new URLSearchParams();
  q.forEach(function (v, k) { if (/^utm_|^fbclid$|^gclid$/.test(k)) keep.set(k, v); });
  var s = keep.toString();
  if (!s) return;
  document.querySelectorAll('a[data-checkout], a[href^="%s"]').forEach(function (a) {
    a.href += (a.href.indexOf('?') < 0 ? '?' : '&') + s;
  });
})();
</script>
""" % CHECKOUT_HOST

# Presencia en la landing para el panel «En vivo» del checkout propio
# (public/t.js de checkout-propio, mismo dominio): view, heartbeat, clic al
# checkout y salida, con la tienda y el checkout de esta oferta.
TRACK_JS = '<script defer src="/t.js" data-store="%s" data-funnel="%s"></script>\n' % (
    CHECKOUT_HOST.rstrip("/").rsplit("/", 1)[1], CHECKOUT.rstrip("/").rsplit("/", 1)[1])


def main():
    src = open(os.path.join(SITO, "ekg.html"), encoding="utf-8").read()
    i = src.index("<body>")
    j = src.index("  <!-- Dynamic Offer Date")
    out = head(src[:i]) + body() + tail(src[j:])
    # Los UTM y el fbclid del anuncio viajan al checkout: así cada venta queda
    # pegada a su campaña, conjunto y anuncio (el checkout los guarda en el pedido).
    out = out.replace("</body>", UTM_JS + TRACK_JS + "</body>", 1)
    # Cada "./archivo" de la página se copia a public/lp/nails/en y pasa a
    # "/lp/nails/en/archivo": la página se sirve en /en, no en su carpeta.
    # El manifest es el de Med Study Lab (start_url medicalstudylab.com): una
    # landing no lo necesita.
    out = re.sub(r'\s*<link rel="manifest"[^>]*>', "", out)
    copiar = set(re.findall(r'(?:src|href)="\./([^"?#]+)', out))
    copiar.add(f"mockups/{SLUG}/og.jpg")
    for rel in sorted(copiar):
        dst = os.path.join(LP_DIR, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(os.path.join(SITO, rel), dst)
    out = re.sub(r'((?:src|href)=")\./', rf'\1{LP_BASE}/', out)
    open(os.path.join(LP_DIR, "index.html"), "w", encoding="utf-8",
         newline="\n").write(out)
    print(f"  -> {LP_DIR}\\index.html + {len(copiar)} files")
    mancano = [p for p in
               [f"mockups/{SLUG}/{n}" for n in
                ("hero.webp", "combo.webp", "bonus-1.webp",
                 "bonus-2.webp", "questo.webp", "og.jpg")]
               + [f"anteprime/{f}.webp" for f, _a, _h in SAMPLES]
               if not os.path.exists(os.path.join(SITO, p))]
    print(f"{PAGE_SLUG}.html: {len(out)//1024} KB - {PAGES} pages, {N_PARTS} parts,"
          f" {N_CHAP} chapters - {PRICE} (value {TOTAL}, save {SAVINGS})")
    if mancano:
        print(f"  missing images: {len(mancano)} -> {mancano[:3]}")
    for tok in ("PLACEHOLDER",):
        if tok in out:
            print(f"  WARNING: {out.count(tok)} x {tok} still in the page")


if __name__ == "__main__":
    main()

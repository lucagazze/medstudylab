# -*- coding: utf-8 -*-
"""
Builds ekg.html — the US English twin of studiofacilebook.com/ecg.

Section by section it mirrors studiofacile/scripts/landing_ecg.py (hero,
stats, previews carousel, real tracings, comparison, contents with the 8
parts and page ranges, the easier way, what you get, 2 bonus books,
decision box, who is it for, author, recap, guarantee, FAQ, final CTA).
<head>, CSS and page scripts come from usd.html (same template as the
Italian index). The contents are computed from EKG-US/struttura.py.

  python tools/make_ekg.py
"""
import importlib.util
import io
import json
import os
import re

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRO = (r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Proyectos (código de los libros)"
         r"\Farmacologia\English\EKG-US")
os.environ["EDIZIONE"] = "US"
_spec = importlib.util.spec_from_file_location("struttura_ekg_us", os.path.join(LIBRO, "struttura.py"))
S = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S)

TITLE = "Reading EKGs Made Visual"
SLUG = "ekg"
CHECKOUT = "https://checkout.medicalstudylab.com/checkout/ekgs-finally-make-sense"
URL = f"https://www.medicalstudylab.com/{SLUG}"
LIVE = True

# Same scheme as the Italian offer: total value 91, today 27.
PRICE = 27
TOTAL = 91
VAL_EM = 19
VAL_LAB = 17
VAL_EKG = TOTAL - VAL_EM - VAL_LAB

N_PAG = S.TOTALE
N_PARTI = len(S.PARTI)
N_CAP = sum(len(c) for *_r, c in S.PARTI)
PAGES_W, PAGES_H = 1100, 1556

DESCR = {
    "I": "The paper, the twelve leads and the waves: the vocabulary you need to read everything else.",
    "II": "Rate, rhythm and axis: the first three steps, done on every strip.",
    "III": "Atrial fibrillation, flutter and SVT: when the rhythm starts in the atria and races.",
    "IV": "From PVCs to the arrest rhythms, split into shockable and non-shockable.",
    "V": "AV blocks and bundle branch blocks: where the impulse slows down or stops.",
    "VI": "The ST elevation you cannot miss, territory by territory, and what mimics it.",
    "VII": "Potassium, calcium and the drugs that prolong the QT: the EKG that changes with the labs.",
    "VIII": "Artifacts and reversed leads, when to call right away, and six guided cases.",
}

PREVIEWS = [
    ("ekg_01", "The EKG paper"),
    ("ekg_02", "Waves and intervals"),
    ("ekg_03", "The 8-step method"),
    ("ekg_04", "Atrial fibrillation"),
    ("ekg_05", "Shockable and non-shockable"),
    ("ekg_06", "The territories of an MI"),
    ("ekg_07", "Hyperkalemia"),
]


def usd(x):
    return f"${x:,.0f}"


def lucide(d):
    return ('<svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            f'{d}</svg>')


ICO_ECG = lucide('<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>')
ICO_LIB = lucide('<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>')
ICO_MONDO = lucide('<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>')
ICO_LUCC = lucide('<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>')
ICO_TEL = lucide('<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>')
ICO_SCUDO = lucide('<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>')
FRECCIA_SX = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
              'stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"></polyline></svg>')
FRECCIA_DX = FRECCIA_SX.replace("15 18 9 12 15 6", "9 18 15 12 9 6")
SPUNTA = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'


def sommario():
    v = []
    for i, (num, tit, _sot, capitoli) in enumerate(S.PARTI, 1):
        da, a = S.PARTI_PG[num], S.fine_parte(num)
        voci = "".join(f"<li>{t}</li>" for t, _k in capitoli)
        v.append(f"""
        <div class="subject-item" data-open="false" role="listitem">
          <button class="subject-summary" type="button" aria-expanded="false" aria-controls="subj-content-{i}">
            <span class="subject-num" aria-hidden="true">{num}</span>
            <span class="subject-title">{tit} <em style="font-style:normal;opacity:.6;font-weight:600">&middot; pp. {da}-{a}</em></span>
            <span class="subject-icon" aria-hidden="true"></span>
          </button>
          <div class="subject-content" id="subj-content-{i}" role="region">
            <div class="subject-content-inner"><ul class="subject-content-list">{voci}</ul></div>
          </div>
        </div>""")
    fine = "".join(f"<li>{t} &mdash; p. {S.CHIUSURA_PG[t]}</li>" for t, _v in S.CHIUSURA)
    da = S.CHIUSURA_PG[S.CHIUSURA[0][0]]
    v.append(f"""
        <div class="subject-item" data-open="false" role="listitem">
          <button class="subject-summary" type="button" aria-expanded="false" aria-controls="subj-content-9">
            <span class="subject-num" aria-hidden="true">&middot;</span>
            <span class="subject-title">At the end <em style="font-style:normal;opacity:.6;font-weight:600">&middot; pp. {da}-{N_PAG}</em></span>
            <span class="subject-icon" aria-hidden="true"></span>
          </button>
          <div class="subject-content" id="subj-content-9" role="region">
            <div class="subject-content-inner"><ul class="subject-content-list">{fine}</ul></div>
          </div>
        </div>""")
    return "".join(v)


def griglia_parti():
    return "".join(f"""
        <div class="topic-item">
          <span class="topic-num">{num}</span>
          <div>
            <span class="topic-pages">pp. {S.PARTI_PG[num]}&ndash;{S.fine_parte(num)}</span>
            <h3>{tit}</h3>
            <p>{DESCR[num]}</p>
          </div>
        </div>""" for num, tit, _s, _c in S.PARTI)


def anteprime():
    return "".join(f"""
          <article class="testimonial-item amostra-item" role="listitem">
            <img src="./amostras/{f}.webp" alt="{cap}" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async">
          </article>""" for f, cap in PREVIEWS)


def carosello(id_, voci, etichetta, prec, succ):
    return f"""
      <div class="testimonials-carousel-wrap" role="region" aria-label="{etichetta}">
        <button type="button" class="carousel-nav" data-dir="prev" data-target="{id_}-scroll" aria-label="{prec}">{FRECCIA_SX}</button>
        <button type="button" class="carousel-nav" data-dir="next" data-target="{id_}-scroll" aria-label="{succ}">{FRECCIA_DX}</button>
        <div class="testimonials-scroll" id="{id_}-scroll" role="list" data-no-autoplay>{voci}
        </div>
        <div class="carousel-progress" aria-hidden="true"><div class="carousel-progress-inner" id="{id_}-progress"></div></div>
        <div class="carousel-dots" id="{id_}-dots" role="tablist" aria-label="Navigation"></div>
      </div>"""


FAQ = [
    ("How will I receive the material?",
     "Right after purchase you get an automatic email with all three books: Reading EKGs Made "
     "Visual and the two bonus books, Emergency Medications and How to Read Lab Tests. They are "
     "high-resolution PDFs, ready to download, print or read on any device."),
    ("Is this a one-time payment or a subscription?",
     f"One-time payment of {usd(PRICE)}. No installments, no recurring charges, no surprises. "
     "You pay once and the material is yours forever."),
    ("Do I need to know anything before I start?",
     "No, you start from zero: Part I explains the paper, the leads and the waves before any "
     "arrhythmia. If you already read EKGs, you get the 8-step method and the chapters on MI and "
     "electrolytes."),
    ("Are the tracings real or drawn?",
     "Real. They come from PTB-XL, a public collection of 21,799 12-lead EKGs from 18,869 patients, "
     "read by cardiologists and published on PhysioNet. A drawn tracing is always clean; the ones "
     "you meet on the unit are not, and those are the ones to train your eye on."),
    ("Does it replace a course or the provider's judgment?",
     "No. It is study material to understand and recognize, not a clinical protocol. With a real "
     "patient you follow your facility's procedures and, when in doubt, ask: the book helps you get "
     "there prepared."),
    ("Can I print the material?",
     "Yes, for personal use and without limits. The PDFs are high resolution, made to print, "
     "annotate and take to clinicals or the floor."),
]


def faq_html():
    return "".join(f"""
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false" aria-controls="faq{i}">
            {d}
          </button>
          <div class="faq-answer" id="faq{i}" hidden>
            <p>{r}</p>
          </div>
        </div>""" for i, (d, r) in enumerate(FAQ, 1))


def schema():
    faq = [{"@type": "Question", "name": d, "acceptedAnswer": {"@type": "Answer", "text": r}} for d, r in FAQ]
    dati = {"@context": "https://schema.org", "@graph": [
        {"@type": "Product", "name": f"{TITLE} — illustrated guide",
         "brand": {"@type": "Brand", "name": "Med Study Lab"},
         "description": (f"{N_PAG} illustrated pages on real tracings: rhythm, arrhythmias, blocks, "
                         "MI and electrolytes. With two bonus books."),
         "image": f"https://www.medicalstudylab.com/mockups/{SLUG}/hero.webp",
         "offers": {"@type": "Offer", "price": str(PRICE), "priceCurrency": "USD",
                    "availability": "https://schema.org/InStock", "url": CHECKOUT,
                    "hasMerchantReturnPolicy": {"@type": "MerchantReturnPolicy",
                                                "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
                                                "merchantReturnDays": 30, "applicableCountry": "US"}}},
        {"@type": "FAQPage", "mainEntity": faq}]}
    return '<script type="application/ld+json">\n' + json.dumps(dati, ensure_ascii=False) + "\n  </script>"


EXTRA_CSS = """
  <style>
    .bonus-sfoglia{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px}
    .bonus-sfoglia figure{margin:0}
    .bonus-sfoglia img{width:100%;height:auto;display:block;border-radius:10px;box-shadow:0 8px 20px rgba(15,23,42,.14)}
    .bonus-sfoglia figcaption{font-size:12px;opacity:.75;margin-top:6px;text-align:center}
    .solution-image img{width:100%;height:auto}
    .topic-pages{display:block;font-size:12px;font-weight:700;opacity:.6;margin-bottom:2px}
  </style>
"""


def corpo(FOOTER):
    return f"""
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
        <img src="./mockups/{SLUG}/hero.webp" alt="{TITLE}, with Emergency Medications and How to Read Lab Tests as bonus books"
             width="1400" height="830" loading="eager" fetchpriority="high" decoding="async">
      </div>
      <p class="hero-social">
        <span class="stars" aria-hidden="true">★★★★★</span>
        <span><strong>+11,978 students & healthcare professionals</strong></span>
      </p>
      <h1>The Easiest Way to Read an EKG <mark>Without Panicking!</mark></h1>
      <p class="subheadline">The material for nurses, nursing students and new grads who need to recognize a rhythm, a block or an MI even when the cardiologist isn't there: explained with pictures, on real tracings.</p>
      <a href="#offer" id="cta-hero" class="btn-cta">I WANT TO READ EKGs WITH CONFIDENCE</a>
      <p class="cta-small-print">
        {ICO_LUCC} Secure checkout · Instant download · 30-day guarantee
      </p>
    </div>
  </section>

  <!-- STATS BAR -->
  <section class="stats-bar">
    <div class="container">
      <div class="stats-grid">
        <div class="stat-item">
          <div class="icon">{ICO_ECG}</div>
          <strong>Real tracings</strong>
          <p>from 21,799 EKGs read by cardiologists, not drawn</p>
        </div>
        <div class="stat-item">
          <div class="icon">{ICO_LIB}</div>
          <strong>{N_PAG} illustrated pages</strong>
          <p>{N_PARTI} parts and {N_CAP} chapters, from the paper to MI</p>
        </div>
        <div class="stat-item">
          <div class="icon">{ICO_MONDO}</div>
          <strong>US edition</strong>
          <p>plain American English, written for the floor</p>
        </div>
      </div>
    </div>
  </section>

  <!-- PREVIEWS -->
  <section class="section" aria-label="Sample pages">
    <div class="container">
      <h2 class="text-center">Here's What the Pages You'll Study Look Like</h2>
      <p class="text-center section-sub-p">One topic per page, the real tracing in the middle and the drawing that tells you where to look. Look inside:</p>
      {carosello("amostras", anteprime(), "Sample pages carousel", "Previous page", "Next page")}
    </div>
  </section>

  <!-- REAL TRACINGS -->
  <section class="section section-alt section-snug-top">
    <div class="container">
      <h2 class="text-center">Why the Tracings Are Real, Not Drawn</h2>
      <div class="solution-content">
        <p class="text-center">Almost every textbook shows perfect, hand-drawn waves: clean lines, no noise, every wave in its place.</p>
        <p class="text-center">Then you get to the unit and the strip in front of you <strong>looks nothing like the ones you studied</strong>.</p>
        <div class="solution-image">
          <img src="./mockups/{SLUG}/strip.webp" alt="A real lead II rhythm strip on EKG paper" width="1600" height="400" loading="lazy" decoding="async">
        </div>
        <p class="text-center">That's why every tracing in the book comes from <strong>PTB-XL</strong>: a public collection of <strong>21,799 12-lead EKGs from 18,869 patients</strong>, each one read by cardiologists and published on PhysioNet.</p>
        <p class="text-center">They're printed on real EKG paper, at 25 mm per second and 10 mm per millivolt, just as they come out of the machine. The drawing around them tells you <strong>where to look</strong>; the tracing stays a real patient's.</p>
        <p class="text-center" style="font-size: 22px; font-weight: 700; margin-top: 40px;">So your eye trains on what you'll really see.</p>
      </div>
    </div>
  </section>

  <!-- COMPARISON -->
  <section class="comparison-section fade-in visible" aria-label="A tracing with no explanation versus the illustrated page">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">The Difference Is Visual</span>
        <h2>Stop staring at a tracing without knowing where to start:</h2>
      </div>
      <div class="comparison-grid">
        <div class="comparison-card bad-card">
          <div class="comparison-label bad">FROM THIS</div>
          <ul class="comparison-bullets bad-list">
            <li>Twelve leads and no order</li>
            <li>You don't know where to look</li>
            <li>The doubt comes when there's no time</li>
          </ul>
          <img src="./img/textbook-dense.webp" alt="A dense textbook page with no explanation" width="768" height="1029" loading="lazy" decoding="async">
        </div>
        <div class="comparison-card good-card">
          <div class="comparison-label good">TO THIS</div>
          <ul class="comparison-bullets good-list">
            <li>A method in eight steps</li>
            <li>The drawing shows you what to look for</li>
            <li>You recognize it at first glance</li>
          </ul>
          <img src="./amostras/ekg_01.webp" alt="The EKG paper explained with illustrations" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <!-- CONTENTS -->
  <section class="subjects-section fade-in visible" aria-label="Table of contents">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow eyebrow-inverse">Table of Contents</span>
        <h2>Take a Look at the {N_PARTI} Parts and {N_CAP} Chapters</h2>
        <p class="subjects-subtitle">From the EKG paper to MI, electrolytes and cases at the bedside: {N_PAG} pages, all illustrated</p>
      </div>
      <div class="subjects-accordion fade-in visible" role="list">{sommario()}
      </div>
    </div>
  </section>

  <!-- SOLUTION -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">What If There Were an Easier Way?</h2>
      <div class="solution-content">
        <p class="text-center">Imagine this:</p>
        <p class="text-center">Instead of trying to remember fifty different patterns...</p>
        <p class="text-center">...you follow <strong>the same eight steps every time</strong>, in the same order: rate, rhythm, axis, P wave, PR, QRS, ST segment, QT.</p>
        <div class="solution-image">
          <img src="./amostras/ekg_03.webp" alt="The 8-step method to read an EKG, illustrated" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async">
        </div>
        <p class="text-center">Your brain <strong>stops searching at random</strong>. Every tracing becomes a checklist, and whatever doesn't fit jumps out on its own.</p>
        <p class="text-center" style="font-size: 22px; font-weight: 700; margin-top: 40px;">That's exactly what {TITLE} does.</p>
        <p class="text-center">It isn't &ldquo;just another PDF&rdquo;. It's a method in <strong>{N_PARTI} parts and {N_CAP} illustrated chapters</strong>, built on real tracings, so you <strong>understand what you see instead of memorizing pictures</strong>.</p>
        <p class="text-center">Because when you know where to look, <strong>even the ugliest strip starts to make sense</strong>.</p>
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
      <div class="topics-grid">{griglia_parti()}
      </div>
      <p class="text-center" style="font-size:15px;color:var(--text-light);max-width:760px;margin:0 auto;">
        At the end: a <strong>glossary</strong>, <strong>sources and references</strong> and an
        <strong>index</strong> to find every topic.
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
            <img src="./mockups/{SLUG}/bonus-em.webp" alt="Emergency Medications, illustrated handbook" width="720" height="1000" loading="lazy" decoding="async">
          </div>
          <div class="bonus-text">
            <h3>BONUS 1: &ldquo;Emergency Medications&rdquo;, the illustrated handbook</h3>
            <p class="value">Standalone value: {usd(VAL_EM)}</p>
            <p>82 pages on the drugs you use when a tracing becomes an emergency: <strong>adenosine, amiodarone, atropine</strong> and the rest of the crash cart, with the doses and dilutions to know by heart.</p>
            <p style="margin-top: 12px;">It completes Part IV of the book: you recognize the rhythm, and you already know what gets prepared.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/ekg_em1.webp" alt="Antiarrhythmics and the adult ACLS algorithm" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>The adult ACLS algorithm</figcaption></figure><figure><img src="./amostras/ekg_em2.webp" alt="Drug card: epinephrine" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>The epinephrine card</figcaption></figure></div>
          </div>
        </div>

        <div class="bonus-item-with-image">
          <div class="bonus-mockup">
            <img src="./mockups/{SLUG}/bonus-lab.webp" alt="How to Read Lab Tests" width="720" height="1000" loading="lazy" decoding="async">
          </div>
          <div class="bonus-text">
            <h3>BONUS 2: &ldquo;How to Read Lab Tests&rdquo;</h3>
            <p class="value">Standalone value: {usd(VAL_LAB)}</p>
            <p>74 pages to read a lab report: <strong>potassium, calcium, troponin</strong> and the CBC, with the critical values and what throws them off.</p>
            <p style="margin-top: 12px;">Read it next to Part VII: a peaked T wave and a high potassium are the same emergency seen from two sides.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/ekg_lab1.webp" alt="Critical results" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>Critical results</figcaption></figure><figure><img src="./amostras/ekg_lab2.webp" alt="Test card: potassium" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>The potassium card</figcaption></figure></div>
          </div>
        </div>
      </div>

      <!-- DECISION BOX -->
      <div class="decision-box" id="offer">
        <img src="./mockups/{SLUG}/hero.webp" alt="{TITLE} with the two bonus books" class="db-mockup" width="1400" height="830" loading="lazy" decoding="async">
        <h3 class="db-title">{TITLE} + 2 Bonus Books</h3>
        <ul class="db-checklist">
          <li><span class="db-check">{SPUNTA}</span>{TITLE}: {N_PAG} illustrated pages<span class="db-price-val">{usd(VAL_EKG)}</span></li>
          <li><span class="db-check">{SPUNTA}</span>Bonus 1: Emergency Medications<span class="db-price-val">{usd(VAL_EM)}</span></li>
          <li><span class="db-check">{SPUNTA}</span>Bonus 2: How to Read Lab Tests<span class="db-price-val">{usd(VAL_LAB)}</span></li>
          <li><span class="db-check">{SPUNTA}</span>High-resolution printable PDFs<span class="db-price-val">Included</span></li>
        </ul>
        <div class="db-anchoring">
          <p class="db-old-price">Total value: {usd(TOTAL)}</p>
          <p class="db-new-price-label">Today only:</p>
          <p class="db-new-price">{usd(PRICE)}</p>
          <span class="db-discount-badge">YOU SAVE {usd(TOTAL - PRICE)}</span>
        </div>
        <a href="{CHECKOUT}" data-checkout class="db-cta">YES, I WANT {TITLE.upper()} FOR {usd(PRICE)}</a>
        <div class="db-trust">
          <span class="db-trust-item"><span class="db-trust-icon"><svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg></span>Secure purchase</span>
          <span class="db-trust-item"><span class="db-trust-icon"><svg viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1s3.1 1.39 3.1 3.1v2z"/></svg></span>Encrypted payment</span>
          <span class="db-trust-item"><span class="db-trust-icon"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></span>30-day guarantee</span>
        </div>
        <p class="db-small-print">All 3 books arrive by email right after purchase. One-time payment, no installments or hidden fees.</p>
      </div>
    </div>
  </section>

  <!-- WHO IS IT FOR -->
  <section class="section">
    <div class="container">
      <h2 class="text-center">Is This Material Right for You?</h2>
      <div class="paraquem-grid">
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/ekg-persona-student.webp" alt="Nursing student" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>Nursing or medical student</h3>
            <p>EKGs are on the exam and in clinicals, and textbooks explain them as if you already knew. You need to start from the paper and get to MI without skipping a step.</p>
          </div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/ekg-persona-tele.webp" alt="Telemetry nurse" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>Floor, telemetry or ER nurse</h3>
            <p>The monitor alarms, the tracing changes, and you're the first to see it. You want to know in seconds whether it's artifact or you need to call right away.</p>
          </div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/ekg-persona-bedside.webp" alt="Nurse at the bedside" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>New grad or on nights</h3>
            <p>On nights or on the floor, you often read the EKG alone. You need a safe method and a quick review of blocks, ischemia and electrolytes.</p>
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
          <p>Pharmacist and founder of Med Study Lab, the series of illustrated books for healthcare: pharmacology, clinical handbooks, lab tests and now EKGs.</p>
          <p>The method is always the same: <strong>visual clarity and one topic per page</strong>, because what the brain sees organized, it remembers.</p>
          <p>For EKGs there was one more problem: a drawn tracing teaches you to recognize a drawing. That's why <strong>every tracing in the book is real</strong>, taken from EKGs read by cardiologists.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- RECAP -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">To Recap: Here's Everything You Get</h2>
      <ul class="recap-list">
        <li>{TITLE}: {N_PAG} illustrated pages in {N_PARTI} parts, from the EKG paper to MI and electrolytes, on real tracings</li>
        <li>Bonus 1: &ldquo;Emergency Medications&rdquo;, illustrated handbook, 82 pages (value {usd(VAL_EM)})</li>
        <li>Bonus 2: &ldquo;How to Read Lab Tests&rdquo;, 74 pages (value {usd(VAL_LAB)})</li>
        <li>Delivery: all 3 books by email right after purchase</li>
        <li>30-day guarantee, no questions asked: try it risk-free</li>
        <li>High-resolution PDFs: print them, annotate them, take them to clinicals</li>
      </ul>
      <div class="price-recap">
        <p class="old-price">{usd(TOTAL)}</p>
        <p class="new-price">{usd(PRICE)}</p>
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
        <div class="icon">{ICO_SCUDO}</div>
        <h3>&ldquo;Risk-Free Trial&rdquo; Guarantee: 30 Days</h3>
        <p>You have 30 full days to try {TITLE} and the two bonus books.</p>
        <p>If in that time you feel the material didn't help you, wasn't useful or simply wasn't what you expected, <strong>I'll refund 100% of your purchase</strong>.</p>
        <p>No questions. No fine print. No hassle.</p>
        <p><strong>The risk is ZERO. The decision is yours.</strong></p>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">Frequently Asked Questions</h2>
      <div class="faq-container">{faq_html()}
      </div>
    </div>
  </section>

  <!-- FINAL CTA -->
  <section class="final-cta">
    <div class="container">
      <h2>One Last Thing Before You Decide...</h2>
      <p>The EKG doesn't have to be the part you avoid.</p>
      <p>You don't have to memorize fifty patterns without understanding why they look that way.</p>
      <p>And you definitely <strong>don't have to find out you can't read one right when it matters</strong>.</p>
      <p style="font-size: 22px; font-weight: 700; margin-top: 32px;">There's an easier way. And it's one click away.</p>
      <p>Eight steps, real tracings and two bonus books for acute care.</p>
      <p><strong>Now it's your turn.</strong></p>
      <div class="cta-summary">
        <ul>
          <li>One-time payment: {usd(PRICE)}</li>
          <li>Guarantee: 30 days, no questions asked</li>
          <li>Delivery: all 3 books right after purchase</li>
        </ul>
      </div>
      <a href="#offer" class="btn-cta">I WANT {TITLE.upper()} FOR {usd(PRICE)}</a>
      <p class="cta-small-print" style="margin-top: 24px;">
        {ICO_TEL} The books arrive by email within minutes
      </p>
    </div>
  </section>

  <!-- FOOTER -->
{FOOTER}
"""


def testa(t):
    h = t[:t.index("</head>")]
    subs = [
        (r"<title>.*?</title>", f"<title>{TITLE}: the illustrated guide on real tracings | Med Study Lab</title>"),
        (r'<meta name="description" content=".*?">',
         f'<meta name="description" content="Rhythm, arrhythmias, blocks, MI and electrolytes in {N_PAG} illustrated pages on real EKGs, plus 2 bonus books. {usd(PRICE)}, 30-day guarantee.">'),
        (r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{URL}">'),
        (r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{URL}">'),
        (r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{TITLE} | Med Study Lab">'),
        (r'<meta property="og:description" content=".*?">',
         '<meta property="og:description" content="Read an EKG without panicking: an 8-step method on real tracings, explained with pictures.">'),
        (r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="https://www.medicalstudylab.com/mockups/{SLUG}/og.jpg">'),
        (r'<meta property="og:image:alt" content=".*?">', f'<meta property="og:image:alt" content="{TITLE} — Med Study Lab">'),
        (r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{TITLE} | Med Study Lab">'),
        (r'<meta name="twitter:description" content=".*?">',
         f'<meta name="twitter:description" content="{N_PAG} illustrated pages on real EKGs + 2 bonus books.">'),
        (r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="https://www.medicalstudylab.com/mockups/{SLUG}/og.jpg">'),
        (r'<script type="application/ld\+json">.*?</script>', schema()),
        (r'<meta name="robots" content=".*?">',
         '<meta name="robots" content="index, follow">' if LIVE else '<meta name="robots" content="noindex, follow">'),
    ]
    for rx, new in subs:
        h, n = re.subn(rx, lambda _m: new, h, count=1, flags=re.S)
        if n != 1:
            raise SystemExit(f"not found in usd.html head: {rx}")
    return h + EXTRA_CSS + "</head>\n<body>\n"


def footer(t):
    f = re.search(r'  <footer class="footer">.*?</footer>', t, re.S).group(0)
    f = f.replace("MedStudyLab · All rights reserved", "Med Study Lab · All rights reserved")
    attr = ('<p style="margin:10px 0 0;font-size:11px;opacity:.55;">EKG tracings from PTB-XL '
            '(Wagner et al., PhysioNet), released under the CC BY 4.0 license, and the MIT-BIH '
            'databases (PhysioNet).</p>')
    i = f.rindex("</div>")
    return f[:i] + attr + "\n    " + f[i:]


def coda(t):
    """Offer date script, analytics (names via json.dumps) and the page scripts. No fake toast."""
    a = t.index("<!-- Dynamic Offer Date")
    b = t.index("<!-- Analytics / GTM -->")
    c = t.index("<!-- Carousels Script -->")
    d = t.index("<!-- Recent Purchase Toast Script -->")
    item = json.dumps({"item_id": SLUG, "item_name": TITLE, "price": PRICE, "currency": "USD", "quantity": 1})
    fb = json.dumps({"content_ids": [SLUG], "content_name": TITLE, "content_type": "product",
                     "value": PRICE, "currency": "USD"})
    analytics = f"""  <!-- Analytics -->
  <script>
    (function () {{
      var ITEM = {item};
      var FB = {fb};
      window.dataLayer = window.dataLayer || [];
      dataLayer.push({{ ecommerce: null }});
      dataLayer.push({{ event: 'view_item', ecommerce: {{ currency: 'USD', value: {PRICE}, items: [ITEM] }} }});
      if (typeof fbq === 'function') fbq('track', 'ViewContent', FB);
      document.addEventListener('click', function (e) {{
        var a = e.target.closest('[data-checkout], a[href*="checkout"]');
        if (!a) return;
        dataLayer.push({{ ecommerce: null }});
        dataLayer.push({{ event: 'begin_checkout', cta_id: a.id || a.className || 'no-id',
                         ecommerce: {{ currency: 'USD', value: {PRICE}, items: [ITEM] }} }});
        if (typeof fbq === 'function') fbq('track', 'InitiateCheckout', FB);
      }}, true);
    }})();
  </script>

"""
    return "  " + t[a:b] + analytics + "  " + t[c:d] + "\n</body>\n</html>\n"


def main():
    t = io.open(os.path.join(SITO, "usd.html"), encoding="utf-8").read()
    html = testa(t) + corpo(footer(t)) + coda(t)
    body = html.split("</head>", 1)[1]
    for bad in ("spToast", "Manchester", "Pharmacology Kit"):
        assert bad not in body, f"leftover from usd.html: {bad}"
    for src in set(re.findall(r'src="\./([^"]+)"', html)):
        assert os.path.exists(os.path.join(SITO, src)), f"missing image: {src}"
    io.open(os.path.join(SITO, f"{SLUG}.html"), "w", encoding="utf-8", newline="\n").write(html)
    print(f"{SLUG}.html: {len(html) // 1024} KB · {N_PAG} pages · {N_PARTI} parts · {N_CAP} chapters · "
          f"{usd(PRICE)} (value {usd(TOTAL)})")


if __name__ == "__main__":
    main()

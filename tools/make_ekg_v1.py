# -*- coding: utf-8 -*-
"""
Builds ekg.html — the EKG Made Visual Kit (US). Same engine as make_pharm.py:
<head>, CSS and scripts from usd.html, body written here. Every page image is a
real page of the delivered US PDFs (tools/assets_ekg.py).

  python tools/make_ekg.py
"""
import io
import json
import os
import re

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SLUG = "ekg"
NAME = "EKG Made Visual Kit"
PRICE = 27
TOTAL = 91
# per-book values shown in the offer box (sum = TOTAL): decided by Luca 16/09/2026
VALUES = {"ekg": 39, "em": 29, "lab": 23}
assert sum(VALUES.values()) == TOTAL
GIORNI = 3
CHECKOUT = "https://checkout.medicalstudylab.com/checkout/ekgs-finally-make-sense"
URL = f"https://www.medicalstudylab.com/{SLUG}"
LIVE = True           # True once the checkout product exists -> indexable

PAGES_W, PAGES_H = 1100, 1556

PREVIEWS = [
    ("ekg_01", "The EKG paper"),
    ("ekg_02", "Waves and intervals"),
    ("ekg_03", "The 8-step method"),
    ("ekg_04", "Atrial fibrillation"),
    ("ekg_05", "Shockable and non-shockable"),
    ("ekg_06", "The territories of an MI"),
    ("ekg_07", "Hyperkalemia"),
    ("ekg_09", "Where the electrodes go"),
    ("ekg_08", "Six guided cases"),
]

CHECK = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'
ARROW_L = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<polyline points="15 18 9 12 15 6"></polyline></svg>')
ARROW_R = ARROW_L.replace("15 18 9 12 15 6", "9 18 15 12 9 6")


def lc(d):
    return ('<svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" '
            'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round">{d}</svg>')


I_LOCK = lc('<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>')
I_BOOKS = lc('<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>')
I_EYE = lc('<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>')
I_PHONE = lc('<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>')
I_SHIELD = lc('<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>')

CONTENTS = [
    ("1", "Reading EKGs Made Visual", "68 pages", [
        "Part I · The basics: the electrical heart, the paper, the 12 leads, waves and intervals, electrode placement, the 8-step method",
        "Part II · Rate, rhythm and axis: three ways to count the rate, sinus rhythms, the axis in two leads",
        "Part III · Supraventricular arrhythmias: PACs, atrial fibrillation, flutter, SVT, Wolff-Parkinson-White",
        "Part IV · Ventricular arrhythmias and arrest: PVCs, VT, torsades, VF, asystole and PEA, shockable vs non-shockable",
        "Part V · Heart blocks: first, second and third-degree AV block, bundle branch and fascicular blocks",
        "Part VI · Ischemia and infarction: STEMI criteria, territories, posterior and right ventricular MI, NSTEMI, mimics",
        "Part VII · Electrolytes, drugs and hypertrophy: potassium, calcium, long QT, digoxin, ventricular hypertrophy",
        "Part VIII · At the bedside: artifacts, when to call right away, six guided cases",
        "A review page at the end of each part, glossary, index and sources"]),
    ("2", "Bonus: Emergency Medications Illustrated", "82 pages", [
        "Seven emergency scenarios and the drugs used in each",
        "Antiarrhythmics and the adult ACLS algorithm: adenosine, amiodarone, epinephrine, atropine and more",
        "Drug cards: dose, how it is given, onset, cautions, adverse effects",
        "Doses at a glance and a checklist of the numbers to know"]),
    ("3", "Bonus: How to Read Lab Tests", "74 pages", [
        "Reading a report: reference ranges, critical results, the commonest mistakes",
        "The complete blood count, kidney, liver and thyroid",
        "Electrolytes and blood gases: potassium, calcium, magnesium, arterial blood gas",
        "Troponin, BNP, D-dimer and clotting, in US conventional units"]),
]

FAQ = [
    ("How will I receive the material?",
     "Right after purchase you get an email with your download link. All three books are "
     "high-resolution PDFs you can read on your phone, tablet or computer, or print."),
    ("Is this a one-time payment or a subscription?",
     f"One-time payment of ${PRICE}. No subscription, no recurring charges. You keep the "
     "files forever."),
    ("Are the tracings real?",
     "Yes. The rhythm strips come from PTB-XL, a public database of 21,799 clinical 12-lead "
     "EKGs published on PhysioNet, and from the MIT-BIH arrhythmia databases. A few teaching "
     "diagrams are drawn and clearly labeled as schematic."),
    ("Is it written for nursing in the US?",
     "Yes. It uses American terms and current AHA/ACC guidance: ACLS rhythms, rapid response, "
     "US drug names and US lab units (potassium in mEq/L)."),
    ("Is this an NCLEX or ACLS course?",
     "No. It is a visual study companion to understand and recognize EKGs. It does not replace "
     "an ACLS certification course or your facility's protocols, and we are not affiliated "
     "with NCSBN or the AHA."),
    ("What if it isn't for me?",
     "You have 30 days. If the material doesn't help you, email us and you get a full refund."),
]

def previews():
    return "".join(
        f'\n          <article class="testimonial-item amostra-item" role="listitem">'
        f'<img src="./amostras/{f}.webp" alt="Sample page: {c}" width="{PAGES_W}" height="{PAGES_H}" '
        f'loading="lazy" decoding="async"></article>' for f, c in PREVIEWS)


def carousel():
    return f"""
      <div class="testimonials-carousel-wrap" role="region" aria-label="Sample pages carousel">
        <button type="button" class="carousel-nav" data-dir="prev" data-target="amostras-scroll" aria-label="Previous page">{ARROW_L}</button>
        <button type="button" class="carousel-nav" data-dir="next" data-target="amostras-scroll" aria-label="Next page">{ARROW_R}</button>
        <div class="testimonials-scroll" id="amostras-scroll" role="list" data-no-autoplay>{previews()}
        </div>
        <div class="carousel-progress" aria-hidden="true"><div class="carousel-progress-inner" id="amostras-progress"></div></div>
        <div class="carousel-dots" id="amostras-dots" role="tablist" aria-label="Sample pages navigation"></div>
      </div>"""


def accordion():
    out = []
    for num, title, pages, items in CONTENTS:
        li = "".join(f"<li>{x}</li>" for x in items)
        out.append(f"""
        <div class="subject-item" data-open="false" role="listitem">
          <button class="subject-summary" type="button" aria-expanded="false" aria-controls="subj-content-{num}">
            <span class="subject-num" aria-hidden="true">{num}</span>
            <span class="subject-title">{title} <em style="font-style:normal;opacity:.6;font-weight:600">&middot; {pages}</em></span>
            <span class="subject-icon" aria-hidden="true"></span>
          </button>
          <div class="subject-content" id="subj-content-{num}" role="region">
            <div class="subject-content-inner"><ul class="subject-content-list">{li}</ul></div>
          </div>
        </div>""")
    return "".join(out)


def faq_html():
    return "".join(f"""
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false" aria-controls="faq{i}">{q}</button>
          <div class="faq-answer" id="faq{i}" hidden><p>{a}</p></div>
        </div>""" for i, (q, a) in enumerate(FAQ, 1))


EXTRA_CSS = """
  <style>
    .pmv-suffix{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;max-width:560px;margin:24px auto}
    .pmv-suffix div{background:#fff;border:2px solid #e3e8f5;border-radius:16px;padding:14px 16px;text-align:center}
    .pmv-suffix b{display:block;font-size:26px;color:#f97216;letter-spacing:-.01em}
    .pmv-suffix span{font-size:14px;color:#475569}
    .pmv-card{max-width:900px;margin:24px auto;border-radius:18px;overflow:hidden;box-shadow:0 14px 34px rgba(15,23,42,.12)}
    .pmv-card img{width:100%;height:auto;display:block}
    .bonus-sfoglia{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px}
    .bonus-sfoglia figure{margin:0}
    .bonus-sfoglia img{width:100%;height:auto;display:block;border-radius:10px;box-shadow:0 8px 20px rgba(15,23,42,.14)}
    .bonus-sfoglia figcaption{font-size:12px;opacity:.75;margin-top:6px;text-align:center}
    .pmv-new{display:inline-block;background:#f97216;color:#fff;font-size:12px;font-weight:800;letter-spacing:.06em;padding:4px 10px;border-radius:999px;margin-bottom:8px}
    .pmv-compare{font-size:14px;color:#64748b;margin:6px 0 0}
    .pmv-perbook{display:inline-block;margin:10px 0 2px;background:#fff4e8;color:#c2410c;font-size:15px;padding:6px 14px;border-radius:999px}
    .pmv-mini{display:grid;gap:10px;margin-top:16px}
    .pmv-mini img{width:100%;height:auto;display:block;border-radius:10px;box-shadow:0 8px 20px rgba(15,23,42,.18)}
    .pmv-mini span{font-size:12px;opacity:.75;text-align:center}
    .hero-mockup img{filter:drop-shadow(0 24px 40px rgba(8,20,60,.35))}
    .pmv-books-strip{display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin:8px auto 36px;max-width:760px}
    .pmv-books-strip span{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);color:#fff;font-size:13px;font-weight:700;padding:8px 14px;border-radius:999px}
    .decision-box .db-checklist li{align-items:center}
    .solution-image img[src*='amostras']{width:100%;max-width:520px;height:auto;margin:0 auto;display:block}
  </style>
"""


def body(footer):
    return f"""
  <!-- OFFER BANNER -->
  <div class="promo" role="status" aria-live="off">
    <div class="promo-in">
      <span class="promo-txt">Launch offer</span>
      <span class="promo-time">3 illustrated books · ${TOTAL} value, today ${PRICE}</span>
    </div>
  </div>

  <!-- HERO -->
  <section class="hero">
    <div class="hero-content">
      <div class="hero-mockup">
        <img src="./mockups/ekg/hero.webp" alt="EKG Made Visual Kit: Reading EKGs Made Visual, Emergency Medications and How to Read Lab Tests"
             width="1400" height="830" loading="eager" fetchpriority="high" decoding="async">
      </div>
      <p class="hero-social"><span class="stars" aria-hidden="true">★★★★★</span><span><strong>+11,978 students</strong> study with our illustrated books</span></p>
      <h1>EKGs Finally Make Sense <mark>When You Can See Them</mark></h1>
      <p class="subheadline">Rhythms, blocks, MI and electrolytes explained with pictures on real patient tracings. One method in 8 steps, so the next strip on your monitor doesn't freeze you.</p>
      <a href="#offer" id="cta-hero" class="btn-cta">GET THE KIT FOR ${PRICE}</a>
      <p class="cta-small-print">{I_LOCK} Secure checkout · One-time payment · 30-day money-back guarantee</p>
    </div>
  </section>

  <!-- STATS BAR -->
  <section class="stats-bar">
    <div class="container">
      <div class="stats-grid">
        <div class="stat-item"><div class="icon">{I_EYE}</div><strong>Real tracings</strong><p>from 21,799 clinical EKGs, not drawn waves</p></div>
        <div class="stat-item"><div class="icon">{I_BOOKS}</div><strong>3 illustrated books</strong><p>EKGs, emergency drugs and lab tests, 224 pages</p></div>
        <div class="stat-item"><div class="icon">{I_PHONE}</div><strong>Made for your phone</strong><p>one idea per page, study in 5 minutes</p></div>
      </div>
    </div>
  </section>

  <!-- PREVIEWS -->
  <section class="section" aria-label="Sample pages">
    <div class="container">
      <h2 class="text-center">Here's What the Pages Look Like</h2>
      <p class="text-center section-sub-p">Real pages from the book. Swipe through:</p>
      {carousel()}
    </div>
  </section>

  <!-- REAL TRACINGS -->
  <section class="section section-alt section-snug-top">
    <div class="container">
      <h2 class="text-center">Why the Tracings Are Real, Not Drawn</h2>
      <div class="solution-content">
        <p class="text-center">Most books show perfect, hand-drawn waves: clean lines, no noise, every wave where it should be.</p>
        <p class="text-center">Then you get to the unit and the strip on the monitor <strong>looks nothing like what you studied</strong>.</p>
        <div class="pmv-card"><img src="./mockups/ekg/strip.webp" alt="Real lead II strip of atrial flutter with the sawtooth waves marked" width="1600" height="400" loading="lazy" decoding="async"></div>
        <p class="text-center">That's why every rhythm in this book comes from <strong>PTB-XL</strong>, a public database of <strong>21,799 clinical 12-lead EKGs</strong> read by cardiologists, and from the MIT-BIH arrhythmia databases.</p>
        <p class="text-center">They're printed on real EKG paper, at 25 mm/s and 10 mm/mV. The drawing around them shows you <strong>where to look</strong>; the tracing stays a real patient's.</p>
      </div>
    </div>
  </section>

  <!-- METHOD -->
  <section class="section">
    <div class="container">
      <h2 class="text-center">One Method, Every Strip</h2>
      <div class="solution-content">
        <p class="text-center">Instead of memorizing fifty patterns, you follow <strong>the same 8 steps</strong> in the same order: rate, rhythm, axis, P wave, PR, QRS, ST and T, QT.</p>
        <div class="pmv-suffix">
          <div><b>Rate</b><span>fast, slow or normal?</span></div>
          <div><b>Rhythm</b><span>regular or not?</span></div>
          <div><b>QRS</b><span>narrow or wide?</span></div>
          <div><b>ST</b><span>up, down or flat?</span></div>
        </div>
        <div class="solution-image">
          <img src="./amostras/ekg_03.webp" alt="The 8-step method to read an EKG, illustrated" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async">
        </div>
        <p class="text-center">Your brain <strong>stops searching at random</strong>. Every strip becomes a checklist, and whatever doesn't fit jumps out on its own.</p>
      </div>
    </div>
  </section>

  <!-- COMPARISON -->
  <section class="comparison-section fade-in visible" aria-label="Textbook versus illustrated page">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">The Difference Is Visual</span>
        <h2>Stop staring at a strip without knowing where to start:</h2>
      </div>
      <div class="comparison-grid">
        <div class="comparison-card bad-card">
          <div class="comparison-label bad">FROM THIS</div>
          <ul class="comparison-bullets bad-list"><li>Twelve leads and no order</li><li>You don't know where to look</li><li>The doubt comes when there's no time</li></ul>
          <img src="./img/textbook-dense.webp" alt="A dense textbook page with no illustrations" width="768" height="1029" loading="lazy" decoding="async">
        </div>
        <div class="comparison-card good-card">
          <div class="comparison-label good">TO THIS</div>
          <ul class="comparison-bullets good-list"><li>One rhythm per page</li><li>The drawing tells you what to find</li><li>You recognize it at a glance</li></ul>
          <img src="./amostras/ekg_04.webp" alt="Atrial fibrillation explained with illustrations on a real tracing" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <!-- CONTENTS -->
  <section class="subjects-section fade-in visible" aria-label="What's inside">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow eyebrow-inverse">What's Inside</span>
        <h2>3 Books, All Illustrated</h2>
        <p class="subjects-subtitle">Tap a book to see what it covers</p>
      </div>
      <div class="subjects-accordion fade-in visible" role="list">{accordion()}
      </div>
    </div>
  </section>

  <!-- BOOK + BONUSES + OFFER -->
  <section class="value-section">
    <div class="container">
      <h2 class="text-center">Here's Everything You Get:</h2>
      <div class="pmv-books-strip"><span>Reading EKGs Made Visual</span><span>Emergency Medications Illustrated</span><span>How to Read Lab Tests</span></div>
      <div class="bonus-grid" style="grid-template-columns:minmax(0,560px);justify-content:center">
        <div class="bonus-item-with-image">
          <div class="bonus-mockup"><img src="./mockups/ekg/book-ekg.webp" alt="Reading EKGs Made Visual" width="720" height="1000" loading="lazy" decoding="async"></div>
          <div class="bonus-text">
            <h3>THE BOOK: &ldquo;Reading EKGs Made Visual&rdquo;</h3>
            <p class="value">Value: ${VALUES["ekg"]}</p>
            <p>68 pages in 8 parts: <strong>the basics, rate and rhythm, arrhythmias, cardiac arrest rhythms, heart blocks, MI, electrolytes</strong> and six guided cases at the bedside.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/ekg_05.webp" alt="Shockable and non-shockable rhythms" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>Shockable or not?</figcaption></figure><figure><img src="./amostras/ekg_06.webp" alt="The territories of an MI" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>The territories of an MI</figcaption></figure></div>
          </div>
        </div>
      </div>

      <h2 class="text-center" style="margin-top:64px">Plus 2 Bonus Books</h2>
      <div class="bonus-grid">
        <div class="bonus-item-with-image">
          <div class="bonus-mockup"><img src="./mockups/ekg/bonus-em.webp" alt="Emergency Medications Illustrated Handbook" width="720" height="1000" loading="lazy" decoding="async"></div>
          <div class="bonus-text">
            <h3>BONUS 1: &ldquo;Emergency Medications Illustrated&rdquo;</h3>
            <p class="value">Value: ${VALUES["em"]}</p>
            <p>82 pages on the drugs you prepare when a strip becomes an emergency: <strong>adenosine, amiodarone, epinephrine, atropine</strong> and the rest of the crash cart.</p>
            <p style="margin-top:12px;">It completes the arrest and arrhythmia chapters: you recognize the rhythm, and you already know what gets drawn up.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/ekg_em1.webp" alt="Antiarrhythmics and the adult ACLS algorithm" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>The adult ACLS algorithm</figcaption></figure><figure><img src="./amostras/ekg_em2.webp" alt="Drug card: epinephrine" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>Drug card: epinephrine</figcaption></figure></div>
          </div>
        </div>
        <div class="bonus-item-with-image">
          <div class="bonus-mockup"><img src="./mockups/ekg/bonus-lab.webp" alt="How to Read Lab Tests" width="720" height="1000" loading="lazy" decoding="async"></div>
          <div class="bonus-text">
            <h3>BONUS 2: &ldquo;How to Read Lab Tests&rdquo;</h3>
            <p class="value">Value: ${VALUES["lab"]}</p>
            <p>74 pages to read a lab report: <strong>potassium, calcium, troponin</strong> and the CBC, with critical values, in US units.</p>
            <p style="margin-top:12px;">Read it next to the electrolytes chapter: a peaked T wave and a high potassium are the same emergency seen from two sides.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/ekg_lab1.webp" alt="Critical results" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>Critical results</figcaption></figure><figure><img src="./amostras/ekg_lab2.webp" alt="Test card: potassium" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>Test card: potassium</figcaption></figure></div>
          </div>
        </div>
      </div>

      <div class="decision-box" id="offer">
        <img src="./mockups/ekg/hero.webp" alt="{NAME}" class="db-mockup" width="1400" height="830" loading="lazy" decoding="async">
        <h3 class="db-title">{NAME}</h3>
        <ul class="db-checklist">
          <li><span class="db-check">{CHECK}</span>Reading EKGs Made Visual · 68 pages<span class="db-price-val">${VALUES["ekg"]}</span></li>
          <li><span class="db-check">{CHECK}</span>Bonus: Emergency Medications Illustrated<span class="db-price-val">${VALUES["em"]}</span></li>
          <li><span class="db-check">{CHECK}</span>Bonus: How to Read Lab Tests<span class="db-price-val">${VALUES["lab"]}</span></li>
        </ul>
        <div class="db-anchoring">
          <p class="db-old-price">Total Value: ${TOTAL}</p>
          <p class="db-new-price-label">Today Only:</p>
          <p class="db-new-price">${PRICE}</p>
          <span class="db-discount-badge">YOU SAVE ${TOTAL - PRICE}</span>
          <p class="pmv-compare">One-time payment. No subscription. Keep the files forever.</p>
        </div>
        <a href="{CHECKOUT}" data-checkout class="db-cta">YES, I WANT THE KIT FOR ${PRICE}</a>
        <div class="db-trust">
          <span class="db-trust-item"><span class="db-trust-icon"><svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg></span>Secure Purchase</span>
          <span class="db-trust-item"><span class="db-trust-icon"><svg viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1s3.1 1.39 3.1 3.1v2z"/></svg></span>Encrypted Checkout</span>
          <span class="db-trust-item"><span class="db-trust-icon"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></span>30-Day Guarantee</span>
        </div>
        <p class="db-small-print">Price in USD. All three books are delivered by email right after purchase.</p>
      </div>
    </div>
  </section>

  <!-- WHO IS THIS FOR -->
  <section class="section">
    <div class="container">
      <h2 class="text-center">Is This Kit for You?</h2>
      <div class="paraquem-grid">
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/ekg-persona-student.webp" alt="Nursing student studying an EKG strip" loading="lazy" width="900" height="672">
          <div class="paraquem-info"><h3>You're a nursing student</h3><p>EKGs show up in med-surg, clinicals and exams, and the textbook explains them as if you already knew. You need to start from the paper and get to MI without skipping a step.</p></div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/ekg-persona-tele.webp" alt="New nurse at a telemetry station" loading="lazy" width="900" height="672">
          <div class="paraquem-info"><h3>You're starting on telemetry</h3><p>The monitor alarms, the rhythm changes, and you're the first to see it. You want to know in seconds if it's artifact or if you need to call right now.</p></div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/ekg-persona-bedside.webp" alt="Nurse reading an EKG at the bedside" loading="lazy" width="900" height="672">
          <div class="paraquem-info"><h3>You want a fast, safe review</h3><p>On nights, in the ER or on the floor, you read strips on your own. You need a method you trust and a quick refresher on blocks, ischemia and electrolytes.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- AUTHOR -->
  <section class="section author-section">
    <div class="container">
      <h2 class="text-center">Who's Behind Med Study Lab</h2>
      <div class="author-content">
        <div class="author-image"><img src="./Img-Leandro.webp" alt="Leandro Moretti, pharmacist and founder of Med Study Lab" width="266" height="400" loading="lazy" decoding="async"></div>
        <div class="author-bio">
          <h3>Leandro Moretti</h3>
          <h4>Pharmacist · Founder of Med Study Lab</h4>
          <p>Pharmacist and founder of Med Study Lab, a series of illustrated study books for healthcare students.</p>
          <p>The method is always the same: <strong>one idea per page, and a drawing that does the explaining</strong>, because what your brain sees organized, it remembers.</p>
          <p>For EKGs there was one more rule: a drawn tracing teaches you to recognize a drawing. That's why <strong>every rhythm strip in the book is a real recording</strong>.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- GUARANTEE -->
  <section class="section section-alt">
    <div class="container">
      <div class="guarantee-box">
        <div class="icon">{I_SHIELD}</div>
        <h3>30-Day Money-Back Guarantee</h3>
        <p>Use the kit for 30 days. If it doesn't help you, email us and <strong>you get 100% of your money back</strong>.</p>
        <p>No questions, no fine print.</p>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section">
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
      <p>EKGs don't have to be the part you avoid.</p>
      <p>You don't need to memorize fifty patterns. You need <strong>a method you follow every time</strong>, on tracings that look like the ones on your monitor.</p>
      <p style="font-size: 22px; font-weight: 700; margin-top: 32px;">3 illustrated books. A ${TOTAL} value, today ${PRICE}.</p>
      <div class="cta-summary">
        <ul>
          <li>One-time payment: ${PRICE}</li>
          <li>30-day money-back guarantee</li>
          <li>Instant PDF download</li>
        </ul>
      </div>
      <a href="#offer" class="btn-cta">GET THE KIT FOR ${PRICE}</a>
    </div>
  </section>

  <!-- FOOTER -->
{footer}
  <p style="text-align:center;font-size:11px;opacity:.55;margin:8px 16px 16px;">EKG tracings from PTB-XL (Wagner et al., PhysioNet, CC BY 4.0) and the MIT-BIH databases (PhysioNet).</p>
"""


def schema():
    faq = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
           for q, a in FAQ]
    d = {"@context": "https://schema.org", "@graph": [
        {"@type": "Product", "name": NAME,
         "description": ("Reading EKGs Made Visual (68 pages on real tracings) with two bonus books: "
                         "Emergency Medications Illustrated and How to Read Lab Tests. US edition."),
         "image": "https://www.medicalstudylab.com/mockups/ekg/hero.webp",
         "brand": {"@type": "Brand", "name": "Med Study Lab"},
         "offers": {"@type": "Offer", "price": str(PRICE), "priceCurrency": "USD",
                    "availability": "https://schema.org/InStock", "url": CHECKOUT,
                    "hasMerchantReturnPolicy": {
                        "@type": "MerchantReturnPolicy",
                        "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
                        "merchantReturnDays": 30, "applicableCountry": "US"}}},
        {"@type": "FAQPage", "mainEntity": faq}]}
    return '<script type="application/ld+json">\n' + json.dumps(d, ensure_ascii=False) + "\n  </script>"


def head(t):
    h = t[:t.index("</head>")]
    subs = [
        (r"<title>.*?</title>", "<title>EKGs Finally Make Sense: Rhythm Strips Explained on Real Tracings | Med Study Lab</title>"),
        (r'<meta name="description" content=".*?">',
         f'<meta name="description" content="Rhythms, blocks, MI and electrolytes explained with pictures on real patient tracings. 3 illustrated books for nurses, US edition. ${PRICE} one-time, 30-day guarantee.">'),
        (r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{URL}">'),
        (r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{URL}">'),
        (r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="EKG Made Visual Kit | Med Study Lab">'),
        (r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="EKGs finally make sense: an 8-step method on real tracings.">'),
        (r'<meta property="og:image" content=".*?">', '<meta property="og:image" content="https://www.medicalstudylab.com/mockups/ekg/og.jpg">'),
        (r'<meta property="og:image:alt" content=".*?">', '<meta property="og:image:alt" content="EKG Made Visual Kit: 3 illustrated books">'),
        (r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="EKG Made Visual Kit | Med Study Lab">'),
        (r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="Reading EKGs Made Visual + Emergency Medications + How to Read Lab Tests.">'),
        (r'<meta name="twitter:image" content=".*?">', '<meta name="twitter:image" content="https://www.medicalstudylab.com/mockups/ekg/og.jpg">'),
        (r'<script type="application/ld\+json">.*?</script>', schema()),
        (r'<meta name="robots" content=".*?">',
         '<meta name="robots" content="index, follow">' if LIVE else '<meta name="robots" content="noindex, follow">'),
    ]
    for rx, new in subs:
        h, n = re.subn(rx, lambda _m: new, h, count=1, flags=re.S)
        if n != 1:
            raise SystemExit(f"not found in usd.html head: {rx}")
    return h + EXTRA_CSS + "</head>\n<body>\n"


def tail(t):
    a = t.index("<!-- Carousels Script -->")
    b = t.index("<!-- Recent Purchase Toast Script -->")
    item = json.dumps({"item_id": SLUG, "item_name": NAME, "price": PRICE, "currency": "USD", "quantity": 1})
    fb = json.dumps({"content_ids": [SLUG], "content_name": NAME, "content_type": "product",
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
    return analytics + "  " + t[a:b] + "\n</body>\n</html>\n"


def main():
    t = io.open(os.path.join(SITO, "usd.html"), encoding="utf-8").read()
    footer = re.search(r'  <footer class="footer">.*?</footer>', t, re.S).group(0)
    footer = footer.replace("MedStudyLab · All rights reserved",
                            "Med Study Lab · All rights reserved")
    footer = footer.replace("</div>\n  </footer>",
                            '<p style="margin:10px 0 0;font-size:11px;opacity:.6;">NCLEX® is a registered trademark of the National Council of State Boards of Nursing (NCSBN), which is not affiliated with Med Study Lab.</p>\n    </div>\n  </footer>')
    html = head(t) + body(footer) + tail(t)
    for bad in ("spToast", "Manchester"):
        assert bad not in html.split("</head>", 1)[1], f"leftover from usd.html: {bad}"
    for src in set(re.findall(r'src="\./([^"]+)"', html)):
        assert os.path.exists(os.path.join(SITO, src)), f"missing image: {src}"
    io.open(os.path.join(SITO, f"{SLUG}.html"), "w", encoding="utf-8", newline="\n").write(html)
    print(f"{SLUG}.html: {len(html) // 1024} KB · ${PRICE} · {'LIVE' if LIVE else 'noindex'}")


if __name__ == "__main__":
    main()

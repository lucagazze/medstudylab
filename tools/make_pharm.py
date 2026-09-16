# -*- coding: utf-8 -*-
"""
Builds pharm.html — the Pharm Made Visual Kit, for the United States.

The <head> (all the CSS) and the carousel / accordion / FAQ scripts are
taken from usd.html, so a style fix there reaches this page on rebuild.
The body is written here.

Deliberately NOT carried over from usd.html, because in the US they are
FTC problems (fake reviews rule, 16 CFR 465; deceptive pricing, 16 CFR 233):
  - the "Sarah from Manchester just purchased" toast (invented buyers)
  - the "+11,978 students" counters and the testimonial carousel
  - (value anchor: Luca chose "Total Value $91 / Today $27", 16/09/2026)
  - "Valid until today" (a deadline that resets every day)

The bonus Dosage Calculations Made Visual is being finished: the page says
so BEFORE checkout and gives the delivery window (GIORNI).

  python tools/make_pharm.py
"""
import io
import json
import os
import re

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SLUG = "pharm"
NAME = "Pharm Made Visual Kit"
PRICE = 27
TOTAL = 91
# per-book values shown in the offer box (sum = TOTAL): decided by Luca 16/09/2026
VALUES = {"ph": 37, "rr": 24, "dc": 17, "gl": 13}
assert sum(VALUES.values()) == TOTAL
GIORNI = 3
CHECKOUT = "https://checkout.medicalstudylab.com/checkout/pharm-made-visual"
URL = f"https://www.medicalstudylab.com/{SLUG}"
LIVE = False          # True once the checkout product exists -> indexable

PAGES_W, PAGES_H = 1100, 1556

PREVIEWS = [
    ("pmv_01", "Antihypertensives: four suffixes, one page"),
    ("pmv_05", "The mechanism, drawn"),
    ("pmv_03", "Every route at a glance"),
    ("pmv_04", "The ADME map"),
    ("pmv_06", "The therapeutic window"),
    ("pmv_02", "Heart: rhythm and digoxin"),
    ("pmv_07", "The interactions worth knowing by heart"),
    ("pmv_08", "The five classes side by side"),
    ("pmv_09", "The errors that cost marks"),
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
    ("1", "Pharmacology Illustrated", "72 pages", [
        "Part I · The language: dose, strength, indications, dosage forms, generic and brand names",
        "Part II · How it gets in: every route, enteral, parenteral, topical and inhaled",
        "Part III · Pharmacokinetics: the ADME map, bioavailability, protein binding, the liver, half-life",
        "Part IV · Pharmacodynamics: receptors, agonists and antagonists, the dose-response curve",
        "Part V · Safety: the therapeutic window, side effects, age, kidney and liver",
        "Part VI · Interactions, system by system: pain, heart, nervous system, infections, hormones",
        "Glossary, prescription abbreviations and index"]),
    ("2", "Rapid Review Cards in Pharmacology", "40 pages", [
        "Antihypertensives: -pril, -sartan, -olol, -dipine",
        "NSAIDs",
        "Antibiotics",
        "Benzodiazepines",
        "Opioids",
        "For each class: the class on one page, the mechanism, use and avoid, the harms, the interactions, a flash recap",
        "The five classes side by side, twenty questions that keep coming back, the errors that cost marks"]),
    ("3", "Bonus: Dosage Calculations Made Visual", "new", [
        "The basics: units, conversions, pounds to kilograms, dimensional analysis",
        "Oral and weight-based doses, safe dose ranges for children",
        "Vials, reconstitution, insulin and heparin units",
        "IV math: mL/hr, drops per minute, infusion time, mcg/kg/min",
        "Safety: trailing and leading zeros, high-alert drugs, practice problems with answers"]),
    ("4", "Bonus: The Words of Clinical Pharmacy", "38 pages", [
        "104 terms explained with illustrations, A to Z",
        "Every entry: what it is, why it matters, what it looks like"]),
]

FAQ = [
    ("How will I receive the material?",
     "Right after purchase you get an email with your download link for Pharmacology "
     "Illustrated, the Rapid Review Cards and The Words of Clinical Pharmacy. Dosage "
     f"Calculations Made Visual is being finished and arrives at the same email within "
     f"{GIORNI} days. Everything is a high-resolution PDF."),
    ("Is this a one-time payment or a subscription?",
     f"One-time payment of ${PRICE}. No subscription, no recurring charges. You keep the "
     "files forever."),
    ("Is it written for nursing school in the US?",
     "Yes. This is the US edition: drug names are the ones on FDA labels (acetaminophen, "
     "epinephrine, albuterol) and the dosage math uses US units and conventions, including "
     "pounds to kilograms and the Joint Commission rules on zeros."),
    ("Can I study on my phone?",
     "Yes. Every page is one topic on one screen, so it reads well on a phone, a tablet or "
     "printed out."),
    ("Is this an NCLEX course?",
     "No. It is a visual study companion for your pharmacology and dosage calculation "
     "classes. The concepts are the same ones exam questions are built on, but we are not "
     "affiliated with NCSBN and no book can promise a passing score."),
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
      <span class="promo-time">4 illustrated books · ${TOTAL} value, today ${PRICE}</span>
    </div>
  </div>

  <!-- HERO -->
  <section class="hero">
    <div class="hero-content">
      <div class="hero-mockup">
        <img src="./mockups/pmv/hero.webp" alt="Pharm Made Visual Kit: Pharmacology Illustrated, Rapid Review Cards, Dosage Calculations Made Visual and The Words of Clinical Pharmacy"
             width="1400" height="830" loading="eager" fetchpriority="high" decoding="async">
      </div>
      <p class="hero-social"><span><strong>For nursing students</strong> · US edition · instant PDF download</span></p>
      <h1>Pharmacology Finally Makes Sense <mark>When You Can See It</mark></h1>
      <p class="subheadline">Drug classes, suffixes, side effects and the dosage math your nursing program tests, explained with pictures. One idea per page, made to study on your phone between shifts, classes and everything else.</p>
      <a href="#offer" id="cta-hero" class="btn-cta">GET THE KIT FOR ${PRICE}</a>
      <p class="cta-small-print">{I_LOCK} Secure checkout · One-time payment · 30-day money-back guarantee</p>
    </div>
  </section>

  <!-- STATS BAR -->
  <section class="stats-bar">
    <div class="container">
      <div class="stats-grid">
        <div class="stat-item"><div class="icon">{I_BOOKS}</div><strong>4 illustrated books</strong><p>pharmacology, the 5 classes that come up most, dosage calc and a glossary</p></div>
        <div class="stat-item"><div class="icon">{I_EYE}</div><strong>One idea per page</strong><p>a drawing does the explaining, the text stays short</p></div>
        <div class="stat-item"><div class="icon">{I_PHONE}</div><strong>Made for your phone</strong><p>study in 5 minutes, print it if you prefer paper</p></div>
      </div>
    </div>
  </section>

  <!-- PREVIEWS -->
  <section class="section" aria-label="Sample pages">
    <div class="container">
      <h2 class="text-center">Here's What the Pages Look Like</h2>
      <p class="text-center section-sub-p">Real pages from the kit. Swipe through:</p>
      {carousel()}
    </div>
  </section>

  <!-- SUFFIXES -->
  <section class="section section-alt section-snug-top">
    <div class="container">
      <h2 class="text-center">Stop Memorizing Drugs One by One</h2>
      <div class="solution-content">
        <p class="text-center">Your pharm exam can throw hundreds of drug names at you. Learning them one at a time is how you run out of time.</p>
        <p class="text-center">The trick nurses use: <strong>the ending of the name tells you the family</strong>. Learn the family once, and every drug that ends the same way comes with it.</p>
        <div class="pmv-suffix">
          <div><b>-pril</b><span>ACE inhibitors</span></div>
          <div><b>-sartan</b><span>ARBs</span></div>
          <div><b>-olol</b><span>beta blockers</span></div>
          <div><b>-dipine</b><span>calcium channel blockers</span></div>
        </div>
        <div class="solution-image">
          <img src="./amostras/pmv_01.webp" alt="Antihypertensives: the four suffixes on one illustrated page" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async">
        </div>
        <p class="text-center">That's how the whole kit works: the class on one page, how it works in one drawing, <strong>what can go wrong and what to watch for</strong>.</p>
      </div>
    </div>
  </section>

  <!-- DOSAGE CALC -->
  <section class="section">
    <div class="container">
      <h2 class="text-center">The Math Test You Can't Afford to Fail</h2>
      <div class="solution-content">
        <p class="text-center">Many nursing programs require <strong>90% or even 100%</strong> on the dosage calculation exam, with a limited number of attempts.</p>
        <p class="text-center">One decimal point in the wrong place and the answer is wrong, no partial credit.</p>
        <div class="pmv-card"><img src="./mockups/pmv/card-weight_based.webp" alt="Worked example: weight-based acetaminophen dose for a 44 lb child" width="1600" height="691" loading="lazy" decoding="async"></div>
        <p class="text-center">Dosage Calculations Made Visual walks you through every type of problem <strong>the same way, step by step</strong>: pounds to kilograms, dimensional analysis, drops per minute, mcg/kg/min.</p>
        <p class="text-center">Every worked example in the book is <strong>calculated and double-checked by software</strong> before it goes on the page, so you learn from numbers you can trust.</p>
        <div class="pmv-card"><img src="./mockups/pmv/card-dopamine.webp" alt="Worked example: dopamine drip from mcg/kg/min to mL/hr" width="1600" height="619" loading="lazy" decoding="async"></div>
      </div>
    </div>
  </section>

  <!-- COMPARISON -->
  <section class="comparison-section fade-in visible" aria-label="Textbook versus illustrated page">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">The Difference Is Visual</span>
        <h2>Same content. A very different night of studying:</h2>
      </div>
      <div class="comparison-grid">
        <div class="comparison-card bad-card">
          <div class="comparison-label bad">FROM THIS</div>
          <ul class="comparison-bullets bad-list"><li>Walls of text</li><li>You reread the same paragraph three times</li><li>Gone by exam day</li></ul>
          <img src="./img/textbook-dense.webp" alt="A dense textbook page with no illustrations" width="768" height="1029" loading="lazy" decoding="async">
        </div>
        <div class="comparison-card good-card">
          <div class="comparison-label good">TO THIS</div>
          <ul class="comparison-bullets good-list"><li>One idea per page</li><li>The drawing explains it</li><li>You remember the picture</li></ul>
          <img src="./amostras/pmv_04.webp" alt="The ADME map, illustrated" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <!-- CONTENTS -->
  <section class="subjects-section fade-in visible" aria-label="What's inside">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow eyebrow-inverse">What's Inside</span>
        <h2>4 Books, All Illustrated</h2>
        <p class="subjects-subtitle">Tap a book to see what it covers</p>
      </div>
      <div class="subjects-accordion fade-in visible" role="list">{accordion()}
      </div>
    </div>
  </section>

  <!-- THE TWO BOOKS (dark background: the bonus-* classes are styled for it) -->
  <section class="value-section">
    <div class="container">
      <h2 class="text-center">Here's Everything You Get:</h2>
      <div class="pmv-books-strip"><span>Pharmacology Illustrated</span><span>Rapid Review Cards</span><span>Dosage Calculations Made Visual</span><span>The Words of Clinical Pharmacy</span></div>
      <div class="bonus-grid">
        <div class="bonus-item-with-image">
          <div class="bonus-mockup"><img src="./mockups/pmv/book-ph.webp" alt="Pharmacology Illustrated" width="720" height="1000" loading="lazy" decoding="async"></div>
          <div class="bonus-text">
            <h3>BOOK 1: &ldquo;Pharmacology Illustrated&rdquo;</h3>
            <p>72 pages that build pharmacology from the ground up: <strong>the language, how drugs get in, pharmacokinetics, pharmacodynamics, safety and interactions</strong> system by system.</p>
            <p style="margin-top:12px;">It's the foundation that makes every drug class easier to learn.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/pmv_03.webp" alt="Every route at a glance" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>Every route at a glance</figcaption></figure><figure><img src="./amostras/pmv_07.webp" alt="The interactions worth knowing by heart" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>Interactions worth knowing</figcaption></figure></div>
          </div>
        </div>
        <div class="bonus-item-with-image">
          <div class="bonus-mockup"><img src="./mockups/pmv/book-rr.webp" alt="Rapid Review Cards in Pharmacology" width="720" height="1000" loading="lazy" decoding="async"></div>
          <div class="bonus-text">
            <h3>BOOK 2: &ldquo;Rapid Review Cards in Pharmacology&rdquo;</h3>
            <p>30 cards on the five classes that come up most: <strong>antihypertensives, NSAIDs, antibiotics, benzodiazepines and opioids</strong>.</p>
            <p style="margin-top:12px;">Mechanism, use and avoid, harms and interactions for each class, plus twenty questions that keep coming back.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/pmv_08.webp" alt="The five classes side by side" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>The five classes side by side</figcaption></figure><figure><img src="./amostras/pmv_09.webp" alt="The errors that cost marks" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>The errors that cost marks</figcaption></figure></div>
          </div>
        </div>
      </div>

      <!-- BONUSES + OFFER (same dark section) -->
      <h2 class="text-center" style="margin-top:64px">Plus 2 Bonus Books</h2>
      <div class="bonus-grid">
        <div class="bonus-item-with-image">
          <div class="bonus-mockup"><img src="./mockups/pmv/bonus-dc.webp" alt="Dosage Calculations Made Visual" width="720" height="1000" loading="lazy" decoding="async"></div>
          <div class="bonus-text">
            <span class="pmv-new">NEW</span>
            <h3>BONUS 1: &ldquo;Dosage Calculations Made Visual&rdquo;</h3>
            <p>Nursing math explained with pictures: <strong>conversions, dimensional analysis, weight-based and pediatric doses, reconstitution, drops per minute and mcg/kg/min</strong>, with practice problems and answers.</p>
            <p style="margin-top:12px;"><strong>Heads up:</strong> this book is being finished. It arrives at your email within {GIORNI} days of purchase; the other three books are instant.</p>
            <div class="pmv-mini"><img src="./mockups/pmv/card-drops.webp" alt="Worked example: drops per minute" width="1600" height="655" loading="lazy" decoding="async"><img src="./mockups/pmv/card-dimensional.webp" alt="Worked example: dimensional analysis" width="1600" height="619" loading="lazy" decoding="async"><span>Two worked examples from the book</span></div>
          </div>
        </div>
        <div class="bonus-item-with-image">
          <div class="bonus-mockup"><img src="./mockups/pmv/bonus-gl.webp" alt="The Words of Clinical Pharmacy" width="720" height="1000" loading="lazy" decoding="async"></div>
          <div class="bonus-text">
            <h3>BONUS 2: &ldquo;The Words of Clinical Pharmacy&rdquo;</h3>
            <p>104 terms explained with illustrations, from A to Z. <strong>Look a word up in seconds</strong> when a lecture or a chart loses you.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/pmv_gl1.webp" alt="How a definition is built" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>How every entry works</figcaption></figure><figure><img src="./amostras/pmv_gl2.webp" alt="Glossary entries D to E" width="{PAGES_W}" height="{PAGES_H}" loading="lazy" decoding="async"><figcaption>Entries D&ndash;E</figcaption></figure></div>
          </div>
        </div>
      </div>

      <div class="decision-box" id="offer">
        <img src="./mockups/pmv/hero.webp" alt="{NAME}" class="db-mockup" width="1400" height="830" loading="lazy" decoding="async">
        <h3 class="db-title">{NAME}</h3>
        <ul class="db-checklist">
          <li><span class="db-check">{CHECK}</span>Pharmacology Illustrated · 72 pages<span class="db-price-val">${VALUES["ph"]}</span></li>
          <li><span class="db-check">{CHECK}</span>Rapid Review Cards · 40 pages<span class="db-price-val">${VALUES["rr"]}</span></li>
          <li><span class="db-check">{CHECK}</span>Bonus: Dosage Calculations Made Visual<span class="db-price-val">${VALUES["dc"]}</span></li>
          <li><span class="db-check">{CHECK}</span>Bonus: The Words of Clinical Pharmacy<span class="db-price-val">${VALUES["gl"]}</span></li>
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
        <p class="db-small-print">Price in USD. Dosage Calculations Made Visual is delivered by email within {GIORNI} days; the other books right after purchase.</p>
      </div>
    </div>
  </section>

  <!-- WHO IS THIS FOR -->
  <section class="section">
    <div class="container">
      <h2 class="text-center">Is This Kit for You?</h2>
      <div class="paraquem-grid">
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/pmv-persona-pharm.webp" alt="Nursing student studying in the library" loading="lazy" width="900" height="672">
          <div class="paraquem-info"><h3>You're in pharm this semester</h3><p>ADN or BSN, the drug list keeps growing and the exam is close. You need the classes to click, not another chapter to reread.</p></div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/pmv-persona-gaps.webp" alt="Nursing student and mom studying on her phone at night" loading="lazy" width="900" height="672">
          <div class="paraquem-info"><h3>You study in the gaps</h3><p>Work, kids, clinicals. Your study time is 10 minutes on your phone. One page, one idea, done.</p></div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/pmv-persona-calc.webp" alt="Nursing student preparing a medication in the skills lab" loading="lazy" width="900" height="672">
          <div class="paraquem-info"><h3>Your dosage calc exam is coming</h3><p>You know the formulas exist; you just don't trust yourself with them yet. You need the same method for every problem.</p></div>
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
          <p>For dosage calculations there was one more rule: <strong>no number is typed by hand</strong>. Every worked example is calculated and checked by software before it goes on the page.</p>
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
      <p>Pharmacology doesn't have to be the class that keeps you up at night.</p>
      <p>You don't need to memorize every drug. You need to <strong>see how they're grouped</strong>, and a method for the math that works every time.</p>
      <p style="font-size: 22px; font-weight: 700; margin-top: 32px;">4 illustrated books. A ${TOTAL} value, today ${PRICE}.</p>
      <div class="cta-summary">
        <ul>
          <li>One-time payment: ${PRICE}</li>
          <li>30-day money-back guarantee</li>
          <li>Dosage Calc delivered within {GIORNI} days</li>
        </ul>
      </div>
      <a href="#offer" class="btn-cta">GET THE KIT FOR ${PRICE}</a>
    </div>
  </section>

  <!-- FOOTER -->
{footer}
"""


def schema():
    faq = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
           for q, a in FAQ]
    d = {"@context": "https://schema.org", "@graph": [
        {"@type": "Product", "name": NAME,
         "description": ("Four illustrated nursing pharmacology books: Pharmacology Illustrated, "
                         "Rapid Review Cards, Dosage Calculations Made Visual and The Words of "
                         "Clinical Pharmacy. US edition."),
         "image": "https://www.medicalstudylab.com/mockups/pmv/hero.webp",
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
        (r"<title>.*?</title>", "<title>Pharm Made Visual: Nursing Pharmacology + Dosage Calc, Illustrated | Med Study Lab</title>"),
        (r'<meta name="description" content=".*?">',
         f'<meta name="description" content="Drug classes, suffixes, side effects and dosage calculations explained with pictures. 4 illustrated books for nursing students, US edition. ${PRICE} one-time, 30-day guarantee.">'),
        (r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{URL}">'),
        (r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{URL}">'),
        (r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Pharm Made Visual Kit | Med Study Lab">'),
        (r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Nursing pharmacology and dosage calc, finally explained with pictures.">'),
        (r'<meta property="og:image" content=".*?">', '<meta property="og:image" content="https://www.medicalstudylab.com/mockups/pmv/og.jpg">'),
        (r'<meta property="og:image:alt" content=".*?">', '<meta property="og:image:alt" content="Pharm Made Visual Kit: 4 illustrated books">'),
        (r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Pharm Made Visual Kit | Med Study Lab">'),
        (r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="4 illustrated books: pharmacology, drug classes, dosage calc and a glossary.">'),
        (r'<meta name="twitter:image" content=".*?">', '<meta name="twitter:image" content="https://www.medicalstudylab.com/mockups/pmv/og.jpg">'),
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
    for bad in ("11,978", "spToast", "Manchester"):
        assert bad not in html.split("</head>", 1)[1], f"leftover from usd.html: {bad}"
    for src in set(re.findall(r'src="\./([^"]+)"', html)):
        assert os.path.exists(os.path.join(SITO, src)), f"missing image: {src}"
    io.open(os.path.join(SITO, f"{SLUG}.html"), "w", encoding="utf-8", newline="\n").write(html)
    print(f"{SLUG}.html: {len(html) // 1024} KB · ${PRICE} · {'LIVE' if LIVE else 'noindex'}")


if __name__ == "__main__":
    main()

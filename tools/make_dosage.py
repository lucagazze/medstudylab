# -*- coding: utf-8 -*-
"""
Builds dosage.html — Dosage Calculations Made Visual kit (US).

Template: ekg.html (same <head> CSS, pixel/analytics, carousels, FAQ and
accordion scripts, section order). Only the content changes. Every claim
about the books comes from the delivered PDFs (Med Study Lab\\Ebooks\\USA):
the contents page (p. 4), "How to use this book" (p. 3) and the note on
p. 2 about how the examples were checked.

Images: python tools/assets_dosage.py
  python tools/make_dosage.py
"""
import html
import json
import os

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TITLE = "Dosage Calculations Made Visual"
SLUG = "dosage"
CHECKOUT = "https://checkout.medicalstudylab.com/checkout/dosage-calculations-made-visual"
URL = f"https://www.medicalstudylab.com/{SLUG}"
IMG = f"https://www.medicalstudylab.com/mockups/{SLUG}"

PRICE, TOTAL, VAL_EM, VAL_GL = 27, 91, 19, 17
VAL_MAIN = TOTAL - VAL_EM - VAL_GL  # 55

B1 = "Emergency Medications"
B2 = "The Words of Clinical Pharmacy"

# Contents page (p. 4) of the PDF: part, title, pages, topics.
PARTS = [
    ("I", "The Basics", "5-11", ["The five-step method", "The metric ladder",
                                 "Pounds, kilograms, mg and mcg", "Dimensional analysis",
                                 "Desired over have", "Rounding rules"]),
    ("II", "Oral and Weight-Based Doses", "12-17", ["Tablets and capsules", "Oral liquids",
                                                    "Weight-based doses", "Safe dose ranges",
                                                    "Body surface area"]),
    ("III", "Injections", "18-23", ["Drawing up from a vial", "Reconstituting powders", "Insulin",
                                    "Heparin", "Percent and ratio strengths"]),
    ("IV", "IV Calculations", "24-30", ["mL per hour", "Drops per minute", "Infusion time",
                                        "mcg/kg/min drips", "Heparin drips", "Working backward"]),
    ("V", "Safety and Practice", "31-36", ["Zeros and dangerous abbreviations",
                                          "High-alert drugs and the double check",
                                          "Practice problems (20 problems)", "Answers, worked out"]),
    ("&middot;", "At the end", "37-40", ["Formula sheet &mdash; p. 37", "Glossary &mdash; p. 38",
                                         "Sources &mdash; p. 39", "Index &mdash; p. 40"]),
]
BLURB = {
    "I": "The five-step method, the metric ladder, and both setups: dimensional analysis and desired over have.",
    "II": "Tablets, oral liquids, doses per kilogram, safe dose ranges and body surface area.",
    "III": "Vials, reconstituted powders, insulin in units, heparin and percent strengths.",
    "IV": "mL/hr, drops per minute, infusion time, mcg/kg/min and heparin drips, and working backward from the pump.",
    "V": "Trailing zeros, dangerous abbreviations, the double check, and 20 practice problems with the answers worked out.",
    "&middot;": "A formula sheet with every formula on one page, a glossary, sources and an index.",
}

FAQ = [
    ("How will I receive the material?",
     f"Right after purchase you get an automatic email with all three books: {TITLE} and the two bonus "
     f"books, {B1} and {B2}. They are high-resolution PDFs, ready to download, print or read on any device."),
    ("Is this a one-time payment or a subscription?",
     "One-time payment of $27. No installments, no recurring charges, no surprises. You pay once and the "
     "material is yours forever."),
    ("Does it teach dimensional analysis or desired over have?",
     "Both. Dimensional analysis has its own page, desired over have (D/H &times; Q) has the next one, and a "
     "side-by-side table shows they give the same answer. Use the one your program teaches: the five steps "
     "work with either."),
    ("Will it help me pass my program's dosage calculation exam?",
     "It covers oral doses, weight-based doses, injections, insulin, heparin and IV math, then gives you 20 "
     "practice problems with every answer worked out. Rounding rules and preferred methods vary between "
     "nursing programs, and the book says so: when they differ, follow your program. No book can promise a "
     "score, which is why you have 30 days to ask for a refund."),
    ("Does it replace my drug reference or the provider's order?",
     "No. It is a study book: the doses and products in the examples illustrate the methods. For a real "
     "patient you follow the prescriber's order, the product label, a current drug reference and your "
     "facility's policies."),
    ("Can I print the material?",
     "Yes, for personal use and without limits. The PDFs are high resolution, made to print, annotate and "
     "take to class, the skills lab or clinicals."),
]

CHECK_SVG = '<span class="db-check"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></span>'


def head(tpl_head):
    h = tpl_head
    rep = [
        ("<title>Reading EKGs Made Visual: the illustrated guide on real tracings | Med Study Lab</title>",
         f"<title>{TITLE}: nursing math explained with pictures | Med Study Lab</title>"),
        ('content="Rhythm, arrhythmias, blocks, MI and electrolytes in 68 illustrated pages on real EKGs, plus 2 bonus books. $27, 30-day guarantee."',
         'content="One five-step method for every dosage problem, from tablets to heparin drips: 40 illustrated pages, 20 practice problems, plus 2 bonus books. $27, 30-day guarantee."'),
        ('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex, nofollow">'),
        ('  <link rel="alternate" hreflang="en" href="https://www.medicalstudylab.com/">\n', ''),
        ('href="https://www.medicalstudylab.com/ekg"', f'href="{URL}"'),
        ('content="https://www.medicalstudylab.com/ekg"', f'content="{URL}"'),
        ('content="Reading EKGs Made Visual | Med Study Lab"', f'content="{TITLE} | Med Study Lab"'),
        ('content="Read an EKG without panicking: an 8-step method on real tracings, explained with pictures."',
         'content="Dosage calculations without the fear: one five-step method, every step shown with pictures."'),
        ("https://www.medicalstudylab.com/mockups/ekg/og.jpg", f"{IMG}/og.jpg"),
        ('content="Reading EKGs Made Visual — Med Study Lab"', f'content="{TITLE} — Med Study Lab"'),
        ('content="68 illustrated pages on real EKGs + 2 bonus books."',
         'content="40 illustrated pages, 20 practice problems + 2 bonus books."'),
    ]
    for a, b in rep:
        assert a in h, a[:60]
        h = h.replace(a, b)
    s = h.index('<script type="application/ld+json">')
    e = h.index("</script>", s) + len("</script>")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Product", "name": f"{TITLE} — illustrated guide", "brand": {"@type": "Brand", "name": "Med Study Lab"},
         "description": "40 illustrated pages on nursing dosage calculations: one five-step method for oral, "
                        "weight-based, injection and IV problems, with 20 practice problems. With two bonus books.",
         "image": f"{IMG}/hero.webp",
         "offers": {"@type": "Offer", "price": str(PRICE), "priceCurrency": "USD",
                    "availability": "https://schema.org/InStock", "url": CHECKOUT,
                    "hasMerchantReturnPolicy": {"@type": "MerchantReturnPolicy",
                                                "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
                                                "merchantReturnDays": 30, "applicableCountry": "US"}}},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}}
            for q, a in FAQ]}]}
    h = h[:s] + '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False) + "\n  </script>" + h[e:]
    return h


def body():
    acc = []
    for i, (num, name, pp, topics) in enumerate(PARTS, 1):
        items = "".join(f"<li>{t}</li>" for t in topics)
        acc.append(f'''        <div class="subject-item" data-open="false" role="listitem">
          <button class="subject-summary" type="button" aria-expanded="false" aria-controls="subj-content-{i}">
            <span class="subject-num" aria-hidden="true">{num}</span>
            <span class="subject-title">{name} <em style="font-style:normal;opacity:.6;font-weight:600">&middot; pp. {pp}</em></span>
            <span class="subject-icon" aria-hidden="true"></span>
          </button>
          <div class="subject-content" id="subj-content-{i}" role="region">
            <div class="subject-content-inner"><ul class="subject-content-list">{items}</ul></div>
          </div>
        </div>''')
    topics = []
    for num, name, pp, _ in PARTS:
        a, b = pp.split("-")
        topics.append(f'''        <div class="topic-item">
          <span class="topic-num">{num}</span>
          <div>
            <span class="topic-pages">pp. {a}&ndash;{b}</span>
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
    samples = [("dosage_01", "The metric ladder"), ("dosage_02", "Dimensional analysis"),
               ("dosage_03", "Drawing up from a vial"), ("dosage_04", "Insulin: units, not mL"),
               ("dosage_05", "mL per hour"), ("dosage_06", "mcg/kg/min drips")]
    sm = "\n".join(f'''          <article class="testimonial-item amostra-item" role="listitem">
            <img src="./amostras/{f}.webp" alt="{alt}" width="1100" height="1556" loading="lazy" decoding="async">
          </article>''' for f, alt in samples)
    testi = "\n".join(f'          <article class="testimonial-item" role="listitem"><img src="./depoimentos/testimonio-{i}.webp" alt="Feedback and reviews from students using MedStudyLab" width="1254" height="1254" loading="lazy" decoding="async"></article>' for i in range(1, 14))
    ico_lock = '<svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
    nav = lambda t, d, lab, pts: f'<button type="button" class="carousel-nav" data-dir="{d}" data-target="{t}" aria-label="{lab}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="{pts}"></polyline></svg></button>'
    P, N = "15 18 9 12 15 6", "9 18 15 12 9 6"
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
        <img src="./mockups/dosage/hero.webp" alt="{TITLE}, with {B1} and {B2} as bonus books"
             width="1400" height="830" loading="eager" fetchpriority="high" decoding="async">
      </div>
      <p class="hero-social">
        <span class="stars" aria-hidden="true">★★★★★</span>
        <span><strong>+11,978 students & healthcare professionals</strong></span>
      </p>
      <h1>The Easiest Way to Pass Your Dosage Calculation Exam <mark>Without Fearing the Math!</mark></h1>
      <p class="subheadline">For nursing students who need 90% or even 100% on the med math exam before they can give medications in clinicals: one five-step method for every problem, from tablets to heparin drips, explained with pictures.</p>
      <a href="#offer" id="cta-hero" class="btn-cta">I WANT TO STOP FEARING MED MATH</a>
      <p class="cta-small-print">
        {ico_lock} Secure checkout · Instant download · 30-day guarantee
      </p>
    </div>
  </section>

  <!-- STATS BAR -->
  <section class="stats-bar">
    <div class="container">
      <div class="stats-grid">
        <div class="stat-item">
          <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></div>
          <strong>One five-step method</strong>
          <p>read, units, set up, calculate, check: for every problem</p>
        </div>
        <div class="stat-item">
          <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg></div>
          <strong>40 illustrated pages</strong>
          <p>5 parts, from the metric ladder to mcg/kg/min drips</p>
        </div>
        <div class="stat-item">
          <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg></div>
          <strong>20 practice problems</strong>
          <p>with every answer worked out, line by line</p>
        </div>
      </div>
    </div>
  </section>

  <!-- PREVIEWS -->
  <section class="section" aria-label="Sample pages">
    <div class="container">
      <h2 class="text-center">Here's What the Pages You'll Study Look Like</h2>
      <p class="text-center section-sub-p">One skill per page, a worked example with every step shown, and the drawing that makes the units click. Look inside:</p>

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
  <section class="section section-alt section-snug-top" aria-label="Student Reviews">
    <div class="container">
      <h2 class="text-center" style="margin-bottom: 32px;">What Over 11,978+ Students Using MedStudyLab Have to Say:</h2>

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

  <!-- EVERY STEP SHOWN -->
  <section class="section section-alt section-snug-top">
    <div class="container">
      <h2 class="text-center">Why Every Example Shows Every Step</h2>
      <div class="solution-content">
        <p class="text-center">Most dosage chapters give you the formula and the final number, and leave the middle to you.</p>
        <p class="text-center">But the middle is <strong>where the exam is lost</strong>: a unit that didn't cancel, a pound that stayed a pound, a decimal rounded too early.</p>
        <div class="solution-image">
          <img src="./mockups/dosage/example.webp" alt="A worked example from the book: cephalexin 500 mg PO, on hand 250 mg per 5 mL, solved by dimensional analysis in four steps" width="1600" height="650" loading="lazy" decoding="async">
        </div>
        <p class="text-center">That's why every worked example is laid out the same way: <strong>the order, what's on hand, the setup, the calculation and the check</strong>, with the units canceling right on the page.</p>
        <p class="text-center">And before any of it went into the book, <strong>every worked example and every practice answer was calculated and verified by software</strong>. So when your answer doesn't match, you know which one to trust.</p>
        <p class="text-center" style="font-size: 22px; font-weight: 700; margin-top: 40px;">So you learn the method, not just the answer.</p>
      </div>
    </div>
  </section>

  <!-- COMPARISON -->
  <section class="comparison-section fade-in visible" aria-label="A page of formulas versus the illustrated page">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">The Difference Is Visual</span>
        <h2>Stop memorizing formulas you don't trust:</h2>
      </div>
      <div class="comparison-grid">
        <div class="comparison-card bad-card">
          <div class="comparison-label bad">FROM THIS</div>
          <ul class="comparison-bullets bad-list">
            <li>A different formula for every problem</li>
            <li>Units you never see cancel</li>
            <li>The mistake shows up on the exam</li>
          </ul>
          <img src="./img/textbook-dense.webp" alt="A dense textbook page full of formulas" width="768" height="1029" loading="lazy" decoding="async">
        </div>
        <div class="comparison-card good-card">
          <div class="comparison-label good">TO THIS</div>
          <ul class="comparison-bullets good-list">
            <li>The same five steps every time</li>
            <li>The drawing shows the units cancel</li>
            <li>A check step that catches the error</li>
          </ul>
          <img src="./amostras/dosage_02.webp" alt="Dimensional analysis explained with illustrations" width="1100" height="1556" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <!-- CONTENTS -->
  <section class="subjects-section fade-in visible" aria-label="Table of contents">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow eyebrow-inverse">Table of Contents</span>
        <h2>Take a Look at the 5 Parts, Page by Page</h2>
        <p class="subjects-subtitle">From the metric ladder to heparin drips and 20 practice problems: 40 pages, all illustrated</p>
      </div>
      <div class="subjects-accordion fade-in visible" role="list">
{chr(10).join(acc)}
      </div>
    </div>
  </section>

  <!-- SOLUTION -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">What If There Were an Easier Way?</h2>
      <div class="solution-content">
        <p class="text-center">Imagine this:</p>
        <p class="text-center">Instead of memorizing one formula for tablets, another for liquids and three more for drips...</p>
        <p class="text-center">...you follow <strong>the same five steps every time</strong>, in the same order: read, units, set up, calculate, check.</p>
        <div class="solution-image">
          <img src="./amostras/dosage_07.webp" alt="The five-step method for dosage calculations, illustrated" width="1100" height="1556" loading="lazy" decoding="async">
        </div>
        <p class="text-center">Your brain <strong>stops guessing which formula to use</strong>. Only the numbers change from problem to problem, and the check step tells you when something's off: half a tablet, fine; twenty tablets, stop.</p>
        <p class="text-center" style="font-size: 22px; font-weight: 700; margin-top: 40px;">That's exactly what {TITLE} does.</p>
        <p class="text-center">It isn't &ldquo;just another PDF&rdquo;. It's <strong>one method in 5 illustrated parts</strong>, from unit conversions to mcg/kg/min, so you <strong>understand the setup instead of memorizing forty formulas</strong>.</p>
        <p class="text-center">Because when the units line up, <strong>even a heparin drip is just five steps</strong>.</p>
      </div>
    </div>
  </section>

  <!-- MODULES -->
  <section class="section">
    <div class="container">
      <h2 class="text-center">Here's What You Get With {TITLE}:</h2>
      <div style="margin: 20px auto 28px;">
        <img src="./mockups/dosage/combo.webp" alt="{TITLE}: mockup with sample pages" width="1100" height="1620" loading="lazy" decoding="async" style="max-width: 480px; width: 100%; display: block; margin: 0 auto;">
      </div>
      <div class="topics-grid">
{chr(10).join(topics)}
      </div>
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
            <img src="./mockups/dosage/bonus-em.webp" alt="{B1}, illustrated handbook" width="720" height="1000" loading="lazy" decoding="async">
          </div>
          <div class="bonus-text">
            <h3>BONUS 1: &ldquo;{B1}&rdquo;, the illustrated handbook</h3>
            <p class="value">Standalone value: ${VAL_EM}</p>
            <p>82 pages and 25 drug cards on the crash cart: <strong>boluses, loading doses, mcg/kg/min infusions</strong> and the dilutions that cause the worst errors, like the two strengths of epinephrine.</p>
            <p style="margin-top: 12px;">It picks up where Part IV leaves off: the drips you learn to calculate, on the drugs where the math matters most.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/dosage_em1.webp" alt="Reading a dose: bolus, loading, micrograms/kg/min" width="1100" height="1556" loading="lazy" decoding="async"><figcaption>Reading a dose</figcaption></figure><figure><img src="./amostras/dosage_em2.webp" alt="The dilutions that kill" width="1100" height="1556" loading="lazy" decoding="async"><figcaption>The dilutions that kill</figcaption></figure></div>
          </div>
        </div>

        <div class="bonus-item-with-image">
          <div class="bonus-mockup">
            <img src="./mockups/dosage/bonus-gl.webp" alt="{B2}, illustrated glossary" width="720" height="1000" loading="lazy" decoding="async">
          </div>
          <div class="bonus-text">
            <h3>BONUS 2: &ldquo;{B2}&rdquo;</h3>
            <p class="value">Standalone value: ${VAL_GL}</p>
            <p>38 pages with <strong>104 terms explained with illustrations</strong>, four to a page, plus the words that get confused and the abbreviations you'll meet on a chart.</p>
            <p style="margin-top: 12px;">Read it next to Part V: q6h, PRN, subcut and the abbreviations that must never be used, all on one page.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/dosage_gl1.webp" alt="Abbreviations on a chart" width="1100" height="1556" loading="lazy" decoding="async"><figcaption>Abbreviations on a chart</figcaption></figure><figure><img src="./amostras/dosage_gl2.webp" alt="A glossary page: four terms explained with illustrations" width="1100" height="1556" loading="lazy" decoding="async"><figcaption>Four terms per page</figcaption></figure></div>
          </div>
        </div>
      </div>

      <!-- DECISION BOX -->
      <div class="decision-box" id="offer">
        <img src="./mockups/dosage/hero.webp" alt="{TITLE} with the two bonus books" class="db-mockup" width="1400" height="830" loading="lazy" decoding="async">
        <h3 class="db-title">{TITLE} + 2 Bonus Books</h3>
        <ul class="db-checklist">
          <li>{CHECK_SVG}{TITLE}: 40 illustrated pages<span class="db-price-val">${VAL_MAIN}</span></li>
          <li>{CHECK_SVG}Bonus 1: {B1}<span class="db-price-val">${VAL_EM}</span></li>
          <li>{CHECK_SVG}Bonus 2: {B2}<span class="db-price-val">${VAL_GL}</span></li>
          <li>{CHECK_SVG}High-resolution printable PDFs<span class="db-price-val">Included</span></li>
        </ul>
        <div class="db-anchoring">
          <p class="db-old-price">Total value: ${TOTAL}</p>
          <p class="db-new-price-label">Today only:</p>
          <p class="db-new-price">${PRICE}</p>
          <span class="db-discount-badge">YOU SAVE ${TOTAL - PRICE}</span>
        </div>
        <a href="{CHECKOUT}" data-checkout class="db-cta">YES, I WANT DOSAGE CALCULATIONS MADE VISUAL FOR ${PRICE}</a>
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
          <img class="paraquem-foto" src="./img/pmv-persona-pharm.webp" alt="Nursing student studying in the library" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>Nursing student before the dosage exam</h3>
            <p>Many programs require 90% or even 100% before you can give medications in clinicals. You need one method you trust, not a stack of formulas.</p>
          </div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/pmv-persona-gaps.webp" alt="Nursing student studying on her phone at night" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>Math was never your thing</h3>
            <p>One slip can mean retaking the exam, and that makes you freeze. You want every step shown, the units canceling on the page, and 20 problems to practice with the answers worked out.</p>
          </div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/pmv-persona-calc.webp" alt="Nursing student preparing a medication in the skills lab" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>In clinicals or a new grad</h3>
            <p>Insulin, heparin, pumps and drips are now real. You want a quick review of mL/hr and mcg/kg/min, and a formula sheet with everything on one page.</p>
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
          <p>Pharmacist and founder of Med Study Lab, the series of illustrated books for healthcare: pharmacology, clinical handbooks, lab tests, EKGs and now dosage calculations.</p>
          <p>The method is always the same: <strong>visual clarity and one topic per page</strong>, because what the brain sees organized, it remembers.</p>
          <p>For dosage math the formulas are simple; the mistakes come from units that don't cancel. That's why <strong>every problem in the book is solved with the same five steps</strong>, and every worked example was verified before it went on the page.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- RECAP -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">To Recap: Here's Everything You Get</h2>
      <ul class="recap-list">
        <li>{TITLE}: 40 illustrated pages in 5 parts, from the metric ladder to heparin drips, with 20 practice problems and a formula sheet</li>
        <li>Bonus 1: &ldquo;{B1}&rdquo;, illustrated handbook, 82 pages (value ${VAL_EM})</li>
        <li>Bonus 2: &ldquo;{B2}&rdquo;, 38 pages (value ${VAL_GL})</li>
        <li>Delivery: all 3 books by email right after purchase</li>
        <li>30-day guarantee, no questions asked: try it risk-free</li>
        <li>High-resolution PDFs: print them, annotate them, take them to class and clinicals</li>
      </ul>
      <div class="price-recap">
        <p class="old-price">${TOTAL}</p>
        <p class="new-price">${PRICE}</p>
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
      <div class="faq-container">
{chr(10).join(faq)}
      </div>
    </div>
  </section>

  <!-- FINAL CTA -->
  <section class="final-cta">
    <div class="container">
      <h2>One Last Thing Before You Decide...</h2>
      <p>Dosage math doesn't have to be the exam you dread.</p>
      <p>You don't have to memorize a formula for every kind of problem and hope you picked the right one.</p>
      <p>And you definitely <strong>don't have to find out on exam day that one unit didn't cancel</strong>.</p>
      <p style="font-size: 22px; font-weight: 700; margin-top: 32px;">There's an easier way. And it's one click away.</p>
      <p>Five steps, 20 practice problems and two bonus books.</p>
      <p><strong>Now it's your turn.</strong></p>
      <div class="cta-summary">
        <ul>
          <li>One-time payment: ${PRICE}</li>
          <li>Guarantee: 30 days, no questions asked</li>
          <li>Delivery: all 3 books right after purchase</li>
        </ul>
      </div>
      <a href="#offer" class="btn-cta">I WANT DOSAGE CALCULATIONS MADE VISUAL FOR ${PRICE}</a>
      <p class="cta-small-print" style="margin-top: 24px;">
        <svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/></svg> The books arrive by email within minutes
      </p>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container">
      <p>© 2026 Med Study Lab · All rights reserved · <a href="/refund-policy" style="color: rgba(255,255,255,0.7); text-decoration: underline; margin-left: 8px;">Refund Policy</a><a href="/privacy" style="color: rgba(255,255,255,0.7); text-decoration: underline; margin-left: 8px;">Privacy</a><a href="/terms" style="color: rgba(255,255,255,0.7); text-decoration: underline; margin-left: 8px;">Terms</a><a href="/support" style="color: rgba(255,255,255,0.7); text-decoration: underline; margin-left: 8px;">Support</a></p><p class="legal-entity" style="margin:12px 0 0;font-size:10.5px;line-height:1.7;letter-spacing:.12em;opacity:.5;">QUILLSTONE DIGITAL LLC<br>1057 NW 136TH AVE, MIAMI, FL 33182</p>
    </div>
  </footer>
'''


def tail(tpl_tail):
    t = tpl_tail
    rep = [('"item_id": "ekg", "item_name": "Reading EKGs Made Visual"', f'"item_id": "{SLUG}", "item_name": "{TITLE}"'),
           ('"content_ids": ["ekg"], "content_name": "Reading EKGs Made Visual"', f'"content_ids": ["{SLUG}"], "content_name": "{TITLE}"')]
    for a, b in rep:
        assert a in t, a
        t = t.replace(a, b)
    return t


def main():
    src = open(os.path.join(SITO, "ekg.html"), encoding="utf-8").read()
    i = src.index("<body>")
    j = src.index("  <!-- Dynamic Offer Date")
    out = head(src[:i]) + body() + tail(src[j:])
    open(os.path.join(SITO, "dosage.html"), "w", encoding="utf-8", newline="\n").write(out)
    print("dosage.html", len(out))


if __name__ == "__main__":
    main()

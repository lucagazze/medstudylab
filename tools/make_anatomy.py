# -*- coding: utf-8 -*-
"""
Builds anatomy.html — Clinical Anatomy Made Visual kit (US).

Template: ekg.html, like every other landing here. Only the content changes.

WHO THIS PAGE TALKS TO, AND WHY IT MATTERS. Every other landing on this
site is written for a student before an exam. The account data says that
is not who buys: over the last 30 days, 82% of US purchases came from
people over 45, 69% women, and the 18-24 bracket bought ONE unit across
every campaign. The dosage campaign, whose copy is aimed squarely at
nursing students, sold nothing at all under 35.

So this page is written for the nurse who has been doing the job for
years and wants the anatomy she uses in a shift — landmarks, injection
sites, coronary territories, catheter routes. Not A&P 1.

Part III is deliberately cardiac and deliberately tied to the EKG leads:
Reading EKGs Made Visual is the best seller in the US and its buyer is
this same reader.

Images: python tools/assets_anatomy.py
  python tools/make_anatomy.py
"""
import html
import json
import os

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TITLE = "Clinical Anatomy Made Visual"
SLUG = "anatomy"
CHECKOUT = "https://www.medicalstudylab.com/anatomy/checkout"  # checkout de la app (07/10/2026); el de Impultienda ya no se usa
URL = f"https://www.medicalstudylab.com/{SLUG}"
IMG = f"https://www.medicalstudylab.com/mockups/{SLUG}"

PRICE, TOTAL, VAL_EM, VAL_LAB = 27, 91, 19, 17
VAL_MAIN = TOTAL - VAL_EM - VAL_LAB  # 55
PAGES = 57

B1 = "Emergency Medications"
B2 = "How to Read Lab Tests"

# The contents, straight out of the book project's struttura.py.
PARTS = [
    ("I", "Landmarks You Find With Your Hands", "6-13",
     ["The four quadrants and what sits under each",
      "Where the organs actually are, front and back",
      "The chest wall: ribs and how to count the spaces",
      "The lung lobes on the chest wall",
      "The five places you listen to the heart",
      "Bowel sounds, quadrant by quadrant",
      "Liver edge, spleen and McBurney's point",
      "The bladder above the symphysis"]),
    ("II", "Where the Needle Goes", "15-22",
     ["Ventrogluteal: finding it, and the sciatic nerve",
      "Deltoid: the safe triangle and the axillary nerve",
      "Vastus lateralis",
      "Subcutaneous: what is under the pinch",
      "Intradermal: the layers, and why a wheal forms",
      "The antecubital fossa: veins, artery, nerve",
      "Veins of the hand and forearm for IV access",
      "The arm you do not use"]),
    ("III", "The Heart and the Vessels", "24-31",
     ["The chambers and the direction of flow",
      "The valves, and what each one sounds like",
      "The coronary arteries: RCA, LAD, circumflex",
      "Which artery feeds which wall, and which leads see it",
      "The conduction system",
      "The great vessels and the path of a central line",
      "The arterial pulses, one by one",
      "Where a blood pressure is actually measured"]),
    ("IV", "The Tubes We Put In", "33-39",
     ["The upper airway, nose to larynx",
      "Trachea and bronchi: why the right one catches everything",
      "Suctioning and intubation: the anatomy that matters",
      "The route of a nasogastric tube",
      "Esophagus or trachea: how you know you are wrong",
      "The female urethra: the landmarks",
      "The male urethra: two curves and the prostate"]),
    ("V", "Nerves, Spine and Skin", "41-47",
     ["The spine: curves, levels, counting vertebrae",
      "Lumbar puncture and epidural: what the needle passes",
      "Dermatomes: the map that explains the pain",
      "The brachial plexus, simply",
      "The layers of the skin",
      "Bony prominences and where the skin breaks",
      "The muscles you test for strength"]),
    ("VI", "What Is Under the Incision", "49-53",
     ["Abdominal surgery: the layers you go through",
      "Common incisions and what is behind them",
      "Hip and knee replacement",
      "Central line sites: IJ, subclavian, femoral",
      "Chest tube: the triangle of safety"]),
    ("&middot;", "At the end", "54-57",
     ["Surface landmark sheet &mdash; p. 54",
      "Glossary of directional terms &mdash; p. 55",
      "Sources &mdash; p. 56", "Index &mdash; p. 57"]),
]
BLURB = {
    "I": "The assessment, in the order you do it: quadrants, rib spaces, "
         "lung lobes, the five listening points, and the landmarks you find "
         "with your fingers instead of guessing by eye.",
    "II": "Every injection site with the nerve you are avoiding drawn "
          "underneath it, the antecubital veins around the brachial artery, "
          "and the arm you never use.",
    "III": "Chambers, valves and the three coronary arteries, then the page "
           "that ties each wall to its artery and to the leads that look at "
           "it.",
    "IV": "Airway, esophagus and urethra seen from the tube's side: why the "
          "right main bronchus catches everything, and the two curves that "
          "stop a catheter.",
    "V": "The spine by level, the dermatome map, the layers of the skin, "
         "and the bony prominences where pressure injuries start.",
    "VI": "The layers a scalpel goes through, the common incisions, the "
          "three central line sites and the triangle of safety.",
    "&middot;": "A one-page sheet of every surface landmark in the book, a "
                "glossary of directional terms, sources and an index.",
}

FAQ = [
    ("How will I receive the material?",
     f"Right after purchase you get an automatic email with all three books: "
     f"{TITLE} and the two bonus books, {B1} and {B2}. They are "
     f"high-resolution PDFs, ready to download, print or read on any device."),
    ("Is this a one-time payment or a subscription?",
     f"One-time payment of ${PRICE}. No installments, no recurring charges, "
     f"no surprises. You pay once and the material is yours forever."),
    ("Is this an anatomy and physiology textbook?",
     "No, and that is the point. It does not start at the cell and it does "
     "not cover physiology. It covers the anatomy you use in a shift: where "
     "to listen, where the needle goes, which artery feeds which wall, what "
     "a catheter passes through, where pressure injuries start. If you need "
     "to pass A&amp;P 1, a course textbook will serve you better."),
    ("I qualified years ago. Is it too basic?",
     "It is not a refresher on what a bone is called. Most of it is the "
     "clinical layer that a course skips: why the aortic area is on the "
     "right, why the old dorsogluteal site was abandoned, why an inferior "
     "infarct comes with bradycardia, why a catheter stops at six inches. "
     "Experienced nurses tell us those are the answers nobody ever gave "
     "them."),
    ("Does it replace my facility's policy or a clinical reference?",
     "No. It is a study book. Sites, techniques and devices vary between "
     "facilities, and the book says so: when they differ, follow your "
     "facility's policy and your provider's order."),
    ("Can I print the material?",
     "Yes, for personal use and without limits. The PDFs are high "
     "resolution, made to print, annotate and take onto the unit."),
]

CHECK_SVG = ('<span class="db-check"><svg viewBox="0 0 24 24">'
             '<polyline points="20 6 9 17 4 12"/></svg></span>')

DESCR = (f"The anatomy you use at the bedside in {PAGES} illustrated pages: "
         f"landmarks, injection sites, coronary territories and catheter "
         f"routes, plus 2 bonus books. ${PRICE}, 30-day guarantee.")


def head(tpl_head):
    h = tpl_head
    rep = [
        ("<title>Reading EKGs Made Visual: the illustrated guide on real "
         "tracings | Med Study Lab</title>",
         f"<title>{TITLE}: the anatomy you use at the bedside | "
         f"Med Study Lab</title>"),
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
         'content="Landmarks, injection sites and catheter routes: the '
         'anatomy you use in a shift, drawn."'),
        ("https://www.medicalstudylab.com/mockups/ekg/og.jpg", f"{IMG}/og.jpg"),
        ('content="Reading EKGs Made Visual — Med Study Lab"',
         f'content="{TITLE} — Med Study Lab"'),
        ('content="68 illustrated pages on real EKGs + 2 bonus books."',
         f'content="{PAGES} illustrated pages + 2 bonus books."'),
    ]
    for a, b in rep:
        assert a in h, a[:70]
        h = h.replace(a, b)
    s = h.index('<script type="application/ld+json">')
    e = h.index("</script>", s) + len("</script>")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Product", "name": f"{TITLE} — illustrated guide",
         "brand": {"@type": "Brand", "name": "Med Study Lab"},
         "description": f"{PAGES} illustrated pages of clinical anatomy for "
                        "practising nurses: surface landmarks, injection "
                        "sites, coronary territories and the leads that see "
                        "them, catheter routes and pressure points. With two "
                        "bonus books.",
         "image": f"{IMG}/hero.webp",
         "offers": {"@type": "Offer", "price": str(PRICE),
                    "priceCurrency": "USD",
                    "availability": "https://schema.org/InStock",
                    "url": CHECKOUT,
                    "hasMerchantReturnPolicy": {
                        "@type": "MerchantReturnPolicy",
                        "returnPolicyCategory":
                            "https://schema.org/MerchantReturnFiniteReturnWindow",
                        "merchantReturnDays": 30,
                        "applicableCountry": "US"}}},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": html.unescape(q),
             "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}}
            for q, a in FAQ]}]}
    h = (h[:s] + '<script type="application/ld+json">\n'
         + json.dumps(ld, ensure_ascii=False) + "\n  </script>" + h[e:])
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
    samples = [("anatomy_01", "The five places you listen to the heart"),
               ("anatomy_02", "Ventrogluteal: the landmarks and the sciatic nerve underneath"),
               ("anatomy_03", "Which coronary artery feeds which wall, and which leads see it"),
               ("anatomy_04", "The dermatome map, front and back"),
               ("anatomy_05", "The male urethra: the two curves a catheter has to pass"),
               ("anatomy_06", "Bony prominences in three positions")]
    sm = "\n".join(f'''          <article class="testimonial-item amostra-item" role="listitem">
            <img src="./amostras/{f}.webp" alt="{alt}" width="1100" height="1556" loading="lazy" decoding="async">
          </article>''' for f, alt in samples)
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
             width="1400" height="830" loading="eager" fetchpriority="high" decoding="async">
      </div>
      <p class="hero-social">
        <span class="stars" aria-hidden="true">★★★★★</span>
        <span><strong>+11,978 students & healthcare professionals</strong></span>
      </p>
      <h1>The Easiest Way to Understand Anatomy <mark>Without Memorizing It!</mark></h1>
      <p class="subheadline">For nurses and clinicians who learned anatomy years ago and use it every shift: the landmarks you find with your hands, the nerve under every injection site, which artery feeds which wall, and what a catheter passes through. {PAGES} pages, all illustrated.</p>
      <a href="#offer" id="cta-hero" class="btn-cta">I WANT THE ANATOMY I ACTUALLY USE</a>
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
          <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 11V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2"/><path d="M14 10V4a2 2 0 0 0-2-2a2 2 0 0 0-2 2v2"/><path d="M10 10.5V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/></svg></div>
          <strong>Landmarks you find by hand</strong>
          <p>every site drawn with the hand that finds it</p>
        </div>
        <div class="stat-item">
          <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg></div>
          <strong>{PAGES} illustrated pages</strong>
          <p>6 parts, from the five listening points to the triangle of safety</p>
        </div>
        <div class="stat-item">
          <div class="icon"><svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l3 8 4-16 3 8h4"/></svg></div>
          <strong>What is underneath, drawn</strong>
          <p>the nerve, the artery and the wall you cannot see</p>
        </div>
      </div>
    </div>
  </section>

  <!-- PREVIEWS -->
  <section class="section" aria-label="Sample pages">
    <div class="container">
      <h2 class="text-center">Here's What the Pages You'll Study Look Like</h2>
      <p class="text-center section-sub-p">One structure per page, the drawing that carries the logic, and the clinical reason underneath it. Look inside:</p>

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
      <h2 class="text-center">Why This Is Drawn and Not Listed</h2>
      <div class="solution-content">
        <p class="text-center">You already know the names. What a list never gives you is <strong>where a thing sits in relation to the thing beside it</strong>.</p>
        <p class="text-center">Three arteries, four walls and twelve leads is a paragraph you read twice and forget. The same thing in three panels, colour-coded, is a map you can rebuild from memory a year later:</p>
        <div class="solution-image">
          <img src="./mockups/{SLUG}/example.webp" alt="From the book: the coronary arteries, the wall each one feeds, and the leads that look at that wall, colour-coded across three panels" width="1600" height="650" loading="lazy" decoding="async">
        </div>
        <p class="text-center">Every page in the book works that way: <strong>the drawing carries the logic and the text is the caption</strong>, not the other way round.</p>
        <p class="text-center" style="font-size: 22px; font-weight: 700; margin-top: 40px;">So you can picture it at the bedside, not recite it.</p>
      </div>
    </div>
  </section>

  <!-- COMPARISON -->
  <section class="comparison-section fade-in visible" aria-label="An atlas page versus a clinical page">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow">The Difference Is Clinical</span>
        <h2>An atlas shows you the body. This shows you the shift:</h2>
      </div>
      <div class="comparison-grid">
        <div class="comparison-card bad-card">
          <div class="comparison-label bad">AN ATLAS</div>
          <ul class="comparison-bullets bad-list">
            <li>Every structure, in Latin, at the same importance</li>
            <li>Beautiful, and 600 pages you will not open on shift</li>
            <li>Never says which one you will actually touch</li>
          </ul>
          <img src="./img/textbook-dense.webp" alt="A dense anatomy textbook page" width="768" height="1029" loading="lazy" decoding="async">
        </div>
        <div class="comparison-card good-card">
          <div class="comparison-label good">THIS BOOK</div>
          <ul class="comparison-bullets good-list">
            <li>One page per thing you do at the bedside</li>
            <li>The hand that finds the landmark, drawn</li>
            <li>What is underneath, and what happens if you miss</li>
          </ul>
          <img src="./amostras/anatomy_02.webp" alt="The ventrogluteal site: the hand position above, the sciatic nerve underneath" width="1100" height="1556" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <!-- CONTENTS -->
  <section class="subjects-section fade-in visible" aria-label="Table of contents">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow eyebrow-inverse">Table of Contents</span>
        <h2>Take a Look at the 6 Parts, Page by Page</h2>
        <p class="subjects-subtitle">From the five places you listen to the heart to the triangle of safety: {PAGES} pages, all illustrated</p>
      </div>
      <div class="subjects-accordion fade-in visible" role="list">
{chr(10).join(acc)}
      </div>
    </div>
  </section>

  <!-- SOLUTION -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">What If You Could Just See It?</h2>
      <div class="solution-content">
        <p class="text-center">Think about the things you were shown once, years ago, and have done a thousand times since.</p>
        <p class="text-center">You find the ventrogluteal site correctly. But <strong>was anyone ever able to show you what is underneath it</strong>, and why the site you were first taught was abandoned?</p>
        <div class="solution-image">
          <img src="./amostras/anatomy_01.webp" alt="The five places you listen to the heart, with the rib spaces drawn" width="1100" height="1556" loading="lazy" decoding="async">
        </div>
        <p class="text-center">You listen in five places. Do you know <strong>why the aortic area is on the right</strong> when the aortic valve is on the left?</p>
        <p class="text-center" style="font-size: 22px; font-weight: 700; margin-top: 40px;">That's exactly what {TITLE} is.</p>
        <p class="text-center">It isn't an anatomy course and it isn't an atlas. It's <strong>the clinical layer</strong>: {PAGES} pages in 6 parts, each one a thing you do on shift, with the reason drawn beside it.</p>
        <p class="text-center">Because once you have seen what is under your hand, <strong>you stop doing it from memory and start doing it from understanding</strong>.</p>
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
            <img src="./mockups/{SLUG}/bonus-em.webp" alt="{B1}, illustrated handbook" width="720" height="1000" loading="lazy" decoding="async">
          </div>
          <div class="bonus-text">
            <h3>BONUS 1: &ldquo;{B1}&rdquo;, the illustrated handbook</h3>
            <p class="value">Standalone value: ${VAL_EM}</p>
            <p>82 pages and 25 drug cards on the crash cart: <strong>boluses, loading doses, mcg/kg/min infusions</strong> and the dilutions that cause the worst errors, like the two strengths of epinephrine.</p>
            <p style="margin-top: 12px;">It is the other half of Part III: you learn where the lines go and which wall is in trouble, and this is what runs through them.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/anatomy_em1.webp" alt="Reading a dose: bolus, loading, micrograms per kilo per minute" width="1100" height="1556" loading="lazy" decoding="async"><figcaption>Reading a dose</figcaption></figure><figure><img src="./amostras/anatomy_em2.webp" alt="The dilutions that cause the worst errors" width="1100" height="1556" loading="lazy" decoding="async"><figcaption>The dilutions that kill</figcaption></figure></div>
          </div>
        </div>

        <div class="bonus-item-with-image">
          <div class="bonus-mockup">
            <img src="./mockups/{SLUG}/bonus-lab.webp" alt="{B2}, illustrated handbook" width="720" height="1000" loading="lazy" decoding="async">
          </div>
          <div class="bonus-text">
            <h3>BONUS 2: &ldquo;{B2}&rdquo;</h3>
            <p class="value">Standalone value: ${VAL_LAB}</p>
            <p>74 pages to read a lab report: <strong>30 test sheets with the reference range, what raises it, what lowers it</strong>, why it was ordered and the draw pitfalls that ruin a sample.</p>
            <p style="margin-top: 12px;">Anatomy tells you where to look at the patient. This tells you what is happening inside them.</p>
            <div class="bonus-sfoglia"><figure><img src="./amostras/anatomy_lab1.webp" alt="A test sheet: range, what raises it, what lowers it" width="1100" height="1556" loading="lazy" decoding="async"><figcaption>One sheet per test</figcaption></figure><figure><img src="./amostras/anatomy_lab2.webp" alt="Reading a full lab report" width="1100" height="1556" loading="lazy" decoding="async"><figcaption>Reading the whole report</figcaption></figure></div>
          </div>
        </div>
      </div>

      <!-- DECISION BOX -->
      <div class="decision-box" id="offer">
        <img src="./mockups/{SLUG}/hero.webp" alt="{TITLE} with the two bonus books" class="db-mockup" width="1400" height="830" loading="lazy" decoding="async">
        <h3 class="db-title">{TITLE} + 2 Bonus Books</h3>
        <ul class="db-checklist">
          <li>{CHECK_SVG}{TITLE}: {PAGES} illustrated pages<span class="db-price-val">${VAL_MAIN}</span></li>
          <li>{CHECK_SVG}Bonus 1: {B1}<span class="db-price-val">${VAL_EM}</span></li>
          <li>{CHECK_SVG}Bonus 2: {B2}<span class="db-price-val">${VAL_LAB}</span></li>
          <li>{CHECK_SVG}High-resolution printable PDFs<span class="db-price-val">Included</span></li>
        </ul>
        <div class="db-anchoring">
          <p class="db-old-price">Total value: ${TOTAL}</p>
          <p class="db-new-price-label">Today only:</p>
          <p class="db-new-price">${PRICE}</p>
          <span class="db-discount-badge">YOU SAVE ${TOTAL - PRICE}</span>
        </div>
        <a href="{CHECKOUT}" data-checkout class="db-cta">YES, I WANT CLINICAL ANATOMY MADE VISUAL FOR ${PRICE}</a>
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
          <img class="paraquem-foto" src="./img/ekg-persona-bedside.webp" alt="A nurse at the bedside" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>You do it right, but nobody showed you why</h3>
            <p>You find the site, you hear the murmur, you pass the catheter. This is the layer underneath: what your hand is on top of, and what happens when it is a centimetre off.</p>
          </div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/ekg-persona-tele.webp" alt="A nurse reading a monitor on the unit" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>New unit, or back after time away</h3>
            <p>Telemetry, drips, central lines and chest tubes are in front of you again. Part III ties the coronary arteries to the walls and to the leads, so a tracing stops being a shape to recognise.</p>
          </div>
        </div>
        <div class="paraquem-card">
          <img class="paraquem-foto" src="./img/persona-professional.webp" alt="An experienced nurse teaching a colleague" loading="lazy" width="900" height="672">
          <div class="paraquem-info">
            <h3>You precept, and you get asked</h3>
            <p>Students ask the questions nobody answered for you. These are pages you can turn round and put in front of someone, and the drawing does the explaining.</p>
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
          <p>Pharmacist and founder of Med Study Lab, the series of illustrated books for healthcare: pharmacology, clinical handbooks, lab tests, EKGs, dosage calculations and now clinical anatomy.</p>
          <p>The method is always the same: <strong>visual clarity and one topic per page</strong>, because what the brain sees organized, it remembers.</p>
          <p>Anatomy is the subject most often taught in the wrong order for the people who use it. This book starts from what happens in a shift and works back to the structure, <strong>not the other way round</strong>.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- RECAP -->
  <section class="section section-alt">
    <div class="container">
      <h2 class="text-center">To Recap: Here's Everything You Get</h2>
      <ul class="recap-list">
        <li>{TITLE}: {PAGES} illustrated pages in 6 parts, from surface landmarks and injection sites to coronary territories, catheter routes and the triangle of safety, with a one-page landmark sheet</li>
        <li>Bonus 1: &ldquo;{B1}&rdquo;, illustrated handbook, 82 pages (value ${VAL_EM})</li>
        <li>Bonus 2: &ldquo;{B2}&rdquo;, 74 pages (value ${VAL_LAB})</li>
        <li>Delivery: all 3 books by email right after purchase</li>
        <li>30-day guarantee: if it doesn't help, I refund you</li>
        <li>High-resolution PDFs: print them, annotate them, take them onto the unit</li>
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
        <p>If the book doesn't help you at work, email me what didn't work and <strong>I'll refund 100% of your purchase</strong>.</p>
        <p>No fine print, no hassle. One email is enough.</p>
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
      <p>You have been doing this for years. Nothing on your unit is going to surprise you.</p>
      <p>But there is a difference between doing something correctly and <strong>being able to see what is under your hand while you do it</strong>.</p>
      <p>That difference is the one nobody had time to teach you, and it is what this book is.</p>
      <p style="font-size: 22px; font-weight: 700; margin-top: 32px;">{PAGES} pages, and every one of them is a shift.</p>
      <p><strong>Now it's your turn.</strong></p>
      <div class="cta-summary">
        <ul>
          <li>One-time payment: ${PRICE}</li>
          <li>Guarantee: 30 days</li>
          <li>Delivery: all 3 books right after purchase</li>
        </ul>
      </div>
      <a href="#offer" class="btn-cta">I WANT CLINICAL ANATOMY MADE VISUAL FOR ${PRICE}</a>
      <p class="cta-small-print" style="margin-top: 24px;">
        <svg aria-hidden="true" focusable="false" class="lc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/></svg> Digital book (PDF) · The books arrive by email within minutes
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
    rep = [('"item_id": "ekg", "item_name": "Reading EKGs Made Visual"',
            f'"item_id": "{SLUG}", "item_name": "{TITLE}"'),
           ('"content_ids": ["ekg"], "content_name": "Reading EKGs Made Visual"',
            f'"content_ids": ["{SLUG}"], "content_name": "{TITLE}"')]
    for a, b in rep:
        assert a in t, a
        t = t.replace(a, b)
    return t


def main():
    src = open(os.path.join(SITO, "ekg.html"), encoding="utf-8").read()
    i = src.index("<body>")
    j = src.index("  <!-- Dynamic Offer Date")
    out = head(src[:i]) + body() + tail(src[j:])
    open(os.path.join(SITO, f"{SLUG}.html"), "w", encoding="utf-8",
         newline="\n").write(out)
    print(f"{SLUG}.html", len(out))


if __name__ == "__main__":
    main()

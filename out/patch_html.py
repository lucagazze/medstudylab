# -*- coding: utf-8 -*-
"""Point index.html at the new English assets, switch the offer to GBP, rebrand the author."""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SB = "https://czocbnyoenjbpxmcqobn.supabase.co/storage/v1/object/public/algoritmia-img/studiofacile"

ASSETS = [
    (SB + "/mockups/57.webp?v=2",                    "./img/kit-hero.webp"),
    (SB + "/amostras/23.webp?v=2",                   "./img/sample-1.webp"),
    (SB + "/amostras/29.webp?v=2",                   "./img/sample-2.webp"),
    (SB + "/amostras/32.webp?v=2",                   "./img/sample-3.webp"),
    (SB + "/amostras/33.webp?v=2",                   "./img/sample-4.webp"),
    (SB + "/amostras/cinetica-x-dinamica.webp?v=2",  "./img/sample-5.webp"),
    ("./esto.jpg?v=2",                               "./img/textbook-dense.webp"),
    (SB + "/mockup-combo-amostras.webp?v=1",         "./img/kit-with-pages.webp"),
    (SB + "/mockup-bonus.webp?v=2",                  "./img/bonus-1.webp"),
    (SB + "/mockup-bonus-2.webp?v=2",                "./img/bonus-2.webp"),
    (SB + "/mockup-combo-entregaveis.webp",          "./img/kit-combo.webp"),
    (SB + "/personagens/estudante.webp",             "./img/persona-student.webp"),
    (SB + "/personagens/recem-formado.webp",         "./img/persona-graduate.webp"),
    (SB + "/personagens/profissional.webp",          "./img/persona-professional.webp"),
    (SB + "/foto-autor.webp?v=3",                    "./img/author.webp"),
    (SB + "/favicon.ico",                            "./brand/favicon.ico"),
    (SB + "/brand/icon-32.png",                      "./brand/icon-32.png"),
    (SB + "/brand/icon-48.png",                      "./brand/icon-48.png"),
    (SB + "/brand/icon-192.png",                     "./brand/icon-192.png"),
    (SB + "/brand/apple-touch-icon.png",             "./brand/apple-touch-icon.png"),
    (SB + "/brand/og-image.jpg",                     "https://www.medstudylab.com/brand/og-image.png"),
]

# Intrinsic sizes changed for a few of the regenerated assets
DIMS = [
    ('alt="A to Z Guide" width="700" height="991"',       'alt="A to Z Guide" width="700" height="889"'),
    ('alt="Rapid Review Sheets" width="700" height="992"', 'alt="Rapid Review Sheets" width="700" height="889"'),
    ('width="768" height="1024"',                          'width="768" height="1029"'),
]

TEXT = [
    # --- currency: the offer now runs in pounds for the UK launch ---
    ('"price":"13","priceCurrency":"USD"', '"price":"13","priceCurrency":"GBP"'),
    ("price: 13, currency: 'USD'", "price: 13, currency: 'GBP'"),
    ("value: 13, currency: 'USD'", "value: 13, currency: 'GBP'"),
    ("currency: 'USD', value: 13", "currency: 'GBP', value: 13"),
    ("$13", "£13"),
    ("$47", "£47"),
    ("$27", "£27"),
    ("$17", "£17"),
    ("$91", "£91"),
    ("The price is in USD and is automatically converted to your local currency at checkout.",
     "The price is in GBP and is automatically converted to your local currency at checkout."),
    ("Yes. The price is in USD ($) and is automatically converted to your local currency at checkout.",
     "Yes. The price is in GBP (£) and is automatically converted to your local currency at checkout."),
    ("Price in USD ($). Automatic conversion for international currencies.",
     "Price in GBP (£). Automatic conversion for international currencies."),

    # --- author identity ---
    ("Leandro Moretti", "Daniel Hartley"),
]


def main():
    p = os.path.join(ROOT, "index.html")
    with io.open(p, encoding="utf-8") as f:
        s = f.read()
    before = s

    for a, b in ASSETS + DIMS + TEXT:
        s = s.replace(a, b)

    left = s.count("supabase.co")
    print("index.html: %d chars changed, %d supabase refs left" % (abs(len(s) - len(before)), left))
    if left:
        for m in re.finditer(r"[^\"']*supabase\.co[^\"']*", s):
            print("   LEFTOVER:", m.group(0)[:120])

    with io.open(p, "w", encoding="utf-8") as f:
        f.write(s)

    # refund-policy.html carries the same currency wording
    rp = os.path.join(ROOT, "refund-policy.html")
    if os.path.exists(rp):
        with io.open(rp, encoding="utf-8") as f:
            r = f.read()
        for a, b in TEXT + [(SB + "/favicon.ico", "./brand/favicon.ico")]:
            r = r.replace(a, b)
        with io.open(rp, "w", encoding="utf-8") as f:
            f.write(r)
        print("refund-policy.html patched")


if __name__ == "__main__":
    main()

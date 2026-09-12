"""Genera aus.html (landing de Australia, en dólares australianos) a partir de usd.html.
Precio A$27, valor total A$91 (A$41 + A$25 + A$25), 70% OFF, píxel y datos estructurados en AUD.
El checkout tiene que cobrar lo mismo: mercado Australia de Impultienda en AUD, kit a A$27.
Uso: python3 tools/build_aus.py  (desde la raíz del repo; falla si usd.html cambió y algún reemplazo no encaja)."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRICE, VALUE, CUR = "27", "27", "AUD"  # PRICE es el que se ve; VALUE el número para el píxel

# (buscar, reemplazar, cuántas veces tiene que aparecer)
SUBS = [
    ('<html lang="en">', '<html lang="en-AU">', 1),
    ('https://www.medicalstudylab.com/usd"', 'https://www.medicalstudylab.com/aus"', 2),
    ('"price":"19","priceCurrency":"USD"', f'"price":"{PRICE}","priceCurrency":"{CUR}"', 1),
    ("The price is in USD and is automatically converted to your local currency at checkout.",
     "The price is in Australian dollars (AUD), so what you see is what you pay.", 1),
    ("The price is in USD ($) and is automatically converted to your local currency at checkout.",
     "The price is in Australian dollars (A$), so what you see is what you pay.", 1),
    ("Automatic currency conversion for international orders.", "Prices in Australian dollars.", 1),
    ("Price in USD ($). Automatic conversion for international currencies.", "Price in Australian dollars (A$).", 1),
    ("Secure checkout with automatic currency conversion", "Secure checkout in Australian dollars", 1),
    ("price: 19, currency: 'USD'", f"price: {VALUE}, currency: '{CUR}'", 1),
    ("value: 19, currency: 'USD'", f"value: {VALUE}, currency: '{CUR}'", 1),
    ("currency: 'USD', value: 19", f"currency: '{CUR}', value: {VALUE}", 2),
    (">79% OFF<", ">70% OFF<", 1),
]
# importes visibles: el kit pasa a A$27; los valores de referencia quedan igual pero en A$
AMOUNTS = [(r"(?<!\w)\$19(?!\d)", f"A${PRICE}", 9), (r"(?<!\w)\$41(?!\d)", "A$41", 1),
           (r"(?<!\w)\$25(?!\d)", "A$25", 6), (r"(?<!\w)\$91(?!\d)", "A$91", 2)]

t = open(os.path.join(ROOT, "usd.html"), encoding="utf-8").read()
for old, new, n in SUBS:
    assert t.count(old) == n, f"'{old[:50]}' aparece {t.count(old)} veces, se esperaban {n}"
    t = t.replace(old, new)
for pat, rep, n in AMOUNTS:
    t, k = re.subn(pat, rep, t)
    assert k == n, f"{pat} aparece {k} veces, se esperaban {n}"
left = re.findall(r"USD|(?<![A\w])\$\d", t)
assert not left, f"quedan importes o menciones en dólares estadounidenses: {left[:5]}"
open(os.path.join(ROOT, "aus.html"), "w", encoding="utf-8").write(t)
print("aus.html generado: A$" + PRICE)

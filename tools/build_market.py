"""Genera las landings de cada mercado en su moneda a partir de usd.html (la de dólares):
  aus → aus.html (Australia, A$)   ·   ca → ca.html (Canadá, CA$)
Cambia precio, moneda del píxel y de los datos estructurados, textos de moneda, canonical y badge de descuento.
El valor de referencia (41 + 25 + 25 = 91) queda igual, con el símbolo de la moneda local.
El checkout tiene que cobrar lo mismo: mercado del país en Impultienda, en su moneda.
Uso: python3 tools/build_market.py aus ca   (falla si usd.html cambió y algún reemplazo no encaja)."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PRICE = "27"   # precio del kit en usd.html

MARKETS = {
    "aus": dict(price="27", cur="AUD", sym="A$", lang="en-AU", off="70% OFF", name="Australian dollars",
                small="Price in Australian dollars (A$).<br>"),
    "ca":  dict(price="35", cur="CAD", sym="CA$", lang="en-CA", off="62% OFF", name="Canadian dollars",
                small=""),   # sin la nota de moneda (Luca la sacó en UK)
}

def build(slug, m):
    t = open(os.path.join(ROOT, "usd.html"), encoding="utf-8").read()
    subs = [
        ('<html lang="en">', f'<html lang="{m["lang"]}">', 1),
        ('https://www.medicalstudylab.com/usd"', f'https://www.medicalstudylab.com/{slug}"', 2),
        (f'"price":"{SRC_PRICE}","priceCurrency":"USD"', f'"price":"{m["price"]}","priceCurrency":"{m["cur"]}"', 1),
        ("The price is in USD and is automatically converted to your local currency at checkout.",
         f"The price is in {m['name']} ({m['cur']}), so what you see is what you pay.", 1),
        ("The price is in USD ($) and is automatically converted to your local currency at checkout.",
         f"The price is in {m['name']} ({m['sym']}), so what you see is what you pay.", 1),
        ("Automatic currency conversion for international orders.", f"Prices in {m['name']}.", 1),
        ("Price in USD ($). Automatic conversion for international currencies.<br>", m["small"], 1),
        ("Secure checkout with automatic currency conversion", f"Secure checkout in {m['name']}", 1),
        (f"price: {SRC_PRICE}, currency: 'USD'", f"price: {m['price']}, currency: '{m['cur']}'", 1),
        (f"value: {SRC_PRICE}, currency: 'USD'", f"value: {m['price']}, currency: '{m['cur']}'", 1),
        (f"currency: 'USD', value: {SRC_PRICE}", f"currency: '{m['cur']}', value: {m['price']}", 2),
        (">70% OFF<", f">{m['off']}<", 1),
    ]
    for old, new, n in subs:
        assert t.count(old) == n, f"{slug}: '{old[:50]}' aparece {t.count(old)} veces, se esperaban {n}"
        t = t.replace(old, new)
    # importes visibles: el kit pasa al precio local; los valores de referencia quedan igual, con el símbolo local
    for amount, rep, n in [(SRC_PRICE, m["price"], 9), ("41", "41", 1), ("25", "25", 6), ("91", "91", 2)]:
        t, k = re.subn(rf"(?<![\w$])\${amount}(?!\d)", f"{m['sym']}{rep}", t)
        assert k == n, f"{slug}: ${amount} aparece {k} veces, se esperaban {n}"
    left = re.findall(r"USD|(?<![A-Z\w])\$\d", t)
    assert not left, f"{slug}: quedan importes o menciones en dólares estadounidenses: {left[:5]}"
    open(os.path.join(ROOT, f"{slug}.html"), "w", encoding="utf-8").write(t)
    print(f"{slug}.html generado: {m['sym']}{m['price']}")

for slug in (sys.argv[1:] or MARKETS):
    build(slug, MARKETS[slug])

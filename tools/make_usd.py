# -*- coding: utf-8 -*-
"""
Genera usd.html a partir de index.html: la MISMA pagina, cobrada en dolares.

Con `cleanUrls: true` en vercel.json, usd.html se sirve en /usd. index.html no
se toca nunca: esta es una copia derivada, y se regenera corriendo el script
cada vez que se edite el index.

Los precios no son la conversion literal (13 x 1,3518 = 17,57): son los puntos
de precio redondeados equivalentes, que mantienen el mismo descuento (80%) sin
quedar con centavos raros en el boton de compra.

    python tools/make_usd.py
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "index.html")
DST = os.path.join(ROOT, "usd.html")

# £ -> $ . El orden importa: primero los de mas digitos, o "£13" pisaria "£130".
PRICES = [
    ("£65", "$87"),   # valor total anclado
    ("£27", "$37"),   # valor de los modulos
    ("£19", "$25"),   # valor de cada bonus
    ("£13", "$17"),   # precio real del kit
]

# Textos donde la moneda se nombra en prosa o en marcado.
TEXT = [
    ("Price in GBP (£). Automatic conversion for international currencies.",
     "Price in USD ($). Automatic conversion for international currencies."),
    ("The price is in GBP (£) and is automatically converted to your local currency at checkout.",
     "The price is in USD ($) and is automatically converted to your local currency at checkout."),
    ("The price is in GBP and is automatically converted to your local currency at checkout.",
     "The price is in USD and is automatically converted to your local currency at checkout."),
    ('"priceCurrency":"GBP"', '"priceCurrency":"USD"'),
    ("currency: 'GBP'", "currency: 'USD'"),
    ('"price":"13"', '"price":"17"'),
    ("price: 13,", "price: 17,"),
    ("value: 13,", "value: 17,"),
    # La pagina en dolares vive para trafico pago: que no compita en Google con
    # el index britanico, que es la version canonica del sitio. Se PISA la
    # etiqueta robots original, no se agrega otra: dos robots en la misma pagina
    # es ambiguo y Google aplica la mas restrictiva sin avisar.
    ('<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">',
     '<meta name="robots" content="noindex, follow">'),
    ('<link rel="canonical" href="https://www.medstudylab.com/">',
     '<link rel="canonical" href="https://www.medstudylab.com/usd">'),
    ('<meta property="og:url" content="https://www.medstudylab.com/">',
     '<meta property="og:url" content="https://www.medstudylab.com/usd">'),
]


def main():
    s = io.open(SRC, encoding="utf-8").read()
    original = s

    for old, new in TEXT:
        if old not in s:
            print("   ! no encontrado (revisar):", old[:70])
        s = s.replace(old, new)

    for old, new in PRICES:
        n = s.count(old)
        s = s.replace(old, new)
        print(f"   {old} -> {new}  ({n})")

    left = re.findall(r"£[0-9.,]*", s)
    if left:
        print("   ! quedaron simbolos £:", left)
    if "GBP" in s:
        print("   ! quedo 'GBP' en el archivo:", s.count("GBP"))

    io.open(DST, "w", encoding="utf-8").write(s)
    print(f"\nusd.html escrito ({len(s)} chars, index sin tocar: {len(original)})")


if __name__ == "__main__":
    sys.exit(main())

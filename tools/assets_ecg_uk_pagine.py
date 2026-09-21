# -*- coding: utf-8 -*-
"""
Sample pages and page collage for /ecg-uk: the SAME pages shown on /ekg (US),
taken from the UK PDF (Reading the ECG: ECG spelling, British English).

  python tools/assets_ecg_uk_pagine.py
"""
import asyncio
import os
import sys

import fitz
from PIL import Image

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UK = r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Med Study Lab\Ebooks\UK"
sys.path.insert(0, r"C:\Users\lucag\Desktop\studiofacile\scripts")
import asset_ecg as A  # noqa: E402

PAG = os.path.join(SITO, "amostras")
A.OUT = os.path.join(SITO, "mockups", "ecg-uk")
ECG = os.path.join(UK, "Reading the ECG.pdf")
COVER = r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Portadas\English-UK\Reading the ECG.webp"
# stesse pagine di tools/assets_ekg.py (ekg_01..09), stesso ordine
PAGINE = [(7, "ecguk_p1"), (9, "ecguk_p2"), (11, "ecguk_p3"), (22, "ecguk_p4"), (33, "ecguk_p5"),
          (46, "ecguk_p6"), (53, "ecguk_p7"), (63, "ecguk_p8"), (10, "ecguk_p9")]


def main():
    doc = fitz.open(ECG)
    for n, nome in PAGINE:
        pix = doc[n - 1].get_pixmap(dpi=150)
        im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        im = im.resize((1100, round(1100 * im.height / im.width)), Image.LANCZOS)
        im.save(os.path.join(PAG, nome + ".webp"), "WEBP", quality=86, method=6)
    fogli = [(-60, -30, -7, "ecguk_p1"), (330, -70, 5, "ecguk_p2"), (660, -20, 9, "ecguk_p4"),
             (-90, 480, 4, "ecguk_p5"), (620, 500, -6, "ecguk_p6"), (-40, 990, -9, "ecguk_p7"),
             (350, 1030, 3, "ecguk_p8"), (660, 980, 7, "ecguk_p3")]
    parti = [f'<div class="sheet" style="left:{x}px;top:{y}px;width:470px;height:665px;'
             f'transform:rotate({r}deg)"><img src="{A._uri(os.path.join(PAG, k + ".webp"))}" alt=""></div>'
             for x, y, r, k in fogli]
    parti.append(A.tab(COVER, 270, 400, 560, 786, 6))
    asyncio.run(A.rendi([("combo", A.page(1100, 1620, "".join(parti)), 1100, 1620, True)]))


if __name__ == "__main__":
    main()

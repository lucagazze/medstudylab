# -*- coding: utf-8 -*-
"""
Images for /dosage — Dosage Calculations Made Visual kit (US).

Every page shown is a real page of the delivered US PDFs (Med Study Lab\\Ebooks\\USA).
Tablet mockups reuse the renderer of studiofacile/scripts/asset_ecg.py (same as assets_ekg.py).

  python tools/assets_dosage.py
"""
import asyncio
import io
import os
import sys

import fitz
from PIL import Image

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USA = r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Med Study Lab\Ebooks\USA"
sys.path.insert(0, r"C:\Users\lucag\Desktop\studiofacile\scripts")
import asset_ecg as A  # noqa: E402

OUT = os.path.join(SITO, "mockups", "dosage")
PAG = os.path.join(SITO, "amostras")
A.OUT = OUT

DOS = os.path.join(USA, "Dosage Calculations Made Visual.pdf")
EM = os.path.join(USA, "Emergency Drugs Illustrated Handbook.pdf")
GL = os.path.join(USA, "Clinical Pharmacy Glossary.pdf")

# (pdf, page number, output name)
PAGINE = [(DOS, 7, "dosage_01"), (DOS, 9, "dosage_02"), (DOS, 19, "dosage_03"),
          (DOS, 21, "dosage_04"), (DOS, 25, "dosage_05"), (DOS, 28, "dosage_06"),
          (DOS, 6, "dosage_07"), (DOS, 15, "dosage_08"),
          (EM, 8, "dosage_em1"), (EM, 10, "dosage_em2"),
          (GL, 35, "dosage_gl1"), (GL, 9, "dosage_gl2")]


def pagina(pdf, n, larghezza=1100):
    d = fitz.open(pdf)
    im = Image.open(io.BytesIO(d[n - 1].get_pixmap(dpi=200).tobytes("png"))).convert("RGB")
    d.close()
    return im.resize((larghezza, round(larghezza * im.height / im.width)), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    cov = {}
    for k, pdf in (("dosage", DOS), ("em", EM), ("gl", GL)):
        p = os.path.join(OUT, f"cover-{k}.jpg")
        pagina(pdf, 1, 1300).save(p, quality=92)
        cov[k] = p
    for pdf, n, nome in PAGINE:
        pagina(pdf, n).save(os.path.join(PAG, nome + ".webp"), "WEBP", quality=86, method=6)

    # the worked-example box of p. 9, for the "every step shown" section
    im = pagina(DOS, 9, 2080)
    w, h = im.size
    c = im.crop((int(w * .115), int(h * .228), int(w * .885), int(h * .449)))
    c.resize((1600, round(1600 * c.height / c.width)), Image.LANCZOS).save(
        os.path.join(OUT, "example.webp"), "WEBP", quality=88, method=6)

    trio = (A.tab(cov["em"], 40, 40, 440, 616, 1) + A.tab(cov["gl"], 920, 40, 440, 616, 1)
            + A.tab(cov["dosage"], 410, 10, 580, 812, 3))
    lavori = [("hero", A.page(1400, 830, trio), 1400, 830, True)]
    og = ('<div style="position:absolute;inset:0;background:linear-gradient(135deg,#1c2b53,#0f1a3a)"></div>'
          f'<div style="position:absolute;left:180px;top:28px;transform:scale(.6);transform-origin:top left">{trio}</div>')
    lavori.append(("og", A.page(1200, 630, og), 1200, 630, False))
    for k, nome in (("dosage", "book-dosage"), ("em", "bonus-em"), ("gl", "bonus-gl")):
        lavori.append((nome, A.page(720, 1000, A.tab(cov[k], 40, 40, 640, 920)), 720, 1000, True))
    fogli = [(-60, -30, -7, "dosage_01"), (330, -70, 5, "dosage_02"), (660, -20, 9, "dosage_03"),
             (-90, 480, 4, "dosage_04"), (620, 500, -6, "dosage_05"), (-40, 990, -9, "dosage_06"),
             (350, 1030, 3, "dosage_08"), (660, 980, 7, "dosage_07")]
    parti = [f'<div class="sheet" style="left:{x}px;top:{y}px;width:470px;height:665px;'
             f'transform:rotate({r}deg)"><img src="{A._uri(os.path.join(PAG, k + ".webp"))}" alt=""></div>'
             for x, y, r, k in fogli]
    parti.append(A.tab(cov["dosage"], 270, 400, 560, 786, 6))
    lavori.append(("combo", A.page(1100, 1620, "".join(parti)), 1100, 1620, True))
    print("mockups:")
    asyncio.run(A.rendi(lavori))


if __name__ == "__main__":
    main()

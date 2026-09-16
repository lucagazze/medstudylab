# -*- coding: utf-8 -*-
"""
Images for /pharm — the Pharm Made Visual Kit (US).

Every page shown is a real page of the US editions (rendered straight from
the PDFs in Med Study Lab\\Ebooks\\USA); the dosage cards are the real
worked examples of Dosage Calculations Made Visual (schede.py, every result
asserted in code). The tablet mockups reuse the Studio Facile renderer.

  python tools/assets_pharm.py
"""
import asyncio
import io
import os
import sys

import fitz
from PIL import Image

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USA = r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Med Study Lab\Ebooks\USA"
DOSE = (r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Proyectos (código de los libros)"
        r"\Farmacologia\English\DosageCalc-US")
sys.path.insert(0, r"C:\Users\lucag\Desktop\studiofacile\scripts")
import asset_ecg as A  # noqa: E402

OUT = os.path.join(SITO, "mockups", "pmv")
PAG = os.path.join(SITO, "amostras")
A.OUT = OUT

PH = os.path.join(USA, "Pharmacology Illustrated.pdf")
RR = os.path.join(USA, "Rapid Review in Pharmacology.pdf")
GL = os.path.join(USA, "Clinical Pharmacy Glossary.pdf")

# (pdf, page number, output name) — must match the carousel in make_pharm.py
PAGINE = [(RR, 6, "pmv_01"), (PH, 59, "pmv_02"), (PH, 17, "pmv_03"),
          (PH, 23, "pmv_04"), (RR, 7, "pmv_05"), (PH, 44, "pmv_06"),
          (PH, 53, "pmv_07"), (RR, 36, "pmv_08"), (RR, 39, "pmv_09"),
          (GL, 5, "pmv_gl1"), (GL, 12, "pmv_gl2")]
CARDS = ["dimensional", "weight_based", "drops", "dopamine"]


def pagina(pdf, n, larghezza=1100):
    d = fitz.open(pdf)
    im = Image.open(io.BytesIO(d[n - 1].get_pixmap(dpi=150).tobytes("png"))).convert("RGB")
    d.close()
    return im.resize((larghezza, round(larghezza * im.height / im.width)), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    cov = {}
    for k, pdf in (("ph", PH), ("rr", RR), ("gl", GL)):
        p = os.path.join(OUT, f"cover-{k}.jpg")
        pagina(pdf, 1, 1300).save(p, quality=92)
        cov[k] = p
    dc = os.path.join(OUT, "cover-dc.jpg")
    im = Image.open(os.path.join(DOSE, "pagine", "copertina.jpeg")).convert("RGB")
    im.resize((1300, round(1300 * im.height / im.width)), Image.LANCZOS).save(dc, quality=92)
    cov["dc"] = dc

    for pdf, n, nome in PAGINE:
        pagina(pdf, n).save(os.path.join(PAG, nome + ".webp"), "WEBP", quality=86, method=6)
    for c in CARDS:
        A._webp(os.path.join(DOSE, "figure", c + ".png"), os.path.join(OUT, f"card-{c}.webp"), 1600)

    quattro = (A.tab(cov["gl"], 40, 30, 400, 560, 1) + A.tab(cov["rr"], 960, 30, 400, 560, 1)
               + A.tab(cov["dc"], 230, 150, 460, 644, 2) + A.tab(cov["ph"], 710, 150, 460, 644, 3))
    lavori = [("hero", A.page(1400, 830, quattro), 1400, 830, True)]
    og = ('<div style="position:absolute;inset:0;background:'
          'linear-gradient(135deg,#2645a0,#1b3277)"></div>'
          f'<div style="position:absolute;left:180px;top:28px;transform:'
          f'scale(.6);transform-origin:top left">{quattro}</div>')
    lavori.append(("og", A.page(1200, 630, og), 1200, 630, False))
    for k, nome in (("dc", "bonus-dc"), ("gl", "bonus-gl"), ("ph", "book-ph"), ("rr", "book-rr")):
        lavori.append((nome, A.page(720, 1000, A.tab(cov[k], 40, 40, 640, 920)), 720, 1000, True))
    fogli = [(-60, -30, -7, "pmv_03"), (330, -70, 5, "pmv_01"), (660, -20, 9, "pmv_04"),
             (-90, 480, 4, "pmv_02"), (620, 500, -6, "pmv_05"), (-40, 990, -9, "pmv_06"),
             (660, 980, 7, "pmv_09")]
    parti = [f'<div class="sheet" style="left:{x}px;top:{y}px;width:470px;height:665px;'
             f'transform:rotate({r}deg)"><img src="{A._uri(os.path.join(PAG, k + ".webp"))}" alt=""></div>'
             for x, y, r, k in fogli]
    parti.append(A.tab(cov["ph"], 270, 400, 560, 786, 6))
    lavori.append(("combo", A.page(1100, 1620, "".join(parti)), 1100, 1620, True))
    print("mockups:")
    asyncio.run(A.rendi(lavori))


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Images for /abg — ABGs & Electrolytes Made Visual kit (US).

The main book is still being written: the only real asset it has is the cover
(Med Study Lab\\Portadas\\09_ABGs-and-Electrolytes-Made-Visual.jpg).
Every page shown on the landing is therefore a REAL page of one of the two
bonus PDFs, and each caption says which book it comes from.

  python tools/assets_abg.py
"""
import asyncio
import io
import os
import sys

import fitz
from PIL import Image

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USA = r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Med Study Lab\Ebooks\USA"
PORTADAS = r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Med Study Lab\Portadas"
sys.path.insert(0, r"C:\Users\lucag\Desktop\studiofacile\scripts")
import asset_ecg as A  # noqa: E402

OUT = os.path.join(SITO, "mockups", "abg")
PAG = os.path.join(SITO, "amostras")
A.OUT = OUT

LAB = os.path.join(USA, "Reading Laboratory Tests.pdf")
EM = os.path.join(USA, "Emergency Drugs Illustrated Handbook.pdf")
COVER_ABG = os.path.join(PORTADAS, "09_ABGs-and-Electrolytes-Made-Visual.jpg")

# (pdf, page number, output name) — all real pages of the two bonus books
PAGINE = [(LAB, 40, "abg_01"),   # acid-base balance on one page
          (EM, 57, "abg_02"),    # scenario: diabetic ketoacidosis
          (EM, 56, "abg_03"),    # hyperkalemia: the emergency treatment
          (EM, 51, "abg_04"),    # balanced crystalloid and sodium chloride 0.9%
          (LAB, 64, "abg_05"),   # in the critically ill
          (EM, 10, "abg_06"),    # the dilutions that kill
          (LAB, 12, "abg_lab1"),  # critical results
          (LAB, 49, "abg_lab2"),  # review of metabolism and balance
          (EM, 50, "abg_em1"),   # fluid and electrolyte replacement
          (EM, 53, "abg_em2")]   # potassium chloride


def pagina(pdf, n, larghezza=1100):
    d = fitz.open(pdf)
    im = Image.open(io.BytesIO(d[n - 1].get_pixmap(dpi=200).tobytes("png"))).convert("RGB")
    d.close()
    return im.resize((larghezza, round(larghezza * im.height / im.width)), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    cov = {}
    for k, pdf in (("lab", LAB), ("em", EM)):
        p = os.path.join(OUT, f"cover-{k}.jpg")
        pagina(pdf, 1, 1300).save(p, quality=92)
        cov[k] = p
    # the ABG cover is a flat JPEG, not a PDF
    p = os.path.join(OUT, "cover-abg.jpg")
    im = Image.open(COVER_ABG).convert("RGB")
    im.resize((1300, round(1300 * im.height / im.width)), Image.LANCZOS).save(p, quality=92)
    cov["abg"] = p

    for pdf, n, nome in PAGINE:
        pagina(pdf, n).save(os.path.join(PAG, nome + ".webp"), "WEBP", quality=86, method=6)

    trio = (A.tab(cov["em"], 40, 40, 440, 616, 1) + A.tab(cov["lab"], 920, 40, 440, 616, 1)
            + A.tab(cov["abg"], 410, 10, 580, 812, 3))
    lavori = [("hero", A.page(1400, 830, trio), 1400, 830, True)]
    og = ('<div style="position:absolute;inset:0;background:linear-gradient(135deg,#1c2b53,#0f1a3a)"></div>'
          f'<div style="position:absolute;left:180px;top:28px;transform:scale(.6);transform-origin:top left">{trio}</div>')
    lavori.append(("og", A.page(1200, 630, og), 1200, 630, False))
    for k, nome in (("abg", "book-abg"), ("lab", "bonus-lab"), ("em", "bonus-em")):
        lavori.append((nome, A.page(720, 1000, A.tab(cov[k], 40, 40, 640, 920)), 720, 1000, True))
    print("mockups:")
    asyncio.run(A.rendi(lavori))


if __name__ == "__main__":
    main()

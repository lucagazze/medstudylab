# -*- coding: utf-8 -*-
"""
Images for /ekg — the EKG Made Visual Kit (US).

Every page shown is a real page of the delivered US PDFs (Med Study Lab\\Ebooks\\USA).
The tablet mockups reuse the renderer of studiofacile/scripts/asset_ecg.py.

  python tools/assets_ekg.py
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

OUT = os.path.join(SITO, "mockups", "ekg")
PAG = os.path.join(SITO, "amostras")
ART = os.path.join(SITO, "tools", "art", "pmv")
A.OUT = OUT

EKG = os.path.join(USA, "Reading EKGs Made Visual.pdf")
EM = os.path.join(USA, "Emergency Drugs Illustrated Handbook.pdf")
LAB = os.path.join(USA, "Reading Laboratory Tests.pdf")

# (pdf, page number, output name) — must match make_ekg.py
PAGINE = [(EKG, 7, "ekg_01"), (EKG, 9, "ekg_02"), (EKG, 11, "ekg_03"), (EKG, 22, "ekg_04"),
          (EKG, 33, "ekg_05"), (EKG, 46, "ekg_06"), (EKG, 53, "ekg_07"), (EKG, 63, "ekg_08"),
          (EKG, 10, "ekg_09"),
          (EM, 12, "ekg_em1"), (EM, 19, "ekg_em2"), (LAB, 12, "ekg_lab1"), (LAB, 44, "ekg_lab2")]


def pagina(pdf, n, larghezza=1100):
    d = fitz.open(pdf)
    im = Image.open(io.BytesIO(d[n - 1].get_pixmap(dpi=150).tobytes("png"))).convert("RGB")
    d.close()
    return im.resize((larghezza, round(larghezza * im.height / im.width)), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    cov = {}
    for k, pdf in (("ekg", EKG), ("em", EM), ("lab", LAB)):
        p = os.path.join(OUT, f"cover-{k}.jpg")
        pagina(pdf, 1, 1300).save(p, quality=92)
        cov[k] = p
    for pdf, n, nome in PAGINE:
        pagina(pdf, n).save(os.path.join(PAG, nome + ".webp"), "WEBP", quality=86, method=6)

    # a real strip for the "real tracings" section, cut from the AFib page
    im = pagina(EKG, 23, 1600)
    w, h = im.size
    im.crop((int(w * 0.08), int(h * 0.195), int(w * 0.92), int(h * 0.375))).save(
        os.path.join(OUT, "strip.webp"), "WEBP", quality=88, method=6)

    for k in ("student", "tele", "bedside"):
        src = os.path.join(ART, f"ekg-persona-{k}.jpeg")
        im = Image.open(src).convert("RGB")
        w, h = im.size
        th = int(w * 672 / 900)
        im.crop((0, (h - th) // 2, w, (h - th) // 2 + th)).resize((900, 672), Image.LANCZOS).save(
            os.path.join(SITO, "img", f"ekg-persona-{k}.webp"), "WEBP", quality=85, method=6)

    trio = (A.tab(cov["em"], 40, 40, 440, 616, 1) + A.tab(cov["lab"], 920, 40, 440, 616, 1)
            + A.tab(cov["ekg"], 410, 10, 580, 812, 3))
    lavori = [("hero", A.page(1400, 830, trio), 1400, 830, True)]
    og = ('<div style="position:absolute;inset:0;background:linear-gradient(135deg,#1c2b53,#0f1a3a)"></div>'
          f'<div style="position:absolute;left:180px;top:28px;transform:scale(.6);transform-origin:top left">{trio}</div>')
    lavori.append(("og", A.page(1200, 630, og), 1200, 630, False))
    for k, nome in (("ekg", "book-ekg"), ("em", "bonus-em"), ("lab", "bonus-lab")):
        lavori.append((nome, A.page(720, 1000, A.tab(cov[k], 40, 40, 640, 920)), 720, 1000, True))
    fogli = [(-60, -30, -7, "ekg_01"), (330, -70, 5, "ekg_02"), (660, -20, 9, "ekg_04"),
             (-90, 480, 4, "ekg_05"), (620, 500, -6, "ekg_06"), (-40, 990, -9, "ekg_07"),
             (350, 1030, 3, "ekg_08"), (660, 980, 7, "ekg_03")]
    parti = [f'<div class="sheet" style="left:{x}px;top:{y}px;width:470px;height:665px;'
             f'transform:rotate({r}deg)"><img src="{A._uri(os.path.join(PAG, k + ".webp"))}" alt=""></div>'
             for x, y, r, k in fogli]
    parti.append(A.tab(cov["ekg"], 270, 400, 560, 786, 6))
    lavori.append(("combo", A.page(1100, 1620, "".join(parti)), 1100, 1620, True))
    print("mockups:")
    asyncio.run(A.rendi(lavori))


if __name__ == "__main__":
    main()

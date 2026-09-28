# -*- coding: utf-8 -*-
"""
Images for /anatomy — Clinical Anatomy Made Visual kit (US).

The main book is being written: what exists of it is the cover and the six
pages already generated, which live as JPEGs in the book project and not
in a PDF. They are real pages of the book, so the carousel shows them.

The two bonus books ARE delivered, so their pages come out of their PDFs
the usual way.

Tablet mockups reuse the renderer of studiofacile/scripts/asset_ecg.py,
same as assets_dosage.py and assets_ekg.py.

  python tools/assets_anatomy.py
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
LIBRO = (r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos"
         r"\Proyectos (código de los libros)\Farmacologia\English"
         r"\Anatomia-US\pagine")
sys.path.insert(0, r"C:\Users\lucag\Desktop\studiofacile\scripts")
import asset_ecg as A  # noqa: E402

OUT = os.path.join(SITO, "mockups", "anatomy")
PAG = os.path.join(SITO, "amostras")
A.OUT = OUT

EM = os.path.join(USA, "Emergency Drugs Illustrated Handbook.pdf")
LAB = os.path.join(USA, "Reading Laboratory Tests.pdf")
COVER = os.path.join(PORTADAS, "10_Clinical-Anatomy-Made-Visual.jpg")

# Le sei del carosello, nell'ordine in cui si scorrono. L'ordine è scelto
# per ALTERNARE LA FORMA: un torace, un fianco a due riquadri, tre pannelli
# in fila, una figura intera, una sezione, tre posizioni a confronto. Sei
# pagine buone ma tutte uguali si scorrono senza fermarsi.
PAGINE_LIBRO = [("l5", "anatomy_01"), ("n1", "anatomy_02"),
                ("c4", "anatomy_03"), ("s3", "anatomy_04"),
                ("t7", "anatomy_05"), ("s6", "anatomy_06")]

# (pdf, pagina, nome) dei due bonus
PAGINE_BONUS = [(EM, 8, "anatomy_em1"), (EM, 10, "anatomy_em2"),
                (LAB, 12, "anatomy_lab1"), (LAB, 30, "anatomy_lab2")]


def pagina(pdf, n, larghezza=1100):
    d = fitz.open(pdf)
    im = Image.open(io.BytesIO(
        d[n - 1].get_pixmap(dpi=200).tobytes("png"))).convert("RGB")
    d.close()
    return im.resize((larghezza, round(larghezza * im.height / im.width)),
                     Image.LANCZOS)


def jpeg(nome, larghezza=1100):
    im = Image.open(os.path.join(LIBRO, nome + ".jpeg")).convert("RGB")
    return im.resize((larghezza, round(larghezza * im.height / im.width)),
                     Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    cov = {}
    # la copertina del libro principale è il mockup di marketing, non la
    # prima pagina di un PDF che ancora non esiste
    p = os.path.join(OUT, "cover-anatomy.jpg")
    im = Image.open(COVER).convert("RGB")
    im.resize((1300, round(1300 * im.height / im.width)),
              Image.LANCZOS).save(p, quality=92)
    cov["anatomy"] = p
    for k, pdf in (("em", EM), ("lab", LAB)):
        p = os.path.join(OUT, f"cover-{k}.jpg")
        pagina(pdf, 1, 1300).save(p, quality=92)
        cov[k] = p

    for chiave, nome in PAGINE_LIBRO:
        jpeg(chiave).save(os.path.join(PAG, nome + ".webp"), "WEBP",
                          quality=86, method=6)
    for pdf, n, nome in PAGINE_BONUS:
        pagina(pdf, n).save(os.path.join(PAG, nome + ".webp"), "WEBP",
                            quality=86, method=6)

    # il riquadro delle arterie e delle derivazioni, per la sezione
    # «perché il disegno spiega meglio di un elenco»
    im = jpeg("c4", 2080)
    w, h = im.size
    c = im.crop((int(w * .06), int(h * .19), int(w * .96), int(h * .47)))
    c.resize((1600, round(1600 * c.height / c.width)), Image.LANCZOS).save(
        os.path.join(OUT, "example.webp"), "WEBP", quality=88, method=6)

    trio = (A.tab(cov["em"], 40, 40, 440, 616, 1)
            + A.tab(cov["lab"], 920, 40, 440, 616, 1)
            + A.tab(cov["anatomy"], 410, 10, 580, 812, 3))
    lavori = [("hero", A.page(1400, 830, trio), 1400, 830, True)]
    og = ('<div style="position:absolute;inset:0;background:'
          'linear-gradient(135deg,#1c2b53,#0f1a3a)"></div>'
          '<div style="position:absolute;left:180px;top:28px;transform:'
          f'scale(.6);transform-origin:top left">{trio}</div>')
    lavori.append(("og", A.page(1200, 630, og), 1200, 630, False))
    for k, nome in (("anatomy", "book-anatomy"), ("em", "bonus-em"),
                    ("lab", "bonus-lab")):
        lavori.append((nome, A.page(720, 1000, A.tab(cov[k], 40, 40, 640, 920)),
                       720, 1000, True))
    fogli = [(-60, -30, -7, "anatomy_01"), (330, -70, 5, "anatomy_02"),
             (660, -20, 9, "anatomy_03"), (-90, 480, 4, "anatomy_04"),
             (620, 500, -6, "anatomy_05"), (-40, 990, -9, "anatomy_06"),
             (350, 1030, 3, "anatomy_01"), (660, 980, 7, "anatomy_04")]
    parti = [f'<div class="sheet" style="left:{x}px;top:{y}px;width:470px;'
             f'height:665px;transform:rotate({r}deg)">'
             f'<img src="{A._uri(os.path.join(PAG, k + ".webp"))}" alt=""></div>'
             for x, y, r, k in fogli]
    parti.append(A.tab(cov["anatomy"], 270, 400, 560, 786, 6))
    lavori.append(("combo", A.page(1100, 1620, "".join(parti)), 1100, 1620,
                   True))
    print("mockups:")
    asyncio.run(A.rendi(lavori))


if __name__ == "__main__":
    main()

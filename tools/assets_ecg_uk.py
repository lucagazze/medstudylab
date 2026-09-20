# -*- coding: utf-8 -*-
"""
Images for /ecg-uk — the ECG offer, UK edition.

The main book (Reading EKGs Made Visual) shares its cover and its interior with
the edition already on /ekg, so /ecg-uk reuses mockups/ekg/* and the main-book
sample pages in amostras/ekg_*.webp. Only the two bonus books have finished UK
PDFs, so their sample pages are re-exported here from the UK files: the adult
ALS algorithm and the adrenaline card, critical results and potassium in mmol/L.

  python tools/assets_ecg_uk.py
"""
import io
import os

import fitz
from PIL import Image

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UK = r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Med Study Lab\Ebooks\UK"
PAG = os.path.join(SITO, "amostras")

EM = os.path.join(UK, "Emergency Drugs Illustrated Handbook.pdf")
LAB = os.path.join(UK, "Reading Laboratory Tests.pdf")

# (pdf, page number, output name) — must match make_ecg_uk.py
PAGINE = [(EM, 12, "ecguk_em1"), (EM, 19, "ecguk_em2"),
          (LAB, 12, "ecguk_lab1"), (LAB, 44, "ecguk_lab2")]


def pagina(pdf, n, larghezza=1100):
    d = fitz.open(pdf)
    im = Image.open(io.BytesIO(d[n - 1].get_pixmap(dpi=150).tobytes("png"))).convert("RGB")
    d.close()
    return im.resize((larghezza, round(larghezza * im.height / im.width)), Image.LANCZOS)


def main():
    for pdf, n, nome in PAGINE:
        im = pagina(pdf, n)
        im.save(os.path.join(PAG, nome + ".webp"), "WEBP", quality=86, method=6)
    print("ecg-uk pages: " + ", ".join(n for *_r, n in PAGINE))


if __name__ == "__main__":
    main()

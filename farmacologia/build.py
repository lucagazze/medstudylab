# -*- coding: utf-8 -*-
"""
Farmacologia Illustrata — builder pagine A4.
_render/pXX.html -> pages/pXX.webp -> Farmacologia-Illustrata.pdf
Uso: python build.py [numeri di pagina da rigenerare]
"""
import os, io, asyncio, sys
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
REN = os.path.join(ROOT, "_render")
PAG = os.path.join(ROOT, "pages")
os.makedirs(REN, exist_ok=True)
os.makedirs(PAG, exist_ok=True)

W, H, SCALE, Q = 794, 1123, 3, 88

import pages1, pages2
PAGES = list(pages1.PAGES) + list(pages2.PAGES)
try:
    import pages3
    PAGES += list(pages3.PAGES)
except ImportError:
    pass

ONLY = [int(a) for a in sys.argv[1:] if a.isdigit()]


async def render():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={"width": W, "height": H}, device_scale_factor=SCALE)
        for i, html in enumerate(PAGES, 1):
            if ONLY and i not in ONLY:
                continue
            f = os.path.join(REN, f"p{i:02d}.html")
            open(f, "w", encoding="utf-8").write(html)
            await pg.goto("file:///" + f.replace("\\", "/"))
            await pg.wait_for_timeout(420)
            png = await pg.screenshot(clip={"x": 0, "y": 0, "width": W, "height": H})
            Image.open(io.BytesIO(png)).convert("RGB").save(
                os.path.join(PAG, f"p{i:02d}.webp"), "WEBP", quality=Q, method=6)
        await b.close()


asyncio.run(render())

# ------------------------------------------------------------------- pdf
import fitz
doc = fitz.open()
for f in sorted(os.listdir(PAG)):
    if not f.endswith(".webp"):
        continue
    im = Image.open(os.path.join(PAG, f)).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=90)
    p = doc.new_page(width=595.28, height=841.89)
    p.insert_image(p.rect, stream=buf.getvalue())
doc.save(os.path.join(ROOT, "Farmacologia-Illustrata.pdf"))
doc.close()

print("OK", len(PAGES), "pagine")

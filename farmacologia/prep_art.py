# -*- coding: utf-8 -*-
"""Toglie il fondo bianco dalle illustrazioni generate (jpeg -> png trasparente)."""
import os, glob
from PIL import Image, ImageDraw, ImageFilter

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "art")
MAGIC = (255, 0, 255)

for f in glob.glob(os.path.join(ART, "*.jpeg")):
    name = os.path.splitext(os.path.basename(f))[0]
    if name.startswith("_"):
        continue
    im = Image.open(f).convert("RGB")
    w, h = im.size
    d = ImageDraw.Draw(im)
    seeds = [(1, 1), (w - 2, 1), (1, h - 2), (w - 2, h - 2),
             (w // 2, 1), (w // 2, h - 2), (1, h // 2), (w - 2, h // 2)]
    for s in seeds:
        if im.getpixel(s) != MAGIC:
            ImageDraw.floodfill(im, s, MAGIC, thresh=44)
    px = im.load()
    alpha = Image.new("L", (w, h), 255)
    ap = alpha.load()
    for y in range(h):
        for x in range(w):
            if px[x, y] == MAGIC:
                ap[x, y] = 0
                px[x, y] = (255, 255, 255)
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.6))
    out = im.convert("RGBA")
    out.putalpha(alpha)
    out.save(os.path.join(ART, name + ".png"))
    print("ok", name)

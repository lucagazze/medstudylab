"""Export every generated asset to WebP at the size the landing page actually uses."""
import os
import shutil
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IMG = os.path.join(ROOT, "img")
BRAND = os.path.join(ROOT, "brand")
os.makedirs(IMG, exist_ok=True)
os.makedirs(BRAND, exist_ok=True)

# (source, destination, target width)
JOBS = [
    ("mockup-hero.png",        "img/kit-hero.webp",           1200),
    ("mockup-combo.png",       "img/kit-combo.webp",          1100),
    ("mockup-bonus-1.png",     "img/bonus-1.webp",             700),
    ("mockup-bonus-2.png",     "img/bonus-2.webp",             700),
    ("mockup-combo-pages.png", "img/kit-with-pages.webp",      900),
    ("page-p1.png",            "img/sample-1.webp",            820),
    ("page-p2.png",            "img/sample-2.webp",            820),
    ("page-p3.png",            "img/sample-3.webp",            820),
    ("page-p4.png",            "img/sample-4.webp",            820),
    ("page-p5.png",            "img/sample-5.webp",            820),
    ("char-student.jpeg",      "img/persona-student.webp",     900),
    ("char-grad-clean.jpeg",   "img/persona-graduate.webp",    900),
    ("char-pro.jpeg",          "img/persona-professional.webp", 900),
    ("textbook-boring.jpeg",   "img/textbook-dense.webp",      768),
    ("brand/og-image.png",     "brand/og-image.webp",         1200),
    ("brand/logo-mark.png",    "brand/logo-mark.webp",         256),
]

for src, dst, width in JOBS:
    img = Image.open(os.path.join(HERE, src))
    img = img.convert("RGBA") if img.mode in ("RGBA", "LA", "P") else img.convert("RGB")
    h = round(img.height * width / img.width)
    img = img.resize((width, h), Image.LANCZOS)
    out = os.path.join(ROOT, dst)
    img.save(out, "WEBP", quality=85, method=6)
    print("%-34s %4dx%-4d %6.1f KB" % (dst, width, h, os.path.getsize(out) / 1024))

# Favicons stay PNG/ICO — browsers need those formats
for name in ("icon-32.png", "icon-48.png", "icon-96.png", "icon-192.png",
             "icon-512.png", "apple-touch-icon.png", "favicon.ico"):
    shutil.copy(os.path.join(HERE, "brand", name), os.path.join(BRAND, name))
shutil.copy(os.path.join(HERE, "brand", "favicon.ico"), os.path.join(ROOT, "favicon.ico"))
print("favicons copied")

# Drop the Italian/Portuguese assets the new set replaces
for stale in ("esto.jpg", "mockup-bonus.webp", "mockup-bonus-2.webp",
              "mockup-combo-amostras.webp", "mockup-combo-entregaveis.webp"):
    p = os.path.join(ROOT, stale)
    if os.path.exists(p):
        os.remove(p)
        print("removed", stale)
for folder in ("amostras", "mockups", "personagens", "depoimentos"):
    p = os.path.join(ROOT, folder)
    if os.path.isdir(p):
        shutil.rmtree(p)
        print("removed", folder + "/")
# The author portrait is a plain stock photo with no localised content — keep it, just rehome it
old_author = os.path.join(ROOT, "foto-autor.webp")
if os.path.exists(old_author):
    a = Image.open(old_author).convert("RGB")
    a = a.resize((532, round(a.height * 532 / a.width)), Image.LANCZOS)
    a.save(os.path.join(IMG, "author.webp"), "WEBP", quality=85, method=6)
    os.remove(old_author)
    print("img/author.webp")

for stale in ("logo.jpg", "og-image.jpg"):
    p = os.path.join(BRAND, stale)
    if os.path.exists(p):
        os.remove(p)
        print("removed brand/" + stale)

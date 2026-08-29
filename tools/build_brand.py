"""Build favicons + a transparent logo mark from the new MedStudyLab logo."""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "brand")
os.makedirs(OUT, exist_ok=True)

src = Image.open(os.path.join(HERE, "logo-src.png")).convert("RGBA")

# The artwork is a circle on a white canvas: crop to the circle's bounding box.
bg = src.getpixel((2, 2))


def is_bg(px):
    return all(abs(px[i] - bg[i]) < 12 for i in range(3)) and px[3] > 0


w, h = src.size
px = src.load()
step = 4
xs, ys = [], []
for y in range(0, h, step):
    for x in range(0, w, step):
        if not is_bg(px[x, y]):
            xs.append(x)
            ys.append(y)
x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
side = max(x1 - x0, y1 - y0)
cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
pad = int(side * 0.02)
half = side // 2 + pad
box = (max(0, cx - half), max(0, cy - half), min(w, cx + half), min(h, cy + half))
mark = src.crop(box)

# Round the corners off into a clean circular mark on transparency
size = mark.size
circle = Image.new("L", (size[0] * 4, size[1] * 4), 0)
from PIL import ImageDraw
ImageDraw.Draw(circle).ellipse([0, 0, size[0] * 4 - 1, size[1] * 4 - 1], fill=255)
circle = circle.resize(size, Image.LANCZOS)
mark.putalpha(circle)
mark.save(os.path.join(OUT, "logo-mark.png"))
print("logo-mark.png", mark.size)

# Favicons: keep the light background so the icon reads on dark browser chrome
flat = Image.new("RGBA", size, (255, 255, 255, 255))
flat.paste(mark, (0, 0), mark)
flat = flat.convert("RGB")

for px_size, name in [(32, "icon-32.png"), (48, "icon-48.png"), (96, "icon-96.png"),
                      (192, "icon-192.png"), (512, "icon-512.png"),
                      (180, "apple-touch-icon.png")]:
    flat.resize((px_size, px_size), Image.LANCZOS).save(os.path.join(OUT, name))
    print(name)

flat.resize((256, 256), Image.LANCZOS).save(
    os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]
)
print("favicon.ico")

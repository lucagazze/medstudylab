"""Compose the 'kit + sample pages' mockup: a tablet in front of scattered sample sheets."""
import os
from PIL import Image, ImageFilter
from build_mockups import load_cover, make_tablet, drop_shadow, trim

HERE = os.path.dirname(os.path.abspath(__file__))

CANVAS = (1800, 3120)  # portrait, matches the original 900x1560 slot


def sheet(path, height, angle):
    img = Image.open(os.path.join(HERE, path)).convert("RGBA")
    w = int(img.width * height / img.height)
    img = img.resize((w, height), Image.LANCZOS)

    # thin border so white pages read against the white section background
    edged = Image.new("RGBA", (img.width + 4, img.height + 4), (222, 230, 244, 255))
    edged.paste(img, (2, 2))

    rot = edged.rotate(angle, expand=True, resample=Image.BICUBIC)
    return drop_shadow(rot, blur=26, offset=(0, 14), opacity=70, pad=90)


def place(canvas, img, cx, cy):
    canvas.alpha_composite(img, (int(cx - img.width / 2), int(cy - img.height / 2)))


if __name__ == "__main__":
    canvas = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    H = 1180

    # back row of sample pages, fanned out
    place(canvas, sheet("page-p1.png", H, 6),   360,  700)
    place(canvas, sheet("page-p2.png", H, -5), 1180,  560)
    place(canvas, sheet("page-p3.png", H, 4),   340, 1900)
    place(canvas, sheet("page-p4.png", H, -6), 1330, 1780)
    place(canvas, sheet("page-p5.png", H, 3),   880, 2560)

    # the tablet sits on top, centred
    main = load_cover("cover-main.jpeg", brand=False)
    tab = drop_shadow(make_tablet(main, 1560), blur=46, offset=(0, 30), opacity=135, pad=170)
    place(canvas, tab, CANVAS[0] // 2, 1450)

    canvas = trim(canvas, 24)
    canvas.save(os.path.join(HERE, "mockup-combo-pages.png"))
    print("mockup-combo-pages.png", canvas.size)

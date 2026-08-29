"""Compose tablet mockups for MedStudyLab from the generated covers."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
F_SEMI = "C:/Windows/Fonts/seguisb.ttf"

COVER_W, COVER_H = 1050, 1400  # 3:4 working size


def load_cover(name, brand=True, brand_color=(255, 255, 255, 235)):
    """Load a generated cover, resize to 3:4 and stamp the brand name."""
    img = Image.open(os.path.join(HERE, name)).convert("RGB")
    img = img.resize((COVER_W, COVER_H), Image.LANCZOS)
    if not brand:
        return img
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    font = ImageFont.truetype(F_SEMI, 30)
    text = "MedStudyLab"
    tw = d.textlength(text, font=font)
    x, y = (COVER_W - tw) / 2, COVER_H - 74
    # soft rounded plate behind the wordmark for legibility on any background
    pad_x, pad_y = 22, 11
    d.rounded_rectangle(
        [x - pad_x, y - pad_y, x + tw + pad_x, y + 38 + pad_y],
        radius=26, outline=brand_color, width=2,
    )
    d.text((x, y), text, font=font, fill=brand_color)
    return Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")


def rounded_mask(size, radius):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius=radius, fill=255)
    return m


def make_tablet(cover, height=1400):
    """Wrap a cover in a dark tablet bezel. Returns RGBA with transparent margins."""
    scale = height / COVER_H
    cw, ch = int(COVER_W * scale), int(COVER_H * scale)
    bezel = max(10, int(24 * scale))
    frame_r = int(52 * scale)
    screen_r = int(30 * scale)

    fw, fh = cw + bezel * 2, ch + bezel * 2
    frame = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
    d = ImageDraw.Draw(frame)
    # body
    d.rounded_rectangle([0, 0, fw - 1, fh - 1], radius=frame_r, fill=(44, 47, 54, 255))
    # subtle metallic edge highlight
    d.rounded_rectangle([0, 0, fw - 1, fh - 1], radius=frame_r, outline=(128, 133, 143, 255), width=max(2, int(3 * scale)))

    screen = cover.resize((cw, ch), Image.LANCZOS).convert("RGBA")
    frame.paste(screen, (bezel, bezel), rounded_mask((cw, ch), screen_r))

    # glass glare: soft diagonal band across the upper-left of the screen
    glare = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glare)
    gd.polygon(
        [(bezel, bezel), (bezel + cw * 0.52, bezel), (bezel + cw * 0.16, bezel + ch), (bezel, bezel + ch)],
        fill=(255, 255, 255, 16),
    )
    glare = glare.filter(ImageFilter.GaussianBlur(int(18 * scale)))
    glare.putalpha(Image.composite(glare.getchannel("A"), Image.new("L", (fw, fh), 0), rounded_mask((fw, fh), frame_r)))
    frame = Image.alpha_composite(frame, glare)

    # camera dot
    d = ImageDraw.Draw(frame)
    cr = max(2, int(5 * scale))
    d.ellipse([fw / 2 - cr, bezel / 2 - cr, fw / 2 + cr, bezel / 2 + cr], fill=(20, 22, 26, 255))
    return frame


def drop_shadow(img, blur=34, offset=(0, 22), opacity=105, pad=140):
    """Return img on a transparent canvas with a soft shadow behind it."""
    w, h = img.size
    canvas = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    alpha = img.getchannel("A").point(lambda a: min(opacity, a))
    solid = Image.new("RGBA", (w, h), (16, 24, 40, 255))
    solid.putalpha(alpha)
    sh.paste(solid, (pad + offset[0], pad + offset[1]), solid)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    canvas = Image.alpha_composite(canvas, sh)
    canvas.paste(img, (pad, pad), img)
    return canvas


def trim(img, margin=24):
    bbox = img.getchannel("A").getbbox()
    if not bbox:
        return img
    x0, y0, x1, y1 = bbox
    x0, y0 = max(0, x0 - margin), max(0, y0 - margin)
    x1, y1 = min(img.width, x1 + margin), min(img.height, y1 + margin)
    return img.crop((x0, y0, x1, y1))


def trio(center, left, right, out, canvas_ratio=None, side_h=0.86, overlap=0.30):
    """Three tablets: two behind at the sides, one in front centred."""
    c = make_tablet(center, 1400)
    l = make_tablet(left, int(1400 * side_h))
    r = make_tablet(right, int(1400 * side_h))

    c = drop_shadow(c, blur=40, offset=(0, 26), opacity=120, pad=160)
    l = drop_shadow(l, blur=30, offset=(-6, 18), opacity=85, pad=120)
    r = drop_shadow(r, blur=30, offset=(6, 18), opacity=85, pad=120)

    cw, ch = c.size
    lw, lh = l.size
    rw, rh = r.size

    gap = int(cw * (1 - overlap) * 0.5)
    total_w = cw + gap * 2 + int((lw + rw) * 0.30)
    total_h = max(ch, lh, rh) + 40
    canvas = Image.new("RGBA", (total_w, total_h), (0, 0, 0, 0))

    cx = (total_w - cw) // 2
    cy = (total_h - ch) // 2
    baseline = cy + ch

    canvas.paste(l, (cx - gap, baseline - lh - int(ch * 0.03)), l)
    canvas.paste(r, (cx + cw + gap - rw, baseline - rh - int(ch * 0.03)), r)
    canvas.paste(c, (cx, cy), c)

    canvas = trim(canvas, 30)
    if canvas_ratio:
        tw = canvas.width
        th = int(tw / canvas_ratio)
        if th < canvas.height:
            th = canvas.height
            tw = int(th * canvas_ratio)
        fitted = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
        fitted.paste(canvas, ((tw - canvas.width) // 2, (th - canvas.height) // 2), canvas)
        canvas = fitted
    canvas.save(os.path.join(HERE, out))
    print(out, canvas.size)


if __name__ == "__main__":
    main = load_cover("cover-main.jpeg", brand=False)
    b1 = load_cover("cover-bonus1.jpeg", brand_color=(255, 255, 255, 220))
    b2 = load_cover("cover-bonus2.jpeg", brand_color=(255, 255, 255, 230))
    main.save(os.path.join(HERE, "cover-main-branded.png"))
    b1.save(os.path.join(HERE, "cover-bonus1-branded.png"))
    b2.save(os.path.join(HERE, "cover-bonus2-branded.png"))

    # Hero: wide trio
    trio(main, b1, b2, "mockup-hero.png", canvas_ratio=1200 / 886)
    # Offer box: slightly wider trio
    trio(main, b1, b2, "mockup-combo.png", canvas_ratio=1100 / 723, overlap=0.42)

    # Single tablets for the bonus cards
    for cov, name in ((b1, "mockup-bonus-1.png"), (b2, "mockup-bonus-2.png")):
        t = drop_shadow(make_tablet(cov, 1400), blur=34, offset=(0, 20), opacity=100, pad=110)
        t = trim(t, 20)
        t.save(os.path.join(HERE, name))
        print(name, t.size)

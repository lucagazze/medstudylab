# -*- coding: utf-8 -*-
"""
Le immagini della landing /dentistry.

Fa le stesse cose di `asset_ecg.py`, da cui copia il CSS del tablet e il
render con Playwright, ma senza la parte dei tracciati: qui non c'e' niente
da disegnare a parte le pagine del libro, che esistono gia'.

  hero.webp              i tre tablet, l'anatomia al centro
  og.jpg                 l'anteprima per WhatsApp e Facebook
  combo.webp             il collage: otto pagine intorno al tablet
  bonus-biologia.webp    i due volumi in regalo, nel tablet dell'index
  bonus-quiz.webp
  ../anteprime/anatomia_0N   le sette anteprime del carosello

LA COPERTINA DEI QUIZ non esiste come file: quel progetto impagina tutto
dal JSON e non tiene una `copertina.jpeg` da parte. Si estrae dalla prima
pagina del PDF venduto, che e' anche la garanzia che sia quella giusta —
la stessa che il cliente ha comprato.

  python scripts/asset_anatomia.py
"""
import asyncio
import io
import os

from PIL import Image

SITO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SITO, "mockups", "dentistry")
ANTE = os.path.join(SITO, "anteprime")
PROG = (r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos"
        r"\Proyectos (código de los libros)")
EBOOKS = (r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos"
          r"\Studio Facile\Ebooks")

PAGINE = os.path.join(r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos", "Dental-US", "pagine")
COP_ANA = os.path.join(PAGINE, "cover.jpeg")
# I due bonus scelti da Luca (30/09/2026): i prontuari clinici, non i volumi
# di biologia con cui la landing era nata.
COP_EM = os.path.join(r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos", "DentalTrays-US",
                      "pagine", "cover.jpeg")
COP_ANTI = os.path.join(r"C:\Users\lucag\Desktop\CLAUDE\Infoproductos", "DentalEmerg-US",
                        "pagine", "cover.jpeg")

# Le sette pagine che diventano anteprime, nell'ordine del carosello.
# Devono corrispondere ad ANTEPRIME in landing_anatomia.py.
# Scelte per mostrare una cosa diversa ciascuna: il vocabolario, il
# confronto fra vertebre, una sezione con le logge, l'aggancio clinico
# delle coronarie, il pugno nel palloncino, la tabella dei nervi cranici,
# e una domanda d'esame risolta — che e' quello che chiude la vendita.
ANTEPRIME = ["num_us", "lay_a", "kit_a", "t_rest_a",
             "comp_b", "chain_a", "nerves"]
# Otto fogli intorno al tablet, tutti diversi dalle anteprime dove si puo',
# cosi' chi scorre non vede due volte la stessa pagina.
COLLAGE = ["t_endo_a", "bur_a", "surf_a", "auto_a",
           "imp_a", "plaque", "dam_a", "t_ext_a"]

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:transparent}
.stage{position:relative}
.tab{position:absolute;border-radius:38px;padding:13px;
  background:linear-gradient(150deg,#4a4d55 0%,#2c2e35 38%,#212329 100%);
  box-shadow:0 34px 64px rgba(15,23,42,.34), 0 8px 18px rgba(15,23,42,.20),
             inset 0 1px 0 rgba(255,255,255,.22), inset 0 -1px 0 rgba(0,0,0,.35);}
.tab .scr{width:100%;height:100%;border-radius:26px;overflow:hidden;background:#fff;
  box-shadow:inset 0 0 0 1px rgba(0,0,0,.35)}
.tab .scr img{width:100%;height:100%;object-fit:cover;display:block}
.tab .gl{position:absolute;inset:13px;border-radius:26px;pointer-events:none;
  background:linear-gradient(118deg,rgba(255,255,255,.30) 0%,rgba(255,255,255,.07) 26%,
             rgba(255,255,255,0) 46%)}
.sheet{position:absolute;border-radius:10px;overflow:hidden;background:#fff;
  box-shadow:0 16px 34px rgba(15,23,42,.20)}
.sheet img{width:100%;height:100%;object-fit:cover;display:block}
"""


def _uri(p):
    return "file:///" + p.replace("\\", "/")


def page(w, h, body):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}'
            f'body{{width:{w}px;height:{h}px}}</style></head><body>'
            f'<div class="stage" style="width:{w}px;height:{h}px">{body}'
            f'</div></body></html>')


def tab(src, x, y, w, h, z=1):
    return (f'<div class="tab" style="left:{x}px;top:{y}px;width:{w}px;'
            f'height:{h}px;z-index:{z}"><div class="scr"><img src="{_uri(src)}"'
            f' alt=""></div><div class="gl"></div></div>')


async def rendi(lavori):
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(channel="msedge")
        for nome, html, w, h, trasparente in lavori:
            pg = await b.new_page(viewport={"width": w, "height": h},
                                  device_scale_factor=2)
            f = os.path.join(OUT, f"_{nome}.html")
            open(f, "w", encoding="utf-8").write(html)
            await pg.goto(_uri(f))
            await pg.wait_for_timeout(700)
            png = await pg.screenshot(omit_background=trasparente,
                                      clip={"x": 0, "y": 0, "width": w,
                                            "height": h})
            os.remove(f)
            im = Image.open(io.BytesIO(png))
            if nome == "og":
                p = os.path.join(OUT, "og.jpg")
                im.convert("RGB").save(p, "JPEG", quality=88)
            else:
                p = os.path.join(OUT, nome + ".webp")
                im.convert("RGBA").save(p, "WEBP", quality=88, method=6)
            print(f"  {os.path.basename(p):<24} {im.size[0]}x{im.size[1]}  "
                  f"{os.path.getsize(p) // 1024} KB")
            await pg.close()
        await b.close()


def _webp(src, dest, larghezza):
    im = Image.open(src).convert("RGB")
    im = im.resize((larghezza, round(larghezza * im.height / im.width)),
                   Image.LANCZOS)
    im.save(dest, "WEBP", quality=86, method=6)
    print(f"  {os.path.basename(dest):<24} {im.size[0]}x{im.size[1]}  "
          f"{os.path.getsize(dest) // 1024} KB")


# Il «QUESTO» del confronto. La prima versione era un ritaglio del pannello
# COSÌ NO della pagina a6, e non funzionava: si portava dietro la didascalia
# «A sinistra: ventidue nomi in fila...», che dentro al libro ha senso perché
# c'è un «a destra», e da sola sulla landing non vuol dire niente.
# Questa invece è la cosa che il lettore fa davvero la sera prima: la lista da
# mandare a memoria. Sono nomi anatomici veri — il carpo e i muscoli della
# spalla e del braccio — messi in colonna, tutti uguali, senza un disegno.
# Non è la pagina di nessun concorrente: è il METODO che il libro dice di
# smettere, e disegnarlo noi è l'unico modo onesto di mostrarlo.
NOMI = ["Mouth mirror", "Explorer", "Cotton pliers", "Excavator",
        "Periodontal probe", "Cement spatula", "Matrix retainer",
        "Matrix band", "Aspirating syringe", "Rubber dam clamp",
        "Dam frame", "Clamp forceps", "Dam punch", "High-speed handpiece",
        "Contra-angle", "Straight attachment", "Ultrasonic scaler",
        "Curette", "Periosteal elevator", "Elevator", "Needle holder"]

CSS_LISTA = """
body{margin:0;background:#fff;font-family:'Inter',system-ui,sans-serif}
.f{width:900px;height:1190px;padding:64px 70px;box-sizing:border-box;
   background:#fff;position:relative}
.t{font-size:30px;font-weight:800;letter-spacing:.04em;color:#8b8f9a;
   text-transform:uppercase;margin-bottom:8px}
.s{font-size:19px;color:#a9adb8;margin-bottom:38px}
.c{column-count:2;column-gap:46px}
.n{font-size:25px;line-height:2.05;color:#6f7480;break-inside:avoid;
   border-bottom:1px solid #edeef2}
"""


def _lista_questo():
    voci = "".join(f'<div class="n">{x}</div>' for x in NOMI)
    html = (f'<!doctype html><html><head><meta charset="utf-8">'
            f'<style>{CSS_LISTA}</style></head><body><div class="f">'
            f'<div class="t">Names to memorize</div>'
            f'<div class="s">before Monday</div>'
            f'<div class="c">{voci}</div></div></body></html>')
    return ("questo", html, 900, 1190, False)


def main():
    os.makedirs(OUT, exist_ok=True)
    if not os.path.exists(COP_ANA):
        raise SystemExit("manca la copertina del volume principale")
    # il secondo bonus si sta ancora generando: se la copertina non c'e'
    # si usa quella del primo come segnaposto e si rigenera dopo
    global COP_ANTI
    if not os.path.exists(COP_ANTI):
        print("  (manca la copertina del bonus 2: uso un segnaposto)")
        COP_ANTI = COP_EM

    lavori = [
        ("bonus-trays", page(720, 1000, tab(COP_EM, 40, 40, 640, 920)),
         720, 1000, True),
        ("bonus-emerg",
         page(720, 1000, tab(COP_ANTI, 40, 40, 640, 920)), 720, 1000, True),
        _lista_questo(),
    ]

    trio = (tab(COP_EM, 36, 35, 460, 640) + tab(COP_ANTI, 704, 35, 460, 640)
            + tab(COP_ANA, 300, 35, 600, 838, 3))
    lavori.append(("hero", page(1200, 886, trio), 1200, 886, True))
    og = (f'<div style="position:absolute;inset:0;background:'
          f'linear-gradient(135deg,#2645a0,#1b3277)"></div>'
          f'<div style="position:absolute;left:204px;top:22px;transform:'
          f'scale(.66);transform-origin:top left">{trio}</div>')
    lavori.append(("og", page(1200, 630, og), 1200, 630, False))

    pronte = [k for k in COLLAGE
              if os.path.exists(os.path.join(PAGINE, k + ".jpeg"))]
    if len(pronte) == len(COLLAGE):
        fogli = [(-60, -30, -7), (330, -70, 5), (660, -20, 9), (-90, 480, 4),
                 (620, 500, -6), (-40, 990, -9), (350, 1030, 3),
                 (660, 980, 7)]
        parti = []
        for (x, y, r), k in zip(fogli, COLLAGE):
            src = os.path.join(PAGINE, k + ".jpeg")
            parti.append(f'<div class="sheet" style="left:{x}px;top:{y}px;'
                         f'width:470px;height:665px;transform:rotate({r}deg)">'
                         f'<img src="{_uri(src)}" alt=""></div>')
        parti.append(tab(COP_ANA, 270, 400, 560, 786, 6))
        lavori.append(("combo", page(1100, 1620, "".join(parti)), 1100, 1620,
                       True))
    else:
        print(f"  combo: pagine pronte {len(pronte)}/{len(COLLAGE)}, lo salto")

    print("mockup:")
    asyncio.run(rendi(lavori))

    fatte = 0
    for i, k in enumerate(ANTEPRIME, 1):
        src = os.path.join(PAGINE, k + ".jpeg")
        if os.path.exists(src):
            _webp(src, os.path.join(ANTE, f"dentistry_{i:02d}.webp"), 1100)
            fatte += 1
    print(f"anteprime: {fatte}/{len(ANTEPRIME)}")


if __name__ == "__main__":
    main()

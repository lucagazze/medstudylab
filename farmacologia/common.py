# -*- coding: utf-8 -*-
"""Helper condivisi per la costruzione delle pagine."""

A = "../art"

HEAD = """<!doctype html><html lang="it"><head><meta charset="utf-8">
<link rel="stylesheet" href="../style.css"></head><body>"""
FOOT = "</body></html>"


def band(pos):
    return f'<div class="band {pos}"><i></i><i></i><i></i><i></i><i></i></div>'


def shell(inner, folio=None):
    f = f'<div class="folio">{folio}</div>' if folio else ""
    return (HEAD + '<div class="page">' + band("top") + inner
            + band("bottom") + f + '</div>' + FOOT)


def head(eyebrow, title, size=33):
    return (f'<div class="hd"><div class="eyebrow"><b></b>{eyebrow}</div>'
            f'<h1 class="title" style="font-size:{size}px;margin-top:6px">{title}</h1></div>')


def row(c, ic, t, p, narrow=False):
    n = " narrow" if narrow else ""
    return (f'<div class="row {c}{n}"><div class="disc"><img src="{A}/{ic}.png"></div>'
            f'<div class="txt"><h2>{t}</h2><p>{p}</p></div></div>')


def note(ic, t, p, style=""):
    return (f'<div class="note" style="{style}"><img src="{A}/{ic}.png"><div>'
            f'<h4>{t}</h4><p>{p}</p></div></div>')


def strip(items, bg="var(--sky-s)", sep="var(--sky)"):
    inner = f'<div class="sep" style="background:{sep}"></div>'.join(
        f'<div class="b"><b>{t}</b>{d}</div>' for t, d in items)
    return f'<div class="strip" style="background:{bg}">{inner}</div>'


def flow(items):
    """items: [(icona, etichetta), ...] con frecce fra un elemento e l'altro."""
    parts = []
    for i, (ic, lab) in enumerate(items):
        if i:
            parts.append('<span class="ar">→</span>')
        parts.append(f'<div class="f"><img src="{A}/{ic}.png">'
                     f'<span>{lab}</span></div>')
    return f'<div class="flow">{"".join(parts)}</div>'


def bullets(items):
    return '<ul class="bul">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def via(tag, color, ics, desc, buls, extra=""):
    """Pannello per una via di somministrazione."""
    return (f'<div class="panel {color}"><span class="tag {"r" if color=="rose" else "p"}">{tag}</span>'
            f'{flow(ics)}'
            f'<div class="concl">{desc}</div>'
            f'{bullets(buls)}{extra}</div>')


def k(tag, tagcls, title, body, ex="", ico="", cls="", big=""):
    i = f'<img class="ico" src="{A}/{ico}.png">' if ico else ""
    h = f'<h4>{title}</h4>' if title else ""
    e = f'<div class="ex">{ex}</div>' if ex else ""
    g = f'<img class="big" src="{A}/{big}.png">' if big else ""
    return (f'<div class="k {cls}">{i}<span class="tag {tagcls}">{tag}</span>'
            f'{h}<p>{body}</p>{e}{g}</div>')

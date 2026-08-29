# -*- coding: utf-8 -*-
"""Localise the remaining US/Spanish copy for the UK launch."""
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WHO = [
    ("Julieta<span>Anatomy Course</span>",     "Grace<span>MPharm, Year 2</span>"),
    ("Miriam<span>Anatomy Course</span>",      "Amelia<span>BSc Nursing, Year 1</span>"),
    ("Laudid<span>Anatomy Course</span>",      "Sophie<span>MPharm, Year 1</span>"),
    ("Sheila<span>Organic Chemistry</span>",   "Olivia<span>Medicine, Year 2</span>"),
    ("Claudia<span>Anatomy Course</span>",     "Charlotte<span>BSc Nursing, Year 2</span>"),
    ("Alfredo<span>Biochemistry</span>",       "Thomas<span>Medicine, Year 3</span>"),
    ("Denise<span>Organic Chemistry</span>",   "Freya<span>Pharmacy technician</span>"),
    ("Apolonia<span>Anatomy Course</span>",    "Emily<span>MPharm, Year 3</span>"),
    ("Alejandra<span>Anatomy Course</span>",   "Isla<span>BSc Nursing, Year 3</span>"),
    ("Francisco<span>Biochemistry</span>",     "Harry<span>Medicine, Year 2</span>"),
]

TOAST = [
    ('<span class="sp-name" id="spName">Sarah from Chicago</span>',
     '<span class="sp-name" id="spName">Sarah from Manchester</span>'),
    ('{ name: "Sarah from New York",',    '{ name: "Sarah from Manchester",'),
    ('{ name: "David from London",',      '{ name: "David from London",'),
    ('{ name: "Emma from Sydney",',       '{ name: "Emma from Birmingham",'),
    ('{ name: "Michael from Toronto",',   '{ name: "Michael from Glasgow",'),
    ('{ name: "Jessica from Los Angeles",', '{ name: "Jessica from Leeds",'),
    ('{ name: "James from Chicago",',     '{ name: "James from Edinburgh",'),
    ('{ name: "Sophia from Boston",',     '{ name: "Sophia from Bristol",'),
    ('{ name: "Daniel from Dublin",',     '{ name: "Daniel from Cardiff",'),
]

# "Real verified reviews" is an unevidenced verification claim — the ASA treats that as
# a substantiation issue, so soften it to what can actually be stood behind.
COPY = [
    ("Real verified reviews from students and healthcare professionals.",
     "Reviews sent in by students and healthcare professionals using our materials."),
    ("memorization", "memorisation"),
    ("Memorization", "Memorisation"),
    ("organized", "organised"),
    ("Organized", "Organised"),
    ("recognize", "recognise"),
    ("summarize", "summarise"),
    ("toLocaleDateString('en-US'", "toLocaleDateString('en-GB'"),
]


def main():
    p = os.path.join(ROOT, "index.html")
    with io.open(p, encoding="utf-8") as f:
        s = f.read()

    misses = []
    for a, b in WHO + TOAST + COPY:
        if a not in s:
            misses.append(a[:60])
        s = s.replace(a, b)

    with io.open(p, "w", encoding="utf-8") as f:
        f.write(s)

    print("patched. not found:", misses if misses else "none")


if __name__ == "__main__":
    main()

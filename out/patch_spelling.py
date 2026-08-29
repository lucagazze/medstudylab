# -*- coding: utf-8 -*-
"""Final pass: British spelling and UK-appropriate drug/placement wording."""
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAIRS = [
    ("Understand instead of memorizing.", "Understand instead of memorising."),
    ("understand instead of memorizing blindly", "understand instead of memorising blindly"),
    ("the visual system that organizes everything", "the visual system that organises everything"),
    ("Direct language, visual organization,", "Direct language, visual organisation,"),
    ("the colors and diagrams are fantastic", "the colours and diagrams are fantastic"),
    ("<li>Fast to memorize</li>", "<li>Fast to memorise</li>"),
    # UK students go on placements, not rotations
    ("taking to clinical rotations", "taking on clinical placements"),
    ("take it to clinical rotations", "take it on clinical placements"),
    ("take to clinical rotations", "take on clinical placements"),
    # UK generic name first; Tylenol is a US brand not sold in the UK
    ("Brand names: understanding Acetaminophen = Paracetamol = Tylenol",
     "Brand names: understanding Paracetamol = Acetaminophen = Panadol"),
    ("why Acetaminophen = Paracetamol = Tylenol",
     "why Paracetamol = Acetaminophen = Panadol"),
]


def main():
    for fname in ("index.html", "refund-policy.html"):
        p = os.path.join(ROOT, fname)
        if not os.path.exists(p):
            continue
        with io.open(p, encoding="utf-8") as f:
            s = f.read()
        hits = 0
        for a, b in PAIRS:
            if a in s:
                hits += s.count(a)
                s = s.replace(a, b)
        with io.open(p, "w", encoding="utf-8") as f:
            f.write(s)
        print("%s: %d replacements" % (fname, hits))


if __name__ == "__main__":
    main()

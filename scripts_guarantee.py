# -*- coding: utf-8 -*-
"""
The guarantee, across MedStudyLab: from "no questions asked" to
"tell me what didn't work".

  python scripts_guarantee.py          apply
  python scripts_guarantee.py --dry    say what it would do

Same change already made on studiofacilebook.com. Refunds were coming in
with no real reason — not because buyers were gaming anything, but
because the pages offered exactly that, in writing and three times over:
"or simply wasn't what you expected", "No questions", "Guarantee: 30 days
no questions asked".

Three edits per page:
  1. the guarantee sentence asks for one line instead of offering the
     refund for "wasn't what you expected";
  2. every "no questions" variant goes;
  3. under the samples subtitle: those are real pages of the book, and
     the contents shown on the page are the book's contents.

THE NUMBERS COME FROM EACH PAGE, never invented. Writing "6 parts and 28
chapters" on the ECG page would wreck the one sentence whose whole job is
to let the buyer check what they are getting. Where a page sells a
three-book kit (pharm, retake) there is no single table of contents, so
its line does not claim one.

WHAT STAYS, on purpose: the 30 days, the 100%, the "Risk-Free" heading
and the badge by the button. Those sell and they are not the cause.

NOT DONE HERE: refund-policy.html still says "unconditional" and "no
justification required". While that stands, a Stripe dispute reads that
one and the rest is decoration.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
MAIL = "info@medicalstudylab.com"

# Tres variantes distintas conviven en el sitio. El orden importa: la
# larga primero, porque la corta esta contenida en ella.
CAMBIOS = [
    ("If in that time you feel the material didn't help you, wasn't useful "
     "or simply wasn't what you expected,",
     "If the book doesn't help you study, email me what didn't work and"),
    ("No questions. No fine print. No hassle.",
     "No fine print, no hassle. One email is enough."),
    ("No questions. No small print. No hassle.",
     "No small print, no hassle. One email is enough."),
    ("No questions asked. No hidden clauses. Zero hassle.",
     "No hidden clauses, zero hassle. One email is enough."),
    ("No questions, no fine print.", "No fine print, no hassle."),
    ("30-day guarantee, no questions asked: try it risk-free",
     "30-day guarantee: if it doesn't help, I refund you"),
    ("Guarantee: 30 days, no questions asked", "Guarantee: 30 days"),
    ("Guarantee: 30 days no questions asked", "Guarantee: 30 days"),
]

FAQ = ("What if it doesn't help me?",
       "You have 30 days. Email me at "
       '<a href="mailto:%s">%s</a> telling me what didn\'t work and I refund '
       "you in full. I ask not to argue, but because that is how I fix the "
       "book for the next person." % (MAIL, MAIL))

# Lo que cada pagina dice de si misma. Nada de esto se invento: sale del
# indice o del bloque de contenidos de la propia pagina.
INDICE = "the contents shown on this page are the book's full contents: "
FORMATO = ("It is a PDF to download: it is not a video course and it is not "
           "a printed book.")
REAL = "These are real pages of the book, not mockups. "

LINEA = {
    "ecg-uk": REAL + INDICE + "8 parts and 51 chapters, in that order. " + FORMATO,
    "ekg": REAL + INDICE + "8 parts and 51 chapters, in that order. " + FORMATO,
    "ekg-ems": REAL + INDICE + "8 parts and 51 chapters, in that order. " + FORMATO,
    "index": REAL + INDICE + "6 parts and 28 chapters, in that order. " + FORMATO,
    "aus": REAL + INDICE + "6 parts and 28 chapters, in that order. " + FORMATO,
    "ca": REAL + INDICE + "6 parts and 28 chapters, in that order. " + FORMATO,
    "usd": REAL + INDICE + "6 parts and 28 chapters, in that order. " + FORMATO,
    "abg": REAL + "the table of contents below is the book's full contents: "
                  "all 8 parts, in that order. " + FORMATO,
    "dosage": REAL + "the main book is 40 illustrated pages in 5 parts, and "
                     "what you see below is what is in it. " + FORMATO,
    # kit de tres libros: no hay un indice unico y no se finge que lo haya
    "pharm": REAL + FORMATO,
    "retake": REAL + FORMATO,
}


def mete_linea(s, nombre):
    if "real pages of the book" in s:
        return s, "already there"
    m = re.search(r"<h2[^>]*>[^<]{0,80}Pages[^<]{0,40}</h2>", s)
    if not m:
        return s, "NO samples heading found"
    p = re.search(r'<p class="[^"]*section-sub-p[^"]*"[^>]*>.*?</p>',
                  s[m.end():], re.S)
    if not p:
        return s, "NO subtitle under the heading"
    corte = m.end() + p.end()
    linea = ('\n      <p class="text-center section-sub-p" '
             'style="max-width:720px;margin:-6px auto 0;">\n        %s\n'
             '      </p>' % LINEA[nombre])
    return s[:corte] + linea + s[corte:], "ok"


def mete_faq(s):
    if 'id="faq-refund"' in s:
        return s, "already there"
    items = list(re.finditer(r'<div class="faq-item">.*?</div>\s*</div>',
                             s, re.S))
    if not items:
        return s, "NO faq on the page"
    bloque = ('\n        <div class="faq-item">\n'
              '          <button class="faq-question" aria-expanded="false" '
              'aria-controls="faq-refund">\n            %s\n'
              '          </button>\n'
              '          <div class="faq-answer" id="faq-refund" hidden>\n'
              '            <p>%s</p>\n          </div>\n        </div>'
              % FAQ)
    fin = items[-1].end()
    return s[:fin] + bloque + s[fin:], "ok"


def una(nombre, dry=False):
    p = os.path.join(RAIZ, nombre + ".html")
    if not os.path.exists(p):
        print("  %-10s does not exist" % nombre)
        return
    s = io.open(p, encoding="utf-8").read()
    antes = s
    n = 0
    for viejo, nuevo in CAMBIOS:
        if viejo in s:
            s = s.replace(viejo, nuevo)
            n += 1
    s, est_l = mete_linea(s, nombre)
    s, est_f = mete_faq(s)
    print("  %-10s %-11s  line: %-26s  faq: %s"
          % (nombre, "%d phrases" % n if n else "no phrases", est_l, est_f))
    if not dry and s != antes:
        io.open(p, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    dry = "--dry" in sys.argv
    for k in LINEA:
        una(k, dry)

# -*- coding: utf-8 -*-
"""
Genera le pagine del libro come immagini intere con Gemini (nano-banana).

  python3 gen.py 6 7 8        una lista di pagine
  python3 gen.py 6-20         un intervallo
  python3 gen.py 6-20 -j 4    con 4 richieste in parallelo
  python3 gen.py 12 -s b      salva come p12b.jpg (variante, non sovrascrive)

La API key si legge, in ordine:  $GEMINI_API_KEY  ->  farmacologia-ai/.key
(.key e' in .gitignore: non finisce mai su GitHub).
"""
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from pages import PAGES

ROOT = os.path.dirname(os.path.abspath(__file__))
MODEL = "gemini-3-pro-image-preview"


def api_key():
    k = os.environ.get("GEMINI_API_KEY", "").strip()
    if k:
        return k
    p = os.path.join(ROOT, ".key")
    if os.path.exists(p):
        return open(p).read().strip().split("=")[-1].strip()
    sys.exit("Manca la API key: export GEMINI_API_KEY=... oppure scrivila in farmacologia-ai/.key")


URL = ("https://generativelanguage.googleapis.com/v1beta/models/"
       + MODEL + ":generateContent?key=")


def gen(n, suffix="", tries=3):
    slug, prompt = PAGES[n]
    body = {"contents": [{"parts": [{"text": " ".join(prompt.split())}]}],
            "generationConfig": {"imageConfig": {"aspectRatio": "3:4",
                                                 "imageSize": "2K"}}}
    data = json.dumps(body).encode()
    for attempt in range(1, tries + 1):
        try:
            req = urllib.request.Request(URL + api_key(), data=data,
                                         headers={"Content-Type": "application/json"})
            r = json.loads(urllib.request.urlopen(req, timeout=900).read())
            for p in r["candidates"][0]["content"]["parts"]:
                if "inlineData" in p:
                    out = os.path.join(ROOT, "p%02d%s.jpg" % (n, suffix))
                    with open(out, "wb") as fh:
                        fh.write(base64.b64decode(p["inlineData"]["data"]))
                    print("ok   p%02d %s" % (n, slug), flush=True)
                    return out
            reason = r["candidates"][0].get("finishReason", "?")
            print("vuota p%02d (%s) tentativo %d" % (n, reason, attempt), flush=True)
        except urllib.error.HTTPError as e:
            msg = e.read()[:200].decode("utf8", "replace")
            print("HTTP %s p%02d tentativo %d: %s" % (e.code, n, attempt, msg), flush=True)
            if e.code in (400, 401, 403):
                break
        except Exception as e:
            print("errore p%02d tentativo %d: %s" % (n, attempt, e), flush=True)
        time.sleep(5 * attempt)
    print("FALLITA p%02d %s" % (n, slug), flush=True)
    return None


def parse(args):
    out, suffix, jobs = [], "", 1
    it = iter(range(len(args)))
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("-s", "--suffix"):
            i += 1
            suffix = args[i]
        elif a in ("-j", "--jobs"):
            i += 1
            jobs = int(args[i])
        elif "-" in a and not a.startswith("-"):
            lo, hi = a.split("-")
            out += list(range(int(lo), int(hi) + 1))
        else:
            out.append(int(a))
        i += 1
    return (out or sorted(PAGES)), suffix, jobs


if __name__ == "__main__":
    todo, suffix, jobs = parse(sys.argv[1:])
    todo = [n for n in todo if n in PAGES] or sys.exit("Nessuna pagina valida in PAGES")
    if jobs > 1:
        with ThreadPoolExecutor(jobs) as ex:
            list(ex.map(lambda n: gen(n, suffix), todo))
    else:
        for n in todo:
            gen(n, suffix)

import os
import threading
import functools
import http.server
import socketserver
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qa")
os.makedirs(SHOTS, exist_ok=True)
PORT = 8731

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
threading.Thread(target=httpd.serve_forever, daemon=True).start()

URL = "http://127.0.0.1:%d/index.html" % PORT
VIEWPORTS = [("mobile", 390, 844), ("tablet", 768, 1024), ("desktop", 1280, 900)]

problems = []

with sync_playwright() as pw:
    b = pw.chromium.launch()
    for name, w, h in VIEWPORTS:
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        errs, bad = [], []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("response", lambda r: bad.append("%d %s" % (r.status, r.url)) if r.status >= 400 else None)
        pg.goto(URL, wait_until="networkidle")
        pg.wait_for_timeout(1800)

        # force every lazy image to load before we judge the page
        pg.evaluate("""() => new Promise(res => {
            let y = 0; const step = () => {
              window.scrollTo(0, y); y += window.innerHeight;
              if (y < document.body.scrollHeight + window.innerHeight) setTimeout(step, 90);
              else { window.scrollTo(0,0); setTimeout(res, 700); }
            }; step();
        })""")
        pg.wait_for_timeout(900)

        overflow = pg.evaluate(
            "() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
        broken = pg.evaluate("""() => [...document.images]
            .filter(i => !i.complete || i.naturalWidth === 0)
            .map(i => i.currentSrc || i.src)""")

        if overflow > 0:
            problems.append("%s: horizontal overflow %dpx" % (name, overflow))
        if broken:
            problems.append("%s: broken images %s" % (name, broken))
        if errs:
            problems.append("%s: console errors %s" % (name, errs[:4]))
        if bad:
            problems.append("%s: failed requests %s" % (name, bad[:4]))

        pg.screenshot(path=os.path.join(SHOTS, "%s-full.png" % name), full_page=True)
        pg.close()
        print("%-8s overflow=%d broken=%d errors=%d failed=%d"
              % (name, overflow, len(broken), len(errs), len(bad)))
    b.close()

httpd.shutdown()
print("\nPROBLEMS:" if problems else "\nNo problems found.")
for p in problems:
    print(" -", p)

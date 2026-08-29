import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "file:///" + os.path.join(HERE, "pages.html").replace("\\", "/")
IDS = ["p1", "p2", "p3", "p4", "p5"]

with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width": 900, "height": 1200}, device_scale_factor=2)
    pg.goto(URL)
    pg.wait_for_timeout(2500)
    for i in IDS:
        el = pg.query_selector("#" + i)
        el.screenshot(path=os.path.join(HERE, f"page-{i}.png"))
        print("page-%s.png" % i)
    b.close()

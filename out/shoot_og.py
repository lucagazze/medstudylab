import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "file:///" + os.path.join(HERE, "og.html").replace("\\", "/")

with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width": 1240, "height": 700}, device_scale_factor=1)
    pg.goto(URL)
    pg.wait_for_timeout(2500)
    pg.query_selector("#og").screenshot(path=os.path.join(HERE, "brand", "og-image.png"))
    b.close()
print("og-image.png done")

# Asset build scripts

These are the scripts that produced everything in `img/` and `brand/`. They are kept so the
artwork can be regenerated or tweaked later — they are **not** part of the site build.

They expect to run from a scratch directory holding the intermediate PNG/JPEG files
(`cover-main.jpeg`, `page-p1.png`, …). Copy them next to those intermediates before running.
The three source covers are archived here as WebP in `covers/`.

| Script | What it does |
|---|---|
| `build_mockups.py` | Wraps the covers in tablet bezels; builds the hero and offer-box trios |
| `build_combo_pages.py` | Tablet over a fan of sample pages |
| `pages.html` + `shoot_pages.py` | The five sample pages, rendered to PNG with Playwright |
| `og.html` + `shoot_og.py` | Open Graph image |
| `build_brand.py` | Favicons and the circular logo mark, from the source logo |
| `export_assets.py` | Resizes and writes every final WebP into `img/` and `brand/` |
| `qa.py` | Serves the site and checks 390/768/1280 for overflow, broken images, console errors |

The covers themselves were generated with `nano-banana` (Gemini 3 Pro Image); the prompts are
not reproducible verbatim, which is why the outputs are archived rather than regenerated.

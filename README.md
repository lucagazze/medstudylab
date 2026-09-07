# Illustrated Pharmacology — MedStudyLab

Landing page for the Illustrated Pharmacology Kit (28 illustrated chapters + 2 bonuses, £15 GBP).
Copy, artwork and spelling are fully localised for the UK and other English-speaking markets.

## Structure
- `index.html` — Landing page (pure HTML/CSS/JS, no build step)
- `refund-policy.html` — 30-day money-back guarantee and refund policy
- `img/` — All page artwork, WebP
- `brand/` — Logo mark, favicons, Open Graph image
- `vercel.json` — Vercel config: clean URLs, www -> apex redirect, HSTS
- `.htaccess` — the same rules for Apache/Hostinger
- `.vercelignore` — keeps the book PDF and the tooling out of the deploy

All images are served from this repo — there are no external asset hosts.

## Artwork
| File | What it is |
|---|---|
| `img/kit-hero.webp` | Hero: the three covers on tablets |
| `img/kit-combo.webp` | Same trio, sized for the offer box |
| `img/kit-with-pages.webp` | Tablet over scattered sample pages |
| `img/bonus-1.webp` / `bonus-2.webp` | The two bonus covers |
| `img/sample-1…5.webp` | Sample pages from the material |
| `img/persona-student/graduate/professional.webp` | "Is this for you?" photos (UK settings) |
| `img/textbook-dense.webp` | The dense-textbook comparison shot |
| `img/author.webp` | Author portrait |

## Colour palette
| Token | Hex |
|---|---|
| Primary blue / hero | `#2645a0` |
| Deep blue | `#1c3479` / `#1b3277` |
| Accent yellow | `#f7cf49` |
| CTA orange | `#f97216` |
| Background | `#FFFFFF` / `#f4f7fd` |

The canonical URL of the site is **https://www.medicalstudylab.com** (no www).

## Before going live
- The checkout is `checkout.medicalstudylab.com/checkout/kit-complete` and must charge in
  **GBP**; the page, the schema markup and the analytics events all declare `GBP`.
- The Meta Pixel domain allow-list must include the live domain or the pixel will not fire.

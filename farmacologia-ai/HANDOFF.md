# Handoff — Farmacologia Illustrata (páginas generadas con Gemini)

Copiá TODO lo que está entre las líneas de guiones y pegalo en la sesión nueva,
adjuntando: el PDF original, el avatar, y las imágenes ya hechas (p01–p05).

---------------------------------------------------------------------------

Vamos a rehacer entero el libro **"Farmacologia Illustrata"** (82 páginas, en italiano).
Te adjunto:
1. El PDF original: `C:\Users\lucag\Desktop\CLAUDE\Infoproductos\Farmacologia\Ebooks Italiano\Farmacologia Illustrata.pdf`
2. El avatar del personaje: `C:\Users\lucag\Downloads\ChatGPT Image 29 ago 2026, 04_38_46 p.m..png`
3. Las 5 primeras páginas ya hechas, como referencia de estilo: `C:\Users\lucag\.gemini\antigravity-ide\scratch\medstudylab\farmacologia-ai\p01.jpg` … `p05.jpg`

## Qué quiero
Cada página del libro es **una sola imagen generada con Gemini** (nada de maquetar en
HTML: cero HTML para las páginas). Después todas las imágenes van a un visor HTML con
botón de descarga en PDF.

## Contenido
La **estructura y la información de cada página tienen que ser las mismas del PDF
original**: página 7 del libro nuevo = página 7 del PDF, con los mismos conceptos y
ejemplos. El texto original está mal escrito en varias partes (es una traducción
automática del portugués): reescribilo en **italiano correcto**, sin cambiar el
significado ni inventar contenido. Si encontrás un error de farmacología de fondo,
corregilo y avisame.

## Cómo generar las imágenes (esto ya está probado y funciona)
- **API directa de Gemini**, NO el CLI: `nano-banana.exe` no se puede lanzar desde
  `subprocess` de Python en esta máquina (WinError 216). Usar `urllib` contra:
  `https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent?key=API_KEY`
- La API key está en `C:\Users\lucag\.nano-banana\.env` (`GEMINI_API_KEY=`).
  Es una key nueva formato `AQ.…`; la vieja `AIzaSy…` está bloqueada por deuda de
  facturación en el proyecto 438183059357 — no la uses.
- Config del request:
  ```json
  {"contents":[{"parts":[{"text":"PROMPT"}]}],
   "generationConfig":{"imageConfig":{"aspectRatio":"3:4","imageSize":"2K"}}}
  ```
  Devuelve un JPEG de 1792×2400 en `candidates[0].content.parts[*].inlineData.data` (base64).
- El script que ya hace todo esto está en
  `C:\Users\lucag\.gemini\antigravity-ide\scratch\medstudylab\farmacologia-ai\gen.py`
  (tiene un diccionario `PAGES = {numero: (slug, prompt)}` y se corre con
  `python gen.py 6 7 8`). Seguí agregando páginas a ese diccionario.

### Reglas aprendidas — importantes
- **NO pasar imagen de referencia** (`-r` / reference image). Con referencia el modelo
  pierde los apóstrofos y los acentos italianos ("dell uso" en vez de "dell'uso"). Sin
  referencia el texto sale perfecto.
- Pedir explícitamente **"NO watermark, no logo"**: si no, mete una marca de agua.
- Escribir en el prompt **el texto italiano exacto entre comillas**, y cerrar con:
  "Reproduce every Italian text EXACTLY as written, with correct accents and
  apostrophes, perfect spelling, no invented words."
- Nada de textos larguísimos en una sola página: si la página tiene mucho contenido,
  repartirlo en tarjetas cortas, si no el modelo empieza a inventar palabras.
- **Revisar cada imagen generada mirándola** y regenerar la que tenga texto mal. No
  entregar sin mirar.

### Bloque de estilo (usar el mismo en todas las páginas)
```
Educational infographic page from an Italian pharmacology study book, vertical A4 page,
clean white background, NO watermark, no logo, no page border. Soft pastel palette of
lavender purple, mint green, sky blue and soft peach; rounded pill-shaped cards; cute
flat vector illustrations with thin dark outlines inside white circles; bold black
uppercase headings in a geometric sans-serif, with one word in purple. Small floating
pastel capsules, tablets and molecules as decoration. Modern, clean, generous spacing,
nothing cropped at the edges. Reproduce every Italian text EXACTLY as written, with
correct accents and apostrophes, perfect spelling, no invented words.
```

### Personaje (describirlo con palabras, no con imagen de referencia)
```
A friendly 3D cartoon young man with dark brown wavy hair, warm skin, big brown eyes,
a wide smile and a white polo shirt, cut out with no frame
```
El personaje **no aparece en todas las páginas**: va rotando como en el PDF original —
a veces el chico, a veces una mascota cápsula (cápsula lavanda y blanca con ojos grandes,
bracitos y piernitas), a veces solo producto/ilustración. Variar página a página.

## Estado actual
- Hechas: páginas **1 a 5** (portada, aviso legal, sommario, divisor "Parte I —
  Fondamenti", conceptos de base). Están en `farmacologia-ai/`.
- Falta: **de la 6 a la 82**.
- Contenido de las siguientes: pág. 6 efecto placebo y nocebo · 7 farmaco vs medicinale,
  potenza ed efficacia · 8 forme solide · 9 forme liquide · 10 forme semisolide y parche
  transdérmico · 11 nomenclatura · 12 clasificación · 13 approcci terapeutici ·
  14-19 vías de administración · 20 la strada del farmaco · 21-28 farmacocinética.

## Visor + PDF
Ya existe un visor en
`C:\Users\lucag\.gemini\antigravity-ide\scratch\medstudylab\farmacologia-illustrata.html`
(grid de páginas, lightbox, botón "Scarica PDF" y "Stampa" en A4). Hay que apuntarlo a
las imágenes nuevas de `farmacologia-ai/` y regenerar el PDF con PyMuPDF (una imagen por
página A4). **No tocar `index.html`**, que es la landing de MedStudyLab.

## Cosas que NO quiero
- Ni marca de agua, ni logo.
- Nada de maquetar las páginas en HTML/CSS: todo generado como imagen.
- No inventar contenido que no esté en el PDF.

---------------------------------------------------------------------------

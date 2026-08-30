# -*- coding: utf-8 -*-
"""Generate all UK/English landing page assets for MedStudyLab.
Covers, Mockups, Sample Pages (Amostras), and Mind Maps.
"""
import os, io, asyncio, math, shutil
from PIL import Image

STUDIO = r"c:\Users\lucag\Desktop\studiofacile"
MED = r"C:\Users\lucag\.gemini\antigravity-ide\scratch\medstudylab"
TOOLS = os.path.join(MED, "tools")
OUT_IMG = os.path.join(MED, "img")
OUT_AMOSTRAS = os.path.join(MED, "amostras")
OUT_MOCKUPS = os.path.join(MED, "mockups")

for d in (TOOLS, OUT_IMG, OUT_AMOSTRAS, OUT_MOCKUPS):
    os.makedirs(d, exist_ok=True)

# Copy art and fonts from studiofacile
ART_SRC = os.path.join(STUDIO, "build-covers", "art")
FONTS_SRC = os.path.join(STUDIO, "build-covers", "fonts")
CUT_SRC = os.path.join(STUDIO, "build-covers", "cut")

ART_DST = os.path.join(TOOLS, "art")
FONTS_DST = os.path.join(TOOLS, "fonts")
CUT_DST = os.path.join(TOOLS, "cut")

for src, dst in [(ART_SRC, ART_DST), (FONTS_SRC, FONTS_DST), (CUT_SRC, CUT_DST)]:
    if os.path.exists(src):
        os.makedirs(dst, exist_ok=True)
        for f in os.listdir(src):
            shutil.copy(os.path.join(src, f), os.path.join(dst, f))

# -------------------------------------------------------------
# CSS FOR COVERS
# -------------------------------------------------------------
COVER_CSS = """
@font-face{font-family:'Poppins';src:url('fonts/Poppins-Regular.ttf');font-weight:400}
@font-face{font-family:'Poppins';src:url('fonts/Poppins-Medium.ttf');font-weight:500}
@font-face{font-family:'Poppins';src:url('fonts/Poppins-SemiBold.ttf');font-weight:600}
@font-face{font-family:'Poppins';src:url('fonts/Poppins-Bold.ttf');font-weight:700}
@font-face{font-family:'Poppins';src:url('fonts/Poppins-ExtraBold.ttf');font-weight:800}

:root{
  --ink:#1c1d2e;
  --teal:#2f897d;
  --lav:#dbc0eb;  --lav-s:#f0e6fa;  --lav2:#c9a8ea;
  --mint:#b6e6d0; --mint-s:#e4f5ec;
  --sky:#b9def8;  --sky-s:#e6f1fc;
  --peach:#fec7a9;--peach-s:#fde9dd;
  --rose:#fbd2da; --rose-s:#fdeaee;
  --gold:#ffd166;
}

*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#c9ccd8}

.page{
  position:relative;width:794px;height:1123px;overflow:hidden;
  font-family:'Poppins',sans-serif;color:#fff;
}
.page.main{background:linear-gradient(158deg,#1e3a8a 0%,#2563eb 45%,#38bdf8 100%)}
.page.b1{background:linear-gradient(158deg,#4b1f86 0%,#6b2fae 42%,#9a52d8 100%)}
.page.b2{background:linear-gradient(158deg,#b81f70 0%,#e5533c 52%,#f89a3c 100%)}

.grid{position:absolute;inset:0;z-index:0;opacity:.16;
  background-image:radial-gradient(rgba(255,255,255,.9) 1.6px, transparent 1.6px);
  background-size:34px 34px}
.halo{position:absolute;left:50%;top:640px;transform:translate(-50%,-50%);
  width:840px;height:840px;border-radius:50%;z-index:1;
  background:radial-gradient(closest-side,rgba(255,255,255,.22),rgba(255,255,255,0) 72%)}

.blob{position:absolute;z-index:1;border-radius:50%;opacity:.16;background:#fff}
.deco{position:absolute;z-index:2;filter:drop-shadow(0 8px 16px rgba(0,0,0,.22))}

.cover{position:absolute;inset:0;z-index:4;display:flex;flex-direction:column;
  align-items:center;text-align:center;padding:56px 52px 0}
.brandmark{display:flex;align-items:center;gap:9px;font-size:11px;font-weight:700;
  letter-spacing:5px;text-transform:uppercase;color:rgba(255,255,255,.84)}
.brandmark b{width:7px;height:7px;border-radius:50%;background:var(--gold)}
.badge{margin-top:15px;padding:8px 24px;border-radius:999px;background:var(--gold);
  font-size:12.5px;font-weight:800;letter-spacing:2.6px;text-transform:uppercase;
  color:#4a2a08;box-shadow:0 8px 18px rgba(0,0,0,.20)}
.cover h1{margin-top:20px;font-size:48px;font-weight:800;line-height:1.04;
  color:#fff;letter-spacing:-1px;text-shadow:0 6px 18px rgba(0,0,0,.22)}
.cover h1 span{display:inline-block;margin-top:12px;padding:6px 26px 10px;
  border-radius:24px;background:#fff;font-size:56px;letter-spacing:-1.6px;
  box-shadow:0 14px 30px rgba(0,0,0,.22);text-shadow:none}
.page.main .cover h1 span{color:#1e3a8a}
.page.b1 .cover h1 span{color:#5b2b8f}
.page.b2 .cover h1 span{color:#c62b74}
.cover .sub{margin-top:20px;font-size:17px;font-weight:600;color:rgba(255,255,255,.95);
  max-width:620px;text-shadow:0 3px 10px rgba(0,0,0,.20)}

.chips{position:absolute;left:0;right:0;bottom:42px;display:flex;flex-wrap:wrap;
  justify-content:center;gap:9px;padding:0 38px;z-index:5}
.chip{padding:9px 20px;border-radius:999px;font-size:13px;font-weight:800;
  background:rgba(255,255,255,.95);color:#2a1733;box-shadow:0 6px 16px rgba(0,0,0,.16)}
.chip.m{background:var(--mint)} .chip.s{background:var(--sky)}
.chip.p{background:var(--peach)} .chip.g{background:var(--gold)}

/* Ring Bonus 1 */
.ring{position:relative;width:600px;height:600px;margin-top:30px;z-index:4}
.ring .dots{position:absolute;inset:44px;border-radius:50%;
  border:3px dotted rgba(255,255,255,.60)}
.ring .core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  width:262px;height:262px;border-radius:50%;background:#fff;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  box-shadow:0 20px 44px rgba(0,0,0,.28)}
.ring .core .az{font-size:72px;font-weight:800;letter-spacing:-2px;color:#5b2b8f;line-height:1}
.ring .core .az i{font-style:normal;color:var(--teal)}
.ring .core .lb{margin-top:6px;font-size:13px;font-weight:800;letter-spacing:2.6px;
  text-transform:uppercase;color:#9470a4}
.node{position:absolute;width:124px;height:124px;border-radius:50%;background:#fff;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 12px 26px rgba(0,0,0,.26)}
.node img{width:88px;height:88px;object-fit:contain}
.node.letter{font-size:46px;font-weight:800;color:#5b2b8f}
.node.t1{background:var(--mint)} .node.t2{background:var(--peach)}
.node.t3{background:var(--sky)}  .node.t4{background:var(--gold)}

/* Ring Bonus 2 */
.ring5{position:relative;width:620px;height:620px;margin-top:34px;z-index:4}
.ring5 .band{position:absolute;inset:40px;border-radius:50%;
  border:3px solid rgba(255,255,255,.55)}
.ring5 .core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  width:274px;height:274px;border-radius:50%;background:#fff;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  box-shadow:0 22px 48px rgba(0,0,0,.30)}
.ring5 .core .big{font-size:118px;font-weight:800;line-height:.86;color:#e0452f;
  letter-spacing:-4px}
.ring5 .core .k1{margin-top:4px;font-size:24px;font-weight:800;letter-spacing:1px;
  text-transform:uppercase;color:#c62b74}
.ring5 .core .k2{margin-top:2px;font-size:12.5px;font-weight:800;letter-spacing:2.8px;
  text-transform:uppercase;color:#8c7f95}
.nd{position:absolute;width:132px;display:flex;flex-direction:column;align-items:center}
.nd .circ{width:132px;height:132px;border-radius:50%;background:#fff;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 14px 28px rgba(0,0,0,.26)}
.nd .circ img{width:92px;height:92px;object-fit:contain}
.nd .lb{margin-top:9px;padding:5px 12px;border-radius:999px;background:#fff;
  font-size:11.5px;font-weight:800;color:#2a1733;white-space:nowrap;
  box-shadow:0 6px 14px rgba(0,0,0,.20)}
.nd.t1 .circ{background:var(--sky)}   .nd.t2 .circ{background:var(--lav)}
.nd.t3 .circ{background:var(--mint)}  .nd.t4 .circ{background:var(--rose)}
.nd.t5 .circ{background:var(--gold)}

/* Main Cover elements */
.avatar-big{width:210px;height:210px;border-radius:50%;background:#fff;margin:24px auto 0;
  display:flex;align-items:center;justify-content:center;overflow:hidden;
  box-shadow:0 18px 40px rgba(0,0,0,.28);border:6px solid #fff}
.avatar-big img{width:100%;height:100%;object-fit:cover;object-position:center 10%}
.pile-img{width:460px;margin:20px auto 0;filter:drop-shadow(0 14px 28px rgba(0,0,0,.25))}
"""

def ring_nodes():
    items = [("i", "art/icon-book.png", "t1"), ("t", "A", "t4"),
             ("i", "art/icon-clipboard.png", "t2"), ("t", "Z", "t3"),
             ("i", "art/icon-magnifier.png", "t2"), ("i", "art/icon-molecule.png", "t1")]
    out = []
    cx = cy = 300.0
    r = 238.0
    for k, (kind, val, tone) in enumerate(items):
        ang = math.radians(-90 + k * 60)
        x = cx + r * math.cos(ang) - 62
        y = cy + r * math.sin(ang) - 62
        if kind == "i":
            out.append(f'<div class="node {tone}" style="left:{x:.0f}px;top:{y:.0f}px"><img src="{val}" alt=""></div>')
        else:
            out.append(f'<div class="node letter {tone}" style="left:{x:.0f}px;top:{y:.0f}px">{val}</div>')
    return "".join(out)

CLASSI = [("art/icon-bloodflow.png", "Antihypertensives", "t1"),
          ("art/icon-headache.png", "NSAIDs", "t2"),
          ("art/icon-microscope.png", "Antibiotics", "t3"),
          ("art/icon-brain.png", "Benzodiazepines", "t4"),
          ("art/icon-capsule.png", "Opioids", "t5")]

def ring5():
    out = []
    cx = cy = 310.0
    r = 244.0
    for k, (img, nm, tone) in enumerate(CLASSI):
        ang = math.radians(-90 + k * 72)
        x = cx + r * math.cos(ang) - 66
        y = cy + r * math.sin(ang) - 78
        out.append(f'<div class="nd {tone}" style="left:{x:.0f}px;top:{y:.0f}px">'
                   f'<div class="circ"><img src="{img}" alt=""></div>'
                   f'<div class="lb">{nm}</div></div>')
    return "".join(out)

HTML_BONUS1 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{COVER_CSS}</style></head><body>
<div class="page b1"><div class="grid"></div><div class="halo"></div>
<div class="blob" style="width:236px;height:236px;left:-56px;top:424px"></div>
<div class="blob" style="width:262px;height:262px;right:-70px;top:648px"></div>
<div class="blob" style="width:168px;height:168px;left:-18px;top:900px"></div>
<img class="deco" src="art/icon-capsule.png" style="width:74px;left:52px;top:398px;transform:rotate(-20deg)">
<img class="deco" src="art/icon-tablet.png"  style="width:64px;right:56px;top:430px;transform:rotate(14deg)">
<img class="deco" src="art/icon-molecule.png" style="width:88px;left:22px;top:668px;opacity:.75">
<img class="deco" src="art/icon-molecule.png" style="width:76px;right:26px;top:912px;opacity:.6;transform:scaleX(-1)">
<img class="deco" src="art/icon-capsule.png" style="width:62px;left:96px;top:942px;transform:rotate(28deg)">
<div class="cover">
  <div class="brandmark"><b></b>MedStudyLab<b></b></div>
  <div class="badge">Bonus 01</div>
  <h1>Key Terms in<span>Clinical Pharmacy</span></h1>
  <div class="sub">The A to Z glossary of clinical practice</div>
  <div class="ring">
    <div class="dots"></div>
    {ring_nodes()}
    <div class="core">
      <div class="az">A<i>&ndash;</i>Z</div>
      <div class="lb">Glossary</div>
    </div>
  </div>
  <div class="chips">
    <span class="chip g">Concise definitions</span>
    <span class="chip m">Clinical examples</span>
    <span class="chip s">Alphabetical order</span>
    <span class="chip p">Quick reference</span>
  </div>
</div></div></body></html>"""

HTML_BONUS2 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{COVER_CSS}</style></head><body>
<div class="page b2"><div class="grid"></div><div class="halo"></div>
<div class="blob" style="width:270px;height:270px;left:-96px;top:392px"></div>
<div class="blob" style="width:236px;height:236px;right:-78px;top:452px"></div>
<div class="blob" style="width:190px;height:190px;left:-58px;top:822px"></div>
<img class="deco" src="art/icon-molecule.png" style="width:88px;left:28px;top:346px;opacity:.7">
<img class="deco" src="art/icon-molecule.png" style="width:76px;right:26px;top:380px;opacity:.6;transform:scaleX(-1)">
<img class="deco" src="art/icon-tablet.png" style="width:58px;left:78px;top:962px;transform:rotate(-12deg)">
<img class="deco" src="art/icon-capsule.png" style="width:64px;right:76px;top:952px;transform:rotate(22deg)">
<div class="cover">
  <div class="brandmark"><b></b>MedStudyLab<b></b></div>
  <div class="badge">Bonus 02</div>
  <h1>Rapid Revision<span>Sheets</span></h1>
  <div class="sub">The 5 most tested drug classes in exams</div>
  <div class="ring5">
    <div class="band"></div>
    {ring5()}
    <div class="core">
      <div class="big">5</div>
      <div class="k1">Essential</div>
      <div class="k2">Classes</div>
    </div>
  </div>
  <div class="chips">
    <span class="chip g">Mechanism of action</span>
    <span class="chip m">Adverse effects</span>
    <span class="chip s">Interactions</span>
    <span class="chip p">Print-ready</span>
  </div>
</div></div></body></html>"""

HTML_MAIN = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{COVER_CSS}</style></head><body>
<div class="page main"><div class="grid"></div><div class="halo"></div>
<div class="blob" style="width:250px;height:250px;left:-70px;top:300px"></div>
<div class="blob" style="width:190px;height:190px;right:-50px;top:560px"></div>
<img class="deco" src="art/icon-molecule.png" style="width:120px;left:44px;top:392px;opacity:.85">
<img class="deco" src="art/icon-molecule.png" style="width:96px;right:56px;top:300px;opacity:.7;transform:scaleX(-1)">
<img class="deco" src="art/icon-capsule.png" style="width:80px;left:150px;top:280px;transform:rotate(-18deg)">
<img class="deco" src="art/icon-tablet.png"  style="width:70px;right:150px;top:610px;transform:rotate(12deg)">
<div class="cover">
  <div class="brandmark"><b></b>MedStudyLab<b></b></div>
  <div class="badge">Complete Guide</div>
  <h1>Illustrated<span>Pharmacology</span></h1>
  <div class="sub">Visual learning, straight to the point</div>
  <div class="avatar-big"><img src="art/avatar.png" alt=""></div>
  <img class="pile-img" src="art/cover-pile.png" alt="">
  <div class="chips">
    <span class="chip g">Fundamentals</span>
    <span class="chip m">Pharmacokinetics</span>
    <span class="chip s">Pharmacodynamics</span>
    <span class="chip p">Interactions</span>
  </div>
</div></div></body></html>"""

# -------------------------------------------------------------
# CSS FOR SAMPLE PAGES (AMOSTRAS)
# -------------------------------------------------------------
PAGE_CSS = """
@font-face{font-family:'Poppins';src:url('fonts/Poppins-Regular.ttf');font-weight:400}
@font-face{font-family:'Poppins';src:url('fonts/Poppins-Medium.ttf');font-weight:500}
@font-face{font-family:'Poppins';src:url('fonts/Poppins-SemiBold.ttf');font-weight:600}
@font-face{font-family:'Poppins';src:url('fonts/Poppins-Bold.ttf');font-weight:700}
@font-face{font-family:'Poppins';src:url('fonts/Poppins-ExtraBold.ttf');font-weight:800}

:root{
  --paper:#f8f6f1;--plum:#562a5f;--teal:#2f897d;--ink:#2a2b3d;--soft:#585755;
  --lav:#f0e6fa;--lav2:#c9a8ea;--mint:#e4f5ec;--mint2:#8fd3b8;--eb:#9470a4;--sky:#e4eefb;--sky2:#9dc2ee;--blu:#24499b;
  --rose:#fdeaee;--rose2:#f598a8;--peach:#fde9dd;--peach2:#fca776;--gold:#fdf3c4;--gold2:#f5a623;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#c9ccd8}
.page{position:relative;width:794px;height:1123px;overflow:hidden;background:var(--paper);
  font-family:'Poppins',sans-serif;color:var(--ink);padding:34px 40px 30px}
.deco{position:absolute;z-index:1;opacity:.85}
.eyebrow{display:flex;align-items:center;gap:9px;font-size:10.5px;font-weight:800;
  letter-spacing:2.8px;text-transform:uppercase;color:var(--eb)}
.eyebrow b{width:16px;height:3px;border-radius:2px;background:var(--lav2)}
h1{margin-top:6px;font-size:46px;font-weight:800;letter-spacing:-1px;line-height:1.05;color:var(--plum)}
h1 i{font-style:normal;color:var(--lav2)}
h1 em{font-style:normal;color:var(--teal)}

.box{position:relative;z-index:2;margin-top:14px;border-radius:24px;padding:18px 22px;background:#fff;
  box-shadow:0 8px 22px rgba(28,29,46,.08)}
.box.sky{background:var(--sky)} .box.mint{background:var(--mint)} .box.lav{background:var(--lav)}
.box.rose{background:var(--rose)} .box.peach{background:var(--peach)}

.box h2{font-size:22px;font-weight:800;letter-spacing:-.3px;margin-bottom:8px}
.box.sky h2{color:var(--blu)} .box.mint h2{color:var(--teal)} .box.lav h2{color:var(--plum)}
.box.rose h2{color:#c62b74} .box.peach h2{color:#d9531e}

p{font-size:14px;line-height:1.52;font-weight:500;color:var(--ink)}
ul{margin-top:8px;padding-left:18px;font-size:13.5px;line-height:1.5}
li{margin-bottom:5px}

.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:12px}
.col{background:#fff;border-radius:18px;padding:14px 16px;box-shadow:0 6px 14px rgba(28,29,46,.06)}
.col h3{font-size:15.5px;font-weight:800;margin-bottom:6px}

.tag{display:inline-block;padding:4px 14px;border-radius:999px;background:#fff;font-size:12px;
  font-weight:800;color:var(--ink);box-shadow:0 4px 10px rgba(28,29,46,.08);margin-bottom:8px}

.rule{display:flex;align-items:center;justify-content:center;gap:14px;margin-top:6px;
  font-size:14px;font-weight:600;color:var(--soft)}
.rule s{flex:0 0 92px;height:2px;background:rgba(0,0,0,.14);border-radius:2px}
.q{margin:12px auto 0;max-width:560px;background:#fff;border-radius:999px;padding:10px 24px;
  font-size:16.5px;font-weight:800;color:var(--ink);text-align:center}
.scene{position:relative;display:flex;align-items:center;justify-content:center;margin-top:10px}
.fig{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;width:240px}
.disc{width:180px;height:180px;border-radius:50%;background:#fff;display:flex;
  align-items:center;justify-content:center;overflow:hidden;box-shadow:0 10px 22px rgba(28,29,46,.12)}
.disc img{max-width:150px;max-height:150px;object-fit:contain}
.disc.av img{max-width:none;max-height:none;width:100%;height:100%;object-fit:cover;object-position:50% 10%}
.arrow{position:absolute;z-index:3;left:50%;top:70px;transform:translateX(-50%);
  display:flex;flex-direction:column;align-items:center}
.arrow span{font-size:14px;font-weight:800;color:var(--blu);margin-bottom:4px}
.box.mint .arrow span{color:var(--teal)}
.arrow svg{width:160px;height:24px}
.foot{margin:14px auto 0;max-width:640px;background:#fff;border-radius:999px;padding:10px 22px;
  font-size:14.5px;font-weight:800;color:var(--ink);text-align:center}
.box.sky .foot{box-shadow:inset 0 0 0 2px var(--sky2)}
.box.mint .foot{box-shadow:inset 0 0 0 2px var(--mint2)}
"""

def arrow_svg(color):
    return (f'<svg viewBox="0 0 120 24" fill="none"><path d="M2 12h96" stroke="{color}" '
            f'stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M92 3l22 9-22 9z" fill="{color}"/></svg>')

# 1. Cinetica vs Dinamica
HTML_CINETICA = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{PAGE_CSS}</style></head><body><div class="page">
<img class="deco" src="art/icon-capsule.png" style="width:56px;left:-6px;top:250px;transform:rotate(-24deg)">
<img class="deco" src="art/icon-tablet.png" style="width:48px;right:2px;top:300px;transform:rotate(16deg)">
<img class="deco" src="art/icon-molecule.png" style="width:70px;right:-6px;top:150px;opacity:.7">
<img class="deco" src="art/icon-molecule.png" style="width:62px;left:-10px;top:604px;opacity:.65">

<div class="eyebrow"><b></b>Chapter 8 &middot; Pharmacokinetics vs Pharmacodynamics</div>
<h1>Kinetics <i>vs</i> <em>Dynamics</em></h1>

<div class="box sky">
  <h2 style="text-align:center">PHARMACOKINETICS</h2>
  <div class="rule"><s></s>drug + movement<s></s></div>
  <div class="q">What the body does to the drug.</div>
  <div class="scene">
    <div class="fig"><div class="disc av"><img src="cut/av-point.png" alt=""></div>
      <div class="tag">body</div></div>
    <div class="fig"><div class="disc"><img src="cut/capsule-scared.png" alt=""></div>
      <div class="tag">drug</div></div>
    <div class="arrow"><span>Action</span>{arrow_svg('#24499b')}</div>
  </div>
  <div class="foot">Absorption + Distribution + Metabolism + Excretion (ADME)</div>
</div>

<div class="box mint" style="margin-top:16px">
  <h2 style="text-align:center">PHARMACODYNAMICS</h2>
  <div class="rule"><s></s>drug + effect<s></s></div>
  <div class="q">What the drug does to the body.</div>
  <div class="scene">
    <div class="fig"><div class="disc"><img src="cut/capsule-strong.png" alt=""></div>
      <div class="tag">drug</div></div>
    <div class="fig"><div class="disc av"><img src="cut/av-wave.png" alt=""></div>
      <div class="tag">body responding</div></div>
    <div class="arrow"><span>Action</span>{arrow_svg('#2f897d')}</div>
  </div>
  <div class="foot">Therapeutic effects, pharmacological effects and adverse reactions</div>
</div>
</div></body></html>"""

# 2. Pagina 21: Pharmacokinetics ADME & Absorption
HTML_PAG21 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{PAGE_CSS}</style></head><body><div class="page">
<img class="deco" src="art/icon-capsule.png" style="width:52px;right:20px;top:40px;opacity:.7">
<div class="eyebrow"><b></b>Chapter 6 &middot; Pharmacokinetics</div>
<h1>Pharmacokinetics</h1>
<div style="font-size:14px;font-weight:600;color:var(--soft);margin-top:2px">&mdash; drug + movement</div>

<div class="box sky" style="margin-top:14px">
  <p><strong>The branch of pharmacology that studies the journey and fate of the drug in the body.</strong> In short: what the organism does to the drug over time.</p>
</div>

<div class="box lav" style="margin-top:14px">
  <span class="tag">THE FOUR STAGES: ADME</span>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:8px;text-align:center">
    <div class="col"><img src="art/icon-taking.png" style="width:54px;margin:0 auto 4px"><strong>1. Absorption</strong></div>
    <div class="col"><img src="art/icon-bloodflow.png" style="width:54px;margin:0 auto 4px"><strong>2. Distribution</strong></div>
    <div class="col"><img src="art/icon-liver.png" style="width:54px;margin:0 auto 4px"><strong>3. Metabolism</strong><br><small>(biotransformation)</small></div>
    <div class="col"><img src="art/icon-medbox.png" style="width:54px;margin:0 auto 4px"><strong>4. Excretion</strong></div>
  </div>
</div>

<div class="box mint" style="margin-top:14px">
  <span class="tag">ABSORPTION</span>
  <p><strong>The passage of the drug from its site of administration into the bloodstream</strong>, reaching the systemic circulation.</p>
  <div style="display:flex;align-items:center;justify-content:space-around;margin-top:12px;text-align:center">
    <div><img src="art/icon-tablet.png" style="width:50px;margin:0 auto"><div>Administration</div></div>
    <div style="font-size:24px;color:var(--teal)">&rarr;</div>
    <div><img src="art/icon-stomach.png" style="width:50px;margin:0 auto"><div>Absorption</div></div>
    <div style="font-size:24px;color:var(--teal)">&rarr;</div>
    <div><img src="art/icon-bloodflow.png" style="width:50px;margin:0 auto"><div>Systemic Circulation</div></div>
  </div>
</div>

<div class="box peach" style="margin-top:14px">
  <span class="tag">WHAT DOES IT DEPEND ON?</span>
  <ul>
    <li><strong>Route of administration:</strong> Intravenous (IV) route bypasses absorption (100% immediate).</li>
    <li><strong>Drug properties:</strong> Lipid solubility, molecular size, and ionization state.</li>
    <li><strong>Site conditions:</strong> Local pH, blood perfusion, and available surface area.</li>
  </ul>
</div>

<div class="box lav" style="margin-top:14px">
  <span class="tag">BIOAVAILABILITY (F)</span>
  <p>The percentage fraction of an administered dose that reaches systemic circulation intact and is available to produce clinical effects.</p>
</div>
</div></body></html>"""

# 3. Pagina 35: Types of Ligands
HTML_PAG35 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{PAGE_CSS}</style></head><body><div class="page">
<img class="deco" src="art/icon-molecule.png" style="width:68px;right:20px;top:40px;opacity:.7">
<div class="eyebrow"><b></b>Chapter 7 &middot; Pharmacodynamics</div>
<h1>Types of Ligands</h1>

<div class="box lav" style="margin-top:14px">
  <div style="display:flex;justify-content:space-around;text-align:center;align-items:center">
    <div class="col" style="flex:1;margin:0 6px">
      <span class="tag" style="background:var(--lav)">Agonist</span>
      <p style="font-size:13px;margin-top:4px">Binds to receptor &rarr; <strong>Activates response</strong></p>
    </div>
    <div class="col" style="flex:1;margin:0 6px">
      <span class="tag" style="background:var(--rose)">Antagonist</span>
      <p style="font-size:13px;margin-top:4px">Binds to receptor &rarr; <strong>Blocks activation</strong></p>
    </div>
  </div>
</div>

<div class="box mint" style="margin-top:16px">
  <h2 style="color:var(--teal)">AGONISTS</h2>
  <p><strong>Substances that bind to a receptor and trigger a biological response</strong>, mimicking endogenous physiological ligands.</p>
  <ul>
    <li><strong>Full Agonist:</strong> Binds and produces the maximum possible response (100% intrinsic efficacy).</li>
    <li><strong>Partial Agonist:</strong> Produces a submaximal response even at 100% receptor occupancy.</li>
    <li><strong>Inverse Agonist:</strong> Binds to receptors with constitutive baseline activity and suppresses it below resting levels.</li>
  </ul>
</div>

<div class="box rose" style="margin-top:16px">
  <h2 style="color:#c62b74">ANTAGONISTS</h2>
  <p><strong>Substances that bind to receptors without triggering activation</strong>: their sole function is preventing agonists from binding.</p>
  <div class="grid2">
    <div class="col">
      <h3 style="color:#c62b74">Competitive</h3>
      <p>Competes directly for the primary agonist binding site. It is reversible: increasing agonist concentration overcomes the block.</p>
    </div>
    <div class="col">
      <h3 style="color:#c62b74">Non-Competitive</h3>
      <p>Binds to an allosteric site or forms an irreversible covalent bond. Changes receptor shape; cannot be overcome by higher agonist doses.</p>
    </div>
  </div>
</div>
</div></body></html>"""

# 4. Pagina 37: Receptors
HTML_PAG37 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{PAGE_CSS}</style></head><body><div class="page">
<img class="deco" src="art/icon-microscope.png" style="width:68px;right:20px;top:40px;opacity:.7">
<div class="eyebrow"><b></b>Chapter 7 &middot; Pharmacodynamics</div>
<h1>Enzymatic &amp; Intracellular Receptors</h1>

<div class="box peach" style="margin-top:14px">
  <span class="tag">ENZYME-LINKED RECEPTORS</span>
  <p><strong>Transmembrane receptors possessing intrinsic intracellular enzymatic activity.</strong></p>
  <ul>
    <li>The most prominent class is the <strong>receptor tyrosine kinases (RTKs)</strong>.</li>
    <li>Ligand binding activates the intracellular catalytic domain, causing <strong>autophosphorylation of tyrosine residues</strong> and initiating downstream kinase cascades.</li>
  </ul>
  <div class="grid2" style="margin-top:10px">
    <div class="col">
      <strong>1. Activation:</strong> Ligand (e.g. Insulin) binds to extracellular alpha subunit.
    </div>
    <div class="col">
      <strong>2. Autophosphorylation:</strong> Beta subunits cross-phosphorylate tyrosine residues.
    </div>
    <div class="col">
      <strong>3. Substrate recruitment:</strong> Phosphorylates IRS (Insulin Receptor Substrate).
    </div>
    <div class="col">
      <strong>4. Signalling cascade:</strong> Activates MAP-kinase and PI3K pathways for metabolic effects.
    </div>
  </div>
</div>

<div class="box sky" style="margin-top:16px">
  <span class="tag">INTRACELLULAR RECEPTORS</span>
  <p><strong>Located entirely inside the cell (in cytoplasm or nucleus).</strong></p>
  <ul>
    <li>The drug must be <strong>highly lipophilic</strong> to cross the lipid bilayer plasma membrane.</li>
    <li>Directly regulate <strong>gene transcription</strong> from genomic DNA into mRNA.</li>
    <li><strong>Key examples:</strong> Corticosteroids, thyroid hormones, and sex steroids (estrogen, testosterone).</li>
  </ul>
</div>
</div></body></html>"""

# 5. Pagina 39: Beta-Blockers & Dose-Response
HTML_PAG39 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{PAGE_CSS}</style></head><body><div class="page">
<img class="deco" src="art/icon-bloodflow.png" style="width:64px;right:20px;top:40px;opacity:.7">
<div class="eyebrow"><b></b>Chapter 7 &middot; Pharmacodynamics</div>
<h1>Classic Example: Beta-Blockers</h1>

<div class="box mint" style="margin-top:14px">
  <span class="tag">SELECTIVITY IN CLINICAL PRACTICE</span>
  <p>To grasp selectivity clinically, look at the difference between <strong>heart (beta-1)</strong> and <strong>lungs (beta-2)</strong>.</p>
  <div class="grid2" style="margin-top:10px">
    <div class="col">
      <h3 style="color:var(--teal)">Non-Selective: Propranolol</h3>
      <p>Blocks both beta-1 (benefits the heart) and beta-2 (constricts bronchioles in lungs). <strong>Contraindicated in asthmatic patients.</strong></p>
    </div>
    <div class="col">
      <h3 style="color:var(--teal)">Cardioselective: Atenolol</h3>
      <p>Preferentially blocks cardiac beta-1 receptors while sparing pulmonary beta-2 receptors. Much safer for patients with respiratory conditions.</p>
    </div>
  </div>
  <div class="foot" style="margin-top:10px;font-size:13px">
    Selectivity enables treating cardiac arrhythmias without triggering bronchospasm.
  </div>
</div>

<div class="box lav" style="margin-top:16px">
  <span class="tag">DOSE-RESPONSE RELATIONSHIP</span>
  <p>Describes how altering drug concentration modifies the magnitude of the physiological response in the organism.</p>
  <div class="q" style="margin:10px auto;font-size:15px">"The dose makes the poison." &mdash; Paracelsus</div>
  <div class="col" style="margin-top:8px">
    <strong>Effective Dose 50 (ED50):</strong> The dose that produces the desired therapeutic effect in 50% of the population. A key metric of drug potency.
  </div>
</div>
</div></body></html>"""

# 6. Pagina 42: Toxicity & Therapeutic Window
HTML_PAG42 = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>{PAGE_CSS}</style></head><body><div class="page">
<img class="deco" src="art/icon-warning.png" style="width:64px;right:20px;top:40px;opacity:.75">
<div class="eyebrow"><b></b>Chapter 9 &middot; Toxicity &amp; Pharmacogenomics</div>
<h1>Toxicity &amp; Safety</h1>

<div class="box sky" style="margin-top:14px">
  <p><strong>Toxicity refers to the capacity of a substance to cause cellular injury and adverse pathological effects in the organism.</strong></p>
</div>

<div class="box lav" style="margin-top:14px">
  <span class="tag">THERAPEUTIC WINDOW (MARGIN OF SAFETY)</span>
  <p>A drug's safety profile depends on the span between effective and toxic concentrations.</p>
  <div class="grid2" style="margin-top:10px">
    <div class="col">
      <h3 style="color:var(--plum)">Wide Window (Safe)</h3>
      <p>Large margin between the therapeutic dose and the toxic threshold. Extremely difficult to overdose accidentally (e.g. Penicillin, Amoxicillin).</p>
    </div>
    <div class="col">
      <h3 style="color:#c62b74">Narrow Window (High Risk)</h3>
      <p>Effective dose is dangerously close to toxic concentration. Requires strict therapeutic drug monitoring (e.g. Warfarin, Digoxin, Lithium).</p>
    </div>
  </div>
</div>

<div class="box mint" style="margin-top:16px">
  <span class="tag">MECHANISMS OF TOXICITY</span>
  <div class="col">
    <strong>Dose-Dependent Toxicity:</strong> Most toxic reactions are directly related to quantity. High doses saturate hepatic metabolic enzymes and renal clearance mechanisms, causing accumulation and tissue injury.
  </div>
</div>
</div></body></html>"""

# -------------------------------------------------------------
# MOCKUPS GENERATOR HTML
# -------------------------------------------------------------
MOCKUP_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:transparent}
.stage{position:relative}
.tab{position:absolute;border-radius:38px;padding:13px;
  background:linear-gradient(150deg,#4a4d55 0%,#2c2e35 38%,#212329 100%);
  box-shadow:0 34px 64px rgba(15,23,42,.34), 0 8px 18px rgba(15,23,42,.20),
             inset 0 1px 0 rgba(255,255,255,.22), inset 0 -1px 0 rgba(0,0,0,.35);}
.tab .scr{width:100%;height:100%;border-radius:26px;overflow:hidden;background:#fff;
  box-shadow:inset 0 0 0 1px rgba(0,0,0,.35)}
.tab .scr img{width:100%;height:100%;object-fit:cover;display:block}
.tab .gl{position:absolute;inset:13px;border-radius:26px;pointer-events:none;
  background:linear-gradient(118deg,rgba(255,255,255,.30) 0%,rgba(255,255,255,.07) 26%,
             rgba(255,255,255,0) 46%)}
.sheet{position:absolute;border-radius:10px;overflow:hidden;background:#fff;
  box-shadow:0 16px 34px rgba(15,23,42,.20)}
.sheet img{width:100%;height:100%;object-fit:cover;display:block}
"""

def page_wrap(w, h, body):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{MOCKUP_CSS}
body{{width:{w}px;height:{h}px}}</style></head><body>
<div class="stage" style="width:{w}px;height:{h}px">{body}</div></body></html>"""

def tab_html(src, x, y, w, h, z=1, rot=0, scale=1.0):
    return (f'<div class="tab" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            f'z-index:{z};transform:rotate({rot}deg) scale({scale})">'
            f'<div class="scr"><img src="{src}" alt=""></div><div class="gl"></div></div>')

def trio_html(b1_src, b2_src, main_src):
    return (tab_html(b1_src, 36, 35, 460, 640, 1)
            + tab_html(b2_src, 704, 35, 460, 640, 1)
            + tab_html(main_src, 300, 35, 600, 838, 3))

def collage_html(main_src, sample_srcs):
    sheets = [(-60, -30, 470, -7), (330, -70, 470, 5), (660, -20, 470, 9),
              (-90, 480, 470, 4), (620, 500, 470, -6),
              (-40, 990, 470, -9), (350, 1030, 470, 3), (680, 980, 470, 7)]
    parts = []
    for i, (x, y, w, rot) in enumerate(sheets):
        src = sample_srcs[i % len(sample_srcs)]
        h = int(w * 1874 / 1405)
        parts.append(f'<div class="sheet" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
                     f'z-index:1;transform:rotate({rot}deg)"><img src="{src}" alt=""></div>')
    parts.append(tab_html(main_src, 270, 400, 560, 786, 6))
    return "".join(parts)


async def main():
    from playwright.async_api import async_playwright
    
    # Save all templates to TOOLS
    files = {
        "_cov_main.html": HTML_MAIN,
        "_cov_b1.html": HTML_BONUS1,
        "_cov_b2.html": HTML_BONUS2,
        "_am_cinetica.html": HTML_CINETICA,
        "_am_p21.html": HTML_PAG21,
        "_am_p35.html": HTML_PAG35,
        "_am_p37.html": HTML_PAG37,
        "_am_p39.html": HTML_PAG39,
        "_am_p42.html": HTML_PAG42,
    }
    
    for fn, html in files.items():
        with open(os.path.join(TOOLS, fn), "w", encoding="utf-8") as f:
            f.write(html)
            
    print("HTML templates written. Launching Playwright...")
    
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        
        # 1. Render Covers (794x1123 @3x)
        covers = [
            ("_cov_main.html", "cover-main.png"),
            ("_cov_b1.html", "cover-bonus-1.png"),
            ("_cov_b2.html", "cover-bonus-2.png"),
        ]
        for src_html, out_png in covers:
            pg = await b.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=3)
            await pg.goto("file:///" + os.path.join(TOOLS, src_html).replace("\\", "/"))
            await pg.wait_for_timeout(600)
            png = await pg.screenshot(clip={"x": 0, "y": 0, "width": 794, "height": 1123})
            im = Image.open(io.BytesIO(png)).convert("RGB")
            im.save(os.path.join(TOOLS, out_png))
            print(f"Rendered {out_png}: {im.size}")
            await pg.close()
            
        # 2. Render Sample Pages (794x1123 -> resized to 1405x1874)
        sample_pages = [
            ("_am_cinetica.html", "cinetica-x-dinamica.webp"),
            ("_am_p21.html", "pag-21.webp"),
            ("_am_p35.html", "pag-35.webp"),
            ("_am_p37.html", "pag-37.webp"),
            ("_am_p39.html", "pag-39.webp"),
            ("_am_p42.html", "pag-42.webp"),
        ]
        for src_html, out_webp in sample_pages:
            pg = await b.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=3)
            await pg.goto("file:///" + os.path.join(TOOLS, src_html).replace("\\", "/"))
            await pg.wait_for_timeout(600)
            png = await pg.screenshot(clip={"x": 0, "y": 0, "width": 794, "height": 1123})
            im = Image.open(io.BytesIO(png)).convert("RGB")
            im_resized = im.resize((1405, 1874), Image.LANCZOS)
            
            # Save in amostras and img
            im_resized.save(os.path.join(OUT_AMOSTRAS, out_webp), "WEBP", quality=90, method=6)
            im_resized.save(os.path.join(TOOLS, out_webp.replace(".webp", ".png")))
            print(f"Rendered sample {out_webp}: {im_resized.size} ({os.path.getsize(os.path.join(OUT_AMOSTRAS, out_webp))//1024} KB)")
            await pg.close()
            
        # Copy cinetica-x-dinamica.webp also to img/sample-5.webp
        shutil.copy(os.path.join(OUT_AMOSTRAS, "cinetica-x-dinamica.webp"), os.path.join(OUT_IMG, "sample-5.webp"))
        shutil.copy(os.path.join(OUT_AMOSTRAS, "pag-21.webp"), os.path.join(OUT_IMG, "sample-1.webp"))
        shutil.copy(os.path.join(OUT_AMOSTRAS, "pag-35.webp"), os.path.join(OUT_IMG, "sample-2.webp"))
        shutil.copy(os.path.join(OUT_AMOSTRAS, "pag-37.webp"), os.path.join(OUT_IMG, "sample-3.webp"))
        shutil.copy(os.path.join(OUT_AMOSTRAS, "pag-39.webp"), os.path.join(OUT_IMG, "sample-4.webp"))
        
        # 3. Render Mockups
        cov_main_rel = "cover-main.png"
        cov_b1_rel = "cover-bonus-1.png"
        cov_b2_rel = "cover-bonus-2.png"
        
        samples_rel = ["cinetica-x-dinamica.png", "pag-21.png", "pag-35.png", "pag-37.png", "pag-39.png", "pag-42.png"]
        
        hero_html = page_wrap(1200, 886, trio_html(cov_b1_rel, cov_b2_rel, cov_main_rel))
        solo1_html = page_wrap(720, 1000, tab_html(cov_b1_rel, 40, 40, 640, 920, 2))
        solo2_html = page_wrap(720, 1000, tab_html(cov_b2_rel, 40, 40, 640, 920, 2))
        collage_html_code = page_wrap(1100, 1620, collage_html(cov_main_rel, samples_rel))
        
        mockups = [
            ("hero-kit", hero_html, 1200, 886),
            ("combo-entregaveis", hero_html, 1200, 886),
            ("bonus-1", solo1_html, 720, 1000),
            ("bonus-2", solo2_html, 720, 1000),
            ("combo-amostras", collage_html_code, 1100, 1620),
        ]
        
        for name, html, w, h in mockups:
            f = os.path.join(TOOLS, f"_mk_{name}.html")
            with open(f, "w", encoding="utf-8") as file:
                file.write(html)
            pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
            await pg.goto("file:///" + f.replace("\\", "/"))
            await pg.wait_for_timeout(700)
            png = await pg.screenshot(omit_background=True, clip={"x": 0, "y": 0, "width": w, "height": h})
            im = Image.open(io.BytesIO(png)).convert("RGBA")
            
            # Save into mockups and img
            p1 = os.path.join(OUT_MOCKUPS, f"{name}.webp")
            p2 = os.path.join(OUT_IMG, f"kit-{name.replace('combo-','').replace('hero-kit','hero')}.webp" if "kit" in name or "combo" in name else f"{name}.webp")
            im.save(p1, "WEBP", quality=90, method=6)
            im.save(p2, "WEBP", quality=90, method=6)
            print(f"Saved mockup {name}.webp: {im.size} ({os.path.getsize(p1)//1024} KB)")
            await pg.close()
            
        await b.close()
        
    print("ALL UK ASSETS GENERATED SUCCESSFULLY!")

if __name__ == "__main__":
    asyncio.run(main())

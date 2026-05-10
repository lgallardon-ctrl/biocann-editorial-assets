#!/usr/bin/env python3
"""
BIOCANN® — Generador de assets Mayo 2026
Produce HTML + batch config JSON para renderizar con render.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
TOKENS = "../../_templates/editorial-html/tokens.css"
COMPONENTS = "../../_templates/editorial-html/components.css"

DISCLAIMER = "El acceso a productos derivados de cannabis medicinal está sujeto a evaluación profesional, documentación correspondiente y normativa vigente."
DISCLAIMER_SHORT = "Información de carácter institucional. No constituye recomendación médica."

def head(title):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>BIOCANN · {title}</title>
<link rel="stylesheet" href="{TOKENS}">
<link rel="stylesheet" href="{COMPONENTS}">"""

# ─────────────────────────────────────────────────────────────
# TEMPLATE BUILDERS
# ─────────────────────────────────────────────────────────────

def feed_monolith(slug, title, eyebrow, headline_lines, subhead="", body="", cta_text="", cta_url="", pagination="01 / 01", marca="BIOCANN"):
    hl = "\n      ".join(f"[{l}]" if l.startswith("<") else l for l in headline_lines)
    body_block = f'\n    <p class="b-body">{body}</p>' if body else ""
    cta_block = f'\n    <div class="b-cta-pill" style="margin-bottom: 28px;">{cta_text} <span class="arrow">→</span> {cta_url}</div>' if cta_text else ""
    wordmark = f"{marca}<sup>®</sup>" if marca != "Los Cauces" else "LOS CAUCES<sup>®</sup>"
    coord = "42°08′S · 71°24′W · PATAGONIA" if marca == "BIOCANN" else "42°08′S · 71°24′W · CHUBUT"
    return f"""{head(title)}
<style>
  body {{ background: var(--green); }}
  .b-canvas {{ background: var(--green); padding: 96px var(--feed-margin) 80px; display: flex; flex-direction: column; }}
  .b-wordmark {{ color: var(--white-pat); }}
  .b-coord {{ color: var(--white-pat); opacity: 0.55; }}
  .b-canvas .b-top-bar {{ position: static; padding: 0; display: flex; }}
</style>
</head>
<body>
  <div class="b-canvas b-canvas--feed noise-overlay">
    <div class="b-top-bar" style="position:static;padding:0 0 36px 0;">
      <div class="b-wordmark">{wordmark}</div>
      <div class="b-coord">{coord}</div>
    </div>
    <div class="b-eyebrow">{eyebrow}</div>
    <h1 class="b-headline b-headline--xl" style="margin-top: 80px;">
      {chr(10).join(headline_lines)}
    </h1>
    <div class="b-hairline b-hairline--lg" style="margin-top: 48px;"></div>
    {"" if not subhead else f'<div class="b-subhead" style="margin-top: 36px;">{subhead}</div>'}{body_block}
    <div class="b-spacer"></div>{cta_block}
    <div class="b-footer">
      <div class="b-disclaimer">{DISCLAIMER}</div>
      <div class="b-pagination">{pagination}</div>
    </div>
  </div>
</body>
</html>"""


def carousel_slide_white(slug, title, eyebrow, headline_lines, subhead="", body="", cta_text="", cta_url="", pagination="", marca="BIOCANN"):
    body_block = f'\n    <p class="b-body" style="color: var(--carbon);">{body}</p>' if body else ""
    cta_block = f'\n    <div class="b-cta-pill b-cta-pill--light" style="margin-bottom: 28px;">{cta_text} <span class="arrow" style="color:var(--green)">→</span> {cta_url}</div>' if cta_text else ""
    wordmark = "BIOCANN<sup>®</sup>"
    return f"""{head(title)}
<style>
  body {{ background: var(--white-pat); }}
  .b-canvas {{ background: var(--white-pat); padding: 96px var(--feed-margin) 80px; display: flex; flex-direction: column; }}
  .b-eyebrow {{ color: var(--copper-base) !important; }}
  .b-headline {{ color: var(--carbon) !important; }}
  .b-subhead {{ color: var(--carbon) !important; opacity: 0.78; }}
  .b-hairline {{ background: var(--copper-base) !important; }}
  .b-wordmark {{ color: var(--green) !important; }}
  .b-coord {{ color: var(--carbon) !important; opacity: 0.4; }}
  .b-disclaimer {{ color: var(--carbon); opacity: 0.42; }}
  .b-pagination {{ color: var(--carbon); opacity: 0.6; }}
  .b-canvas .b-top-bar {{ position: static; padding: 0; display: flex; }}
</style>
</head>
<body>
  <div class="b-canvas b-canvas--feed">
    <div class="b-top-bar" style="position:static;padding:0 0 36px 0;">
      <div class="b-wordmark">{wordmark}</div>
      <div class="b-coord">42°08′S · 71°24′W · PATAGONIA</div>
    </div>
    <div class="b-eyebrow">{eyebrow}</div>
    <h1 class="b-headline b-headline--xl" style="margin-top: 80px;">
      {chr(10).join(headline_lines)}
    </h1>
    <div class="b-hairline b-hairline--lg" style="margin-top: 48px;"></div>
    {"" if not subhead else f'<div class="b-subhead" style="margin-top: 36px;color:var(--carbon);opacity:0.78">{subhead}</div>'}{body_block}
    <div class="b-spacer"></div>{cta_block}
    <div class="b-footer">
      <div class="b-disclaimer">{DISCLAIMER}</div>
      <div class="b-pagination">{pagination}</div>
    </div>
  </div>
</body>
</html>"""


def story_monolith(slug, title, eyebrow, headline_lines, subhead="", body="", cta_text="", cta_url="", marca="BIOCANN"):
    body_block = f'\n    <p class="b-body" style="font-size: 17px; margin-top: 32px;">{body}</p>' if body else ""
    cta_block = f'\n    <div class="b-cta-pill b-cta-pill--story" style="margin-bottom: 32px;">{cta_text} <span class="arrow">→</span> {cta_url}</div>' if cta_text else ""
    wordmark = "BIOCANN<sup>®</sup>" if marca == "BIOCANN" else "LOS CAUCES<sup>®</sup>"
    coord = "42°08′S · 71°24′W · PATAGONIA"
    return f"""{head(title)}
<style>
  body {{ background: var(--green); }}
  .b-canvas {{ background: var(--green); padding: 120px var(--story-margin) 96px; display: flex; flex-direction: column; }}
  .b-wordmark {{ color: var(--white-pat); }}
  .b-coord {{ color: var(--white-pat); opacity: 0.55; }}
</style>
</head>
<body>
  <div class="b-canvas b-canvas--story noise-overlay">
    <div class="b-top-bar" style="position:static;padding:0 0 48px 0;">
      <div class="b-wordmark b-wordmark--story">{wordmark}</div>
      <div class="b-coord b-coord--story">{coord}</div>
    </div>
    <div class="b-eyebrow b-eyebrow--story">{eyebrow}</div>
    <h1 class="b-headline b-headline--xl" style="margin-top: 120px; font-size: 78px;">
      {chr(10).join(headline_lines)}
    </h1>
    <div class="b-hairline b-hairline--lg" style="margin-top: 60px;"></div>
    {"" if not subhead else f'<div class="b-subhead b-subhead--story" style="margin-top: 40px;">{subhead}</div>'}{body_block}
    <div class="b-spacer"></div>{cta_block}
    <div class="b-footer">
      <div class="b-disclaimer" style="font-size: 9.5px;">{DISCLAIMER}</div>
    </div>
  </div>
</body>
</html>"""


def linkedin_t10(slug, title, hl_green, hl_white, category, subhead, cta_text="Consultar", cta_url="biocann.ar"):
    return f"""{head(title)}
<style>
  body {{ background: var(--green); margin: 0; padding: 0; }}
  .canvas {{ width: 1200px; height: 628px; display: flex; flex-direction: row; overflow: hidden; position: relative; }}
  .col-green {{ width: 528px; background: var(--green); padding: 52px 48px 48px 72px; display: flex; flex-direction: column; position: relative; flex-shrink: 0; }}
  .col-green::before {{ content: ''; position: absolute; inset: 0; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.2' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.030 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"); pointer-events: none; }}
  .col-green > * {{ position: relative; z-index: 1; }}
  .divider {{ width: 1px; background: var(--copper-light); opacity: 0.4; flex-shrink: 0; }}
  .col-white {{ flex: 1 1 auto; background: var(--white-pat); padding: 52px 64px 48px 56px; display: flex; flex-direction: column; }}
  .lk-wordmark {{ font-family: var(--font-display); font-weight: 600; font-size: 18px; letter-spacing: 0.04em; color: var(--white-pat); }}
  .lk-wordmark sup {{ font-size: 8px; vertical-align: 8px; }}
  .lk-headline-green {{ font-family: var(--font-display); font-weight: 300; font-size: 40px; line-height: 1.1; letter-spacing: -0.02em; color: var(--white-pat); margin-top: 24px; max-width: 440px; }}
  .lk-headline-green em {{ font-style: italic; font-weight: 400; color: var(--copper-light); }}
  .lk-hairline-green {{ width: 48px; height: 1px; background: var(--copper-light); margin-top: 28px; }}
  .lk-coord {{ font-family: var(--font-microcopy); font-size: 9px; letter-spacing: 0.30em; text-transform: uppercase; color: var(--white-pat); opacity: 0.42; margin-top: auto; }}
  .lk-category {{ font-family: var(--font-microcopy); font-size: 10px; font-weight: 500; letter-spacing: 0.36em; text-transform: uppercase; color: var(--copper-base); display: flex; align-items: center; gap: 10px; }}
  .lk-category::before {{ content: ''; display: block; width: 20px; height: 1px; background: var(--copper-base); }}
  .lk-headline-white {{ font-family: var(--font-display); font-weight: 300; font-size: 34px; line-height: 1.15; letter-spacing: -0.018em; color: var(--carbon); margin-top: 20px; max-width: 560px; }}
  .lk-headline-white em {{ font-style: italic; font-weight: 400; color: var(--green); }}
  .lk-hairline-white {{ width: 48px; height: 1px; background: var(--copper-base); margin-top: 20px; }}
  .lk-subhead {{ font-family: var(--font-microcopy); font-size: 15px; font-weight: 500; line-height: 1.45; color: var(--carbon); opacity: 0.72; margin-top: 16px; max-width: 560px; }}
  .spacer {{ flex: 1 1 auto; }}
  .lk-cta {{ display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px; border: 1px solid var(--copper-base); border-radius: 999px; font-family: var(--font-microcopy); font-size: 10px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; color: var(--carbon); align-self: flex-start; }}
  .lk-disclaimer {{ font-family: var(--font-body); font-size: 8px; line-height: 1.5; color: var(--carbon); opacity: 0.38; margin-top: 10px; max-width: 580px; }}
</style>
</head>
<body>
<div class="canvas">
  <div class="col-green">
    <div class="lk-wordmark">BIOCANN<sup>®</sup></div>
    <div class="lk-headline-green">{hl_green}</div>
    <div class="lk-hairline-green"></div>
    <div class="lk-coord">42°08′S · 71°24′W · PATAGONIA ARGENTINA</div>
  </div>
  <div class="divider"></div>
  <div class="col-white">
    <div class="lk-category">{category}</div>
    <div class="lk-headline-white">{hl_white}</div>
    <div class="lk-hairline-white"></div>
    <div class="lk-subhead">{subhead}</div>
    <div class="spacer"></div>
    <div class="lk-cta">{cta_text} <span style="font-size:13px;font-weight:300;">→</span> {cta_url}</div>
    <div class="lk-disclaimer">{DISCLAIMER_SHORT}</div>
  </div>
</div>
</body>
</html>"""


def feed_photo_overlay(slug, title, eyebrow, headline_lines, subhead="", cta_text="", cta_url="", photo_src="", marca="BIOCANN"):
    """Feed with photo as background + green gradient overlay. Photo placeholder if no src."""
    bg = f"url('{photo_src}')" if photo_src else "linear-gradient(135deg, #1a2e24 0%, #2F4F3E 100%)"
    photo_note = '<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:rgba(255,255,255,0.15);font-family:sans-serif;font-size:14px;letter-spacing:0.2em;text-transform:uppercase;pointer-events:none">INSERTAR FOTO</div>' if not photo_src else ""
    cta_block = f'<div class="b-cta-pill" style="margin-bottom: 28px;">{cta_text} <span class="arrow">→</span> {cta_url}</div>' if cta_text else ""
    return f"""{head(title)}
<style>
  body {{ background: var(--green); }}
  .b-canvas {{
    background: {bg} center/cover no-repeat;
    padding: 0;
    display: flex;
    flex-direction: column;
    position: relative;
  }}
  .b-canvas::after {{
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(47,79,62,0.96) 0%, rgba(47,79,62,0.82) 40%, rgba(47,79,62,0.2) 70%, transparent 100%);
    pointer-events: none;
  }}
  .overlay-content {{
    position: absolute;
    inset: 0;
    padding: 96px var(--feed-margin) 80px;
    display: flex;
    flex-direction: column;
    z-index: 1;
  }}
  .b-wordmark {{ color: var(--white-pat); }}
  .b-coord {{ color: var(--white-pat); opacity: 0.55; }}
</style>
</head>
<body>
  <div class="b-canvas b-canvas--feed noise-overlay">
    {photo_note}
    <div class="overlay-content">
      <div class="b-top-bar" style="position:static;padding:0 0 36px 0;">
        <div class="b-wordmark">BIOCANN<sup>®</sup></div>
        <div class="b-coord">42°08′S · 71°24′W · PATAGONIA</div>
      </div>
      <div class="b-spacer"></div>
      <div class="b-eyebrow" style="color:var(--copper-light);margin-bottom:20px">{eyebrow}</div>
      <h1 class="b-headline b-headline--xl" style="font-size:72px">
        {chr(10).join(headline_lines)}
      </h1>
      <div class="b-hairline b-hairline--lg" style="margin-top: 40px;"></div>
      {'<div class="b-subhead" style="margin-top:28px;color:rgba(247,245,240,0.88)">' + subhead + '</div>' if subhead else ''}
      {cta_block}
      <div class="b-footer" style="margin-top:auto;padding-top:24px">
        <div class="b-disclaimer" style="color:rgba(247,245,240,0.55)">{DISCLAIMER}</div>
      </div>
    </div>
  </div>
</body>
</html>"""


def feed_photo_split(slug, title, eyebrow, headline_lines, subhead="", cta_text="", cta_url="", photo_src="", marca="BIOCANN"):
    """Feed split: photo top 58% + green block bottom 42%"""
    photo_css = f"url('{photo_src}') center/cover no-repeat" if photo_src else "linear-gradient(135deg, #1a2e24 0%, #2b4438 100%)"
    photo_note = '<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,0.18);font-family:sans-serif;font-size:14px;letter-spacing:0.2em;text-transform:uppercase">INSERTAR FOTO</div>' if not photo_src else ""
    cta_block = f'<div class="b-cta-pill" style="margin-bottom:0;margin-top:auto;">{cta_text} <span class="arrow">→</span> {cta_url}</div>' if cta_text else ""
    return f"""{head(title)}
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ width: 1080px; height: 1350px; overflow: hidden; }}
  .photo-block {{
    width: 1080px; height: 785px;
    background: {photo_css};
    position: relative;
    flex-shrink: 0;
  }}
  .green-block {{
    width: 1080px;
    height: 565px;
    background: var(--green);
    padding: 44px var(--feed-margin) 56px;
    display: flex;
    flex-direction: column;
    position: relative;
  }}
  .green-block::before {{
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.2' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.025 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
    pointer-events: none;
  }}
  .green-block > * {{ position: relative; z-index: 1; }}
  .top-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }}
  .wordmark {{ font-family: var(--font-display); font-weight: 600; font-size: 15px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--white-pat); }}
  .wordmark sup {{ font-size: 7px; vertical-align: 7px; }}
  .coord {{ font-family: var(--font-microcopy); font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase; color: var(--white-pat); opacity: 0.5; }}
  .eyebrow {{ font-family: var(--font-microcopy); font-size: 10px; font-weight: 500; letter-spacing: 0.28em; text-transform: uppercase; color: var(--copper-light); margin-bottom: 14px; }}
  .headline {{ font-family: var(--font-display); font-weight: 300; font-size: 52px; line-height: 1.05; letter-spacing: -0.02em; color: var(--white-pat); }}
  .headline em {{ font-style: italic; font-weight: 400; }}
  .subhead {{ font-family: var(--font-microcopy); font-size: 14px; color: rgba(247,245,240,0.72); margin-top: 14px; }}
  .hairline {{ width: 48px; height: 1px; background: var(--copper-light); margin-top: 20px; }}
  .footer {{ margin-top: auto; padding-top: 16px; }}
  .disclaimer {{ font-family: var(--font-body); font-size: 8.5px; color: rgba(247,245,240,0.45); line-height: 1.5; }}
</style>
</head>
<body>
  <div class="photo-block">{photo_note}</div>
  <div class="green-block">
    <div class="top-bar">
      <span class="wordmark">BIOCANN<sup>®</sup></span>
      <span class="coord">PATAGONIA</span>
    </div>
    <div class="eyebrow">{eyebrow}</div>
    <div class="headline">
      {chr(10).join(headline_lines)}
    </div>
    {'<div class="hairline"></div><div class="subhead">' + subhead + '</div>' if subhead else ''}
    {cta_block}
    <div class="footer">
      <div class="disclaimer">{DISCLAIMER}</div>
    </div>
  </div>
</body>
</html>"""


# ─────────────────────────────────────────────────────────────
# POST DEFINITIONS
# ─────────────────────────────────────────────────────────────

def save(filename, content):
    path = BASE / filename
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {filename}")
    return str(path)


posts = []  # list of (html_path, png_path, story, linkedin)

# ─── THIS WEEK (8–11 May) ────────────────────────────────────

posts.append((save("feed-03-08mayo-no-todo-igual.html",
    feed_photo_split("feed-03-08mayo", "POST-003 · No todo cannabis igual",
        eyebrow="ACCESO REGULADO · CALIDAD",
        headline_lines=["No todo cannabis", "medicinal es igual."],
        subhead="La trazabilidad de origen hace la diferencia.",
        cta_text="Conocé más", cta_url="biocann.ar",
        photo_src="../photos/gus01953.jpg"
    )), BASE / "feed-03-08mayo-no-todo-igual.png", False, False))

posts.append((save("feed-05-11mayo-reprocann-dm.html",
    feed_photo_overlay("feed-05-11mayo", "POST-005 · REPROCANN + DM",
        eyebrow="ACCESO REGULADO",
        headline_lines=["¿Tenés REPROCANN", "y sabés qué", "consumís?"],
        subhead="Escribinos y te orientamos sobre tu acceso.",
        cta_text="Escribir COBERTURA", cta_url="DM @biocannok",
        photo_src="../photos/gus01956.jpg"
    )), BASE / "feed-05-11mayo-reprocann-dm.png", False, False))

posts.append((save("story-11mayo-lote-historia.html",
    story_monolith("story-11mayo", "STORY-11/05 · Trazabilidad",
        eyebrow="TRAZABILIDAD",
        headline_lines=["El lote", "tiene", "<em>historia.</em>"],
        subhead="Cada número de lote documenta cultivo, proceso y análisis.",
        cta_text="Conocer BIOCANN", cta_url="biocann.ar"
    )), BASE / "story-11mayo-lote-historia.png", True, False))

# ─── WEEK 2 (12–15 May) ──────────────────────────────────────

posts.append((save("linkedin-06-12mayo-b2b-institucional.html",
    linkedin_t10("lk-06-12mayo", "POST-006 · LinkedIn B2B Institucional",
        hl_green="Ciencia regulada.<br><em>Integración</em><br>vertical.",
        hl_white="Cultivamos, procesamos y distribuimos bajo protocolo.",
        category="B2B · INSTITUCIONAL · MAYO 2026",
        subhead="BIOCANN® opera bajo marco regulatorio Ley 27.350 con trazabilidad desde semilla hasta producto final disponible para farmacias, dispensarios y ONGs.",
        cta_text="Contactar", cta_url="biocann.ar"
    )), BASE / "linkedin-06-12mayo-b2b-institucional.png", False, True))

posts.append((save("story-12mayo-origen-proceso.html",
    story_monolith("story-12mayo", "STORY-12/05 · Patagonia",
        eyebrow="ORIGEN · PATAGONIA",
        headline_lines=["Del sur,", "con", "<em>protocolo.</em>"],
        subhead="El origen de un producto de cannabis define su calidad. Patagonia no es un paisaje: es una condición de cultivo.",
        cta_text="Ver origen", cta_url="biocann.ar/nosotros"
    )), BASE / "story-12mayo-origen-proceso.png", True, False))

# POST-007 Carrusel 5 razones trazabilidad — 6 slides
slides_5razones = [
    ("s01", "feed-monolith",  "TRAZABILIDAD · BIOCANN®",    ["Cinco razones por", "las que la", "<em>trazabilidad</em>", "importa."],           "",                         "", "01 / 06"),
    ("s02", "white-slide",    "RAZÓN 01 · ORIGEN",          ["Sabés de", "dónde viene", "lo que consumís."],          "Genética registrada en INASE. Cultivo en Patagonia documentado por lote.",   "", "02 / 06"),
    ("s03", "white-slide",    "RAZÓN 02 · PROCESO",         ["Sabés cómo fue", "<em>procesado.</em>"],                 "Extracción CO₂ supercrítico. Temperatura y tiempo registrados. Sin solventes residuales.",  "", "03 / 06"),
    ("s04", "white-slide",    "RAZÓN 03 · ANÁLISIS",        ["Cada lote tiene", "análisis de", "<em>laboratorio.</em>"],"Concentración de cannabinoides, terpenos y ausencia de contaminantes verificada antes del despacho.", "", "04 / 06"),
    ("s05", "white-slide",    "RAZÓN 04 + 05 · ACCESO",     ["Sabés qué", "recibís. Y", "<em>cuándo.</em>"],           "Número de lote en cada envase. Consulta de historial disponible. Renovación documentada.",     "", "05 / 06"),
    ("s06", "feed-monolith",  "TRAZABILIDAD · BIOCANN®",    ["Acceso", "documentado.", "<em>Siempre.</em>"],           "Coberturas BIOCANN® — acceso con trazabilidad completa.",  "Conocer Coberturas →", "06 / 06"),
]
for i, (sid, kind, ey, hls, sub, cta_str, pag) in enumerate(slides_5razones):
    fn = f"carrusel-07-12mayo-5razones-{sid}.html"
    cta_t = cta_str.replace(" →","") if " →" in cta_str else ""
    cta_u = "biocann.ar/pricing-plans/list" if cta_t else ""
    if kind == "feed-monolith":
        html = feed_monolith(fn, f"POST-007 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag)
    else:
        html = carousel_slide_white(fn, f"POST-007 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag)
    posts.append((save(fn, html), BASE / fn.replace(".html",".png"), False, False))

# POST-008 Reel cover lote trazable
posts.append((save("feed-08-13mayo-lote-trazable.html",
    feed_photo_split("feed-08-13mayo", "POST-008 · Lote trazable",
        eyebrow="CALIDAD · TRAZABILIDAD",
        headline_lines=["Un lote trazable", "no es solo un", "<em>número.</em>"],
        subhead="Es la documentación completa de un recorrido regulado.",
        cta_text="Consultar", cta_url="biocann.ar",
        photo_src="../photos/gus01957.jpg"
    )), BASE / "feed-08-13mayo-lote-trazable.png", False, False))

posts.append((save("story-13mayo-papel-no-basta.html",
    story_monolith("story-13mayo", "STORY-13/05 · Coberturas",
        eyebrow="COBERTURAS BIOCANN®",
        headline_lines=["El papel no", "es", "<em>suficiente.</em>"],
        subhead="Tener REPROCANN es el primer paso. Acceder a producto trazable, con acompañamiento profesional, es el siguiente.",
        cta_text="Ver Coberturas", cta_url="biocann.ar/pricing-plans/list"
    )), BASE / "story-13mayo-papel-no-basta.png", True, False))

posts.append((save("linkedin-09-14mayo-ley-salome.html",
    linkedin_t10("lk-09-14mayo", "POST-009 · LinkedIn Ley Salomé",
        hl_green="Ley Salomé:<br>el marco<br><em>provincial.</em>",
        hl_white="Chubut habilita el acceso regulado a cannabis medicinal.",
        category="FARMACIAS · CHUBUT · LEY I N° 790",
        subhead="La Ley I N° 790 (\"Ley Salomé\") habilita a personas físicas y jurídicas con proyectos de I+D aprobados bajo Ley 27.350 a operar en la cadena de cannabis medicinal en Chubut. BIOCANN® está habilitado por Res. 2609/2022 del Ministerio de Salud de la Nación.",
        cta_text="Contactar equipo B2B", cta_url="biocann.ar"
    )), BASE / "linkedin-09-14mayo-ley-salome.png", False, True))

posts.append((save("story-14mayo-4pasos-teaser.html",
    story_monolith("story-14mayo", "STORY-14/05 · 4 pasos teaser",
        eyebrow="COBERTURAS BIOCANN®",
        headline_lines=["Tu acceso en", "cuatro", "<em>pasos.</em>"],
        subhead="Evaluación → Plan → Producto trazable → Acompañamiento. Sin vueltas.",
        cta_text="Ver proceso", cta_url="biocann.ar/pricing-plans/list"
    )), BASE / "story-14mayo-4pasos-teaser.png", True, False))

# POST-010 Carrusel Coberturas 4 pasos — 5 slides
slides_4pasos = [
    ("s01","feed-monolith", "COBERTURAS BIOCANN® · 4 PASOS", ["Tu acceso", "a cannabis", "<em>medicinal.</em>"],       "", "", "01 / 05"),
    ("s02","white-slide",   "PASO 01 · EVALUACIÓN",         ["Evaluación", "<em>profesional.</em>"],                   "Consulta inicial con profesional de salud integrado a la Red Médica BIOCANN®.",   "", "02 / 05"),
    ("s03","white-slide",   "PASO 02 · PLAN",               ["Elegís tu", "<em>cobertura.</em>"],                      "Tres planes disponibles. Producto trazable con lote documentado incluido.",       "", "03 / 05"),
    ("s04","white-slide",   "PASO 03 · PRODUCTO",           ["Producto", "trazable a", "<em>domicilio.</em>"],          "Envío a todo el país. Etiqueta con número de lote, análisis y fecha de producción.", "", "04 / 05"),
    ("s05","feed-monolith", "PASO 04 · ACOMPAÑAMIENTO",     ["Seguimiento.", "<em>Siempre.</em>"],                      "Renovaciones, ajustes, consultas. El acceso no termina con el primer producto.",    "Ver Coberturas →", "05 / 05"),
]
for i, (sid, kind, ey, hls, sub, cta_str, pag) in enumerate(slides_4pasos):
    fn = f"carrusel-10-14mayo-coberturas-4pasos-{sid}.html"
    cta_t = cta_str.replace(" →","") if " →" in cta_str else ""
    cta_u = "biocann.ar/pricing-plans/list" if cta_t else ""
    html = feed_monolith(fn, f"POST-010 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag) if kind == "feed-monolith" \
           else carousel_slide_white(fn, f"POST-010 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag)
    posts.append((save(fn, html), BASE / fn.replace(".html",".png"), False, False))

posts.append((save("feed-11-15mayo-loscauces.html",
    feed_photo_overlay("feed-11-15mayo", "POST-011 · Los Cauces",
        eyebrow="LOS CAUCES® · PATAGONIA",
        headline_lines=["Una experiencia", "diseñada en", "<em>Patagonia.</em>"],
        subhead="Reserva cannábica en Chubut. Entorno, conocimiento y acceso regulado.",
        cta_text="Reservar", cta_url="reservaloscauces.com",
        photo_src="../photos/gus01959.jpg"
    )), BASE / "feed-11-15mayo-loscauces.png", False, False))

posts.append((save("story-15mayo-cordillera.html",
    story_monolith("story-15mayo", "STORY-15/05 · Los Cauces",
        eyebrow="LOS CAUCES® · RESERVA",
        headline_lines=["700 msnm.", "<em>Patagonia.</em>"],
        subhead="Rodeados de cordillera. Cultivamos con protocolo donde la naturaleza marca el ritmo.",
        cta_text="Reservar visita", cta_url="reservaloscauces.com"
    )), BASE / "story-15mayo-cordillera.png", True, False))

# ─── WEEK 3 (17–22 May) ──────────────────────────────────────

posts.append((save("story-17mayo-lote-trazable.html",
    story_monolith("story-17mayo", "STORY-17/05 · Calidad",
        eyebrow="CALIDAD · TRAZABILIDAD",
        headline_lines=["¿Sabés qué", "es un lote", "<em>trazable?</em>"],
        subhead="Número de lote = origen + proceso + análisis de laboratorio documentados. Chequeá el tuyo en la etiqueta.",
        cta_text="Más info", cta_url="biocann.ar"
    )), BASE / "story-17mayo-lote-trazable.png", True, False))

posts.append((save("feed-13-18mayo-del-lote.html",
    feed_photo_overlay("feed-13-18mayo", "POST-013 · Del lote al paciente",
        eyebrow="TRAZABILIDAD · INTEGRACIÓN VERTICAL",
        headline_lines=["Del lote", "al", "<em>paciente.</em>"],
        subhead="Cultivo documentado → extracción registrada → análisis de laboratorio → envío trazado.",
        cta_text="Conocer proceso", cta_url="biocann.ar/nosotros",
        photo_src="../photos/gus01953.jpg"
    )), BASE / "feed-13-18mayo-del-lote.png", False, False))

posts.append((save("linkedin-14-19mayo-genetica-inase.html",
    linkedin_t10("lk-14-19mayo", "POST-014 · LinkedIn INASE",
        hl_green="Genética<br>registrada.<br><em>Calidad</em><br>documentada.",
        hl_white="Nuestras variedades tienen registro oficial en INASE.",
        category="INASE · GENÉTICA · CALIDAD",
        subhead="BIOCANN® trabaja con genéticas cannabinoides registradas en el Instituto Nacional de Semillas (INASE), garantizando trazabilidad desde la semilla hasta el producto final.",
        cta_text="Ver estándares", cta_url="biocann.ar/nosotros"
    )), BASE / "linkedin-14-19mayo-genetica-inase.png", False, True))

posts.append((save("story-19mayo-inase-diferencial.html",
    story_monolith("story-19mayo", "STORY-19/05 · INASE",
        eyebrow="INASE · GENÉTICA REGISTRADA",
        headline_lines=["Genética.", "<em>Registrada.</em>"],
        subhead="Nuestras variedades están registradas en INASE. No es marketing: es documentación oficial.",
        cta_text="Conocer BIOCANN", cta_url="biocann.ar/nosotros"
    )), BASE / "story-19mayo-inase-diferencial.png", True, False))

# POST-015 Carrusel FAQ REPROCANN — 6 slides
slides_faq = [
    ("s01","feed-monolith", "REPROCANN · PREGUNTAS FRECUENTES", ["¿Necesitás", "<em>REPROCANN?</em>"],               "", "", "01 / 06"),
    ("s02","white-slide",   "¿QUÉ ES REPROCANN?",              ["El registro", "nacional."],                         "Registro del Programa de Cannabis del Ministerio de Salud de la Nación. Habilita el uso terapéutico.", "", "02 / 06"),
    ("s03","white-slide",   "¿QUIÉN LO NECESITA?",             ["Pacientes con", "indicación", "<em>médica.</em>"],  "Quien use cannabis con fines terapéuticos bajo indicación profesional. El médico inicia el trámite.", "", "03 / 06"),
    ("s04","white-slide",   "¿CUÁNTO TARDA?",                  ["Variable según", "<em>caso.</em>"],                 "El proceso depende de la documentación y la revisión del MSN. Tu médico puede orientarte en el tiempo estimado.", "", "04 / 06"),
    ("s05","white-slide",   "¿SE RENUEVA?",                    ["Sí. Con", "<em>seguimiento.</em>"],                 "REPROCANN tiene vigencia determinada. Se renueva con el profesional tratante y documentación actualizada.", "", "05 / 06"),
    ("s06","feed-monolith", "BIOCANN® + REPROCANN",            ["Acceso con", "<em>trazabilidad.</em>"],             "Tenés REPROCANN y buscás producto de calidad. Coberturas BIOCANN® te da acceso completo.", "Ver Coberturas →", "06 / 06"),
]
for i, (sid, kind, ey, hls, sub, cta_str, pag) in enumerate(slides_faq):
    fn = f"carrusel-15-19mayo-faq-reprocann-{sid}.html"
    cta_t = cta_str.replace(" →","") if " →" in cta_str else ""
    cta_u = "biocann.ar/pricing-plans/list" if cta_t else ""
    html = feed_monolith(fn, f"POST-015 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag) if kind == "feed-monolith" \
           else carousel_slide_white(fn, f"POST-015 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag)
    posts.append((save(fn, html), BASE / fn.replace(".html",".png"), False, False))

posts.append((save("feed-16-20mayo-origen-importa.html",
    feed_photo_overlay("feed-16-20mayo", "POST-016 · Origen importa",
        eyebrow="PATAGONIA · ORIGEN",
        headline_lines=["Origen", "<em>importa.</em>"],
        subhead="Cultivado en Patagonia a 700 msnm. El entorno no es estética: es calidad.",
        cta_text="Conocer origen", cta_url="biocann.ar/nosotros",
        photo_src="../photos/gus01959.jpg"
    )), BASE / "feed-16-20mayo-origen-importa.png", False, False))

posts.append((save("story-20mayo-700msnm.html",
    story_monolith("story-20mayo", "STORY-20/05 · 700 msnm",
        eyebrow="PATAGONIA · ORIGEN",
        headline_lines=["700 msnm.", "<em>Origen.</em>"],
        subhead="Cultivamos donde pocas empresas operan. La cordillera patagónica no es decoración: es parte del proceso.",
        cta_text="Conocer origen", cta_url="biocann.ar/nosotros"
    )), BASE / "story-20mayo-700msnm.png", True, False))

posts.append((save("linkedin-17-21mayo-plataforma-b2b.html",
    linkedin_t10("lk-17-21mayo", "POST-017 · LinkedIn B2B Plataforma",
        hl_green="BIOCANN® como<br><em>plataforma</em><br>B2B.",
        hl_white="Integración vertical desde cultivo hasta distribución B2B.",
        category="B2B · PLATAFORMA · INTEGRACIÓN VERTICAL",
        subhead="Farmacias, dispensarios, ONGs y operadores turísticos: BIOCANN® ofrece producto trazable, documentación regulatoria completa y acompañamiento profesional como partners del sistema de acceso.",
        cta_text="Ser partner", cta_url="biocann.ar"
    )), BASE / "linkedin-17-21mayo-plataforma-b2b.png", False, True))

posts.append((save("story-21mayo-beneficios-activos.html",
    story_monolith("story-21mayo", "STORY-21/05 · Beneficios Coberturas",
        eyebrow="COBERTURAS BIOCANN®",
        headline_lines=["Beneficios", "<em>activos</em>", "de tu plan."],
        subhead="Producto trazable · Acompañamiento profesional · Renovación asistida · Envío documentado.",
        cta_text="Ver planes", cta_url="biocann.ar/pricing-plans/list"
    )), BASE / "story-21mayo-beneficios-activos.png", True, False))

# POST-018 Carrusel Beneficios Cobertura — 5 slides
slides_beneficios = [
    ("s01","feed-monolith", "COBERTURAS BIOCANN® · BENEFICIOS", ["Lo que incluye", "tu", "<em>cobertura.</em>"],       "", "", "01 / 05"),
    ("s02","white-slide",   "BENEFICIO 01 · PRODUCTO",          ["Producto", "<em>trazable.</em>"],                    "Aceite BIOCANN® con número de lote, análisis de laboratorio y fecha de producción documentados.", "", "02 / 05"),
    ("s03","white-slide",   "BENEFICIO 02 · MÉDICO",            ["Acompañamiento", "<em>profesional.</em>"],            "Acceso a profesionales de la Red Médica BIOCANN® para orientación y seguimiento de tu tratamiento.", "", "03 / 05"),
    ("s04","white-slide",   "BENEFICIO 03 · RENOVACIÓN",        ["Renovación", "<em>asistida.</em>"],                  "El equipo BIOCANN® te acompaña en cada renovación de documentación para mantener tu acceso activo.", "", "04 / 05"),
    ("s05","feed-monolith", "BENEFICIO 04 · ENVÍO",             ["Envío a todo", "el país.", "<em>Siempre.</em>"],      "Despacho documentado con seguimiento. Tu producto llega con la trazabilidad intacta.", "Ver planes →", "05 / 05"),
]
for i, (sid, kind, ey, hls, sub, cta_str, pag) in enumerate(slides_beneficios):
    fn = f"carrusel-18-21mayo-beneficios-{sid}.html"
    cta_t = cta_str.replace(" →","") if " →" in cta_str else ""
    cta_u = "biocann.ar/pricing-plans/list" if cta_t else ""
    html = feed_monolith(fn, f"POST-018 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag) if kind == "feed-monolith" \
           else carousel_slide_white(fn, f"POST-018 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag)
    posts.append((save(fn, html), BASE / fn.replace(".html",".png"), False, False))

posts.append((save("feed-19-22mayo-remarketing.html",
    feed_monolith("feed-19-22mayo", "POST-019 · Remarketing",
        eyebrow="ACCESO REGULADO",
        headline_lines=["El momento", "es", "<em>ahora.</em>"],
        subhead="Si ya preguntaste, ya sabés que el sistema existe. El siguiente paso es tuyo.",
        cta_text="Iniciar acceso", cta_url="biocann.ar/pricing-plans/list"
    )), BASE / "feed-19-22mayo-remarketing.png", False, False))

posts.append((save("story-22mayo-si-ya-preguntaste.html",
    story_monolith("story-22mayo", "STORY-22/05 · Remarketing",
        eyebrow="ACCESO · REMARKETING",
        headline_lines=["Si ya", "preguntaste,", "<em>este es</em>", "el momento."],
        subhead="El acceso regulado existe. BIOCANN® tiene el sistema completo para darte certeza.",
        cta_text="Retomar consulta", cta_url="biocann.ar/pricing-plans/list"
    )), BASE / "story-22mayo-si-ya-preguntaste.png", True, False))

# ─── WEEK 4 (24–31 May) ──────────────────────────────────────

posts.append((save("story-24mayo-ley-salome.html",
    story_monolith("story-24mayo", "STORY-24/05 · Ley Salomé",
        eyebrow="INSTITUCIONAL · CHUBUT",
        headline_lines=["Ley I N° 790.", "<em>Chubut.</em>"],
        subhead="La Ley Salomé habilita el acceso al cannabis medicinal en Chubut. BIOCANN® opera bajo esta norma como proyecto de I+D aprobado.",
        cta_text="Más información", cta_url="biocann.ar/nosotros"
    )), BASE / "story-24mayo-ley-salome.png", True, False))

posts.append((save("feed-21-25mayo-proceso-legal.html",
    feed_monolith("feed-21-25mayo", "POST-021 · Proceso legal",
        eyebrow="ACCESO REGULADO · PROCESO",
        headline_lines=["El proceso legal,", "paso a", "<em>paso.</em>"],
        subhead="REPROCANN → evaluación profesional → cobertura → producto trazable → seguimiento.",
        cta_text="Conocer proceso", cta_url="biocann.ar/servicios"
    )), BASE / "feed-21-25mayo-proceso-legal.png", False, False))

posts.append((save("story-25mayo-proceso-regulado.html",
    story_monolith("story-25mayo", "STORY-25/05 · Acceso",
        eyebrow="ACCESO REGULADO",
        headline_lines=["El acceso", "está", "<em>regulado.</em>"],
        subhead="No es un trámite complicado. Es un sistema documentado con profesionales que te acompañan.",
        cta_text="Iniciar acceso", cta_url="biocann.ar/pricing-plans/list"
    )), BASE / "story-25mayo-proceso-regulado.png", True, False))

posts.append((save("linkedin-22-26mayo-cierre-institucional.html",
    linkedin_t10("lk-22-26mayo", "POST-022 · LinkedIn Cierre Institucional",
        hl_green="Construcción<br>regulada.<br><em>Largo plazo.</em>",
        hl_white="Mayo 2026: un mes de operación desde Patagonia.",
        category="INSTITUCIONAL · MAYO 2026",
        subhead="BIOCANN® cierra un mes de actividad sostenida: nuevos pacientes incorporados, lotes despachados con trazabilidad completa y alianzas B2B en construcción bajo marco regulatorio Ley 27.350.",
        cta_text="Conectar", cta_url="biocann.ar/nosotros"
    )), BASE / "linkedin-22-26mayo-cierre-institucional.png", False, True))

# POST-023 Carrusel Qué mirar — 6 slides
slides_que_mirar = [
    ("s01","feed-monolith", "TRAZABILIDAD · GUÍA DE ELECCIÓN",   ["Qué mirar antes", "de elegir un", "<em>producto.</em>"],    "", "", "01 / 06"),
    ("s02","white-slide",   "CRITERIO 01 · ORIGEN",              ["¿De dónde", "<em>viene?</em>"],                            "Verificá que el cultivador esté bajo marco regulatorio. INASE registra las genéticas autorizadas.", "", "02 / 06"),
    ("s03","white-slide",   "CRITERIO 02 · TRAZABILIDAD",        ["¿Tiene número", "de <em>lote?</em>"],                      "Todo producto trazable lleva número de lote en la etiqueta. Sin lote, no hay documentación.", "", "03 / 06"),
    ("s04","white-slide",   "CRITERIO 03 · ANÁLISIS",            ["¿Tiene análisis", "<em>de laboratorio?</em>"],             "Concentración de cannabinoides y ausencia de contaminantes. Exigí el certificado de análisis.", "", "04 / 06"),
    ("s05","white-slide",   "CRITERIO 04 · ACOMPAÑAMIENTO",      ["¿Hay seguimiento", "<em>profesional?</em>"],               "El acceso al cannabis medicinal requiere seguimiento. Un producto sin acompañamiento no es un sistema.", "", "05 / 06"),
    ("s06","feed-monolith", "BIOCANN® · LOS CUATRO CRITERIOS",   ["Todo esto,", "<em>documentado.</em>"],                     "Origen patagónico · Lote trazable · Análisis de laboratorio · Acompañamiento profesional.", "Ver Coberturas →", "06 / 06"),
]
for i, (sid, kind, ey, hls, sub, cta_str, pag) in enumerate(slides_que_mirar):
    fn = f"carrusel-23-26mayo-que-mirar-{sid}.html"
    cta_t = cta_str.replace(" →","") if " →" in cta_str else ""
    cta_u = "biocann.ar/pricing-plans/list" if cta_t else ""
    html = feed_monolith(fn, f"POST-023 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag) if kind == "feed-monolith" \
           else carousel_slide_white(fn, f"POST-023 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag)
    posts.append((save(fn, html), BASE / fn.replace(".html",".png"), False, False))

posts.append((save("feed-24-27mayo-equipo.html",
    feed_photo_overlay("feed-24-27mayo", "POST-024 · Equipo",
        eyebrow="INSTITUCIONAL · EQUIPO",
        headline_lines=["Equipo.", "Proceso.", "<em>Propósito.</em>"],
        subhead="El sistema BIOCANN® es el resultado de años de trabajo documentado desde Patagonia.",
        cta_text="Conocer BIOCANN", cta_url="biocann.ar/nosotros",
        photo_src="../photos/gus01956.jpg"
    )), BASE / "feed-24-27mayo-equipo.png", False, False))

posts.append((save("story-27mayo-equipo-proposito.html",
    story_monolith("story-27mayo", "STORY-27/05 · Equipo",
        eyebrow="INSTITUCIONAL · EQUIPO",
        headline_lines=["Equipo.", "<em>Propósito.</em>"],
        subhead="Cultivadores, científicos, médicos y operadores logísticos trabajando bajo el mismo protocolo.",
        cta_text="Conocer equipo", cta_url="biocann.ar/nosotros"
    )), BASE / "story-27mayo-equipo-proposito.png", True, False))

posts.append((save("linkedin-25-28mayo-cierre-b2b.html",
    linkedin_t10("lk-25-28mayo", "POST-025 · LinkedIn B2B Cierre",
        hl_green="Patagonia como<br><em>ventaja</em><br>competitiva.",
        hl_white="B2B: cerramos mayo con nuevas alianzas estratégicas.",
        category="B2B · EXPORTACIÓN · CIERRE MAYO 2026",
        subhead="Patagonia no es solo origen: es un argumento diferencial para mercados internacionales. BIOCANN® trabaja activamente en acuerdos B2B para exportación de derivados de cannabis medicinal.",
        cta_text="Ser partner", cta_url="biocann.ar"
    )), BASE / "linkedin-25-28mayo-cierre-b2b.png", False, True))

posts.append((save("story-28mayo-5-motivos-teaser.html",
    story_monolith("story-28mayo", "STORY-28/05 · Los Cauces",
        eyebrow="LOS CAUCES® · 5 MOTIVOS",
        headline_lines=["5 motivos para", "visitar", "<em>Los Cauces.</em>"],
        subhead="Patagonia · Cultivo en vivo · Cannabis medicinal · Gastronomía regional · Naturaleza sin filtros.",
        cta_text="Reservar visita", cta_url="reservaloscauces.com"
    )), BASE / "story-28mayo-5-motivos-teaser.png", True, False))

# POST-026 Carrusel Los Cauces 5 motivos — 6 slides
slides_loscauces = [
    ("s01","feed-monolith", "LOS CAUCES® · 5 MOTIVOS",    ["5 motivos para", "visitar la", "<em>Reserva.</em>"],           "", "", "01 / 06"),
    ("s02","white-slide",   "MOTIVO 01 · PATAGONIA",      ["Entorno", "<em>único.</em>"],                                  "La Reserva Los Cauces está en Chubut, rodeada de cordillera. Naturaleza patagónica sin distancias.", "", "02 / 06"),
    ("s03","white-slide",   "MOTIVO 02 · CULTIVO",        ["Ves el cultivo", "<em>en vivo.</em>"],                         "Conocés el origen del producto. El proceso de cultivo cannabis bajo protocolo, en el campo.", "", "03 / 06"),
    ("s04","white-slide",   "MOTIVO 03 · EXPERIENCIA",    ["Cannabis", "medicinal con", "<em>contexto.</em>"],             "Educación, acceso regulado y experiencia integrada. No es turismo recreativo: es conocimiento.", "", "04 / 06"),
    ("s05","white-slide",   "MOTIVO 04 + 05",             ["Gastronomía.", "<em>Naturaleza.</em>"],                        "Cocina regional con ingredientes locales. Senderismo y paisaje patagónico como fondo de cada visita.", "", "05 / 06"),
    ("s06","feed-monolith", "LOS CAUCES® · RESERVAR",     ["La experiencia", "<em>comienza</em>", "en Patagonia."],        "Reservas limitadas por período. Consultá disponibilidad.", "Reservar →", "06 / 06"),
]
for i, (sid, kind, ey, hls, sub, cta_str, pag) in enumerate(slides_loscauces):
    fn = f"carrusel-26-28mayo-loscauces-{sid}.html"
    cta_t = cta_str.replace(" →","") if " →" in cta_str else ""
    cta_u = "reservaloscauces.com" if cta_t else ""
    html = feed_monolith(fn, f"POST-026 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag, marca="Los Cauces") if kind == "feed-monolith" \
           else carousel_slide_white(fn, f"POST-026 · Slide {sid}", ey, hls, sub, "", cta_t, cta_u, pag)
    posts.append((save(fn, html), BASE / fn.replace(".html",".png"), False, False))

posts.append((save("feed-27-29mayo-seguimiento.html",
    feed_photo_split("feed-27-29mayo", "POST-027 · Seguimiento",
        eyebrow="ACOMPAÑAMIENTO · SEGUIMIENTO",
        headline_lines=["El acompañamiento", "no termina con", "el primer", "<em>producto.</em>"],
        subhead="Seguimiento profesional continuo.",
        cta_text="Conocer", cta_url="biocann.ar/servicios",
        photo_src="../photos/gus01957.jpg"
    )), BASE / "feed-27-29mayo-seguimiento.png", False, False))

posts.append((save("story-29mayo-seguimiento.html",
    story_monolith("story-29mayo", "STORY-29/05 · Acompañamiento",
        eyebrow="ACOMPAÑAMIENTO PROFESIONAL",
        headline_lines=["Seguimiento", "<em>profesional.</em>", "Siempre."],
        subhead="Las coberturas BIOCANN® incluyen acompañamiento durante todo el tratamiento. No te dejamos solo después del primer envío.",
        cta_text="Ver coberturas", cta_url="biocann.ar/pricing-plans/list"
    )), BASE / "story-29mayo-seguimiento.png", True, False))

posts.append((save("story-30mayo-sistema-completo.html",
    story_monolith("story-30mayo", "POST-028 / STORY-30/05 · Sistema completo",
        eyebrow="COBERTURAS BIOCANN® · CONVERSIÓN",
        headline_lines=["El sistema", "completo,", "<em>tuyo.</em>"],
        subhead="Producto trazable + acompañamiento profesional + renovación asistida + envío documentado. Todo en Coberturas BIOCANN®.",
        cta_text="Iniciar acceso", cta_url="biocann.ar/pricing-plans/list"
    )), BASE / "story-30mayo-sistema-completo.png", True, False))

posts.append((save("story-31mayo-cierre-patagonia.html",
    story_monolith("story-31mayo", "STORY-31/05 · Cierre mayo",
        eyebrow="MAYO 2026 · CIERRE",
        headline_lines=["Un mes desde", "<em>Patagonia.</em>"],
        subhead="Cultivamos, procesamos, acompañamos. Mayo 2026. Gracias por ser parte del acceso regulado.",
        cta_text="Seguir BIOCANN", cta_url="biocann.ar"
    )), BASE / "story-31mayo-cierre-patagonia.png", True, False))

posts.append((save("feed-29-31mayo-resumen.html",
    feed_monolith("feed-29-31mayo", "POST-029 · Resumen mayo",
        eyebrow="RESUMEN MAYO 2026",
        headline_lines=["Mayo 2026.", "Un mes de trabajo", "desde", "<em>Patagonia.</em>"],
        subhead="Lotes despachados · Pacientes acompañados · Alianzas construidas · Sistema documentado.",
        cta_text="Conocer BIOCANN", cta_url="biocann.ar/nosotros"
    )), BASE / "feed-29-31mayo-resumen.png", False, False))

# ─────────────────────────────────────────────────────────────
# BUILD BATCH CONFIG
# ─────────────────────────────────────────────────────────────

jobs = []
for (html_path, png_path, is_story, is_linkedin) in posts:
    jobs.append({
        "html":    str(html_path),
        "png":     str(png_path),
        "story":   is_story,
        "linkedin": is_linkedin,
        "retina":  False,
    })

batch_path = BASE / "batch-mayo-2026.json"
batch_path.write_text(json.dumps({"jobs": jobs}, indent=2, ensure_ascii=False))
print(f"\n✓ {len(jobs)} jobs → {batch_path.name}")
print(f"  Correr: python3 render.py --config '{batch_path}'")

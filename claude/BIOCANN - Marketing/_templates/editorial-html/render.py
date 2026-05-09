#!/usr/bin/env python3
"""
BIOCANN® — Editorial Design System · Render Pipeline
Renderiza cualquier HTML del sistema a PNG 1080×1350 (feed) o 1080×1920 (story).
Soporta build:single, build:all y build desde un YAML/JSON config.

USO BÁSICO:
    python3 render.py layouts/feed-photo-split.html out.png
    python3 render.py layouts/story-monolith.html out.png --story
    python3 render.py layouts/feed-photo-split.html out.png --retina

USO BATCH:
    python3 render.py --config piezas.yaml          # genera todas las piezas del YAML

NOTAS:
- Las fuentes se cargan vía Google Fonts CDN (requiere internet la primera vez).
- device_scale_factor=1 produce PNG exact 1080×N. Con --retina usa device_scale_factor=2.
- Todos los assets relativos al HTML se resuelven correctamente.

Requiere: pip install playwright pyyaml && python3 -m playwright install chromium
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("ERROR: playwright no está instalado. Corré:")
    print("  pip install --user playwright && python3 -m playwright install chromium")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent

CANVAS_FEED     = (1080, 1350)
CANVAS_STORY    = (1080, 1920)
CANVAS_LINKEDIN = (1200, 628)


async def _render_one(page, html_path: Path, png_path: Path, canvas, scale: int):
    url = html_path.resolve().as_uri()
    await page.goto(url, wait_until="networkidle")
    await page.evaluate("document.fonts.ready")
    await page.wait_for_timeout(900)
    png_path.parent.mkdir(parents=True, exist_ok=True)
    await page.screenshot(
        path=str(png_path),
        clip={"x": 0, "y": 0, "width": canvas[0], "height": canvas[1]},
        type="png",
    )
    print(f"  ✓ {png_path.relative_to(ROOT) if str(png_path).startswith(str(ROOT)) else png_path}  ({canvas[0]}x{canvas[1]} @ {scale}x)")


async def render_one(html_path: Path, png_path: Path, story: bool = False, retina: bool = False, linkedin: bool = False):
    if linkedin:
        canvas = CANVAS_LINKEDIN
    elif story:
        canvas = CANVAS_STORY
    else:
        canvas = CANVAS_FEED
    scale = 2 if retina else 1
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": canvas[0], "height": canvas[1]},
            device_scale_factor=scale,
        )
        page = await context.new_page()
        await _render_one(page, html_path, png_path, canvas, scale)
        await browser.close()


async def render_batch(jobs):
    """jobs: list of dicts with keys html, png, story (bool), retina (bool)"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Group by canvas + scale to reuse contexts
        by_ctx = {}
        for j in jobs:
            if j.get("linkedin"):
                canvas = CANVAS_LINKEDIN
            elif j.get("story"):
                canvas = CANVAS_STORY
            else:
                canvas = CANVAS_FEED
            scale = 2 if j.get("retina") else 1
            key = (canvas, scale)
            by_ctx.setdefault(key, []).append(j)

        for (canvas, scale), group in by_ctx.items():
            ctx = await browser.new_context(
                viewport={"width": canvas[0], "height": canvas[1]},
                device_scale_factor=scale,
            )
            page = await ctx.new_page()
            print(f"\n[Context {canvas[0]}x{canvas[1]} @ {scale}x] — {len(group)} pieza(s)")
            for j in group:
                await _render_one(page, Path(j["html"]), Path(j["png"]), canvas, scale)
            await ctx.close()
        await browser.close()


def parse_args():
    ap = argparse.ArgumentParser(description="BIOCANN editorial design render")
    ap.add_argument("html", nargs="?", help="HTML source path")
    ap.add_argument("png",  nargs="?", help="PNG output path")
    ap.add_argument("--story", action="store_true", help="Use story canvas 1080×1920")
    ap.add_argument("--linkedin", action="store_true", help="Use LinkedIn canvas 1200×628")
    ap.add_argument("--retina", action="store_true", help="Render at 2x device pixel ratio")
    ap.add_argument("--config", help="JSON config with batch jobs")
    return ap.parse_args()


def main():
    args = parse_args()

    if args.config:
        cfg_path = Path(args.config).resolve()
        cfg = json.loads(cfg_path.read_text())
        # Resolve relative paths from the config's directory
        base = cfg_path.parent
        jobs = []
        for j in cfg.get("jobs", []):
            jobs.append({
                "html":    str((base / j["html"]).resolve()),
                "png":     str((base / j["png"]).resolve()),
                "story":   bool(j.get("story", False)),
                "retina":  bool(j.get("retina", False)),
                "linkedin": bool(j.get("linkedin", False)),
            })
        if not jobs:
            print("config sin jobs."); sys.exit(1)
        asyncio.run(render_batch(jobs))
    else:
        if not (args.html and args.png):
            print("uso: render.py <html> <png> [--story] [--retina]")
            sys.exit(1)
        asyncio.run(render_one(Path(args.html), Path(args.png), args.story, args.retina, args.linkedin))


if __name__ == "__main__":
    main()

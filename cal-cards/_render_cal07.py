import asyncio
from pathlib import Path
import shutil

async def render():
    from playwright.async_api import async_playwright

    html_path = Path("/Users/Leo/Claud Brain/BIOCANN - IA TEAM/claude/BIOCANN - Marketing/_renders/cal-cards/cal-07-faq.html").resolve()
    png_primary = Path("/Users/Leo/Claud Brain/BIOCANN - IA TEAM/claude/BIOCANN - Marketing/_renders/cal-cards/cal-07-faq.png")
    png_copy    = Path("/Users/Leo/Claud Brain/BIOCANN - IA TEAM/cal-cards/cal-07-faq.png")

    print(f"Rendering: {html_path}")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})
        await page.goto(f"file://{html_path}", wait_until="networkidle")
        await page.screenshot(path=str(png_primary), full_page=True)
        await browser.close()

    print(f"PNG guardado: {png_primary}")

    # copiar al directorio raíz cal-cards
    png_copy.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(png_primary, png_copy)
    print(f"PNG copiado: {png_copy}")

asyncio.run(render())

# BIOCANN® — Editorial HTML Templates

**Sistema oficial de templates editoriales para piezas BIOCANN.**
**Versión:** 1.0 · 2026-05-02
**Pipeline:** HTML/CSS + Playwright headless → PNG pixel-perfect

> Para el manual visual completo: `claude/BIOCANN - Marketing/brand kit/06_DESIGN_SYSTEM.md`

---

## 🗂️ Estructura

```
_templates/editorial-html/
├── tokens.css          ← Color, fuentes, spacing, tokens (single source)
├── components.css      ← Componentes reutilizables (.b-wordmark, .b-headline, etc)
├── render.py           ← Render pipeline (Playwright)
├── img/                ← Imágenes referencia / placeholder
└── layouts/
    ├── feed-photo-split.html      ← Foto top 60% + bloque verde 40% (Var 4 Aceites)
    ├── feed-monolith.html         ← Verde sólido institucional (Var 1)
    ├── feed-photo-overlay.html    ← Foto full bleed con gradient verde (Var 6)
    ├── story-photo-split.html     ← Story foto top + bloque verde
    └── story-monolith.html        ← Story verde sólido
```

---

## 🚀 Quick start

### 1. Crear pieza nueva

Copiar el layout que más se ajuste:

```bash
cp layouts/feed-photo-split.html mi-campana.html
```

### 2. Editar contenido

Abrir `mi-campana.html` y reemplazar los placeholders entre `[]`:

| Placeholder | Qué reemplazar |
|---|---|
| `[EYEBROW]` | Categoría uppercase (ej: "Coberturas Biocann® · Acceso regulado") |
| `[HEADLINE LINEA 1-4]` | 4 líneas del titular. Última línea con `<em>palabra</em>` para el acento italic. |
| `[SUBHEAD]` | Línea descriptiva en Space Grotesk |
| `[CTA TEXTO]` | Texto del botón (uppercase, ej: "Conocé los planes") |
| `[CTA URL]` | URL canónica BIOCANN (ej: "biocann.ar/pricing-plans/list") |
| `[PRODUCT TAG]` | Microcopy técnica del producto sobre la foto |
| `--photo-src` | URL/path de la foto en `:root { --photo-src: url('...'); }` |

### 3. Renderizar

```bash
# 1080x1350 exact (para upload IG)
python3 render.py mi-campana.html mi-campana.png

# 2160x2700 retina (para web/decks)
python3 render.py mi-campana.html mi-campana_2x.png --retina

# Story 1080x1920
python3 render.py mi-campana.html mi-campana.png --story
```

### 4. Batch render (varias piezas a la vez)

Crear `mi-config.json`:

```json
{
  "jobs": [
    { "html": "mi-feed.html",    "png": "out/mi-feed_1080.png" },
    { "html": "mi-feed.html",    "png": "out/mi-feed_2x.png", "retina": true },
    { "html": "mi-story.html",   "png": "out/mi-story.png", "story": true }
  ]
}
```

Y correr:

```bash
python3 render.py --config mi-config.json
```

---

## 🎨 Layouts disponibles

### `feed-photo-split.html` *(Var 4 Aceites)*
**Cuándo usarlo:** producto BIOCANN protagónico + mensaje fuerte. Conversión directa.
**Anatomía:** foto top 540×810 / hairline copper / bloque verde bottom con eyebrow + headline + hairline + subhead + CTA + footer.

### `feed-monolith.html` *(Var 1 Verde)*
**Cuándo usarlo:** awareness institucional, voz de marca, sin foto. Headline grande dominante.
**Anatomía:** Verde Bosque sólido con noise overlay sutil + tipografía como única protagonista.

### `feed-photo-overlay.html` *(Var 6 Patagonia)*
**Cuándo usarlo:** foto patagónica/lifestyle como heroína (paisaje, cultivo, cosecha). Foto full bleed.
**Anatomía:** foto full canvas + gradient overlay vertical → verde 92% en bottom 40% donde vive la tipografía.

### `story-photo-split.html` *(Story Var 4/5)*
**Cuándo usarlo:** Story refuerzo de un feed photo split. Mismo lenguaje, formato 9:16.
**Anatomía:** foto 1080×1180 + hairline + bloque verde 1080×740.

### `story-monolith.html`
**Cuándo usarlo:** Story de awareness puro. Headline 78pt dominante.

---

## 🧩 Componentes reutilizables (`components.css`)

Si necesitás componer un layout custom, todos los componentes están como CSS classes:

| Class | Descripción |
|---|---|
| `.b-canvas .b-canvas--feed` / `--story` | Wrapper de canvas con dimensiones exactas |
| `.b-top-bar` | Wordmark + coord en flex justify-between |
| `.b-wordmark` (`--light` / `--story`) | "BIOCANN®" tipografiado |
| `.b-coord` (`--light` / `--story`) | "42°08′S · 71°24′W · PATAGONIA" |
| `.b-eyebrow` (`--story`) | Categoría uppercase con tracking |
| `.b-headline` (`--xl` / `--lg` / `--md` / `--sm` / `--story` / `--dark`) | Titular Sora Light |
| `.b-hairline` (`--lg` / `--dark`) | Línea fina copper |
| `.b-subhead` (`--story` / `--dark`) | Subtítulo Space Grotesk |
| `.b-body` (`--dark`) | Texto body Inter |
| `.b-cta-pill` (`--dark` / `--story`) | Botón pill con border copper |
| `.b-footer` | Disclaimer + paginación |
| `.b-disclaimer` (`--dark`) | Disclaimer regulatorio |
| `.b-pagination` (`--dark`) | "01 / 01" |
| `.b-photo` + modifiers | Foto background con cover/position |
| `.b-divider` (`--dark`) | Línea horizontal copper full width |
| `.b-green-block` (`--story`) | Bloque Verde Bosque con padding y noise |
| `.b-photo-overlay` | Gradient overlay para layouts photo-overlay |
| `.b-content-bottom` | Posicionamiento absoluto bottom para overlay layouts |
| `.b-spacer` | Flex spacer para empujar CTA al fondo |

---

## 🎨 Tokens (`tokens.css`)

Para cambiar paleta o tipografía globalmente, editar `tokens.css`. **No hardcodees colores ni fuentes en los layouts** — siempre usar tokens (`var(--green)`, `var(--font-display)`, etc).

```css
:root {
  --green:        #2F4F3E;   /* Verde Bosque */
  --white-pat:    #F7F5F0;   /* Blanco Patagónico */
  --carbon:       #222A2B;
  --copper-light: #D6995E;
  --copper-base:  #B07A4A;
  --font-display:   'Sora', 'Telegraf', sans-serif;
  --font-microcopy: 'Space Grotesk', monospace;
  --font-body:      'Inter', 'Helvetica Neue', sans-serif;
}
```

### Cambiar fuentes a las oficiales (Telegraf + Helvetica Neue)

Cuando los OTF de Dropbox estén accesibles vía link público (ver gap en `feedback_design_pipeline.md`), agregar `@font-face` en `tokens.css`:

```css
@font-face {
  font-family: 'Telegraf';
  src: url('fonts/Telegraf-Light.otf') format('opentype');
  font-weight: 300;
}
/* ...idem Regular/Medium */
```

Las cadenas `--font-display` y `--font-body` ya tienen Telegraf y Helvetica Neue priorizados — el navegador los usa automáticamente cuando estén disponibles.

---

## 📋 Checklist por pieza nueva

Antes de exportar el PNG final, verificar:

- [ ] Texto de eyebrow no excede 60 caracteres
- [ ] Headline de 4 líneas sin viuda/huérfano
- [ ] Última línea del headline tiene `<em>palabra</em>` italic
- [ ] CTA URL es canónica (ver `06_DESIGN_SYSTEM.md §10`)
- [ ] Disclaimer regulatorio presente y legible
- [ ] Coordenadas patagónicas correctas (42°08′S · 71°24′W)
- [ ] Wordmark con `<sup>®</sup>`
- [ ] White space ratio ≥ 50%
- [ ] Sin emojis en la pieza (solo en captions)
- [ ] Compliance review (no promesas médicas, no recreativo)

---

## 🔧 Pipeline de aprobación

1. Diseñador IA / humano clona layout y completa contenido.
2. Render local con `python3 render.py`.
3. Brand-guardian-agent revisa contra `06_DESIGN_SYSTEM.md`.
4. Compliance-agent revisa contra `02_REGULATORY_GUARDRAILS.md`.
5. CMO aprueba.
6. Export final PNG (1x + 2x) a Dropbox `08. Biocann - Contenido Final/Aprobado/`.
7. Una vez publicado, mover a `Publicado/`.

---

## 🆘 Troubleshooting

**Las fuentes salen en system default:**
Las Google Fonts requieren conexión a internet en el primer render. Una vez cacheadas por Chromium, funcionan offline.

**El render queda en blanco:**
Verificá que la ruta de la foto en `--photo-src` sea relativa al HTML (no absoluta) y que el archivo exista en `img/`.

**El PNG sale más grande que 1080×N:**
Sin `--retina` el output es exact 1080×N. Con `--retina` es 2160×N (2x device pixel ratio).

**Quiero usar un formato distinto a feed/story:**
Editá las dimensiones en `tokens.css` (`.b-canvas--feed` y `.b-canvas--story`) o agregá una nueva clase modifier. El render acepta cualquier viewport via los flags pero por defecto usa 1080×1350 / 1080×1920.

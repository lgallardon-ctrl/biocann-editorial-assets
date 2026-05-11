# Protocolo de versiones — CAL Cards

## Estructura de carpetas

```
cal-cards/
├── cal-NN-nombre.png         ← versión activa aprobada
├── cal-NN-nombre.html        ← template fuente
└── _archivo/
    ├── cal-NN-nombre-v1.png  ← versión anterior
    ├── cal-NN-nombre-v2.png  ← versión anterior
    └── PROTOCOLO_VERSIONES.md
```

## Flujo obligatorio al generar una nueva versión

1. **Mover la versión activa a `_archivo/`** con sufijo `-vN` antes de sobreescribir
   - Ejemplo: `cal-04-coberturas.png` → `_archivo/cal-04-coberturas-v1.png`
2. **Guardar la nueva versión** en `cal-cards/` con el nombre base sin sufijo
3. **Commit y push** a `biocann-editorial-assets` (main)
4. **Actualizar Airtable** → campo `Media URL / Archivo final` con la nueva URL GitHub raw
5. **Una vez aprobada**: copiar a Dropbox `/Content Room.../08. Biocann - Contenido Final/Aprobado/`

## Convención de nombres en archivo

| Patrón | Ejemplo |
|---|---|
| `{id}-v{N}.png` | `cal-04-coberturas-v1.png` |
| `{id}-v{N}-{descripcion}.png` | `cal-04-coberturas-v1-laptop.png` |

## Versiones actuales registradas (mayo 2026)

| Card | Versión activa | Archivo |
|---|---|---|
| CAL-01 | v2 (auditada mayo 2026) | `cal-01-reprocann-v1.png` |
| CAL-02 | v2 (auditada mayo 2026) | `cal-02-trazabilidad-v1.png` |
| CAL-03 | v2 (auditada mayo 2026) | `cal-03-patagonia-v1.png` |
| CAL-04 | v2 (persona celu, 2026-05-11) | `cal-04-coberturas-v1-laptop.png` |
| CAL-05 | v2 (auditada mayo 2026) | `cal-05-full-spectrum-v1.png` |
| CAL-06 | v2 (auditada mayo 2026) | `cal-06-cultivo-v1.png` |
| CAL-07 | v2 (auditada mayo 2026) | `cal-07-faq-v1.png` |
| CAL-08 | v2 (auditada mayo 2026) | `cal-08-no-todo-igual-v1.png` |
| CAL-09 | v2 (auditada mayo 2026) | `cal-09-loscauces-v1.png` |

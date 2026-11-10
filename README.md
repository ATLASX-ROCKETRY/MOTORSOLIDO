# Atlas X — Propulsión

Diseño de un motor cohete de propelente sólido (grano BATES) para el cohete Atlas X.

## Misión

| Requisito | Valor |
|---|---|
| Masa al despegue (incluye motor cargado) | 10 kg |
| Apogeo objetivo | 1000 m |
| Diámetro del fuselaje | 150 mm |

## Contenido

| Archivo | Qué hace |
|---|---|
| [`docs/01_mision_a_geometria.md`](docs/01_mision_a_geometria.md) | Cadena de ecuaciones en símbolos: de la misión a las longitudes del grano (pasos 1–12) |
| [`scripts/vuelo.py`](scripts/vuelo.py) | Pasos 1–5: simulación de vuelo 1D → impulso requerido y masa de propelente |
| [`scripts/dimensionar.py`](scripts/dimensionar.py) | Pasos 6–12: presupuesto de masa → D, d₀, L₀, w y dimensiones del tubo |

Ejecutar (solo Python estándar):

```bash
python3 scripts/vuelo.py
python3 scripts/dimensionar.py
```

## Resultados preliminares

| Magnitud | Valor |
|---|---|
| Impulso requerido (C_d = 0.5) | ~1830 N·s |
| Impulso de diseño (+20 % margen) | ~2200 N·s (clase K) |
| Masa de propelente | ~2.16 kg |
| Masa del motor (ζ = 0.5 supuesto) | ~4.3 kg |
| Grano (N = 4, k = 0.5) | D ≈ 67 mm, d₀ ≈ 34 mm, L₀ ≈ 118 mm |

> ⚠️ **Provisional.** ρ_p e I_sp son estimaciones para un propelente tipo KN.
> k, N y ζ todavía no están validados: requieren el modelo de cámara (volumen de
> control), que es la siguiente etapa.

## Estado

- [x] Misión → impulso → masa de propelente
- [x] Presupuesto de masa (preliminar)
- [x] Geometría del grano (longitudes)
- [ ] Modelo de cámara: P(t), Kn, garganta, verificación de G y A_núcleo/A_t
- [ ] Tobera
- [ ] Carcasa: espesor de pared, tapas, validación de ζ

## Seguridad

Un motor clase K es cohetería de alta potencia. Antes de cualquier vuelo hacen falta:
pruebas estáticas en banco con distancia de seguridad, prueba hidrostática de la
carcasa y los permisos que exija la normativa local.

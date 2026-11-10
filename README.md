# Atlas X — Propulsión

Diseño de un motor cohete de propelente sólido para el cohete Atlas X.

## Contenido

### Ecuaciones (solo símbolos)

| Archivo | Qué contiene |
|---|---|
| [`docs/01_mision_a_geometria.md`](docs/01_mision_a_geometria.md) | Cadena de ecuaciones: de la misión a las longitudes del grano BATES (pasos 1–12) |
| [`docs/02_numero_de_granos.md`](docs/02_numero_de_granos.md) | Cómo se define el número de segmentos N: mínimo por volumen, máximo por flujo másico, espacio |
| [`docs/03_geometria_finocyl.md`](docs/03_geometria_finocyl.md) | Ecuaciones del grano Finocyl (reemplazan a los pasos 8–11) |

### Ejemplos aplicados (hasta el paso 12)

Misión: 10 kg al despegue (con motor), 1000 m de apogeo, fuselaje de 150 mm, propelente KNSB.

| Archivo | Qué contiene |
|---|---|
| [`ejemplos/00_mision_comun.md`](ejemplos/00_mision_comun.md) | Pasos 1–5 y 7, iguales para los tres ejemplos |
| [`ejemplos/ejemplo_1_bates_acero304.md`](ejemplos/ejemplo_1_bates_acero304.md) | BATES + acero AISI 304 |
| [`ejemplos/ejemplo_2_bates_al6061.md`](ejemplos/ejemplo_2_bates_al6061.md) | BATES + aluminio 6061-T6 |
| [`ejemplos/ejemplo_3_finocyl_acero304.md`](ejemplos/ejemplo_3_finocyl_acero304.md) | Finocyl + acero AISI 304 |

### Scripts (Python 3 + numpy)

```bash
python3 scripts/comun.py                    # misión común
python3 scripts/ejemplo_bates.py acero304   # ejemplo 1
python3 scripts/ejemplo_bates.py al6061     # ejemplo 2
python3 scripts/ejemplo_finocyl.py          # ejemplo 3 (~25 s, búsqueda de geometría)
```

## Resumen de resultados

Común: impulso de diseño 2191 N·s (clase K), 2.148 kg de propelente, 1228 cm³.

| | Ej. 1: BATES + 304 | Ej. 2: BATES + 6061 | Ej. 3: Finocyl + 304 |
|---|---|---|---|
| Grano | 4 × (D 66.8, d₀ 33.4, L₀ 116.9 mm) | igual al ej. 1 | 1 × (D 66.8, r_c 20, 10 aletas 4×4 mm) |
| Tubo: diámetro interior | 69.3 mm | 69.3 mm | 69.3 mm |
| Largo de grano | 473 mm | 473 mm | 589 mm |
| Neutralidad | 7.5 % | 7.5 % | 3.5 % |
| ζ supuesto | 0.40 | 0.55 | 0.40 |
| Margen de masa | **−0.32 kg ❌** | **+1.14 kg ✅** | **−0.32 kg ❌** (≈ −0.8 por el largo extra) |

Para que el cohete no supere 10 kg, el motor debe lograr **ζ ≥ 0.425**
(estructura ≤ 2.90 kg).

> ⚠️ ζ es un supuesto. Se verifica en la etapa siguiente (modelo de cámara →
> P_max → espesor de pared con SF 1.5–2 → masa real de la carcasa).

## Estado

- [x] Ecuaciones: misión → geometría (BATES y Finocyl)
- [x] Ejemplos 1–3 hasta el paso 12
- [ ] Modelo de cámara: P(t), Kn, garganta
- [ ] Carcasa: espesor de pared, tapas, ζ real
- [ ] Tobera

## Seguridad

Un motor de alta potencia requiere, antes de cualquier vuelo: pruebas estáticas en
banco con distancia de seguridad, prueba hidrostática de la carcasa y los permisos
que exija la normativa local.

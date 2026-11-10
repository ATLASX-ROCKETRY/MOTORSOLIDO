# Ejemplo 3 — Grano Finocyl + carcasa de acero AISI 304

Pasos 6 y 12 de [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md).
Los pasos 8–11 se reemplazan por las ecuaciones del Finocyl de
[`docs/03_geometria_finocyl.md`](../docs/03_geometria_finocyl.md).
Los pasos 1–5 y 7 están en [`00_mision_comun.md`](00_mision_comun.md).

Cálculo: `python3 scripts/ejemplo_finocyl.py`

---

## Datos de entrada

| Dato | Valor |
|---|---|
| $m_p$ | 2.148 kg |
| $V_p$ | 1228 cm³ |
| $\rho_p$ (KNSB) | 1749 kg/m³ |
| Material | AISI 304: $\sigma_y$ ~205 MPa, ~8000 kg/m³ (igual que el [ejemplo 1](ejemplo_1_bates_acero304.md)) |

**Decisión de comparación:** se usa el **mismo diámetro de grano que el BATES**
($D = 66.8$ mm, tubo de 69.3 mm de diámetro interior). Así la única variable que
cambia respecto del ejemplo 1 es la geometría del grano.

## Paso 6 — Presupuesto de masa

Con el mismo supuesto del ejemplo 1 ($\zeta = 0.40$):

$$\text{margen} = -0.32\ \text{kg} \;\Rightarrow\; \text{el presupuesto NO cierra}$$

Como se ve en el paso 12, el Finocyl resulta **25 % más largo** que el BATES, así que
su carcasa de acero pesará más y $\zeta$ será **menor** que en el ejemplo 1. Una
estimación gruesa (suponiendo que el tubo es ~60 % de la estructura y que su masa
crece con el largo) da $\zeta \approx 0.37$ y un margen de **≈ −0.8 kg**. Es solo
una indicación del sentido del efecto; el valor real sale de la etapa de carcasa.

## F1–F3 — Geometría y largo

Se buscaron combinaciones de $n_f \in \{4, 6, 8, 10, 12\}$,
$w_f \in \{3, 4, 6\}$ mm, $r_c$ de 4 a 22 mm y $R_f$ desde $r_c + 2$ mm hasta 3 mm de la pared:

- **Objetivo:** mínima variación de $A_b$ entre el 0 y el 90 % de la masa quemada.
- **Restricción:** $G_{final} \le 1400$ kg/m²s, con $r = 7.76$ mm/s (meseta KNSB).

Mejores candidatos:

| $\varepsilon$ | $n_f$ | $w_f$ [mm] | $r_c$ [mm] | $R_f$ [mm] | $L$ [mm] | $G_{final}$ [kg/m²s] |
|---|---|---|---|---|---|---|
| **3.5 %** | **10** | **4** | **20** | **24** | **589** | **1206** |
| 4.0 % | 12 | 3 | 22 | 26 | 668 | 1276 |
| 4.0 % | 10 | 6 | 22 | 26 | 706 | 1244 |
| 5.6 % | 10 | 3 | 20 | 24 | 578 | 1236 |
| 7.8 % | 10 | 3 | 18 | 22 | 520 | 1287 |

**Diseño elegido:** 10 aletas de 4 mm de ancho y 4 mm de largo, sobre un núcleo de
radio 20 mm.

$$A_{port,0} = \pi (20)^2 + 10 \times 4 \times 4 = 1418\ \text{mm}^2$$

$$A_{prop} = \frac{\pi}{4}(66.8)^2 - 1418 = 2087\ \text{mm}^2 \qquad \lambda = 59.5\ \%$$

$$L = \frac{V_p}{A_{prop}} = \frac{1\,228\,000}{2087} = 589\ \text{mm} \qquad (L/D = 8.8)$$

## F4–F6 — Regresión y área de quemado

| Masa quemada | x [mm] | $A_b$ [mm²] |
|---|---|---|
| 0 % | 0.1 | 122 242 |
| 20 % | 2.1 | 122 618 |
| 40 % | 4.1 | 124 075 |
| 60 % | 6.0 | 126 719 |
| 80 % | 8.0 | 124 804 |
| 90 % | 9.0 | 126 711 |
| 95 % | 9.5 | 68 775 |
| 98 % | 10.1 | 39 942 |

- **Variación (0–90 %): 3.5 %**, menos de la mitad que el BATES (7.5 %).
- Web en la punta de la aleta: $33.4 - 24 = 9.4$ mm. Ahí la llama toca la pared.
- $x_{max} = 11.4$ mm. Entre 9.4 y 11.4 mm se quema el **5 % de la masa** remanente
  entre aletas (la cola).
- Tiempo de combustión: ~1.2 s para el 95 % de la masa, ~1.5 s en total.
  Empuje medio ≈ 1500–1800 N. El impulso necesario casi no cambia (paso 4).

**Por qué es neutro:** el núcleo de 20 mm es progresivo (su perímetro crece al
quemar); las 10 aletas cortas aportan perímetro al inicio y lo pierden al
redondearse. Las dos tendencias se compensan.

**Verificación de flujo:**

$$G_{final} = \frac{1749 \times 0.00776 \times 126\,814 \times 10^{-6}}{1418 \times 10^{-6}} \approx 1214\ \text{kg/m}^2\text{s} \le 1400 \;✅$$

## Paso 12 — Dimensiones del tubo del motor

$$D_{int,c} = 66.8 + 2(1.0) + 2(0.25) = 69.3\ \text{mm}$$

$$L_{grano} = 589\ \text{mm} \quad(\text{un solo grano, sin separaciones}) \;+\; \text{tapas}$$

## Comparación con el ejemplo 1 (mismo acero, mismo diámetro)

| | BATES (ej. 1) | Finocyl (ej. 3) |
|---|---|---|
| Neutralidad | 7.5 % | **3.5 %** |
| Carga volumétrica | **74 %** | 59.5 % |
| Largo de grano | **473 mm** | 589 mm (+25 %) |
| $A_b$ típica | ~73 000 mm² | ~124 000 mm² (+70 %) |
| $t_b$ | 2.15 s | ~1.2–1.5 s |
| $G_{final}$ prelim. | 1167 | 1214 |
| Fabricación | 4 granos simples | 1 grano largo con macho de 10 aletas |
| Masa de carcasa (acero) | menor | **mayor** (tubo más largo) |

**Lectura de ingeniería:** el Finocyl gana en neutralidad, pero la paga con volumen.
Necesita un puerto grande para mantener G bajo control, y por eso carga menos
propelente por sección y resulta más largo. Con acero, ese largo extra empeora un
presupuesto de masa que ya no cerraba. Además, su $A_b$ es ~70 % mayor, así que a
igual presión necesitará una garganta ~70 % más grande y dará un empuje más alto
y corto.

## Resultado

| Magnitud | Valor |
|---|---|
| Grano | Finocyl, 1 grano, extremos inhibidos |
| $D$ / $r_c$ / $R_f$ | 66.8 / 20 / 24 mm |
| Aletas | 10 × (4 mm ancho × 4 mm largo) |
| Diámetro interior del tubo | ≥ 69.3 mm |
| Largo de grano | 589 mm |
| Neutralidad | 3.5 % (0–90 % de masa) |
| Presupuesto de masa | **no cierra** (ζ = 0.40 → −0.32 kg; estimado ≈ −0.8 kg por el largo extra) |

**Pendiente (etapa de carcasa):** el mismo análisis del ejemplo 1, con tubo más largo.
Fabricación: las aletas de 4 mm exigen un macho (mandril) preciso. Una tolerancia
de ±0.5 mm en las aletas cambia la neutralidad de forma apreciable (ver en la tabla
de candidatos cómo pasar de $w_f$ = 4 a 3 mm sube ε de 3.5 a 5.6 %).

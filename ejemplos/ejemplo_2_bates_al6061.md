# Ejemplo 2 — Grano BATES + carcasa de aluminio 6061-T6

Pasos 6 y 8–12 de [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md),
con el número de granos según [`docs/02_numero_de_granos.md`](../docs/02_numero_de_granos.md).
Los pasos 1–5 y 7 están en [`00_mision_comun.md`](00_mision_comun.md).

Cálculo: `python3 scripts/ejemplo_bates.py al6061`

> **Nota de método.** Hasta el paso 12, el material entra **solo** en el paso 6, a
> través de $\zeta$. La geometría del grano (pasos 8–12) es **idéntica** a la del
> [ejemplo 1](ejemplo_1_bates_acero304.md). La diferencia real entre materiales
> (espesor de pared, masa, temperatura admisible) aparece en la etapa de carcasa.

---

## Datos de entrada

| Dato | Valor |
|---|---|
| $m_p$ | 2.148 kg |
| $V_p$ | 1228 cm³ |
| $\rho_p$ (KNSB) | 1749 kg/m³ |

**Material** (se usa en la etapa de carcasa; aquí solo entra a través de $\zeta$):

| Propiedad | Al 6061-T6 |
|---|---|
| Límite elástico $\sigma_y$ | ~276 MPa |
| Resistencia última $\sigma_u$ | ~310 MPa |
| Densidad | ~2700 kg/m³ |
| Resistencia específica $\sigma_y/\rho$ | ~102 kN·m/kg (≈ 4 veces la del acero 304) |
| Limitación | pierde resistencia rápido por encima de ~150 °C: depende del liner |

## Paso 6 — Presupuesto de masa

Fracción de propelente supuesta para una carcasa de aluminio: $\zeta = 0.55$
(rango típico de motores amateur de aluminio: 0.50–0.60).

$$m_{motor} = \frac{2.148}{0.55} = 3.91\ \text{kg} \quad(\text{estructura del motor: } 1.76\ \text{kg})$$

$$m_{resto,disp} = 10 - 3.91 = 6.09\ \text{kg} \quad>\quad m_{resto,nec} = 4.95\ \text{kg}$$

$$\boxed{\text{margen} = +1.14\ \text{kg} \;\Rightarrow\; \text{el presupuesto cierra}}$$

Sensibilidad:

| $\zeta$ | Margen |
|---|---|
| 0.50 | +0.75 kg |
| **0.55** | **+1.14 kg** |
| 0.60 | +1.47 kg |

Incluso en el extremo pesimista (ζ = 0.50), el presupuesto cierra con 0.75 kg de
margen. Ese margen puede usarse para carga útil o para un liner más grueso, que
protege mejor al aluminio del calor.

**Requisito derivado para la etapa de carcasa:** $\zeta \ge 0.425$, es decir, una
estructura de **2.90 kg como máximo**. El supuesto (1.76 kg) deja holgura amplia.

## Pasos 8–11 — Geometría

Iguales al ejemplo 1: BATES con $k = 0.5$ y $L_0 = (3D + d_0)/2$.

| N | D [mm] | d₀ [mm] | L₀ [mm] | w [mm] | D_int [mm] | Largo granos [mm] | G_final prelim. [kg/m²s] |
|---|---|---|---|---|---|---|---|
| 2 | 84.1 | 42.1 | 147.2 | 21.0 | 86.6 | 296 | 584 |
| 3 | 73.5 | 36.8 | 128.6 | 18.4 | 76.0 | 390 | 875 |
| **4** | **66.8** | **33.4** | **116.9** | **16.7** | **69.3** | **473** | **1167** |
| 5 | 62.0 | 31.0 | 108.5 | 15.5 | 64.5 | 550 | 1459 ❌ |
| 6 | 58.3 | 29.2 | 102.1 | 14.6 | 60.8 | 623 | 1751 ❌ |

**Elección: N = 4**, por el mismo criterio del ejemplo 1: es el máximo N con
$G \le 1400$ kg/m²s, y da el motor más delgado.

**Curva de área de quemado:**

| x [mm] | 0 | 3.34 | 6.68 | 10.02 | 13.36 | 16.70 |
|---|---|---|---|---|---|---|
| $A_b$ [mm²] | 70 058 | 73 421 | 75 102 | 75 102 | 73 421 | 70 058 |

Neutralidad 7.5 %; $t_b = 2.15$ s.

## Paso 12 — Dimensiones del tubo del motor

$$D_{int,c} = 69.3\ \text{mm} \qquad L_{granos} = 473\ \text{mm} \quad(+\ \text{tapas})$$

## Resultado

| Magnitud | Valor |
|---|---|
| Grano | BATES, N = 4 |
| $D$ / $d_0$ / $L_0$ / $w$ | 66.8 / 33.4 / 116.9 / 16.7 mm |
| Diámetro interior del tubo | ≥ 69.3 mm |
| Largo de granos | 473 mm |
| Neutralidad | 7.5 % |
| $t_b$ (meseta) | 2.15 s |
| Presupuesto de masa | **cierra con ζ = 0.55** (+1.14 kg) |

**Pendiente (etapa de carcasa):** espesor de pared con $\sigma_y = 276$ MPa (reducido
por temperatura) y SF 1.5–2, espesor del liner necesario para mantener el aluminio
por debajo de ~150 °C, masa real y verificación de $\zeta$.

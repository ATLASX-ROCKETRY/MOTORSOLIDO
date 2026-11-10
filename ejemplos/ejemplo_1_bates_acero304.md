# Ejemplo 1 — Grano BATES + carcasa de acero AISI 304

Pasos 6 y 8–12 de [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md),
con el número de granos según [`docs/02_numero_de_granos.md`](../docs/02_numero_de_granos.md).
Los pasos 1–5 y 7 están en [`00_mision_comun.md`](00_mision_comun.md).

Cálculo: `python3 scripts/ejemplo_bates.py acero304`

---

## Datos de entrada

| Dato | Valor |
|---|---|
| $m_p$ | 2.148 kg |
| $V_p$ | 1228 cm³ |
| $\rho_p$ (KNSB) | 1749 kg/m³ |

**Material** (se usa en la etapa de carcasa; aquí solo entra a través de $\zeta$):

| Propiedad | AISI 304 (recocido) |
|---|---|
| Límite elástico $\sigma_y$ | ~205 MPa |
| Resistencia última $\sigma_u$ | ~515 MPa |
| Densidad | ~8000 kg/m³ |
| Resistencia específica $\sigma_y/\rho$ | ~26 kN·m/kg |

## Paso 6 — Presupuesto de masa

Fracción de propelente supuesta para una carcasa de acero: $\zeta = 0.40$
(rango típico de motores amateur de acero: 0.35–0.45).

$$m_{motor} = \frac{2.148}{0.40} = 5.37\ \text{kg} \quad(\text{estructura del motor: } 3.22\ \text{kg})$$

$$m_{resto,disp} = 10 - 5.37 = 4.63\ \text{kg} \quad<\quad m_{resto,nec} = 4.95\ \text{kg}$$

$$\boxed{\text{margen} = -0.32\ \text{kg} \;\Rightarrow\; \text{el presupuesto NO cierra}}$$

Sensibilidad:

| $\zeta$ | Margen |
|---|---|
| 0.35 | −1.09 kg |
| **0.40** | **−0.32 kg** |
| 0.45 | +0.28 kg |

**Requisito derivado para la etapa de carcasa:** el motor de acero debe lograr
$\zeta \ge 0.425$, es decir, una estructura (carcasa + tapas + tobera + liner) de
**2.90 kg como máximo**. Si no lo logra, hay que aligerar el resto del cohete o
aceptar un apogeo menor.

El presupuesto no cierra, pero el ejemplo sigue con la geometría: el grano no depende
del material, y el número real de $\zeta$ solo se conocerá en la etapa de carcasa.

## Pasos 8–9 — Geometría BATES y neutralidad

$$A_{b,seg}(x) = \pi(d_0+2x)(L_0-2x) + \frac{\pi}{2}\left[D^2 - (d_0+2x)^2\right]$$

$$L_0 = \frac{3D + d_0}{2}$$

## Paso 10 — Núcleo

$$k = 0.5 \;\Rightarrow\; d_0 = 0.5\,D$$

## Paso 11 — Diámetro y número de segmentos

$$D = \left[\frac{8\,V_p}{\pi\,N\,(1-k^2)(3+k)}\right]^{1/3}$$

| N | D [mm] | d₀ [mm] | L₀ [mm] | w [mm] | D_int [mm] | Largo granos [mm] | G_final prelim. [kg/m²s] |
|---|---|---|---|---|---|---|---|
| 2 | 84.1 | 42.1 | 147.2 | 21.0 | 86.6 | 296 | 584 |
| 3 | 73.5 | 36.8 | 128.6 | 18.4 | 76.0 | 390 | 875 |
| **4** | **66.8** | **33.4** | **116.9** | **16.7** | **69.3** | **473** | **1167** |
| 5 | 62.0 | 31.0 | 108.5 | 15.5 | 64.5 | 550 | 1459 ❌ |
| 6 | 58.3 | 29.2 | 102.1 | 14.6 | 60.8 | 623 | 1751 ❌ |

**G preliminar** con $r = 7.76$ mm/s (meseta KNSB a 2.5 MPa):

$$G_{final} = \frac{\rho_p\,r\,A_{b,max}}{\frac{\pi}{4}d_0^2}$$

**Elección: N = 4.**
- $N_{max} = 4$: con N = 5, G supera 1400 kg/m²s (riesgo de combustión erosiva).
- Se elige el **máximo N permitido** porque da el motor más delgado. A igual volumen,
  la masa del tubo cambia poco con D, pero las tapas crecen fuerte con el diámetro.
  Con acero, cada gramo cuenta.

**Curva de área de quemado** (N = 4):

| x [mm] | 0 | 3.34 | 6.68 | 10.02 | 13.36 | 16.70 |
|---|---|---|---|---|---|---|
| $A_b$ [mm²] | 70 058 | 73 421 | 75 102 | 75 102 | 73 421 | 70 058 |

- $A_b(0) = A_b(w)$: la neutralidad se cumple exactamente.
- Variación máxima: **7.5 %** (sube en el medio y baja simétrica).
- Tiempo de combustión estimado: $t_b = w/r = 16.7 / 7.76 = 2.15$ s.
- Coherencia con el paso 4: empuje medio ≈ 2191 / 2.15 ≈ 1020 N, y el impulso
  necesario casi no depende del empuje.

## Paso 12 — Dimensiones del tubo del motor

Liner $e_{liner} = 1.0$ mm, holgura $\delta = 0.25$ mm, separación $s = 2$ mm.

$$D_{int,c} = 66.8 + 2(1.0) + 2(0.25) = 69.3\ \text{mm}$$

$$L_{granos} = 4(116.9) + 3(2) = 473\ \text{mm} \quad(+\ \text{tapas, en la etapa de carcasa})$$

Cabe sobrado en el fuselaje de 150 mm.

## Resultado

| Magnitud | Valor |
|---|---|
| Grano | BATES, N = 4 |
| $D$ / $d_0$ / $L_0$ / $w$ | 66.8 / 33.4 / 116.9 / 16.7 mm |
| Diámetro interior del tubo | ≥ 69.3 mm |
| Largo de granos | 473 mm |
| Neutralidad | 7.5 % |
| $t_b$ (meseta) | 2.15 s |
| Presupuesto de masa | **no cierra con ζ = 0.40** (−0.32 kg); exige ζ ≥ 0.425 |

**Pendiente (etapa de carcasa):** P_max con el modelo de cámara, espesor de pared con
$\sigma_y = 205$ MPa y SF 1.5–2, masa real y verificación de $\zeta$. El tubo comercial
concreto se elige ahí: si su diámetro interior difiere de 69.3 mm, se recalcula N
con la ruta B de `02_numero_de_granos.md`.

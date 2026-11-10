# Misión común — pasos 1–5 y 7

Estos pasos **no dependen ni del grano ni del material de la carcasa**: el impulso
lo exigen la masa, el apogeo y el arrastre. Se calculan una vez y los usan los tres
ejemplos.

Ecuaciones: [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md).
Cálculo: `python3 scripts/comun.py`.

---

## Paso 1 — Requisitos

| Símbolo | Valor |
|---|---|
| $m_0$ | 10 kg (incluye el motor cargado) |
| $h_{ap}$ | 1000 m |
| $D_{cohete}$ | 150 mm |
| $(F/W)_{min}$ | 5 → $\bar F \ge 5 \times 10 \times 9.81 = 490$ N |

## Propelente: KNSB (65 % KNO₃ / 35 % sorbitol)

| Propiedad | Valor | Origen |
|---|---|---|
| $I_{sp}$ | 104 s | modelo termoquímico previo (conservador) |
| $\rho_{ideal}$ | 1841 kg/m³ | teórico |
| $\rho_p$ | 1749 kg/m³ | 95 % del ideal (grano colado real) |
| $r = aP^n$ | por tramos (tabla abajo) | datos experimentales de R. Nakka |

| P [MPa] | a [mm/s·MPaⁿ] | n |
|---|---|---|
| 0.10–0.81 | 10.708 | 0.625 |
| 0.81–1.50 | 8.763 | −0.314 |
| **1.50–3.79** | **7.852** | **−0.013** |
| 3.79–7.03 | 3.907 | 0.535 |
| 7.03–10.67 | 9.653 | 0.064 |

En la **meseta** (1.5–3.8 MPa), $n \approx 0$: a 2.5 MPa, $r = 7.76$ mm/s, y casi no
cambia con la presión. Los tres ejemplos suponen que el motor opera en la meseta.
El modelo de cámara lo verificará.

## Paso 2 — Velocidad necesaria (sin aire)

$$v_b = \sqrt{2 \times 9.81 \times 1000} = 140\ \text{m/s}$$

## Paso 3 — Estimación a mano

$$I \approx m_0 v_b + m_0 g t_b = 10 \times 140 + 98.1 \times 2.3 \approx 1625\ \text{N·s}$$

## Paso 4 — Vuelo con arrastre

Supuestos: $C_d = 0.5$, $\bar F = 800$ N, $\rho_0 = 1.225$ kg/m³ (nivel del mar,
conservador), $H = 8500$ m.

| $C_d$ | $I_{req}$ [N·s] | $v_{max}$ [m/s] | $m_p$ [kg] | $t_b$ [s] |
|---|---|---|---|---|
| 0.4 | 1723 | 159 | 1.69 | 2.15 |
| **0.5** | **1826** | **166** | **1.79** | **2.28** |
| 0.6 | 1936 | 173 | 1.90 | 2.42 |

El empuje medio casi no influye: con 600, 800 y 1200 N se necesitan 1840, 1826 y
1812 N·s. Por eso los ejemplos pueden tener distinto $t_b$ sin rehacer este paso.

La estimación a mano (1625) queda 11 % por debajo: es la pérdida por arrastre.

## Paso 5 — Margen y propelente

$$I_{dis} = 1.20 \times 1826 = 2191\ \text{N·s} \quad(\text{clase K})$$

$$m_p = \frac{2191}{104 \times 9.80665} = 2.148\ \text{kg}$$

Apogeo nominal con $I_{dis}$: **1258 m**. El exceso sobre 1000 m es el margen.

## Paso 7 — Volumen de propelente

$$V_p = \frac{2.148}{1749} = 1228\ \text{cm}^3$$

## Presupuesto del resto del cohete (entra al paso 6 de cada ejemplo)

| Componente | Masa |
|---|---|
| Tubo de fuselaje (~1.3 m, fibra de vidrio) | 1.75 kg |
| Cono de nariz | 0.70 kg |
| Aletas | 0.60 kg |
| Soporte del motor | 0.50 kg |
| Recuperación | 0.90 kg |
| Aviónica | 0.50 kg |
| **Total necesario** | **4.95 kg** |

**Paracaídas** (descenso a 5.5 m/s, $m_{desc} = 10 - 2.148 = 7.85$ kg, $C_{D,par} = 1.5$):

$$A_{par} = \frac{2 \times 7.85 \times 9.81}{1.225 \times 1.5 \times 5.5^2} = 2.77\ \text{m}^2 \;\Rightarrow\; \varnothing = 1.88\ \text{m}$$

**Fracción de propelente mínima** para que el presupuesto cierre:

$$\zeta_{min} = \frac{m_p}{m_0 - m_{resto}} = \frac{2.148}{10 - 4.95} = 0.425$$

Cualquier motor con $\zeta < 0.425$ hace que el cohete supere los 10 kg.

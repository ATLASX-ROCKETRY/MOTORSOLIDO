# De la misión al impulso requerido — cadena de ecuaciones

Cadena de ecuaciones, **solo en símbolos**, desde los requisitos de la misión hasta
el impulso total requerido (pasos 1–4).

**Convención:**
- 🟦 = decisión de diseño
- 🟨 = propiedad del propelente (dato de entrada)
- sin marca = se calcula

---

## Paso 1 — Requisitos de la misión

| Símbolo | Significado |
|---|---|
| 🟦 $m_0$ | masa total al despegue (incluye el motor cargado) |
| 🟦 $h_{ap}$ | apogeo objetivo |
| 🟦 $D_{cohete}$ | diámetro del fuselaje |
| 🟦 $(F/W)_{min}$ | relación empuje/peso mínima para salir estable del riel |

## Paso 2 — Velocidad necesaria (cota inferior, sin aire)

La energía cinética en el apagado se convierte en altura:

$$\tfrac{1}{2}v_b^2 = g\,(h_{ap} - h_b) \quad\Rightarrow\quad v_b = \sqrt{2g\,(h_{ap}-h_b)}$$

- $v_b$: velocidad en el apagado del motor
- $h_b$: altura ganada durante la combustión

## Paso 3 — Impulso necesario (estimación a mano)

Ecuación de Tsiolkovsky con pérdida por gravedad:

$$\Delta v = I_{sp}\,g_0\,\ln\!\left(\frac{m_0}{m_0 - m_p}\right) - g\,t_b$$

Impulso total:

$$I = \bar F\,t_b = m_p\,I_{sp}\,g_0$$

Estimación rápida (cantidad de movimiento + gravedad):

$$I \approx m_0\,v_b + m_0\,g\,t_b$$

- 🟨 $I_{sp}$: impulso específico (de la termoquímica del propelente)
- $\bar F$: empuje medio
- $t_b$: tiempo de combustión
- $m_p$: masa de propelente

## Paso 4 — Impulso necesario (vuelo con arrastre, integración numérica)

$$\frac{dh}{dt} = v$$

$$m(t)\,\frac{dv}{dt} = F(t) - \tfrac{1}{2}\rho(h)\,C_d\,A_{ref}\,v\,|v| - m(t)\,g$$

$$\frac{dm}{dt} = -\frac{F(t)}{I_{sp}\,g_0}\quad (t<t_b), \qquad 0\quad (t\ge t_b)$$

$$A_{ref} = \frac{\pi}{4}D_{cohete}^2 \qquad \rho(h) = \rho_0\,e^{-h/H}$$

- $C_d$: coeficiente de arrastre del cohete
- $\rho_0$: densidad del aire en el sitio de lanzamiento
- $H$: altura de escala de la atmósfera

**Cierre:** se busca el $I$ tal que $h = h_{ap}$ cuando $v = 0$.

**Restricción de empuje:**

$$\bar F \ge (F/W)_{min}\,m_0\,g$$

Implementación: [`scripts/vuelo.py`](../scripts/vuelo.py).

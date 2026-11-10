# De la misión a la geometría del grano — cadena de ecuaciones

Cadena completa, **solo en símbolos**, desde los requisitos de la misión hasta las
longitudes del grano BATES. Se detiene **antes** del volumen de control de la cámara
(no aparecen presión de cámara, Kn ni garganta).

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

## Paso 5 — Margen y masa de propelente

$$I_{dis} = (1+\mu)\,I_{req} \qquad m_p = \frac{I_{dis}}{I_{sp}\,g_0}$$

- 🟦 $\mu$: margen de diseño (incertidumbre de $C_d$, $I_{sp}$ y masas)

## Paso 6 — Presupuesto de masa

Masa del motor completo, a partir de la fracción de propelente:

$$m_{motor} = \frac{m_p}{\zeta}$$

Masa disponible para el resto del cohete:

$$m_{resto} = m_0 - m_{motor} \;\ge\; \sum_i m_i \quad(\text{fuselaje, cono, aletas, recuperación, aviónica, carga útil})$$

Paracaídas (se iguala el arrastre al peso en descenso):

$$m_{desc} = m_0 - m_p \qquad A_{par} = \frac{2\,m_{desc}\,g}{\rho_0\,C_{D,par}\,v_{desc}^2} \qquad \varnothing_{par} = \sqrt{\frac{4A_{par}}{\pi}}$$

- 🟦 $\zeta$: fracción de propelente supuesta (se verifica con la masa real de la carcasa)
- 🟦 $v_{desc}$: velocidad de aterrizaje aceptable

Si el presupuesto no cierra: reducir $m_{resto}$, mejorar $\zeta$ o revisar la misión, y volver al paso 1.

## Paso 7 — Volumen de propelente

$$V_p = \frac{m_p}{\rho_p}$$

- 🟨 $\rho_p$: densidad real del grano colado

## Paso 8 — Geometría de un segmento BATES

- $D$: diámetro exterior del grano
- $d_0$: diámetro inicial del núcleo
- $L_0$: largo inicial de un segmento
- $x$: espesor ya quemado

$$d(x) = d_0 + 2x \qquad L(x) = L_0 - 2x$$

Área de quemado (núcleo + 2 caras):

$$A_{b,seg}(x) = \pi\,d\,L + 2\cdot\frac{\pi}{4}\left(D^2 - d^2\right)$$

Volumen de un segmento:

$$V_{seg} = \frac{\pi}{4}\left(D^2 - d_0^2\right)L_0$$

Espesor de alma (*web*):

$$w = \frac{D - d_0}{2}$$

## Paso 9 — Neutralidad: sale $L_0$

Se pide igual área de quemado al inicio y al final:

$$A_{b,seg}(0) = A_{b,seg}(w)$$

$$\pi d_0 L_0 + \frac{\pi}{2}\left(D^2 - d_0^2\right) = \pi D\left(L_0 - D + d_0\right)$$

$$\boxed{L_0 = \frac{3D + d_0}{2}}$$

## Paso 10 — Proporción del núcleo

$$d_0 = k\,D \quad\Rightarrow\quad L_0 = \frac{D\,(3+k)}{2}$$

- 🟦 $k$: fracción del núcleo, típicamente 0.35–0.5 (se verifica con el flujo másico
  y la relación núcleo/garganta, que requieren el modelo de cámara)

## Paso 11 — Diámetro del grano: sale $D$

$$V_p = N\cdot\frac{\pi}{4}D^2\left(1-k^2\right)\cdot\frac{D\,(3+k)}{2} = \frac{\pi\,N\,(1-k^2)(3+k)}{8}\,D^3$$

$$\boxed{D = \left[\frac{8\,V_p}{\pi\,N\,(1-k^2)(3+k)}\right]^{1/3}}$$

- 🟦 $N$: número de segmentos

En cascada: $d_0 = kD$, $L_0 = D(3+k)/2$, $w = D(1-k)/2$.

Implementación: [`scripts/dimensionar.py`](../scripts/dimensionar.py).

## Paso 12 — Dimensiones del tubo del motor

$$D_{int,c} = D + 2\,e_{liner} + 2\,\delta \qquad L_c = N\,L_0 + (N-1)\,s + L_{tapas}$$

- 🟦 $e_{liner}$: espesor del liner
- 🟦 $\delta$: holgura radial
- 🟦 $s$: separación entre segmentos

Restricciones (si fallan, cambiar $N$ o $k$ y volver al paso 11):

$$D_{ext,c} < D_{cohete} \qquad L_c \le L_{disponible}$$

---

## Mapa de la cadena

```
Misión (m₀, h_ap, D_cohete)
   │  Pasos 2–4: energía + Tsiolkovsky + vuelo con arrastre
   ▼
I_req ──(1+μ)──► I_dis ──÷ I_sp g₀──► m_p
                                       │  Paso 6: ¿cabe en m₀? (ζ)
                                       ▼
                                 V_p = m_p/ρ_p
                                       │  Pasos 8–11: BATES + neutralidad + d₀ = kD
                                       ▼
                           D → d₀ → L₀ → w
                                       │  Paso 12
                                       ▼
                            D_int,c , L_c del tubo
```

## Qué queda abierto (necesita el volumen de control de la cámara)

1. **Coherencia de $t_b$:** debe cumplirse $t_b \approx w/\bar r$, con $r = aP^n$ dependiente de la presión de cámara.
2. **Criterios de flujo para $k$ y $N$:** el flujo másico $G$ y la relación $A_{núcleo}/A_t$ necesitan $\dot m$ y $A_t$.
3. **Validez de $\zeta$:** el espesor de pared (y con él la masa de la carcasa) depende de $P_{max}$.

# Número de granos (segmentos) de un motor BATES

El número de segmentos $N$ no se elige al azar. Sale de tres cosas:

- el **volumen** de propelente necesario fija un mínimo,
- el **flujo de gas** por el núcleo fija un máximo,
- el **espacio** disponible confirma que quepa.

**Convención:**
- 🟦 = decisión de diseño
- 🟨 = propiedad del propelente (dato de entrada)
- sin marca = se calcula

---

## Dónde va en la secuencia de diseño

Este cálculo toma resultados de [`01_mision_a_geometria.md`](01_mision_a_geometria.md)
y depende de qué se conoce primero, $D$ o $N$:

**Ruta A: $D$ libre.** Se elige $N$ y sale $D$ (paso 11 de `01`, raíz cúbica).

```
7. V_p → 8–9. geometría y neutralidad → 10. k → [elegir N] → 11. D (raíz cúbica) → 12. tubo
```

**Ruta B: $D$ impuesto por la carcasa.** Sale $N$ (este documento).

```
7. V_p → 8–9. geometría y neutralidad → 10. k
   → D = tubo comercial − 2·liner − holgura
   → N_min = ⌈V_p / V_seg⌉                 ← sección 2
   → 12. tubo y largo de cámara             ← sección 4
   → [volumen de control: P(t), r, ṁ]
   → verificar N ≤ N_max (G_final ≤ G_max)  ← sección 3
```

| Parte de la decisión sobre N | Dónde va | Qué necesita |
|---|---|---|
| $N_{min}$ (por volumen) | después del paso 10 | $V_p$, $D$, $k$ |
| Espacio ($L_c \le L_{disp}$) | paso 12 | $N$, $L_0$ |
| $N_{max}$ (por flujo másico) | después del volumen de control | $r(P)$, $A_b$, $d_0$ |

---

## 1. Por qué se divide en segmentos

En un grano tubular largo, casi toda el área que quema está en el núcleo, y el
núcleo crece al quemar: la combustión es **progresiva**. Al segmentar aparecen
caras que se achican mientras el núcleo crece, y los dos efectos se compensan.

La neutralidad fija el largo de cada segmento:

$$L_0 = \frac{3D + d_0}{2} \approx 1.5\text{–}2\,D$$

Cada segmento tiene un largo "correcto" que depende de su diámetro. Para tener más
propelente no se alargan los segmentos: se agregan más.

Hay también una razón práctica: los granos cortos se cuelan con menos burbujas y
grietas, y son más fáciles de inspeccionar.

## 2. Mínimo: lo exige el volumen de propelente

Con $D$ (impuesto por la carcasa) y $d_0 = kD$:

$$V_{seg} = \frac{\pi}{4}\left(D^2 - d_0^2\right)L_0$$

$$\boxed{N_{min} = \left\lceil \frac{V_p}{V_{seg}} \right\rceil}$$

(redondeado hacia arriba)

Es la misma relación del paso 11 de `01`, vista al revés. $N$ y $D$ están atados por
el volumen: menos granos exigen un motor más grueso.

## 3. Máximo: el flujo de gas por el núcleo

Todo el gas de los segmentos de adelante pasa por el núcleo de los de atrás. Al
final del último segmento:

$$G_{final} = \frac{\dot m}{A_{núcleo}} = \frac{\rho_p\,r\,N\,A_{b,seg}}{\frac{\pi}{4}d_0^2}$$

$G$ crece proporcionalmente a $N$. Por encima de un límite aparece la **combustión
erosiva**: el gas rápido barre la superficie, la velocidad de regresión supera $aP^n$
y hay un pico de presión al encender. Despejando:

$$\boxed{N_{max} = \frac{G_{max}\,\frac{\pi}{4}d_0^2}{\rho_p\,r\,A_{b,seg}}}$$

- 🟦 $G_{max}$: límite de flujo másico (regla práctica ~1400 kg/m²s)
- 🟨 $\rho_p$: densidad del propelente
- $r = aP^n$: depende de la presión de cámara

Por eso $N$ solo se confirma después de modelar la cámara (volumen de control).

## 4. Verificación de espacio

$$L_c = N\,L_0 + (N-1)\,s + L_{tapas} \le L_{disponible}$$

- 🟦 $s$: separación entre segmentos

El motor tiene que caber en el cohete sin desplazar demasiado el centro de gravedad
hacia atrás (afecta la estabilidad en vuelo).

## 5. Qué hacer si $N_{min} > N_{max}$

| Acción | Efecto |
|---|---|
| Aumentar $D$ (carcasa más gruesa) | cada segmento lleva más propelente → baja $N_{min}$ |
| Aumentar $k$ (núcleo más abierto) | crece $A_{núcleo}$ → sube $N_{max}$ (pero cada segmento lleva menos propelente) |
| Núcleo escalonado | los segmentos de atrás llevan el núcleo más grande, donde pasa más gas |

## Resumen

```
D (carcasa) → V_seg → N_min = ⌈V_p / V_seg⌉   ← propelente necesario
                      N_max (por G)            ← flujo por el núcleo
                      L_c ≤ L_disp             ← espacio
     elegir N_min ≤ N ≤ N_max ; si no existe, cambiar D o k
```

En motores amateur, $N$ suele quedar entre 2 y 6; 4 es muy común.

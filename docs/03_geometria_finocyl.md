# Geometría del grano Finocyl — ecuaciones

Reemplaza a los pasos 8–11 de [`01_mision_a_geometria.md`](01_mision_a_geometria.md)
cuando el grano es **Finocyl** (*fin + cylinder*: núcleo cilíndrico con aletas radiales).
Los pasos 1–7 y 12 no cambian.

**Convención:**
- 🟦 = decisión de diseño
- 🟨 = propiedad del propelente (dato de entrada)
- sin marca = se calcula

---

## F1 — Variables geométricas

Sección transversal (igual en todo el largo del grano):

| Símbolo | Significado |
|---|---|
| $D$ | diámetro exterior del grano |
| 🟦 $r_c$ | radio del núcleo cilíndrico |
| 🟦 $n_f$ | número de aletas |
| 🟦 $w_f$ | ancho de cada aleta |
| 🟦 $R_f$ | radio hasta la punta de la aleta (largo de aleta $= R_f - r_c$) |
| $L$ | largo del grano (un solo grano, sin segmentar) |

**Puerto inicial** (región vacía): la unión del círculo de radio $r_c$ con $n_f$
rectángulos de ancho $w_f$, que salen del centro hasta $R_f$, separados $2\pi/n_f$.

## F2 — Áreas iniciales

$$A_{port,0} \approx \pi r_c^2 + n_f\,w_f\,(R_f - r_c)$$

$$A_{prop} = \frac{\pi}{4}D^2 - A_{port,0}$$

(La aproximación ignora el pequeño solape entre aletas y círculo; el cálculo numérico es exacto.)

**Carga volumétrica** (fracción de la sección ocupada por propelente):

$$\lambda = \frac{A_{prop}}{\frac{\pi}{4}D^2}$$

## F3 — Largo del grano

Con extremos inhibidos, todo el propelente está en la sección transversal:

$$\boxed{L = \frac{V_p}{A_{prop}}}$$

## F4 — Regresión: principio de Huygens

Cada punto de la superficie retrocede **en dirección normal** a la misma velocidad $r$.
Después de quemar un espesor $x$, el puerto es el conjunto de puntos que están a
distancia $\le x$ del puerto inicial:

$$\Omega(x) = \{\,\mathbf{p} : d(\mathbf{p}) \le x\,\} \cap \{\,|\mathbf{p}| \le D/2\,\}$$

con la **función distancia** al puerto inicial:

$$d(\mathbf{p}) = \min\Big( d_{círculo}(\mathbf{p}),\; d_{aleta,1}(\mathbf{p}),\;\dots,\; d_{aleta,n_f}(\mathbf{p}) \Big)$$

$$d_{círculo} = \max\left(|\mathbf{p}| - r_c,\; 0\right)$$

Para la aleta $i$, en coordenadas giradas el ángulo $\theta_i = 2\pi i/n_f$
($u$ a lo largo de la aleta, $v$ perpendicular):

$$d_{aleta,i} = \sqrt{\max(-u,\;u - R_f,\;0)^2 + \max(|v| - w_f/2,\;0)^2}$$

Por esto las esquinas de las aletas se **redondean** al quemar y los huecos entre aletas
se llenan: la forma cambia y no existe una fórmula cerrada para $A_b(x)$.

## F5 — Perímetro y área de quemado

Área del puerto quemado: $A(x) = \text{área de } \Omega(x)$.

El perímetro que quema es la derivada del área:

$$\mathcal{P}(x) = \frac{dA}{dx}$$

Con extremos inhibidos:

$$\boxed{A_b(x) = \mathcal{P}(x)\cdot L}$$

## F6 — Fin de la combustión

$$x_{max} = \max_{|\mathbf{p}|\le D/2} d(\mathbf{p})$$

- **web en la punta de la aleta**: $D/2 - R_f$. Ahí la llama llega primero a la pared.
- Entre las aletas queda propelente remanente (*sliver*) que se quema hasta $x_{max}$
  con área decreciente: es la cola de la curva.

## F7 — Criterios de diseño

**Neutralidad** (objetivo): minimizar la variación de $A_b$ durante el 0–90 % de la
masa quemada (sin contar la cola):

$$\varepsilon = \frac{A_{b,max} - A_{b,min}}{A_{b,min}}$$

**Física de la neutralidad:** el núcleo cilíndrico es **progresivo** (su perímetro
crece como $2\pi(r_c + x)$). Las aletas aportan perímetro al inicio y lo **pierden**
al redondearse y fundirse. Un buen Finocyl hace que una pérdida compense a la otra.

**Flujo másico** (restricción, como en el BATES):

$$G_{final} = \frac{\rho_p\,r\,A_{b,max}}{A_{port,0}} \le G_{max}$$

Requiere $r$. Con KNSB en su **meseta** (1.5–3.8 MPa, $n \approx 0$), $r$ casi no
depende de la presión y la verificación se puede hacer como **estimación preliminar**
antes del modelo de cámara.

## F8 — Procedimiento

```
D (de la carcasa o igual al de otro diseño para comparar)
  → elegir n_f, w_f, r_c, R_f
  → F2: A_port,0 , A_prop , λ        → F3: L
  → F4–F5: A_b(x) numérico           → F6: x_max, cola
  → F7: ¿ε mínimo? ¿G ≤ G_max?  → si no, cambiar parámetros
  → paso 12 de 01: D_int, largo de cámara
```

Implementación numérica: [`scripts/finocyl_geom.py`](../scripts/finocyl_geom.py).

"""Pasos 6-12 para grano Finocyl + acero 304 (mismo diámetro que el BATES N=4)."""
import math
import numpy as np
from comun import mision, presupuesto, r_knsb, RHO_P
from ejemplo_bates import geometria, E_LINER, DELTA, G_MAX, P_MESETA
from finocyl_geom import metricas, curva

ZETA = 0.40           # acero 304 (mismo supuesto que el ejemplo 1)


def buscar(D, Vp, r):
    """Minimiza la variación de A_b (0-90 % de masa) con G_final <= G_MAX."""
    mejores = []
    for n_f in (4, 6, 8, 10, 12):
        for w_f in (3e-3, 4e-3, 6e-3):
            for r_c in np.arange(4e-3, 24e-3, 2e-3):
                for R_f in np.arange(r_c + 2e-3, D / 2 - 3e-3, 2e-3):
                    if n_f * w_f > 2 * math.pi * r_c * 0.9:
                        continue
                    m = metricas(D, r_c, n_f, w_f, R_f)
                    L = Vp / (m["At"] - m["A0"])
                    G = RHO_P * r * m["Pmax"] * L / m["A0"]
                    if G <= G_MAX:
                        mejores.append((m["var"], n_f, w_f, r_c, R_f, L, G))
    mejores.sort()
    return mejores


def main():
    mi = mision()
    Vp = mi["Vp"]
    b = presupuesto(mi["mp"], ZETA)
    gb = geometria(Vp, 4)
    D = gb["D"]
    r = r_knsb(P_MESETA)
    print(f"D (igual al BATES N=4) = {D*1e3:.1f} mm ; criterio G_final <= {G_MAX:.0f} kg/m2s")
    print(f"margen de masa (zeta={ZETA}) = {b['margen']:+.2f} kg")
    res = buscar(D, Vp, r)
    print("Mejores 8 (var, n_f, w_f, r_c, R_f, L, G):")
    for c in res[:8]:
        print(f"  var={c[0]*100:5.1f}%  n_f={c[1]} w_f={c[2]*1e3:.0f} r_c={c[3]*1e3:.0f} R_f={c[4]*1e3:.0f} mm  L={c[5]*1e3:.0f} mm  G={c[6]:.0f}")
    var, n_f, w_f, r_c, R_f, L, _ = res[0]
    xs, P, A, xmax, A0, At = curva(D, r_c, n_f, w_f, R_f, h=5e-5)
    Ab = P * L
    frac = (A - A0) / (At - A0)
    Gf = RHO_P * r * Ab[1:].max() / A0
    print(f"\nDiseño elegido: n_f={n_f}, w_f={w_f*1e3:.0f} mm, r_c={r_c*1e3:.0f} mm, R_f={R_f*1e3:.0f} mm")
    print(f"  largo de aleta = {(R_f-r_c)*1e3:.0f} mm ; web en punta de aleta = {(D/2-R_f)*1e3:.1f} mm ; web en el cilindro = {(D/2-r_c)*1e3:.1f} mm")
    print(f"  A_port0={A0*1e6:.0f} mm2  A_prop={(At-A0)*1e6:.0f} mm2  carga volumétrica={(At-A0)/At*100:.1f} %")
    print(f"  L={L*1e3:.0f} mm  L/D={L/D:.1f}  x_max={xmax*1e3:.1f} mm  t_b(meseta)~{xmax/r:.2f} s")
    print(f"  Ab0={Ab[1]*1e6:.0f}  Ab_max={Ab[frac<=0.9][1:].max()*1e6:.0f}  Ab_min(0-90%)={Ab[frac<=0.9][1:].min()*1e6:.0f} mm2")
    print(f"  G_final prelim={Gf:.0f} kg/m2s ; D_int={ (D+2*E_LINER+2*DELTA)*1e3:.1f} mm ; L_grano={L*1e3:.0f} mm")
    print("  curva (fracción quemada, x, Ab):")
    for f in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.98):
        i = min(np.searchsorted(frac, f), len(xs) - 2)
        i = max(i, 1)
        print(f"    {f:4.2f}  x={xs[i]*1e3:5.2f} mm  Ab={Ab[i]*1e6:7.0f} mm2")
    media = Ab[frac <= 0.9][1:].mean()
    i_cola = np.argmax((frac > 0.5) & (Ab < 0.8 * media))
    print(f"  cola: A_b cae bajo 80 % de la media en x={xs[i_cola]*1e3:.2f} mm, con {frac[i_cola]*100:.1f} % de masa quemada")
    # BATES equivalente para comparar carga volumétrica
    Lb = gb["L_gr"]
    Ab_b = math.pi / 4 * (gb["D"]**2) * Lb
    print(f"\nBATES N=4: carga volumétrica (granos/cilindro) = {Vp/Ab_b*100:.1f} %  L={Lb*1e3:.0f} mm")


if __name__ == "__main__":
    main()

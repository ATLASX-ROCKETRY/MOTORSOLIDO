"""Pasos 6-12 para grano BATES. Uso: python3 scripts/ejemplo_bates.py acero304|al6061"""
import math
import sys
from comun import mision, presupuesto, r_knsb, RHO_P

ZETA = {"acero304": 0.40, "al6061": 0.55}   # fracción de propelente supuesta
K = 0.5            # d0 = K·D
N_ELEGIDO = 4
E_LINER = 1.0e-3   # liner [m]
DELTA = 0.25e-3    # holgura radial [m]
S_SEP = 2.0e-3     # separación entre segmentos [m]
G_MAX = 1400.0     # kg/m2s
P_MESETA = 2.5     # MPa (supuesto: diseño dentro de la meseta KNSB)


def geometria(Vp, N, k=K):
    D = (8 * Vp / (math.pi * N * (1 - k**2) * (3 + k))) ** (1 / 3)
    d0 = k * D
    L0 = (3 * D + d0) / 2
    w = (D - d0) / 2

    def Ab(x):
        d, L = d0 + 2 * x, L0 - 2 * x
        return N * (math.pi * d * L + math.pi / 2 * (D**2 - d**2))
    xs = [w * i / 200 for i in range(201)]
    Abs = [Ab(x) for x in xs]
    return dict(D=D, d0=d0, L0=L0, w=w, Ab0=Ab(0), Abmax=max(Abs), Abmin=min(Abs),
                Abw=Ab(w), D_int=D + 2 * E_LINER + 2 * DELTA,
                L_gr=N * L0 + (N - 1) * S_SEP, Ab=Ab)


def main(mat):
    m = mision()
    b = presupuesto(m["mp"], ZETA[mat])
    print(f"== {mat}  zeta={ZETA[mat]} ==")
    print(f"m_p={m['mp']:.3f}  m_motor={b['m_motor']:.2f}  estructura={b['m_estr']:.2f}  "
          f"disp={b['disp']:.2f}  nec={b['nec']:.2f}  margen={b['margen']:+.2f} kg  "
          f"paracaidas {b['A_par']:.2f} m2 / {b['d_par']:.2f} m")
    # sensibilidad de zeta
    for z in (ZETA[mat] - 0.05, ZETA[mat], ZETA[mat] + 0.05):
        print(f"   zeta={z:.2f} -> margen {presupuesto(m['mp'], z)['margen']:+.2f} kg")
    print(f"V_p = {m['Vp']*1e6:.0f} cm3")
    r = r_knsb(P_MESETA)
    print(" N |   D    d0    L0     w  | D_int | L_granos | L/D_mot | dAb%  | G_fin(prelim)")
    for N in (2, 3, 4, 5, 6):
        g = geometria(m["Vp"], N)
        G = RHO_P * r * g["Abmax"] / (math.pi / 4 * g["d0"]**2)
        var = (g["Abmax"] - g["Abmin"]) / g["Abmin"] * 100
        print(f" {N} | {g['D']*1e3:5.1f} {g['d0']*1e3:5.1f} {g['L0']*1e3:5.1f} {g['w']*1e3:5.1f} |"
              f" {g['D_int']*1e3:5.1f} | {g['L_gr']*1e3:7.0f}  | {g['L_gr']/g['D_int']:5.1f}  | {var:4.1f} | {G:5.0f}")
    g = geometria(m["Vp"], N_ELEGIDO)
    print(f"Elegido N={N_ELEGIDO}: Ab0={g['Ab0']*1e6:.0f} Abmax={g['Abmax']*1e6:.0f} Abw={g['Abw']*1e6:.0f} mm2")
    print(f"t_b (meseta) = w/r = {g['w']/r:.2f} s ; A_port/A_b0 = {math.pi/4*g['d0']**2/g['Ab0']:.4f}")
    for i in range(0, 11, 2):
        x = g["w"] * i / 10
        print(f"   x={x*1e3:5.2f} mm  Ab={g['Ab'](x)*1e6:7.0f} mm2")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "acero304")

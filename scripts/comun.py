"""Datos comunes a los tres ejemplos: misión, propelente KNSB y vuelo 1D.

Pasos 1-5 de docs/01_mision_a_geometria.md (no dependen del grano ni del material).
"""
import math

# --- Paso 1: misión ---
M0 = 10.0            # masa al despegue, incluye motor cargado [kg]
H_AP = 1000.0        # apogeo objetivo [m]
D_COHETE = 0.150     # diámetro del fuselaje [m]
FW_MIN = 5.0         # relación empuje/peso mínima [-]

# --- Supuestos de vuelo ---
CD = 0.5             # coeficiente de arrastre del cohete [-]
F_MEDIO = 800.0      # empuje medio (perfil rectangular) [N]
RHO0 = 1.225         # densidad del aire [kg/m3] (nivel del mar: conservador)
H_ESC = 8500.0       # altura de escala [m]
MARGEN = 0.20        # margen sobre el impulso [-]

# --- Propelente KNSB (65 % KNO3 / 35 % sorbitol) ---
ISP = 104.0          # impulso específico [s] (modelo termoquímico previo, conservador)
RHO_IDEAL = 1841.0   # densidad teórica [kg/m3]
RHO_P = 0.95 * RHO_IDEAL   # densidad real del grano colado (95 %) [kg/m3]
# Vieille por tramos (Nakka): P [MPa] -> r [mm/s]
VIEILLE = [(0.101, 0.807, 10.708, 0.625), (0.807, 1.503, 8.763, -0.314),
           (1.503, 3.792, 7.852, -0.013), (3.792, 7.033, 3.907, 0.535),
           (7.033, 10.67, 9.653, 0.064)]

# --- Presupuesto del resto del cohete (paso 6) [kg] ---
MASAS_RESTO = {"Tubo de fuselaje (~1.3 m, fibra de vidrio)": 1.75,
               "Cono de nariz": 0.70, "Aletas": 0.60, "Soporte del motor": 0.50,
               "Recuperación": 0.90, "Aviónica": 0.50}
V_DESC = 5.5         # velocidad de descenso [m/s]
CD_PAR = 1.5         # coef. de arrastre del paracaídas [-]

G = 9.81
G0 = 9.80665


def r_knsb(P_MPa):
    """Velocidad de regresión KNSB [m/s] para P en MPa."""
    for lo, hi, a, n in VIEILLE:
        if lo <= P_MPa <= hi:
            return a * P_MPa**n * 1e-3
    raise ValueError("Presión fuera del rango medido")


def apogeo(I, F=F_MEDIO, d_cohete=D_COHETE, cd=CD, dt=1e-3):
    """Vuelo vertical 1D. Devuelve (h_ap, v_max, m_p, t_b)."""
    A = math.pi / 4 * d_cohete**2
    mp = I / (ISP * G0)
    tb = I / F
    mdot = mp / tb
    h = v = t = vmax = 0.0
    m = M0
    while True:
        quemando = t < tb
        T = F if quemando else 0.0
        if quemando:
            m -= mdot * dt
        rho = RHO0 * math.exp(-h / H_ESC)
        a = (T - 0.5 * rho * cd * A * v * abs(v)) / m - G
        v += a * dt
        h += v * dt
        t += dt
        vmax = max(vmax, v)
        if not quemando and v < 0:
            return h, vmax, mp, tb


def impulso_requerido(h_obj=H_AP, **kw):
    lo, hi = 100.0, 10000.0
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if apogeo(mid, **kw)[0] < h_obj:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def mision():
    """Pasos 2-5 + 7. Devuelve dict con resultados comunes."""
    I_req = impulso_requerido()
    I_dis = (1 + MARGEN) * I_req
    mp = I_dis / (ISP * G0)
    return dict(v_b=math.sqrt(2 * G * H_AP), I_req=I_req, I_dis=I_dis, mp=mp,
                Vp=mp / RHO_P, h_nom=apogeo(I_dis)[0],
                F_min=FW_MIN * M0 * G, I_est=M0 * math.sqrt(2 * G * H_AP) + M0 * G * I_req / F_MEDIO)


def presupuesto(mp, zeta):
    """Paso 6."""
    m_motor = mp / zeta
    m_resto_disp = M0 - m_motor
    m_resto_nec = sum(MASAS_RESTO.values())
    m_desc = M0 - mp
    A_par = 2 * m_desc * G / (RHO0 * CD_PAR * V_DESC**2)
    return dict(m_motor=m_motor, m_estr=m_motor - mp, disp=m_resto_disp, nec=m_resto_nec,
                margen=m_resto_disp - m_resto_nec, A_par=A_par,
                d_par=math.sqrt(4 * A_par / math.pi))


if __name__ == "__main__":
    m = mision()
    print(f"v_b sin aire = {m['v_b']:.0f} m/s ; I estimado a mano = {m['I_est']:.0f} N·s")
    for cd in (0.4, 0.5, 0.6):
        I = impulso_requerido(cd=cd)
        h, vm, mp, tb = apogeo(I, cd=cd)
        print(f"Cd={cd}: I_req={I:.0f} v_max={vm:.0f} m_p={mp:.2f} t_b={tb:.2f}")
    print(f"I_req={m['I_req']:.0f}  I_dis={m['I_dis']:.0f}  m_p={m['mp']:.3f} kg  "
          f"V_p={m['Vp']*1e6:.0f} cm3  rho_p={RHO_P:.0f}  h_nom={m['h_nom']:.0f} m  F_min={m['F_min']:.0f} N")
    print(f"r en meseta (2.5 MPa) = {r_knsb(2.5)*1e3:.2f} mm/s")

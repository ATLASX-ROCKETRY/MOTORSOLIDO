"""Pasos 1-4: de la misión al impulso total requerido.

Vuelo vertical 1D con masa variable, arrastre cuadrático y atmósfera
exponencial. Busca por bisección el impulso que lleva el cohete al apogeo
objetivo. Ver docs/01_mision_a_impulso.md.
"""
import math

# --- Paso 1: requisitos de la misión (decisiones) ---
M0 = 10.0            # masa al despegue, incluye motor cargado [kg]
H_AP = 1000.0        # apogeo objetivo [m]
D_COHETE = 0.150     # diámetro del fuselaje [m]
FW_MIN = 5.0         # relación empuje/peso mínima [-]

# --- Supuestos del modelo de vuelo ---
CD = 0.5             # coeficiente de arrastre del cohete [-]
F_MEDIO = 800.0      # empuje medio (perfil rectangular) [N]
RHO0 = 1.225         # densidad del aire en el sitio [kg/m3] (nivel del mar: conservador)
H_ESC = 8500.0       # altura de escala de la atmósfera [m]

# --- Propelente (de la termoquímica) ---
ISP = 104.0          # impulso específico [s]

G = 9.81
G0 = 9.80665


def apogeo(I, F=F_MEDIO, d_cohete=D_COHETE, cd=CD, dt=1e-3):
    """Integra el vuelo hasta el apogeo. Devuelve (h_ap, v_max, m_p, t_b)."""
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


def impulso_requerido(h_obj=H_AP, lo=100.0, hi=10000.0, **kw):
    """Bisección sobre I para alcanzar h_obj."""
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if apogeo(mid, **kw)[0] < h_obj:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


if __name__ == "__main__":
    assert F_MEDIO >= FW_MIN * M0 * G, "Empuje medio por debajo de (F/W)_min"

    # Paso 2: cota inferior sin aire
    print(f"v_b sin aire (h_b≈0): {math.sqrt(2 * G * H_AP):.0f} m/s\n")

    # Paso 4: sensibilidad a C_d
    for cd in (0.4, 0.5, 0.6):
        I = impulso_requerido(cd=cd)
        h, vm, mp, tb = apogeo(I, cd=cd)
        print(f"Cd={cd}: I_req={I:.0f} N·s  v_max={vm:.0f} m/s  m_p={mp:.2f} kg  t_b={tb:.2f} s")


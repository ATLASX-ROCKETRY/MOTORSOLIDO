"""Pasos 6-12: de la masa de propelente a las longitudes del grano BATES.

Ver docs/01_mision_a_geometria.md. No incluye el modelo de cámara
(presión, Kn, garganta): eso valida k, N y zeta en la siguiente etapa.
"""
import math

# --- Entradas de pasos anteriores ---
M0 = 10.0            # masa al despegue [kg]
I_DIS = 2200.0       # impulso de diseño (salida de vuelo.py) [N·s]

# --- Propelente (PROVISIONAL: reemplazar con datos medidos) ---
ISP = 104.0          # impulso específico [s]
RHO_P = 1710.0       # densidad real del grano colado [kg/m3]

# --- Decisiones de diseño ---
ZETA = 0.5           # fracción de propelente m_p/m_motor [-] (a verificar)
V_DESC = 5.5         # velocidad de descenso [m/s]
CD_PAR = 1.5         # coef. de arrastre del paracaídas [-]
RHO0 = 1.225         # densidad del aire [kg/m3]
K = 0.5              # d0 = K·D [-]
N = 4                # número de segmentos [-]
E_LINER = 1.0e-3     # espesor de liner [m]
DELTA = 0.25e-3      # holgura radial [m]
S_SEP = 2.0e-3       # separación entre segmentos [m]

G = 9.81
G0 = 9.80665


def main():
    # Paso 5
    mp = I_DIS / (ISP * G0)

    # Paso 6: presupuesto de masa
    m_motor = mp / ZETA
    m_resto = M0 - m_motor
    m_desc = M0 - mp
    A_par = 2 * m_desc * G / (RHO0 * CD_PAR * V_DESC**2)
    d_par = math.sqrt(4 * A_par / math.pi)

    # Paso 7
    Vp = mp / RHO_P

    # Pasos 9-11: neutralidad + d0 = K·D + volumen total
    D = (8 * Vp / (math.pi * N * (1 - K**2) * (3 + K))) ** (1 / 3)
    d0 = K * D
    L0 = (3 * D + d0) / 2
    w = (D - d0) / 2

    # Comprobación de neutralidad (Paso 8)
    def Ab_seg(x):
        d, L = d0 + 2 * x, L0 - 2 * x
        return math.pi * d * L + math.pi / 2 * (D**2 - d**2)

    # Paso 12
    D_int_c = D + 2 * E_LINER + 2 * DELTA
    L_granos = N * L0 + (N - 1) * S_SEP

    print(f"m_p      = {mp:.3f} kg")
    print(f"m_motor  = {m_motor:.2f} kg   m_resto disponible = {m_resto:.2f} kg")
    print(f"Paracaídas: A = {A_par:.2f} m2, diámetro = {d_par:.2f} m")
    print(f"V_p      = {Vp*1e6:.0f} cm3")
    print(f"D        = {D*1e3:.1f} mm")
    print(f"d0       = {d0*1e3:.1f} mm")
    print(f"L0       = {L0*1e3:.1f} mm")
    print(f"w        = {w*1e3:.1f} mm")
    print(f"A_b,seg(0) = {Ab_seg(0)*1e6:.0f} mm2   A_b,seg(w) = {Ab_seg(w)*1e6:.0f} mm2")
    print(f"D_int tubo  = {D_int_c*1e3:.1f} mm")
    print(f"Largo granos = {L_granos*1e3:.0f} mm (+ tapas)")


if __name__ == "__main__":
    main()

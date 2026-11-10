"""Regresión 2D de un grano Finocyl por campo de distancias.

Puerto inicial = círculo de radio r_c ∪ n_f aletas rectangulares de ancho w_f
que van del centro hasta el radio R_f. Con regresión normal uniforme, la
superficie en el instante x es el conjunto de puntos a distancia x del puerto
inicial (principio de Huygens). Perímetro: P(x) = dA_quemada/dx.
Extremos inhibidos: A_b(x) = P(x)·L.
"""
import numpy as np


def campo_distancia(D, r_c, n_f, w_f, R_f, h=1e-4):
    R = D / 2
    c = np.arange(-R + h / 2, R, h)
    X, Y = np.meshgrid(c, c)
    rho = np.hypot(X, Y)
    dist = np.maximum(rho - r_c, 0.0)
    for i in range(n_f):
        th = 2 * np.pi * i / n_f
        u = X * np.cos(th) + Y * np.sin(th)
        v = -X * np.sin(th) + Y * np.cos(th)
        du = np.maximum(np.maximum(-u, u - R_f), 0.0)
        dv = np.maximum(np.abs(v) - w_f / 2, 0.0)
        dist = np.minimum(dist, np.hypot(du, dv))
    dentro = rho <= R
    return dist[dentro], h * h


def curva(D, r_c, n_f, w_f, R_f, h=1e-4, dx=None):
    """Devuelve x, perímetro P(x), área de puerto A(x), x_max, A_port0, A_total."""
    d, a = campo_distancia(D, r_c, n_f, w_f, R_f, h)
    x_max = d.max()
    dx = dx or 2 * h
    xs = np.arange(0, x_max + dx, dx)
    ds = np.sort(d)
    A = np.searchsorted(ds, xs, side="right") * a
    P = np.gradient(A, xs)
    return xs, P, A, x_max, A[0], d.size * a


def metricas(D, r_c, n_f, w_f, R_f, h=2e-4):
    xs, P, A, xmax, A0, At = curva(D, r_c, n_f, w_f, R_f, h)
    frac = (A - A0) / (At - A0)           # fracción de masa quemada
    sel = frac <= 0.90
    Ps = P[sel][1:]
    var = (Ps.max() - Ps.min()) / Ps.min()
    return dict(var=var, P0=P[1], A0=A0, At=At, xmax=xmax, Pmax=Ps.max(), Pmin=Ps.min())

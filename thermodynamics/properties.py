# properties.py
# este código é para facilitar a "comunicação" com os arquivos de calculo de propriedades e o firedrake

import numpy as np

from interpolators import load_interpolators


# carrega uma vez
Z_interp, rho_interp, mu_interp = load_interpolators()


Temperature = 300.0


def _make_point(P, T):
    """
    Prepara ponto para o RegularGridInterpolator.
    """
    return np.array([[P, T]])



def hydrogen_Z(P, T=Temperature):
    """
    Retorna o fator Z do H2.
    P em Pa
    T em K
    """

    point = _make_point(P, T)

    return Z_interp(point)[0]



def hydrogen_density(P, T=Temperature):
    """
    Retorna densidade do H2.
    """

    point = _make_point(P, T)

    return rho_interp(point)[0]



def hydrogen_viscosity(P, T=Temperature):
    """
    Retorna viscosidade do H2.
    """

    point = _make_point(P, T)

    return mu_interp(point)[0]
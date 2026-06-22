# properties.py
import numpy as np

# =================
# Fator de compressibilidade do hidrogênio (Z)
# =================

# Coeficientes do ajuste polinomial
# Obtidos usando Peng-Robinson via NeqSim
Z_coefficients = np.array([
    2.68916593e-33,
   -6.59128807e-25,
    6.78271975e-17,
    3.00817947e-09,
    9.98373263e-01,
])


def calculate_Z(P, T=300.0):
    """
    Fator de compressibilidade do hidrogênio.

    Parâmetro:
    P : pressão em Pa
    T : temperatura em K (atualmente não usada)

    Retorna:
    Z : fator de compressibilidade
    """

    return np.polyval(Z_coefficients, P)

# =================
# Viscosidade do hidrogênio (mu)
# =================
mu_coefficients = np.array([
    1.47004003e-31,
   -2.36789532e-23,
   -5.71096443e-16,
    7.82787947e-06,
])


def calculate_viscosity(P, T=300):
    """
    Viscosidade do hidrogênio.

    P em Pa
    T em K

    Correlação ajustada para T=300 K
    """

    return np.polyval(mu_coefficients, P)
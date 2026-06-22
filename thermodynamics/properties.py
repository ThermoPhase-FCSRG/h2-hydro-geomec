import numpy as np


# Coeficientes do ajuste polinomial
# Obtidos usando Peng-Robinson via NeqSim
Z_coefficients = np.array([
    2.68916593e-33,
   -6.59128807e-25,
    6.78271975e-17,
    3.00817947e-09,
    9.98373263e-01,
])


def calculate_Z(P):
    """
    Fator de compressibilidade do hidrogênio.

    Parâmetro:
    P : pressão em Pa

    Retorna:
    Z : fator de compressibilidade
    """

    return np.polyval(Z_coefficients, P)
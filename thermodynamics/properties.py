# properties.py
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

def calculate_viscosity(P,T=300):
    """
    Viscosidade do hidrogênio.
    Ajuste inicial.
    """
    return 0.94e-5  #precisa alterar esse valor. essse valor é pra T=50C
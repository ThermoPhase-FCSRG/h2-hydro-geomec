# fit_h2_mu.py

import numpy as np
import matplotlib.pyplot as plt

from neqsim_model import calculate_viscosity


# intervalo de pressão
P_bar = np.linspace(100,700,50)

# converter para Pa
P = P_bar*1e5


# temperaturas
T_values = [300]


for T in T_values:

    mu_values = []

    print(f"Calculando viscosidade para T={T} K")

    for p in P:
        mu = calculate_viscosity(p,T)
        mu_values.append(mu)


    mu_values = np.array(mu_values)


    # ajuste polinomial em pressão
    degree = 3

    coef = np.polyfit(
        P,
        mu_values,
        degree
    )


    print("\nTemperatura:",T)
    print("Coeficientes:")
    print(coef)


    mu_fit=np.polyval(coef,P)


    print("Erro máximo:")
    print(np.max(np.abs(mu_values-mu_fit)))


    plt.figure()

    plt.plot(
        P_bar,
        mu_values,
        "o",
        label="NeqSim"
    )

    plt.plot(
        P_bar,
        mu_fit,
        label="fit"
    )

    plt.xlabel("Pressure [bar]")
    plt.ylabel("Viscosity [Pa.s]")
    plt.grid()
    plt.legend()

    plt.savefig(f"mu_fit_H2_{T}K.png")
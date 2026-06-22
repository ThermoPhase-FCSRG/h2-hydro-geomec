import numpy as np
import matplotlib.pyplot as plt

from neqsim_model import calculate_Z


# pressão em Pa
P_bar = np.linspace(100, 700, 50)

# converter bar -> Pa
P = P_bar * 1e5

T = 300.0


Z_values = []

print("Calculando Z do hidrogênio...")

for p in P:
    z = calculate_Z(p, T)
    Z_values.append(z)


Z_values = np.array(Z_values)


# Ajuste polinomial
degree = 4

coefficients = np.polyfit(
    P,
    Z_values,
    degree
)


print("\nCoeficientes:")
print(coefficients)


# teste do ajuste
Z_fit = np.polyval(coefficients, P)


plt.figure(figsize=(8,5))

plt.plot(P_bar, Z_values, "o", label="NeqSim PR")
plt.plot(P_bar, Z_fit, "-", label="Polinômio")

plt.xlabel("Pressure [bar]")
plt.ylabel("Z")
plt.grid()
plt.legend()

plt.savefig("Z_fit_H2.png", dpi=200)

print("\nErro máximo:")
print(np.max(np.abs(Z_values-Z_fit)))
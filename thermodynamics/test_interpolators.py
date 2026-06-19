from interpolators import load_interpolators
import numpy as np


# carregar interpoladores
Z_interp, rho_interp, mu_interp = load_interpolators()


# condição de teste
P_test = 700e5     # 700 bar em Pa
T_test = 300.0     # Kelvin


# RegularGridInterpolator espera um ponto no formato:
# [[P,T]]
point = np.array([[P_test, T_test]])


Z_value = Z_interp(point)[0]
rho_value = rho_interp(point)[0]
mu_value = mu_interp(point)[0]


print("Teste termodinâmico H2")
print("-----------------------")
print(f"P = {P_test/1e5:.1f} bar")
print(f"T = {T_test:.1f} K")

print(f"Z   = {Z_value:.5f}")
print(f"rho = {rho_value:.5f} kg/m3")
print(f"mu  = {mu_value:.5e} Pa.s")
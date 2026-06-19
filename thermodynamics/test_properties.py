# test_properties.py


from properties import (
    hydrogen_Z,
    hydrogen_density,
    hydrogen_viscosity,
)


# condições de teste
P_test = 700e5     # Pa
T_test = 300.0     # K


Z = hydrogen_Z(P_test, T_test)
rho = hydrogen_density(P_test, T_test)
mu = hydrogen_viscosity(P_test, T_test)


print("Teste properties.py - Hidrogênio")
print("--------------------------------")
print(f"P   = {P_test/1e5:.1f} bar")
print(f"T   = {T_test:.1f} K")

print(f"Z   = {Z:.5f}")
print(f"rho = {rho:.5f} kg/m3")
print(f"mu  = {mu:.5e} Pa.s")
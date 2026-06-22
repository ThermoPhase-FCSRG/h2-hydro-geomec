from properties import calculate_viscosity


P_values = [
    100e5,
    300e5,
    700e5
]


print("Teste viscosidade H2")
print("--------------------")


for P in P_values:

    mu = calculate_viscosity(P)

    print(
        f"P={P/1e5:.0f} bar   "
        f"mu={mu:.8e} Pa.s"
    )
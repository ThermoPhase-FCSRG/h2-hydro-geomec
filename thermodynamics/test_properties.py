# test_properties.py

from properties import calculate_Z


P = 700e5   # 700 bar em Pa

Z = calculate_Z(P)

print("Teste properties.py - Hidrogênio")
print("--------------------------------")
print(f"P = {P/1e5:.1f} bar")
print(f"Z = {Z:.5f}")
# grid.py

import numpy as np

def create_grid(): # criando uma grade de pontos para interpolação
    P_vals = np.linspace(1e7, 7e7, 150) # 150 pontos de pressão entre 100 bar (1e7 Pa) e 700 bar (7e7 Pa)
    T_vals = np.linspace(200, 500, 50)  # 50 pontos de temperatura entre 200 K e 500 K
    return P_vals, T_vals
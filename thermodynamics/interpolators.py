# interpolators.py

from pathlib import Path
import numpy as np
from scipy.interpolate import RegularGridInterpolator

repo_root = Path(__file__).resolve().parents[1]
data_dir = repo_root / "data" / "tables"

def load_interpolators():
    P = np.load(data_dir / "P.npy")
    T = np.load(data_dir / "T.npy")

    Z = np.load(data_dir / "Z.npy")
    rho = np.load(data_dir / "rho.npy")
    mu = np.load(data_dir / "mu.npy")

    Z_interp = RegularGridInterpolator((P, T), Z)  # Cria um interpolador para Z
    rho_interp = RegularGridInterpolator((P, T), rho)
    mu_interp = RegularGridInterpolator((P, T), mu)

    return Z_interp, rho_interp, mu_interp
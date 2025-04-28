import numpy as np

# Constantes de degeneración
G_Q = 12  # Quarks: 3 colores x 2 spins x 2 sabores
G_G = 16  # Gluones: 8 colores x 2 spins

# Constantes físicas
VOLUME = 2.1446605848506324  # Volumen fijo del protón en fm^3
HBAR_C = 197.3269804  # MeV*fm (para conversiones)

# Factores de conversión
CONVERSION_T4 = (1e9 / 1.973e8) ** 3   # Para T^4 (MeV^4 a MeV/fm^3)
CONVERSION_T7 = (1e9 / 1.973e8) ** 6   # Para T^7 (MeV^7 a MeV/fm^3)

# Presión de gluones (Bose-Einstein ultrarrelativista)
def pressure_gluons(T):
    return (G_G * np.pi**2 / 90) * T**4 * CONVERSION_T4

# Presión de quarks (Fermi-Dirac ultrarrelativista)
def pressure_quarks(T, mu):
    term1 = (7 * np.pi**2 / 60) * T**4
    term2 = (mu**2 * T**2) / 2
    term3 = mu**4 / (4 * np.pi**2)
    return (G_Q / 6) * (term1 + term2 + term3) * CONVERSION_T4

# Presión total clásica (gluones + quarks)
def pressure_total(T, mu):
    return pressure_gluons(T) + pressure_quarks(T, mu)

# Presión total en Tsallis (con corrección completa)
def pressure_tsallis(T, mu, q):
    # Presión clásica BG
    P_BG = pressure_total(T, mu)
    
    # Corrección Tsallis
    correction_factor = ((8 * np.pi**2) / 90) * G_Q * G_G * (np.pi**2 / 90 + (1 / 30) * (mu / T)**2) * VOLUME
    P_Tsallis = (1 - q) * correction_factor * T**7 * CONVERSION_T7
    
    return P_BG + P_Tsallis
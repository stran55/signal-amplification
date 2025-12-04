import numpy as np
import matplotlib.pyplot as plt

from scipy.special import gamma

freq = np.linspace(10, 1000, 2000)


#dimensionless GW frequency
def w_f(f, M_Lsun, z_L=1):
    G = 6.6743e-11 # m^3 / (kg*s^2)
    c = 299792458 # m/s
    M_sun = 1.9891e30 # kg

    
    M_L = M_Lsun * M_sun
    print("GM/c3 = ", G * M_L / c**3, " seconds")
    return 8 * np.pi * G * M_L * (1 + z_L) * f / c**3



print(w_f(100, 20))


"""
Pour modifier les paramètres aérodynamiques de l'avion
"""
from atmosphere import Atmosphere
from Avion import Avion
import math


def portance_L (monAvion: Avion):
    return monAvion.get_masse() * 9.81  # Vol en palier

def coef_portance_cl (cl_alpha):
    alpha_l0 = 0  # angle d'attaque à portance nulle
    alpha_aile = 3  # angle d'attaque de l'avion en croisière
    return cl_alpha * (alpha_aile - alpha_l0)

def cl_avec_portance (monAvion: Avion):
    return portance_L(monAvion) / (0.5 * monAtmo.get_density() * monA320.get_surface() * monA320.get_ground_speed()**2)

def allongement_AR_2(monAvion: Avion):
    return monAvion.get_envergure()**2 / monAvion.get_surface()

def oswald_factor_e_2(monAvion: Avion):
    if monAvion.get_angle_fleche() > 30:
        return 4.61 * (1 - 0.045 * allongement_AR_2(monAvion) ** 0.68) * (math.cos(monAvion.get_angle_fleche())) ** 0.15 - 3.1
    else:
        return 0.8

def correction_k_2(monAvion: Avion):
    return 1 / (math.pi * oswald_factor_e_2(monAvion) * allongement_AR_2(monAvion))

def coef_trainee_2(monAvion: Avion):
    return monAvion.get_cd0() + correction_k_2(monAvion) * cl_avec_portance(monAvion)
def trainee(monAvion: Avion):
    return 0.5 * monAtmo.get_density() * monAvion.get_ground_speed() **2 * monAvion.get_surface() * coef_trainee_2(monAvion)

def finesse(monAvion : Avion):
    return cl_avec_portance(monAvion) / coef_trainee_2(monAvion)


monAtmo = Atmosphere(10000)
# A320 W=73500kg S=112.4m2 b=34.1m delta_le=25° cd0=0.02

monA320 = Avion(10000, 238, monAtmo, 34.1, 112.4, 73500, 25, 0.02)
lift = portance_L(monA320)
cl = cl_avec_portance(monA320)
drag = trainee(monA320)
print(f'L = {lift} N, CL = {cl}, D = {drag} N')
print(finesse(monA320))

# A330 W=242000kg S=361.6m2 b=60.3m delta_le=30° cd0=0.025
monA330 = Avion(10000, 238, monAtmo, 60.3, 361.6, 242000, 30, 0.025)

# A380 W=560000kg S=845m2 b=79.8m delta_le=33.5° cd0=0.022
monA380 = Avion(10000, 238, monAtmo, 79.8, 845, 560000, 33.5, 0.022)

# B777 W=299000kg S=427.8m2 b=60.9m delta_le=31.6° cd0=0.025
monB777 = Avion(10000, 238, monAtmo, 60.9, 427.8, 299000, 31.6, 0.025)

# B737 W=79000kg S=124.6m2 b=35.8m delta_le=25° cd0=0.02
monB737 = Avion(10000, 238, monAtmo, 35.8, 124.6, 79000, 35.8, 0.02)

# B787 W=227930kg S=325m2 b=60.1m delta_le=32.2° cd0=0.017
monB787 = Avion(10000, 238, monAtmo, 60.1, 325, 227930, 32.2, 0.017)

# B747 W=396890kg S=511m2 b=64.4m delta_le=37.5° cd0=0.024
# B727 W=95000kg S=164.3m2 b=32.9m delta_le=25° cd0=0.03

"""
Pour modifier les paramètres aérodynamiques de l'avion
"""
from atmosphere import Atmosphere
from avion import Avion
import math


def controle(avion, new_altitude, new_vitesse, atmosphere):

    atmosphere = Atmosphere(new_altitude)
    avion = Avion(new_altitude, new_vitesse, atmosphere)

    print("nouvelles conditions")
    avion.affichage()
    print(avion.conditions_atmospheriques())

    return avion

def portance (densite, vitesse_sol, surface, envergure):
    # Paramètres de départs
    a0 = 2 * math.pi  # 1/rad
    alpha_l0 = 0  # angle d'attaque à portance nulle
    alpha_aile = 3  # angle d'attaque de l'avion en croisière

    allongement = envergure**2 / surface
    a = a0 / ( 1 + 2 / (allongement))
    coef_portance = a * (alpha_aile - alpha_l0) * (math.pi / 180) #  coef portance en reconvertissant a en degré
    portance  = 0.5 * densite * vitesse_sol**2 * surface * coef_portance

    return portance

def portance_L (poids):
    return poids * 9.81  # Vol en palier

def coef_portance_cl (cl_alpha):
    alpha_l0 = 0  # angle d'attaque à portance nulle
    alpha_aile = 3  # angle d'attaque de l'avion en croisière
    return cl_alpha * (alpha_aile - alpha_l0)

def cl_avec_portance (L, densite, vitesse, surface):
    return L / (0.5 * densite * surface * vitesse**2)

def coef_trainee (envergure, surface, angle_aile_bord_attaque, cd0, cl):
    def allongement_AR(envergure, surface):
        return envergure ** 2 / surface

    def oswald_factor_e (envergure, surface, angle_aile_bord_attaque):
        if angle_aile_bord_attaque > 30:
            return 4.61 * (1 - 0.045 * allongement_AR(envergure, surface) ** 0.68 ) * (math.cos(angle_aile_bord_attaque))**0.15 - 3.1
        else:
            return 0.8

    def correction_k(envergure, surface, angle_aile_bord_attaque):

        return 1 / (math.pi * oswald_factor_e(envergure, surface, angle_aile_bord_attaque) * allongement_AR(envergure, surface))

    print(allongement_AR(envergure, surface), oswald_factor_e (envergure, surface, angle_aile_bord_attaque), correction_k(envergure, surface, angle_aile_bord_attaque))
    return cd0 + correction_k(envergure, surface, angle_aile_bord_attaque) * cl**2


monAtmo = Atmosphere(10000)
monAvion = Avion(10000, 283, monAtmo)
controle(monAvion, 5000, 250, monAtmo)
print(monAtmo.get_density())
print(portance(monAtmo.get_density(), 405, 112.4, 34.1))
print(portance_L(73500))

monA320 = Avion(10000, 238, monAtmo)
lift = portance_L(73500)
cl = cl_avec_portance(lift, monAtmo.get_density(), monA320.get_ground_speed(), 112.4)
trainee_A320 = 0.5 * monAtmo.get_density() * monA320.get_ground_speed() ** 2 * coef_trainee(34.1, 112.4, 30, 0.02, cl) * 112.4
print(f'L = {lift} N, CL = {cl}, D = {trainee_A320} N')
"""
Pour modifier les paramètres aérodynamiques de l'avion
"""
from atmosphere import Atmosphere
from parametres import Parametres


def coef_portance_cl (cl_alpha):
    alpha_l0 = 0  # angle d'attaque à portance nulle
    alpha_aile = 3  # angle d'attaque de l'avion en croisière
    return cl_alpha * (alpha_aile - alpha_l0)


def get_dict_parametre():
    dico = {"A320": Parametres(34.1, 112.4, 73500, 25, 0.02, 281.11), "A330": Parametres(60.3, 361.6, 242000, 30, 0.025, 253.61),
            "A380": Parametres(60.3, 361.6, 242000, 30, 0.025, 523.61), "B777": Parametres(60.9, 427.8, 299000, 31.6, 0.025, 305.28),
            "B747": Parametres(64.4, 511, 396890, 37.5, 0.024, 313.89), "B737": Parametres(35.8, 124.6, 79000, 35.8, 0.02, 233.89),
            "B787": Parametres(60.1, 325, 227930, 32.2, 0.017, 262.5), "B727": Parametres(32.9, 164.3, 95000, 25, 0.03, 266.67)}

    return dico


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
    dico = {}
    monAtmo = Atmosphere(10000)
    dico["A320"] = Parametres(238, monAtmo, 34.1, 112.4, 73500, 25, 0.02)
    dico["A330"] = Parametres( 238, monAtmo, 60.3, 361.6, 242000, 30, 0.025)
    dico["A380"] = Parametres( 238, monAtmo, 60.3, 361.6, 242000, 30, 0.025)
    dico["B777"] = Parametres( 238, monAtmo, 60.9, 427.8, 299000, 31.6, 0.025)
    dico["B747"] = Parametres(238, monAtmo, 64.4, 511, 396890, 37.5, 0.024)
    dico["B737"] = Parametres( 238, monAtmo, 35.8, 124.6, 79000, 35.8, 0.02)
    dico["B787"] = Parametres( 238, monAtmo, 60.1, 325, 227930, 32.2, 0.017)
    dico["B727"] = Parametres(238, monAtmo, 32.9, 164.3, 95000, 25, 0.03)

    return dico


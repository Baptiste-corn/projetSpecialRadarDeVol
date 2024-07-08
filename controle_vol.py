"""
Pour modifier les paramètres aérodynamiques de l'avion
"""
from parametres import Parametres
from atmosphere import Atmosphere


def get_dict_parametre():
    dico = {}
    dico["A320"] = Parametres(34.1, 112.4, 73500, 25, 0.02)
    dico["A330"] = Parametres(60.3, 361.6, 242000, 30, 0.025)
    dico["A380"] = Parametres(60.3, 361.6, 242000, 30, 0.025)
    dico["B777"] = Parametres(60.9, 427.8, 299000, 31.6, 0.025)
    dico["B747"] = Parametres(64.4, 511, 396890, 37.5, 0.024)
    dico["B737"] = Parametres(35.8, 124.6, 79000, 35.8, 0.02)
    dico["B787"] = Parametres(60.1, 325, 227930, 32.2, 0.017)
    dico["B727"] = Parametres(32.9, 164.3, 95000, 25, 0.03)

    return dico


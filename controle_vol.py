"""
Contient la classe avion dont chaque objet est créé à partir de la récupération des API de FlightRadar24.

Utilisation (pour créer un objet) :

        Avoir créé un objet avion au préalable.

        Exemple :
        flight1.parametre = dico[flight1.modele]

Auteur : Baptiste Corn
"""

from classes.parametres import Parametres


def get_dict_parametre():
    dico = {"A320": Parametres(34.1, 112.4, 73500, 25, 0.02, 281.11),
            "A330": Parametres(60.3, 361.6, 242000, 30, 0.025, 253.61),
            "A380": Parametres(79.8, 845, 560000, 33.5, 0.024, 329.17),
            "B777": Parametres(60.9, 427.8, 299000, 31.6, 0.025, 305.28),
            "B747": Parametres(64.4, 511, 396890, 37.5, 0.024, 313.89),
            "B737": Parametres(35.8, 124.6, 79000, 35.8, 0.02, 233.89),
            "B787": Parametres(60.1, 325, 227930, 32.2, 0.017, 262.5),
            "B727": Parametres(32.9, 164.3, 95000, 25, 0.03, 266.67)}
    return dico

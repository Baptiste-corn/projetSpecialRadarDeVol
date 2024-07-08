"""
Fichier main de test API flightradar24
Modèles à viser :
- A320, A380, A330
- B777, B737, B787, B727, B747
"""

from FlightRadar24 import FlightRadar24API
import avion
import atmosphere
import entrees_utilisateur
from controle_vol import get_dict_parametre

fr_api = FlightRadar24API()
flight = fr_api.get_flights()


def main():
    """
    Fonction principale pour récupérer les données des vols, filtrer les avions souhaités,
    créer des objets Avion et Atmosphere, et interagir avec l'utilisateur ou l'administrateur.

    Cette fonction récupère les vols en cours, filtre les avions en fonction des modèles spécifiés,
    crée des objets Avion et Atmosphere pour chaque avion, et gère l'interaction avec l'utilisateur
    ou l'administrateur pour afficher ou modifier les données des vols.

    :return: liste_objets_avion (list) : Liste des objets Avion créés.
    """
    liste_modeles = ['A320', 'A330', 'A380', 'B777', 'B737', 'B787', 'B747', 'B727']
    liste_avions = []
    liste_atmo = []
    liste_objets_avion = []
    liste_objets_atmo = []
    liste_idd_avion = []

    # Récupération des vols pour les modèles spécifiés
    for i in range(len(flight)):
        if flight[i].aircraft_code in liste_modeles:
            liste_avions.append(flight[i])

    dico = get_dict_parametre()

    # Création des objets Avion (+ attribut de type objet Parametre avec le dictionnaire)
    # et Atmosphere pour chaque avion récupéré de l'API
    for j in range(len(liste_avions)):
        nouvel_avion = avion.Avion(liste_avions[j].aircraft_code, liste_avions[j].number, int(liste_avions[j].altitude * 0.3048)
                                   , liste_avions[j].ground_speed * 0.5144, liste_avions[j].heading, liste_avions[j].longitude
                                   , liste_avions[j].latitude)
        nouvel_avion.parametre = dico[nouvel_avion.modele]
        liste_objets_avion.append(nouvel_avion)
        liste_idd_avion.append(nouvel_avion.affichage_vol())

        liste_objets_atmo.append(atmosphere.Atmosphere(nouvel_avion.get_altitude()))

    # Affichage des vols et de leurs caractéristiques
    print('Voici la liste des avions actuellement en vol : \n')
    print("".join(liste_idd_avion))

    # Interactions utilisateur
    user = int(input('Etes-vous un utilisateur ou un admin ? \n1) Utilisateur \n2) Admin \n3) Quitter\n'))
    while user != 1 or user != 2:
        if user == 1:
            entrees_utilisateur.guest(liste_objets_avion)
            print(len(liste_objets_avion))
            return 0
        elif user == 2:
            numero_vol_to_modifier = input('Quel vol souhaitez vous modifier ?\n')
            entrees_utilisateur.tour_de_controle(liste_objets_avion, liste_objets_atmo, numero_vol_to_modifier, liste_idd_avion)
            return 0
        elif user == 3:
            return 0
        else:
            user = int(input('Etes-vous un utilisateur ou un admin ? \n1) Utilisateur \n2) Admin \n'))

    return liste_objets_avion


if __name__ == '__main__':
    main()

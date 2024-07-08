"""
Fichier main de test API flightradar24
Modèles à viser :
- A320, A380, A330
- B777, B737, B787, B727, B747
"""

from FlightRadar24 import FlightRadar24API
import avion
import atmosphere
import parametres
import entrees_utilisateur
from controle_vol import get_dict_parametre
import sphinx

fr_api = FlightRadar24API()
flight = fr_api.get_flights()


def main():
    liste_modeles = ['A320', 'A330', 'A380', 'B777', 'B737', 'B787', 'B747', 'B727']
    liste_avions = []
    liste_atmo = []
    liste_objets_avion = []
    liste_objets_atmo = []
    liste_idd_avion = []

    for i in range(len(flight)):
        if flight[i].aircraft_code in liste_modeles:
            liste_avions.append(flight[i])

    print(liste_avions)
    print('TEST : ', liste_avions[0].registration)

    dico = get_dict_parametre()

    for j in range(len(liste_avions)): # modele = liste... . aircraft_code
        nouvel_avion = avion.Avion(liste_avions[j].aircraft_code, liste_avions[j].number, int(liste_avions[j].altitude * 0.3048)
                                   , liste_avions[j].ground_speed * 0.5144, liste_avions[j].heading, liste_avions[j].longitude
                                   , liste_avions[j].latitude)
        nouvel_avion.parametre = dico[nouvel_avion.modele]  # modele de la classe Avion = aircraft code de l'API
        liste_objets_avion.append(nouvel_avion)
        liste_idd_avion.append(nouvel_avion.affichage_vol())

        liste_objets_atmo.append(atmosphere.Atmosphere(nouvel_avion.get_altitude()))

    print('Voici la liste des avions actuellement en vol : \n')
    print("".join(liste_idd_avion))

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

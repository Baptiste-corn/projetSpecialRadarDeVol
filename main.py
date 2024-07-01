"""
Fichier main de test API flightradar24
Modèles à viser :
- A320, A380, A330
- B777, B737, B787, B727, B747
"""

from FlightRadar24 import FlightRadar24API
import Avion
import entrees_utilisateur
import numpy as np

fr_api = FlightRadar24API()
flight = fr_api.get_flights()


def main():
    liste_modeles = ['A320', 'A330', 'A380', 'B777', 'B737', 'B787', 'B747', 'B727']
    liste_avions = []
    liste_objets = []

    for i in range(len(flight)):
        if flight[i].aircraft_code in liste_modeles:
            liste_avions.append(flight[i])

    print(liste_avions)

    for j in range(len(liste_avions)):
        nouvel_avion = Avion.Avion(liste_avions[j].aircraft_code, liste_avions[j].number, liste_avions[j].altitude
                                   , liste_avions[j].ground_speed, liste_avions[j].heading, liste_avions[j].longitude
                                   , liste_avions[j].latitude)
        liste_objets.append(nouvel_avion)

    user = int(input('Etes-vous un utilisateur ou un admin ? \n1) Utilisateur \n2) Admin '))
    while user != 1 or user != 2:
        if user == 1:
            entrees_utilisateur.guest(liste_objets)
            break
        elif user == 2:
            print('prout')
        # entrees_utilisateur.tour_de_controle()
        else:
            user = int(input('Etes-vous un utilisateur ou un admin ? \n1) Utilisateur \n2) Admin '))

    return liste_objets


if __name__ == '__main__':
    main()

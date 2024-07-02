"""
Fichier main de test API flightradar24
Modèles à viser :
- A320, A380, A330
- B777, B737, B787, B727, B747
"""

from FlightRadar24 import FlightRadar24API
import Avion
import Atmopshere
import entrees_utilisateur
import numpy as np

fr_api = FlightRadar24API()
flight = fr_api.get_flights()


def main():
    liste_modeles = ['A320', 'A330', 'A380', 'B777', 'B737', 'B787', 'B747', 'B727']
    liste_avions = []
    liste_atmo = []
    liste_objets_avion = []
    liste_objets_atmo = []

    for i in range(len(flight)):
        if flight[i].aircraft_code in liste_modeles:
            liste_avions.append(flight[i])

    print(liste_avions)
    print('TEST : ', liste_avions[0].registration)

    for j in range(len(liste_avions)):
        nouvel_avion = Avion.Avion(liste_avions[j].aircraft_code, liste_avions[j].number, liste_avions[j].altitude
                                   , liste_avions[j].ground_speed, liste_avions[j].heading, liste_avions[j].longitude
                                   , liste_avions[j].latitude)
        liste_objets_avion.append(nouvel_avion)

        liste_objets_atmo.append(Atmopshere.Atmosphere(nouvel_avion.get_altitude()))

    print(liste_objets_avion[0].get_altitude(), liste_objets_atmo[0].get_temperature(), liste_objets_atmo[0].temperature())

    user = int(input('Etes-vous un utilisateur ou un admin ? \n1) Utilisateur \n2) Admin \n3) Quitter'))
    while user != 1 or user != 2:
        if user == 1:
            entrees_utilisateur.guest(liste_objets_avion)
            break
        elif user == 2:
            numero_vol_to_modifier = input('Quel vol souhaitez vous modifier ?')
            entrees_utilisateur.tour_de_controle(liste_objets_avion, liste_objets_atmo, numero_vol_to_modifier)
        elif user == 3:
            return 0
        else:
            user = int(input('Etes-vous un utilisateur ou un admin ? \n1) Utilisateur \n2) Admin '))

    return liste_objets_avion


if __name__ == '__main__':
    main()
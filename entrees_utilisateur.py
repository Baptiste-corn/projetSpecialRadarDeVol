"""

"""
import gestion_cartopy as gc
import Avion
import Atmopshere


def guest(avions):
    gc.affichage_carte(avions)


def tour_de_controle(avions: list[Avion], numero_vol):
    for x in range(len(avions)):
        print(avions[x].get_numero_vol(), avions[x].get_altitude())
    avion = input('Avec quel avion voulez-vous intéragir ?\n')
    choix = int(input('Quel paramètre de vol souhaitez-vous modifier ?  \n1) Altitude \n2) Vitesse ?'))
    avion_a_modifier = ''

    while choix != 1 or choix != 2:
        if choix == 1:
            for i in range(len(avions)):
                if avions[i].get_numero_vol() == avion:
                    print('Vous souhaitez modifier l altitude du vol suivant : ', avions[i].get_numero_vol()
                          , 'volant à l altitude :', avions[i].get_altitude())
                    avion_a_modifier = avions[i]
                    break
            nouvelle_altitude = int(input('Quelle est la nouvelle altitude à atteindre pour ce vol ?'))
            avion_a_modifier.set_altitude(nouvelle_altitude)
            for c in range(len(avions)):
                print(avions[c].get_numero_vol(), avions[c].get_altitude())


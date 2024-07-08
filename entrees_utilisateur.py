from classes import atmosphere, avion
from affichage import gestion_courbes, gestion_cartopy as gc


def guest(avions):
    """
    Fonction pour afficher une carte des avions.

    :param avions: Liste des objets Avion à afficher sur la carte.
    :return: Aucune valeur de retour spécifiée.
    """
    gc.affichage_carte(avions)


def tour_de_controle(avions: list[avion], atmospheres: list[atmosphere], numero_vol, liste_idd_avion):
    """
    Permet de modifier les paramètres de vol (altitude ou vitesse) d'un avion spécifique.

    Cette fonction demande à l'utilisateur quel paramètre (altitude ou vitesse) il souhaite modifier pour un vol
    spécifique. Elle met à jour l'altitude ou la vitesse de l'avion et ajuste les paramètres atmosphériques
    correspondants. Elle génère ensuite des courbes pour visualiser les changements.

    :param avions: Liste des objets avion contenant les informations des vols.
    :param atmospheres: Liste des objets atmosphere correspondant à chaque avion.
    :param numero_vol: Numéro de vol de l'avion dont les paramètres doivent être modifiés.
    :param liste_idd_avion: Liste des identifiants des avions pour affichage.
    :return: None
    """
    choix = ""

    while not choix.isnumeric():
        choix = input('Quel paramètre de vol souhaitez-vous modifier ?  \n1) Altitude \n2) Vitesse ?')
    choix = int(choix)

    ex_altitude = 0
    ex_temp = 0
    ex_vitesse = 0
    ex_densite = 0
    ex_coef_portance = 0
    ex_coef_trainee = 0
    ex_trainee = 0
    ex_finesse = 0

    print("".join(liste_idd_avion))

    while choix != 1 or choix != 2:
        if choix == 1:
            for i in range(len(avions)):
                if avions[i].get_numero_vol() == numero_vol:
                    print(f'Vous souhaitez modifier l altitude du vol suivant :  '
                          f'{avions[i].get_numero_vol()} volant à l altitude {int(avions[i].altitude)}m')

                    avion_a_modifier = avions[i]
                    atmo_a_modifier = atmospheres[i]
                    ex_altitude = avion_a_modifier.get_altitude()
                    ex_temp = atmo_a_modifier.temperature()
                    ex_vitesse = avion_a_modifier.ground_speed
                    ex_densite = atmo_a_modifier.density()[0]
                    ex_coef_portance = avion_a_modifier.parametre.cl_avec_portance(ex_vitesse, ex_densite)
                    ex_coef_trainee = avion_a_modifier.parametre.coef_trainee_2(ex_vitesse, ex_densite)
                    ex_trainee = avion_a_modifier.parametre.trainee(ex_vitesse, ex_densite)
                    ex_finesse = avion_a_modifier.parametre.finesse(ex_vitesse, ex_densite)

            nouvelle_altitude = ""
            while not nouvelle_altitude.isnumeric():
                nouvelle_altitude = input('Quelle est la nouvelle altitude en mètres à atteindre pour ce vol ?')
            nouvelle_altitude = int(nouvelle_altitude)
            avion_a_modifier.set_altitude(nouvelle_altitude)
            atmo_a_modifier.set_altitude(nouvelle_altitude)

            gestion_courbes.courbe_atmo_temperature(atmo_a_modifier, ex_altitude, ex_temp, ex_densite, ex_finesse, avion_a_modifier)
            break

        elif choix == 2:
            for i in range(len(avions)):
                if avions[i].get_numero_vol() == numero_vol:
                    print(f'Vous souhaitez modifier la vitesse du vol suivant : {avions[i].get_numero_vol()}'
                          f', volant à la vitesse : {avions[i].get_ground_speed()} m/s')
                    avion_a_modifier = avions[i]
                    atmo_a_modifier = atmospheres[i]
                    ex_altitude = avion_a_modifier.get_altitude()
                    ex_temp = atmo_a_modifier.temperature()
                    ex_vitesse = avion_a_modifier.ground_speed
                    ex_densite = atmo_a_modifier.density()[0]
                    ex_coef_portance = avion_a_modifier.parametre.cl_avec_portance(ex_vitesse, ex_densite)
                    ex_coef_trainee = avion_a_modifier.parametre.coef_trainee_2(ex_vitesse, ex_densite)
                    ex_trainee = avion_a_modifier.parametre.trainee(ex_vitesse, ex_densite)
                    ex_finesse = avion_a_modifier.parametre.finesse(ex_vitesse, ex_densite)
                    break
            while 1:
                try:
                    nouvelle_vitesse = float(input('Quelle est la nouvelle vitesse à atteindre pour ce vol ?'))
                    break
                except ValueError:
                    print('Mauvaise entrée, veuillez réessayer.')

            avion_a_modifier.set_ground_speed(nouvelle_vitesse)

            gestion_courbes.courbe_coefs_finesse_pour_vitesse(atmo_a_modifier, ex_altitude, ex_vitesse, ex_coef_portance, ex_coef_trainee, ex_trainee, ex_finesse, avion_a_modifier)
            break

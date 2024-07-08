import matplotlib.pyplot as plt
import numpy as np
import math


def courbe_atmo_temperature(atmosphere, ex_altitude, ex_temperature, ex_densite, ex_finesse, avion):
    """
    Génère des courbes de température, densité et finesse selon l'altitude avant et après modification.

    Cette fonction crée des graphiques montrant les distributions de la température, de la densité et de la finesse
    en fonction de l'altitude pour un avion spécifique avant et après une modification de l'altitude de vol.
    Les courbes tracées sont basées sur des modèles déjà existants et servent de validation des données transformées.

    :param atmosphere: Objet atmosphere contenant les informations atmosphériques.
    :param ex_altitude: Altitude avant modification.
    :param ex_temperature: Température avant modification.
    :param ex_densite: Densité avant modification.
    :param ex_finesse: Finesse avant modification.
    :param avion: Objet avion contenant les informations du vol.
    :return: None
    """
    # Récupérartion des valeurs après la modification de la vitesse (valeurs actuelles des attributs des objets)
    altitude_apres = atmosphere.get_altitude()
    temperature_apres = atmosphere.get_temperature()
    densite_apres = atmosphere.density()[0]
    finesse_apres = avion.parametre.finesse(avion.ground_speed, atmosphere.density()[0])

    # Valeurs de début et de fin des listes pour les axes des courbes
    altitude_start = 0
    altitude_end = 15000
    altitude_transition = 11000

    # Trouver le plus grand commun diviseur (GCD) pour s'assurer que l'incrément est un diviseur commun
    gcd = math.gcd(altitude_end, altitude_transition)

    # Calculer le nombre de points nécessaires
    N = 150000 // gcd + 1

    # Créer le linspace pour l'altitude
    axe_altitude = np.linspace(altitude_start, altitude_end, N)

    # Vérifier où se trouve 11000 mètres
    index_transition = np.where(axe_altitude == altitude_transition)[0][0]

    # Créer les linspace pour la température
    temperature_part1 = np.linspace(288.15, 216.66, index_transition + 1)
    temperature_part2 = np.full(N - index_transition - 1, 216.66)

    # Combiner les deux parties
    # Cet axe s'assure de la validation des états avant modif et après modif
    axe_temp_concatene = np.concatenate((temperature_part1, temperature_part2))

    # Cet axe s'assure de la validation des états avant modif et après modif
    axe_densite = np.linspace(1.225, 0.195, N)

    # Cet axe s'assure de la validation des états avant modif et après modif
    axe_finesse = np.linspace(avion.parametre.finesse(avion.ground_speed, 1.225),
                              avion.parametre.finesse(avion.ground_speed, 0.195), N)

    plt.figure()
    plt.plot(axe_altitude, axe_temp_concatene)
    plt.scatter(altitude_apres, temperature_apres, label='Après modif')
    plt.scatter(ex_altitude, ex_temperature, label='Avant modif')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Température (K)')
    plt.title('Distribution de la température selon l altitude pour le vol ' + str(avion.get_numero_vol()))
    plt.legend()
    plt.grid(True)

    plt.figure()
    plt.plot(axe_altitude, axe_densite)
    plt.scatter(altitude_apres, densite_apres, label='Apres modif')
    plt.scatter(ex_altitude, ex_densite, label='Avant modif')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Densité (kg/m3)')
    plt.title('Distribution de la densité selon l altitude pour le vol ' + str(avion.numero_vol))
    plt.legend()
    plt.grid(True)

    plt.figure()
    plt.plot(axe_altitude, axe_finesse)
    plt.scatter(altitude_apres, finesse_apres, label='Apres modif')
    plt.scatter(ex_altitude, ex_finesse, label='Avant modif')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Finesse')
    plt.title('Distribution de la finesse selon l altitude pour le vol ' + str(avion.numero_vol))
    plt.legend()
    plt.grid(True)

    plt.show()


def courbe_coefs_finesse_pour_vitesse(atmosphere, ex_altitude, ex_vitesse, ex_coef_portance, ex_coef_trainee, ex_trainee, ex_finesse, avion):
    """
    Génère des courbes de coefficients de portance, de traînée, de traînée et de finesse selon la vitesse
    avant et après modification.

    Cette fonction crée des graphiques montrant les distributions des coefficients de portance, de traînée,
    de la traînée et de la finesse en fonction de la vitesse pour un avion spécifique avant et après une modification
    de la vitesse de vol.
    Les courbes tracées sont basées sur des modèles déjà existants et servent de validation des données transformées.

    :param atmosphere: Objet atmosphere contenant les informations atmosphériques.
    :param ex_altitude: Altitude avant modification.
    :param ex_vitesse: Vitesse avant modification.
    :param ex_coef_portance: Coefficient de portance avant modification.
    :param ex_coef_trainee: Coefficient de traînée avant modification.
    :param ex_trainee: Traînée avant modification.
    :param ex_finesse: Finesse avant modification.
    :param avion: Objet avion contenant les informations du vol.
    :return: None
    """
    coefficients_portance = []
    coefficients_trainee = []
    trainee = []
    finesse = []

    altitude_apres = atmosphere.altitude
    coef_portance_apres = avion.parametre.cl_avec_portance(avion.parametre.vitesse_convertie(avion.ground_speed), atmosphere.density()[0])
    coef_trainee_apres = avion.parametre.coef_trainee_2(avion.parametre.vitesse_convertie(avion.ground_speed), atmosphere.density()[0])
    trainee_apres = avion.parametre.trainee(avion.parametre.vitesse_convertie(avion.ground_speed), atmosphere.density()[0])
    finesse_apres = avion.parametre.finesse(avion.parametre.vitesse_convertie(avion.ground_speed), atmosphere.density()[0])

    # Ces axes s'assurent de la validation des états avant modif et après modif
    axe_altitude = np.linspace(0, 15000, 100)
    axe_vitesse = np.linspace(50, avion.parametre.vitesse_max, 100)

    # Fonctions pour calculer les listes de coefficients et finesse selon la vitesse
    def liste_coef_portance():
        """
        Calcule les coefficients de portance pour une gamme de vitesses.

        Cette fonction génère une liste des coefficients de portance (Cl) pour des vitesses allant de 50 m/s
        à la vitesse maximale de l'avion, en utilisant la densité de l'atmosphère actuelle.

        :return: Liste des coefficients de portance.
        """
        for i in range(100):
            coefficients_portance.append(avion.parametre.cl_avec_portance(axe_vitesse[i], atmosphere.density()[0]))
        return coefficients_portance

    def liste_coef_trainee():
        """
        Calcule les coefficients de traînée pour une gamme de vitesses.

        Cette fonction génère une liste des coefficients de traînée (Cd) pour des vitesses allant de 50 m/s
        à la vitesse maximale de l'avion, en utilisant la densité de l'atmosphère actuelle.

        :return: Liste des coefficients de traînée.
        """
        for i in range(100):
            coefficients_trainee.append(avion.parametre.coef_trainee_2(axe_vitesse[i], atmosphere.density()[0]))
        return coefficients_trainee

    def liste_trainee():
        """
        Calcule la traînée pour une gamme de vitesses.

        Cette fonction génère une liste de la traînée (en Newtons) pour des vitesses allant de 50 m/s
        à la vitesse maximale de l'avion, en utilisant la densité de l'atmosphère actuelle.

        :return: Liste de la traînée.
        """
        for i in range(100):
            trainee.append(avion.parametre.trainee(axe_vitesse[i], atmosphere.density()[0]))
        return trainee

    def liste_finesse():
        """
        Calcule la finesse pour une gamme de vitesses.

        Cette fonction génère une liste de la finesse (rapport portance/traînée) pour des vitesses allant de 50 m/s
        à la vitesse maximale de l'avion, en utilisant la densité de l'atmosphère actuelle.

        :return: Liste de la finesse.
        """
        for i in range(100):
            finesse.append(avion.parametre.finesse(axe_vitesse[i], atmosphere.density()[0]))
        return finesse

    plt.figure()
    plt.plot(axe_vitesse, liste_coef_portance())
    plt.scatter(avion.parametre.vitesse_convertie(avion.ground_speed), coef_portance_apres, label='Apres modif')
    plt.scatter(ex_vitesse, ex_coef_portance, label='Avant modif')
    plt.xlabel('Vitesse (m/s)')
    plt.ylabel('Cl')
    plt.title('Distribution du coefficient de portance selon la vitesse pour le vol ' + str(avion.numero_vol))
    plt.legend()
    plt.grid(True)

    plt.figure()
    plt.plot(axe_vitesse, liste_coef_trainee())
    plt.scatter(avion.parametre.vitesse_convertie(avion.ground_speed), coef_trainee_apres, label='Apres modif')
    plt.scatter(ex_vitesse, ex_coef_trainee, label='Avant modif')
    plt.xlabel('Vitesse (m/s)')
    plt.ylabel('Cd')
    plt.title('Distribution du coefficient de trainee selon la vitesse pour le vol ' + str(avion.numero_vol))
    plt.legend()
    plt.grid(True)

    plt.figure()
    plt.plot(axe_vitesse, liste_trainee())
    plt.scatter(avion.parametre.vitesse_convertie(avion.ground_speed), trainee_apres, label='Apres modif')
    plt.scatter(ex_vitesse, ex_trainee, label='Avant modif')
    plt.xlabel('Vitesse (m/s)')
    plt.ylabel('Trainee (N)')
    plt.title('Distribution de la traînée selon la vitesse pour le vol ' + str(avion.numero_vol))
    plt.legend()
    plt.grid(True)

    plt.figure()
    plt.plot(axe_vitesse, liste_finesse())
    plt.scatter(avion.parametre.vitesse_convertie(avion.ground_speed), finesse_apres, label='Apres modif')
    plt.scatter(ex_vitesse, ex_finesse, label='Avant modif')
    plt.xlabel('Vitesse (m/s)')
    plt.ylabel('Finesse L/D')
    plt.title('Distribution de la finesse selon la vitesse pour le vol ' + str(avion.numero_vol))
    plt.legend()
    plt.grid(True)

    plt.show()

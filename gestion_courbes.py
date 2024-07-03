"""

"""
import avion
import atmosphere
import parametres
import matplotlib.pyplot as plt
import numpy as np


def courbe_atmo_temperature(atmosphere, ex_altitude, ex_temperature, ex_densite, avion):
    altitude_apres = atmosphere.get_altitude()
    temperature_apres = atmosphere.get_temperature()
    densite_apres = atmosphere.density()[0]

    axe_temp1 = np.linspace(288.15, 223.26, 64)
    axe_temp2 = np.linspace(216.66, 216.66, 36)
    axe_temp_concatene = np.concatenate((axe_temp1,axe_temp2))

    axe_densite = np.linspace(1.225, 0.195, 100)

    axe_altitude = np.linspace(0, 15000, 100)

    plt.figure()
    plt.plot(axe_altitude, axe_temp_concatene)
    plt.scatter(altitude_apres, temperature_apres, label='Après modif')
    plt.scatter(ex_altitude * 0.3048, ex_temperature, label='Avant modif')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Température (K)')
    plt.title('Distribution de la température selon l altitude pour le vol ' + str(avion.get_numero_vol()))
    plt.legend()
    plt.grid(True)

    plt.figure()
    plt.plot(axe_altitude, axe_densite)
    plt.scatter(altitude_apres, densite_apres, label='Apres modif')
    plt.scatter(ex_altitude * 0.3048, ex_densite, label='Avant modif')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Densité (kg/m3)')
    plt.title('Distribution de la densité selon l altitude pour le vol ' + str(avion.numero_vol))
    plt.legend()
    plt.grid(True)

    plt.show()


def courbe_coefs_finesse_pour_vitesse(atmosphere, ex_altitude, ex_vitesse, ex_coef_portance, ex_coef_trainee, ex_trainee, ex_finesse, avion):
    coefficients_portance = []
    coefficients_trainee = []
    trainee = []
    finesse = []

    altitude_apres = atmosphere.altitude
    coef_portance_apres = avion.parametre.cl_avec_portance(avion.parametre.vitesse_convertie(avion.ground_speed), atmosphere.density()[0])
    coef_trainee_apres = avion.parametre.coef_trainee_2(avion.parametre.vitesse_convertie(avion.ground_speed), atmosphere.density()[0])
    trainee_apres = avion.parametre.trainee(avion.parametre.vitesse_convertie(avion.ground_speed), atmosphere.density()[0])
    finesse_apres = avion.parametre.finesse(avion.parametre.vitesse_convertie(avion.ground_speed), atmosphere.density()[0])

    axe_altitude = np.linspace(0, 15000, 100)
    axe_vitesse = np.linspace(10, avion.parametre.vitesse_max, 100)

    def liste_coef_portance():
        for i in range(100):
            coefficients_portance.append(avion.parametre.cl_avec_portance(axe_vitesse[i], atmosphere.density()[0]))
        return coefficients_portance

    def liste_coef_trainee():
        for i in range(100):
            coefficients_trainee.append(avion.parametre.coef_trainee_2(axe_vitesse[i], atmosphere.density()[0]))
        return coefficients_trainee

    def liste_trainee():
        for i in range(100):
            trainee.append(avion.parametre.trainee(axe_vitesse[i], atmosphere.density()[0]))
        return trainee

    def liste_finesse():
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

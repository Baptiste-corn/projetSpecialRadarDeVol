"""

"""
import avion
import atmosphere
import matplotlib.pyplot as plt
import numpy as np


def courbe_atmo_temperature(atmosphere, ex_altitude, ex_temperature, avion):
    altitude_avant = ex_altitude
    temperature_avant = ex_temperature
    altitude_apres = atmosphere.get_altitude()
    temperature_apres = atmosphere.get_temperature()

    axe_temp1 = np.linspace(288.15, 223.26, 64)
    axe_temp2 = np.linspace(216.66, 216.66, 36)
    axe_temp_concatene = np.concatenate((axe_temp1,axe_temp2))

    axe_altitude = np.linspace(0, 15000, 100)

    plt.plot(axe_altitude, axe_temp_concatene, label='Distribution de la température selon l altitude pour le vol '
                                                    + str(avion.get_numero_vol()))
    plt.scatter(altitude_apres, temperature_apres, label='Après modif')
    plt.scatter(altitude_avant * 0.3048, temperature_avant, label='Avant modif')

    plt.xlabel('Altitude (m)')
    plt.ylabel('Température (K)')
    plt.legend()
    plt.grid(True)

    plt.show()

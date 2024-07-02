"""

"""
import avion
import atmosphere
import matplotlib.pyplot as plt
import numpy as np

def courbe_atmo_temperature(atmosphere, ex_altitude, ex_temperature):
    altitude_avant = ex_altitude
    temperature_avant = ex_temperature
    altitude_apres = atmosphere.get_altitude()
    temperature_apres = atmosphere.get_temperature()

    axe_temp = np.linspace(288.15, )

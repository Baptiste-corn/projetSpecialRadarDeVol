# Basée sur la classe atmosphere vu en cours
import math


class Atmosphere:
    def __init__(self, altitude):
        self.altitude = altitude * 0.3048
        self.liste_temperature = [
            (0, 288.15, 101.235, 1.225),
            (1000, 281.65, 89.876, 1.1117),
            (2000, 275.15, 79.501, 1.007),
            (3000, 268.67, 70.121, 0.9093),
            (4000, 262.18, 61.66, 0.8193),
            (5000, 255.69, 54.048, 0.7364),
            (6000, 249.2, 47.217, 0.6601),
            (7000, 242.71, 41.105, 0.59),
            (8000, 236.23, 35.651, 0.526),
            (9000, 229.74, 30.8, 0.467),
            (10000, 223.26, 26.5, 0.413),
            (11000, 216.78, 22.7, 0.365),
            (12000, 216.66, 19.399, 0.312),
            (13000, 216.66, 16.579, 0.267),
            (14000, 216.66, 14.17, 0.228),
            (15000, 216.66, 12.112, 0.195)
        ]

    def get_altitude(self):
        return self.altitude

    def get_temperature(self):
        for altitude, temperature, _, _ in self.liste_temperature:
            if self.altitude <= altitude:
                return temperature
        return self.liste_temperature[-1][1]

    def density(self):

        g = 9.81  # m/s^2
        M = 0.0289644  # kg/mol - Masse molaire de l'air
        R = 8.31447  # J/(mol*K) - Constante des gaz parfaits
        T0 = 288.15  # K - Température standard au niveau de la mer
        p0 = 101325  # Pa - Pression standard au niveau de la mer
        rayonTerre = 6371  # km
        gravity = 6.674 * 10**(-11) * (rayonTerre/(rayonTerre + self.altitude))**2
        pressure = p0 * (1 - 0.0000225577 * self.altitude) ** 5.25588  # Pa - https://fr.wikipedia.org/wiki/Formule_du_nivellement_barom%C3%A9trique
        density = pressure * M / (R * self.get_temperature())  # kg/m^3 - Densité de l'air en fonction de la pression et de la température, equation gaz parfait
        return density, pressure, gravity

    def speed_of_sound(self):
        # Supposons que la vitesse du son dans l'air dépende de la température selon la formule suivante :
        # a = sqrt(gamma * R * T), où gamma est le coefficient de dilatation adiabatique de l'air,
        # R est la constante spécifique de l'air, T est la température en Kelvin
        gamma = 1.4  # coefficient de dilatation adiabatique de l'air
        R = 287  # J/kg/K
        T = self.temperature()
        return math.sqrt(gamma * R * T)

    def temperature(self):
        # Supposons que la température de l'air diminue avec l'altitude selon la formule suivante :
        # T = T0 - L * h, où T0 est la température à une altitude de 0 mètres,
        # L est la constante de gradient thermique, et h est l'altitude en mètres
        T0 = 288.15  # K
        L = 0.0065  # K/m
        return T0 - L * self.altitude

    def gravite(self):
        rayonTerre = 6371  # km
        gravite = 6.674 * 10 ** (-11) * (rayonTerre / (rayonTerre + self.altitude)) ** 2
        return gravite

    def set_altitude(self, nouvelle_altitude):
        self.altitude = nouvelle_altitude

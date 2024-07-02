from atmosphere import Atmosphere
import math
class Parametres:
    def __init__(self, ground_speed, atmosphere:Atmosphere, envergure, surface, masse, angle_fleche, cd0):
        self.ground_speed = ground_speed  # noeuds
        self.atmosphere = atmosphere
        self.envergure = envergure
        self.surface = surface
        self.masse = masse
        self.angle_fleche = angle_fleche
        self.cd0 = cd0

    def get_ground_speed(self):
        return self.ground_speed

    def get_envergure(self):
        return self.envergure

    def get_surface(self):
        return self.surface

    def get_masse(self):
        return self.masse

    def get_atmosphere(self):
        return self.atmosphere

    def get_angle_fleche(self):
        return self.angle_fleche

    def get_cd0(self):
        return self.cd0

    def portance_L(self):
        return self.masse * 9.81  # Vol en palier
    
    def cl_avec_portance (self):
        return self.portance_L() / (0.5 * self.atmosphere.density()[0] * self.surface * self.ground_speed**2)

    def allongement_AR_2(self):
        return self.envergure**2 / self.surface

    def oswald_factor_e_2(self):
        if self.get_angle_fleche() > 30:
            return 4.61 * (1 - 0.045 * self.allongement_AR_2() ** 0.68) * (math.cos(self.angle_fleche)) ** 0.15 - 3.1
        else:
            return 0.8

    def correction_k_2(self):
        return 1 / (math.pi * self.oswald_factor_e_2() * self.allongement_AR_2())

    def coef_trainee_2(self):
        return self.get_cd0() + self.correction_k_2() * self.cl_avec_portance()
    def trainee(self):
        return 0.5 * self.atmosphere.density()[0] * self.get_ground_speed() **2 * self.get_surface() * self.coef_trainee_2()

    def finesse(self):
        return self.cl_avec_portance() / self.coef_trainee_2()

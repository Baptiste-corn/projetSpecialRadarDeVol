from atmosphere import Atmosphere
class Avion:
    def __init__(self, altitude, ground_speed,
                 atmosphere, envergure, surface, masse, angle_fleche,
                 cd0
                 ):
        self.altitude = altitude  # mètres
        self.ground_speed = ground_speed # noeuds
        self.atmosphere = atmosphere
        self.envergure = envergure
        self.surface = surface
        self.masse = masse
        self.angle_fleche = angle_fleche
        self.cd0 = cd0
        # heading
        # Consommation
        #Temps de vol
        # ...

    def get_altitude(self):
        return self.altitude
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
    def affichage(self):
        print(f'Les caractéristiques de l\'avion sont : '
              f'\nAltitude = {self.altitude} mètres'
              f'\nVitesse au sol = {self.ground_speed} noeuds')


    def conditions_atmospheriques(self):
        temperature = self.atmosphere.get_temperature()
        densite = self.atmosphere.get_density()
        vitesse_du_son = self.atmosphere.speed_of_sound()

        return temperature, vitesse_du_son, densite



monAtmopshere = Atmosphere(10000)
#monAvion = Avion(10000, 500, monAtmopshere)
#Avion.affichage(monAvion)
#print(Avion.conditions_atmospheriques(monAvion))
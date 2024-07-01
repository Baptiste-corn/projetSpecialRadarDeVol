from atmosphere import Atmosphere
class Avion:
    def __init__(self, altitude, ground_speed, atmosphere):
        self.altitude = altitude  # mètres
        self.ground_speed = ground_speed # noeuds
        self.atmosphere = atmosphere
        # heading
        # Consommation
        #Temps de vol
        # ...

    def get_ground_speed(self):
        return self.ground_speed
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
monAvion = Avion(10000, 500, monAtmopshere)
Avion.affichage(monAvion)
print(Avion.conditions_atmospheriques(monAvion))
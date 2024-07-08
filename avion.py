"""
Contient la classe avion dont chaque objet est créé à partir de la récupération des API de FlightRadar24.

Utilisation (pour créer un objet) :

        flight1 = avion.Avion(modele, numero_vol, altitude, ground_speed, heading, lon, lat)

        Exemple :
        flight1 = avion.Avion("A380", "D521", 6500, 230, 265, 21.8, 39.2)

Auteurs : Baptiste Corn, Augustin Montredon
"""


class Avion:
    def __init__(self, modele, numero_vol, altitude, ground_speed, heading, lon, lat):
        self.modele = modele
        self.numero_vol = numero_vol
        self.altitude = altitude
        self.ground_speed = ground_speed
        self.heading = heading
        self.lon = lon
        self.lat = lat
        self.parametre = None  # On initialise plus tard

    def get_modele(self):
        return self.modele

    def get_numero_vol(self):
        return self.numero_vol

    def get_altitude(self):
        return self.altitude

    def get_ground_speed(self):
        return self.ground_speed

    def get_heading(self):
        return self.heading

    def get_lon(self):
        return self.lon

    def get_lat(self):
        return self.lat

    def set_altitude(self, nouvelle_altitude):
        self.altitude = nouvelle_altitude

    def set_ground_speed(self, nouvelle_vitesse):
        self.ground_speed = nouvelle_vitesse

    # Retourne les informations souhaitées et principales
    def affichage_vol(self):
        return ('<' + self.modele + '>' + ' - ' + self.numero_vol + ' - ' + 'Altitude : ' + str(self.altitude) + ' - '
                + 'Vitesse : ' + str(self.ground_speed) + ' - ' + 'Heading : ' + str(self.heading) + '\n')

# projetSpecialRadarDeVol

## Classes 
### Atmosphère
Cette classe contient une altitude et un tuple avec des altitudes et la température, pression et densité associée. Ce tuple sert principalement à comparer les valeurs des différentes propriétés atmosphériques issues de nos calculs avec la table. Nous allons aborder les fonctions qui nécessitent des éclaircissements : 

#### density(self)
Permet de calculer calculer et retourner la densité, la pression et la gravité terrestre, seuls les deux premiers paramètres sont utilisés. 

#### temperature(self)
Retourne la température en faisant la distinction entre la troposphère et la stratosphère. 

### Avion
Cette classe permet de créer notre l'avion ansi que ses informations de vol. Cette classe a pour attributs le modèle de l'avion, le numéro de vol, l'altitude, la vitesse, la direction, la longitude et la latitude en guise de coordonnées géographiques. Le dernier atttribut est un objet de la classe Paramètres.
#### affichage_vol(self)
Permet d'afficher de manière claire les paramètres de l'avion, l'affichage proposé par l'API manque de précision et lisibilité. 

### Paramètres
Cette classe est utilisée pour calculer les paramètres aérodynamiques de l'avion. Ses attributes sont les suivants : l'envergure, la surface, la masse, l'angle de flèche, le coefficient de trainée parasite à portance nulle et la vitesse maximale de l'avion.

#### portance_L(self)
Retourne la portance à partir de la masse de l'avion. 

#### trainee(self)
Permet de calculer la trainée totale de l'avion en utilisant d'autres paramètres tel que l'allongement, le coefficient de trainée calculées au préalable. 

### finesse(self)
Quotient de la portance et de la trainée, représentant l'efficacité de l'aile ou de l'avion. Plus elle est élevée, plus l'avion ira loin en consommant peu de carburant. 







# projetSpecialRadarDeVol
## Objectifs
Le projet Spécial FlightRadar permet de simuler l'impact d'un changement dans un paramètre physique d'un vol (pour l'instant uniquement altitude et vitesse) sur ses performances aéronautiques. Utiliser le mode Admin au lancement pour ce faire.  
Plus spécifiquement, le projet est orienté en 3 axes : 
- Récupération des données des vols via un API;
- Transformation de ces données via des entrées utilisateur;
- Validation des résultats via des courbes basées sur des modèles existants.

Il permet aussi de visualiser les vols sur une carte via le mode Utilisateur au lancement. 
## Contenu du repository
### Documentation Sphinx
Pour y accéder, télécharger tout le dossier du repository, éxecuter le main.py puis se rendre dans Pycharm et dans :
- le dossier build
- puis html
- puis ouvrir le fichier index.html avec un navigateur.
### Dossier 110m_cultural
Nécéssite d'être installé dans le même dossier que le projet. Il contient le fichier d'affichage de la carte du monde.
### Module classes
#### Classe Atmosphère
Cette classe contient une altitude et un tuple avec des altitudes et la température, pression et densité associée. Ce tuple sert principalement à comparer les valeurs des différentes propriétés atmosphériques issues de nos calculs avec la table. Nous allons aborder les fonctions qui nécessitent des éclaircissements : 

##### density(self)
Permet de calculer calculer et retourner la densité, la pression et la gravité terrestre, seuls les deux premiers paramètres sont utilisés. 

##### temperature(self)
Retourne la température en faisant la distinction entre la troposphère et la stratosphère. 

#### Classe Avion
Cette classe permet de créer notre l'avion ansi que ses informations de vol. Cette classe a pour attributs le modèle de l'avion, le numéro de vol, l'altitude, la vitesse, la direction, la longitude et la latitude en guise de coordonnées géographiques. Le dernier atttribut est un objet de la classe Paramètres.
##### affichage_vol(self)
Permet d'afficher de manière claire les paramètres de l'avion, l'affichage proposé par l'API manque de précision et lisibilité. 

#### Classe Paramètres
Cette classe est utilisée pour calculer les paramètres aérodynamiques de l'avion. Ses attributes sont les suivants : l'envergure, la surface, la masse, l'angle de flèche, le coefficient de trainée parasite à portance nulle et la vitesse maximale de l'avion.

##### portance_L(self)
Retourne la portance à partir de la masse de l'avion. 

##### trainee(self, ground_speed, densite)
Permet de calculer la trainée totale de l'avion en utilisant d'autres paramètres tel que l'allongement, le coefficient de trainée calculées au préalable. 

##### finesse(self, ground_speed, densite)
Quotient de la portance et de la trainée, représentant l'efficacité de l'aile ou de l'avion. Plus elle est élevée, plus l'avion ira loin en consommant peu de carburant.
### Module affichage
Regroupe les deux scripts liés à un affichage.  
"gestion.cartopy.py" ouvre une carte sur votre navigateur par défaut en local et y affiche tous les vols récupérés par l'API de FlightRadar24, ainsi que leur numéro de vol, leur position, leur altitude et leur vitesse.  
"gestion_courbes.py" est appelée dans "entrees_utilisateur.py" et affiche des courbes selon deux paramètres :
- soit l'altitude;
- soit la vitesse.
#### gestion_cartopy.py
##### affichage_carte(avion : Avion)
Affiche une carte interactive montrant les positions et informations de vol des avions.  
Cette fonction utilise GeoPandas pour charger les données de carte, Plotly pour créer une figure interactive et ajouter les positions des avions avec leurs informations de vol (altitude, vitesse, numéro de vol et position).
#### gestion_courbes.py
Sort plusieurs courbes selon le choix de l'utilisateur de modifier l'altitude ou la vitesse. Les courbes sorties afficheront alors les modifications relatives au paramètre changé.
##### courbe_atmo_temperature(atmosphere, ex_altitude, ex_temperature, ex_densite, ex_finesse, avion)
Affiche trois courbes :
- Température selon altitude;
- Densité selon altitude;
- Finesse selon altitude.
  
Avec pour chaque courbe deux points représentant les données relatives du vol sélectionné avant et après modification de son altitude.
##### courbe_coefs_finesse_pour_vitesse(atmosphere, ex_altitude, ex_vitesse, ex_coef_portance, ex_coef_trainee, ex_trainee, ex_finesse, avion)
Affiche quatre courbes :
- Coefficient de portance selon vitesse;
- Coefficient de traînée selon vitesse;
- Traînée selon vitesse;
- Finesse selon vitesse.  
  
Avec pour chaque courbe deux points représentant les données relatives du vol sélectionné avant et après modification de sa vitesse.
### Autres scripts
#### controle_vol.py
##### get_dict_parametre()
Initialise l'attribut-objet Parametres de chaque objet Avion selon son modèle.
#### entrees_utilisateur.py
Choix entre le mode guest ou tour de contrôle. L'un permet de visualiser les vols sur une carte, l'autre de modifier l'altitude ou la vitesse d'un vol.
##### guest(avions : list[avion])
Appelle gestion_cartopy.affichage_carte et ouvre une carte en local sur votre navigateur. 
##### tour_de_controle(avions: list[avion], atmospheres: list[atmosphere], numero_vol, liste_idd_avion)
Donne le choix de modifier l'altitude ou la vitesse.  
Lorsque le paramètre choisi est modifié, la nouvelle valeur remplace l'initiale à l'aide d'un setter (set_altitude) et les attributs de l'objet Avion et Atmosphere sont alors modifiés.  
Pour l'altitude, la méthode courbe_atmo_temperature (de gestion_courbes.py) est appelée.  
Pour la vitesse, la méthode courbe_coefs_finesse_pour_vitesse est appelée.
#### main.py
Récupère les données de vols (selon les modèles d'avion spécifiés) depuis l'API FlightRadar24API.  
Initialise les objets Avion et Atmosphere.  
Affiche la liste des avions.  
Interragi avec l'utilisateur pour choisir le mode Utilisateur ou Admin.
## Références
- API de FlightRadar : https://pypi.org/project/FlightRadarAPI/  
- Github de l'API : https://github.com/JeanExtreme002/FlightRadarAPI
- FlightRadar24 : https://www.flightradar24.com/
- Geopandas : https://geopandas.org/en/stable/
- Fichier carte du monde : https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/
- Pypi
- Chatgpt : le script gestion_cartopy.py a principalement été obtenu par cet outil.
- Modèles atmosphériques : Cours MEC671 - ÉTS

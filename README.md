# projetSpecialRadarDeVol
## Objectifs
Le projet Spécial FlightRadar permet de simuler l'impact d'un changement dans un paramètre physique d'un vol (pour l'instant uniquement altitude et vitesse) sur ses performances aéronautiques. Utiliser le mode Admin au lancement pour ce faire.  
Plus spécifiquement, le projet est orienté en 3 axes : 
- Récupération des données des vols via un API;
- Transformation de ces données via des entrées utilisateur;
- Validation des résultats via des courbes basées sur des modèles existants.

Il permet aussi de visualiser les vols sur une carte via le mode Utilisateur au lancement. 
## Contenu du repository

### Module classes
### Module affichage
#### gestion_cartopy.py

#### gestion_courbes.py
### Autres scripts
#### controle_vol.py
#### entrees_utilisateur.py
#### main.py
## Stratégie
## Références
- API de FlightRadar : https://pypi.org/project/FlightRadarAPI/  
- Github de l'API : https://github.com/JeanExtreme002/FlightRadarAPI
- FlightRadar24 : https://www.flightradar24.com/
- Geopandas : https://geopandas.org/en/stable/
- Fichier carte du monde : https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/
- Pypi
- Chatgpt : le script gestion_cartopy.py a principalement été obtenu par cet outil.
- Modèles atmosphériques : Cours MEC671 - ÉTS

import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go


def affichage_carte(avions):
    """
    Affiche une carte interactive montrant les positions et informations de vol des avions.

    Cette fonction utilise GeoPandas pour charger les données de carte, Plotly pour créer une figure interactive
    et ajouter les positions des avions avec leurs informations de vol (altitude et vitesse).

    :param avions: Liste des objets avion contenant les informations de vol (numéro de vol, longitude, latitude
    , altitude, vitesse au sol).
    :return: None
    """
    # Charger les données de carte
    shapefile_path = '110m_cultural/ne_110m_admin_0_countries.shp'

    world = gpd.read_file(shapefile_path)

    # Convertir les données Geopandas en GeoJSON
    world_geojson = world.__geo_interface__

    # Créer une figure interactive avec Plotly
    fig = px.choropleth_mapbox(world, geojson=world_geojson, locations=world.index, color=world.index,
                               mapbox_style="carto-positron", zoom=1, center={"lat": 0, "lon": 0},
                               opacity=0.5, labels={'index': 'country'})

    # Dictionnaire des caractéristiques de chaque avion pour la carte
    cities = [
        {"name": avion.get_numero_vol(), "lon": avion.get_lon(), "lat": avion.get_lat(), "altitude": avion.altitude,
         "ground_speed": avion.ground_speed} for avion in avions
    ]

    # Ajouter la position
    fig.add_trace(go.Scattermapbox(
        mode="markers+text",
        lon=[city["lon"] for city in cities],
        lat=[city["lat"] for city in cities],
        text=[city["name"] + ", Altitude: " + str(city["altitude"]) + "m, Speed: " + str(city["ground_speed"]) + "m/s"
              for city in cities],
        textposition="top right",
        marker={'size': 10, 'color': "red"},
        line=dict(width=2, color='red')
    ))

    fig.update_layout(mapbox_style="carto-positron",
                      mapbox_zoom=1,
                      mapbox_center={"lat": 0, "lon": 0})

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()

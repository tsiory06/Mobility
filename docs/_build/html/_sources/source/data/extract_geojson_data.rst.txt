loadRepartitionZonale
=====================

Cette fonction charge les données géographiques des limites communales d'Antananarivo à partir d'un fichier GeoJSON.

Description
-----------
La fonction lit un fichier GeoJSON contenant les limites communales et renvoie un GeoDataFrame (``gpd.GeoDataFrame``) en s'assurant que le système de coordonnées est conforme à ``EPSG:4326`` (latitude/longitude).

Étapes principales :
- Chargement des données GeoJSON.
- Vérification et transformation du système de coordonnées en ``EPSG:4326`` si nécessaire.

Paramètres
----------
Aucun.

Retour
------
**Type** : ``geopandas.GeoDataFrame``  
Un GeoDataFrame contenant les limites communales d'Antananarivo.

Exemple d'utilisation
----------------------
::

    # Charger les données géographiques des limites communales
    gdf_communes = loadRepartitionZonale()

    # Afficher les premières lignes
    print(gdf_communes.head())

Source des données
------------------
Le fichier utilisé est : ``data/limites_communes_ANTANANARIVO.geojson``.

---

transform_coordinate_point_noir
===============================

Cette fonction transforme les coordonnées d'un fichier GeoJSON contenant des points noirs de trafic d'un système de projection ``EPSG:3857`` (Système Mercator) vers ``EPSG:4326`` (latitude/longitude).

Description
-----------
La fonction lit un fichier GeoJSON contenant des points noirs, transforme les coordonnées à l'aide de la bibliothèque PyProj et renvoie un DataFrame contenant les colonnes suivantes :
- ``Name`` : Nom des points noirs.
- ``latitude`` : Latitude des points noirs en degrés.
- ``longitude`` : Longitude des points noirs en degrés.

Étapes principales :
- Chargement du fichier GeoJSON.
- Transformation des coordonnées des points.
- Extraction des colonnes pertinentes dans un DataFrame.

Paramètres
----------
Aucun.

Retour
------
**Type** : ``pandas.DataFrame``  
Un DataFrame contenant les colonnes :
- ``Name`` : Nom des points noirs.
- ``latitude`` : Latitude des points transformés.
- ``longitude`` : Longitude des points transformés.

Exemple d'utilisation
----------------------
::

    # Charger et transformer les points noirs
    df_points_noirs = transform_coordinate_point_noir()

    # Afficher les points transformés
    print(df_points_noirs.head())

Source des données
------------------
Le fichier utilisé est : ``data/Point.geojson``.

Notes
-----
- Cette fonction utilise PyProj pour la transformation des coordonnées.
- Assurez-vous que le fichier GeoJSON utilise le système de coordonnées ``EPSG:3857`` avant transformation.

============================================
Documentation Technique : Données Géospatiales et Démographiques
============================================

Ce module contient des fonctions pour manipuler et analyser les données géospatiales et démographiques liées aux communes et aux routes. Il intègre des requêtes SQLAlchemy, des manipulations de GeoDataFrames et des calculs statistiques.

Contenu du module
------------------
- `get_merged_geo_population_data`
- `get_volume_deplacement_route`

---

**get_merged_geo_population_data**
----------------------------------

**Description :**
Cette fonction fusionne les données démographiques issues de la base de données avec les données géospatiales provenant d'un fichier GeoJSON. Elle calcule également la moyenne de la population pour remplir les valeurs manquantes.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Un GeoDataFrame fusionné contenant les colonnes suivantes :
  - `ADM3_EN` : Nom des communes (GeoJSON).
  - `total_population` : Population totale par commune (données enrichies depuis la base de données).

**Étapes de traitement :**
1. Chargement des données GeoJSON via la fonction `loadGeojson`.
2. Requête SQLAlchemy pour récupérer les données de population par commune depuis la vue `vue_population_par_commune`.
3. Conversion des noms de colonnes en chaînes de caractères en minuscules pour harmoniser la correspondance.
4. Fusion des données GeoJSON avec les données de population.
5. Conversion des valeurs `Decimal` en `float` pour éviter les erreurs de sérialisation JSON.
6. Remplissage des valeurs manquantes de population avec la moyenne calculée.

**Exemple d'utilisation :**
.. code-block:: python

   gdf_merged = get_merged_geo_population_data()

---

**get_volume_deplacement_route**
--------------------------------

**Description :**
Cette fonction récupère le volume de déplacement par route depuis une vue en base de données et l'associe aux données géospatiales des routes issues d'un fichier GeoJSON.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Un DataFrame contenant les colonnes suivantes :
  - `id_osm` : Identifiant OSM des routes.
  - `centroid` : Centroid des segments routiers.
  - Données enrichies provenant de la vue `vue_volume_deplacement_par_route`.

**Étapes de traitement :**
1. Chargement de la vue `vue_volume_deplacement_par_route` depuis la base de données.
2. Conversion de l'identifiant `id_osm` en entier pour assurer la correspondance.
3. Chargement du GeoJSON des routes et conversion des coordonnées au système EPSG:3857.
4. Calcul des centroides pour chaque segment routier, reconvertis en EPSG:4326.
5. Fusion des données géospatiales des routes avec les volumes de déplacement.

**Exemple d'utilisation :**
.. code-block:: python

   df_volume_route = get_volume_deplacement_route()

---

**Remarques**
-------------
- La fonction `get_merged_geo_population_data` utilise la vue `vue_population_par_commune` pour récupérer les données démographiques.
- La fonction `get_volume_deplacement_route` nécessite un fichier GeoJSON nommé `Antananarivo_voiries_primaires-secondaires-tertiaire.geojson`.

Pour toute modification ou ajout, veuillez respecter les conventions et tester les fonctions avec des données pertinentes.

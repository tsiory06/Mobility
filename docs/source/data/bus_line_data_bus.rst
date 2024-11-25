===================================================
Documentation Technique : Analyse des Lignes de Bus
===================================================

Ce module contient des fonctions pour manipuler, enrichir et analyser des données relatives aux lignes de transport en commun. Il intègre des calculs analytiques, des transformations géospatiales et des opérations sur les bases de données.

Contenu du module
------------------
- `get_bus_lines_dropdown_options`
- `get_all_ligne_from_geojson`
- `get_all_ligne_from_database`
- `get_geo_data_all_ligne`
- `convert_utm_to_latlon`
- `extract_lat_lon`
- `enrich_lignes_data`

---

**get_bus_lines_dropdown_options**
----------------------------------

**Description :**
Récupère les options pour un menu déroulant représentant les lignes de transport en commun.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Une liste de dictionnaires contenant :
  - `label` : numéro de ligne.
  - `value` : numéro de ligne.

**Exemple d'utilisation :**
.. code-block:: python

   options = get_bus_lines_dropdown_options()

---

**get_all_ligne_from_geojson**
------------------------------

**Description :**
Charge les données des lignes de transport en commun à partir des fichiers GeoJSON situés dans un répertoire spécifique.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Un GeoDataFrame combiné contenant les colonnes essentielles.

**Exemple d'utilisation :**
.. code-block:: python

   geojson_df = get_all_ligne_from_geojson()

---

**get_all_ligne_from_database**
-------------------------------

**Description :**
Récupère les données des lignes de transport en commun depuis la base de données.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Un DataFrame contenant les données des lignes de transport.

**Exemple d'utilisation :**
.. code-block:: python

   db_df = get_all_ligne_from_database()

---

**get_geo_data_all_ligne**
--------------------------

**Description :**
Fusionne les données des lignes de transport provenant des fichiers GeoJSON et de la base de données.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Un DataFrame combiné des données GeoJSON et des données de la base de données.

**Exemple d'utilisation :**
.. code-block:: python

   combined_df = get_geo_data_all_ligne()

---

**convert_utm_to_latlon**
-------------------------

**Description :**
Convertit les coordonnées UTM d'un GeoDataFrame en latitude et longitude (WGS84).

**Paramètres d'entrée :**
- `gdf` : GeoDataFrame contenant des données en UTM.
- `utm_crs` : Code EPSG du système de coordonnées UTM source.

**Valeurs retournées :**
- Un GeoDataFrame avec les coordonnées converties.

**Exemple d'utilisation :**
.. code-block:: python

   converted_gdf = convert_utm_to_latlon(gdf, 3857)

---

**extract_lat_lon**
-------------------

**Description :**
Extrait les coordonnées de latitude et de longitude des objets géométriques de type `LineString`.

**Paramètres d'entrée :**
- `geom` : Objet géométrique.

**Valeurs retournées :**
- Deux listes contenant les latitudes et longitudes.

**Exemple d'utilisation :**
.. code-block:: python

   lats, lons = extract_lat_lon(geometry)

---

**enrich_lignes_data**
----------------------

**Description :**
Enrichit les données des lignes de transport en commun avec des indicateurs calculés tels que les coûts, les revenus, et les ratios d'utilisation.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Un DataFrame contenant les données enrichies avec des indicateurs tels que :
  - `cout_carburant_par_jour`
  - `revenu_par_jour`
  - `ratio_remplissage`, etc.

**Exemple d'utilisation :**
.. code-block:: python

   enriched_data = enrich_lignes_data()

---

**Calculs Implémentés dans enrich_lignes_data**
-----------------------------------------------

1. **Coût de carburant par jour :**
   .. code-block:: python

      cout_carburant_par_jour = (
          (consomation_jour / 100) * distance_aller_retour * prix_carburant_par_litre * nombre_rotation
      )

2. **Revenu total par jour :**
   .. code-block:: python

      revenu_par_jour = frais_par_passager * nombre_passager_jour / nombre_bus_jour

3. **Rentabilité par jour :**
   .. code-block:: python

      rentabilite_par_jour = revenu_par_jour - cout_exploitation_total

4. **Ratio de remplissage :**
   .. code-block:: python

      ratio_remplissage = (
          nombre_passager_jour / (nombre_vehicule * capacite_bus * nombre_rotation) * 100
      )

5. **Bus par kilomètre :**
   .. code-block:: python

      bus_par_km = nombre_vehicule / distance_primus_terminus

6. **Distance moyenne par arrêt :**
   .. code-block:: python

      distance_par_arret = distance_primus_terminus / nombre_arret

7. **Durée moyenne d'une rotation :**
   .. code-block:: python

      duree_rotation = (heure_exploitation * 60) / nombre_rotation

---

**Remarques**
Pour toute modification ou ajout, veuillez suivre le format standard de la documentation et tester les fonctions avec des données pertinentes.

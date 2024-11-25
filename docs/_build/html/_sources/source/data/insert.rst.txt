Fonctions d'Insertion dans la Base de Données
=============================================

Ce module propose diverses fonctions pour insérer des données dans une base relationnelle à l'aide de SQLAlchemy. Il gère les données provenant de fichiers GeoJSON, Excel, et génère également des données de test aléatoires.

Fonctions
---------

insert_communes(geojson_path)
-----------------------------
Insère les communes dans la table `commune` à partir d'un fichier GeoJSON.

**Paramètres :**
- `geojson_path` (str) : Chemin vers le fichier GeoJSON contenant les données des communes.

**Comportement :**
- Lit le fichier GeoJSON.
- Extrait `ADM3_EN` (nom) et `ADM3_PCODE` (identifiant).
- Insère ces valeurs dans la table `commune`.

**Exemple :**
.. code-block:: python

    insert_communes("chemin/vers/communes.geojson")


insert_fokotany(file_path)
--------------------------
Insère les fokontany dans la table `fokotany` à partir d'un fichier Excel.

**Paramètres :**
- `file_path` (str) : Chemin vers le fichier Excel contenant les données des fokontany.

**Comportement :**
- Associe les fokontany à leurs communes correspondantes.
- Insère les colonnes `id_commune` et `nom_fokotany` dans la table `fokotany`.

**Exemple :**
.. code-block:: python

    insert_fokotany("chemin/vers/fokotany.xlsx")


insert_population_from_excel(file_path)
---------------------------------------
Insère les données de population dans la table `population` à partir d'un fichier Excel.

**Paramètres :**
- `file_path` (str) : Chemin vers le fichier Excel contenant les données de population.

**Comportement :**
- Associe les fokontany à leurs tranches d'âge.
- Insère les comptes de population dans la table `population`.

**Exemple :**
.. code-block:: python

    insert_population_from_excel("chemin/vers/population.xlsx")


insert_vehicules()
------------------
Insère les types de véhicules prédéfinis dans la table `types_vehicules`.

**Comportement :**
- Ajoute les types de véhicules : "Voiture", "Moto", et "Bus".

**Exemple :**
.. code-block:: python

    insert_vehicules()


insert_hierarchie_fonctionnelle()
---------------------------------
Insère les niveaux de hiérarchie routière dans la table `hierarchie_fonctionnelle`.

**Comportement :**
- Ajoute les niveaux : "primary", "secondary", et "tertiary".

**Exemple :**
.. code-block:: python

    insert_hierarchie_fonctionnelle()


insert_routes_from_geojson_with_hierarchy(geojson_path)
-------------------------------------------------------
Insère les routes dans la table `route` avec les informations de hiérarchie.

**Paramètres :**
- `geojson_path` (str) : Chemin vers le fichier GeoJSON contenant les données des routes.

**Comportement :**
- Associe les niveaux de hiérarchie aux routes.
- Insère `osm_id` et `id_hierarchie` dans la table `route`.

**Exemple :**
.. code-block:: python

    insert_routes_from_geojson_with_hierarchy("chemin/vers/routes.geojson")


insert_flux_trafic()
--------------------
Insère des données aléatoires sur les flux de trafic dans la table `flux_trafic`.

**Comportement :**
- Génère 20 entrées aléatoires sur les flux de trafic.
- Insère des données telles que volume, vitesse moyenne et temps de trajet.

**Exemple :**
.. code-block:: python

    insert_flux_trafic()


insert_cooperatives(data)
-------------------------
Insère les coopératives dans la table `cooperatives`.

**Paramètres :**
- `data` (DataFrame) : DataFrame contenant les noms des coopératives.

**Comportement :**
- Ajoute les coopératives uniques à la base de données.
- Retourne un dictionnaire associant les noms des coopératives à leurs ID.

**Exemple :**
.. code-block:: python

    cooperative_map = insert_cooperatives(cooperative_data)


insert_lignes(data)
-------------------
Insère les lignes de transport en commun dans la table `lignes`.

**Paramètres :**
- `data` (DataFrame) : DataFrame contenant les données des lignes et des coopératives.

**Comportement :**
- Associe chaque ligne à sa coopérative.
- Insère les lignes si elles n'existent pas encore.

**Exemple :**
.. code-block:: python

    insert_lignes(ligne_data)


insert_antennes(data)
---------------------
Insère les détails des lignes de transport en commun dans la table `antenne`.

**Paramètres :**
- `data` (DataFrame) : DataFrame contenant les détails des lignes.

**Comportement :**
- Remplace les valeurs manquantes par la médiane des colonnes correspondantes.
- Insère des données telles que les arrêts, rotations, et nombres de passagers.

**Exemple :**
.. code-block:: python

    insert_antennes(antenne_data)


Gestion des erreurs
-------------------

- Les erreurs SQL sont gérées avec un rollback via `session.rollback()`.
- Les exceptions sont relancées après rollback pour faciliter le débogage.

Dépendances
-----------

- **Bibliothèques Python :**
  - `pandas`
  - `numpy`
  - `sqlalchemy`
  - `pyproj`
  - `geopandas`

- **Tables de la base de données :**
  - `commune`
  - `fokotany`
  - `population`
  - `types_vehicules`
  - `hierarchie_fonctionnelle`
  - `route`
  - `flux_trafic`
  - `cooperatives`
  - `lignes`
  - `antenne`

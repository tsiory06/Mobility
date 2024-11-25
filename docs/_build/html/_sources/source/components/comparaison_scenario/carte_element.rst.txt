Carte Element Module
====================

Ce module contient les fonctions nécessaires à la création de différents types de cartes interactives utilisant Plotly et GeoPandas. Ces cartes incluent des visualisations de densité de population, de trafic routier, et d'autres aspects géographiques.

---

Fonctions principales
---------------------

### **`create_density_carte`**
Crée une carte choroplèthe représentant la densité de population.

.. code-block:: python

    def create_density_carte(geo_population_data):
        """
        Génère une carte choroplèthe basée sur la densité de population.

        Args:
            geo_population_data (GeoDataFrame): Données géographiques et démographiques.

        Returns:
            go.Choroplethmapbox: Carte choroplèthe interactive.
        """

### **`create_default_carte`**
Crée une carte par défaut sans données spécifiques, avec un thème grisé.

.. code-block:: python

    def create_default_carte(geo_population_data):
        """
        Génère une carte de base avec un style grisé.

        Args:
            geo_population_data (GeoDataFrame): Données géographiques.

        Returns:
            go.Choroplethmapbox: Carte interactive par défaut.
        """

### **`create_route`**
Crée une carte montrant des routes avec des lignes.

.. code-block:: python

    def create_route(lats, lons):
        """
        Génère une carte de routes à partir de listes de latitudes et longitudes.

        Args:
            lats (list): Liste des latitudes.
            lons (list): Liste des longitudes.

        Returns:
            go.Scattermapbox: Trace de routes.
        """

### **`create_traffic_markers`**
Crée des marqueurs sur la carte pour visualiser le trafic.

.. code-block:: python

    def create_traffic_markers(geo_traffic_data):
        """
        Génère des marqueurs indiquant le trafic sur une carte.

        Args:
            geo_traffic_data (DataFrame): Données sur le trafic.

        Returns:
            go.Scattermapbox: Marqueurs de trafic.
        """

### **`load_and_prepare_traffic_data`**
Charge et prépare les données de trafic à partir d'un fichier GeoJSON et d'une fonction de traitement des données.

.. code-block:: python

    def load_and_prepare_traffic_data(geojson_path, traffic_data_function):
        """
        Charge et fusionne les données de trafic avec les données géographiques.

        Args:
            geojson_path (str): Chemin du fichier GeoJSON.
            traffic_data_function (callable): Fonction pour récupérer les données de trafic.

        Returns:
            GeoDataFrame: Données fusionnées avec les volumes de trafic.
        """

### **`create_route_with_traffic`**
Ajoute des informations sur le trafic aux routes.

.. code-block:: python

    def create_route_with_traffic(geo_traffic_data):
        """
        Génère des routes sur une carte avec des volumes de trafic.

        Args:
            geo_traffic_data (GeoDataFrame): Données de trafic par route.

        Returns:
            list: Traces Plotly des routes.
        """

### **`create_route_with_traffic_colored`**
Ajoute des couleurs aux routes en fonction du volume de trafic.

.. code-block:: python

    def create_route_with_traffic_colored(geo_traffic_data):
        """
        Génère des routes avec un code couleur en fonction du volume de trafic.

        Args:
            geo_traffic_data (GeoDataFrame): Données de trafic par route.

        Returns:
            list: Traces Plotly des routes colorées.
        """

### **`create_traffic_markers_from_df`**
Crée des marqueurs pour des points de trafic spécifiques.

.. code-block:: python

    def create_traffic_markers_from_df():
        """
        Génère des marqueurs pour les points noirs de trafic.

        Returns:
            go.Scattermapbox: Marqueurs de trafic.
        """

---

Structure des données
---------------------

### Données géographiques
Les fonctions de ce module utilisent des `GeoDataFrame` contenant des informations géographiques et attributaires.

### Données de trafic
Les volumes de trafic sont représentés par un DataFrame qui contient des colonnes telles que :
- `id_osm`: Identifiant unique des routes.
- `total_traffic_volume`: Volume total de trafic.

---

Utilisation
-----------

Les fonctions du module `carte_element.py` peuvent être utilisées pour :
- Visualiser les densités de population.
- Afficher les volumes de trafic.
- Générer des routes colorées en fonction de métriques.

Ces cartes sont conçues pour être intégrées dans des tableaux de bord interactifs utilisant Dash.

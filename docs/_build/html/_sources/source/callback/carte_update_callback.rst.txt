Carte Update Callback Module
============================

Ce module gère la mise à jour dynamique de la carte interactive en fonction des thématiques sélectionnées par l'utilisateur dans l'application Dash.

Fonctions principales :
- `carte_update_callback`: Initialise un callback pour actualiser la carte en fonction des données et des thématiques sélectionnées.

---

Fonctions
---------

carte_update_callback
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def carte_update_callback(app, gdf_merged, gdf_geojson, lats, lons, congestion, df_filtered):
        """
        Initialise un callback pour mettre à jour la carte interactive.

        Args:
            app (dash.Dash): L'application Dash principale.
            gdf_merged (GeoDataFrame): Données géographiques fusionnées pour la densité.
            gdf_geojson (GeoDataFrame): Données GeoJSON pour la carte par défaut.
            lats (list): Liste des latitudes des routes.
            lons (list): Liste des longitudes des routes.
            congestion (DataFrame): Données de congestion.
            df_filtered (DataFrame): Données filtrées pour les itinéraires et la congestion.

        Returns:
            None
        """

    Description :
    - Cette fonction actualise la figure de la carte basée sur les thématiques sélectionnées par l'utilisateur.
    - La carte peut afficher des densités, des segments de trafic, des itinéraires colorés en fonction de la congestion, ou des points de trafic.

    Arguments du Callback :
    - **Input**: `selected-thematiques.data` - Thématiques sélectionnées par l'utilisateur (ex. : densité, segment, itinéraire, congestion, point).
    - **Output**: `map.figure` - Carte mise à jour sous forme de figure Plotly.

    Thématiques prises en charge :
    - **Densité (`densite`)** : Affiche les zones de densité en utilisant `gdf_merged`.
    - **Segment (`segment`)** : Affiche les marqueurs de trafic basés sur les données de congestion.
    - **Itinéraire (`itineraire`)** : Trace des itinéraires colorés en fonction du trafic à partir de `df_filtered`.
    - **Congestion (`congestion`)** : Trace des itinéraires congestionnés.
    - **Point (`point`)** : Affiche des points de trafic spécifiques.

    Exemple :
    ---------
    - Si l'utilisateur sélectionne "densité" et "itinéraire", la carte affichera des zones de densité et les itinéraires correspondants.
    - En l'absence de sélection, une carte par défaut est affichée à l'aide de `gdf_geojson`.

---

Utilisation
-----------
Cette fonction est utilisée pour créer des cartes interactives et informatives, adaptées aux besoins de l'utilisateur en matière de visualisation de la mobilité et du trafic.

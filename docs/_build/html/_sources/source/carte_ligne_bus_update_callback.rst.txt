Carte Ligne Bus Update Callback Module
======================================

Ce module gère les interactions pour la visualisation des lignes de bus sur une carte dans l'application Dash.

---

Fonctions
---------

carte_ligne_bus_update_callback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def carte_ligne_bus_update_callback(app, prepared_dataframe, gdf_geojson, stops):
        """
        Initialise les callbacks nécessaires pour gérer les interactions et mises à jour
        des données et de la carte dans l'application.

        Args:
            app (dash.Dash): L'application Dash principale.
            prepared_dataframe (pandas.DataFrame): Les données préparées des lignes de bus.
            gdf_geojson (GeoDataFrame): Les données géographiques pour la carte.
            stops (str): Fichier contenant les arrêts de bus.

        Returns:
            None
        """

---

Détails des Callbacks
---------------------

1. **update_store**
   - Stocke les options sélectionnées par l'utilisateur.

   .. code-block:: python

        @app.callback(
            Output('selected-affichage', 'data'),
            Input('transport_en_commun-visual-options', 'value')
        )
        def update_store(selected_options):
            return selected_options

---

2. **update_figure**
   - Met à jour la figure de la carte en fonction des options sélectionnées.

   .. code-block:: python

        @app.callback(
            Output('transport_en_commun-map', 'figure'),
            [Input('selected-affichage', 'data'),
             Input('ligne-visual-options', 'value'),
             Input('transport_en_commun-line-analyse_par_commune', 'value')]
        )
        def update_figure(selected_affichage, indicateurs, selected_lines):
            """
            Met à jour la carte en fonction des options sélectionnées et des lignes de bus.
            """
            ...

---

3. **store_selected_bus_lines**
   - Stocke les lignes de bus sélectionnées.

   .. code-block:: python

        @app.callback(
            Output('selected-transport_en_commun-lines-store', 'data'),
            Input('transport_en_commun-line-analyse_par_commune', 'value')
        )
        def store_selected_bus_lines(selected_lines):
            return selected_lines if selected_lines else []

---

4. **update_bus_lines**
   - Met à jour les options du Dropdown pour les lignes de bus.

   .. code-block:: python

        @app.callback(
            Output('transport_en_commun-line-analyse_par_commune', 'options'),
            Input('transport_en_commun-line-analyse_par_commune', 'id')
        )
        def update_bus_lines(_):
            return get_bus_lines_dropdown_options()

---

5. **update_legend**
   - Met à jour le style et les valeurs de la légende de la carte.

   .. code-block:: python

        @app.callback(
            [Output('couleur-legend', 'style'),
             Output('left-speed', 'children'),
             Output('right-speed', 'children')],
            [Input('ligne-visual-options', 'value'),
             Input('couleur-legend', 'n_clicks')]
        )
        def update_legend(selected_option, n_clicks):
            """
            Met à jour la légende en fonction de l'option sélectionnée.
            """
            ...

---

Utilisation
-----------

Ce module permet aux utilisateurs de :

- Sélectionner et visualiser des thématiques spécifiques liées aux lignes de bus.
- Interagir avec une carte dynamique pour explorer les données.
- Gérer les légendes et les annotations associées aux données sélectionnées.

---

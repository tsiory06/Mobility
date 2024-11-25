Indicateurs Bus Callback Module
===============================

Ce module gère les callbacks liés à l'affichage, la mise à jour et le téléchargement des données sur les lignes de bus dans l'application Dash.

---

Fonctions
---------

indicateurs_bus_callback
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def indicateurs_bus_callback(app):
        """
        Initialise les callbacks nécessaires pour gérer les interactions avec les indicateurs des lignes de bus.

        Args:
            app (dash.Dash): L'application Dash principale.

        Returns:
            None
        """

---

Détails des Callbacks
---------------------

1. **update_graph**
   - Met à jour le graphique principal basé sur l'indicateur sélectionné.

   .. code-block:: python

        @app.callback(
            [Output('graphique', 'figure'),
             Output('kpi-moyenne', 'children'),
             Output('kpi-mediane', 'children'),
             Output('kpi-min', 'children'),
             Output('kpi-max', 'children')],
            [Input('indicateur-dropdown', 'value')]
        )
        def update_graph(indicateur):
            """
            Met à jour le graphique en barres et les KPI associés pour l'indicateur sélectionné.
            """
            ...

---

2. **update_bus_details**
   - Met à jour les détails des lignes de bus sélectionnées dans un tableau.

   .. code-block:: python

        @app.callback(
            Output('transport_en_commun-details-container', 'children'),
            Input('transport_en_commun-line-analyse_par_commune', 'value')
        )
        def update_bus_details(selected_lines):
            """
            Met à jour les détails des lignes sélectionnées dans un tableau interactif.
            """
            ...

---

3. **update_tables**
   - Met à jour les tableaux des performances financières, des ressources et des passagers.

   .. code-block:: python

        @app.callback(
            [Output("finance-table-body", "children"),
             Output("resources-table-body", "children"),
             Output("passenger-table-body", "children")],
            [Input("finance-page", "data"),
             Input("resources-page", "data"),
             Input("passenger-page", "data")]
        )
        def update_tables(finance_page, resources_page, passenger_page):
            """
            Met à jour le contenu des tableaux en fonction de la pagination.
            """
            ...

---

4. **download_finance_excel**
   - Permet le téléchargement des données financières sous forme de fichier Excel.

   .. code-block:: python

        @app.callback(
            Output("download-Performance Financière et Rentabilité-excel", "data"),
            Input("download-Performance Financière et Rentabilité-btn", "n_clicks"),
            prevent_initial_call=True
        )
        def download_finance_excel(n_clicks):
            """
            Génère un fichier Excel pour les performances financières.
            """
            ...

---

Utilisation
-----------

- Sélectionnez un indicateur dans le Dropdown pour mettre à jour les graphiques et les KPI.
- Naviguez à travers les tableaux des lignes de bus pour analyser les données financières, les ressources, et les volumes de passagers.
- Téléchargez les données au format Excel en cliquant sur les boutons dédiés.

---

Libellés des Colonnes
---------------------

Les colonnes des tableaux utilisent les libellés 

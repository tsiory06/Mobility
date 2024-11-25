Scenario Figure Module
======================

Ce module contient les fonctions nécessaires pour gérer les comparaisons de scénarios, générer des indicateurs clés de performance (KPI), et produire des tableaux et graphiques pour l'analyse des scénarios.

---

Fonctions principales
---------------------

1. **`get_scenario_options`**
   Récupère les options de scénarios disponibles dans la base de données pour les affichages de sélection.

   .. code-block:: python

       def get_scenario_options():
           """
           Retourne une liste de dictionnaires contenant les options des scénarios
           disponibles pour un composant Dropdown Dash.

           Returns:
               list[dict]: Liste des options avec 'label' et 'value'.
           """

2. **`generate_kpi_card`**
   Crée une carte KPI (indicateur clé de performance) avec une valeur, un label et une couleur.

   .. code-block:: python

       def generate_kpi_card(value, label, color):
           """
           Génère une carte KPI affichant une valeur et une description.

           Args:
               value (str): La valeur de l'indicateur.
               label (str): Le libellé descriptif de l'indicateur.
               color (str): La couleur de fond de la carte.

           Returns:
               dbc.Card: Carte Dash Bootstrap contenant l'indicateur.
           """

3. **`generate_scenario_kpi`**
   Génère les KPI pour un scénario donné sous forme de rangée Dash Bootstrap.

   .. code-block:: python

       def generate_scenario_kpi(scenario_data):
           """
           Génère une rangée de cartes KPI pour un scénario.

           Args:
               scenario_data (dict): Données du scénario.

           Returns:
               dbc.Row: Ligne de cartes KPI.
           """

4. **`generate_comparison_list`**
   Produit une liste de comparaisons détaillées entre plusieurs scénarios sélectionnés.

   .. code-block:: python

       def generate_comparison_list(selected_scenarios):
           """
           Génère une liste de comparaisons entre les scénarios sélectionnés.

           Args:
               selected_scenarios (list): Liste des ID des scénarios sélectionnés.

           Returns:
               list[dict]: Liste des comparaisons par indicateurs.
           """

5. **`generate_impact_card`**
   Produit des cartes contenant les comparaisons des impacts entre différents scénarios.

   .. code-block:: python

       def generate_impact_card(selected_scenarios):
           """
           Génère des cartes affichant les impacts des différences entre scénarios.

           Args:
               selected_scenarios (list): Liste des ID des scénarios sélectionnés.

           Returns:
               html.Div: Division HTML contenant les cartes de comparaison.
           """

6. **`generate_card_header_with_tooltip`**
   Crée un en-tête de tableau avec un titre et un infobulle explicatif.

   .. code-block:: python

       def generate_card_header_with_tooltip(title, table_id):
           """
           Crée un en-tête de tableau avec un infobulle.

           Args:
               title (str): Le titre à afficher.
               table_id (str): L'identifiant du tableau.

           Returns:
               html.Div: En-tête de tableau avec infobulle.
           """

7. **`generate_table`**
   Génère un tableau comparatif des indicateurs pour plusieurs scénarios.

   .. code-block:: python

       def generate_table(row_headers, scenario_ids, table_id):
           """
           Génère un tableau pour comparer les indicateurs des scénarios sélectionnés.

           Args:
               row_headers (list): Liste des noms des indicateurs (lignes).
               scenario_ids (list): Liste des ID des scénarios sélectionnés (colonnes).
               table_id (str): Identifiant HTML du tableau.

           Returns:
               dbc.Table: Tableau HTML Dash Bootstrap.
           """

Comparaison Scénarios Module
============================

Ce module gère l'affichage de la page de comparaison des scénarios dans l'application Dash. Il fournit une interface utilisateur pour comparer plusieurs scénarios en termes d'indicateurs de transport, d'émissions de gaz et d'impacts.

---

Fonction
--------

comparaison
~~~~~~~~~~~

.. code-block:: python

    def comparaison():
        """
        Génère la mise en page pour la comparaison des scénarios.

        Returns:
            dbc.Container: Conteneur Dash Bootstrap Components contenant la mise en page de la page de comparaison.
        """

---

Structure de la Page
--------------------

1. **Sélection des Scénarios**
   - Une carte interactive permet de sélectionner plusieurs scénarios via un Dropdown. Les options sont générées dynamiquement par la fonction `get_scenario_options()`.

   .. code-block:: python

        dbc.Card([
            dbc.CardHeader(
                html.H5("Sélection des Scénarios", className="text-center"),
                style={'backgroundColor': 'rgba(0, 147, 69, 0.43)'}
            ),
            dbc.CardBody([
                dbc.Label("Veuillez sélectionner les scénarios pour la comparaison :"),
                dcc.Dropdown(
                    id='comparaison_scenario-dropdown',
                    options=get_scenario_options(),
                    multi=True,
                    placeholder="Sélectionnez plusieurs scénarios",
                    value=['sc1', 'sc2']
                ),
            ])
        ])

---

2. **Comparaison des Indicateurs**
   - Cette section affiche deux tableaux côte à côte :
     - **Indicateurs de Transport**
     - **Émissions de Gaz**
   - Les données sont mises à jour dynamiquement via des callbacks.

   .. code-block:: python

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        html.H5("Comparaison des Indicateurs de Transport et des Émissions de Gaz", className="text-center"),
                        style={'backgroundColor': 'rgba(0, 147, 69, 0.43)'}
                    ),
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.CardHeader(
                                    html.H6("Indicateurs de Transport", className="text-center"),
                                    style={'backgroundColor': '#f0f0f0', 'font-weight': 'bold'}
                                ),
                                html.Div(id='tableau-transport')
                            ], width=6),
                            dbc.Col([
                                dbc.CardHeader(
                                    html.H6("Émissions de Gaz", className="text-center"),
                                    style={'backgroundColor': '#f0f0f0', 'font-weight': 'bold'}
                                ),
                                html.Div(id='tableau-gaz')
                            ], width=6)
                        ])
                    ])
                ], className="mb-4 shadow-sm")
            ], width=12)
        ])

---

3. **Impact des Différences**
   - Affiche une carte résumant les différences clés entre les scénarios sélectionnés.

   .. code-block:: python

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        html.H5("Impact des Différences entre les Scénarios", className="text-center"),
                        style={'backgroundColor': 'rgba(0, 147, 69, 0.43)'}
                    ),
                    dbc.CardBody(
                        html.Div(id='impact-card')
                    )
                ], className="mb-4 shadow-sm")
            ], width=12)
        ])

---

Utilisation
-----------

1. Sélectionnez plusieurs scénarios via le Dropdown.
2. Consultez les indicateurs de transport et les émissions de gaz dans les tableaux.
3. Observez l'impact des différences entre les scénarios via la carte dédiée.

--- 

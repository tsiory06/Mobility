Simulation Scénarios Module
===========================

Ce module gère l'affichage de la page de création de scénarios dans l'application Dash. Il fournit une interface utilisateur pour saisir et enregistrer les informations relatives à un nouveau scénario.

---

Fonction
--------

simulation
~~~~~~~~~~

.. code-block:: python

    def simulation():
        """
        Génère la mise en page pour la création d'un scénario.

        Returns:
            dbc.Container: Conteneur Dash Bootstrap Components contenant les champs de saisie pour un scénario.
        """

---

Structure de la Page
--------------------

1. **Informations de base du Scénario**
   - Nom du Scénario : Champ de texte pour entrer le nom.
   - Description : Zone de texte pour ajouter une description.
   - Type de Scénario : Champ de texte pour définir le type.

   .. code-block:: python

        dbc.Card([
            dbc.CardHeader(html.H5("Informations de base du Scénario", className="text-primary")),
            dbc.CardBody([
                dbc.Label('Nom du Scénario'),
                dbc.Input(id='nom', type='text', placeholder='Nom du Scénario', className='mb-3'),

                dbc.Label('Description'),
                dbc.Textarea(id='description', placeholder='Description du Scénario', className='mb-3',
                             style={'min-height': '60px'}),

                dbc.Label('Type de Scénario'),
                dbc.Input(id='type-comparaison_scenario', type='text', placeholder='Type de Scénario',
                          className='mb-3'),
            ])
        ])

---

2. **Données SUMO**
   - Débit moyen : Champ numérique pour la saisie du débit moyen (veh/h).
   - Vitesse moyenne : Champ numérique pour la vitesse moyenne (km/h).
   - Temps de trajet moyen : Champ numérique pour le temps moyen (min).
   - Volume de carburant simulé : Champ numérique pour le volume de carburant (L).
   - Longueur de trajet moyenne : Champ numérique pour la longueur moyenne (km).

   .. code-block:: python

        dbc.Card([
            dbc.CardHeader(html.H5("Données SUMO", className="text-success")),
            dbc.CardBody([
                dbc.Label('Débit moyen (veh/h)'),
                dbc.Input(id='debit', type='number', placeholder='Débit moyen', className='mb-3'),

                dbc.Label('Vitesse moyenne (km/h)'),
                dbc.Input(id='vitesse-moyenne', type='number', placeholder='Vitesse moyenne',
                          className='mb-3'),

                dbc.Label('Temps de trajet moyen (min)'),
                dbc.Input(id='temps-trajet', type='number', placeholder='Temps de trajet moyen',
                          className='mb-3'),

                dbc.Label('Volume de carburant simulé (L)'),
                dbc.Input(id='volume-carburant', type='number', placeholder='Volume de carburant simulé', className='mb-3'),

                dbc.Label('Longueur de trajet moyenne (km)'),
                dbc.Input(id='longueur-trajet-moyenne', type='number', placeholder='Longueur de trajet moyenne', className='mb-3'),
            ])
        ])

---

3. **Aspects Environnementaux**
   - Émissions de CO2 : Champ numérique pour saisir les émissions de CO2 (g/km).
   - Émissions de NOx : Champ numérique pour saisir les émissions de NOx (g/km).
   - Monoxyde de carbone (CO) : Champ numérique pour les émissions de CO (g/km).

   .. code-block:: python

        dbc.Card([
            dbc.CardHeader(html.H5("Aspects Environnementaux", className="text-warning")),
            dbc.CardBody([
                dbc.Label('Émissions de CO2 (g/km)'),
                dbc.Input(id='co2', type='number', placeholder='Émissions de CO2', className='mb-3'),

                dbc.Label('Émissions de NOx (g/km)'),
                dbc.Input(id='nox', type='number', placeholder='Émissions de NOx', className='mb-3'),

                dbc.Label('Monoxyde de carbone (CO) (g/km)'),
                dbc.Input(id='co', type='number', placeholder='Monoxyde de carbone', className='mb-3'),
            ])
        ])

---

4. **Actions**
   - Bouton "Enregistrer" : Soumet les données.
   - Message de retour : Affiche un message de succès ou d'erreur après l'enregistrement.

   .. code-block:: python

        dbc.Row([
            dbc.Col(
                dbc.Button("Enregistrer", id="submit-button", color="primary", className="mt-2"),
                width=2
            ),
            dbc.Col(
                html.Div(id="output-message", className="mt-3"),
                width=10
            )
        ], justify="end")

---

Utilisation
-----------

1. Remplissez les champs relatifs aux informations de base, aux données SUMO et aux aspects environnementaux.
2. Cliquez sur "Enregistrer" pour soumettre les données.
3. Consultez le message de retour pour vérifier si l'opération a réussi.

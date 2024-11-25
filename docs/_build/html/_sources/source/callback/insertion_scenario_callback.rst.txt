insertion_scenario_callback module
==================================

Ce module gère les callbacks nécessaires pour la gestion des scénarios dans l'application Dash. Il inclut des fonctionnalités pour mettre à jour les tableaux comparatifs et pour insérer des données de scénario dans la base de données.

Fonctions principales :
- `insertion_scenario_callback`: Initialise les callbacks pour la gestion des scénarios.
- `update_content`: Met à jour les tableaux comparatifs des scénarios sélectionnés.
- `submit_form`: Insère un nouveau scénario dans la base de données via un formulaire.

---

Fonctions
---------

insertion_scenario_callback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def insertion_scenario_callback(app):
        """
        Initialise les callbacks nécessaires pour gérer les scénarios.

        Args:
            app (dash.Dash): L'application Dash principale.

        Returns:
            None
        """

    Cette fonction enregistre les callbacks pour :
    - Mettre à jour les tableaux comparatifs et la carte des impacts en fonction des scénarios sélectionnés.
    - Insérer un nouveau scénario dans la base de données via un formulaire.

---

update_content
~~~~~~~~~~~~~~

.. code-block:: python

    def update_content(selected_scenarios):
        """
        Met à jour les tableaux et la carte des impacts pour les scénarios sélectionnés.

        Args:
            selected_scenarios (list): Liste des identifiants des scénarios sélectionnés.

        Returns:
            tuple: Contient les tableaux comparatifs des indicateurs de transport, des émissions de gaz,
            et la carte des impacts.

        Cette fonction :
        - Charge les scénarios sélectionnés ou les deux plus récents par défaut.
        - Génère des tableaux comparatifs pour les indicateurs de transport et les émissions de gaz.
        - Crée une carte affichant les impacts des scénarios.
        """

---

submit_form
~~~~~~~~~~~

.. code-block:: python

    def submit_form(n_clicks, nom, description, type_scenario, debit, vitesse_moyenne, temps_trajet,
                    volume_carburant, longueur_trajet_moyenne, co2, nox, co):
        """
        Insère un nouveau scénario dans la base de données via un formulaire.

        Args:
            n_clicks (int): Nombre de clics sur le bouton de soumission.
            nom (str): Nom du scénario.
            description (str): Description du scénario.
            type_scenario (str): Type du scénario (simulation, comparaison, etc.).
            debit (float): Débit moyen simulé.
            vitesse_moyenne (float): Vitesse moyenne simulée.
            temps_trajet (float): Temps de trajet moyen simulé.
            volume_carburant (float): Volume de carburant simulé.
            longueur_trajet_moyenne (float): Longueur moyenne des trajets simulés.
            co2 (float): Émissions de CO2 simulées.
            nox (float): Émissions de NOx simulées.
            co (float): Émissions de CO simulées.

        Returns:
            str: Message indiquant le succès ou l'échec de l'opération.

        Cette fonction :
        - Valide les données saisies par l'utilisateur.
        - Insère un nouveau scénario dans la base de données via `insert_scenario_data`.
        """

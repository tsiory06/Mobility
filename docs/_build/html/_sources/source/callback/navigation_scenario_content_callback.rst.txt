navigation_scenario_content_callback module
===========================================

Ce module gère les callbacks nécessaires pour changer dynamiquement le contenu de la page en fonction des clics sur les boutons de navigation (simulation ou comparaison).

Fonctions principales :
- `navigation_scenario_content_callback`: Initialise le callback pour la navigation entre les onglets "Simulation" et "Comparaison".
- `update_content`: Met à jour dynamiquement le contenu affiché selon l'onglet sélectionné.

---

Fonctions
---------

navigation_scenario_content_callback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def navigation_scenario_content_callback(app):
        """
        Initialise le callback nécessaire pour naviguer entre les contenus de simulation et de comparaison.

        Args:
            app (dash.Dash): L'application Dash principale.

        Returns:
            None
        """

    Cette fonction enregistre un callback pour changer le contenu de la section dynamique
    en fonction des clics sur les boutons de navigation.

---

update_content
~~~~~~~~~~~~~~

.. code-block:: python

    def update_content(simulation_clicks, comparaison_clicks):
        """
        Met à jour dynamiquement le contenu en fonction du bouton cliqué.

        Args:
            simulation_clicks (int): Nombre de clics sur le bouton "Simulation".
            comparaison_clicks (int): Nombre de clics sur le bouton "Comparaison".

        Returns:
            dash.html.Div: Le contenu correspondant à l'onglet sélectionné.

        Cette fonction :
        - Vérifie quel bouton a été cliqué en utilisant le contexte du callback.
        - Charge le contenu correspondant (simulation ou comparaison) via les fonctions `simulation()` ou `comparaison()`.
        - Affiche un message si aucun bouton n'a été cliqué.
        """

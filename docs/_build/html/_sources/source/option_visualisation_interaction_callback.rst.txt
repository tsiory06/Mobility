Option Visualisation Interaction Callback Module
================================================

Ce module gère les interactions pour sélectionner les thématiques et les options de visualisation dans l'application Dash.

---

Fonctions
---------

option_visualisation_interaction_callback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def option_visualisation_interaction_callback(app):
        """
        Initialise les callbacks pour gérer les interactions liées aux thématiques sélectionnées.

        Args:
            app (dash.Dash): L'application Dash principale.

        Returns:
            None
        """

    Description :
    - Cette fonction initialise un callback qui met à jour les thématiques sélectionnées par l'utilisateur via deux listes de contrôle (checklists).

---

Détails des Callbacks
---------------------

update_selected
~~~~~~~~~~~~~~~

.. code-block:: python

    def update_selected(selected_values, selected_route):
        """
        Combine les thématiques sélectionnées par l'utilisateur.

        Args:
            selected_values (list): Liste des thématiques sélectionnées dans la première checklist.
            selected_route (list): Liste des options sélectionnées dans la deuxième checklist.

        Returns:
            list: Une liste combinée des thématiques et options sélectionnées.
        """

    Détails :
    - Si aucune valeur n'est sélectionnée, des listes vides sont utilisées par défaut.
    - Les thématiques et les options sont combinées en une liste unique, sans doublons, grâce à `set`.

---

Utilisation
-----------

Ce module permet aux utilisateurs d'interagir avec l'interface de sélection de thématiques et d'options dans l'application Dash. Il synchronise les données sélectionnées et garantit une liste cohérente des options.

---

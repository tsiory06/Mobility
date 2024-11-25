detail_commune_callback module
=============================

Ce module gère les callbacks nécessaires pour afficher les détails d'une commune dans l'application Dash.

Fonctions principales :
- `detail_commune_callback`: Initialise le callback pour la sélection de commune.
- `update_zone_details`: Met à jour les détails d'une commune spécifique.

---

Fonctions
---------

detail_commune_callback
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def detail_commune_callback(app):
        """
        Enregistre les callbacks nécessaires pour afficher les détails d'une commune.

        Args:
            app (dash.Dash): L'application Dash principale.

        Returns:
            None
        """

    Cette fonction initialise le callback pour mettre à jour les détails d'une commune.
    Elle prend en entrée une instance de l'application Dash et associe la fonction `update_zone_details`
    au dropdown des communes.

---

update_zone_details
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def update_zone_details(selected_commune):
        """
        Met à jour les détails pour la commune sélectionnée.

        Args:
            selected_commune (str): Le nom de la commune sélectionnée dans le dropdown.

        Returns:
            list: Une liste d'éléments HTML contenant les informations détaillées sur la commune.

        Cette fonction récupère les informations d'une commune via `get_all_data_commune` et génère
        un contenu détaillé (graphiques, tableaux, etc.) pour l'affichage.
        """

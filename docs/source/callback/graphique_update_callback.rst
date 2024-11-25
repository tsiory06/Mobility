Graphique Update Callback Module
================================

Ce module gère les mises à jour des graphiques dynamiques dans le tableau de bord de l'application Dash en fonction des thématiques sélectionnées et des zones cliquées par l'utilisateur.

---

Fonctions
---------

graphique_update_callback
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def graphique_update_callback(app):
        """
        Initialise les callbacks pour mettre à jour les graphiques dans le tableau de bord.

        Args:
            app (dash.Dash): L'application Dash principale.

        Returns:
            None
        """

    Description :
    - Cette fonction définit plusieurs callbacks pour actualiser différents types de graphiques (densité, typologie, matrice, volumes).
    - Les graphiques sont mis à jour en fonction des thématiques sélectionnées et des zones cliquées.

---

Détails des Callbacks
---------------------

update_density_graph
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def update_density_graph(selected_thematiques):
        """
        Met à jour le graphique de densité basé sur les thématiques sélectionnées.

        Args:
            selected_thematiques (list): Liste des thématiques sélectionnées.

        Returns:
            html.Div: Contient le graphique de densité ou un élément vide si la thématique n'est pas sélectionnée.
        """

    Thématique prise en charge :
    - **Densité (`densite`)** : Affiche un histogramme de la population.

---

update_typology_graph
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def update_typology_graph(selected_thematiques, clicked_zones):
        """
        Met à jour le graphique de typologie basé sur les thématiques et zones sélectionnées.

        Args:
            selected_thematiques (list): Liste des thématiques sélectionnées.
            clicked_zones (list): Liste des zones cliquées.

        Returns:
            html.Div: Contient le graphique de typologie ou un élément vide si la thématique n'est pas sélectionnée.
        """

    Thématique prise en charge :
    - **Typologie (`typologie`)** : Génère un graphique des véhicules par type dans les zones cliquées.

---

update_matrice_graph
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def update_matrice_graph(selected_thematiques, clicked_zones):
        """
        Met à jour la matrice de flux basé sur les thématiques et zones sélectionnées.

        Args:
            selected_thematiques (list): Liste des thématiques sélectionnées.
            clicked_zones (list): Liste des zones cliquées.

        Returns:
            html.Div: Contient un diagramme de Sankey ou un élément vide si la thématique n'est pas sélectionnée.
        """

    Thématique prise en charge :
    - **Matrice (`matrice`)** : Affiche un diagramme de Sankey pour les flux de mobilité.

---

update_finances_graph
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def update_finances_graph(selected_thematiques, clicked_zones):
        """
        Met à jour le graphique de volumes financiers basé sur les thématiques et zones sélectionnées.

        Args:
            selected_thematiques (list): Liste des thématiques sélectionnées.
            clicked_zones (list): Liste des zones cliquées.

        Returns:
            html.Div: Contient le graphique des déplacements ou un élément vide si la thématique n'est pas sélectionnée.
        """

    Thématique prise en charge :
    - **Volumes (`volumes`)** : Génère un graphique des volumes de déplacements pour les zones cliquées.

---

Utilisation
-----------
Ce module est essentiel pour dynamiser le tableau de bord en affichant des graphiques pertinents et interactifs en fonction des actions de l'utilisateur.

Legend Update Callback Module
=============================

Ce module gère les mises à jour dynamiques des légendes affichées dans le tableau de bord en fonction des thématiques sélectionnées par l'utilisateur.

---

Fonctions
---------

legend_update_callback
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def legend_update_callback(app):
        """
        Initialise les callbacks pour mettre à jour les légendes affichées dans le tableau de bord.

        Args:
            app (dash.Dash): L'application Dash principale.

        Returns:
            None
        """

    Description :
    - Cette fonction initialise un callback qui met à jour dynamiquement plusieurs légendes (population, segment, route, densité) en fonction des thématiques sélectionnées.

---

Détails des Callbacks
---------------------

update_legends
~~~~~~~~~~~~~~

.. code-block:: python

    def update_legends(selected_thematiques):
        """
        Met à jour les légendes en fonction des thématiques sélectionnées.

        Args:
            selected_thematiques (list): Liste des thématiques sélectionnées.

        Returns:
            tuple: Quatre éléments `html.Div` représentant les légendes de population, segment, route, et densité.
        """

    Détails :
    - La fonction vérifie les thématiques activées dans `selected_thematiques` et génère des légendes correspondantes à l'aide de la fonction `generate_legend`.

    **Légendes générées** :
    - **Population** :
        - Couleurs : `['#FFEDA0', '#FEB24C', '#FC4E2A', '#E31A1C', '#BD0026']`
        - Valeurs : `['0- 60,000 habitants', '60,001 - 100,000 habitants', '100,001 - 150,000 habitants', '150,001 - 250,000 habitants', '250,001+ habitants']`
    - **Segment** :
        - Couleurs : `['#440154', '#3B528B', '#21918C', '#5EC962', '#FDE725']`
        - Valeurs : `['100-200 volume/heure', '201-300 volume/heure', '301-500 volume/heure', '501-800 volume/heure', '800+ volume/heure']`
    - **Point Noir** (Route) :
        - Couleurs : `['black']`
        - Valeurs : `['Les points noirs dans la ville']`
    - **Densité** :
        - Non défini dans cet exemple, retourne un élément `html.Div` vide par défaut.

---

Utilisation
-----------

Ce module est utile pour adapter les légendes aux données visualisées dans le tableau de bord, offrant ainsi une meilleure lisibilité et compréhension pour les utilisateurs.

---

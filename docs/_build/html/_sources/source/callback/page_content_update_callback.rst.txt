page_content_update_callback module
===================================

Ce module gère le routage dynamique des pages dans l'application Dash. En fonction de l'URL, il charge la page correspondante pour l'utilisateur.

Fonctions principales :
- `page_content_update_callback`: Initialise le callback pour gérer le contenu dynamique de l'application en fonction de l'URL.
- `display_page`: Détermine la page à afficher en fonction du chemin fourni dans l'URL.

---

Fonctions
---------

page_content_update_callback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def page_content_update_callback(app):
        """
        Initialise le callback pour mettre à jour dynamiquement le contenu de la page
        principale en fonction de l'URL.

        Args:
            app (dash.Dash): L'application Dash principale.

        Returns:
            None
        """

    Cette fonction enregistre un callback pour changer dynamiquement le contenu affiché
    dans la section `page-content` de l'application Dash.

---

display_page
~~~~~~~~~~~~

.. code-block:: python

    def display_page(pathname):
        """
        Charge la page correspondant à l'URL fournie.

        Args:
            pathname (str): Le chemin de l'URL actuel.

        Returns:
            dash.html.Div: Le contenu de la page correspondant au chemin fourni.

        Description :
        - Cette fonction utilise `pathname` pour déterminer quelle page charger.
        - Elle gère plusieurs pages, y compris :
          - `/analyse_par_commune`: Charge la page d'analyse par commune.
          - `/comparaison_scenario`: Charge la page de comparaison des scénarios.
          - `/reference`: Charge la page de références.
          - `/transport_en_commun`: Charge la page de transport en commun.
          - `/bord`: Charge le tableau de bord principal.
          - `/detail_bus/<ligne_id>`: Affiche les détails d'une ligne de bus spécifique.
        - Si l'URL ne correspond à aucune page connue, elle affiche la page d'accueil par défaut.

        Exemple :
        ---------
        - Pour une URL `/analyse_par_commune`, la fonction retournera le contenu `detail_zone(app)`.
        - Pour une URL `/transport_en_commun`, la fonction retournera le contenu `bus()`.
        """

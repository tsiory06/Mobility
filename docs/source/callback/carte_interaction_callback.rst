Carte Interaction Callback Module
=================================

Ce module gère les interactions utilisateur avec la carte dans l'application Dash, notamment les clics sur des zones spécifiques et l'activation du mode plein écran.

Fonctions principales :
- `carte_interaction_callback`: Initialise le callback pour détecter les zones cliquées sur la carte.
- `plein_ecran_carte`: Gère le basculement entre le mode plein écran et le mode partagé pour la carte et les graphiques.

---

Fonctions
---------

carte_interaction_callback
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def carte_interaction_callback(app, gdf_communes):
        """
        Initialise un callback pour détecter les zones cliquées sur une carte.

        Args:
            app (dash.Dash): L'application Dash principale.
            gdf_communes (GeoDataFrame): Données géographiques des communes.

        Returns:
            None
        """

    Description :
    - Lorsque l'utilisateur clique sur la carte, cette fonction récupère les coordonnées ou l'emplacement cliqué.
    - Si le lieu cliqué correspond à une zone, elle est ajoutée à la liste des zones cliquées.

    Arguments du Callback :
    - **Input**: `map.clickData` - Données sur le clic de l'utilisateur sur la carte.
    - **State**: `clicked-zones.data` - Liste des zones déjà cliquées.

    Exemple :
    ---------
    - Si un utilisateur clique sur une commune, la zone correspondante est ajoutée à la liste des zones.

---

plein_ecran_carte
~~~~~~~~~~~~~~~~~

.. code-block:: python

    def plein_ecran_carte(app):
        """
        Initialise un callback pour basculer entre les modes plein écran et partagé pour la carte et les graphiques.

        Args:
            app (dash.Dash): L'application Dash principale.

        Returns:
            None
        """

    Description :
    - Permet de basculer entre une vue plein écran de la carte et une vue partagée avec des graphiques.
    - Le style des colonnes contenant la carte et les graphiques est ajusté dynamiquement.

    Arguments du Callback :
    - **Input**: `fullscreen-btn.n_clicks` - Nombre de clics sur le bouton plein écran.
    - **State**: `map-col.style` - Style actuel de la colonne contenant la carte.

    Exemple :
    ---------
    - Lors d'un clic sur le bouton plein écran, la carte occupe toute la largeur disponible.
    - Les graphiques associés sont masqués ou affichés en fonction de l'état actuel.

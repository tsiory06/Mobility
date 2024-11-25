Carte Ligne Bus Layout Module
=============================

Ce module définit la disposition de la carte interactive pour les lignes de bus. Cette disposition permet à l'utilisateur de visualiser et d'interagir avec les données géospatiales des lignes de transport en commun.

---

Fonction principale
-------------------

### **`carte_ligne_bus_layout`**
Crée le composant principal de visualisation des lignes de bus.

.. code-block:: python

    def carte_ligne_bus_layout():
        """
        Crée une disposition interactive pour visualiser les lignes de transport en commun sur une carte.

        Returns:
            html.Div: Un div contenant tous les composants nécessaires pour la carte interactive.
        """

---

Structure du layout
-------------------

1. **Stores (`dcc.Store`) :**
   - `selected-transport_en_commun-lines-store` : Stocke les lignes de transport sélectionnées.
   - `legend-visible` : Gère la visibilité de la légende.

2. **Filtres et options :**
   - **Dropdowns (`dcc.Dropdown`) :**
     - Sélection des lignes de transport en commun à analyser.
     - Options de visualisation des couleurs des lignes.
   - **Menu de visualisation (`dbc.DropdownMenu`) :**
     - Options supplémentaires telles que la répartition zonale, les arrêts de bus, et les points de congestion.

3. **Carte interactive (`dcc.Graph`) :**
   - ID : `transport_en_commun-map`
   - Visualise les lignes de transport avec des options configurables pour les couleurs et les couches supplémentaires.

4. **Légende :**
   - ID : `couleur-legend`
   - Affiche des indications sur les couleurs utilisées pour les données affichées (comme le nombre de rotations ou les passagers).

5. **Détails des lignes :**
   - ID : `transport_en_commun-details-container`
   - Affiche les détails des lignes sélectionnées.

---

Composants interactifs
----------------------

1. **Dropdowns :**
   - `transport_en_commun-line-analyse_par_commune` : Permet de sélectionner une ou plusieurs lignes de transport en commun.
   - `ligne-visual-options` : Définit la manière dont les couleurs des lignes sont affichées sur la carte (ex. distance aller-retour, nombre de passagers).

2. **Checklist :**
   - Options pour visualiser les arrêts, les points de congestion, ou les répartitions zonales.

3. **Carte :**
   - Représente les lignes et les données associées sur une carte interactive.

4. **Légende :**
   - Dynamique, visible uniquement lorsque nécessaire.

---

Détails des arguments et retour
-------------------------------

- **Aucun argument requis.**
- **Retourne :** Une instance de `html.Div` contenant la disposition complète pour la carte interactive.

---

Style et personnalisation
-------------------------

- **Disposition flexible :**
  - Les éléments sont organisés en flexbox pour une mise en page fluide.

- **Légende dynamique :**
  - La visibilité de la légende est gérée dynamiquement via un `dcc.Store`.

- **Composants Dash Bootstrap :**
  - Utilisation de `dbc.DropdownMenu` et `dbc.Card` pour une présentation moderne et réactive.

---

Exemple d'intégration
----------------------

### **Ajout au layout principal**

.. code-block:: python

    from dash import html
    from my_app.carte_ligne_bus_layout import carte_ligne_bus_layout

    app.layout = html.Div(
        [
            carte_ligne_bus_layout(),
            html.Div(id='main-content', style={'margin-left': '250px'}),
        ]
    )

---

Avantages
---------

- Intégration des options de personnalisation directement dans l'interface.
- Disposition moderne et flexible adaptée à diverses tailles d'écrans.
- Ajout dynamique de couches de données sur la carte en fonction des choix de l'utilisateur.

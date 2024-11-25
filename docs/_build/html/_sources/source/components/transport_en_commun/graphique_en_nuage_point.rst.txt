Graphique en Nuage de Points Module
===================================

Ce module définit une disposition interactive pour visualiser les relations entre deux indicateurs sous forme de nuage de points (scatter plot). Il permet de comparer divers indicateurs à l'aide de dropdowns interactifs.

---

Fonction principale
-------------------

### **`graphique_en_nuage_point`**
Crée une disposition permettant de sélectionner deux indicateurs et de visualiser leur relation via un graphique interactif.

.. code-block:: python

    def graphique_en_nuage_point():
        """
        Crée une interface utilisateur pour afficher un graphique en nuage de points et comparer deux indicateurs.

        Returns:
            html.Div: Un div contenant la disposition de l'interface.
        """

---

Structure du layout
-------------------

1. **Colonne gauche : Filtres interactifs**
   - **Dropdown pour l'axe X (`dcc.Dropdown`) :**
     - Permet de sélectionner l'indicateur à afficher sur l'axe X.
     - Valeur par défaut : `nombre_passager_jour`.
   - **Dropdown pour l'axe Y (`dcc.Dropdown`) :**
     - Permet de sélectionner l'indicateur à afficher sur l'axe Y.
     - Valeur par défaut : `nombre_bus_jour`.

   **Indicateurs disponibles :**
   - Nombre de passagers (`nombre_passager_jour`)
   - Distance Primus-Terminus (`distance_primus_terminus`)
   - Nombre de transport_en_commun (`nombre_bus_jour`)
   - Nombre de rotations par jour (`nombre_rotation`)
   - Consommation moyenne par jour (`consomation_jour`)

2. **Colonne droite : Graphique et statistiques**
   - **Graphique interactif (`dcc.Graph`) :**
     - ID : `scatter`
     - Affiche la relation entre les indicateurs sélectionnés.
   - **Statistiques (`html.Div`) :**
     - Zone réservée pour des informations comme la corrélation, les moyennes ou les médianes des indicateurs.

3. **Disposition générale :**
   - Disposition en deux colonnes :
     - **Colonne gauche (Filtres interactifs)** : Largeur 4.
     - **Colonne droite (Graphique et statistiques)** : Largeur 8.

---

Composants interactifs
----------------------

1. **Filtres :**
   - Deux dropdowns pour sélectionner les indicateurs des axes X et Y.
   - Options personnalisées pour des analyses spécifiques aux données de mobilité.

2. **Graphique :**
   - Nuage de points généré dynamiquement en fonction des sélections des axes.

3. **Statistiques :**
   - Section réservée pour afficher des mesures complémentaires, telles que :
     - Corrélation entre les deux indicateurs.
     - Moyenne et médiane des valeurs.

---

Détails des arguments et retour
-------------------------------

- **Aucun argument requis.**
- **Retourne :** Une instance de `html.Div` contenant la disposition complète.

---

Style et personnalisation
-------------------------

- **Design épuré :**
  - Colonne gauche avec un fond clair pour les filtres.
  - Colonne droite avec une carte ombrée pour le graphique.

- **Dropdowns :**
  - Labels descriptifs pour faciliter la sélection des indicateurs.

- **Graphique :**
  - Carte ombrée avec un en-tête stylisé.

---

Exemple d'intégration
----------------------

### **Ajout au layout principal**

.. code-block:: python

    from dash import html
    from my_app.graphique_en_nuage_point import graphique_en_nuage_point

    app.layout = html.Div(
        [
            graphique_en_nuage_point(),
            html.Div(id='main-content', style={'margin-left': '20px'}),
        ]
    )

---

Avantages
---------

- Interface utilisateur intuitive pour explorer les relations entre les indicateurs.
- Options variées pour personnaliser l'analyse.
- Visualisation claire des relations via un nuage de points interactif.
- Extensible pour ajouter des indicateurs ou des statistiques complémentaires.

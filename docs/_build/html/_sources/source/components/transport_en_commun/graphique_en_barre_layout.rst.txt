Graphique en Barre Layout Module
================================

Ce module définit une disposition interactive pour visualiser les indicateurs sous forme de graphique en barre. Il inclut une interface utilisateur intuitive pour sélectionner les indicateurs, consulter des KPI, et afficher les graphiques.

---

Fonction principale
-------------------

### **`graphique_en_barre_layout`**
Crée l'interface principale pour sélectionner et visualiser des indicateurs.

.. code-block:: python

    def graphique_en_barre_layout():
        """
        Crée une interface utilisateur pour afficher des graphiques et des KPI.

        Returns:
            html.Div: Un div contenant la disposition de l'interface.
        """

---

Structure du layout
-------------------

1. **Colonne gauche : Filtres et KPI**
   - **Dropdown (`dcc.Dropdown`) :**
     - Permet de sélectionner un indicateur à visualiser.
     - Options disponibles :
       - Nombre de passagers (`nombre_passager_jour`)
       - Distance Primus-Terminus (`distance_primus_terminus`)
       - Nombre de bus (`nombre_bus_jour`)
       - Nombre de rotations par jour (`nombre_rotation`)

   - **KPI Cards :**
     - Moyenne, Médiane, Valeur minimale, et Valeur maximale.
     - Couleurs pour chaque KPI :
       - Moyenne : Bleu (`#17a2b8`)
       - Médiane : Vert (`#28a745`)
       - Min : Jaune (`#ffc107`)
       - Max : Rouge (`#dc3545`)

2. **Colonne droite : Graphique**
   - **Graphique interactif (`dcc.Graph`) :**
     - ID : `graphique`
     - Affiche un graphique en barre basé sur l'indicateur sélectionné.

3. **Disposition générale :**
   - Disposition en deux colonnes :
     - **Colonne gauche (Filtres et KPI)** : Largeur 4.
     - **Colonne droite (Graphique)** : Largeur 8.

---

Composants interactifs
----------------------

1. **Filtres :**
   - Dropdown pour sélectionner l'indicateur.
   - Options adaptées à l'analyse des données de mobilité.

2. **KPI :**
   - Quatre cartes affichant des mesures clés calculées dynamiquement.

3. **Graphique :**
   - Généré dynamiquement selon l'indicateur sélectionné.

---

Détails des arguments et retour
-------------------------------

- **Aucun argument requis.**
- **Retourne :** Une instance de `html.Div` contenant la disposition complète.

---

Style et personnalisation
-------------------------

- **Design épuré :**
  - Utilisation de `dash-bootstrap-components` pour un style moderne et réactif.
  - Fond clair pour la colonne des filtres.

- **KPI :**
  - Cartes colorées avec bordures et alignement en grille.

- **Graphique :**
  - Carte ombrée avec un en-tête stylisé.

---

Exemple d'intégration
----------------------

### **Ajout au layout principal**

.. code-block:: python

    from dash import html
    from my_app.graphique_en_barre_layout import graphique_en_barre_layout

    app.layout = html.Div(
        [
            graphique_en_barre_layout(),
            html.Div(id='main-content', style={'margin-left': '20px'}),
        ]
    )

---

Avantages
---------

- Interface utilisateur intuitive pour explorer les données.
- Mesures clés (KPI) présentées de manière claire et concise.
- Graphique généré dynamiquement selon les sélections.
- Facilement extensible pour inclure d'autres indicateurs ou fonctionnalités.

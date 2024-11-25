Sidebar Layout Module
=====================

Ce module définit la disposition de la barre latérale pour une application Dash. La barre latérale est utilisée pour afficher des options interactives permettant à l'utilisateur de sélectionner des thèmes et des catégories pour la visualisation de données.

---

Fonction principale
-------------------

### **`sidebar_layout`**
Génère le composant de la barre latérale avec des sections interactives.

.. code-block:: python

    def sidebar_layout():
        """
        Crée la disposition de la barre latérale avec des options interactives pour les utilisateurs.

        Returns:
            html.Div: Un div contenant la barre latérale, ses sections, et ses éléments interactifs.
        """

        ### Exemple d'utilisation:
        ```
        app.layout = html.Div(
            [
                sidebar_layout(),
                html.Div(id='main-content', style={'margin-left': '250px'}),
            ]
        )
        ```

---

Structure de la barre latérale
------------------------------

1. **En-tête :** 
   - Le titre "Thèmes" centré, avec un fond sombre et du texte blanc.

2. **Sections :**
   - Chaque section est encapsulée dans un composant `Accordion` de Dash Bootstrap Components (DBC).
   - Les éléments interactifs sont des listes de cases à cocher (`dcc.Checklist`).

3. **Sections incluses :**

   **Trafic et Circulation**
   - Segments routiers avec le plus grand trafic.
   - Itinéraires les plus empruntés.
   - Routes les plus congestionnées.
   - Points de congestion dans la ville.

   **Mobilité et Données Démographiques**
   - Densité de population.
   - Typologie modale.
   - Matrice Origine-Destination (OD).
   - Volume de déplacement.

---

Détails des arguments et retour
-------------------------------

- **Aucun argument requis.**
- **Retourne :** Une instance de `html.Div` contenant le layout complet de la barre latérale.

---

Composants interactifs
----------------------

1. **Checklists (`dcc.Checklist`) :**
   - Permettent à l'utilisateur de sélectionner un ou plusieurs thèmes à visualiser.
   - Chaque option est configurée avec une étiquette (`label`) et une valeur (`value`).

2. **Accordéons (`dbc.Accordion`) :**
   - Permettent de regrouper les thèmes par catégories et d'optimiser l'espace en rendant les sections extensibles.

3. **Défilement :**
   - Une hauteur fixe est définie (`90vh`) avec un défilement vertical activé (`overflow-y: auto`).

---

Style et personnalisation
-------------------------

- **Couleurs :**
  - Fond sombre (`#2c3e50`) pour une bonne lisibilité.
  - Texte en blanc pour un contraste optimal.

- **Disposition :**
  - Chaque section est bien espacée avec des marges et des styles de padding.

- **Scroll :**
  - Un style de défilement est activé pour gérer les options dans des écrans plus petits.

---

Exemple d'intégration
----------------------

### **Ajout au layout principal**

.. code-block:: python

    from dash import html
    from my_app.sidebar import sidebar_layout

    app.layout = html.Div(
        [
            sidebar_layout(),
            html.Div(id='main-content', style={'margin-left': '250px'}),
        ]
    )

### **Style CSS recommandé pour les scrollbars**

Ajoutez le style suivant dans votre fichier CSS pour une barre de défilement personnalisée :

```css
.scroll-style {
    scrollbar-width: thin;
    scrollbar-color: #888 #2c3e50;
}

.scroll-style::-webkit-scrollbar {
    width: 8px;
}

.scroll-style::-webkit-scrollbar-track {
    background: #2c3e50;
}

.scroll-style::-webkit-scrollbar-thumb {
    background-color: #888;
    border-radius: 10px;
}

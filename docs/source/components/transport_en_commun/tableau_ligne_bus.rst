Génération des Tableaux par Lignes de Bus
=========================================

Ce module définit des fonctions pour créer des tableaux interactifs, formatés et organisés en trois catégories principales : **Performance Financière**, **Utilisation des Ressources**, et **Volume de Passagers**. Les données sont présentées avec des options de tri, de filtrage, et des boutons de téléchargement.

---

Fonctions principales
---------------------

### **`generate_table_ligne_bus`**
Crée trois tableaux interactifs, un pour chaque catégorie d'indicateurs.

.. code-block:: python

    def generate_table_ligne_bus():
        """
        Génère des tableaux interactifs pour afficher les performances financières, l'utilisation des ressources
        et le volume de passagers des lignes de bus.

        Returns:
            html.Div: Un div contenant trois cartes avec les tableaux pour chaque catégorie.
        """

---

### **`create_table_ligne_bus`**
Crée un tableau interactif pour une catégorie spécifique.

.. code-block:: python

    def create_table_ligne_bus(df, columns, title):
        """
        Crée un tableau interactif pour afficher des indicateurs spécifiques.

        Args:
            df (pd.DataFrame): Données formatées des lignes de bus.
            columns (list): Liste des colonnes à inclure dans le tableau.
            title (str): Titre de la table.

        Returns:
            dbc.Card: Une carte contenant un tableau interactif et un bouton de téléchargement.
        """

---

### **`format_value`**
Formate les valeurs numériques avec des unités et un alignement cohérent.

.. code-block:: python

    def format_value(value, column):
        """
        Formate une valeur avec des unités appropriées.

        Args:
            value (int, float): Valeur à formater.
            column (str): Nom de la colonne, utilisé pour déterminer l'unité.

        Returns:
            str: Valeur formatée avec l'unité.
        """

---

Structure des tableaux
----------------------

1. **Tableau : Performance Financière et Rentabilité**
   - Colonnes incluses :
     - Numéro de ligne
     - Coût de carburant par jour (Ar)
     - Revenu par jour (Ar)
     - Coût total d'exploitation (Ar)
     - Rentabilité par jour (Ar)
     - Coût par passager (Ar)

2. **Tableau : Utilisation des Ressources et Efficacité Opérationnelle**
   - Colonnes incluses :
     - Numéro de ligne
     - Consommation moyenne par jour (L)
     - Nombre de transport_en_commun par jour
     - Nombre de rotations par jour
     - Bus par kilomètre
     - Distance moyenne entre arrêts (km)
     - Durée moyenne d'une rotation (min)

3. **Tableau : Volume de Passagers et Occupation**
   - Colonnes incluses :
     - Numéro de ligne
     - Nombre de passagers par jour
     - Taux de remplissage moyen
     - Capacité d'un transport_en_commun

---

Caractéristiques des tableaux
-----------------------------

- **Interactions disponibles :**
  - Tri des colonnes
  - Pagination
  - Filtrage (uniquement pour certaines colonnes)

- **Bouton de téléchargement :**
  - Permet de télécharger les données au format Excel.
  - Bouton unique pour chaque tableau.

- **Formatage des valeurs :**
  - Valeurs numériques formatées avec séparateurs de milliers et unités appropriées.
  - Exemple : `10 000,00 Ar`, `15,50 %`.

---

Style et personnalisation
-------------------------

- **Tableaux :**
  - Alignement des cellules à droite pour les données numériques.
  - En-têtes centrés et stylisés.

- **Boutons de téléchargement :**
  - Couleur bleue avec une ombre légère.

- **Cartes :**
  - Fond ombré et marges entre les cartes.

---

Exemple d'intégration
----------------------

.. code-block:: python

    from dash import Dash, html
    from my_app.tableau_lignes_bus import generate_table_ligne_bus

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Analyse des Lignes de Bus"),
        generate_table_ligne_bus()  # Intégration des tableaux
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)

---

Avantages
---------

1. Présentation organisée des indicateurs en catégories logiques.
2. Fonctionnalités interactives pour explorer les données.
3. Possibilité de télécharger les données pour des analyses supplémentaires.
4. Formatage professionnel des valeurs pour une meilleure lisibilité.

---

Extensions possibles
--------------------

1. **Ajout de graphiques :**
   - Inclure des graphiques résumant les indicateurs principaux pour chaque tableau.

2. **Filtres avancés :**
   - Ajouter des options de filtrage global (ex. par plage de valeurs).

3. **Exportation au format CSV ou PDF :**
   - Étendre les fonctionnalités de téléchargement.

4. **Personnalisation des couleurs :**
   - Adapter les styles en fonction de la charte graphique.

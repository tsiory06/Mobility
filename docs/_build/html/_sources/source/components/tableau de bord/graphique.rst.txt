Graphique Module
=================

Ce module contient des fonctions pour générer divers graphiques et visualisations utilisées dans les tableaux de bord. Ces visualisations incluent des histogrammes, des graphiques à barres, des diagrammes circulaires, et des diagrammes de Sankey.

---

Fonctions principales
---------------------

### **`generate_population_histogram`**
Génère un histogramme de population ou un diagramme circulaire en fonction des zones sélectionnées.

.. code-block:: python

    def generate_population_histogram(noms_communes=None):
        """
        Crée un histogramme ou un diagramme circulaire pour afficher les données de population.

        Args:
            noms_communes (list, optional): Liste des communes sélectionnées. Si une seule commune est sélectionnée,
                                            un diagramme circulaire est généré.

        Returns:
            html.Div: Div contenant le graphique généré et les détails contextuels.
        """

### **`generate_graph_deplacement`**
Génère un graphique à barres empilées pour les productions et attractions de déplacements par zone.

.. code-block:: python

    def generate_graph_deplacement(noms_zones=None):
        """
        Crée un graphique à barres empilées pour visualiser les productions et attractions.

        Args:
            noms_zones (list, optional): Liste des zones sélectionnées.

        Returns:
            html.Div: Div contenant le graphique généré et des détails explicatifs.
        """

### **`generate_graph_vehicules`**
Crée une visualisation des types de véhicules par zone.

.. code-block:: python

    def generate_graph_vehicules(noms_zones=None):
        """
        Génère un graphique circulaire ou un graphique à barres empilées pour représenter la répartition
        des types de véhicules.

        Args:
            noms_zones (list, optional): Liste des zones sélectionnées.

        Returns:
            html.Div: Div contenant le graphique généré.
        """

### **`generate_sankey_diagram`**
Crée un diagramme de Sankey pour visualiser les flux de déplacements entre zones.

.. code-block:: python

    def generate_sankey_diagram(noms_zones=None):
        """
        Crée un diagramme de Sankey pour représenter les flux de déplacements.

        Args:
            noms_zones (list, optional): Liste des zones sélectionnées.

        Returns:
            html.Div: Div contenant le diagramme généré et les explications contextuelles.
        """

---

Détails des visualisations
--------------------------

### Population par commune
- Affiche la répartition de la population pour les communes sélectionnées.
- Utilise un histogramme pour plusieurs communes ou un diagramme circulaire pour une seule commune.

### Déplacements
- Visualisation des productions (départs) et attractions (arrivées) par zone.
- Les données sont exprimées en pourcentage pour faciliter la comparaison.

### Répartition des véhicules
- Représente la part des types de véhicules par zone.
- Utilise un graphique à barres empilées ou un diagramme circulaire.

### Diagramme de Sankey
- Affiche les flux de mobilité entre différentes zones.
- Les liens indiquent les volumes de déplacements.

---

Exemples d'utilisation
-----------------------

Ces fonctions peuvent être intégrées dans des applications Dash pour fournir des visualisations interactives et riches en informations dans des tableaux de bord analytiques.

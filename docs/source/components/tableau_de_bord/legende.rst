Legend Module
=============

Ce module fournit une fonction principale pour générer des légendes personnalisées dans une application Dash. Les légendes permettent de fournir des informations visuelles et contextuelles sur les graphiques ou les visualisations.

---

Fonctions principales
---------------------

### **`generate_legend`**
Génère une légende interactive avec des couleurs, des valeurs associées, un titre, et une icône d'information.

.. code-block:: python

    def generate_legend(titre, couleurs, valeurs, legend_id):
        """
        Crée une légende interactive avec des couleurs et des valeurs associées.

        Args:
            titre (str): Le titre de la légende.
            couleurs (list): Liste des couleurs associées aux valeurs.
            valeurs (list): Liste des valeurs ou descriptions correspondant aux couleurs.
            legend_id (str): Identifiant unique pour l'élément de légende.

        Returns:
            html.Div: Une div contenant la légende avec les couleurs, descriptions, et une icône d'information.
        """

        ### Exemple d'utilisation:
        ```
        couleurs = ['#FFEDA0', '#FEB24C', '#FC4E2A', '#E31A1C', '#BD0026']
        valeurs = ['0-60,000 habitants', '60,001-100,000 habitants', '100,001-150,000 habitants', 
                   '150,001-250,000 habitants', '250,001+ habitants']
        generate_legend('Population', couleurs, valeurs, 'population-legend')
        ```

---

Structure des éléments générés
------------------------------

1. **Titre de la légende :** Un titre principal pour identifier le contexte de la légende.
2. **Couleurs et valeurs :** Une liste d'éléments où chaque couleur est associée à une description ou une valeur.
3. **Icône d'information :** Une icône qui, lorsqu'elle est survolée, affiche un popover contenant des détails supplémentaires sur la légende.

---

Détails des arguments
---------------------

- **`titre`** : Le titre de la légende affiché au-dessus des éléments.
- **`couleurs`** : Une liste de couleurs en format hexadécimal ou CSS.
- **`valeurs`** : Une liste de valeurs ou descriptions correspondant à chaque couleur.
- **`legend_id`** : Identifiant unique pour permettre de cibler chaque légende individuellement dans le DOM.

---

Comportement interactif
-----------------------

- Lors du survol de l'icône d'information (`info-icon`), un popover s'affiche avec des détails explicatifs.
- Chaque couleur et valeur est affichée dans un bloc avec un cercle coloré et une description.

---

Exemples d'intégration
-----------------------

### **Exemple 1 : Légende pour la densité de population**

.. code-block:: python

    couleurs = ['#FFEDA0', '#FEB24C', '#FC4E2A', '#E31A1C', '#BD0026']
    valeurs = ['0-60,000 habitants', '60,001-100,000 habitants', 
               '100,001-150,000 habitants', '150,001-250,000 habitants', 
               '250,001+ habitants']
    legend = generate_legend('Densité de Population', couleurs, valeurs, 'population-legend')

### **Exemple 2 : Légende pour les volumes de trafic**

.. code-block:: python

    couleurs = ['#440154', '#3B528B', '#21918C', '#5EC962', '#FDE725']
    valeurs = ['100-200 véhicules/heure', '201-300 véhicules/heure', 
               '301-500 véhicules/heure', '501-800 véhicules/heure', 
               '800+ véhicules/heure']
    legend = generate_legend('Volume de Trafic', couleurs, valeurs, 'traffic-legend')

---

Avantages
---------

- Permet une personnalisation complète des couleurs et des valeurs.
- Ajoute des informations interactives pour améliorer l'expérience utilisateur.
- Facile à intégrer dans n'importe quelle application Dash avec `Dash Bootstrap Components`.

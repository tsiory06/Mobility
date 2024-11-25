extractKodatuDataBus
=====================

Cette fonction extrait, nettoie et enrichit les données des lignes de bus à partir d'un fichier Excel. Les données sont préparées pour une utilisation dans des analyses avancées.

Description
-----------
La fonction lit les données depuis une feuille Excel contenant les informations sur les lignes de bus, sélectionne les colonnes pertinentes, calcule des métriques supplémentaires (comme la consommation totale de carburant), et retourne un DataFrame prêt pour l'analyse.

Étapes principales :
- Chargement des données brutes depuis le fichier Excel.
- Nettoyage : suppression des colonnes vides et des lignes inutiles.
- Sélection des colonnes pertinentes.
- Calcul de la consommation totale en carburant en fonction des distances parcourues et des rotations.
- Renvoi du DataFrame formaté.

Paramètres
----------
Aucun.

Colonnes finales
----------------
Le DataFrame retourné contient les colonnes suivantes :

+----------------------------+-------------------------------------------------------------+
| Nom de colonne             | Description                                                 |
+============================+=============================================================+
| ``ligne``                  | Identifiant ou numéro de la ligne                           |
+----------------------------+-------------------------------------------------------------+
| ``cooperative``            | Coopérative responsable de la ligne                        |
+----------------------------+-------------------------------------------------------------+
| ``primus``                 | Point de départ (Primus)                                    |
+----------------------------+-------------------------------------------------------------+
| ``terminus``               | Point d'arrivée (Terminus)                                  |
+----------------------------+-------------------------------------------------------------+
| ``distance_primus_terminus``| Distance entre Primus et Terminus (en km)                  |
+----------------------------+-------------------------------------------------------------+
| ``distance_aller_retour``  | Distance aller-retour totale (en km)                       |
+----------------------------+-------------------------------------------------------------+
| ``nombre_arret``           | Nombre d'arrêts                                             |
+----------------------------+-------------------------------------------------------------+
| ``passsage_zone``          | Passage par des zones d'activité                            |
+----------------------------+-------------------------------------------------------------+
| ``intermodalite_rocade``   | Indicateur d'intermodalité avec la rocade                   |
+----------------------------+-------------------------------------------------------------+
| ``Nombre_Bus``             | Nombre de bus opérant sur cette ligne                      |
+----------------------------+-------------------------------------------------------------+
| ``Age_Moyen_Parc``         | Âge moyen du parc de bus                                    |
+----------------------------+-------------------------------------------------------------+
| ``rotation``               | Nombre de rotations effectuées par jour                    |
+----------------------------+-------------------------------------------------------------+
| ``heure_travail``          | Heures de travail                                           |
+----------------------------+-------------------------------------------------------------+
| ``heure_exploitation``     | Heures d'exploitation                                       |
+----------------------------+-------------------------------------------------------------+
| ``nombre_passager``        | Nombre de passagers transportés                            |
+----------------------------+-------------------------------------------------------------+
| ``Consommation``           | Consommation moyenne de carburant (en L/100 km)            |
+----------------------------+-------------------------------------------------------------+
| ``Consommation_totale``    | Consommation totale (basée sur les distances et rotations)  |
+----------------------------+-------------------------------------------------------------+

Retour
------
**Type** : ``pandas.DataFrame``  
Le DataFrame formaté contenant les données enrichies.

Exemple d'utilisation
----------------------
::

    # Extraction des données des lignes de bus
    df_bus = extractKodatuDataBus()

    # Affichage des premières lignes du DataFrame
    print(df_bus.head())

    # Calcul de statistiques descriptives
    print(df_bus.describe())

Extensions possibles
--------------------
- **Visualisation :**
  Générer des graphiques pour analyser la consommation ou le nombre de rotations par ligne.
- **Validation :**
  Ajouter des étapes pour détecter et corriger les valeurs aberrantes.
- **Intégration SIG :**
  Ajouter des coordonnées géographiques pour une visualisation cartographique.
- **Estimation des coûts :**
  Modéliser les coûts par ligne en fonction des données extraites.

Source des données
------------------
Le fichier utilisé est : ``data/Codatu_BDD lignes existantes_202407.xlsx``.

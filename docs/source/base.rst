=====================================================
Documentation des Tables et Vues SQL pour le Projet
=====================================================

Ce fichier SQL structure une base de données pour un projet de gestion et d'analyse de la mobilité urbaine. Il comprend les tables, les vues et des exemples d'insertion de données initiales.

---

**Base de Données :** `buss`

La base de données `buss` est destinée à stocker et analyser les informations relatives aux déplacements urbains, aux scénarios de simulation, et aux caractéristiques des communes.

---

**Création des Tables**
-----------------------

1. **commune**
   - Stocke les informations de base des communes géographiques.
   - **Colonnes :**
     - `id` : Identifiant unique (clé primaire).
     - `nom_commune` : Nom de la commune.
     - `identifiant_commune` : Code unique de la commune.

2. **fokotany**
   - Associe les fokotany à leurs communes respectives.
   - **Colonnes :**
     - `id` : Identifiant unique.
     - `id_commune` : Référence à la table `commune`.
     - `nom_fokotany` : Nom du fokotany.

3. **population**
   - Stocke les données de population par fokotany et tranche d'âge.
   - **Colonnes :**
     - `id` : Identifiant unique.
     - `id_fokotany` : Référence au fokotany.
     - `id_tranche_age` : Référence à la tranche d'âge.
     - `annee_enregistrement` : Année de l'enregistrement.
     - `nombre_population` : Nombre d'individus.

4. **tranche_age**
   - Définit les tranches d'âge.
   - **Colonnes :**
     - `id` : Identifiant unique.
     - `tranche` : Description de la tranche (ex. : "0-5 ans").
     - `age_min` : Âge minimum.
     - `age_max` : Âge maximum.

5. **types_vehicules**
   - Stocke les types de véhicules utilisés dans la base.
   - **Colonnes :**
     - `id` : Identifiant unique.
     - `nom_type` : Nom du type de véhicule (ex. : "Voiture").

6. **matrice_od**
   - Définit les origines et destinations des déplacements.
   - **Colonnes :**
     - `id` : Identifiant unique.
     - `id_origine_commune` : Commune d'origine.
     - `id_destination_commune` : Commune de destination.
     - `id_type_vehicule` : Type de véhicule utilisé.
     - `nombre_deplacements` : Nombre de déplacements.

7. **hierarchie_fonctionnelle**
   - Définit les niveaux de hiérarchie des routes.
   - **Colonnes :**
     - `id` : Identifiant unique.
     - `nom_niveau` : Niveau hiérarchique (ex. : "Route principale").

8. **route**
   - Stocke les informations sur les routes et leur hiérarchie.
   - **Colonnes :**
     - `id` : Identifiant unique.
     - `id_hierarchie` : Référence à la hiérarchie fonctionnelle.
     - `id_OSM` : Identifiant OpenStreetMap.

9. **flux_trafic**
   - Stocke les données de flux de trafic pour chaque route.
   - **Colonnes :**
     - `id` : Identifiant unique.
     - `id_departed` : Route de départ.
     - `id_arrived` : Route d'arrivée.
     - `id_type_vehicule` : Type de véhicule utilisé.
     - `id_periode_temps` : Période temporelle (ex. : "Matin").
     - `volume_deplacement` : Volume total des déplacements.
     - `vitesse_moyenne` : Vitesse moyenne des véhicules.
     - `temps_de_trajet` : Temps de trajet moyen.
     - `distance` : Distance moyenne.

10. **scenario**
    - Stocke les scénarios simulés pour les analyses de mobilité.
    - **Colonnes :**
      - `id` : Identifiant unique.
      - `nom_scenario` : Nom du scénario.
      - `description_scenario` : Description du scénario.
      - `type_scenario` : Type de scénario (ex. : "Base", "Projection").
      - `date_simulation` : Date de simulation.

---

**Création des Vues**
---------------------

1. **vue_population_par_commune**
   - Agrège les données de population par commune et par tranche d'âge.
   - **Colonnes :**
     - `nom_commune` : Nom de la commune.
     - `tranche` : Tranche d'âge.
     - `total_population` : Total de la population.

2. **vue_productions_attractions**
   - Analyse les productions et attractions de déplacements par commune.
   - **Colonnes :**
     - `nom_commune` : Nom de la commune.
     - `total_productions` : Nombre total de déplacements produits.
     - `total_attractions` : Nombre total de déplacements attirés.
     - `total_volume` : Volume total de déplacements.

3. **vue_matrice_od_par_commune**
   - Matrice origine-destination regroupée par commune.
   - **Colonnes :**
     - `nom_origine` : Commune d'origine.
     - `nom_destination` : Commune de destination.
     - `nombre_deplacements` : Nombre total de déplacements.

4. **vue_volume_deplacement_par_route**
   - Volume total des déplacements par route.
   - **Colonnes :**
     - `id_osm` : Identifiant OpenStreetMap.
     - `total_traffic_volume` : Volume total du trafic.

5. **vue_scenario**
   - Combinaison des détails des scénarios et indicateurs environnementaux.
   - **Colonnes :**
     - `nom_scenario` : Nom du scénario.
     - `debit_moyen` : Débit moyen simulé.
     - `co2`, `nox`, `co` : Émissions simulées.

---

**Exemple d'Insertion**
-----------------------

- Ajout de types de véhicules :
  .. code-block:: sql

     INSERT INTO types_vehicules (nom_type) VALUES ('Voiture'), ('Bus'), ('Moto');

- Ajout de tranches d'âge :
  .. code-block:: sql

     INSERT INTO tranche_age (tranche, age_min, age_max)
     VALUES
       ('0-5 ans', 0, 5),
       ('6-15 ans', 6, 15),
       ('16-25 ans', 16, 25),
       ('26-60 ans', 26, 60),
       ('61 ans et plus', 61, 120);

---

**Dépendances et Relations**
----------------------------

- `population` dépend de `fokotany` et `tranche_age`.
- `matrice_od` relie `commune` et `types_vehicules`.
- `flux_trafic` dépend de `route` et `periodes_temps`.

---

**Note :**
Les vues et les tables sont optimisées pour fournir des données agrégées et faciliter les analyses dans le contexte de la mobilité urbaine.

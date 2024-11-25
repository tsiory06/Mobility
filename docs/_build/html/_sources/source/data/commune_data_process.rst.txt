==============================================
Documentation Technique : Gestion des Communes
==============================================

Ce module contient des fonctions permettant d'extraire, de manipuler et d'analyser les données relatives aux communes, notamment les données de population, de connectivité, et de typologie modale.

Contenu du module
------------------
- `get_list_commune`
- `get_population_commune`
- `get_age_distribution_commune`
- `get_connections_commune`
- `get_typologie_modale_commune`
- `get_attraction_production_commune`
- `get_all_data_commune`

---

**get_list_commune**
---------------------

**Description :**
Cette fonction récupère la liste des noms de communes disponibles dans la vue `vue_population_par_commune`.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Une liste contenant les noms des communes.

**Exemple d'utilisation :**
.. code-block:: python

   communes = get_list_commune()

---

**get_population_commune**
---------------------------

**Description :**
Récupère les données de population pour une commune spécifique, regroupe les valeurs si plusieurs entrées existent, et calcule le pourcentage de population par rapport au total des communes.

**Paramètres d'entrée :**
- `commune` (str) : Le nom de la commune.

**Valeurs retournées :**
- Un DataFrame contenant :
  - `commune` : Le nom de la commune.
  - `population` : La population totale de la commune.
  - `population_percentage` : Pourcentage de la population par rapport au total.
  - `rank` : Classement de la commune (non calculé ici).

**Exemple d'utilisation :**
.. code-block:: python

   population_data = get_population_commune("Antananarivo")

---

**get_age_distribution_commune**
---------------------------------

**Description :**
Récupère la répartition par tranche d'âge pour une commune spécifique à partir de la vue `vue_population_par_commune`.

**Paramètres d'entrée :**
- `commune` (str) : Le nom de la commune.

**Valeurs retournées :**
- Un DataFrame contenant les tranches d'âge comme colonnes.

**Exemple d'utilisation :**
.. code-block:: python

   age_distribution = get_age_distribution_commune("Antananarivo")

---

**get_connections_commune**
----------------------------

**Description :**
Identifie les communes les plus et les moins connectées à une commune donnée, basée sur le nombre de déplacements dans la matrice OD.

**Paramètres d'entrée :**
- `commune` (str) : Le nom de la commune.

**Valeurs retournées :**
- Un DataFrame contenant :
  - `most_connected` : Liste des communes les plus connectées.
  - `most_connected_counts` : Liste des volumes de déplacements pour ces connexions.
  - `least_connected` : Liste des communes les moins connectées.
  - `least_connected_counts` : Liste des volumes de déplacements pour ces connexions.

**Exemple d'utilisation :**
.. code-block:: python

   connections = get_connections_commune("Antananarivo")

---

**get_typologie_modale_commune**
---------------------------------

**Description :**
Récupère la répartition des types de véhicules dans une commune spécifique.

**Paramètres d'entrée :**
- `commune` (str) : Le nom de la commune.

**Valeurs retournées :**
- Un DataFrame contenant :
  - Les colonnes pour chaque type de véhicule (e.g., Voiture, Moto, Bus).
  - Le total des véhicules par type.

**Exemple d'utilisation :**
.. code-block:: python

   typologie_modale = get_typologie_modale_commune("Antananarivo")

---

**get_attraction_production_commune**
--------------------------------------

**Description :**
Récupère les volumes de production et d'attraction pour une commune spécifique à partir de la vue `vue_productions_attractions`.

**Paramètres d'entrée :**
- `commune` (str) : Le nom de la commune.

**Valeurs retournées :**
- Un DataFrame contenant :
  - `commune` : Le nom de la commune.
  - `attraction` : Volume total d'attractions.
  - `production` : Volume total de productions.

**Exemple d'utilisation :**
.. code-block:: python

   attraction_production = get_attraction_production_commune("Antananarivo")

---

**get_all_data_commune**
-------------------------

**Description :**
Récupère toutes les données nécessaires pour une commune spécifique en combinant les résultats des autres fonctions.

**Paramètres d'entrée :**
- `commune` (str) : Le nom de la commune.

**Valeurs retournées :**
- Un dictionnaire structuré contenant les informations suivantes :
  - `general_info` : Population totale, pourcentage et rang.
  - `age_distribution` : Répartition par tranche d'âge.
  - `attraction_production` : Données de production et d'attraction.
  - `typologie_modale` : Répartition des types de véhicules.
  - `connections` : Communes les plus et les moins connectées.

**Exemple d'utilisation :**
.. code-block:: python

   commune_data = get_all_data_commune("Antananarivo")

---

**Remarques**
-------------
- Assurez-vous que les vues SQL utilisées dans les fonctions (e.g., `vue_population_par_commune`, `vue_productions_attractions`) existent dans la base de données.
- Chaque fonction ferme automatiquement la session SQL pour éviter les fuites de connexions.

**Avertissement :**
Certaines colonnes ou vues peuvent nécessiter une adaptation si leur structure change dans la base de données.

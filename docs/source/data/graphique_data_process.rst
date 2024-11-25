=======================================
Documentation des Fonctions de Requête
=======================================

Ce module fournit des fonctions pour interagir avec une base de données et extraire des informations sur les populations, les déplacements, et les véhicules par zone ou commune.

Contenu du module
------------------
- `get_population_par_commune`
- `get_volume_deplacements`
- `get_nombre_vehicules_par_zone`
- `create_od_matrix`
- `get_od_count`

---

**get_population_par_commune**
------------------------------

**Description :**
Récupère les données de population par commune à partir de la vue `vue_population_par_commune`. Si des noms de communes sont spécifiés, les données sont filtrées pour ces communes. Sinon, les communes avec les plus grandes populations sont sélectionnées.

**Paramètres d'entrée :**
- `noms_communes` (list, optionnel) : Liste des noms des communes à filtrer.

**Valeurs retournées :**
- Un DataFrame Pandas contenant :
  - `nom_commune` : Nom de la commune.
  - `total_population` : Population totale.

**Exemple d'utilisation :**
.. code-block:: python

   df_population = get_population_par_commune(['Antananarivo', 'Fianarantsoa'])

---

**get_volume_deplacements**
----------------------------

**Description :**
Récupère le volume total des déplacements produits et attirés par zone ou commune à partir de la vue `vue_productions_attractions`.

**Paramètres d'entrée :**
- `noms_zones` (list, optionnel) : Liste des noms de zones ou communes à filtrer.

**Valeurs retournées :**
- Un DataFrame Pandas contenant :
  - `nom_commune` : Nom de la commune.
  - `total_productions` : Nombre total de productions.
  - `total_attractions` : Nombre total d'attractions.
  - `total_volume` : Volume total des déplacements.

**Exemple d'utilisation :**
.. code-block:: python

   df_deplacements = get_volume_deplacements(['Antananarivo', 'Toamasina'])

---

**get_nombre_vehicules_par_zone**
----------------------------------

**Description :**
Récupère le nombre de véhicules par type et par zone ou commune à partir de la vue `vue_nombre_vehicules_par_commune`.

**Paramètres d'entrée :**
- `noms_zones` (list, optionnel) : Liste des noms de zones ou communes à filtrer.

**Valeurs retournées :**
- Un DataFrame Pandas contenant :
  - `nom_commune` : Nom de la commune.
  - `type_vehicule` : Type de véhicule (e.g., voiture, moto, bus).
  - `nombre_total` : Nombre total de véhicules.

**Exemple d'utilisation :**
.. code-block:: python

   df_vehicules = get_nombre_vehicules_par_zone(['Antananarivo'])

---

**create_od_matrix**
---------------------

**Description :**
Crée une matrice origine-destination (OD) à partir d'un DataFrame contenant les déplacements entre les communes d'origine et de destination.

**Paramètres d'entrée :**
- `df_matrice` (DataFrame) : Un DataFrame contenant les colonnes :
  - `nom_origine` : Nom de la commune d'origine.
  - `nom_destination` : Nom de la commune de destination.
  - `nombre_deplacements` : Nombre de déplacements.

**Valeurs retournées :**
- Un DataFrame Pandas représentant la matrice OD avec :
  - Les communes d'origine comme lignes.
  - Les communes de destination comme colonnes.

**Exemple d'utilisation :**
.. code-block:: python

   df_od_matrix = create_od_matrix(df_deplacements)

---

**get_od_count**
-----------------

**Description :**
Récupère le nombre de déplacements entre les zones d'origine et de destination à partir de la vue `vue_matrice_od_par_commune`.

**Paramètres d'entrée :**
- `noms_zones` (list, optionnel) : Liste des noms de zones ou communes d'origine à filtrer.

**Valeurs retournées :**
- Un DataFrame Pandas contenant :
  - `nom_origine` : Nom de la commune d'origine.
  - `nom_destination` : Nom de la commune de destination.
  - `nombre_deplacements` : Nombre total de déplacements.

**Exemple d'utilisation :**
.. code-block:: python

   df_od_count = get_od_count(['Antananarivo'])

---

**Remarques**
-------------
- Les fonctions utilisent SQLAlchemy pour interagir avec la base de données.
- Les noms des communes sont convertis en minuscules pour garantir la cohérence dans les requêtes.
- Assurez-vous que les vues utilisées (e.g., `vue_population_par_commune`, `vue_productions_attractions`, `vue_matrice_od_par_commune`) existent dans la base de données et contiennent les colonnes nécessaires.


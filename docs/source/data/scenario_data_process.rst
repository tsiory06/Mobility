=========================================
Documentation des Fonctions de Scénarios
=========================================

Ce module gère les interactions avec une base de données pour manipuler les scénarios de simulation, y compris leur insertion, récupération, et comparaison.

Contenu du module
------------------
- `fetch_scenarios_from_db`
- `insert_scenario_data`
- `get_all_scenarios`
- `fetch_two_most_recent_scenarios`

---

**fetch_scenarios_from_db**
---------------------------

**Description :**
Récupère tous les scénarios de la base de données à partir de la vue `vue_scenario`.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Un DataFrame Pandas contenant les colonnes :
  - `nom_scenario` : Nom du scénario.
  - `description_scenario` : Description du scénario.
  - `type_scenario` : Type de scénario (e.g., hypothèse, simulation).
  - `date_simulation` : Date de simulation.
  - Autres colonnes spécifiques à la vue.

**Exemple d'utilisation :**
.. code-block:: python

   df_scenarios = fetch_scenarios_from_db()

---

**insert_scenario_data**
-------------------------

**Description :**
Insère un nouveau scénario dans la base de données, en remplissant les tables `comparaison_scenario`, `scenario_detail_indicateur` et `scenario_detail_environement`.

**Paramètres d'entrée :**
- `nom` (str) : Nom du scénario.
- `description` (str) : Description du scénario.
- `type_scenario` (str) : Type de scénario (e.g., simulation ou hypothèse).
- `date_simulation` (datetime) : Date de la simulation.
- `debit_moyen` (float) : Débit moyen.
- `vitesse_moyenne` (float) : Vitesse moyenne (km/h).
- `temps_trajet_moyen` (float) : Temps de trajet moyen (minutes).
- `volume_carburant_simule` (float) : Volume de carburant simulé (litres).
- `longueur_trajet_moyenne` (float) : Longueur moyenne des trajets (km).
- `co2` (float) : Émissions de CO2 (g/km).
- `nox` (float) : Émissions de NOx (g/km).
- `co` (float) : Émissions de CO (g/km).

**Valeurs retournées :**
- Aucun. Insère les données dans les tables correspondantes.

**Exemple d'utilisation :**
.. code-block:: python

   insert_scenario_data(
       nom="Scénario A",
       description="Simulation de référence",
       type_scenario="Simulation",
       date_simulation=datetime.now(),
       debit_moyen=200.0,
       vitesse_moyenne=45.5,
       temps_trajet_moyen=15.0,
       volume_carburant_simule=1200.0,
       longueur_trajet_moyenne=12.0,
       co2=95.0,
       nox=40.0,
       co=10.0
   )

---

**get_all_scenarios**
----------------------

**Description :**
Récupère tous les scénarios existants dans la vue `vue_scenario`.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Un DataFrame Pandas contenant les colonnes de la vue `vue_scenario`.

**Exemple d'utilisation :**
.. code-block:: python

   df_all_scenarios = get_all_scenarios()

---

**fetch_two_most_recent_scenarios**
------------------------------------

**Description :**
Récupère les deux scénarios les plus récents, triés par la date de simulation décroissante.

**Paramètres d'entrée :**
- Aucun.

**Valeurs retournées :**
- Un DataFrame Pandas contenant les deux scénarios les plus récents.

**Exemple d'utilisation :**
.. code-block:: python

   df_recent_scenarios = fetch_two_most_recent_scenarios()

---

**Remarques**
-------------
- Les fonctions utilisent SQLAlchemy pour interagir avec la base de données.
- Les vues doivent exister dans la base de données et contenir les colonnes spécifiées.
- En cas d'erreur lors de l'insertion, la transaction est annulée.

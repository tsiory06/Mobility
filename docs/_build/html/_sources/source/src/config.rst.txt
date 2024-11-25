config module
=============

Ce module contient la configuration de la base de données utilisée dans le projet.

Configuration de la base de données
-----------------------------------

La variable `DATABASE_CONFIG` est un dictionnaire contenant les informations nécessaires pour se connecter à la base de données PostgreSQL. Ces informations incluent le nom de la base de données, l'utilisateur, le mot de passe, l'hôte, et le port.

**Détails des clés du dictionnaire :**

- `dbname`: Nom de la base de données utilisée.
- `user`: Nom d'utilisateur pour se connecter à la base de données.
- `password`: Mot de passe pour l'utilisateur.
- `host`: Adresse de l'hôte où la base de données est hébergée.
- `port`: Port utilisé pour accéder à la base de données.

**Exemple de configuration :**

```python
DATABASE_CONFIG = {
    'dbname': 'buss',
    'user': 'postgres',
    'password': 'pronokeys06',
    'host': 'localhost',
    'port': '5432',
}

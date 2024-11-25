
Installation de TanaMobility
============================

Ce guide vous permettra d'installer et de configurer le projet **TanaMobility** sur votre environnement local.

Prérequis
---------

- Python 3.12 installé sur votre machine.
- Accès à une base de données (PostgreSQL recommandé).
- Git pour cloner le dépôt.

Étapes d'installation
----------------------

1. **Télécharger le code source**

   Vous pouvez obtenir le code source via le lien GitHub suivant :

   - Téléchargez le code ZIP directement depuis [TanaMobility GitHub](https://github.com/tsii06/TanaMobility.git)
   - **OU** clonez le dépôt en exécutant la commande suivante :

     ```bash
     git clone https://github.com/tsii06/TanaMobility.git
     ```

2. **Créer et activer un environnement virtuel**

   Assurez-vous d'être dans le répertoire du projet cloné, puis exécutez les commandes suivantes :

   ```bash
   python -m venv env
   source env/bin/activate  # Sous Linux/Mac
   env\Scripts\activate  # Sous Windows
   ```

3. **Installer les dépendances**

   Installez les packages requis pour le projet en utilisant le fichier `requirement.txt` :

   ```bash
   pip install -r environnement/requirement.txt
   ```

4. **Configurer la base de données**

   - Accédez au répertoire `config` et configurez votre fichier de configuration de base de données.
   - Copiez le script SQL `buss.sql` dans votre gestionnaire de base de données PostgreSQL et exécutez-le pour créer les tables nécessaires :

     ```sql
     \i chemin/vers/buss.sql
     ```

5. **Insérer les données initiales**

   - Exécutez le script `insertionStatique.py` pour insérer les données initiales provenant des fichiers Excel et GeoJSON :

     ```bash
     python insertionStatique.py
     ```

   - Ensuite, exécutez le script `insertion.sql` dans votre base de données PostgreSQL pour compléter les données :

     ```sql
     \i chemin/vers/insertion.sql
     ```

6. **Lancer l'application**

   - **Pour un environnement local**, exécutez le fichier `app.py` :

     ```bash
     python app.py
     ```

   - **Pour un déploiement local (par exemple avec un serveur WSGI comme Gunicorn)**, utilisez `wsgi.py` :

     ```bash
     gunicorn -w 4 -b 127.0.0.1:8000 wsgi:app
     ```

Notes supplémentaires
---------------------

- Assurez-vous que votre base de données est opérationnelle et correctement configurée avant de lancer l'application.
- Consultez le fichier `README.md` du dépôt pour des instructions supplémentaires si nécessaire.
- Si vous rencontrez des problèmes, contactez le support ou ouvrez une issue sur le dépôt GitHub.

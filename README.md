## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Les variables de l'environnement sont à définir dans un fichier `oc-lettings-site/.env`.
Ces variables sont utilisées dans le fichier `oc-lettings-site/settings.py`. 

Un fichier `.env.example` est ici fourni.

### Applications et comptes nécessaires :

Au cours de l'utilisation de la pipeline, des comptes sont requis pour les applications suivantes:
- [Github](https://github.com/signup)
- [DockerHub](https://hub.docker.com/signup)
- [CircleCi](https://circleci.com/signup/)
- [Heroku](https://signup.heroku.com/)
- [Sentry](https://sentry.io/signup/)

### Fonctionnement de la Pipeline

La pipeline utilise CircleCI.
Il est configuré dans le fichier `.circleci/config.yml`

Deux types de commits sont considérés :
- 1- déploiement sur une autre branche que main (développement)
  - compilation, tests, linting
  

- 2- déploiement sur la branche `main` (production)
  - compilation, tests, linting
  - déploiement docker
  - déploiement heroku
  
Pour la branche main, chaque étape requiert que la précédente soit réussie.

---
## Applications :

---
### Github (Repository):

Le repository [BeanEden/P13_2](https://github.com/BeanEden/P13_2) est la base du versioning de l'application.

---

### Docker Hub (Conteneur):

Le [Docker-Hub](https://hub.docker.com/repository/docker/beaneden/oc-lettings) stocke en ligne l'image docker de l'application.  

La commande unique pour récupération de l'application en local et son démarrage immédiat est
Il est possible de démarrer l'application en local via la commande unique suivante :

`docker run --pull always -p 8000:8000 --name P13 beaneden/oc-lettings:lastest`

- `-p 8000:8000` défini l port utilisé
- `--name P13` est le nom donné au conteneur créé 
- `beaneden/oc-lettings` est le nom de l'image dans le repository en ligne 
- `:lastest` défini la version de l'image utilisée. Ici, la dernière. Il peut être remplacé par le hash du commit souhaité.

---
### CircleCi (Pipeline):

#### 1 - Mettez en place votre projet sur CircleCI

Liez votre git et lancez un nouveau projet avec le code de l'application.

#### 2 - Variables d'environnement
Il est nécessaire d'inclure au projet des variables d'environnement.

- Une fois sur la page de votre projet, cliquez sur `Project Settings`.
![alt text](C:\opc finis\P13_2\pwp p13\Prject_settings_location.png)
- Sélectionnez `Environment Variables`  
- Cliquez `Add Environment Variables`  

|   Nom des Variables  |   Description   |   Valeurs à renseigner   |
|---    |---   |---    |
|   DOCKERHUB_LOGIN   |   User Docker Hub   |   `beaneden`   |
|   DOCKERHUB_PASSWORD   |   Token Dockerhub ou Mdp   |   `1321654654654651231654`   |
|   HEROKU_API_KEY |  API Token Heroku  |   `1321654654654651231654`   |
|   HEROKU_APP_NAME | nom de l'application | oc-lettings-124 |

---

## Heroku (Hébergement):
[L'application](https://oc-lettings-124.herokuapp.com/) est hébergée sur Heroku.
![alt text](C:\opc finis\P13_2\pwp p13\heroku.png)

En cas de suppression:
  - créer l'application 'oc-lettings-124' :`heroku create oc-lettings-124`
  - trigger la pipeline de la branche `main` sur circleci.
  - si la base de donnée sqlite n'est pas correctement lue : `heroku addons:remove heroku-postgresql`

L'application gère Heroku de la manière suivante :
- Django : via `django_on_heroku` 
- CircleCi : via [l'orb Heroku](https://circleci.com/developer/orbs/orb/circleci/heroku)

---

## Sentry (Monitoring):

[Le monitoring de l'application](https://sentry.io/organizations/bean-7m/projects/oc-lettings/?project=4504122861486080) est géré par Sentry.
![alt text](C:\opc finis\P13_2\pwp p13\sentry 2.png)

Elle permet également de détecter des éventuels bug/issues.
![alt text](C:\opc finis\P13_2\pwp p13\sentry issues.png)

La variable `SENTRY_DSN` est requise pour l'utilisation de Sentry.
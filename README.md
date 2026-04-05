# SoftDesk Support - API REST

API REST pour le suivi de problèmes techniques dans des projets logiciels.

## 📋 Description

SoftDesk Support est une application B2B permettant aux équipes de :
- Créer et gérer des projets (backend, frontend, iOS, Android)
- Suivre des issues (bugs, fonctionnalités, tâches) avec priorités et statuts
- Ajouter des contributeurs aux projets
- Commenter les issues pour faciliter la communication

## 🛠️ Technologies utilisées

- Python 3.14.0
- Django 6.0.3 
- Django REST Framework 3.16.1
- Poetry 2.3.2

## 📦 Installation

### Prérequis

Avant de commencer, vous devez avoir installé :
- **Python 3.14** : [python.org/downloads](https://www.python.org/downloads/)
- **Poetry 2.3.2** : Gestionnaire de dépendances Python


### Installation du projet

**1. Cloner le repository**
```bash
git clone https://github.com/myriamdesporte/Softdesk-support.git
cd Softdesk-support
```

**2. Installer les dépendances**
```bash
poetry install
```

**3. Créer la base de données**
```bash
poetry run python manage.py migrate
```

**4. Créer un utilisateur administrateur**
```bash
poetry run python manage.py createsuperuser
```

Suivez les instructions (username, email, password).

**5. Lancer le serveur de développement**
```bash
poetry run python manage.py runserver
```

Le serveur est maintenant accessible sur : **http://127.0.0.1:8000/**

L'interface d'administration est accessible sur : **http://127.0.0.1:8000/admin/**


## 📡 Endpoints API disponibles

### Utilisateurs

| Méthode     | Endpoint           | Description |
|-------------|--------------------|-------------|
| GET         | `/api/users/`      | Lister tous les utilisateurs |
| POST        | `/api/users/`      | Créer un utilisateur |
| GET         | `/api/users/{id}/` | Détails d'un utilisateur |
| PUT / PATCH | `/api/users/{id}/` | Modifier un utilisateur |
| DELETE      | `/api/users/{id}/` | Supprimer un utilisateur |

### Projets

| Méthode     | Endpoint | Description |
|-------------|----------|-------------|
| GET         | `/api/projects/` | Lister tous les projets |
| POST        | `/api/projects/` | Créer un projet |
| GET         | `/api/projects/{id}/` | Détails d'un projet |
| PUT / PATCH | `/api/projects/{id}/` | Modifier un projet |
| DELETE      | `/api/projects/{id}/` | Supprimer un projet |

### Contributeurs

| Méthode   | Endpoint | Description                        |
|-----------|----------|------------------------------------|
| GET       | `/api/projects/{project_id}/contributors/` | Lister les contributeurs d'un projet |
| POST      | `/api/projects/{project_id}/contributors/` | Ajouter un contributeur à un projet |
| GET       | `/api/projects/{project_id}/contributors/{id}/` | Détails d'un contributeur          |
| DELETE    | `/api/projects/{project_id}/contributors/{id}/` | Retirer un contributeur d'un projet |

### Issues

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/projects/{project_id}/issues/` | Lister les issues d'un projet |
| POST | `/api/projects/{project_id}/issues/` | Créer une issue dans un projet |
| GET | `/api/projects/{project_id}/issues/{id}/` | Détails d'une issue |
| PUT | `/api/projects/{project_id}/issues/{id}/` | Modifier une issue |
| DELETE | `/api/projects/{project_id}/issues/{id}/` | Supprimer une issue |

### Commentaires

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/projects/{project_id}/issues/{issue_id}/comments/` | Lister les commentaires d'une issue |
| POST | `/api/projects/{project_id}/issues/{issue_id}/comments/` | Créer un commentaire sur une issue |
| GET | `/api/projects/{project_id}/issues/{issue_id}/comments/{id}/` | Détails d'un commentaire |
| PUT | `/api/projects/{project_id}/issues/{issue_id}/comments/{id}/` | Modifier un commentaire |
| DELETE | `/api/projects/{project_id}/issues/{issue_id}/comments/{id}/` | Supprimer un commentaire |


### Exemple de requête (création d'utilisateur)
```
POST http://127.0.0.1:8000/api/users/

{
    "username": "alice",
    "email": "alice@example.com",
    "password": "SecurePass123!",
    "password2": "SecurePass123!",
    "date_of_birth": "2000-05-15",
    "can_be_contacted": true,
    "can_data_be_shared": false
}
```
# Habit Tracker API - Backend

Ce projet est une API de suivi d'habitudes construite avec Django et Django REST Framework. Il permet la gestion des utilisateurs, des tâches quotidiennes, des objectifs et des notifications automatisées.

## Table des Matières

1. [Habit Tracker API - Backend](#habit-tracker-api---backend)
   - [Installation et Configuration](#installation-et-configuration)
     - [1. Environnement virtuel](#1-environnement-virtuel)
     - [2. Installation des dépendances](#2-installation-des-dependances)
     - [3. Base de données et Serveur](#3-base-de-donnees-et-serveur)
   - [Utilisation et Tests](#utilisation-et-tests)
     - [Authentification par Session](#authentification-par-session)
     - [Points d'entrée principaux](#points-dentree-principaux)
   - [Travaux restants et Améliorations](#travaux-restants-et-ameliorations)
   - [Architecture](#architecture)

## Installation et Configuration

### 1. Environnement virtuel

Exécutez les commandes suivantes dans le répertoire racine :

```bash
python -m venv venv
# Activation (Windows)
venv\Scripts\activate
# Activation (macOS/Linux)
source venv/bin/activate

```

### 2. Installation des dépendances

```bash
pip -r requirements.txt
```

### 3. Base de données et Serveur

```bash
python manage.py migrate
python manage.py runserver

```

L'API est accessible à l'adresse : `http://127.0.0.1:8000/api/`

---

## Utilisation et Tests

### Authentification par Session

1. **Inscription** : POST vers `/api/auth/register/` (données : username, email, password).
2. **Connexion** : POST vers `/api/auth/login/`. Le navigateur gère ensuite le cookie `sessionid`.
3. **Sécurité** : Les requêtes de modification requièrent le header `X-CSRFToken`.

### Points d'entrée principaux

- **Tâches** : `/api/habits/tasks/`
- **Journal** : `/api/habits/journals/`
- **Objectifs** : `/api/goals/`
- **Notifications** : `/api/notifications/`

---

## Travaux restants et Améliorations

- **Administration** : Création d'un compte **super-utilisateur** pour la gestion via l'interface `/admin`.
- **Système Cron** : Mise en place de **notifications** planifiées pour les rappels de fin de journée.
- **Dépendances de données** : Liaison hiérarchique entre les tâches (Tasks) et les objectifs globaux (Goals).
- **Logique du Journal** : Approfondissement du système de notes avec suivi de l'état émotionnel.
- **Analytique** : Développement de l'endpoint `/api/analytics/` pour le calcul des taux de complétion.
- **Recherche et Filtrage**
- **Documentation Swagger**

---

### Architecture

- `apps.users` : Authentification et profils.
- `apps.habits` : Tâches et entrées de journal.
- `apps.goals` : Objectifs à long terme.
- `apps.notifications` : Système d'alertes via Django Signals.

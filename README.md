# Habit Tracker API - Backend

Ce projet est une API de suivi d'habitudes construite avec Django et Django REST Framework. Il permet la gestion des utilisateurs, des tâches quotidiennes, des objectifs et des notifications automatisées.

## Table des Matières

1. [Habit Tracker API - Backend](#habit-tracker-api---backend)
   - [Installation et Configuration](#installation-et-configuration)
     - [1. Environnement virtuel](#1-environnement-virtuel)
     - [2. Installation des dépendances](#2-installation-des-dépendances)
     - [3. Base de données et Serveur](#3-base-de-données-et-serveur)
   - [Système d'Authentification](#système-dauthentification)
   - [Logique Métier et Fonctionnalités](#logique-métier-et-fonctionnalités)
   - [Points d'entrée de l'API](#points-dentrée-de-lapi)
   - [Travaux restants et Améliorations](#travaux-restants-et-améliorations)
     - [Architecture du Projet](#architecture-du-projet)

---

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
pip install -r requirements.txt

```

### 3. Base de données et Serveur

```bash
python manage.py migrate
python manage.py runserver

```

L'API est accessible à l'adresse : `http://127.0.0.1:8000/api/`

---

## Système d'Authentification

L'application propose deux méthodes de connexion sécurisées basées sur le système de **Session Django** :

1. **Authentification Native** : Inscription et connexion classique via les endpoints `/api/auth/`.
2. **Authentification Google (OAuth2)** : Intégration de `django-allauth` permettant aux utilisateurs de se connecter ou de s'inscrire en un clic via leur compte Google. Cette méthode crée automatiquement un profil utilisateur en base de données.

---

## Logique Métier et Fonctionnalités

### 1. Relation Hiérarchique Objectifs / Tâches

Contrairement à une simple liste, l'application lie techniquement les tâches aux objectifs :

- **Structure** : Un Objectif (Goal) peut contenir plusieurs Tâches (Tasks).
- **Automation** : Lorsqu'une tâche est marquée comme terminée, le système vérifie automatiquement l'état des autres tâches liées. Si 100% des tâches d'un objectif sont finies, l'Objectif est automatiquement marqué comme complété.

### 2. Système de Notifications Événementiel

L'application utilise les **Django Signals** pour générer des notifications sans intervention manuelle :

- **À la création** : Une notification est créée dès qu'un nouvel objectif est défini.
- **À la réussite** : Dès qu'un objectif est atteint (automatiquement ou manuellement), une notification de félicitations est générée pour l'utilisateur.

### 3. Module d'Analytique Dynamique

L'endpoint `/api/analytics/` compile les données en temps réel pour offrir une vue d'ensemble :

- **Calculs** : Taux de complétion global des tâches.
- **Traçabilité** : Retourne non seulement les compteurs, mais aussi les listes d'IDs des tâches et objectifs "En cours" vs "Terminés", permettant un suivi précis.

### 4. Journal de Bord

Un espace dédié aux notes quotidiennes permettant à l'utilisateur de consigner ses réflexions sur sa progression.

---

## Points d'entrée de l'API

| Endpoint                  | Méthode   | Description                                             |
| ------------------------- | --------- | ------------------------------------------------------- |
| `/api/auth/login/`        | POST      | Connexion session classique                             |
| `/accounts/google/login/` | GET       | Connexion via Google OAuth2                             |
| `/api/habits/tasks/`      | GET/POST  | Gestion des tâches (liées ou non à un objectif)         |
| `/api/goals/`             | GET/POST  | Gestion des objectifs (inclut les IDs des tâches liées) |
| `/api/analytics/`         | GET       | Statistiques globales et listes d'IDs de suivi          |
| `/api/notifications/`     | GET/PATCH | Consultation et marquage des alertes                    |
| `/api/habits/journals/`   | GET/POST  | Gestion des notes de réflexion                          |

---

## Architecture du Projet

- **`apps.users`** : Gestion des comptes, de la sécurité et de l'intégration sociale.
- **`apps.habits`** : Gestion des tâches (Tasks) et du journal quotidien.
- **`apps.goals`** : Gestion des objectifs et logique de complétion automatique.
- **`apps.notifications`** : Moteur d'alertes basé sur les signaux de la base de données.

---

## Travaux restants et Améliorations

- **Documentation Swagger/OpenAPI** : Génération d'une interface interactive pour tester l'API.
- **Système de Rappels (Cron)** : Envoi automatique de notifications de rappel pour les tâches non remplies en fin de journée.
- **Filtres Avancés** : Recherche par date et filtrage par statut sur les listes de tâches.
- **Évolution du Journal** : Ajout d'un système de suivi de l'humeur (Mood Tracking) pour enrichir les analyses.
- **Interface d'Administration** : Finalisation de la personnalisation du dashboard `/admin` pour le support client.

---

**Souhaitez-vous que je vous aide à implémenter l'une de ces améliorations, comme la documentation Swagger, pour rendre le projet encore plus "clés en main" pour votre client ?**

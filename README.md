## Deep Cleaning Operations Pipeline :

Projet inspiré de mon expérience terrain dans le nettoyage industriel, notamment sur des opérations de remise en état complètes (zones froides, laboratoires, entrepôts…).

L’objectif est de simuler un pipeline data réaliste permettant de suivre, analyser et prioriser des missions de nettoyage critiques.

## Objectif :

Construire une pipeline de données de bout en bout :

- génération de missions de nettoyage réalistes
- transformation et enrichissement des données
- chargement dans PostgreSQL
- orchestration avec Airflow
- visualisation (Streamlit / futur dashboard)

️## Architecture :

Raw Data → Transform → PostgreSQL → Dashboard
            ↑
         Airflow

## Stack :

- Python (Pandas, SQLAlchemy)
- PostgreSQL
- Apache Airflow
- Docker / Docker Compose
- Streamlit (dashboard)
- Faker (simulation de données)
  
## Pipeline :

1. Génération

Création de missions réalistes :

type d’intervention (dégivrage, désinfection…)
niveau de risque
contraintes (température, surface…)
score de priorité

2. Transformation

Nettoyage et enrichissement :

calcul du risk_score
normalisation des données
préparation pour analyse

3. Load

Chargement dans PostgreSQL :

table deep_cleaning_missions
reset automatique à chaque run

4. Orchestration

DAG Airflow :

generate_missions
transform_missions
load_to_postgres

## Lancer le projet :

docker compose up -d --build

## Airflow :

http://localhost:8080

## Identifiants :

admin / admin

## Cas métier simulés :

- nettoyage complet de chambres froides après période de forte activité
- zones à risque (alimentaire, chimie…)
- gestion des équipes et du temps
- priorisation des interventions critiques

## Auteur : 

Philippe Kirstetter-Fender
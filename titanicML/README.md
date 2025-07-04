# Titanic Machine Learning Project

## Description
Ce projet est dédié à l'analyse et à la modélisation des données du challenge Titanic sur Kaggle. L'objectif est de prédire la survie des passagers en fonction de diverses caractéristiques.

## Structure du projet
- **Data/** : Contient les fichiers de données nécessaires pour l'analyse et la modélisation.
  - `train.csv` : Données d'entraînement avec les caractéristiques des passagers et les informations sur leur survie.
  - `test.csv` : Données de test pour générer des prédictions.
  - `gender_submission.csv` : Exemple de soumission montrant le format attendu pour les prédictions.

- **notebooks/** : Contient des notebooks Jupyter pour différentes étapes du projet.
  - `titanic_setup.ipynb` : Configuration de l'environnement de travail et vérification des données.
  - `exploratory_analysis.ipynb` : Analyse exploratoire des données.
  - `preprocessing.ipynb` : Prétraitement des données, gestion des valeurs manquantes et encodage des variables.
  - `modeling.ipynb` : Modélisation avec différents algorithmes de classification.

- **src/** : Contient le code source réutilisable pour le projet.
  - `preprocessing/` : Fonctions pour le prétraitement des données.
    - `feature_engineering.py` : Création de nouvelles caractéristiques.
    - `missing_data.py` : Gestion des valeurs manquantes.
  - `models/` : Fonctions pour entraîner et évaluer les modèles.
    - `train.py` : Entraînement des modèles.
    - `evaluation.py` : Évaluation des performances des modèles.
  - `utils/` : Fonctions utilitaires pour la visualisation et d'autres tâches.
    - `visualization.py` : Visualisation des données et résultats.

- **models/** : Contient des informations sur les modèles utilisés dans le projet.

- **submissions/** : Contient des informations sur le format et le contenu des fichiers de soumission.

- **kaggle.json** : Fichier d'authentification pour l'API Kaggle.

## Instructions
1. **Installation des dépendances** : Assurez-vous d'avoir installé toutes les bibliothèques nécessaires pour l'analyse de données et le machine learning.
2. **Configuration de l'API Kaggle** : Placez votre fichier `kaggle.json` à la racine du projet pour accéder aux données.
3. **Exécution des notebooks** : Ouvrez les notebooks dans le dossier `notebooks` pour commencer l'analyse, le prétraitement et la modélisation des données.

## Prochaines étapes
- Effectuer une analyse exploratoire approfondie des données.
- Prétraiter les données pour préparer les ensembles d'entraînement et de test.
- Tester différents modèles de machine learning et évaluer leurs performances.
- Générer des prédictions et soumettre les résultats sur Kaggle.
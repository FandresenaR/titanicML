# Titanic - Machine Learning from Disaster

## À propos du Challenge

Le naufrage du Titanic est l'un des naufrages les plus célèbres de l'histoire.

Le 15 avril 1912, lors de son voyage inaugural, le RMS Titanic, largement considéré comme "insubmersible", a coulé après être entré en collision avec un iceberg. Malheureusement, il n'y avait pas assez de canots de sauvetage pour tout le monde à bord, ce qui a entraîné la mort de 1502 des 2224 passagers et membres d'équipage.

Bien que la chance ait joué un rôle dans la survie, il semble que certains groupes de personnes avaient plus de chances de survivre que d'autres.

## Objectif du Challenge

Dans ce challenge, nous devons construire un modèle prédictif qui répond à la question : "Quels types de personnes avaient plus de chances de survivre ?" en utilisant les données des passagers (nom, âge, sexe, classe socio-économique, etc.).

## Données Utilisées dans la Compétition

Dans cette compétition, nous avons accès à deux ensembles de données similaires qui incluent des informations sur les passagers :

1. **train.csv** : contient les détails d'un sous-ensemble des passagers à bord (891 exactement) et, plus important encore, révèle s'ils ont survécu ou non, également connu sous le nom de "vérité terrain".
2. **test.csv** : contient des informations similaires mais ne divulgue pas si les 418 autres passagers ont survécu.

Notre tâche est de prédire ces résultats en utilisant les modèles que nous développons à partir des données d'entraînement.

## Structure du Projet

Le projet est organisé comme suit:

```
titanicML/
│
├── Data/                       # Données brutes et prétraitées
│   ├── train.csv              # Ensemble d'entraînement
│   ├── test.csv               # Ensemble de test
│   ├── gender_submission.csv  # Exemple de soumission
│   └── preprocessed/          # Données après prétraitement
│
├── models/                     # Modèles entraînés sauvegardés
│
├── notebooks/                  # Notebooks Jupyter pour l'analyse et la modélisation
│   ├── 1_analyse_exploratoire.ipynb     # Analyse exploratoire des données
│   ├── 2_pretraitement_donnees.ipynb    # Prétraitement des données
│   ├── 3_modelisation.ipynb             # Modélisation et optimisation
│   ├── 4_evaluation_modeles.ipynb       # Évaluation approfondie des modèles
│   └── 5_soumission_kaggle.ipynb        # Génération des prédictions et soumission
│
├── src/                        # Code source Python modulaire
│
├── submissions/                # Fichiers de soumission pour Kaggle
│
├── titanic_setup.ipynb         # Notebook de configuration initiale
├── kaggle.json                 # Configuration de l'API Kaggle
└── README.md                   # Ce fichier
```

## Notre Approche

Nous avons adopté une démarche structurée pour résoudre ce challenge:

1. **Analyse exploratoire des données**: Comprendre les relations entre les variables et la survie
2. **Prétraitement des données**: Gérer les valeurs manquantes, créer de nouvelles caractéristiques, encoder les variables catégorielles
3. **Modélisation**: Tester différents algorithmes de classification (Random Forest, XGBoost, etc.)
4. **Évaluation**: Mesurer les performances des modèles
5. **Soumission**: Générer des prédictions pour les données de test et les soumettre à Kaggle

## Instructions d'Utilisation

### Prérequis

Pour exécuter ce projet, vous aurez besoin des bibliothèques Python suivantes:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- xgboost
- kaggle

Vous pouvez installer ces bibliothèques avec la commande:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn xgboost kaggle
```

### Configuration initiale

1. Exécutez d'abord le notebook `titanic_setup.ipynb` pour configurer l'environnement et vérifier l'accès aux données.
2. Assurez-vous que votre fichier `kaggle.json` est correctement placé pour permettre l'interaction avec l'API Kaggle.

### Exécution des notebooks

Les notebooks doivent être exécutés dans l'ordre suivant pour reproduire l'ensemble du processus:

1. **`notebooks/1_analyse_exploratoire.ipynb`** - Exploration approfondie des données
2. **`notebooks/2_pretraitement_donnees.ipynb`** - Transformation des données brutes
3. **`notebooks/3_modelisation.ipynb`** - Test et optimisation des algorithmes de classification
4. **`notebooks/4_evaluation_modeles.ipynb`** - Analyse détaillée des performances des modèles
5. **`notebooks/5_soumission_kaggle.ipynb`** - Génération des prédictions et soumission à Kaggle

### Soumission à Kaggle

Vous pouvez soumettre vos prédictions à Kaggle de deux façons:

1. **Via l'API Kaggle** (automatisé dans le notebook de soumission)
   - Assurez-vous que votre fichier `kaggle.json` est correctement configuré
   - Exécutez le notebook `5_soumission_kaggle.ipynb` jusqu'à la fin

2. **Manuellement**
   - Téléchargez le fichier `submissions/submission_final.csv` généré
   - Visitez la page de soumission du challenge Titanic sur Kaggle
   - Importez votre fichier de soumission

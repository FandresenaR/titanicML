#!/bin/bash

# Script de configuration complet pour le challenge Titanic ML

echo "===== Configuration du projet Titanic ML ====="

# 1. Installation des dépendances Python
echo -e "\n[1/4] Installation des bibliothèques Python nécessaires..."
pip install -r requirements.txt

# 2. Configuration de Kaggle API
echo -e "\n[2/4] Configuration de l'API Kaggle..."
mkdir -p ~/.kaggle
chmod 700 ~/.kaggle

# Vérifier si le fichier kaggle.json existe à la racine du projet
if [ -f "./kaggle.json" ]; then
    cp ./kaggle.json ~/.kaggle/kaggle.json
    chmod 600 ~/.kaggle/kaggle.json
    echo "Fichier kaggle.json copié dans ~/.kaggle/"
else
    echo "Fichier kaggle.json non trouvé à la racine du projet."
    echo "Pour utiliser l'API Kaggle, veuillez télécharger votre fichier kaggle.json depuis votre compte Kaggle"
    echo "et le placer à la racine du projet."
fi

# 3. Téléchargement des données si nécessaires
echo -e "\n[3/4] Vérification/téléchargement des données..."
mkdir -p Data

if [ -f "~/.kaggle/kaggle.json" ] && [ ! -f "./Data/train.csv" -o ! -f "./Data/test.csv" ]; then
    echo "Téléchargement des données depuis Kaggle..."
    kaggle competitions download -c titanic -p ./Data
    unzip -o "./Data/titanic.zip" -d ./Data
    echo "Données téléchargées avec succès!"
else
    echo "Vérification des données existantes..."
    if [ -f "./Data/train.csv" ] && [ -f "./Data/test.csv" ]; then
        echo "Les fichiers de données existent déjà."
    else
        echo "ATTENTION: Certains fichiers de données sont manquants."
    fi
fi

# 4. Création de la structure du projet
echo -e "\n[4/4] Création de la structure du projet..."
mkdir -p notebooks models submissions src

echo -e "\n===== Configuration terminée ! ====="
echo "Vous pouvez maintenant travailler sur le challenge Titanic ML."
echo "Pour commencer, ouvrez le notebook titanic_setup.ipynb"

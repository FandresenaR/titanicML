#!/bin/bash

# Script d'installation des dépendances pour le projet Titanic ML

echo "Installation des dépendances Python..."
pip install -r requirements.txt

echo "Configuration du répertoire .kaggle pour l'API Kaggle..."
mkdir -p ~/.kaggle
chmod 700 ~/.kaggle

echo "Rappel : Pour utiliser l'API Kaggle, placez votre fichier kaggle.json dans ~/.kaggle/"
echo "Vous pouvez le télécharger depuis votre compte Kaggle (Mon compte > API > Créer un nouveau jeton d'API)"

echo "Création des dossiers du projet si nécessaire..."
mkdir -p notebooks models submissions src

echo "Configuration terminée ! Vous êtes prêt à relever le challenge Titanic."

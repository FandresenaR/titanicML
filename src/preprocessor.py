"""
Module contenant des fonctions de prétraitement pour les données du Titanic.
"""
import pandas as pd
import numpy as np
import re
from sklearn.base import BaseEstimator, TransformerMixin

def extract_title(name):
    """Extrait le titre d'un nom complet."""
    title_search = re.search(' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ''

def create_family_size(df):
    """Crée une colonne FamilySize et IsAlone."""
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = 0
    df.loc[df['FamilySize'] == 1, 'IsAlone'] = 1
    return df

def fill_missing_ages(df):
    """Remplit les âges manquants en se basant sur le titre, la classe et le sexe."""
    age_avg = df['Age'].mean()
    age_std = df['Age'].std()
    
    # Créer des groupes par titre, Pclass et Sex
    age_null_count = df['Age'].isnull().sum()
    
    # Conditions pour les âges manquants
    age_null_random_list = np.random.randint(age_avg - age_std, age_avg + age_std, size=age_null_count)
    df.loc[df['Age'].isnull(), 'Age'] = age_null_random_list
    df['Age'] = df['Age'].astype(int)
    
    return df

def process_cabin(df):
    """Traite la colonne Cabin pour en extraire des informations utiles."""
    df['CabinLetter'] = df['Cabin'].str.slice(0, 1)
    df['CabinLetter'].fillna('U', inplace=True)  # U pour Unknown
    return df

def create_age_categories(df):
    """Crée des catégories d'âge."""
    df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 35, 60, 100], 
                            labels=['Child', 'Teenager', 'Young Adult', 'Adult', 'Senior'])
    return df

def create_fare_categories(df):
    """Crée des catégories de tarifs."""
    df['FareGroup'] = pd.qcut(df['Fare'], 4, labels=['Low', 'Medium', 'High', 'Very High'])
    return df

class TitanicPreprocessor(BaseEstimator, TransformerMixin):
    """
    Classe pour prétraiter les données du Titanic.
    Peut être utilisée dans un pipeline sklearn.
    """
    
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        data = X.copy()
        
        # Extraire les titres des noms
        data['Title'] = data['Name'].apply(extract_title)
        
        # Regrouper les titres rares
        title_mapping = {
            "Mr": "Mr",
            "Miss": "Miss",
            "Mrs": "Mrs",
            "Master": "Master",
            "Dr": "Officer",
            "Rev": "Officer",
            "Col": "Officer",
            "Major": "Officer",
            "Mlle": "Miss",
            "Mme": "Mrs",
            "Don": "Royalty",
            "Lady": "Royalty",
            "Sir": "Royalty",
            "Countess": "Royalty",
            "Jonkheer": "Royalty",
            "Dona": "Royalty",
            "Capt": "Officer"
        }
        
        data['Title'] = data['Title'].map(title_mapping)
        data['Title'].fillna('Other', inplace=True)
        
        # Créer la taille de la famille
        data = create_family_size(data)
        
        # Remplir les âges manquants
        data = fill_missing_ages(data)
        
        # Créer des catégories d'âge
        data = create_age_categories(data)
        
        # Traiter la cabine
        data = process_cabin(data)
        
        # Remplir les valeurs manquantes de Embarked
        data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
        
        # Remplir les valeurs manquantes de Fare
        data['Fare'].fillna(data['Fare'].median(), inplace=True)
        
        # Créer des catégories de tarifs
        data = create_fare_categories(data)
        
        # Supprimer les colonnes inutiles pour la modélisation
        columns_to_drop = ['Name', 'Ticket', 'Cabin', 'PassengerId']
        data.drop(columns_to_drop, axis=1, inplace=True, errors='ignore')
        
        return data

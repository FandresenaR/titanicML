"""
Module contenant des classes et fonctions pour l'entraînement et l'évaluation des modèles.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

def evaluate_model(model, X_train, X_val, y_train, y_val):
    """
    Évalue un modèle sur les données d'entraînement et de validation.
    
    Args:
        model: Modèle sklearn ou compatible
        X_train: Caractéristiques d'entraînement
        X_val: Caractéristiques de validation
        y_train: Cibles d'entraînement
        y_val: Cibles de validation
        
    Returns:
        dict: Dictionnaire contenant les métriques d'évaluation
    """
    model.fit(X_train, y_train)
    y_train_pred = model.predict(X_train)
    y_val_pred = model.predict(X_val)
    
    train_acc = accuracy_score(y_train, y_train_pred)
    val_acc = accuracy_score(y_val, y_val_pred)
    
    try:
        y_train_proba = model.predict_proba(X_train)[:, 1]
        y_val_proba = model.predict_proba(X_val)[:, 1]
        train_auc = roc_auc_score(y_train, y_train_proba)
        val_auc = roc_auc_score(y_val, y_val_proba)
    except:
        train_auc = 0
        val_auc = 0
    
    results = {
        'train_accuracy': train_acc,
        'val_accuracy': val_acc,
        'train_auc': train_auc,
        'val_auc': val_auc,
        'confusion_matrix': confusion_matrix(y_val, y_val_pred),
        'classification_report': classification_report(y_val, y_val_pred)
    }
    
    return results

def get_feature_importance(model, feature_names):
    """
    Extrait les importances des caractéristiques d'un modèle.
    
    Args:
        model: Modèle entraîné avec feature_importance_
        feature_names: Noms des caractéristiques
        
    Returns:
        pd.DataFrame: DataFrame avec les importances triées
    """
    if hasattr(model, 'feature_importances_'):
        importance = model.feature_importances_
    elif hasattr(model, 'coef_'):
        importance = np.abs(model.coef_[0])
    else:
        return pd.DataFrame()
    
    feature_importance = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importance
    })
    
    return feature_importance.sort_values('Importance', ascending=False)

def get_best_models():
    """
    Retourne un dictionnaire des meilleurs modèles à tester.
    
    Returns:
        dict: Dictionnaire de modèles
    """
    models = {
        'logistic': LogisticRegression(max_iter=1000, random_state=42),
        'random_forest': RandomForestClassifier(random_state=42),
        'gradient_boosting': GradientBoostingClassifier(random_state=42),
        'xgboost': xgb.XGBClassifier(random_state=42)
    }
    
    return models

def get_model_params():
    """
    Retourne un dictionnaire de paramètres pour la recherche par grille.
    
    Returns:
        dict: Dictionnaire de paramètres pour chaque modèle
    """
    params = {
        'logistic': {
            'C': [0.01, 0.1, 1, 10, 100],
            'penalty': ['l1', 'l2'],
            'solver': ['liblinear', 'saga']
        },
        'random_forest': {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 5, 10, 15],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        },
        'gradient_boosting': {
            'n_estimators': [100, 200, 300],
            'learning_rate': [0.01, 0.1, 0.2],
            'max_depth': [3, 5, 7]
        },
        'xgboost': {
            'n_estimators': [100, 200, 300],
            'learning_rate': [0.01, 0.1, 0.2],
            'max_depth': [3, 5, 7],
            'colsample_bytree': [0.7, 0.8, 0.9]
        }
    }
    
    return params

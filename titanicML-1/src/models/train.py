import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Exemple de prétraitement: suppression des colonnes inutiles et gestion des valeurs manquantes
    data = data.drop(columns=['Name', 'Ticket', 'Cabin'], errors='ignore')
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
    data['Age'].fillna(data['Age'].median(), inplace=True)
    data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)
    return data

def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def save_model(model, filename):
    joblib.dump(model, filename)

def main():
    # Chargement des données
    train_data = load_data('/workspaces/titanicML/Data/train.csv')
    
    # Prétraitement des données
    processed_data = preprocess_data(train_data)
    
    # Séparation des caractéristiques et de la cible
    X = processed_data.drop(columns=['Survived'])
    y = processed_data['Survived']
    
    # Division des données en ensembles d'entraînement et de validation
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entraînement du modèle
    model = train_model(X_train, y_train)
    
    # Évaluation du modèle
    val_predictions = model.predict(X_val)
    accuracy = accuracy_score(y_val, val_predictions)
    print(f'Accuracy: {accuracy:.2f}')
    
    # Sauvegarde du modèle
    save_model(model, '/workspaces/titanicML/src/models/titanic_model.pkl')

if __name__ == "__main__":
    main()
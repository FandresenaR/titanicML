def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

    # Prédictions sur les données de test
    y_pred = model.predict(X_test)

    # Calcul des métriques
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Affichage des résultats
    print("Évaluation du modèle:")
    print(f"Précision: {accuracy:.4f}")
    print(f"Précision: {precision:.4f}")
    print(f"Rappel: {recall:.4f}")
    print(f"Score F1: {f1:.4f}")
    print("Matrice de confusion:")
    print(conf_matrix)

    return accuracy, precision, recall, f1, conf_matrix

def plot_confusion_matrix(cm, classes):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=classes, yticklabels=classes)
    plt.ylabel('Vérité terrain')
    plt.xlabel('Prédictions')
    plt.title('Matrice de confusion')
    plt.show()
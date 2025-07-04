import matplotlib.pyplot as plt
import seaborn as sns

def plot_survival_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Survived', data=data, palette='viridis')
    plt.title('Distribution des survivants')
    plt.xlabel('Survécu (0 = Non, 1 = Oui)')
    plt.ylabel('Nombre de passagers')
    plt.xticks(ticks=[0, 1], labels=['Non', 'Oui'])
    plt.show()

def plot_age_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Age'].dropna(), bins=30, kde=True, color='blue')
    plt.title('Distribution des âges des passagers')
    plt.xlabel('Âge')
    plt.ylabel('Nombre de passagers')
    plt.show()

def plot_class_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Pclass', data=data, palette='viridis')
    plt.title('Distribution des classes des passagers')
    plt.xlabel('Classe')
    plt.ylabel('Nombre de passagers')
    plt.show()

def plot_survival_by_class(data):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Pclass', y='Survived', data=data, palette='viridis')
    plt.title('Taux de survie par classe')
    plt.xlabel('Classe')
    plt.ylabel('Taux de survie')
    plt.show()
def create_feature_engineering_features(df):
    # Exemple de création d'une nouvelle caractéristique : le titre des passagers
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    
    # Regrouper les titres peu fréquents
    df['Title'] = df['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer'], 'Rare')
    df['Title'] = df['Title'].replace('Mlle', 'Miss')
    df['Title'] = df['Title'].replace('Ms', 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')
    
    # Exemple de création d'une caractéristique binaire : est-ce un enfant ?
    df['Is_Child'] = df['Age'].apply(lambda x: 1 if x < 18 else 0)
    
    # Exemple de création d'une caractéristique : taille de la famille
    df['Family_Size'] = df['SibSp'] + df['Parch'] + 1
    
    return df
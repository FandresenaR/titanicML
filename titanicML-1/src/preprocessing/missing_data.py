def handle_missing_values(df):
    """
    Gère les valeurs manquantes dans le DataFrame donné.

    Args:
        df (pd.DataFrame): Le DataFrame à traiter.

    Returns:
        pd.DataFrame: Le DataFrame avec les valeurs manquantes gérées.
    """
    # Exemple de gestion des valeurs manquantes
    # Remplacer les valeurs manquantes par la moyenne pour les colonnes numériques
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].mean(), inplace=True)

    # Remplacer les valeurs manquantes par la valeur la plus fréquente pour les colonnes catégorielles
    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)

    return df

def check_missing_values(df):
    """
    Vérifie les valeurs manquantes dans le DataFrame donné.

    Args:
        df (pd.DataFrame): Le DataFrame à vérifier.

    Returns:
        pd.DataFrame: Un DataFrame contenant le nombre et le pourcentage de valeurs manquantes par colonne.
    """
    missing_values = df.isnull().sum()
    missing_percent = (missing_values / len(df)) * 100
    return pd.DataFrame({'Nombre de valeurs manquantes': missing_values,
                         'Pourcentage (%)': missing_percent})
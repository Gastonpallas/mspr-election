import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

def load_data(file_path):
    """Charger les données à partir d'un fichier Excel."""
    return pd.read_excel(file_path)

def explore_data(df, features, target):
    """Exploration des données."""
    sns.pairplot(df[features + [target]])
    plt.show()

def preprocess_data(df, features, target):
    """Prétraitement des données : normalisation et sélection des caractéristiques."""
    X = df[features]
    Y = df[target]

    # Normalisation
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Sélection des caractéristiques
    selector = SelectKBest(score_func=f_regression, k=min(10, len(features)))
    X_selected = selector.fit_transform(X_scaled, Y)

    return X_selected, Y

def split_data(X, Y, test_size=0.2, random_state=42):
    """Division des données en ensembles d'entraînement et de test."""
    return train_test_split(X, Y, test_size=test_size, random_state=random_state)

def train_linear_regression(X_train, Y_train):
    """Entraîner un modèle de régression linéaire."""
    model = LinearRegression()
    model.fit(X_train, Y_train)
    return model

def evaluate_model(model, X_test, Y_test):
    """Évaluation du modèle."""
    Y_pred = model.predict(X_test)
    mse = mean_squared_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)
    return mse, r2

def cross_validate(model, X, Y, cv=5):
    """Validation croisée."""
    scores = cross_val_score(model, X, Y, cv=cv)
    return scores.mean()

def tune_random_forest(X, Y):
    """Réglage des hyperparamètres du modèle Random Forest."""
    rf_model = RandomForestRegressor(random_state=42)
    param_grid = {'n_estimators': [100, 200, 300],
                  'max_depth': [None, 10, 20]}
    grid_search = GridSearchCV(rf_model, param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X, Y)
    best_rf_model = grid_search.best_estimator_
    return best_rf_model, grid_search.best_params_

def main():
    # Charger les données
    file_path = 'finalExcel/MergeElection2022_Faits_Sociale_Culture.xlsx'
    df = load_data(file_path)

    # Paramètres
    features = ['Tableau1AutresdpensesdaidesocialeTotalnetpardpartement31_2021',
                'Tableau1Dpensesnettestotalesdaideauxpersonnesgespardpartement3_2021',
                'Tableau1Dpensesnettestotalesdaidesocialelenfancepardpartementhorsdpensesdepersonnellexceptiondecellesliesauxassistantsfamiliaux18_2021',
                'Tableau1Dpensestotalesnettesdaidesocialeycomprislaidemdicalegnralelesfraiscommunsetlesdpensesdepersonnelpardpartement1_2021',
                'Tableau2AutresdpensesdaidesocialeTotalbrutpardpartement32_2021',
                'Tableau2Dpensesbrutestotalesdaideauxpersonnesgespardpartement4_2021',
                'Tableau2Dpensesbrutestotalesdaidesocialelenfancepardpartementhorsdpensesdepersonnellexceptiondecellesliesauxassistantsfamiliaux19_2021',
                'Tableau2Dpensestotalesbrutesdaidesocialeycomprislaidemdicalegnralelesfraiscommunsetlesdpensesdepersonnelpardpartement2_2021',
                'Tableau3Dpensesbrutesdaidedomicilepardpartement13_2021',
                'Tableau3Dpensesbrutestotalesdallocationspardpartement20_2021',
                'Tableau4DpensesbrutesdactionsducativesAEDetAEMOhorsdpensesdepersonnelsdpartementauxpardpartement21_2021',    
                'Tableau4Dpensestotalesbrutesdaidedomicilepardpartement6_2021',
                'Tableau5Dpensesbrutesdeprventionspcialisehorsdpensesdepersonnelsdpartementauxpardpartement22_2021',
                'Tableau6Dpensesbrutestotalesdeplacementspardpartement23_2021',
                'Tableau6Dpensestotalesbrutesdaidelaccueilpardpartement8_2021',
                'Tableau7Dpensesbrutesdeplacementfamilialassistantsfamiliauxpardpartement24_2021',
                'Tableau8Dpensesbrutesdeplacementshorsfamillesdaccueilpardpartement25_2021',
                'culture/1000POP', 'total_population', 'tauxpourmille', 'nuls', 'blancs', 'abstentions']
    target = 'LFI'

    # Exploration des données
    explore_data(df, features, target)

    # Prétraitement des données
    X, Y = preprocess_data(df, features, target)

    # Division des données
    X_train, X_test, Y_train, Y_test = split_data(X, Y)

    # Entraînement du modèle de régression linéaire
    linear_model = train_linear_regression(X_train, Y_train)

    # Évaluation du modèle de régression linéaire
    mse_linear, r2_linear = evaluate_model(linear_model, X_test, Y_test)
    print("Régression linéaire - Mean Squared Error:", mse_linear)
    print("Régression linéaire - R^2 Score:", r2_linear)

    # Validation croisée
    cross_val_score_linear = cross_validate(linear_model, X, Y)
    print("Régression linéaire - Scores de validation croisée :", cross_val_score_linear)

    # Réglage des hyperparamètres pour Random Forest
    best_rf_model, best_params_rf = tune_random_forest(X, Y)
    print("Meilleurs hyperparamètres Random Forest:", best_params_rf)

    # Évaluation du modèle Random Forest
    mse_rf, r2_rf = evaluate_model(best_rf_model, X, Y)
    print("Random Forest - Mean Squared Error:", mse_rf)
    print("Random Forest - R^2 Score:", r2_rf)

if __name__ == "__main__":
    main()

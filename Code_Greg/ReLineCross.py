import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Charger les données depuis le fichier Excel
df = pd.read_excel('finalExcel/MergeElection2022_Faits_Sociale_Culture.xlsx')

df = df.dropna()

# Colonnes à inclure dans la variable indépendante X
colonnes_X = ['Tableau1AutresdpensesdaidesocialeTotalnetpardpartement31_2021',
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
              'Tableau8Dpensesbrutesdeplacementshorsfamillesdaccueilpardpartement25_2021','culture/1000POP','total_population', 'tauxpourmille', 'nuls', 'blancs', 'abstentions']

# Diviser les données en variables indépendantes (X) et dépendante (Y)
X = df[colonnes_X]
Y = df['LFI']

# Créer un objet de modèle de régression linéaire
model = LinearRegression()

# Effectuer une validation croisée (cross-validation)
scores = cross_val_score(model, X, Y, cv=5)  # Utilisation de la validation croisée à 5 plis

# Imprimer les scores de validation croisée
print("Scores de validation croisée :", scores)
print("Moyenne des scores de validation croisée :", scores.mean())


# Calcul des résidus
y_pred = model.fit(X, Y).predict(X)
residuals = Y - y_pred

# Tracer le graphique des résidus
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, alpha=0.5)
plt.title("Graphique des résidus")
plt.xlabel("Valeurs prédites")
plt.ylabel("Résidus")
plt.axhline(y=0, color='r', linestyle='--')
plt.show()
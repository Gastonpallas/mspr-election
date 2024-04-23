import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Charger les données depuis un fichier CSV par exemple
data = pd.read_excel('finalExcel/gagnant.xlsx')
data = data.drop('DÃ©partement', axis=1)


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
              'Tableau8Dpensesbrutesdeplacementshorsfamillesdaccueilpardpartement25_2021',
              'culture/1000POP',
              'total_population',
              'tauxpourmille',
              'nuls',
              'blancs',
              'abstentions',
              'Taux de chÃ´mage',
              '[0;5[',
              '[10;15[',	'[15;20[',	'[20;25[',	'[25;30[',	'[30;35[',	'[35;40[',	'[40;45[',	'[45;50[',	'[50;55[',	'[55;60[',	'[5;10[',	'[60;65[',	'[65;70[',	'[70;75[',	'[75;80[',	'[80;85[',	'[85;90[',	'[90;95[',	'[95;99+]',	'Nombre de crÃ©ations d\'entreprises']




gironde = data[data['code_departement_1'] == 33]
gironde_parti = gironde['LFI']
gironde = gironde.drop('LFI', axis=1)
data = data.drop(31) # on enleve la gironde

Y = data['LFI']
X = data.drop('LFI', axis=1)


# On divise les données en ensembles d'entraînement et de test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# On créé et entraîner un modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, Y_train)

# On fait des prédictions sur l'ensemble de test
predictions = model.predict(X_test)

# On évalue les performances du modèle
mse = mean_squared_error(Y_test, predictions)
r2 = r2_score(Y_test, predictions)

print("Coefficients : ", model.coef_)
print("Intercept : ", model.intercept_)
print("Erreur quadratique moyenne (MSE) :", mse)
print("Coefficient de détermination (R²) :", r2)
print("Prédictions pour les prochaines élections présidentielles :", model.predict(gironde)[0])





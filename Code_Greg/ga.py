import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_excel('finalExcel/merge_v3_0.xlsx')

df

df.columns

for i, col in enumerate(df[df['code_departement_1'] == 33]):
    print(i, df[df['code_departement_1'] == 33][col])

df = df.drop('DÃ©partement', axis=1)

df

df['gagnant'].unique()

df['gagnant'] = df['gagnant'].map({parti:i+1 for i, parti in enumerate(df['gagnant'].unique())}) # transformation en valeur numérique des parti gagnante

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
              '[10;15[',	'[15;20[',	'[20;25[',	'[25;30[',	'[30;35[',	'[35;40[',	'[40;45[',	'[45;50[',	'[50;55[',	'[55;60[',	'[5;10[',	'[60;65[',	'[65;70[',	'[70;75[',	'[75;80[',	'[80;85[',	'[85;90[',	'[90;95[',	'[95;99+]',	'Nombre de crÃ©ations d\'entreprises',]

df['gagnant']

gironde = df[df['code_departement_1'] == 33]
gironde_gagnant = gironde['gagnant']
gironde = gironde.drop('gagnant', axis=1)

df = df.drop(31) # on enleve la gironde
df

Y = df['gagnant']
X = df.drop('gagnant', axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=42)

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



# On charge de nouvelles données
nouvelles_donnees = pd.read_excel('finalExcel/gagnant.xlsx')
nouvelles_donnees = nouvelles_donnees[nouvelles_donnees['Code dÃ©partement'] == 33]

# On fait des prédictions sur les nouvelles données
nouvelles_predictions = model.predict(nouvelles_donnees[[ 'tauxpourmille', 'Code dÃ©partement',
       'Tableau1AutresdpensesdaidesocialeTotalnetpardpartement31_2021',
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
       'code_departement_1', 'DLF', 'EELV', 'LFI', 'LO', 'LR', 'LREM', 'NPA',
       'PCF', 'PS', 'RN', 'ReconuÃªte', 'RÃ©sistons', 'abstentions', 'blancs',
       'nuls', 'gagnant', 'culture/1000POP', 'total_population',
        'Taux de chÃ´mage', '[0;5[', '[10;15[', '[15;20[',
       '[20;25[', '[25;30[', '[30;35[', '[35;40[', '[40;45[', '[45;50[',
       '[50;55[', '[55;60[', '[5;10[', '[60;65[', '[65;70[', '[70;75[',
       '[75;80[', '[80;85[', '[85;90[', '[90;95[', '[95;99+]',
       'Nombre de crÃ©ations d\'entreprises']])

# On affiche les prédictions pour les prochaines élections présidentielles
print("Prédictions pour les prochaines élections présidentielles :", nouvelles_predictions)



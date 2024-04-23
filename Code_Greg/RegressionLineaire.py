import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Créer un objet de modèle de régression linéaire
model = LinearRegression()

# Entraîner le modèle sur les données d'entraînement
model.fit(X_train, Y_train)

# Évaluer le modèle sur les données de test
score = model.score(X_test, Y_test)
print("Score de performance du modèle sur les données de test :", score)

# Afficher les coefficients du modèle
print("Coefficients du modèle :", model.coef_)

# Afficher l'ordonnée à l'origine du modèle
print("Ordonnée à l'origine du modèle :", model.intercept_)

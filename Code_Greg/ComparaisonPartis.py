import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données depuis le fichier Excel
df = pd.read_excel('finalExcel/MergeElection2022_Faits_Sociale_Culture.xlsx')

# Filtrer les données pour inclure uniquement les lignes correspondant aux partis RN, LREM et LFI
df_filtered = df[df['Parti'].isin(['RN', 'LREM', 'LFI'])].dropna()

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
              'culture/1000POP', 'total_population', 'tauxpourmille', 'nuls', 'blancs', 'abstentions']

# Diviser les données en variables indépendantes (X) et dépendante (Y) pour chaque parti
X_RN = df_filtered[df_filtered['Parti'] == 'RN'][colonnes_X]
Y_RN = df_filtered[df_filtered['Parti'] == 'RN']['abstentions']

X_LREM = df_filtered[df_filtered['Parti'] == 'LREM'][colonnes_X]
Y_LREM = df_filtered[df_filtered['Parti'] == 'LREM']['abstentions']

X_LFI = df_filtered[df_filtered['Parti'] == 'LFI'][colonnes_X]
Y_LFI = df_filtered[df_filtered['Parti'] == 'LFI']['abstentions']

# Créer un objet de modèle de régression linéaire pour chaque parti
model_RN = LinearRegression()
model_LREM = LinearRegression()
model_LFI = LinearRegression()

# Effectuer une validation croisée pour chaque parti
scores_RN = cross_val_score(model_RN, X_RN, Y_RN, cv=5)
scores_LREM = cross_val_score(model_LREM, X_LREM, Y_LREM, cv=5)
scores_LFI = cross_val_score(model_LFI, X_LFI, Y_LFI, cv=5)

# Imprimer les scores de validation croisée pour chaque parti
print("Scores de validation croisée pour RN:", scores_RN)
print("Moyenne des scores de validation croisée pour RN:", scores_RN.mean())
print("\nScores de validation croisée pour LREM:", scores_LREM)
print("Moyenne des scores de validation croisée pour LREM:", scores_LREM.mean())
print("\nScores de validation croisée pour LFI:", scores_LFI)
print("Moyenne des scores de validation croisée pour LFI:", scores_LFI.mean())

# Créer des graphiques pour visualiser les performances des modèles pour chaque parti
plt.figure(figsize=(8, 6))
sns.barplot(x=['RN', 'LREM', 'LFI'], y=[scores_RN.mean(), scores_LREM.mean(), scores_LFI.mean()])
plt.title('Scores moyens de validation croisée pour les différents partis')
plt.xlabel('Parti')
plt.ylabel('Score moyen de validation croisée')
plt.ylim(0, 1)  # Limiter l'axe y entre 0 et 1 pour les scores
plt.show()

import pandas as pd

# Charger les fichiers Excel dans des dataframes
df1 = pd.read_excel('CleanForMerge/Tableau1AutresdpensesdaidesocialeTotalnetpardpartement31_renamed.xlsx')
df2 = pd.read_excel('CleanForMerge/Tableau1Dpensesnettestotalesdaideauxpersonnesgespardpartement3_renamed.xlsx')

# Fusionner les dataframes en utilisant la fonction merge de pandas
merged_df = pd.merge(df1, df2, how='inner')

# Écrire le résultat fusionné dans un nouveau fichier Excel
merged_df.to_excel('finalExcel/fusionTest2.xlsx', index=False)

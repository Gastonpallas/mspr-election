import pandas as pd

# Charger le fichier Excel dans un dataframe
df = pd.read_excel('finalExcel/fichier_fusionne6.xlsx')

# Supprimer les 100 premières lignes des colonnes 6 à 9
df.iloc[100:, 10:19] = None

# Écrire le résultat dans un nouveau fichier Excel
df.to_excel('finalExcel/fichier_fusionneTest1.xlsx', index=False)

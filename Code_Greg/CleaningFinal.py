import pandas as pd

# Charger le fichier Excel
df = pd.read_excel('finalExcel/donneesPropres.xlsx')

# # Supprimer les lignes avec des valeurs NaN (cellules vides)
# df = df.dropna()

print(df.info())

# # Enregistrer le DataFrame modifié dans un nouveau fichier Excel
# df.to_excel('finalExcel/donneesPropresFinal.xlsx', index=False)

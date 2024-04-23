import pandas as pd

# Charger le fichier Excel
df = pd.read_excel('finalExcel/merge_v3_0.xlsx')

# Sélectionner la colonne à modifier
colonne = 'gagnant'

print(df.columns)


# # Remplacer les valeurs par les valeurs numériques souhaitées
# remplacements = {'LREM': 0, 'RN': 1, 'LFI': 2}
# df[colonne] = df[colonne].replace(remplacements)

# # Sauvegarder dans un nouveau fichier Excel
# df.to_excel('finalExcel/gagnant.xlsx', index=False)

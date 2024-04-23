import os
import pandas as pd

repertoire = 'CleanForMerge'
dfs = []
columns = set()  # Utilisation d'un ensemble pour éviter les doublons
for fichier in os.listdir(repertoire):
    if fichier.endswith('.xlsx'):
        chemin_fichier_excel = os.path.join(repertoire, fichier)
        df = pd.read_excel(chemin_fichier_excel)
        dfs.append(df)
        columns.update(df.columns)

new_df = pd.concat(dfs, ignore_index=True)
# Réorganiser les colonnes dans l'ordre obtenu (convertir l'ensemble en une liste)
columns_list = list(columns)
new_df = new_df[columns_list]

chemin_fichier_fusionne = 'finalExcel/fichier_fusionne7.xlsx'
new_df.to_excel(chemin_fichier_fusionne, index=False)

print("Fusion des fichiers terminée. Le fichier fusionné a été enregistré à :", chemin_fichier_fusionne)

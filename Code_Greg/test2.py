import os
import pandas as pd

repertoire = 'CleanForMerge'
dfs = []
columns = []
for fichier in os.listdir(repertoire):
    if fichier.endswith('.xlsx'):
        chemin_fichier_excel = os.path.join(repertoire, fichier)
        df = pd.read_excel(chemin_fichier_excel)
        dfs.append(df)
        column = df.columns
        for i in column:
            if i not in columns:
                columns.append(i)

new_df = pd.concat(dfs, ignore_index=True)

chemin_fichier_fusionne = 'finalExcel/fichier_fusionne8.xlsx'
new_df.to_excel(chemin_fichier_fusionne, index=False)

print("Fusion des fichiers terminée. Le fichier fusionné a été enregistré à :", chemin_fichier_fusionne)
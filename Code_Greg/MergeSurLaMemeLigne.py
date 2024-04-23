import os
import pandas as pd

# Chemin du répertoire contenant vos fichiers Excel
repertoire = 'CleanForMerge'

# Liste pour stocker les dataframes de chaque fichier
dfs = []

# Parcourir tous les fichiers dans le répertoire
for fichier in os.listdir(repertoire):
    if fichier.endswith('.xlsx'):
        chemin_fichier_excel = os.path.join(repertoire, fichier)

        # Lire le fichier Excel dans un dataframe
        df = pd.read_excel(chemin_fichier_excel)

        # Ajouter le dataframe à la liste
        dfs.append(df)

# Fusionner tous les dataframes en un seul en conservant la première ligne de chaque fichier
df_merged = pd.concat(dfs, ignore_index=True)

# Supprimer les doublons de la première ligne
df_merged = pd.concat([df_merged.loc[:1], df_merged.loc[~df_merged.duplicated()]])

# Réinitialiser l'index
df_merged.reset_index(drop=True, inplace=True)

# Enregistrer le dataframe fusionné dans un nouveau fichier Excel
chemin_fichier_fusionne = 'finalExcel/fichier_fusionne4.xlsx'
df_merged.to_excel(chemin_fichier_fusionne, index=False)

print("Fusion des fichiers terminée. Le fichier fusionné a été enregistré à :", chemin_fichier_fusionne)
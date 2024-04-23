import pandas as pd
import glob
from xlsxwriter import Workbook

# Chemin du dossier contenant les fichiers Excel à fusionner
chemin_dossier = './Clean/'

# Modèle du nom des fichiers Excel à fusionner
modele_nom_fichier = '*.xlsx'

# Liste des fichiers Excel correspondant au modèle
fichiers_excel = glob.glob(chemin_dossier + modele_nom_fichier)

# Créer un DataFrame pandas pour chaque fichier Excel et les stocker dans un dictionnaire
dfs = {}
for fichier in fichiers_excel:
    nom_feuille = pd.ExcelFile(fichier).sheet_names[0]  # Utilisez le premier nom de feuille
    dfs[nom_feuille] = pd.read_excel(fichier)

# Fusionner les DataFrames dans un seul DataFrame avec plusieurs feuilles
with pd.ExcelWriter('fichier_final.xlsx', engine='xlsxwriter') as writer:
    for nom_feuille, df in dfs.items():
        df.to_excel(writer, sheet_name=nom_feuille, index=False)



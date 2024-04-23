import pandas as pd

# Chemin vers les fichiers Excel à fusionner
chemin_fichier_1 = 'Clean/Tableau1AutresdpensesdaidesocialeTotalnetpardpartement31.xlsx'
chemin_fichier_2 = 'Clean/Tableau1Dpensesnettestotalesdaideauxpersonnesgespardpartement3.xlsx'

nom = "Tableau1AutresdpensesdaidesocialeTotalnetpardpartement31"

# On lit les fichiers Excel dans des dataframes
df1 = pd.read_excel(chemin_fichier_1)
df2 = pd.read_excel(chemin_fichier_2)


# Obtenir le nom de fichier sans l'extension
nom_fichier_sans_extension = chemin_fichier_1.split('/')[-1].split('.')[0]

# Renommer les colonnes en ajoutant le nom de fichier
nouveaux_noms_colonnes = {}
for colonne in df1.columns:
    nouveaux_noms_colonnes[colonne] = f"{nom_fichier_sans_extension}_{colonne}"

# Utiliser la méthode rename() pour renommer les colonnes
df = df1.rename(columns=nouveaux_noms_colonnes)


# Afficher les noms des colonnes
print("Noms des colonnes dans le fichier Excel:")
print(df.columns)

# # On fusionne les dataframes
# df_fusionne = pd.concat([df1, df2], ignore_index=True)

# # Chemin pour enregistrer le fichier Excel fusionné
# chemin_fichier_fusionne = 'chemin/vers/fichier_fusionne.xlsx'

# # Écrire le dataframe fusionné dans un nouveau fichier Excel
# df_fusionne.to_excel(chemin_fichier_fusionne, index=False)

# print("Fusion terminée. Le fichier fusionné a été enregistré à :", chemin_fichier_fusionne)

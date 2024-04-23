import os
import pandas as pd

# Chemin du répertoire contenant vos fichiers Excel
repertoire = 'Clean'
repertoireEnregistrement = 'CleanForMerge'

# Parcourir tous les fichiers dans le répertoire
for fichier in os.listdir(repertoire):
    if fichier.endswith('.xlsx'):
        chemin_fichier_excel = os.path.join(repertoire, fichier)

        # Lire le fichier Excel dans un dataframe
        df = pd.read_excel(chemin_fichier_excel)

        # Obtenir le nom de fichier sans l'extension
        nom_fichier_sans_extension = fichier.split('.')[0]

        # Renommer les colonnes en ajoutant le nom de fichier
        nouveaux_noms_colonnes = {}
        for colonne in df.columns:
            nouveaux_noms_colonnes[colonne] = f"{nom_fichier_sans_extension}_{colonne}"

        # Utiliser la méthode rename() pour renommer les colonnes
        df = df.rename(columns=nouveaux_noms_colonnes)

        # Chemin pour enregistrer le fichier Excel avec les colonnes renommées
        chemin_fichier_renomme = os.path.join(repertoireEnregistrement, f"{nom_fichier_sans_extension}_renamed.xlsx")

        # Écrire le dataframe avec les colonnes renommées dans un nouveau fichier Excel
        df.to_excel(chemin_fichier_renomme, index=False)

        print(f"Colonnes renommées pour le fichier {fichier}. Fichier renommé enregistré à : {chemin_fichier_renomme}")

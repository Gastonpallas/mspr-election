import pandas as pd

# Chemin vers votre fichier Excel
chemin_fichier_excel = "finalExcel/donneesPropresFinal.xlsx"

# Lire le fichier Excel
donnees_excel = pd.read_excel(chemin_fichier_excel)

# Supprimer les colonnes "Code région" et "Département"
donnees_sans_colonnes = donnees_excel.drop(columns=["Code région", "Département"])

# Sauvegarder les données modifiées dans un nouveau fichier Excel
chemin_fichier_excel_modifie = "finalExcel/AidesSociales.xlsx"
donnees_sans_colonnes.to_excel(chemin_fichier_excel_modifie, index=False)

print("Les colonnes 'Code région' et 'Département' ont été supprimées avec succès.")

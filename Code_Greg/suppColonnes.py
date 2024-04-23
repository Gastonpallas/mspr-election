import pandas as pd
import re

# Chargement du fichier Excel
df = pd.read_excel('finalExcel/AidesSociales.xlsx')

# Définition des mots-clés à exclure et à conserver
mots_cles_exclus = ["2016", "2017", "2018", "2019", "2020"]
mots_cles_conserver = ["2021"]

# Fonction pour vérifier si un mot-clé spécifique est présent dans le nom de colonne
def mot_cle_present(colonne, mots_cles):
    for mot_cle in mots_cles:
        if re.search(mot_cle, colonne, re.IGNORECASE):
            return True
    return False

# Liste des colonnes à conserver
colonnes_a_conserver = [colonne for colonne in df.columns if mot_cle_present(colonne, mots_cles_conserver)]

# Liste des colonnes à supprimer
colonnes_a_supprimer = [colonne for colonne in df.columns if mot_cle_present(colonne, mots_cles_exclus) and colonne not in colonnes_a_conserver]

# Suppression des colonnes
df = df.drop(columns=colonnes_a_supprimer)

# Enregistrement du DataFrame dans un nouveau fichier Excel
df.to_excel('finalExcel/AidesSociales2.xlsx', index=False)

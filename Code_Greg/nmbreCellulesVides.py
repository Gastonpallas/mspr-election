import openpyxl

# Chargement du fichier Excel
wb = openpyxl.load_workbook('finalExcel/AidesSociales.xlsx')

# Sélection de la feuille de calcul
feuille = wb.active

# Initialisation du compteur de cellules vides
cellules_vides = 0

# Parcours de chaque ligne et colonne
for ligne in feuille.iter_rows():
    for cellule in ligne:
        if cellule.value is None:
            cellules_vides += 1

# Affichage du nombre de cellules vides
print("Nombre de cellules vides :", cellules_vides)

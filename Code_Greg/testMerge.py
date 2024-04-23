import os
from aspose.cells import Workbook

# Chemin du répertoire contenant les fichiers Excel à fusionner
repertoire = 'CleanForMerge'

# Créer un workbook vide comme destination pour la fusion
destination_workbook = Workbook()

# Parcourir tous les fichiers dans le répertoire
for fichier in os.listdir(repertoire):
    if fichier.endswith('.xlsx'):
        chemin_fichier_excel = os.path.join(repertoire, fichier)

        # Charger le fichier Excel dans un workbook
        workbook = Workbook(chemin_fichier_excel)

        # Combiner le contenu du fichier Excel actuel avec le workbook de destination
        destination_workbook.combine(workbook)

# Enregistrer le workbook fusionné dans un nouveau fichier Excel
chemin_fichier_fusionne = 'finalExcel/Output.xlsx'
destination_workbook.save(chemin_fichier_fusionne)

print("Fusion des fichiers terminée. Le fichier fusionné a été enregistré à :", chemin_fichier_fusionne)

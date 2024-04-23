import pandas as pd

# Chargement du fichier Excel
df = pd.read_excel('finalExcel/fusionne.xlsx')

# Création d'un dictionnaire pour stocker le nom de la colonne et les valeurs non nulles associées
valeurs_non_nulles_par_colonne = {}

# Parcours de chaque colonne
for colonne in df.columns:
    # Filtrage des valeurs non nulles pour cette colonne
    valeurs_non_nulles_colonne = df[colonne].dropna().tolist()
    
    # Ajout du nom de la colonne et des valeurs non nulles associées au dictionnaire
    if valeurs_non_nulles_colonne:
        valeurs_non_nulles_par_colonne[colonne] = valeurs_non_nulles_colonne

# Création d'un DataFrame à partir du dictionnaire
df_valeurs_non_nulles = pd.DataFrame.from_dict(valeurs_non_nulles_par_colonne, orient='index').transpose()

# Enregistrement du DataFrame contenant les valeurs non nulles dans un nouveau fichier Excel
df_valeurs_non_nulles.to_excel('finalExcel/valeurs_non_nulles.xlsx', index=False)

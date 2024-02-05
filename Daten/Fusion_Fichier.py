import pandas as pd

# Liste des noms de fichiers CSV
noms_fichiers = ['/Users/sacha/Documents/Cours Epsi 2023/MSPR1/Données/Temps de parole/46TP-TA_Presidentielle_2022__1er au 16 janvier 2022_v5_Nettoye.csv',
 '/Users/sacha/Documents/Cours Epsi 2023/MSPR1/Données/Temps de parole/47TP-TA_Presidentielle_2022__1er au 30 janvier 2022_v5_Nettoye.csv',
  '/Users/sacha/Documents/Cours Epsi 2023/MSPR1/Données/Temps de parole/48TP-TA_Presidentielle_2022__1er janvier au 13 février 2022_v3_Nettoye.csv',
   '/Users/sacha/Documents/Cours Epsi 2023/MSPR1/Données/Temps de parole/49TP-TA_Presidentielle_2022__1er janvier au 27 février 2022_v2_Nettoye.csv',
    '/Users/sacha/Documents/Cours Epsi 2023/MSPR1/Données/Temps de parole/50TP-TA_Presidentielle_2022__1er janvier au 7 mars 2022_v2_Nettoye.csv']

# Créer une liste pour stocker les DataFrames
dfs = []

# Charger chaque fichier CSV dans un DataFrame et l'ajouter à la liste dfs
for nom_fichier in noms_fichiers:
    df = pd.read_csv(nom_fichier)
    dfs.append(df)

# Fusionner tous les DataFrames en un seul
df_combine = pd.concat(dfs, ignore_index=True)

# Afficher un aperçu du DataFrame combiné
print(df_combine.head())

# Enregistrer le DataFrame combiné dans un nouveau fichier CSV
df_combine.to_csv('fusion_Temps_Parole.csv', index=False)

# Afficher un message de confirmation
print("La fusion des fichiers CSV est terminée. Le fichier fusion.csv a été créé.")

import pandas as pd
import matplotlib.pyplot as plt

# Charger les données à partir du fichier Excel
df = pd.read_excel('finalExcel/merge_v3_0.xlsx')

# Supprimer les lignes contenant des valeurs manquantes
df = df.dropna()

# Filtrer les données pour inclure uniquement le département avec le code 33
df_filtered = df[df['Code dÃ©partement'] == 33]

# Sélectionner la colonne contenant les dépenses nettes totales d'aide sociale pour le département 33
depenses_par_departement = df_filtered['Tableau1AutresdpensesdaidesocialeTotalnetpardpartement31_2021','Tableau1Dpensesnettestotalesdaideauxpersonnesgespardpartement3_2021']

# Création du diagramme circulaire
plt.figure(figsize=(8, 8))
plt.pie(depenses_par_departement, labels=df_filtered, autopct='%1.1f%%', startangle=140)
plt.title('Répartition des dépenses nettes totales d\'aide sociale pour le département 33')
plt.axis('equal')  # Assure que le diagramme est un cercle

# Affichage du diagramme circulaire
plt.show()

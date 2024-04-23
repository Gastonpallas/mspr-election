import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# On récupère l'emplacement du fichier
file_path = 'Excel/Tableau1Dpensesnettestotalesdaideauxpersonnesgespardpartement3.xlsx'


# On utilise read_excel pour lire le fichier Excel
df = pd.read_excel(file_path)

# on affiche les premières lignes
print(df.head(2))


# On récupère le nombre de lignes
nombre_de_lignes = len(df)

# On affiche le nombre de lignes
print(f"Le dataset contient {nombre_de_lignes} lignes.")

# On récupère le nombre de colonnes
nombre_de_colonnes = df.shape

# On affiche le nombre de colonnes
print(f"Le dataset contient {nombre_de_colonnes} colonnes.")


# On récupère le nom des colonnes du DataFrame
noms_des_colonnes = df.columns

# On affiche le nom des colonnes
print("Noms des colonnes :")
for nom_colonne in noms_des_colonnes:
    print(nom_colonne)

# On récupère nos données
annee2021 = df['2021']
departement = df['Département']

# On crée notre bar plot
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
sns.barplot(x=departement, y=annee2021, palette='viridis')

plt.title('Distribution des aides par département')
plt.xlabel('Département')
plt.ylabel('Prix (en euros)')
plt.show()
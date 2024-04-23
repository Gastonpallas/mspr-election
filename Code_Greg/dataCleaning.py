# Data Cleaning du jeu de données sur les aides sociales par départements

# On commence par importer la librairies Pandas
import pandas as pd

# On récupère notre fichier excel puis on le stocke dans une variable
data = pd.read_excel('./Données/AidesSocialesTableau.xlsx')

# On récupère notre fichier csv puis on le stocke dans une variable
# dataCSV = pd.read_csv('./Données/AidesSocialesTableau.csv')

# On utilise cette ligne de commande afin de lire le fichier excel
xls = pd.ExcelFile('./Données/AidesSocialesTableau.xlsx')

# On utilise cette ligne de commande afin de lire le fichier csv
# xlsCSV = pd.ExcelFile('./Données/AidesSocialesTableau.csv')

# On affiche la liste de nos feuilles
#print(xls.sheet_names)

# On récupère une feuille
f1_depenses_totales_aide_soc = pd.read_excel(xls, 'Feuil1')

# ********************************************************** EXCEL **********************************************************


# On veut compter le nombre de valeurs manquantes par variable
# print(data.isnull().sum())

# On récupère des informations sur nos données

# print("Sommaire")
# data.info()

# On récupère le nom des colonnes
# print("Nom des colonnes")
# nom_colonne = data.columns
# print(nom_colonne)

# On récupère des données statistiques sur notre jeu de données
# print("Données Statistiques")
# description = data.describe()
# print(description) 

# On lit le fichier excel
#print(data)

# On souhaite visualiser les données nulles

don_nulles = data.isnull()
#print(don_nulles)

# On retire les lignes contenant des données manquantes
data_na_drop = data.dropna(how='all', axis=1)
print(data_na_drop)

# On veut compter le nombre de valeurs manquantes par variable
print(data_na_drop.isnull().sum())


# On vérifie la présence de doublons
dupli = data_na_drop.duplicated()
print(dupli)

# On supprime les années qui ne sont pas utiles
dataF = data_na_drop.drop(['1999', '2000',
       '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
       '2010', '2011', '2012', '2013', '2014', '2015', '2016'], axis=1)

print(dataF)

dataF = dataF.dropna()
print(dataF)
don_nulles = dataF.isnull()
print(don_nulles)


# Enregistrer les données nettoyées dans un fichier CSV
dataF.to_excel("données_nettoyées_aides_sociales.xlsx")

# ********************************************************** EXCEL **********************************************************



# ********************************************************** CSV **********************************************************


# On veut compter le nombre de valeurs manquantes par variable
#print(data.isnull().sum())

# On récupère des informations sur nos données

# print("Sommaire")
# dataCSV.info()

# # On récupère le nom des colonnes
# print("Nom des colonnes")
# nom_colonne = dataCSV.columns
# print(nom_colonne)

# # On récupère des données statistiques sur notre jeu de données
# print("Données Statistiques")
# description = dataCSV.describe()
# print(description) 




# ********************************************************** CSV **********************************************************

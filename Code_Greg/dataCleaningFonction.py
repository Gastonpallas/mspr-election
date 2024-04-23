# On commence par importer la librairies Pandas
import pandas as pd

def dataCleaning(nomDuFichierExcel):
    # On récupère notre fichier excel puis on le stocke dans une variable
    data = pd.read_excel(nomDuFichierExcel)
    
    don_nulles = data.isnull()

    # On retire les lignes contenant des données manquantes
    data_na_drop = data.dropna(how='all', axis=1)

    # On supprime les années qui ne sont pas utiles
    dataF = data_na_drop.drop(['1999', '2000',
        '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
        '2010', '2011', '2012', '2013', '2014', '2015', '2016'], axis=1)

    dataF = dataF.dropna()
    don_nulles = dataF.isnull()




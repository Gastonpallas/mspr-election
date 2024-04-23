import pandas as pd
import re
import glob

def retirer_caracteres_speciaux(chaine):
    # Utilisation d'une expression régulière pour ne conserver que les lettres et les chiffres
    chaine_sans_speciaux = re.sub(r'[^a-zA-Z0-9_]', '', chaine)
    return chaine_sans_speciaux




def supprimer_colonne_ligne_fichier_excel(tab):

    for i in range (0, len(tab)):

        chemin_fichier_sortie = './Clean/' + tab[i]
        chemin_fichier_entree = './Données/' + tab[i]
        # Charger le fichier Excel
        df = pd.read_excel(chemin_fichier_entree, header=None)

        
        # Supprimer la colonne A (index 0)
        df = df.drop(0, axis=1)

        # Supprimer la ligne 1
        df = df.drop(0, axis=0)

        # Utiliser la première ligne comme en-tête de colonnes
        df.columns = df.iloc[0]

        # Supprimer les colonnes 4 à 16
        df = df.drop(df.columns[3:20], axis=1)

        # Supprimer les lignes contenant des valeurs vides
        df = df.dropna()

        # Écrire le DataFrame modifié dans un nouveau fichier Excel
        df.to_excel(chemin_fichier_sortie, index=False, header=False)



def dataCleaning():
    tab = creatoinFichierExcel()
    dossier = "./Clean/"
    dossier2 = "./Données/"
    # On récupère notre fichier excel puis on le stocke dans une variable
    for i in range (0, len(tab)):
        chemin = dossier2 + tab[i]
        data = pd.read_excel(chemin)

        # On retire les lignes contenant des données manquantes
        data_na_drop = data.dropna(how='all', axis=1)

        # On supprime les années qui ne sont pas utiles
        dataF = data_na_drop.drop(['1999', '2000',
            '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
            '2010', '2011', '2012', '2013', '2014', '2015', '2016'], axis=2)

        dataF = dataF.dropna()
        chemin_complet = dossier + tab[i] 
        dataF.to_excel(chemin_complet)


def reu():

    # Spécifiez le chemin vers le dossier contenant les fichiers Excel
    chemin_dossier_excel = "./Delete/"

    # Obtenez la liste de tous les fichiers Excel dans le dossier
    fichiers_excel = glob.glob(chemin_dossier_excel + "*.xlsx")

    # Créez une liste pour stocker les DataFrames de chaque fichier Excel
    dfs = []

    # Lisez chaque fichier Excel et ajoutez le DataFrame à la liste
    for fichier_excel in fichiers_excel:
        df = pd.read_excel(fichier_excel)
        dfs.append(df)

    # Concaténez tous les DataFrames en un seul
    df_final = pd.concat(dfs, ignore_index=True)

    # Spécifiez le chemin pour le fichier Excel final
    chemin_fichier_final = "./Clean/Final.xlsx"

    # Écrivez le DataFrame final dans un fichier Excel
    df_final.to_excel(chemin_fichier_final, index=False)


def reu2():

    # Spécifiez le chemin vers le dossier contenant les fichiers Excel
    chemin_dossier_excel = "./Delete/"

    # Obtenez la liste de tous les fichiers Excel dans le dossier
    fichiers_excel = glob.glob(chemin_dossier_excel + "*.xlsx")

    # Spécifiez le chemin pour le fichier Excel final
    chemin_fichier_final = "./Clean/Final.xlsx"

    # Utilisez ExcelWriter pour écrire plusieurs DataFrames dans un fichier Excel
    with pd.ExcelWriter(chemin_fichier_final, engine='xlsxwriter') as writer:
        # Lisez chaque fichier Excel et écrivez-le dans une feuille différente
        for i, fichier_excel in enumerate(fichiers_excel):
            df = pd.read_excel(fichier_excel, sheet_name=f"Feuille_{i+1}")
            df.to_excel(writer, sheet_name=f"Feuille_{i+1}", index=False)




def creatoinFichierExcel():
    tab = []

    # Spécifiez le chemin vers votre fichier Excel
    chemin_fichier_excel = "./Données/AidesSociales.xlsx"

    # Spécifiez le chemin vers votre fichier Excel

    dossier = "./Données/"

    chiffre = 1

    # Chargez le fichier Excel
    xls = pd.ExcelFile(chemin_fichier_excel)

    # Récupérez la liste des noms de feuilles
    noms_feuilles = xls.sheet_names

    # print(noms_feuilles)

    # df = pd.read_excel(chemin_fichier_excel, sheet_name = "PA-tab1", header=None)

    # valeur_cellule_A1 = df.at[0, 0]

    # print(valeur_cellule_A1)


    for i in range (3, len(noms_feuilles)):

        # Chargez le fichier Excel en spécifiant la feuille
        df = pd.read_excel(chemin_fichier_excel, sheet_name = noms_feuilles[i], header=None)

        # On récupère le nom du tableau
        valeur_cellule_A1 = df.at[0, 0]

        # Sélectionnez les lignes de la 8e à la 112e et les 26 colonnes
        tableau = df.iloc[7:112, :26]

        # Concaténation du chemin de fichier
        chemin_complet = valeur_cellule_A1 + str(chiffre) 

        chemin_complet = retirer_caracteres_speciaux(chemin_complet)

        chemin_complet = chemin_complet + ".xlsx"
        tab.append(chemin_complet)
        chemin_complet = dossier + chemin_complet 


        
        # tableau.to_excel(chemin_complet)
        # print(chemin_complet)
        chiffre +=1


    return tab



def supprimer_colonne(tab):

    for i in range (0, len(tab)):

        chemin_fichier_sortie = './Clean/' + tab[i]
        chemin_fichier_entree = './Delete/' + tab[i]
        # Charger le fichier Excel
        df = pd.read_excel(chemin_fichier_entree, header=None)


       # Supprimer les colonnes spécifiées
        colonnes_a_supprimer = ['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                                '2010', '2011', '2012', '2013', '2014', '2015', '2016']
        
        df = df.drop(colonnes_a_supprimer, axis=1, errors='ignore')  # errors='ignore' permet d'ignorer les colonnes absentes

        # Écrire le DataFrame modifié dans un nouveau fichier Excel
        df.to_excel(chemin_fichier_sortie, index=False, header=False)

# dataCleaning()
# print(creatoinFichierExcel())

# 'Tableau1Dpensestotalesnettesdaidesocialeycomprislaidemdicalegnralelesfraiscommunsetlesdpensesdepersonnelpardpartement1.xlsx'
tab = creatoinFichierExcel()
supprimer_colonne_ligne_fichier_excel(tab)


# reu2()
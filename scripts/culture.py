import pandas as pd

df = pd.read_csv('./data_raw/base-des-lieux-et-des-equipements-culturels.csv', sep=';', low_memory=False)
column = ['n_departement', 'type_equipement_ou_lieu','fonction_1']
df = df[column]
result = df.groupby(['n_departement', 'type_equipement_ou_lieu', 'fonction_1']).size().reset_index(name='nombre')

for i in range(len(result)):
    if result.iloc[i]['n_departement'] == '2':
        result.at[i, 'n_departement'] = '20'
    
    if result.iloc[i]['n_departement'] == '6':
        result.at[i, 'n_departement'] = '60'

result.drop(columns=['type_equipement_ou_lieu'], inplace=True)
culture_df = result.groupby(['n_departement'])['nombre'].sum().reset_index()
culture_df = culture_df.rename(columns={'n_departement': 'code_departement'})
population_df = pd.read_csv("./donnees/population_departement.csv")
result_merged = pd.merge(culture_df, population_df, on='code_departement', how='left')
result_merged['culture/1000POP'] = result_merged['nombre'] / result_merged['total_population'] * 1000
colonnes_a_garder = ['code_departement', 'culture/1000POP']
result_merged = result_merged[colonnes_a_garder]

output_path = './data_clean/culture.csv'
result_merged.to_csv(output_path, index=False)
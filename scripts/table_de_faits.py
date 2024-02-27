import pandas as pd

population = pd.read_excel('./data_raw/Populations.xlsx')
departement = pd.read_csv('./data_raw/departements-france.csv')
output_path = './data_clean/population_departement.csv'
df = pd.merge(population, departement, on='code_departement', how='inner')
df = df[['code_departement', 'nom_departement', 'Total']]
df = df.rename(columns={'Total': 'total_population'})
df.to_csv(output_path, index=False)
import pandas as pd
df = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/acc332f6-92be-42af-9721-f3609bea8cfc',  sep= ';')
df['tauxpourmille'] = df['tauxpourmille'].str.replace(',', '.')
df['LOG'] = df['LOG'].str.replace(',', '.')
df['tauxpourmille'] = df['tauxpourmille'].astype(float)
df['LOG'] = df['LOG'].astype(float)
missing_count = df.isnull().sum()
null_values = df[df.isnull().any(axis=1)]
df = df.dropna()
df['Code.région'] = df['Code.région'].astype(int)
df['annee'] = '20' + df['annee'].astype(str)
df_sorted = df.sort_values(by='Code.département')

df_sorted['annee'] = df_sorted['annee'].astype(int)


df_filtered = df_sorted.query('annee == 2022')

group_df = df_filtered.groupby(['Code.département', 'Code.région']).agg({
    'faits': 'sum',
    'tauxpourmille': 'sum'
}).reset_index()

# Sélectionner uniquement les colonnes requises
group_df = group_df[['Code.département', 'faits', 'tauxpourmille']]

# Afficher le DataFrame résultant
group_df = group_df.rename(columns={'Code.département': 'code_departement'})
sortie = './data_clean/security.csv'
group_df.to_csv(sortie, index=False)
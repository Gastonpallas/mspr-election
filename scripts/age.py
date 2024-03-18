import pandas as pd

df = pd.read_excel('./data_raw/age.xlsx')

column = ['ZONE', 'SEXE', 'TRAGE', 'POP_2022']
df = df[column]

df_pivot = df.pivot(index=['code_departement', 'SEXE'], columns='TRAGE', values='POP_2022').reset_index()
df_pivot.columns.name = None
df = df_pivot

df.drop(columns=['SEXE'], inplace=True)

output_path = './data_clean/age.csv'
df.to_csv(output_path, index=False)
import pandas as pd

df = pd.read_excel('./data_raw/age.xlsx')
to_keep = ['ZONE','SEXE','TRAGE',  'POP_2022']
df = df[to_keep]
df = df.rename(columns={'ZONE': 'code_departement'})
df_pivot = df.pivot(index=['code_departement', 'SEXE'], columns='TRAGE', values='POP_2022').reset_index()
df_pivot.columns.name = None
df = df_pivot
df = df.groupby(['code_departement']).sum().reset_index()
df.drop(columns=['SEXE'], inplace=True)

output = './data_clean/age.csv'
df.to_csv(output, index=False)

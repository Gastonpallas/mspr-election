import pandas as pd

df = pd.read_excel('../data/Entreprise.xlsx', skiprows=3)
df = df.rename(columns={'Unnamed: 0': 'Code', 'Unnamed: 1': 'Département'})

df_mean = df[['Département', 'Nombre de créations d\'entreprises']]
df_mean = df_mean[:96]
df_mean.isetitem(1, df_mean.iloc[:, 1].astype(int))
df_mean.to_csv('../data_clean/entreprise.csv', index=False, sep=';')

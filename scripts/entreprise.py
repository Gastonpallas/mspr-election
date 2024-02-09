#!/usr/bin/env python3

import pandas as pd

df = pd.read_excel('./data_raw/Entreprise.xlsx', skiprows=3)
df = df.rename(columns={'Unnamed: 0': 'Code', 'Unnamed: 1': 'Département'})

df_mean = df[['Département', 'Nombre de créations d\'entreprises']]
df_mean = df_mean[:96]
df_mean.isetitem(1, df_mean.iloc[:, 1].astype(int))
df_sorted = df_mean.sort_values(by='Département', ascending=True)

df_sorted.to_csv('./data_clean/entreprise.csv', index=False, sep=';')

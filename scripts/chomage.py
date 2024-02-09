#!/usr/bin/env python3

import pandas as pd
import warnings

df = pd.read_csv('./data_raw/chomage_per_region_and_dep.csv', sep=';')
df[df.columns[~df.columns.isin(['Libellé', '1982-T2'])]]
df = df[df['Libellé'] != 'Codes']

df_mean = df[['Libellé', '2022-T1','2022-T2', '2022-T3', '2022-T4']]
df_mean = df_mean[:-4]
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    df_mean.loc[:, -1] = df_mean.loc[:, '2022-T1'].astype(float)
    df_mean.loc[:, -2] = df_mean.loc[:, '2022-T2'].astype(float)
    df_mean.loc[:, -3] = df_mean.loc[:, '2022-T3'].astype(float)
    df_mean.loc[:, -4] = df_mean.loc[:, '2022-T4'].astype(float)
    df_mean['2022'] = df_mean.mean(axis=1)
    df_mean= df_mean[['Libellé', '2022']]
    df_mean = df_mean[~df_mean['Libellé'].str.contains('région')]
    df_mean['Libellé'] = df_mean['Libellé'].str.replace('Taux de chômage localisé par département - ', '')
    df_sorted = df_mean.sort_values(by='Libellé', ascending=True)

df_sorted.to_csv('./data_clean/chomage.csv', index=False)
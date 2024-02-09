#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/acc332f6-92be-42af-9721-f3609bea8cfc', encoding='latin1', sep= ';')
csv = df.to_csv()
output_path = './data_clean/security.csv'

missing_count = df.isnull().sum()
missing_count
null_values = df[df.isnull().any(axis=1)]
df = df.dropna()
df['Code.région'] = df['Code.région'].astype(int)
df['annee'] = '20' + df['annee'].astype(str)
df = df.sort_values(by='Code.département')
df = df.rename(columns={'Code.département': 'Département'})

df.to_csv(output_path, index=False)
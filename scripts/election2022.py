#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/12591a2e-3735-4471-959b-69782eb0f62f')
csv = df.to_csv()
output_path = './data_clean/election2022.csv'

column_rm = ['prenom', 'libelle_departement']

df = df.drop(columns=column_rm)
df = df.loc[df['code_departement'] != 'fr_etranger']

correspondance_partis = {'nom': ['MACRON', 'LE PEN', 'MÉLENCHON', 'ZEMMOUR', 'JADOT', 'LASSALLE', 'PÉCRESSE','ROUSSEL', 'HIDALGO', 'DUPONT-AIGNAN', 'POUTOU', 'ARTHAUD', 'abstentions', 'blancs', 'nuls'],
                         'parti_politique': ['LREM', 'RN', 'LFI', 'Reconuête', 'EELV', 'Résistons', 'LR', 'PCF', 'PS', 'DLF', 'NPA', 'LO', 'abstentions','blancs', 'nuls' ]}

df_correspondance = pd.DataFrame(correspondance_partis)

df = pd.merge(df, df_correspondance, on='nom', how='left')
df = df.drop('nom', axis=1)
df.drop(df[(df['code_departement'] == '986') | (df['code_departement'] == '987') | (df['code_departement'] == '988') | (df['code_departement'] == '989')].index, inplace=True)

df.to_csv(output_path, index=False)
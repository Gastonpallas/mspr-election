#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/12591a2e-3735-4471-959b-69782eb0f62f')
csv = df.to_csv()
output_path = './data_clean/election2022.csv'

column_rm = ['prenom', 'libelle_departement']

df = df.drop(columns=column_rm)
df = df.loc[df['code_departement'] != 'fr_etranger']
df.to_csv(output_path, index=False)
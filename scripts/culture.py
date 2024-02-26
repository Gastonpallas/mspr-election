#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('./data_raw/base-des-lieux-et-des-equipements-culturels.csv', sep=';', low_memory=False)
column = ['n_departement', 'type_equipement_ou_lieu','fonction_1']
df = df[column]
result = df.groupby(['n_departement', 'type_equipement_ou_lieu', 'fonction_1']).size().reset_index(name='nombre')
output_path = './data_clean/culture.csv'
result.to_csv(output_path, index=False)
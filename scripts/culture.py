#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('./data_raw/base-des-lieux-et-des-equipements-culturels.csv', sep=';', low_memory=False)
column = ['n_departement', 'type_equipement_ou_lieu','fonction_1']
df = df[column]
output_path = './data_clean/culture.csv'
df.to_csv(output_path, index=False)
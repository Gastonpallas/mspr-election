#!/usr/bin/env python3

import pandas as pd

df = pd.read_excel('./data_raw/age.xlsx')

column = ['ZONE', 'SEXE', 'TRAGE', 'POP_2022']
df = df[column]

output_path = './data_clean/age.csv'
df.to_csv(output_path, index=False)
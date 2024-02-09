#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/db89a4c3-18b5-4c3a-bffc-d69cbc507997')

csv = df.to_csv()
output_path = './data_clean/election2017.csv'

column_rm = ['Inscrits', 'Abstentions_ins', 'Votants_ins', 'Blancs_ins', 'Blancs_vot', 'Nuls_ins', 'Nuls_vot', 'Exprimés', 'Exprimés_ins', 'Exprimés_vot', 'LE PEN.ins', 'MACRON.ins', 'MÉLENCHON.ins', 'FILLON.ins', 'HAMON.ins', 'DUPONT-AIGNAN.ins', 'LASSALLE.ins', 'POUTOU.ins', 'ASSELINEAU.ins', 'ARTHAUD.ins', 'CHEMINADE.ins', 'LE PEN.exp', 'MACRON.exp', 'MÉLENCHON.exp', 'FILLON.exp', 'HAMON.exp', 'DUPONT-AIGNAN.exp', 'LASSALLE.exp', 'POUTOU.exp', 'ASSELINEAU.exp', 'ARTHAUD.exp', 'CHEMINADE.exp', 'Département', 'Votants']

df = df.drop(columns=column_rm)
df = pd.melt(df, id_vars=['CodeDépartement'], var_name='nom', value_name='votes')
df.columns = ['code_departement', 'nom', 'voix']
df.replace(to_replace='Abstentions', value='abstentions', inplace=True)
df.replace(to_replace='Blancs', value='blancs', inplace=True)
df.replace(to_replace='Nuls', value='nuls', inplace=True)
df.to_csv(output_path, index=False)
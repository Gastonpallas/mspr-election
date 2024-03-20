import pandas as pd

df = pd.read_csv('./data_clean/election2022.csv')
csv = df.to_csv()
output_path = './data_refactor/election2022.csv'

df = df.loc[df['code_departement'] != 'fr_etranger']

correspondance_partis = {
    'nom': ['MACRON', 'LE PEN', 'MÉLENCHON', 'ZEMMOUR', 'JADOT', 'LASSALLE', 'PÉCRESSE', 'ROUSSEL', 'HIDALGO', 'DUPONT-AIGNAN', 'POUTOU', 'ARTHAUD', 'abstentions', 'blancs', 'nuls'],
    'parti_politique': ['LREM', 'RN', 'LFI', 'Reconuête', 'EELV', 'Résistons', 'LR', 'PCF', 'PS', 'DLF', 'NPA', 'LO', 'abstentions', 'blancs', 'nuls']
}

df_correspondance = pd.DataFrame(correspondance_partis)
df = pd.merge(df, df_correspondance, on='nom', how='left')
df = df.drop('nom', axis=1)

df.drop(df[(df['code_departement'] == '986') | (df['code_departement'] == '987') | (df['code_departement'] == '988') | (df['code_departement'] == '989')].index, inplace=True)


df_pivot = df.pivot(index='code_departement', columns='parti_politique', values='voix').reset_index()

df_pivot.columns.name = None
df_pivot = df_pivot.rename_axis(None, axis=1)

df_pivot['gagnant'] = df_pivot[['LREM', 'RN', 'LFI', 'Reconuête', 'EELV', 'Résistons', 'LR', 'PCF', 'PS', 'DLF', 'NPA', 'LO']].idxmax(axis=1)

df_pivot.to_csv(output_path, index=False)

print(df_pivot)
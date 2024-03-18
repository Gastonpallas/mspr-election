import pandas as pd
import warnings

df_chomage_entreprise_per_dep = pd.read_csv('./data_merge/chomage_entreprise_per_dep.csv', sep=';')
df_age = pd.read_csv('./data_clean/age.csv', sep=',')



# print(df_chomage_entreprise_per_dep.head())
# print(df_age.head())

array_type = df_age['TRAGE'].unique()

# df_chomage_entreprise_per_dep['array_type'] = array_type
# print(df_chomage_entreprise_per_dep.head())

for i in array_type:
    df_chomage_entreprise_per_dep.insert(1, i, 0)
    
for i in df_age.iterrows():
    for j in df_chomage_entreprise_per_dep.iterrows():
        # print('[%s] & [%s]' % (i[1]['ZONE'], j[1]['Département']))
        if (i[1]['ZONE'].strip()) == j[1]['Département'].strip():
            # print("TEST")
            for k in array_type:
                print(df_chomage_entreprise_per_dep[j][1].iloc[k])
                # df_chomage_entreprise_per_dep[j][1][k] = i[1]['POP_2022']
        # if (i[1]['ZONE']) == j[1]['Département']:
        #     print("TEST")
            # for k in array_type:
            #     df_chomage_entreprise_per_dep[j][1][k] = i[1]['POP_2022']

print(df_chomage_entreprise_per_dep.head())
# for row in df_chomage_entreprise_per_dep.iterrows():
#     print(row)
#     for i in array_type:
#         row[i] = df_age[(df_age['ZONE'] == row['Département']) & (df_age['TRAGE'] == i)]['POP_2022'].values[0]
    #     print(df_age['ZONE'], row['Département'])
        # print(df_age[(df_age['ZONE'] == row['Département']) & (df_age['TRAGE'] == i)]['POP_2022'].values)
        # print(df_age[(df_age['ZONE'] == row['Département']) & (df_age['TRAGE'] == i)])
        # df_chomage_entreprise_per_dep.loc[index, i] = df_age[(df_age['ZONE'] == row['Département']) & (df_age['TRAGE'] == i)]['POP_2022'].values[0]
        
# print(df_chomage_entreprise_per_dep.head())
# df[df.columns[~df.columns.isin(['Libellé', '1982-T2'])]]
# df = df[df['Libellé'] != 'Codes']

# df_mean = df[['Libellé', '2022-T1','2022-T2', '2022-T3', '2022-T4']]
# df_mean = df_mean[:-4]
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     df_mean.loc[:, -1] = df_mean.loc[:, '2022-T1'].astype(float)
#     df_mean.loc[:, -2] = df_mean.loc[:, '2022-T2'].astype(float)
#     df_mean.loc[:, -3] = df_mean.loc[:, '2022-T3'].astype(float)
#     df_mean.loc[:, -4] = df_mean.loc[:, '2022-T4'].astype(float)
#     df_mean['2022'] = df_mean.mean(axis=1)
#     df_mean= df_mean[['Libellé', '2022']]
#     df_mean = df_mean[~df_mean['Libellé'].str.contains('région')]
#     df_mean['Libellé'] = df_mean['Libellé'].str.replace('Taux de chômage localisé par département - ', '')
#     df_sorted = df_mean.sort_values(by='Libellé', ascending=True)

# df_sorted = df_sorted.rename(columns={'2022': 'Taux de chômage'})
df_chomage_entreprise_per_dep.to_csv('./test.csv', index=False)
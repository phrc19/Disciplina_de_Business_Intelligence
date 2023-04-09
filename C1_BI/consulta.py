import pandas as pd
import numpy as np
import sqlite3

df = pd.read_csv('MICRODADOS.csv', sep=";", encoding='latin1')

#Criando um DataFrame para cada tabela de dimensão

df_dim1 = df[['Municipio']].drop_duplicates().reset_index(drop=True)
df_dim2 = df[['ViagemBrasil']].drop_duplicates().reset_index(drop=True)
df_dim3 = df[['ViagemInternacional']].drop_duplicates().reset_index(drop=True)
df_dim4 = df[['Sexo']].drop_duplicates().reset_index(drop=True)
df_dim5 = df[['ComorbidadeTabagismo']].drop_duplicates().reset_index(drop=True)
df_dim6 = df[['ComorbidadeCardio']].drop_duplicates().reset_index(drop=True)
df_dim7 = df[['ComorbidadeRenal']].drop_duplicates().reset_index(drop=True)
df_dim8 = df[['ComorbidadeObesidade']].drop_duplicates().reset_index(drop=True)
df_dim9 = df[['ComorbidadeDiabetes']].drop_duplicates().reset_index(drop=True)


#Criando uma nova coluna em cada DataFrame de dimensão para armazenar a chave primária

df_dim1['id_dim1'] = df_dim1.index + 1
df_dim2['id_dim2'] = df_dim2.index + 1
df_dim3['id_dim3'] = df_dim3.index + 1
df_dim4['id_dim4'] = df_dim4.index + 1
df_dim5['id_dim5'] = df_dim5.index + 1
df_dim6['id_dim6'] = df_dim6.index + 1
df_dim7['id_dim7'] = df_dim7.index + 1
df_dim8['id_dim8'] = df_dim8.index + 1
df_dim9['id_dim9'] = df_dim9.index + 1

#Criando uma nova coluna no DataFrame principal para cada chave estrangeira

#Dimenssão 1
df['id_dim1'] = df['Municipio'].map(df_dim1.set_index('Municipio')['id_dim1'])

#Dimenssão 2

df['id_dim2'] = df['ViagemBrasil'].map(df_dim2.set_index('ViagemBrasil')['id_dim2'])

#Dimenssão 3
df['id_dim3'] = df['ViagemInternacional'].map(df_dim3.set_index('ViagemInternacional')['id_dim3'])

#Dimenssão 4
df['id_dim4'] = df['Sexo'].map(df_dim4.set_index('Sexo')['id_dim4'])

#Dimenssão 5

df['id_dim5'] = df['ComorbidadeTabagismo'].map(df_dim5.set_index('ComorbidadeTabagismo')['id_dim5'])

#Dimenssão 6

df['id_dim6'] = df['ComorbidadeCardio'].map(df_dim6.set_index('ComorbidadeCardio')['id_dim6'])

#Dimenssão 7

df['id_dim7'] = df['ComorbidadeRenal'].map(df_dim7.set_index('ComorbidadeRenal')['id_dim7'])

#Dimenssão 8

df['id_dim8'] = df['ComorbidadeObesidade'].map(df_dim8.set_index('ComorbidadeObesidade')['id_dim8'])

#Dimenssão 9

df['id_dim9'] = df['ComorbidadeDiabetes'].map(df_dim9.set_index('ComorbidadeDiabetes')['id_dim9'])


#Removendo as colunas de dimensão do DataFrame principal

df = df.drop(['Municipio', 'ViagemBrasil', 'ViagemInternacional', 'Sexo', 'ComorbidadeTabagismo', 'ComorbidadeCardio', 'ComorbidadeRenal','ComorbidadeObesidade', 'ComorbidadeDiabetes'], axis=1)




con = sqlite3.connect('MICRODADO.db')

df.to_sql('fato_dados', con, if_exists='replace', index=False)
df_dim1.to_sql('dim_municipio', con, if_exists='replace', index=False)
df_dim2.to_sql('dim_viagembr', con, if_exists='replace', index=False)
df_dim3.to_sql('dim_viagemExt', con, if_exists='replace', index=False)
df_dim4.to_sql('dim_sexo', con, if_exists='replace', index=False)
df_dim5.to_sql('dim_ComorbT', con, if_exists='replace', index=False)
df_dim6.to_sql('dim_ComorbC', con, if_exists='replace', index=False)
df_dim7.to_sql('dim_ComorbR', con, if_exists='replace', index=False)
df_dim8.to_sql('dim_ComorbO', con, if_exists='replace', index=False)
df_dim9.to_sql('dim_comorbD', con, if_exists='replace', index=False)

con.close()
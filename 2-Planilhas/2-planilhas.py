import pandas as pd

# Lendo planilhas
df1 = pd.read_excel('./2-vendas-loja1.xlsx', sheet_name='Vendas')
df2 = pd.read_excel('./2-vendas-loja2.xlsx', sheet_name='Vendas')

# Concatenando DataFrames
df = pd.concat([df1, df2])

# Amostras aleatórias
# print(df.sample(5))

# Alterar o tipo de dado
# df['Produto'] = df['Produto'].astype('object')

# Consultando linhas com valores faltantes (por coluna)
print(df.isnull().sum())

# ABORDAGENS PARA VALORES NULOS


# 1 - Substituindo os valores nulos por 0 (Parametro inplace substitui o armazenamento do objeto na memória)
# df['Quantidade'].fillna(0, inplace=True)
# df['Valor'].fillna(0, inplace=True)
# print(df.isnull().sum())

# 2 - Substituindo os valores nulos por 0 (Parametro inplace substitui o armazenamento do objeto na memória)
# df['Quantidade'].fillna(df['Quantidade'].mean(), inplace=True)
# df['Valor'].fillna(df['Valor'].mean(), inplace=True)
# print(df.isnull().sum())

# 3 - Apagar valores nulos
# df.dropna(inplace=True)
# print(df.isnull().sum())

# 4 - Apagar linhas com valores nulos com base apenas em 1 coluna
# df.dropna(subset=['Quantidade'], inplace=True)

# 5 - Apagar linhas com valores nulos em todas as colunas
# df.dropna(how=all, inplace=True)
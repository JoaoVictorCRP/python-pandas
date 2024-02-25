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
# print(df.isnull().sum())

# ABORDAGENS PARA VALORES NULOS


# 1 - Substituindo os valores nulos por 0 (Parametro inplace substitui o armazenamento do objeto na memória)
# df['Quantidade'].fillna(0, inplace=True)
# df['Receita'].fillna(0, inplace=True)
# print(df.isnull().sum())

# 2 - Substituindo os valores nulos por 0 (Parametro inplace substitui o armazenamento do objeto na memória)
# df['Quantidade'].fillna(df['Quantidade'].mean(), inplace=True)
# df['Valor'].fillna(df['Receita'].mean(), inplace=True)
# print(df.isnull().sum())

# 3 - Apagar valores nulos
# df.dropna(inplace=True)
# print(df.isnull().sum())

# 4 - Apagar linhas com valores nulos com base apenas em 1 coluna
# df.dropna(subset=['Quantidade'], inplace=True)

# 5 - Apagar linhas com valores nulos em todas as colunas
# df.dropna(how=all, inplace=True)

# Criando novas colunas
df['Ticket Médio'] = df['Receita']/df['Quantidade']

# Retornando a maior receita
# print(df['Receita'].max())

# Com o metódo acima, apenas o valor máximo é retornado, porém não nos é dado o produto a qual o valor pertence.
# Para ver a linha completa utilize:
# print(df.nlargest(3, 'Receita')) # (3 primeiras linhas)

# Vendo as menores receitas:
# print(df.nsmallest(3, 'Receita'))

# Agrupamento por produto
# print(df.groupby('Produto')['Receita'].sum())

# Ordenando o conjunto de dados
ordenado = df.sort_values('Receita', ascending=False)
print(ordenado.head(10))
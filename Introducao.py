import pandas as pd

# Lendo dataset (População mundial por país, de 1800 até 2100)
df = pd.read_csv('./gapminder-pop.csv')

# Renomear Coluna
df = df.rename(columns={'country':'País'})

# Lendo as 5 primeiras linhas
# print(df.head(10))

# Total de linhas e colunas
# print(df.shape[0])

# Nome das colunas
# print(df.columns)

# Tipo de dado em cada coluna
print(df.dtypes)
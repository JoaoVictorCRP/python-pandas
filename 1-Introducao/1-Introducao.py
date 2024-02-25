import pandas as pd

# Lendo dataset 
df = pd.read_csv('./1-gapminder-pop.csv')

# Renomear Coluna
df = df.rename(columns={
    'country':'País', 
    'continent':'Continente',
    'year':'Ano',
    'lifeExp':'Expectativa de Vida',
    'pop':'População', 
    'gdpPercap':'PIB per Capita'
})

# Lendo as 5 primeiras linhas
# print(df.head())

# Lendo as 5 últimas linhas
# print(df.tail())

# Total de linhas e colunas
# print(df.shape)

# Nome das colunas
# print(df.columns)

# Tipo de dado em cada coluna
# print(df.dtypes)

# Informações estatísiticas da tabela
# print(df.describe())

# Filtrando a  tabela
# print(df['País'].unique())

# Aplicando filtros e colocando em uma variável
# dados_brasil = df.loc[df['País'] == 'Germany']
# print(dados_brasil)

# Agrupando dados ( Group By)
# agrupado_continentes = df.groupby('Continente')['País'].nunique()
# print(agrupado_continentes)

# Expectativa de vida média, agrupada por ano
# expec_vida_media_por_ano = df.groupby('Ano')['Expectativa de Vida'].mean()
# print(expec_vida_media_por_ano)

# PIB Global (PIB somado)
# pib_global = df['PIB per Capita'].sum()
# print(pib_global)
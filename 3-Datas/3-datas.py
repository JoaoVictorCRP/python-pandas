import pandas as pd

# Lendo dados
df = pd.read_excel('./3-vendas.xlsx')

# Passando a coluna de data para o tipo inteiro (Suponhamos que o pandas tenha reconhecido a coluna Data como inteiro)
df['Data'] = df['Data'].astype('int64')

# Verificando os tipos
# print(df.dtypes)

# Transformando coluna de data em data novamente
df['Data'] = pd.to_datetime(df['Data'])

# Adicionando coluna de faturamento
df['Faturamento'] = df['Preço'] * df['Quantidade']

# Agrupamentos
# faturamento_anual = df.groupby(df['Data'].dt.year)['Faturamento'].sum()
# print(faturamento_anual)

# Criando uma nova coluna com o ano da venda
# df['Ano_Venda'] = df['Data'].dt.year

# Extraindo mês e dia
# df['Mes_Venda'], df['dia_venda'] = (df['Data'].dt.month, df['Data'].dt.day) # Desestruturação!
# print(df.sample(4))

# Retornando a data mais antiga
# print(df['Data'].min())

# Calculando a diferença0 de dias (Nesse caso, a partir da menor data)
df['Diferenca_Dias'] = df['Data'] - df['Data'].min()

# Criando a coluna de trimestre
df['Trimestre_Venda'] = df['Data'].dt.quarter
# print(df.sample(3))

# Filtrando as vendas de 2019 no mês de março
vendas_marco_19 = df.loc[(df['Data'].dt.year == 2019) & (df['Data'].dt.month == 3)]
print(vendas_marco_19)

faturamento_por_estado = df.groupby(['Estado'])['Faturamento'].sum()
print(faturamento_por_estado)
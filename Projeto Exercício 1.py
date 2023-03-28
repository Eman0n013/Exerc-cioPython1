import pandas as pd

# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada


# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        Vendedor = tabela_vendas.loc[(tabela_vendas['Vendas'] > 55000), 'Vendedor'].values[0]
        Vendas = tabela_vendas.loc[(tabela_vendas['Vendas'] > 55000), 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {Vendedor}, Vendas: {Vendas}')








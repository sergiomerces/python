import pandas as pd

# criar um dicionário com nomes e idades
dados = {
    'Nome': ['Alice', 'Bon', 'Carol', 'David', 'Eve'],
    'Idade': [25, 30, 22, 35, 28]
}

# cria uma série a partir do dicionário
serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])

# exibir a série de idades
print('Série de idades: ')
print(serie_idades)

# calcular a média das idades
media_idades = serie_idades.mean()

print('\nMédia das Idades: ', media_idades)
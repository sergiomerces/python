import pandas as pd

dados = {
    'Produto': ['A', 'B', 'C'],
    'qtde_vendida': [33, 50, 45]
}

df = pd.DataFrame(dados)
df.plot(x='Produto', y='qtde_vendida', kind='bar')
df.plot(x='Produto', y='qtde_vendida', kind='pie')
df.plot(x='Produto', y='qtde_vendida', kind='line')
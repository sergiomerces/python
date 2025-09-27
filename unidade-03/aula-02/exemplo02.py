import pandas as pd

# criando um dicionário com pares chave-valor
data = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

# criando uma Series a partir do dicionário
series2 = pd.Series(data)

print(series2)
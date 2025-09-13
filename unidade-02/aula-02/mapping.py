# exemplo 1 - criação de um dicionario vazio seguido de atribuição
dici_1 = {}
dici_1['nome'] = 'Maria'
dici_1['idade'] = 25

# exemplo 2 - criação de um dicionário com par de chave e valor
dici_2 = {'nome': 'Maria', 'idade': 25}

# exemplo 3 - criação de um dicionário com uma lista de tuplas representandopares chave e valor
dici_3 = dict([('nome', 'Maria'), ('idade', 25)])

# exemplo 4 - criação de um dicionário usando a funçaõ built-in zip() e duas listas
dici_4 = dict(zip(['nome', 'idade'], ['Maria', 25]))

# teste se todas as construções são objetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4)
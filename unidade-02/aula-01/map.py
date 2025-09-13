preco_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25

preco_em_reais = list(map(lambda x: x * taxa_de_cambio, preco_em_dolares))

print(preco_em_dolares)
print(preco_em_reais)
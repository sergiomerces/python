set1 = {'a', 'b', 'c'}
print(set1)


# usando construtor set()
meu_conjunto = set()

# adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

print(meu_conjunto)

#removendo elemento
meu_conjunto.remove(20)

print(meu_conjunto)


# verificando se um elemento está no conjunto
elemento = 10

if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto")
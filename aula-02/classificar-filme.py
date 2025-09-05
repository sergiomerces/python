filmes = [
    "O Senhor dos Anéis",
    "Harry Potter",
    "Percy Jackson",
    "Piratas do Caribe",
    "Crepúsculo"
]

print()
print()
print()

for filme in filmes:
    classificacao = int(input(f"\nDigite a nota de 1 a 5 para {filme} ou zero para sair: "))

while True:

    if classificacao == 0:
        print(f"\n{filme} interrompido")
        break
    elif classificacao < 1 or classificacao > 5:
        print()
    else:
        print(f"\n{filme} com {classificacao} estrela(s)")
        break
print()
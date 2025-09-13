cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa']

for cor in cores:
    print(cor)

for cor in cores: 
    print(f"Posicao: {cores.index(cor)}, cor: {cor}")


linguagens = ['Python', 'Java', 'Javascript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']

print("\nAntes da listcomp = ", linguagens)

#  .lower() converte todo texto para letras minúsculas
linguagens = [item.lower() for item in linguagens]

print("Depois da listcomp ", linguagens)

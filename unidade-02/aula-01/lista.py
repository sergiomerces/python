cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa']

for cor in cores:
    print(cor)

linguagens = ['Python', 'Java', 'Javascript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']

print("\nAntes da listcomp = ", linguagens)
linguagens = [item.lower() for item in linguagens]
print("Depois da listcomp ", linguagens)

nota_01 = int(input("Digite a nota 1: "))
nota_02 = int(input("Digite a nota 2: "))
nota_03= int(input("Digite a nota 3: "))
nota_04= int(input("Digite a nota 4: "))

media = (nota_01 + nota_02 + nota_03 + nota_04) / 4

if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "reprovado"

print(f"A média das notas é {media}\n Você foi {situacao}")
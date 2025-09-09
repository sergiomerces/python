# 1. capturar notas dos alunos
# 2. armazenar notas numa lista
# 3. calcular média das notas inseridas
# 4. aprovar se a média for maior que 7
# 5. exibir notas, média e a situação do aluno

notas = []

for x in range(4):
    nota = float(input("Digite as notas do aluno: "))
    notas.append(nota)


def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def informar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

arredondar_media = lambda media: round(media, 2)

media = calcular_media(notas) 
media_arredondada = arredondar_media(media)
situacao = informar_situacao(media)

print(f"Notas do aluno: {notas}")
print(f"A média é: {media}")
print(f"A média arredondada: {media_arredondada}")
print(f"O aluno está: {situacao}")
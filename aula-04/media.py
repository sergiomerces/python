notas = [8.0, 7.5, 6.5, 9.75]

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

print(notas)
print(f"A média é: {media}")
print(f"A média arredondada: {media_arredondada}")
print(f"O aluno está: {situacao}")


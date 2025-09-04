print("\n\n## Bem-vindo(a) à Máquina de Venda Automàtica de Ingressos ##")

idade = int(input("\n\nInforme sua idade para receber uma recomendação: "))

if idade < 12:
    print("\nRecomendo o filme infantil Elio!")
elif 12 <= idade <= 18:
    print("\nRecomendo o filme Quarteto Fantástico!")
else:
    print("\nRecomendo o filme O Poderoso Chefão!")

ingressos = 10

if ingressos > 0:
    print("\nIngressos estão disponíveis. Divirta-se no cinema\n\n")
else:
    print("\nDesculpe, todos os ingressos estão esgotados para hoje!\n\n")
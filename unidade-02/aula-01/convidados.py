# tupla de convidados
convidados = ('Alice', 'Bob', 'Carol', 'Davi', 'Eve')

# lista de confirmações
confirmados = ['Bob', 'David']

# identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

#exibir os convidados que ainda não confirmaram
print('Convidados que ainda não confirmaram')

for pessoa in nao_confirmados:
    print(pessoa)

# enviar lembretes aos não confirmados
print("\nEnviando lembrete para os convidados que ainda não confirmaram.")
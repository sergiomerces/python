numero = int(input("\nDigite um número ou 0 para sair: "))

while numero != 0:
    if numero % 2 == 0:
        print(f"\nO número {numero} é par")
        break
    else:
        print(f"\nO número {numero} é ímpar")
        break

#o break força a saído do bloco de código e continua executando o algoritmo
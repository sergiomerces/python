# 1. solicitar valor do produto
# 2. solicitar o percentual de desconto
# 3. verificar se o percentual de desconto está no limite (0 a 100%)

print("###############################################################################\n")
print("                           CALCULADORA DE DESCONTO                             ")
print("\n###############################################################################\n")

valor_produto = float(input("Valor do Produto R$: "))
percentual_desconto = float(input("Percentual de Desconto  %: "))

while percentual_desconto <= 0 or percentual_desconto > 100:
    percentual_desconto = float(input("Informe um valor valido em %: "))
    
desconto = lambda preco, percentual: preco * (percentual/100)
valor_produto = round(valor_produto, 2)
percentual_desconto = round(percentual_desconto, 2)
valor_do_desconto = desconto(valor_produto, percentual_desconto)
valor_do_desconto = round(valor_do_desconto, 2)
valor_a_pagar = valor_produto - valor_do_desconto

print(f"\nValor do Produto: R$ {valor_produto}")
print(f"Percentual de Desconto: {percentual_desconto} %")
print(f"Valor do Desconto: R$ {valor_do_desconto}")
print(f"\nValor a Pagar: R$ {valor_a_pagar}\n")


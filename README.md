# Python

## Introdução

- criada por Guido Van Rossun em 1991
- linguagem de alto nível
- linguagem orientada a objetos
- leitura fácil e sintaxe simples
- desenvolvimento web, automação, aprendizado de máquina e análise de dados
- PEP8
  - indentação com 4 espaços (não tabulações)
  - uso de nomes descritivos minúsculos para variáveis minha_variavel
    uso de letras maiúsculas separadas por sublinhado para nomes de classes MINHA_CLASSE
  - comprimento de linha de código com 79 caracteres
    importações organizadas em forma ordenada e agrupada em seções
- linguagem interpretada
- linguagem open source
- tipagem dinâmica

## Ambientes de Desenvolvimento

### IDES

**PyCharm** - da JetBrains

**Visual Studio Code** da Microsoft

**Jupyter Notebook**

**Google Collab**

## Saída de dados

Usamos o comando **print("string")**

```
#linha de comentário
print("hello world")
```

## Variáveis

A declaração de variáveis é detipagem dinâmica, basta digitar um nome para a variável e atribuir um valor usando o sinal de (=) igual.

```
x = 10
nome = "Sérgio"
nota = 8.75
fez_inscricao = True
```

Para verificar o tipo de dado de uma variável usamos o comando **type(variavel)**

```
print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_incricao))
```

O interpretador Python consegue estabelecer o tipo de dado da variável observando seu valor e contexto.

## Formatadores de caracteres de saída

Quando imprimimos strings e variáveis ao mesmo tempo podemos usar um **token** do tipo de dado na sentença e ao final a variável que fará a substituição.

```
print("\nOlá %s bem vindo à disciplina de programação.\nParabéns pelo seu primeiro hello world\n" %(nome))
```

## F-String

Podemos formatar a saída de tela com string e variáveis ao mesmo tempo usando o comando **f** antes do conteúdo a ser impresso e o nome das variáveis entre chaves nas posições em que aparecerão seus valores.

```
print(f"\nOla {nome} bem-vindo à disciplinade programação.\nParabéns pelo seu primeiro hello world\n")
```

## Captura de dado de usuário

Usamos o comando **input("string")**

```
nota_do_aluno = int(input("Digite a nota do aluno: "))

print(f"A nota do aluno é {nota_do_aluno}")
```

## Condicional if-else

Primeiro testamos uma condição lógica que retorna o valor booleano verdadeiro ou falso e depois executa o bloco de código correspondente.

```
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
```

## Operadores relacionais

Eles permitem avaliar as relações entre valore, respondendo à perguntas. A estrutura condicional guia a tomada de decisões na execução do algoritmo.

(< ) estritamente menor que

(<=) menor ou igual

(.>) estritamente maior que

(.>=) maior ou igual que

(==) igual

(!=) diferente

(is) identidade do objeto

(is not) negação da identidade do objeto

## Estruturas lógicas

São como peças de quebra-cabeça que unem condições para critérios mais complexos. São elas que nos permitem tomar decisões mais elaboradas, combinando várias comparações.

E (and)

OU (or)

NÃO (not)

## Operadores booleanos

São essenciais para a criação de estruturas sofisticadas permitindo que os programas lidem com uma variedade de situações e critérios lógicos.

Eles são usados para controlar o fluxo de execução com base em condições complexas.

```
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
```

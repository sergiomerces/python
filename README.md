# Python

## Introdução

- criada por Guido Van Rossun em 1991
- linguagem de alto nível
- linguagem orientada a objetos
- leitura fácil e sintaxe simples
- desenvolvimento web, automação, aprendizado de máquina e análise de dados
- PEP8
  - indentação com 4 espaços (não tabulações)
  - uso de nomes descritivos minúsculos para variáveis minha_variavel (notação snake case)
    uso de letras maiúsculas separadas por sublinhado para nomes de classes MINHA_CLASSE
  - comprimento de linha de código com 79 caracteres
    importações organizadas em forma ordenada e agrupada em seções
- linguagem interpretada
- linguagem open source
- tipagem dinâmica

## Ambientes de Desenvolvimento

### IDES

**PyCharm** - da JetBrains
Para instalar acessar a página da JetBrains baixar a versão mais compatível com sua
distro, estou usando o PopOS! LTS 22.04; logo optei pela versão do PyCharm Community 2022.3.3
Descompactar para o diretório /opt.

```
$ sudo tar xzf pycharm-*.tar.gz -C /opt/
$ cd /opt/
# acessar o diretório do Pycharm
$ cd bin/
$ sh pycharm

```

**Visual Studio Code** da Microsoft
Instalação
Extensões:

- Python
- Pylance
- Python Debugger
- Python Enviroments

Todas da Microsoft.

Opções online:

- **Jupyter Notebook**

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

## elif

Seu uso propicia:

1. Avaliação em sequência
2. Verificação múltipla
3. Flexibilidade

> Na programação, a criação de algortimos pararesolver problemas envolve a capacidade de tomar decisões. Tais decisões são guiadas por uma técnica chama "estrutura condicional" (Manzano; Oliveira, 2019).

## Estruturas de repetição

- estrutura de repetição for
- estrutura de repetição while
- controle de fluxo de repetição range, break e continue

## for

Permite percorrer uma sequência de elementos, como uma lista e executar ações para cada item.

Permite realizar ações repetitivas de maneira controlada.

É especialmente útil quando sabemos previuamente quantas vezes repetir uma ação ou quando temos uma lista de itens a serem processados.

```
numeros = [1, 2, 3, 4, 5]

for num in numeros:
    print(num)
```

## while

Para ter controle das repetições ou ter uma condição atendida o while permite tal controle.

É usado para criar estruturas de repetição quando o número de repetições não é conhecido antecipadamente. A execução de continuar até uma condição específica ser atendida.

```
numero = int(input("\nDigite um número ou 0 para sair: "))

while numero != 0:
    if numero % 2 == 0:
        print(f"\nO número {numero} é par")
        break
    else:
        print(f"\nO número {numero} é ímpar")
        break

#o break força a saído do bloco de código e continua executando o algoritmo
```

## Controle de repetição range break e continue

A função **range()** é uma ferramenta útil para criar sequências numéricas que podem ser usadas em estruturas de repetição, com o comando **for**. Ela especifica os limitese o incremento da sequência.

### Método 1 - repetição por quantidade

```
# loop de repetição por quantidade

for x in range(5):
    print(x)

#não preciso de um array de números o interpretador entende o contexto do
#parâmetro
```

### Método 2 - limites inicial e superior

```
#loop com limite inicial e incremento

for y in range(2, 7):
    print(y)

#o início é sempre intervalo fechado (conta o número)
#o fim sempre intervalo aberto (não conta o número)
```

### Método 3 - com incremento

```
for z in range(1, 11, 2):
    print(z)

#primeiro indicador - início
#segundo indicado - limite
#terceiro indicador - incremento
```

## break

É usado para interromper a execução de uma estrutura de repetição quando uma condição é atendida. Esse comando permite sair do loop antes que ele seja concluído.

## continue

É usado para pular a iteração atual em uma estrutura de repetição e continuar co a próxima iteração. Isso é vantajoso quando se deseja ignorar uma iteração com base em uma condição, mas quer continuar com o restante do loop.

```
for numero in range (1, 11):
    if numero == 5:
        continue
    print(numero)

#ignora a posição de iteração
```

## Exercício

```
filmes = [
    "O Senhor dos Anéis",
    "Harry Potter",
    "Percy Jackson",
    "Piratas do Caribe",
    "Crepúsculo"
]

print()
print()
print()

for filme in filmes:
    classificacao = int(input(f"\nDigite a nota de 1 a 5
    para {filme} ou zero para sair: "))

while True:

    if classificacao == 0:
        print(f"\n{filme} interrompido")
        break
    elif classificacao < 1 or classificacao > 5:
        print()
    else:
        print(f"\n{filme} com {classificacao} estrela(s)")
        break
print()
```

Nessa solução, utilizamos **while True:**, que é uma técnica comum para criar loops em que a condição de parada pode variar ou não é conhecida, visto que o usuário pode parar a classifiucação escolhendo 0 ou encerrá-lo depois de classificar todos os cinco filmes.

## Funções em Python

### Funções built-in

São blocos de código pré-implementados e incorporados diretamente na linguagem, consitituindo um conjunto essencial de ferramentas que estão prontamente disponíveis para programadores.

O Python possui um repertório de 70 funções built-in (pré-construídas)

- print()
- input()
- int()
- range()

### Função len()

Calcula o comprimento de uma lista

```
# cria uma lista de números
numeros = [1, 2, 3, 4, 5]

# conta o comprimento da lista
numero_elementos = len(numeros)

# imprime a quantidade de elementos
print(numero_elementos)
```

### Função definida pelo usuário (com retorno de parâmetro)

As funções definidas pelo usuário são criadas pelo programador para atender requisitos específicos dentro de um programa.

```
# função soma
def soma(a, b):
    resultado = a + b
    return resultado

# função classificar número par
def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# chamando uma função
print(soma(3, 5))
print(e_par(100))

```

### Funções anônimas

Conhecidas como funções **lambda**, são declaradas sem a necessidade de um nome, permitindo que sejam definidas e utilizadas no local em que são necessárias.

São úteis para uma ação simples que será usada penas uma vez.

```
soma = lambda a, b: a + b
resultado = soma(3, 4)

print(resultado)
```

### Função round

Usada para fazer o arredondamento de casas decimais

```
numero = round(numero)
```

## Exercício

1. calcular a média
2. arredondar a média
3. informar se foi aprovado ou reprovado

```

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

```

## Estruturas de Dados em Python

### Objetos do tipo sequência

Sequências são estruturas de dados que nos permitem armazenar coleções ordenadas de informações.

- coleções são versáteis podem incluir elementos de tipos diferentes
- organizam dados em ordem específica
- são indexados por números inteiros positivos
- primeiro índice da sequência acessado pleo indice zero (0)

## Operações comuns com sequências

**x in s** True caso um item de s seja igual a x

**s + t** concatenação de s e t

**n \* s** adiciona s a si mesmo n vezes (multiplicação)

**s[i]** acessa o valor guardado na posição i da sequência

**s[i:j]** acessa os valores da posição de i até j

**s[i:j:k]** acessa valores da posição i até j, com passo k

**len(s)** comprimento de s

**min(s)** menor valor de s

**max(s)** maior valor de s

\*\*s.count(x)\*\* número total de ocorrências de x em s

Um texto é representado por objetos da classe string, pode ser manipulado por diversas das operações vistas, porém uma string é imutável.

```
texto = "Explorando a diversidade de linguagens de programação com Python."

# imprime o tamanho da string
print(f"O tamanho do texto é = {len(texto)}")

# retorna se o termo Python faz parte do texto
print(f"Python in texto = {'Python' in texto}")

# retorna quantidade de letras 'e' no texto
print(f"Quantidade de 'e' no texto = {texto.count('e')}")

# retorna os 5 primeiros caracteres do texto
print(f"As 5 primeiras letras são = {texto[:5]}")

```

## Listas

- forma fundamental de objetos do tipo sequência
- são mutáveis, podemos adcionar, remover e alterar elementos

Lista de cores:

```
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa']

for cor in cores:
    print(cor)

for cor in cores:
    # cores.index acessa o índice de cada cor do laço
    print(f"Posicao: {cores.index(cor)}, cor: {cor}")

```

Lista de linguagens:

```
linguagens = ['Python', 'Java', 'Javascript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']

print("\nAntes da listcomp = ", linguagens)

#  .lower() converte todo texto para letras minúsculas
linguagens = [item.lower() for item in linguagens]

print("Depois da listcomp ", linguagens)
```

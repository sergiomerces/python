# importar biblioteca matplotlib
import matplotlib.pyplot as plt

# cria a classe Livros
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.titulo} por {self.autor} * {self.genero} * {self.quantidade} unidades"


# cria lista para receber os livros
estante = []


# cria função para cadastrar livros
def cadastrar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)
    estante.append(novo_livro)
    print(f"O livro {titulo} foi cadastrado com sucesso!")


# função para listar todos os livros
def listar_livros():
    print("\nLivros na estante:")
    for livro in estante:
        print(livro)


#   Busca um livro na estante pelo título, de forma case-insensitive.
#   Retorna o objeto Livro se encontrado, ou None caso contrário.
def buscar_livro_por_titulo(titulo_busca):
    titulo_normalizado = titulo_busca.casefold()

    livro_encontrado = next(
        (livro for livro in estante if livro.titulo.casefold() == titulo_normalizado),
        None
    )
    return livro_encontrado


# adicionar livros à estante
cadastrar_livro('Harry Potter e a Pedra Filosofal', 'J. K. Rowlling', 'fantasia', 35)
cadastrar_livro('Percy Jackson e o Ladrão de Raios', 'Rick Hyodan', 'fantasia', 23)
cadastrar_livro('O Senhor dos Anéis - A Sociedade do Anel', 'J. R. R. Tolkien', 'fantasia', 19)

# listar os livros na estante
listar_livros()

# testes de uso da nova função de busca:
print("\n--- Testando a função de busca ---")

# teste 1: Título com correspondência exata
titulo_exato = 'Harry Potter e a Pedra Filosofal'
livro = buscar_livro_por_titulo(titulo_exato)
if livro:
    print(f"\nLivro encontrado: {livro}")
else:
    print(f"\nLivro '{titulo_exato}' não encontrado.")

# teste 2: Título com capitalização diferente
titulo_diferente = 'percy jackson e o ladrão de raios'
livro = buscar_livro_por_titulo(titulo_diferente)
if livro:
    print(f"\nLivro encontrado (busca case-insensitive): {livro}")
else:
    print(f"\nLivro '{titulo_diferente}' não encontrado.")

# teste 3: Título inexistente
titulo_inexistente = 'O Ladrão de Raios'
livro = buscar_livro_por_titulo(titulo_inexistente)
if livro is None:  # Verificação explícita para None
    print(f"\nLivro '{titulo_inexistente}' não encontrado. O retorno foi: {livro}")
else:
    print(f"\nLivro encontrado (busca inesperada): {livro}")



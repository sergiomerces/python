# corrigir código

# criar a classe livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

# criar um array vazio para receber os livros
livros = []

# cadastrar um novo livro
def cadastrar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(input('titulo, autor, genero, quantidade'))
    livros.append(novo_livro)
    print(f'{titulo} foi adicionado com sucesso!')
    return

# listar todos os livros
def listar_livros():
    print()
    for livro in livros:
        print(livro)
    return

# buscar livro
def buscar_livro():
    livro_procurado = input('Informe o título a ser buscado: ')
    livros_encontrados = []

    for livro in livros:
        if livro['titulo'] == livro_procurado:
            livros_encontrados.append(livro)
            print(livros_encontrados)
            return
        else:
            print('Desculpe, ainda não temos esse livro em nosso acervo!')
            return

def main():
    option = 9

    while option != 0:
        print('Menu: 1: Cadastrar | 2: Listar | 3: Buscar | 0: Sair')
        option = int(input())
        if option == 1:
            cadastrar_livro()
        elif option == 2:
            listar_livros()
        elif option == 3:
            buscar_livro()
        elif option == 0:
            print('Encerrar sistema...')
            break

print('BIBLIOTECA DIGITAL')
main()
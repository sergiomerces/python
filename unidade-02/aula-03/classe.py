# define uma classe chamada Pessoa
class Pessoa:
    # o método _init_ é um construtor, chamado  quando um objeto, da classe é criado
    # ele inicializa os atributos da classe
    # self é uma convenção que se refere à própria instância da classe
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    # o méto do cumprimentar retorna uma saudação com o nome da pessoa
    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}."
    
    # o método aniversário aumenta idade da pessoa em 1 ano
    def aniversario(self):
        self.idade += 1

# cria uma instância da classe Pessoa
pessoa1 = Pessoa('Sérgio', 46, 'masculino')

# chama o método cumprimentar na instância da pessoa1
print(pessoa1.cumprimentar())

#acessa o atributo idade da instância pessoas1
print(f"Idade: {pessoa1.idade}")

# chama o método aniversário
pessoa1.aniversario()

# acessa o atributo idade atualizado
print(f"Nova idade: {pessoa1.idade}")
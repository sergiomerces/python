# o valor __init__() é capaz de receber um valor diferente para cada objeto

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        return "Au au au au au"
    
class Gato(Animal):
    def fazer_barulho(self):
        return "Miau miau miau miau miau"
    
# criando objetos das classe filhas
rex = Cachorro('Rex')
whiskers = Gato('Whiskers')

# chamando método fazer_barulho
print(f"{rex.nome} faz: {rex.fazer_barulho()}")
print(f"{whiskers.nome} faz: {whiskers.fazer_barulho()}")
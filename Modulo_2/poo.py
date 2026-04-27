
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):        
        return "O animal faz um som."
    
    def andar(self):
        return f"{self.nome} está andando."
    
class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro late."
    
class Gato(Animal):
    def emitir_som(self):
        return "O gato mia."

pessoa1 = Pessoa("João", 30)
print(pessoa1.nome)  # Saída: João
print(pessoa1.saudacao())  # Saída: Olá, meu nome é João e tenho 30 anos.

animal1 = Animal("Rex")
print(animal1.emitir_som())  # Saída: O animal faz um som.
print(animal1.andar())  # Saída: Rex está andando.

cachorro1 = Cachorro("Buddy")
print(cachorro1.emitir_som())  # Saída: O cachorro late.
print(cachorro1.andar())  # Saída: Buddy está andando.

gato1 = Gato("Whiskers")
print(gato1.emitir_som())  # Saída: O gato mia.
print(gato1.andar())  # Saída: Whiskers está andando.

# Exemplo de abstração
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar():
        pass

    @abstractmethod
    def desligar():
        pass

class Carro(Veiculo):
    def __init__(self):
        super().__init__()

    def ligar(self):
        return "Carro ligado"
    
    def desligar(self):
        return "Carro desligado"


carro_verde = Carro()
print(carro_verde.ligar())
print(carro_verde.desligarligar())
class MinhaClasse:
    valor = 10
    def __init__(self, nome):
        self.nome = nome
    
    def metodo_instancia(self):
        print(f"O método de instância foi chamado para {self.nome}")

    @classmethod
    def metodo_classe(cls):
        print(f"O método da classe foi chamado e o valor = {cls.valor}")

    @staticmethod
    def metodo_estatico():
        print("O método estático foi chamado")

obj = MinhaClasse("Método de exemplo")
obj.metodo_instancia()

MinhaClasse.metodo_classe()
MinhaClasse.metodo_estatico()

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(", ")
        return cls(marca, modelo, int(ano))

configuracao = "Toyota, corola, 2022"
meu_carro = Carro.criar_carro(configuracao)
print(meu_carro.modelo)
print(meu_carro.marca)
print(meu_carro.ano)
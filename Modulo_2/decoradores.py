def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("A função foi chamada")
        
minha_funcao()

# Depurador em classe
class MeuDecoradorDeClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Antes do depurador de classe ser chamado")
        self.func()
        print("Depois do depurador de classe ser chamado")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("A função de classe foi chamada")

segunda_funcao()

# Exemplo de exceções

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"ValueError: Digite um número inteiro {e}")
    raise ValueError("Variavel incompativel")
except Exception as erro:
    print(f"Erro: {erro}")
else:
    print(f"O resultado da divisão de 10 por {numero} é {resultado}")
    print("Executado com sucesso")
finally:
    print("Sempre executa, mesmo dando certo ou errado")
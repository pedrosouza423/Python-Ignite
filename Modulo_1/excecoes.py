#Exemplo de exceção
numero = int(input("Digite um número: "))
try:
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
    raise print("Erro: Não é possível dividir por zero.")
except ValueError as e:
    print(f"Erro: Entrada inválida. Por favor, digite um número inteiro. Detalhes do erro: {e}")
    raise print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
else:
    print("O resultado é:", resultado)
finally:
    print("Programa finalizado.")
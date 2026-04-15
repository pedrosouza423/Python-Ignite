# Módulos
from math import sqrt
# Usando o módulo math para calcular a raiz quadrada
numero = int(input("Digite um número para calcular a raiz quadrada: "))
raiz_quadrada = sqrt(numero)
raiz_quadrada_formatada = "{:.2f}".format(raiz_quadrada)
print(f"A raiz quadrada de {numero} é {raiz_quadrada_formatada}")

from meu_modulo import saudacao, numero_par
saudacao_usuario = saudacao("Pedro")
print(saudacao_usuario)
numero = int(input("Digite um número para verificar se é par ou ímpar: "))
par_ou_impar = numero_par(numero)
print(par_ou_impar)
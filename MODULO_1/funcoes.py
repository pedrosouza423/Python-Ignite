# definindo funções para saldação
def saudacao():
    print('Olá, tudo bem?')

def saudacao_com_parametro(nome):
    print(f'Olá {nome}, tudo bem?')

def saudacao_com_parametro_e_retorno(nome):
    return f'Olá {nome}, tudo bem?'

# Função numero ao quadrado
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado(5))
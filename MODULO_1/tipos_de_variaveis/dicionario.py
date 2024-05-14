# Criando um dicionario
pessoa = {'nome': 'Pedro', 'idade': 25, 'cidade': 'São Paulo'}

print(pessoa)
print(pessoa['nome'])

pessoa['sobrenome'] = "Souza"
print(pessoa)

pessoa['idade'] = 22
print(pessoa)

# remover um item
del pessoa['sobrenome']
print(pessoa)

# keys
chaves = list(pessoa.keys())
print(chaves[0])

# values
valores = list(pessoa.values())
print(valores[0])

# items
itens = list(pessoa.items())
print(itens[0])
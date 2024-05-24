
lista = [1, 2, 3, 4, 5]

for i in lista:
    print(i)

pessoa = {"nome": "João", "idade": 20, "cidade": "São Paulo"}

for chave, valor in pessoa.items():
    print(chave, valor)

for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

# Do 0 ao 9
for i in range(10):
    print(i)

# Quebra de linha
print("\n")
lista = [1, 2, 3, 4, "JAVASCRIPT"]
for i in range(0, len(lista)):
    print(f"Indice: {i}")
    print(f"Elemento: {lista[i]}")

print("\n\n Enumerate")
lista_enumerate = ["a", "b", "c", "d", "e"]
for indice, valor in enumerate(lista_enumerate):
    print(f"Indice: {indice}")
    print(f"Valor: {valor}")
# Criando uma lista
frutas = ["maçã", "banana", "laranja"]

# append() - adiciona um elemento ao final
frutas.append("uva")

# insert() - adiciona em uma posição específica
frutas.insert(1, "morango")

# extend() - adiciona múltiplos elementos
frutas.extend(["abacaxi", "melancia"])

# remove() - remove a primeira ocorrência de um elemento
frutas.remove("banana")

# pop() - remove e retorna o elemento de uma posição
ultimo = frutas.pop()


# index() - retorna o índice de um elemento
indice = frutas.index("maçã")
print(indice)


# count() - conta quantas vezes um elemento aparece
quantidade = frutas.count("laranja")
print(quantidade)

# sort() - ordena a lista
print("Lista antes de ser ordenada:", frutas)
frutas.sort()
print("Lista depois de ser ordenada:", frutas)

# reverse() - inverte a ordem
frutas.reverse()
print("Lista depois de ser invertida:", frutas)
# clear() - limpa a lista
# frutas.clear()

# len() - retorna o tamanho
tamanho = len(frutas)

print(frutas)
print(ultimo)
print(f"Tamanho: {tamanho}")

minha_lista = [1, 2, 3, 4, 5]
print(minha_lista)
print(minha_lista[0])


print(minha_lista[1:3])
print(minha_lista[:3])
print(minha_lista[2:])

minha_lista.append(6)
print(minha_lista)

# remover o primeiro elemento com valor 3
minha_lista.remove(3)
print(minha_lista)

# insert
minha_lista.insert(3, 10)
print(minha_lista)

# pop -> remover o index 3
minha_lista.pop(3)
print(minha_lista)

# index -> mostra qual a posição do elemento
indice = minha_lista.index(4)
print(indice)

# sort -> ordena a lista
minha_lista.sort()
print(minha_lista)
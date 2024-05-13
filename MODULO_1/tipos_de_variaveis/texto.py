# Declaração
nome_completo = "Fulano de Tal"

nome_completo_aspas = """Fulano de 
Tal"""

nome_completo_qubra = "Fulano \
de Tal"

nome = "Fulano"
sobrenome = "de Tal"

# Formatação
nome_completo = nome + " " + sobrenome
print(nome_completo)

print("Nome completo: %s %s" % (nome, sobrenome))	

print("Nome completo: {} {}".format(nome, sobrenome))

print(f"Nome completo: {nome} {sobrenome}")

# Maiusculo e minusculo
print(nome_completo.upper())
print(nome_completo.lower())

# Contador (Quantas vezes aparece derminado caractere
print(nome_completo.count("a"))

# Procura (Em qual posição aparece determinado caractere)
print(nome_completo.find("a"))

# Transformar em byte
print(nome_completo.encode())

print(nome_completo.encode().decode())

# Replace
print(nome_completo.replace("Fulano", "Beltrano"))

# Join
print("-".join(nome))

# Split
print(nome_completo.split(" "))

# Strip ao final ou começo
nome = "xPedrox"
print(nome.strip("x"))
print(nome.rstrip("x"))


print(nome.startswith("x"))


print("Pedro" in nome)
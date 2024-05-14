# idade = 20
# Entrada de dados
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
elif idade < 0:
    print("Idade inválida.")
else:
    print("Você é menor de idade.")

# mensagem = "Você é maior de idade." if idade >= 18 else "Você é menor de idade."
# print(mensagem)
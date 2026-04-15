import requests

response = requests.get("https://api.github.com")
print(response.status_code)
nome = "Pedro"
nome_formatado = nome.lower()
print(nome_formatado)
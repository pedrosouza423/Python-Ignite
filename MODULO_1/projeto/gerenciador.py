def adicionar_tarefa(tarefas, nome_tarefa = "Tarefa padrão"):
    tarefas.append({"nome": nome_tarefa, "completa": False})
    print(f"A Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nTarefas:")
    for indice,tarefa in enumerate(tarefas, start=1):
       status = "✔" if tarefa['completa'] else " "
       print(f"{indice}. [{status}] {tarefa['nome']}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, nome_tarefa_novo):
    if indice_tarefa >= 1 and indice_tarefa <= len(tarefas):
        tarefas[indice_tarefa - 1]['nome'] = nome_tarefa_novo
        print(f"A tarefa {indice_tarefa} foi atualizada para {nome_tarefa_novo} com sucesso!")
    else:
        print(f"Índice inválido! A tarefa de índice {indice_tarefa} não existe.")

def completar_tarefa(tarefas, indice_tarefa):
    if indice_tarefa >= 1 and indice_tarefa <= len(tarefas):
        tarefas[indice_tarefa - 1]['completa'] = True
        print(f"A tarefa {indice_tarefa} foi completada com sucesso!")
    else:
        print(f"Índice inválido! A tarefa de índice {indice_tarefa} não existe.")
    
def remover_tarefas_completadas(tarefas):
    tarefas = [tarefa for tarefa in tarefas if not tarefa['completa']]
    print("Tarefas completadas removidas com sucesso!")
    return tarefas

# Lista de tarefas
tarefas = []

while True:
    print("\nMenu gerenciador de lista de tarefas")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Completar tarefa")
    print("5 - Remover tarefas completadas tarefa")
    print("6 - Sair")
    print("\n")
    escolha = int(input("Escolha a sua escolha: "))

    
    if escolha == 1:
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == 2:
        ver_tarefas(tarefas)
    elif escolha == 3:
        ver_tarefas(tarefas)
        indice_tarefa = int(input("\nDigite o índice da tarefa que deseja atualizar: "))
        nome_tarefa_novo = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, nome_tarefa_novo)
    elif escolha == 4:
        ver_tarefas(tarefas)
        indice_tarefa = int(input("\nDigite o índice da tarefa que deseja completar: "))
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == 5:
        tarefas = remover_tarefas_completadas(tarefas)
    elif escolha == 6:
        break

print("Fim do programa")

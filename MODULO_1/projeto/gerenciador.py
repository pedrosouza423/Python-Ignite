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

def atualizar_tarefa(tarefas, nome_tarefa):
    for tarefa in tarefas:
        if tarefa['nome'] == nome_tarefa:
            tarefa['completa'] = True
            print(f"A tarefa {nome_tarefa} foi atualizada com sucesso!")
            return
    print(f"A tarefa {nome_tarefa} não foi encontrada!")
    return

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
    elif escolha == 6:
        break

print("Fim do programa")

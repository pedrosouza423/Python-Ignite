tarefas = []

def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {
        "descricao": descricao,
        "completa": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada.")

def ver_tarefas():
    if tarefas:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            status = "X" if tarefa["completa"] else " "
            print(f"{i}.[{status}] {tarefa['descricao']}")
    else:
        print("Nenhuma tarefa encontrada.")

def atualizar_tarefa():
    ver_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
            if 0 <= indice < len(tarefas):
                nova_descricao = input("Digite a nova descrição da tarefa: ")
                tarefas[indice]["descricao"] = nova_descricao
                print("Tarefa atualizada.")
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def completar_tarefa():
    ver_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa que deseja completar: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice]["completa"] = True
                print("Tarefa marcada como completa.")
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def deletar_tarefas_completadas():
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if not tarefa["completa"]]
    print("Tarefas completadas deletadas.")

while True:
    print("\nGerenciador de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        print("Exibindo tarefas...")
        ver_tarefas()
    elif escolha == "3":
        atualizar_tarefa()
    elif escolha == "4":
        completar_tarefa()
    elif escolha == "5":
        deletar_tarefas_completadas()
    elif escolha == "6":
        print("Saindo do gerenciador de tarefas.")
        break
    else:
        print("Opção inválida. Tente novamente.")
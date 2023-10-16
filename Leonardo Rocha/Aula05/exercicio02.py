lista_tarefas = []

while (True):
    print ("Escolha uma opção: \n")
    print ("Opção 1: Adicionar uma tarefa a lista \n")
    print ("Opção 2: Excluir uma tarefa da lista \n")
    print ("Opção 3: Listar tarefas \n")
    print ("Opção 4: Sair do Programa \n")

    opcao = int(input())
    if (opcao == 1):
        tarefas = input("Digite a tarefa: ")
        lista_tarefas.append(tarefas)
        print (f"Você adicionou {tarefas} a tarefa")

    elif (opcao == 2):
        excluir_tarefas = input("Digite a tarefa que você deseja excluir: ")
        lista_tarefas.remove(excluir_tarefas)
        print (f"Você excluiu {excluir_tarefas} da tarefa")
    
    elif (opcao == 3):
        len(lista_tarefas)
        print ("A quantidade de tarefas é: ", lista_tarefas)

    else:
        print ("Você saiu do programa \n")
        break
agenda = [] 

while True: 
    print("1. Adicionar o contato a agenda \n")
    print("2. Verificar a agenda \n")
    print("3. Buscar na agenda \n")
    print("4. Sair")

    opccao = int(input())

    if (opccao == 1):
        nome = input("Adicione o contato a agenda: \n")
        telefone = int(input("Adicione o telefone do contato: \n"))
        dici = {'nome': nome,'telefone': telefone}
        agenda.append(dici)
        print(agenda)

    elif (opccao == 2):
        for i in agenda:
            print (i, '\n')

    elif (opccao == 3):
        busca = input("Buscar o contato na agenda: \n")

        for busca in agenda:
                print (busca)

    else:
         break
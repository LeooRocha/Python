'''num1 = 0
num2 = 0

def somar (num1, num2):
    return num1 + num2

def subtrair (num1, num2):
    return num1 - num2

def multipicar (num1, num2):
    return num1 * num2

def dividir (num1, num2):
    return num1 / num2'''

estoque = {}

def create (codigo, nome, quantidade):
    nome = input("Escreva o nome do produto: ")
    codigo = input("Escreva o código do produto: ")
    quantidade = input("Escreva a quantidade do produto: ")
    if codigo not in estoque:
        estoque [codigo] = {'nome' : nome, 'quantidade' : quantidade}

    else:
        print("O item já existe no estoque. Use a função atualizar_item para modificar a quantidade. ")

def upd (codigo, nome, quantidade):
    if codigo in estoque:
        estoque [codigo] ["quantidade"] =  quantidade

    else:
        print ("O item não existe no estoque. Use fução incluir_item para adiciona-lo")
        
def read (codigo, nome, quantidade):
    if codigo in estoque:
        for i in estoque:
            print (i, '\n')
    
    else:
        print ("O item não existe no estoque. Use fução incluir_item para adiciona-lo")

def delete (codigo, nome, quantidade):
    if codigo in estoque:
        del estoque ["codigo"] ["nome"] ["quantidade"]

    else:
        print ("O item não existe no estoque. Use fução incluir_item para adiciona-lo")

def menu():
    while (True): 
        print ("Escolha uma opção: \n")
        print ("Opção 1 : Adicionar um produto \n")
        print ("Opção 2: Ler um produto \n")
        print ("Opção 3: Atualizar o estoque \n")
        print ("Opção 4: Excluir um produto do estoque \n")
        print ("Opção 5: Sair \n")

        opcao = int(input())

        if (opcao == 1):
            create ('codigo', 'nome', 'quantidade')
            print (f"Você adicionou o produto {nome}")


        '''elif (opcao == 2):
            read()
        
        elif (opcao == 3):
            upd()

        elif (opcao == 4):
            delete()
            print (f"Você deletou {nome}")

        elif (opcao == 5):
            print ("Você saiu.")

        else:
            print ("Opcção incorreta")

            
        elif (opcao == 2):
            
        elif (opcao == 3):

        elif (opcao == 4):
            
        elif (opcao == 5):
            print ("Você saiu")
            break

        else:
            print ("Opção incorreta")'''
        
menu()
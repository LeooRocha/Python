from filme import Filme, Serie, Documentario
from cliente import Cliente
from login import Login

print ("-----------------------------------------------")
print ("             Bem vindo a SenaiFlix             ")
print ("-----------------------------------------------")

login = Login()

login.efetua_login()

titulos = {}

while True:
    print ("Escolha uma opção: ")
    print ("Opção 1: Alugar Filmes")
    print ("Opção 2: Alugar uma série")
    print ("Opção 3: Alugar um documentário")
    print ("Opção 4: Sair")

    opcao = int(input())

    if (opcao == '4'):
        print ("Você saiu!")
        break 

    elif (opcao == '1'):
    

  

    elif (opcao == 

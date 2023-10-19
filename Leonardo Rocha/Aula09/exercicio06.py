from layout_exercicio06 import *

calculadora = Calculadora(0,0)

print ("----------------------------------------------------------------")
print ("----------------BEM VINDO A CALCULADORA-------------------------")
while (True):
    print ("Escolha uma opção \n")
    print ("Opção 1: Adição \n")
    print ("Opção 2 : Subtração \n")
    print ("Opção 3 : Multiplicação \n")
    print ("Opção 4 : Divisão \n")
    print ("Opção 5 : Sair \n")

    opcao = int(input("Escolha uma opção: "))

    if (opcao == 5):
        print ("Você saiu!")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if (opcao == 1):
        print(calculadora.somar (num1, num2))

'''    elif (opcao == 2):
        num1 = int(input("Você escolheu a opção 2, digite o 1° número que você deseja subtrair: "))
        num2 = int(input("Escolha o 2° número: "))
        resultado = num1 - num2 
        print ("O resultado foi ", resultado)

    elif (opcao == 3):
        num1 = int(input("Você escolheu a opção 3, digite o 1° número que você deseja multiplicar: "))
        num2 = int(input("Escolha o 2° número: "))
        resultado = num1 * num2 
        print ("O resultado foi ", resultado)

    elif (opcao == 4):
        num1 = int(input("Você escolheu a opção 4, digite o 1° número que você deseja dividir: "))
        num2 = int(input("Escolha o 2° número: "))
        resultado = num1 / num2
        print ("O resultado foi ", resultado)

    else:
        print ("Você saiu")
        break'''
    
    
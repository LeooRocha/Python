import random
numero_sorteado = random.randint(1,100)
while (True):
    
    palpite = int(input("Advinhe o número entre 1 e 100: "))
    palpite += 1

    if (numero_sorteado < palpite):
        print ("Seu número é maior do que o número sorteado")

    elif (numero_sorteado > palpite):
        print ("Seu número é menor do que o número sorteado")
    else:
        print ("Você acertou o número!")
        break
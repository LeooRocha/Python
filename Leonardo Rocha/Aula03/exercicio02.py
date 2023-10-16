idade1 = int(input("Fale sua idade: "))

if (idade1 < 16):
    print("Você não pode votar")

elif (idade1 >= 16 and idade1 < 18):
    print("Seu voto é facultativo")

else:
    print("Seu voto é obrigatório")
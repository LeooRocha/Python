numero = float(input("Digite um número:"))

contador_par=0
contador_impar=0

while(True):
    if numero % 2 == 0:
        print(f"De 1 até {numero} temos {contador_par + 1} números pares.")
    else:
        print(f"De 1 até {numero} temos {numero}")
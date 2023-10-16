num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
num3 = float(input("Digite o 3° número: "))

print("O 1° número digitado foi: ", num1)
print("O 2° número digitado foi: ", num2)
print("O 3° número digitado foi: ", num3)

if (num1 > num2 > num3):
    print("O maior número digitado foi: ", num1)
elif (num2 > num1 > num3):
    print("O maior número digitado foi: ", num2)
else:
    print ("O maior número digitado foi", num3)
   

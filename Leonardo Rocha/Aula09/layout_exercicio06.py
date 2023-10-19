# Neste projeto você pode criar uma calculadora interativa que utiliza a classe Calculadora para realizar operações.

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar (num1, num2):
        return num1 + num2
    
    def subtrair (num1, num2):
        return num1 - num2
    
    def multiplicar (num1, num2):
        return num1 * num2
    
    def dividir (num1, num2):
        if num2 == 0:
            return ("Não é possivel dividir por zero. ")
        return num1 / num2
    
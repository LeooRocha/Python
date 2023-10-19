class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar (self, num1, num2):
        return num1 + num2
    
    def subtrair (self, num1, num2):
        return num1 - num2
    
    def multiplicar (self, num1, num2):
        return num1 * num2
    
    def dividir (self, num1, num2):
        if num2 == 0:
            return ("Não é possivel dividir por zero. ")
        return num1 / num2
    
soma = Calculadora(2,3)

soma.somar(2,3)
    
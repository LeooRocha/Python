class Shape():
    def calcular_area(self):
        pass

class Circulo(Shape):
    def calcular_area(self, r, pi):
       return pi * r * r

class Retangulo(Shape):
    def calcular_area(self, x, y):
        return  (x * y)

circulo = Circulo()
circulo.calcular_area(2,3.14)

retangulo = Retangulo()
retangulo.calcular_area(10, 5)

print("A area do circulo é: " ,circulo.calcular_area(2,3.14))
print("A area do retangulo é: " ,retangulo.calcular_area(10,5))
# Crie uma classe "veiculo" com um metodo "mover()"
# Cire duas subclasses, "Carro" e "Aviao" , que sobrescrevam o método "mover()"
# para exibir "au au" e "miau" , respectivamente, em seguida ,crie instancias de ambas as subclasses echame o metodo "emitir som() nelas"

class Veiculo:
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        return "Dirigindo: vrummmmm"
    
class Aviao(Veiculo):
    def mover(self):
        return "Voando: zummmmmmmm"
    
carro = Carro()
aviao = Aviao()

print(carro.mover())
print(aviao.mover())

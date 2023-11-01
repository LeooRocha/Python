# Crie uma classe "animal" com um metodo "emitir_som"
# Cire duas subclasses, "Cachorro" e "Gato" , que sobrescrevam o método "emitir_som()"
# para exibir "au au" e "miau" , respectivamente, em seguida ,crie instancias de ambas as subclasses echame o metodo "emitir som() nelas"

class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "AuAu"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau"
    
cachorro = Cachorro()
gato = Gato()

print(cachorro.emitir_som())
print(gato.emitir_som())





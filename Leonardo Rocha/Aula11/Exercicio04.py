class Animal:
    def emitir_som(self):
        pass

class Peixe(Animal):
    def emitir_som(self):
        return "Nadando..."
    
class Ave(Animal):
    def emitir_som(self):
        return "Voando..."
    
peixe = Peixe()
ave = Ave()

print(peixe.emitir_som())
print(ave.emitir_som())

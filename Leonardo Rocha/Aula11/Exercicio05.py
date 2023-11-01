# Crie um sistema de registro de funcionarios em uma 
# empresa, onde diferentes tipos de funcionário tem
# comportamentos especificos.
# crie uma classe Funcionario generica com um metódo
# "calcular salario" . Após , crie subclasses de funcionarios
# especificos, como funcionario ClT , funcionario comissionado,
# funcionario estagiário

# Crie um sistema que solicite e guarde os dados numa lista
# ou dicionarios


class Funcionario:
    def calcular_salario(self, nome, base):
        self.nome = nome
        self.base = base
        pass


class CLT(Funcionario):
    def calcular_salario(self, base):
        return base
    
class Comissionado(Funcionario):
    def calcular_salario(self, base, comissao):
        return base + comissao 
class Estagiário(Funcionario):
    def calcular_salario(self, base):
        return base / 2


funcionario = Funcionario()
clt = CLT()
comissionado  = Comissionado()
estagiario = Estagiário()

nome = (input)
cargo = (input("Digite o cargo: "))





if cargo == estagiario:
    print({nome, estagiario.calcular_salario})

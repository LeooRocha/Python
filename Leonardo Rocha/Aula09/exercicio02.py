#Crie uma classe Aluno que possui atributos como nome, idade e notas. Implemente métodos para calcular a idade, a média (3 notas) das notas e verificar se o aluno foi aprovado (média maior ou igual a 6).

class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcula_media (self):    #podemos definir parâmetros novos
        return sum (self.notas) / len(self.notas)
    
    def faca_aprov_reprov (self, nome, notas):
        media = self.calcula_media()
        if (media >= 6):
            return ("Aprovado")
        else:
            return ("Reprovado") 

aluno1 = Aluno("João", 20, [])
#Crie uma classe Pessoa que possui um atributo de classe para manter o número de pessoas criadas. Cada vez que você instacia um objeto da classe Pessoa, o contador deve ser incrementado.

class Pessoa:
    total_pessoas = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1

pessoa1 = Pessoa ("Alice" , 25)
pessoa2 = Pessoa ("Bob", 30)
pessoa3 = Pessoa 
'''print (f"Total de pessoas: {}")'''
#Crie uma classe Tarefa que representa uma tarefa a ser realizada. A classe deve ter atribuido como nome da tarefa, data de vencimento e status (pendente, em andamento, concluída). Implemente métodos para marcar a tarefa.

class Tarefa:
    def __init__(self, nome_tarefa, data_vencimento):
        self.nome_tarefa = nome_tarefa
        self.data_vencimento = data_vencimento
        self.status = "Pendente"

    def marcar_concluida (self):
        self.status = "Concluída"

    def verificar_vencimento (self):

        data_tarefa = input("Digite a data da tarefa")
        if self.status == "Pendente" and self.data_vencimento < data_tarefa:
            return (f"A tarefa {self.nome} está atrasada")
        
        return (f"A tarefa {self.nome} está em em dia")

tarefa1 = Tarefa ("Passear com cachorro", "2023-10-1/")

print (tarefa1.data_vencimento())
print(tarefa1.status())
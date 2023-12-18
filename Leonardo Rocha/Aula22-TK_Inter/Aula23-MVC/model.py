class Tarefa:
    def __init__(self, descricao, concluida = False):
        self.descricao = descricao
        self.concluida = concluida

class ListaTarefaModelo: #Possível herança
    def __init__(self):
        self.tarefa = []

    def adicionar_tarefa(self, tarefa):
        self.tarefa.append(tarefa) #self é a classe

    def obter_tarefa(self):
        return self.tarefa
from model import ListaTarefaModelo
from view import ListaTarefasVisao
from controller import ListaTarefaController

def principal():
    model = ListaTarefaModelo()
    view = ListaTarefasVisao()
    controller = ListaTarefaController(model, view)
    controller.executar()

principal()
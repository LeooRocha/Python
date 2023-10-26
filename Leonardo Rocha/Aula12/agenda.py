# class Contato parâmetros: nome, telefone e email. Class Agenda metodo construtor que vai receber uma lista de contatos vazia, métodos: adicionar contato, listar contatos, buscar contatos e deletar contatos.
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contato(self):
        for contato in self.contatos:
            print (contato)

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None
    
    def remover_contato (self, nome):
        contato = self.buscar_contato
        if  (contato is not nome):
            self.contatos.remove(contato)
            print (f"Contato {nome} removido com sucesso." )

        else:
            print (f"Contato {nome} não encontrado na agenda.")
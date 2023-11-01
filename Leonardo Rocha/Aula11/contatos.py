# class Contato parâmetros: nome, telefone e email. Class Agenda metodo construtor que vai receber uma lista de contatos vazia, parâmetros: adicionar contato, listar contatos, buscar contatose deletar contatos.

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return (f"Nome: {self.nome}\n telefone: {self.telefone}\n email: {self.email}")
                
        
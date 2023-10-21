#site de locação, filmes, séries e documentários. "Personagem" chamado Banco, Cartão de crédito, Locação, Catálogo

class Cliente:
    def __init__(self, nome, endereco, email, login):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.login = login
class Filme:
    def __init__(self, nome, genero, classificacao, duracao):
        self.nome = nome
        self.genero = genero
        self.classificacao = classificacao
        self.duracao = duracao

class Serie(Filme):
    def __init__(self, nome, genero, classificacao, duracao, temporada):
        self.temporada = temporada
        super().__init__(nome, genero, classificacao, duracao)

class Documentario(Filme):
    def __init__(self, nome, genero, classificaco, duracao, tema):
        self.tema = tema
        super ().__init__(nome, genero, classificaco, duracao, tema)

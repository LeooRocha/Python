
class Login:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def efetua_login(email, senha):
        if (email == email):
            if (senha == senha):
                print ("Login efetuado com sucesso")
            else:
                print ("E-mail ou senha inválidos")
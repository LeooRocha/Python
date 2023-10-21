from cliente import Cliente

class Cadastro(Cliente):
    def __init__(self, nome, endereco, email, login, senha):
        self.senha = senha
        super().__init__(self, nome, endereco, email, login)

    def efuta_cadastro(self):
        nome = input("Digite seu nome: ")
        endereco =  input("Digite seu endereco: ")
        email = input("Digite seu email: ") 
        senha = input("Crie uma senha de 4 números: ")

        print (f"Bem vindo {nome}.")
        print (f"Seu endereço {endereco} e emails {email} foram cadastrados com sucesso")
        print (f"A senha cadastrada é {senha}, memorize e não compartilhe esse dado")
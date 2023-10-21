

class Banco:
    def __init__(self, nome, endereco, agencia):
        self.nome = nome
        self.endereco = endereco
        self.agencia = agencia

    def pagamento_cartao(self, conta, agencia, saldo, valor_aluguel):
        # conta = int(input("Digite o número da sua conta: "))
        # agencia = int(input("Digite o número da sua agencia: "))

        if (saldo >= valor_aluguel):
            return saldo - valor_aluguel
        else:
            print("Saldo insuficiente")


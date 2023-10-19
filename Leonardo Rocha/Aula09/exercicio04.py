#Crie uma classe Pedido que permite criar objetos que represente pedidos em um restaurante. Cada objeto de pedido deve conter informações como nome do cliente, itens do pedido e valor total.

class Pedido:
    def __init__(self, nome_cliente, itens_pedido, valor_total):
        self.nome_cliente = nome_cliente
        self.itens_pedido = itens_pedido
        self.valor_total = valor_total

'''   def exibir_pedido (self, valor_total):'''

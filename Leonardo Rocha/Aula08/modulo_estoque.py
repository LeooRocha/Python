def diminui_estoque (estoque_inicial, estoque_final, compras):
    cmv = estoque_final + compras - estoque_inicial
    print ("O estoque atual é de: ", cmv)

def valor_compras_periodo (estoque_inicial, estoque_final, compras):
    valor_compras_periodo = estoque_final - estoque_inicial
    print ("O valor compras: ", valor_compras_periodo)


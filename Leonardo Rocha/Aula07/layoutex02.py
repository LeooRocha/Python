estoque = {}

def create (codigo, nome, quantidade):
    if codigo not in estoque:
        estoque [codigo] = {'nome' : nome, 'quantidade' : quantidade}

    else:
        print("O item já existe no estoque. Use a função atualizar_item para modificar a quantidade. ")

def upd (codigo, nome, quantidade):
    if codigo in estoque:
        estoque [codigo] ["quantidade"] =  quantidade

    else:
        print ("O item não existe no estoque. Use fução incluir_item para adiciona-lo")
        
def read (codigo, nome, quantidade):
    if codigo in estoque:
        for i in estoque:
            print (i, '\n')
    
    else:
        print ("O item não existe no estoque. Use fução incluir_item para adiciona-lo")

def delete (codigo, nome, quantidade):
    if codigo in estoque:
        del estoque ["codigo"] ["nome"] ["quantidade"]

    else:
        print ("O item não existe no estoque. Use fução incluir_item para adiciona-lo")
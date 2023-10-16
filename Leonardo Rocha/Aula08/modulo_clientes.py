#inserir, excluir, ler e atualizar

oficina = {}

def informacoes_cliente():
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    print("O cliente foi adicionado com sucesso")
    print ("Nome: ", nome, '\n')
    print ("Telefone: ", telefone, '\n')
    print ("Email: ", email, '\n')

def inserir_veiculo ():
    marca = input("Digite a marca do veículo: \n")
    modelo = input("Digite o modelo do veículo: \n")
    placa = input("Digite a placa do veículo: \n")
    ano_fabricacao = input("Digite o ano de fabricação do veículo: \n")
    print ("O veículo foi incluido com sucesso \n")
    print ("Marca", marca, '\n')
    print ("Modelo", modelo, '\n')
    print ("Placa", placa, '\n')
    print ("Ano", ano_fabricacao, '\n')
    if marca in oficina:
        print ("Este veículo já está registrado na oficina")



'''def excluir_veiculo (marca, modelo, placa, ano_fabricação):
'''
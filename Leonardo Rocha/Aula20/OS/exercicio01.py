# Crie uma função que peça para o usuário digitar o caminho de uma pasta/diretorio e que liste os arquivos de um diretorio utilizando a biblioteca OS:

import os

def listar_arquivos():
    caminho_diretorio = input("Informe o caminho do diretório: ")
    # Listar os arquivos do diretório passado
    arquivos = os.listdir(caminho_diretorio)

    print("os Arquivos do diretório são: ")
    for arquivo in arquivos:
        print(arquivo)
    else:
        print("Diretório Inválido")

listar_arquivos()
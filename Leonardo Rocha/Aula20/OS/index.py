import os

# Exemplo 1: Obter o Diretorio de Trabalho Atual
'''diretorio_atual = os.getcwd()
print(f"O direório atual é {diretorio_atual}")'''

# Exemplo 2: Listar os arquivos em um Diretório
'''diretorio = "A:\\Prof. Cassio de Albuquerque\Python III\Leonardo Rocha"

arquivos = os.listdir(diretorio)

print("os Arquivos do diretório são: ")
for arquivos in arquivos:
    print(arquivos)'''

# Exemplo 3: Criar um diretório
'''novo_diretorio = "A:\\Prof. Cassio de Albuquerque\\Python III\\Leonardo Rocha"

os.mkdir(novo_diretorio)'''

# Exemplo 4: Executar comandos no sistema
contador = 0
while contador < 10:
    os.system("echo Olá, Mundo")
    contador == 1

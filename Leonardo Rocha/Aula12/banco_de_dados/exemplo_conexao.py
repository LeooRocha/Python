import mysql.connector

# Configurações da conexão com o Banco de Dados
config = {
    'user' : 'se usuário',
    'password' : 'sua senha',
    'host' : 'Localhodt',
    'database' : 'nome_do_banco_de_dados'
}

# Estabelecer a conexão com o banco de dados
conexao =  mysql.connector.connect(**config)

# Criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Exemplo de consulta SQL
selecionarDB = "use loja_ii"
consulta = "SELECT * FROM tabela"

# Executar a consulta 
cursor.execute(selecionarDB)
cursor.execute(consulta)

# Recuperar os resultados
resultados = cursor.fetchall()

# Imprimir os resultados 
for linha in resultados:
    print (linha)

# Fechar o cursor da conexão
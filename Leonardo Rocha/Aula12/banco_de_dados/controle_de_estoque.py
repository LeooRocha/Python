import mysql.connector

config = {
    'user': 'root',
    'password' : 'senai',
    'host': 'localhost',
    'database': 'loja_ii'
}

#Estabelecer a conexão com o banco de dados
conexao = mysql.connector.connect(**config)

#criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Exemplo de consulta SQL
#selecionarDB = "use loja_II"

inserir_cliente = """INSERT INTO clientes (nome,endereco, telefone, e-mail, cpf) VALUES (%s,%s,%s,%s,%s)"""

# Dados novo cliente
nova_cliente = ("Ana Paula", "Rua do Bosque", 123456, "ana@ana", 3214453)

# Executar a consulta
#cursor.execute(selecionarDB)
cursor.execute(consulta)

# Recuperar os resultados
resultados = cursor.fetchall()

#Imprimir os resultados
for linha in resultados:
    print(linha)


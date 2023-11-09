import mysql.connector

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',                  #recebeu a conexão
    password = 'senai',
    database = 'banco_de_talentos'
    )

cursor = conn.cursor()

# Função para inserir dados na tabela cliente

def inserir_candiato (nome, email, cpf, linkdl, github):
    query = 'INSERT INTO candidato_vip (nome, email, cpf, linkdl, github) VALUES (%s, %s, %s, %s, %s)'
    values = (nome, email, cpf, linkdl, github)
    cursor.execute(query,values)
    conn.commit()
# Importa as bibliotecas
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#Instancia o navegador
navegador = webdriver.Chrome()

#Digita e busca a URl
navegador.get("https://github.com/login")

try: #Encapsula o  cogido que pode gerrar erro
    time.sleep(2) #Aguarda 2 segundos

    #Enconta pelo ID
    elemento = navegador.find_element(By.ID,"login_field")

    #Digita email 
    elemento.send_keys("leorochapro@outlook.com")

    #Enconta pelo ID
    elemento = navegador.find_element(By.ID,"password")

    #Digita senha
    elemento.send_keys("leo3010*06")


    #Confirmação do digitado
    elemento.send_keys(Keys.RETURN)
    time.sleep(3)
    


finally: #Fecha o navegador
    navegador.close

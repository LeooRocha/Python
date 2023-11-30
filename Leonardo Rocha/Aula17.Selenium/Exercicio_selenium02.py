# Entrar no sie da Anhanguera ,
# escolher o curso de ADM , continuar inscrição , 
# preencher com os dados , 
# gerador de de Cpf para gerar cpf copiar e colar no site.
# fazer o mesmo com o cep. 


# Importa as bibliotecas
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Instancia o navegador
navegador = webdriver.Edge()

# Navega na URL
navegador.get("https://www.anhanguera.com/")

try: #Encapsula o codigo que pode gerrar erro
    time.sleep(1)

    elemento = navegador.find_element(By.ID,"open-inscricao")
    elemento.click()
    time.sleep(2)

    # elemento.find_element(By.CLASS_NAME,"form-control")
    # elemento.send_keys("Bruce Wayne Terceiro")

    # elemento.find_element(By.NAME,"email")
    # elemento.send_keys("emailbemcomleto@gmail.com")

    # elemento.find_element(By.NAME,"phone")
    # elemento.send_keys("40028922")

    elemento.send_keys(Keys.RETURN)
    time.sleep(3)
    


finally:
    navegador.close()

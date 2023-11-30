# importar biblioteca selenium
# import selenium
from selenium  import webdriver #Webdriver vai ser o vai operar o navegador
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Instanciar o navegador( Chorme, neste exemplo)
navegador = webdriver.Chrome()


#Navegar utilizando o selenium (Navegar para um URL)
navegador.get("https://www.google.com.br/")

try: #Encapsula um codigo que pode gerrar erro
    time.sleep(2) #Aguarda 2 segundos

    #Encontar um elemento pelo ID
    elemento = navegador.find_element(By.ID,"APjFqb")


    # elemento.click()

    elemento.send_keys("Greve de Metro em São Paulos")

    elemento.send_keys(Keys.RETURN)
    time.sleep(3)



finally:
    #Fechar navegador

    navegador.close()


# Criar um scrip com selenium e pyautogui que pesquisa sobre um tema no google, copia e cola o título e cola o título no bloco de notas e o salva

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/') 
time.sleep(2)

pyautogui.typewrite("GTA 6") 
pyautogui.press('enter') 
time.sleep(3)

elemento = navegador.find_element(By.XPATH,"//*[@id="TnFuZZimHcDU1sQPm6yGoAo__49"]/div/a/div/div[2]/div[2]")
texto_elemento = elemento.text
time.sleep(2)

pyautogui.hotkey('ctrl', 'c')

pyautogui.press('winleft')
programa = "Bloco de notas"
pyautogui.write(programa)
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'v')

pyautogui.hotkey('ctrl', 's')

pyautogui.press('enter')
nome_arquivo= 'GTA 6.txt'
pyautogui.write(nome_arquivo)
pyautogui.press('enter')

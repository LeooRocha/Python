# Criar uma automação com pyautogui, pela qula o programa abre o bloco de notas e digita digite uma mensagem e a salve

import pyautogui
import time

pyautogui.press('winleft')
programa = "Bloco de notas"
pyautogui.write(programa)
pyautogui.press('enter')

time.sleep(2)

pyautogui.typewrite("Salve Salve maluko") 

pyautogui.hotkey('ctrl', 's')

pyautogui.press('enter')
nome_arquivo= 'salve.txt'
pyautogui.write(nome_arquivo)
pyautogui.press('enter')


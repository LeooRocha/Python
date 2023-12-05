# Criar um pyautogui que digite um texto no bloco de notas 
import pyautogui
import time

pyautogui.press('winleft')
programa = "Bloco de notas"
pyautogui.write(programa)
pyautogui.press('enter')

time.sleep(2)

pyautogui.typewrite("Salve Salve maluko") 

pyautogui.hotkey('ctrl', 'a')

pyautogui.hotkey('ctrl', 'c')

pyautogui.press('winleft')
programa = "Bloco de notas"
pyautogui.write(programa)
pyautogui.press('enter')

time.sleep(2)

pyautogui.hotkey('ctrl', 'v')
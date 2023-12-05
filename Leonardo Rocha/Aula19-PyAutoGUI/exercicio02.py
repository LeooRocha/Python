import pyautogui
import time

pyautogui.press('winleft')
programa = "Chrome"
pyautogui.write(programa)
pyautogui.press('enter')

time.sleep(2)

pyautogui.typewrite("https://youtu.be/QdBZY2fkU-0?si=PEpJqw8K-iCCN5od") 
pyautogui.press('enter')



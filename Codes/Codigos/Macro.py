import os
import pyautogui
import time  # Importando time para adicionar delays

while True:  # Loop infinito
    try:
        # Move para primeira posição e clica
        pyautogui.moveTo(-1186, 501)
        pyautogui.rightClick()
        pyautogui.moveTo(-1106, 546)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.hotkey('enter')
        
        # Move para segunda posição e clica
        pyautogui.moveTo(-987, 930)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        
        # Pequeno delay entre cada ciclo (2 segundos)
        time.sleep(2)
        
    except KeyboardInterrupt:
        # Permite parar o programa com Ctrl+C
        print("Programa interrompido pelo usuário")
        break




import os
import time
import pyautogui
import subprocess

# Caminho para o executável do Chrome
chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
opera_path = r'"C:\Users\matheus.oliveira.TECNO\AppData\Local\Programs\Opera GX\opera"'
edge_path = r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"'
NDD_path = r"C:\Program Files (x86)\NDDigital\MPSDesktop\MPSDesktop.exe"

# URL a ser aberta
url = "https://grupotecnoset.custhelp.com/AgentWeb/Bookmark/Report/101900/1722604097111"
url2 = "https://mps.tecnoset360.com.br/docmps/index.php"

login= "matheus.oliveira"
senha= "Dalmarmat200!"

LoginDoc = 'matheus.oliveira'
senhaDoc = 'Stocco92257'

subprocess.run(f'powershell Start-Process \'{NDD_path}\' -Verb runAs', shell=True)
time.sleep(2)
pyautogui.moveTo(817, 720)
pyautogui.mouseDown
pyautogui.mouseUp

# Abrir o Chrome com a primeira URL
subprocess.Popen(chrome_path + '' + url)
time.sleep(3)  # Tempo para garantir que o Chrome abriu
# Logando no RN
pyautogui.typewrite(login)
pyautogui.hotkey('Tab')
pyautogui.typewrite(senha)
pyautogui.hotkey('Tab')
pyautogui.hotkey('enter')
time.sleep(3)

# Pressionar Ctrl + n para abrir uma nova janela e carregar a mesma URL
pyautogui.hotkey('ctrl', 'n')  
time.sleep(2)
pyautogui.typewrite(url)
pyautogui.press('enter')
time.sleep(3)
# abrindo em formato de duas telas
pyautogui.hotkey('win', 'right')
pyautogui.moveTo(200,265)
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(3)
# Logando no RN
pyautogui.typewrite(login)
pyautogui.hotkey('Tab')
pyautogui.typewrite(senha)
pyautogui.hotkey('Tab')
pyautogui.hotkey('enter')

# Espera um pouco para garantir que a nova aba carregue
time.sleep(3)

pyautogui.hotkey('win', 'right')
pyautogui.moveTo(200, 275)
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(3)

#Abrir o Edge com o link do DOC
subprocess.Popen(edge_path + '' + url2)
time.sleep(4)
#Selecionar o campo de login para seguir com credenciais
pyautogui.moveTo(-1355, 474)
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.typewrite(LoginDoc) #Login Doc
time.sleep(2)
pyautogui.hotkey('tab')
pyautogui.typewrite(senhaDoc)#Senha Doc
time.sleep(2)
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
time.sleep(6)
pyautogui.moveTo(-2275, 303) #Altera para o campo Monitor
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(4)
pyautogui.moveTo(-2091, 131)#Desmarca bolinha para estender a aba 
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(3)
pyautogui.hotkey('ctrl', 'n') #Cria nova janela e loga com o link
time.sleep(3)
pyautogui.typewrite(url2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(-257, 136) #Muda o banco 
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(4)
pyautogui.moveTo(-314, 251)
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(4)
pyautogui.moveTo(-2275, 303) #Seleciona o Monitor
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(4)
pyautogui.moveTo(-2091, 131)#Desmarca bolinha para estender a aba 
pyautogui.mouseDown()
pyautogui.mouseUp()
time.sleep(4)
pyautogui.moveTo(-2091, 131)
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.hotkey('win','rigth')
time.sleep(4)
pyautogui.moveTo(-1946, 304)
pyautogui.mouseDown()
pyautogui.mouseUp()
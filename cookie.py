from selenium import webdriver 
import time
import os

navegador = webdriver.Firefox()
navegador.get("https://orteil.dashnet.org/cookieclicker/")
print("Verificando seu save, por favor não use o site até o menu do script aparecer")
time.sleep(6)
if os.path.exists("save.txt"):
    navegador.find_element_by_id('prefsButton').click()
    navegador.execute_script("Game.ImportSave()")
    save = open("save.txt", "r")
    navegador.find_element_by_id('textareaPrompt').send_keys(save.read())
    navegador.find_element_by_id('promptOption0').click()
else:
    print("Save não encontrado")

def clicaCookie(qnt):
    quantidade = int(qnt)
    x = 0
    while x < quantidade:
        navegador.execute_script("document.getElementById('bigCookie').click()")
        x += 1

def sair():
    navegador.execute_script("Game.toSave=true")
    navegador.find_element_by_id('prefsButton').click()
    navegador.execute_script("Game.ExportSave()")
    export = navegador.find_element_by_id('textareaPrompt')
    arq = open("save.txt", "w+")
    arq.write(export.text)
    navegador.close()

menu = True
while menu:
    qnt = input("Digite uma quantidade para clicar, ou 'sair' para sair do script: ")
    if qnt.upper() == "SAIR":
            sair()
            menu = False
    elif qnt.isdigit():
            clicaCookie(qnt)
    else:
        print("Opção inválida\n")


#<a class="option" onclick="Game.ExportSave();PlaySound('snd/tick.mp3');">Export save</a>
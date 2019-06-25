from selenium import webdriver 
import time
import os

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

browser = webdriver.Firefox()
browser.get("https://orteil.dashnet.org/cookieclicker/")
print(colors.WARNING + "Checking your save file and loading the page, don't use the game page until the menu show up" + colors.ENDC)
time.sleep(4)

if os.path.exists("save.txt"):
    browser.find_element_by_id('prefsButton').click()
    browser.execute_script("Game.ImportSave()")
    save = open("save.txt", "r")
    browser.find_element_by_id('textareaPrompt').send_keys(save.read())
    browser.find_element_by_id('promptOption0').click()
    browser.find_element_by_id('prefsButton').click()
    print(colors.OKBLUE + "Game loaded!" + colors.ENDC)
else:
    print(colors.OKBLUE + "Save file not found, starting a new game" + colors.ENDC)

def clicaCookie(qnt):
    quantity = int(qnt)
    twentyFive = (quantity * 25) / 100
    fifty = (quantity * 50) / 100
    seventyFive = (quantity * 75) / 100
    x = 1
    while x <= quantity:
        browser.execute_script("document.getElementById('bigCookie').click()")
        if x == round(twentyFive):
            print(colors.OKGREEN + '25%('+ str(round(twentyFive)) +') of ' + qnt + ' clicks reached' + colors.ENDC)
        elif x == round(fifty):
            print(colors.OKGREEN + '50%('+ str(round(fifty)) +') of ' + qnt + ' clicks reached' + colors.ENDC)
        elif x == round(seventyFive):
            print(colors.OKGREEN + '75%('+ str(round(seventyFive)) +') of ' + qnt + ' clicks reached' + colors.ENDC)
        elif x == quantity:
            print(colors.OKGREEN + '100%('+ str(quantity) +') of ' + qnt + ' clicks reached' + colors.ENDC)
        x += 1

def exitGame():
    browser.execute_script("Game.toSave=true")
    browser.find_element_by_id('prefsButton').click()
    browser.execute_script("Game.ExportSave()")
    export = browser.find_element_by_id('textareaPrompt')
    arq = open("save.txt", "w+")
    arq.write(export.text)
    browser.close()

menu = True
while menu:
    qnt = input(colors.OKBLUE + "Type the number of clicks, or 'exit' to save and quit the game: " + colors.ENDC)
    if qnt.upper() == "EXIT":
            exitGame()
            menu = False
    elif qnt.isdigit():
            clicaCookie(qnt)
    else:
        print(colors.FAIL + "Invalid option" + colors.ENDC)
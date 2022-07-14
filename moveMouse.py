from cgitb import text
from pickle import FALSE, TRUE
import pyautogui
import time
import random
from pygame import mixer
import pytesseract
import webbrowser

def safePosition():
    x = random.randint(0,300)
    y = random.randint(200,250)
    pyautogui.moveTo(x, y)

def makeSound():
    while(TRUE):
        sound.play()

mixer.init() 
sound=mixer.Sound("sound.wav")

ticketAvailable = ["Baja","Media","Alta","Disponibilidad"]
ticketNotAvailable = ["No","Disponible","Actualmente"]
correctPage = False
correctPageAgain = False

while(TRUE):
    for i in range(0,2):
        time.sleep(2)
        safePosition()
    correctPage = False
    correctPageAgain = False

    time.sleep(1)
    #click dropdown
    pyautogui.moveTo(450, 370)
    pyautogui.click()

    time.sleep(1)
    #click argentina
    pyautogui.moveTo(450, 430)
    pyautogui.click()

    time.sleep(1)

    #Take screenshots
    imgCheckCheckbox = pyautogui.screenshot("checkbox.png", region=(1100,1050, 1000, 800))
    textCheck = pytesseract.image_to_string('checkbox.png')
    
    if (not(any(possibleString in textCheck for possibleString in ticketAvailable) or any(possibleString in textCheck for possibleString in ticketNotAvailable))):
        pyautogui.moveTo(685, 370)
        pyautogui.click()
    
    time.sleep(1)

    imgDetailArabia = pyautogui.screenshot("arabia.png", region=(1100,1050, 1000, 200))
    imgDetailMexico = pyautogui.screenshot("mexico.png", region=(1100,1280, 1000, 200))
    imgDetailPolonia = pyautogui.screenshot("polonia.png", region=(1100, 1510, 1000, 200))

    #Take out the text in images

    textArabia = pytesseract.image_to_string('arabia.png')
    textMexico = pytesseract.image_to_string('mexico.png')
    textPolonia = pytesseract.image_to_string('polonia.png')

    for i in range(0,2):
        time.sleep(1)
        safePosition()
    
    if(any(possibleString in textArabia for possibleString in ticketNotAvailable) and not any(possibleString in textArabia for possibleString in ticketAvailable)):
        print("NO DISPONIBLE ARABIA YET")
    else:
        webbrowser.open('https://api.telegram.org/bot5495483613:AAFgQvGLTdKehIz9X3UvrI01ccRWztbO2L8/sendMessage?chat_id=-776832185&text=Hay entradas de ARABIA CARAJO, COMPRENLE A FELIPE POR FAVOR.')
        makeSound()
    if(any(possibleString in textMexico for possibleString in ticketNotAvailable) and not any(possibleString in textMexico for possibleString in ticketAvailable)):
        print("NO DISPONIBLE MEXICO YET")
    else:
        webbrowser.open('https://api.telegram.org/bot5495483613:AAFgQvGLTdKehIz9X3UvrI01ccRWztbO2L8/sendMessage?chat_id=-776832185&text=Hay entradas de MEXICO CARAJO, COMPRENLE A FELIPE POR FAVOR.')
        makeSound()
    if(any(possibleString in textPolonia for possibleString in ticketNotAvailable) and not any(possibleString in textPolonia for possibleString in ticketAvailable)):
        print("NO DISPONIBLE POLONIA YET")
    else:
        webbrowser.open('https://api.telegram.org/bot5495483613:AAFgQvGLTdKehIz9X3UvrI01ccRWztbO2L8/sendMessage?chat_id=-776832185&text=Hay entradas de POLONIA CARAJO, COMPRENLE A FELIPE POR FAVOR.')
        makeSound()

    #reset searchbar
    time.sleep(1)
    pyautogui.moveTo(550, 340)
    pyautogui.click()

    #######################
    #check OCTAVOS
    #######################
    time.sleep(1)
    pyautogui.moveTo(450, 480)
    pyautogui.click()
    time.sleep(1)
    imgDetailOctavos = pyautogui.screenshot("octavos.png", region=(1100,1395, 900, 200))
    textOctavos = pytesseract.image_to_string('octavos.png')

    for i in range(0,2):
        time.sleep(1)
        safePosition()

    if(any(possibleString in textOctavos for possibleString in ticketNotAvailable) and not any(possibleString in textOctavos for possibleString in ticketAvailable)):
        print("NO DISPONIBLE OCTAVOS YET")
    else:
        webbrowser.open('https://api.telegram.org/bot5495483613:AAFgQvGLTdKehIz9X3UvrI01ccRWztbO2L8/sendMessage?chat_id=-776832185&text=Hay entradas de OCTAVOS CARAJO, COMPRENLE A FELIPE POR FAVOR.')
        makeSound()
    
    #######################
    #check CUARTOS
    #######################
    time.sleep(1)
    pyautogui.moveTo(450, 525)
    pyautogui.click()
    time.sleep(1)
    imgDetailCuartos = pyautogui.screenshot("cuartos.png", region=(1100,1260, 900, 200))
    textCuartos = pytesseract.image_to_string('cuartos.png')

    for i in range(0,2):
        time.sleep(1)
        safePosition()

    if(any(possibleString in textCuartos for possibleString in ticketNotAvailable) and not any(possibleString in textCuartos for possibleString in ticketAvailable)):
        print("NO DISPONIBLE CUARTOS YET")
    else:
        webbrowser.open('https://api.telegram.org/bot5495483613:AAFgQvGLTdKehIz9X3UvrI01ccRWztbO2L8/sendMessage?chat_id=-776832185&text=Hay entradas de CUARTOS CARAJO, COMPRENLE A FELIPE POR FAVOR.')
        makeSound()

    #######################
    #check SEMIS
    #######################
    time.sleep(2)
    pyautogui.moveTo(450, 570)
    pyautogui.click()
    time.sleep(2)
    imgDetailSemis = pyautogui.screenshot("semis.png", region=(1100,1355, 900, 200))
    textSemis = pytesseract.image_to_string('semis.png')

    for i in range(0,2):
        time.sleep(1)
        safePosition()

    if(any(possibleString in textSemis for possibleString in ticketNotAvailable) and not any(possibleString in textSemis for possibleString in ticketAvailable)):
        print("NO DISPONIBLE SEMIS YET")
    else:
        webbrowser.open('https://api.telegram.org/bot5495483613:AAFgQvGLTdKehIz9X3UvrI01ccRWztbO2L8/sendMessage?chat_id=-776832185&text=Hay entradas de SEMIS CARAJO, COMPRENLE A FELIPE POR FAVOR.')
        makeSound()
    
    #######################
    #check FINAL
    #######################
    time.sleep(1)
    pyautogui.moveTo(450, 645)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(450, 685)
    pyautogui.click()
    time.sleep(1)
    imgDetailFinal = pyautogui.screenshot("final.png", region=(1100,1560, 900, 200))
    textFinal = pytesseract.image_to_string('final.png')

    for i in range(0,2):
        time.sleep(1)
        safePosition()

    if(any(possibleString in textFinal for possibleString in ticketNotAvailable) and not any(possibleString in textFinal for possibleString in ticketAvailable)):
        print("NO DISPONIBLE FINAL YET")
    else:
        webbrowser.open('https://api.telegram.org/bot5495483613:AAFgQvGLTdKehIz9X3UvrI01ccRWztbO2L8/sendMessage?chat_id=-776832185&text=Hay entradas de FINAL CARAJO, COMPRENLE A FELIPE POR FAVOR.')
        makeSound()

    #click checkbox
    time.sleep(1)
    pyautogui.moveTo(685, 370)
    pyautogui.click()

    #enter random match to not lose connectivity
    time.sleep(1)
    pyautogui.moveTo(450, 550)
    pyautogui.click()

    while(not correctPage):
        imgInsideMatch = pyautogui.screenshot("match.png", region=(300,750, 600, 300))
        textMatch = pytesseract.image_to_string('match.png')
        if("entradas" in textMatch):
            correctPage = True

    #go back to buy tickets
    for i in range(0,3):
        time.sleep(2)
        safePosition()
    pyautogui.moveTo(950, 150)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click()

    while(not correctPageAgain):
        imgInsideTickets = pyautogui.screenshot("tickets.png", region=(300,500, 600, 200))
        textTickets = pytesseract.image_to_string('tickets.png')
        if("partidos" in textTickets):
            correctPageAgain = True
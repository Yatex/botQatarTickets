from pickle import FALSE, TRUE
import pyautogui
import time
import random
from pygame import mixer
import pytesseract
import hashlib
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
original_md5 = '5f3b9a8d2d554dc4d370d96ccd8bbf7a'

ticketAvailable = ["Baja","Media","Alta","Disponibilidad"]
ticketNotAvailable = ["No","Disponible","Actualmente"]

while(TRUE):
    for i in range(0,3):
        time.sleep(2)
        safePosition()
    
    #check checkbox
    imgCheckbox = pyautogui.screenshot("compare.png", region=(1270,705, 500, 50))
    checksumChecked = hashlib.md5(open('compare.png','rb').read()).hexdigest()

    if(checksumChecked != original_md5):
        time.sleep(2)
        pyautogui.moveTo(685, 370)
        pyautogui.click()

    time.sleep(2)
    #click dropdown
    pyautogui.moveTo(450, 370)
    pyautogui.click()

    time.sleep(2)
    #click argentina
    pyautogui.moveTo(450, 430)
    pyautogui.click()

    time.sleep(2)

    #Take screenshots
    imgCheckCheckbox = pyautogui.screenshot("checkbox.png", region=(1100,1050, 1000, 800))
    textCheck = pytesseract.image_to_string('checkbox.png')
    
    if (not(any(possibleString in textCheck for possibleString in ticketAvailable) or any(possibleString in textCheck for possibleString in ticketNotAvailable))):
        pyautogui.moveTo(685, 370)
        pyautogui.click()
    
    time.sleep(3)

    imgDetailArabia = pyautogui.screenshot("arabia.png", region=(1100,1050, 1000, 200))
    imgDetailMexico = pyautogui.screenshot("mexico.png", region=(1100,1280, 1000, 200))
    imgDetailPolonia = pyautogui.screenshot("polonia.png", region=(1100, 1510, 1000, 200))

    #Take out the text in images

    textArabia = pytesseract.image_to_string('arabia.png')
    textMexico = pytesseract.image_to_string('mexico.png')
    textPolonia = pytesseract.image_to_string('polonia.png')

    for i in range(0,5):
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
    time.sleep(2)
    pyautogui.moveTo(550, 340)
    pyautogui.click()

    #######################
    #check OCTAVOS
    #######################
    time.sleep(2)
    pyautogui.moveTo(450, 480)
    pyautogui.click()
    time.sleep(2)
    imgDetailOctavos = pyautogui.screenshot("octavos.png", region=(1100,1395, 900, 200))
    textOctavos = pytesseract.image_to_string('octavos.png')

    for i in range(0,3):
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
    time.sleep(2)
    pyautogui.moveTo(450, 525)
    pyautogui.click()
    time.sleep(2)
    imgDetailCuartos = pyautogui.screenshot("cuartos.png", region=(1100,1260, 900, 200))
    textCuartos = pytesseract.image_to_string('cuartos.png')

    for i in range(0,3):
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

    for i in range(0,3):
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
    time.sleep(2)
    pyautogui.moveTo(450, 645)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(450, 685)
    pyautogui.click()
    time.sleep(2)
    imgDetailFinal = pyautogui.screenshot("final.png", region=(1100,1560, 900, 200))
    textFinal = pytesseract.image_to_string('final.png')

    for i in range(0,3):
        time.sleep(1)
        safePosition()

    if(any(possibleString in textFinal for possibleString in ticketNotAvailable) and not any(possibleString in textFinal for possibleString in ticketAvailable)):
        print("NO DISPONIBLE FINAL YET")
    else:
        webbrowser.open('https://api.telegram.org/bot5495483613:AAFgQvGLTdKehIz9X3UvrI01ccRWztbO2L8/sendMessage?chat_id=-776832185&text=Hay entradas de FINAL CARAJO, COMPRENLE A FELIPE POR FAVOR.')
        makeSound()

    #click checkbox
    time.sleep(2)
    pyautogui.moveTo(685, 370)
    pyautogui.click()

    #enter random match to not lose connectivity
    time.sleep(2)
    pyautogui.moveTo(450, 550)
    pyautogui.click()    

    time.sleep(4)
    pyautogui.moveTo(20, 60)
    pyautogui.click()

    #click refresh
    time.sleep(4)
    pyautogui.moveTo(90, 60)
    pyautogui.click()
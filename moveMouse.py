from pickle import FALSE, TRUE
import pyautogui
import time
import random
from pygame import mixer
import pytesseract
import hashlib
import pywhatkit
from threading import Thread

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

while(TRUE):
    for i in range(0,5):
        time.sleep(2)
        safePosition()
    buttonUnChecked = FALSE
    
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

    imgDetailArabia = pyautogui.screenshot("arabia.png", region=(1100,1050, 900, 150))
    imgDetailMexico = pyautogui.screenshot("mexico.png", region=(1100,1280, 900, 150))
    imgDetailPolonia = pyautogui.screenshot("polonia.png", region=(1100, 1510, 900, 150))

    #Take out the text in images

    textArabia = pytesseract.image_to_string('arabia.png')
    textMexico = pytesseract.image_to_string('mexico.png')
    textPolonia = pytesseract.image_to_string('polonia.png')

    for i in range(0,5):
        time.sleep(1)
        safePosition()
    
    if("No" in textArabia):
        print("NO DISPONIBLE ARABIA YET")
    else:
        if("Disponibilidad" in textArabia):
            pywhatkit.sendwhatmsg_to_group_instantly("BB3cfiT3zAlGw6YXXNLpMF", "Hay entradas de ARABIA CARAJO, COMPRENLE A FELIPE CAT 3. SOY EL BOT!")
            makeSound()
        else:
            pyautogui.moveTo(685, 370)
            pyautogui.click()
            buttonUnChecked = TRUE
    if("No" in textMexico):
        print("NO DISPONIBLE MEXICO YET")
    else:
        if("Disponibilidad" in textMexico):
            pywhatkit.sendwhatmsg_to_group_instantly("BB3cfiT3zAlGw6YXXNLpMF", "Hay entradas de MEXICO CARAJO, COMPRENLE A FELIPE CAT 3. SOY EL BOT!")
            makeSound()
        else:
            if(buttonUnChecked):
                pyautogui.moveTo(685, 370)
                pyautogui.click()
                buttonUnChecked = TRUE
    if("No" in textPolonia):
        print("NO DISPONIBLE POLONIA YET")
    else:
        if("Disponibilidad" in textPolonia):
            pywhatkit.sendwhatmsg_to_group_instantly("BB3cfiT3zAlGw6YXXNLpMF", "Hay entradas de POLONIA CARAJO, COMPRENLE A FELIPE CAT 3. SOY EL BOT!")
            makeSound()
        else:
            if(buttonUnChecked):
                pyautogui.moveTo(685, 370)
                pyautogui.click()
                buttonUnChecked = TRUE

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
    imgDetailOctavos = pyautogui.screenshot("octavos.png", region=(1100,1395, 900, 150))
    textOctavos = pytesseract.image_to_string('octavos.png')

    for i in range(0,3):
        time.sleep(1)
        safePosition()

    if("No" in textOctavos):
        print("NO DISPONIBLE OCTAVOS YET")
    else:
        pywhatkit.sendwhatmsg_to_group_instantly("BB3cfiT3zAlGw6YXXNLpMF", "Hay entradas de OCTAVOS CARAJO, COMPRENLE A FELIPE CAT 3. SOY EL BOT!")
        makeSound()
    
    #######################
    #check CUARTOS
    #######################
    time.sleep(2)
    pyautogui.moveTo(450, 525)
    pyautogui.click()
    time.sleep(2)
    imgDetailCuartos = pyautogui.screenshot("cuartos.png", region=(1100,1260, 900, 150))
    textCuartos = pytesseract.image_to_string('cuartos.png')

    for i in range(0,3):
        time.sleep(1)
        safePosition()

    if("No" in textCuartos):
        print("NO DISPONIBLE CUARTOS YET")
    else:
        pywhatkit.sendwhatmsg_to_group_instantly("BB3cfiT3zAlGw6YXXNLpMF", "Hay entradas de CUARTOS CARAJO, COMPRENLE A FELIPE CAT 3. SOY EL BOT!")
        makeSound()

    #######################
    #check SEMIS
    #######################
    time.sleep(2)
    pyautogui.moveTo(450, 570)
    pyautogui.click()
    time.sleep(2)
    imgDetailSemis = pyautogui.screenshot("semis.png", region=(1100,1355, 900, 150))
    textSemis = pytesseract.image_to_string('semis.png')

    for i in range(0,3):
        time.sleep(1)
        safePosition()

    if("No" in textSemis):
        print("NO DISPONIBLE SEMIS YET")
    else:
        pywhatkit.sendwhatmsg_to_group_instantly("BB3cfiT3zAlGw6YXXNLpMF", "Hay entradas de SEMIS CARAJO, COMPRENLE A FELIPE CAT 3. SOY EL BOT!")
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
    imgDetailFinal = pyautogui.screenshot("final.png", region=(1100,1560, 900, 150))
    textFinal = pytesseract.image_to_string('final.png')

    for i in range(0,3):
        time.sleep(1)
        safePosition()

    if("No" in textFinal):
        print("NO DISPONIBLE FINAL YET")
    else:
        pywhatkit.sendwhatmsg_to_group_instantly("BB3cfiT3zAlGw6YXXNLpMF", "Hay entradas de FINAL CARAJO, COMPRENLE A FELIPE CAT 3. SOY EL BOT!")
        makeSound()

    #click checkbox
    time.sleep(2)
    pyautogui.moveTo(685, 370)
    pyautogui.click()

    #enter random match to not lose connectivity
    time.sleep(2)
    pyautogui.moveTo(450, 550)
    pyautogui.click()    

    time.sleep(5)
    pyautogui.moveTo(20, 60)
    pyautogui.click()

    #click refresh
    time.sleep(5)
    pyautogui.moveTo(90, 60)
    pyautogui.click()
from pickle import FALSE, TRUE
import pyautogui
import time
import random
from pygame import mixer
import pytesseract
import hashlib

def safePosition():
    x = random.randint(0,300)
    y = random.randint(200,250)
    pyautogui.moveTo(x, y)

mixer.init() 
sound=mixer.Sound("sound.wav")
original_md5 = '5f3b9a8d2d554dc4d370d96ccd8bbf7a'

while(TRUE):
    for i in range(0,5):
        time.sleep(1)
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

    imgDetailArabia = pyautogui.screenshot("arabia.png", region=(1100,1050, 900, 150))
    imgDetailMexico = pyautogui.screenshot("mexico.png", region=(1100,1280, 900, 150))
    imgDetailPolonia = pyautogui.screenshot("polonia.png", region=(1100, 1510, 900, 150))

    #Take out the text in images

    textArabia = pytesseract.image_to_string('arabia.png')
    textMexico = pytesseract.image_to_string('mexico.png')
    textPolonia = pytesseract.image_to_string('polonia.png')
    print(textArabia)
    print(textMexico)
    print(textPolonia)

    for i in range(0,5):
        time.sleep(1)
        safePosition()
    
    if("No" in textArabia):
        print("NO DISPONIBLE ARABIA YET")
    else:
        while(TRUE):
            sound.play()
    if("No" in textMexico):
        print("NO DISPONIBLE MEXICO YET")
    else:
        while(TRUE):
            sound.play()
    if("No" in textPolonia):
        print("NO DISPONIBLE POLONIA YET")
    else:
        while(TRUE):
            sound.play()

    time.sleep(2)

    #click refresh
    pyautogui.moveTo(90, 60)
    pyautogui.click()
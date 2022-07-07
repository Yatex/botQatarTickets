from pickle import FALSE, TRUE
import pyautogui
import time
import random
from pygame import mixer
import pytesseract

def randomPosition():
    x = random.randint(0,500)
    y = random.randint(200,500)
    pyautogui.moveTo(x, y)

while(TRUE):
    for i in range(0,5):
        time.sleep(1)
        randomPosition()
    
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
        randomPosition()
    
    

    # TELL ME THE TICKETS ARE AVAILABLE
    # try:
    #     compareInfo = pyautogui.locateOnScreen('compare.png', confidence=0.9)
    #     print('COMPARANDO')
    #     print(compareInfo)
    # except:
    #     mixer.init() 
    #     sound=mixer.Sound("sound.wav")
    #     sound.play()

    # time.sleep(2)


    # time.sleep(5)

    #click match
    pyautogui.moveTo(340, 570)
    # pyautogui.click()

    # for i in range(0,5):
    #     time.sleep(5)
    #     randomPosition()

    time.sleep(2)

    #click back
    pyautogui.moveTo(20, 60)
    # pyautogui.click()
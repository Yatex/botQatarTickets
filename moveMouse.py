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
    # for i in range(0,5):
    #     time.sleep(5)
    #     randomPosition()
    
    time.sleep(2)
    #unclick checkbox

    text = pytesseract.image_to_string('check.png')
    print(text)

    # infoCheck = pyautogui.locateOnScreen('check.png', confidence=0.9)
    # pyautogui.moveTo(infoCheck[0], infoCheck[1])
    # print('CHEQUEANDO CLICK')
    # print(infoCheck)
    # pyautogui.click()
    time.sleep(5)
    # try:
        # infoCheck = pyautogui.locateOnScreen('check.png', confidence=0.9)
        # pyautogui.moveTo(infoCheck[0], infoCheck[1])
    # except:
    #     print("Check desclickeado\n")
    
    time.sleep(2)
    #click dropdown
    pyautogui.moveTo(450, 370)
    pyautogui.click()

    time.sleep(2)
    #click argentina
    pyautogui.moveTo(450, 430)
    pyautogui.click()

    time.sleep(2)

    # im1 = pyautogui.screenshot('qatar.png', region=(1000,800, 1100, 1100))

    try:
        compareInfo = pyautogui.locateOnScreen('compare.png', confidence=0.9)
        print('COMPARANDO')
        print(compareInfo)
    except:
        mixer.init() 
        sound=mixer.Sound("sound.wav")
        sound.play()

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
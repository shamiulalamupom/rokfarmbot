from pyautogui import *
import pyautogui
import time
import keyboard 
import numpy as np
import random 
import win32api, win32con

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def wheatButtonPress():
    # WHEAT MENU PRESS
    # X: -1762 Y:  878
    click(-1762, 878)
    time.sleep(np.random.uniform(1, 1.2))

    # FIND BUTTON PRESS
    # X: -1764 Y:  749
    click(-1764, 749)
    time.sleep(np.random.uniform(3, 3.2))

def farm():
    # clicking the farm
    # X: -1599 Y:  496
    click(-1599, 496)
    time.sleep(np.random.uniform(1, 1.2))

    # GATHER BUTTON PRESS
    # X: -1317 Y:  603
    click(-1317, 603)
    time.sleep(np.random.uniform(1, 1.2))
    
    # NEW TROOP BUTTON
    # X: -1017 Y:  306
    click(-1017, 306)
    time.sleep(np.random.uniform(1, 1.2))

    # CLEAR BUTTON PRESS
    # X: -1561 Y:  731
    # click(-1561, 731)
    # time.sleep(np.random.uniform(1, 1.2))
    res = pyautogui.locateCenterOnScreen('clear.png', grayscale=True, confidence=0.8)
    if res != None:
        click(res[0], res[1])
        time.sleep(np.random.uniform(1, 1.2))
    else:
        click(res[0], res[1])
        time.sleep(np.random.uniform(1, 1.2))
        click(res[0], res[1])
        time.sleep(np.random.uniform(1, 1.2))

    # AFTER 0 CLICK
    # X: -1266 Y:  325
    click(-1266, 325)
    time.sleep(np.random.uniform(1, 1.2))

    # WRITING 500
    pyautogui.keyDown('5')
    time.sleep(np.random.uniform(0.3, 0.5))
    pyautogui.keyUp('5')
    time.sleep(0.8)
    pyautogui.keyDown('0')
    time.sleep(np.random.uniform(0.3, 0.5))
    pyautogui.keyUp('0')
    time.sleep(0.8)
    pyautogui.keyDown('0')
    time.sleep(np.random.uniform(0.3, 0.5))
    pyautogui.keyUp('0')

    time.sleep(np.random.uniform(1, 1.2))

    # GATHER BUTTON PRESS
    # X: -1341 Y:  735
    click(-1341, 735)
    time.sleep(np.random.uniform(1, 1.2))

def buttonPress(btn: str):
    pyautogui.keyDown(btn)
    time.sleep(np.random.uniform(0.3, 0.5))
    pyautogui.keyUp(btn)

    time.sleep(np.random.uniform(1, 1.2))

def farmWheat():
    buttonPress('space')
    buttonPress('f')
    wheatButtonPress()
    farm()
    buttonPress('space')

while keyboard.is_pressed('q') == False:
    farmWheat()

    time.sleep(300)
    print("Farming complete...")
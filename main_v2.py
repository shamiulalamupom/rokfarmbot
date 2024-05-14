from pyautogui import *
import pyautogui
import time
import keyboard 
import numpy as np
import random 
import win32api, win32con

try:
    farm_node = pyautogui.prompt(text='What do you want to farm? (Food, Wood, Stone)', title='Rise of Kingdom: Farm Bot').lower()
    if farm_node == '':
        farm_node = 'food'
except AttributeError:
    farm_node = 'food'
print(farm_node)

number = ''
try:
    number = pyautogui.prompt(text='How many troops should I send per node?', title='Rise of Kingdom: Farm Bot').lower()
except AttributeError:
    farm_node = ''

pyautogui.alert(text='Switch to the game to make the bot work', title='Rise of Kingdom: Farm Bot')

time.sleep(3)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    time.sleep(np.random.uniform(1, 1.2))

def buttonPress(btn: str):
    pyautogui.keyDown(btn)
    time.sleep(np.random.uniform(0.3, 0.5))
    pyautogui.keyUp(btn)

    time.sleep(np.random.uniform(1, 1.2))

def locateAndClick(path: str, btn: str, grayscale=False, confidence=1.0):
    try:
        if pyautogui.locateCenterOnScreen(path, grayscale=grayscale, confidence=confidence) != None:
            buttonPress(btn)
    except pyautogui.ImageNotFoundException:
        pass

while keyboard.is_pressed('q') == False:
    locateAndClick(path='images/map.png', btn='space', grayscale=True, confidence=0.8)
    # try:
    #     if pyautogui.locateCenterOnScreen('images/map.png', grayscale=True, confidence=0.8) != None:
    #         buttonPress('space')
    # except pyautogui.ImageNotFoundException:
    #     pass

    buttonPress('f')

    try:
        node_button = pyautogui.locateCenterOnScreen(f'images/{farm_node}_button.png', grayscale=True, confidence=0.8)
        if node_button != None:
            click(node_button[0], node_button[1])
    except pyautogui.ImageNotFoundException:
        pass

    try:
        search = pyautogui.locateCenterOnScreen('images/search.png', grayscale=True, confidence=0.8)
        if search != None:
            click(search[0], search[1])
    except pyautogui.ImageNotFoundException:
        pass

    # Give some time to load the node.
    time.sleep(np.random.uniform(3.5, 3.7))

    try:
        node = pyautogui.locateCenterOnScreen(f'images/{farm_node}.png', grayscale=True, confidence=0.8)
        if node != None:
            click(node[0], node[1])
    except pyautogui.ImageNotFoundException:
        pass

    try:
        gather_button = pyautogui.locateCenterOnScreen('images/gather_button.png', grayscale=True, confidence=0.8)
        if gather_button != None:
            click(gather_button[0], gather_button[1])
    except pyautogui.ImageNotFoundException:
        pass

    try:
        newTroop_button = pyautogui.locateCenterOnScreen('images/newTroop_button.png', grayscale=True, confidence=0.8)
        if newTroop_button != None:
            click(newTroop_button[0], newTroop_button[1])
    except pyautogui.ImageNotFoundException:
        pass

    # Give some time to load the node.
    time.sleep(np.random.uniform(1, 1.2))
    
    if number:
        try:
            max = pyautogui.locateCenterOnScreen('images/max.png', grayscale=True, confidence=0.8)
            if max != None:
                click(max[0], max[1])
        except pyautogui.ImageNotFoundException:
            pass

        try:
            clear = pyautogui.locateCenterOnScreen('images/clear.png', grayscale=True, confidence=0.8)
            if clear != None:
                click(clear[0], clear[1])
        except pyautogui.ImageNotFoundException:
            pass

        try:
            zero = pyautogui.locateCenterOnScreen('images/zero.png', grayscale=True, confidence=0.8)
            if zero != None:
                click(zero[0], zero[1])
        except pyautogui.ImageNotFoundException:
            pass

        for digits in number:
            pyautogui.keyDown(digits)
            time.sleep(np.random.uniform(0.3, 0.5))
            pyautogui.keyUp(digits)

    try:
        march = pyautogui.locateCenterOnScreen('images/march.png', grayscale=True, confidence=0.8)
        if march != None:
            click(march[0], march[1])
    except pyautogui.ImageNotFoundException:
        pass
 
    buttonPress('space')
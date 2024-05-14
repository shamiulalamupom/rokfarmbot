from pyautogui import *
import pyautogui
import pyscreeze
import time
import keyboard 
import numpy as np
import random 
import win32api, win32con

time.sleep(3)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    time.sleep(np.random.uniform(1, 1.2))

def buttonPress(btn: str, iter: int = 1):
    for _ in range(iter):
        pyautogui.keyDown(btn)
        time.sleep(np.random.uniform(0.3, 0.5))
        pyautogui.keyUp(btn)

        time.sleep(np.random.uniform(1, 1.2))

def scrollabit():
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(1)
    pyautogui.scroll(-1)

def find_node() -> pyscreeze.Point:
    while True:
        pyautogui.keyDown('up')
        time.sleep(0.1)
        pyautogui.keyUp('up')

        time.sleep(np.random.uniform(3, 3.2))

        try:
            node = pyautogui.locateCenterOnScreen('images/gem_v2_l.png', grayscale=True, confidence=0.8)
            if node != None:
                print('Large...')
                return pyautogui.locateCenterOnScreen('images/gem_v2_l.png', grayscale=True, confidence=0.8)
        except pyautogui.ImageNotFoundException:
            pass

        try:
            node = pyautogui.locateCenterOnScreen('images/gem_v2_n.png', grayscale=True, confidence=0.8)
            if node != None:
                print('Normal...')
                return pyautogui.locateCenterOnScreen('images/gem_v2_n.png', grayscale=True, confidence=0.8)
        except pyautogui.ImageNotFoundException:
            pass

        try:
            node = pyautogui.locateCenterOnScreen('images/gem_v2_s.png', grayscale=True, confidence=0.8)
            if node != None:
                print('Small...')
                return pyautogui.locateCenterOnScreen('images/gem_v2_s.png', grayscale=True, confidence=0.8)
        except pyautogui.ImageNotFoundException:
            continue

while keyboard.is_pressed('q') == False:
    try:
        if pyautogui.locateCenterOnScreen('images/map.png', grayscale=True, confidence=0.8) != None:
            buttonPress('space')
    except pyautogui.ImageNotFoundException:
        buttonPress('space', iter=2)

    scrollabit()

    res = find_node()
    click(res[0], res[1])

    time.sleep(np.random.uniform(1, 1.2)) 

    time.sleep(np.random.uniform(10, 10.2))
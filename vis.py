from pyautogui import *
import pyautogui
import pydirectinput
import time
import keyboard 
import numpy as np
import random 
import win32api, win32con

time.sleep(3)

def scrollabit():
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(1)
    pyautogui.scroll(-1)

print('Scrolled...')

time.sleep(3)

found = []

try:
    node = pyautogui.locateCenterOnScreen('images/gem_v2_l.png', grayscale=True, confidence=0.8)
    if node != None:
        # found.append()
        print('Large...')
except pyautogui.ImageNotFoundException:
    pass

try:
    node = pyautogui.locateCenterOnScreen('images/gem_v2_n.png', grayscale=True, confidence=0.8)
    if node != None:
        print('Normal...')
except pyautogui.ImageNotFoundException:
    pass

try:
    node = pyautogui.locateCenterOnScreen('images/gem_v2_s.png', grayscale=True, confidence=0.8)
    if node != None:
        print('Small...')
except pyautogui.ImageNotFoundException:
    pass
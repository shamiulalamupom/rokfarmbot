from pyautogui import *
import pyautogui
import pydirectinput
import time
import keyboard 
import numpy as np
import random 
import win32api, win32con

time.sleep(3)

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    click()
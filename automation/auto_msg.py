import pyautogui as py
import time

greet = [i for i in range(6)]

for i in greet:
    py.write(f" {i}")
    py.press('enter')

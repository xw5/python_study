import pyautogui
import time

time.sleep(5)
distanceX = 0
distanceY = 0
tag = 0
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
while True:
    tag = tag + 1
    if tag == 1:
        distanceX = 50
        distanceY = 0
    if tag == 2:
        distanceX = 0
        distanceY = 50
    if tag == 3:
        distanceX = -50
        distanceY = 0
    if tag == 4:
        distanceX = 0
        distanceY = -50
        tag = 0
    # pyautogui.moveRel(distanceX, distanceY)
    pyautogui.drag(distanceX, distanceY, duration=0.5)
    time.sleep(5)

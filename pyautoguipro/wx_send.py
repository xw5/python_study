import pyautogui
import pypaperclip
import time


def send(users, content):
    for item in users:
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        print(item)
        pypaperclip.copy(item,)
        pyautogui.typewrite(message=item, interval=0.25)
        pyautogui.hotkey('enter')
        time.sleep(2)
        pyautogui.typewrite(message=content, interval=0.25)


time.sleep(5)
users = ['文件传输助手']
send(users, 'hello tkinter')

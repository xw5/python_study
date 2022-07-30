import pyautogui
import pyperclip
import time

def enter_text(content):
    pyperclip.copy(content)
    time.sleep(1)
    # pyperclip.paste()
    pyautogui.hotkey('ctrl', 'v')

def send(users, content, callback = None):
    users_len = len(users)
    pyautogui.hotkey('ctrl', 'alt', 'z')
    time.sleep(0.5)
    for index, item in enumerate(users):
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        print(item)
        enter_text(item)
        time.sleep(2)
        pyautogui.hotkey('enter')
        time.sleep(1)
        enter_text(content)
        pyautogui.hotkey('enter')
        time.sleep(3)
        if callback:
            callback(users_len, index)
        print(users_len, index + 1)

users = ['肥肥']
send(users, 'hello tkinter')

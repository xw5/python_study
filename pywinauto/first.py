from pywinauto import application
from pywinauto.keyboard import send_keys
import time

# import pywinauto.mouse

app = application.Application(backend='uia').start('notepad.exe')

wind_notepad = app['无标题 - 记事本']

edit = wind_notepad['Edit']

edit.type_keys("python自动化")
edit.type_keys("解放双手，享受生活！")

send_keys("^a")

print("默认状态值：", wind_notepad.get_show_state())
time.sleep(2)
wind_notepad.maximize()
time.sleep(2)
print("最大化状态值：", wind_notepad.get_show_state())
wind_notepad.restore()
print("还原到默认状态值：", wind_notepad.get_show_state())
# wind_notepad.minimize()
# print("最小化状态值：", wind_notepad.get_show_state())

time.sleep(2)
win = app['Dialog']
wind_notepad["帮助"].click_input()
time.sleep(2)
wind_notepad['关于记事本'].click_input()  # or .click_input()
# pywinauto.mouse.move(coords=(500, 500))

# pywinauto.mouse.right_click(coords=(400, 400))

wind_notepad.close()
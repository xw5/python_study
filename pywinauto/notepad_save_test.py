import time
from pywinauto import Application

app = Application(backend='uia').start("notepad.exe")
wind_notepad = app['无标题 - 记事本']
titleBar = wind_notepad['帮助']
titleBar.click_input()
time.sleep(1)
wind_notepad['关于计事本'].click_input()
time.sleep(1)
wind_notepad['确定'].click_input()

edit = wind_notepad['Edit']

edit.type_keys("python自动化")
edit.type_keys("解放双手，享受生活！")
time.sleep(1)
wind_notepad['文件'].click_input()
time.sleep(1)
wind_notepad['保存(S)\tCtrl+S'].click_input()
time.sleep(3)
saveDlg = wind_notepad['另存为']
print(saveDlg.print_control_identifiers())
# inputObj = saveDlg['Edit']
saveDlg.type_keys("test.txt")
wind_notepad['保存(S)'].click_input()

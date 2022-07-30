# coding=utf-8
# import subprocess
#
# subprocess.Popen('E:\soft\WeChat\WeChat.exe')

# import os

# os.system('C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe')
# 优
# os.startfile(r'C:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe')

import win32gui, win32con
import time

handle = win32gui.FindWindow('TXGuiFoundation', 'QQ')
time.sleep(1)
handleDetail = win32gui.GetWindowRect(handle)
class_name = win32gui.GetClassName(handle)
title = win32gui.GetWindowText(handle)
# win32gui.SetForegroundWindow(handle)
win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)

# win32gui.SetForegroundWindow(handle)
# win32gui.SetActiveWindow(handle)

print(handleDetail, class_name, title)

import pyautogui

# import time

x, y = pyautogui.position()
print("当前鼠标的X轴的位置为：{}，Y轴的位置为：{}".format(x, y))
winW, winH = pyautogui.size()
print("当前屏幕的宽为：{}，屏幕的高为：{}".format(winW, winH))
# 移动鼠标到屏幕中心
pyautogui.moveTo(x=winW / 2, y=winH / 2, duration=0.25)
# 单击
# pyautogui.click(x=70, y=160, button='left')

# 双击
# pyautogui.doubleClick(x=652, y=509, button="left")

# 拖拽鼠标
# pyautogui.dragTo(100, 200, duration=0.25)

# 发送组合键
# pyautogui.hotkey('win', 'r')

# 输入内容 message后面跟要输入的内容,interval用于设置输入的速度
# pyautogui.typewrite(message="calc", interval=0.25)

# 截屏，获取颜色
img = pyautogui.screenshot()
color = img.getpixel((61, 164))
print("该坐标的像素点的颜色是：{}".format(color))

# 找图片在屏幕上位置和宽高
imgX, imgY, width, height = pyautogui.locateOnScreen('./blueocean.png')
print("csdn图片的位置x:{}y:{}和宽高w:{}h:{}".format(imgX, imgY, width, height))

# 获取区域中心点
centerX, centerY = pyautogui.center((9, 741, 81, 95))
print("中心点位置是x:{},y:{}".format(centerX, centerY))

pyautogui.alert('This is the message to display.')

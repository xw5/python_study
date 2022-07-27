import shutil

print(shutil)
# 删除目录下所有文件，目录
try:
    shutil.rmtree('./1')
except:
    pass

try:
    shutil.copytree('../pyautogui', 'newFolder')
except:
    pass
shutil.copy('【技术】研发质量能力认证练习.zip', '【技术】研发质量能力认证练习test.zip')

shutil.move('【技术】研发质量能力认证练习test.zip', '【技术】研发质量能力认证练习testtest.zip')
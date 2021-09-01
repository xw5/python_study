import os

print("=" * 30, "os.path.abspath")
print(os.path.abspath("【技术】研发质量能力认证练习.zip"))

print("=" * 30, "os.path.isdir")
print(os.path.isdir("【技术】研发质量能力认证练习.zip"))

print("=" * 30, "os.path.isfile")
print(os.path.isfile("【技术】研发质量能力认证练习.zip"))

print("=" * 30, "os.path.basename")
print(os.path.basename(r"E:\study\python\python_reptile\file_operation\【技术】研发质量能力认证练习.zip"))

print("=" * 30, "os.path.split")
print(os.path.split("E:\\study\\python\\python_reptile\\file_operation\\【技术】研发质量能力认证练习.zip"))

print("=" * 30, "os.path.join")
print(os.path.join("E:\\","study\\python\\python_reptile\\file_operation\\","【技术】研发质量能力认证练习.zip"))

print("=" * 30, "os.path.getsize")
filesize = os.path.getsize("E:\\study\\python\\python_reptile\\file_operation\\【技术】研发质量能力认证练习.zip")
print(filesize/1024)
print(format(filesize/1024, '.2f'))

print("=" * 30, "os.getcwd")
nowPath = os.getcwd()
print(nowPath)

print("=" * 30, "os.listdir")
for f in os.listdir(os.getcwd()):
    print(nowPath + os.sep + f)

print("=" * 30, "os.mkdir")
os.mkdir('111')

print("=" * 30, "os.mkdirs")
os.makedirs('112/123/2')

print("=" * 30, "os.remove")
# 删除文件
try:
    os.remove('aa.py')
except:
    pass

# 删除目录
print("=" * 30, "os.rmdir")
os.rmdir('111')

# 删除目录
print("=" * 30, "os.removemdirs")
os.removedirs('112/123/2')


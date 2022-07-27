import os

targetDir = r'E:\study\python'


# 改变当前工作目录到另外的路径
# os.chdir(targetDir)
# 当前工作目录
# print(os.getcwd())

# 创建目录,exist_ok=True 指定了，如果某个要创建的目录已经存在，也不报错
# os.makedirs('test/aaa',exist_ok=True)
# os.remove('sdf.py')

# print('文件是否存在', os.path.exists(r'E:\study\python\python_reptile\auto_send_msg.py'))
# print('路径中的文件名部分', os.path.basename(r'E:\study\python\python_reptile\auto_send_msg.py'))
# print('路径中的目录部分', os.path.dirname(r'E:\study\python\python_reptile\auto_send_msg.py'))
# print('路径拼接', os.path.join('tmp', 'data', r'study\python\python_reptile\auto_send_msg.py'))
# print('是否是文件', os.path.isfile(r'E:\study\python\python_reptile\auto_send_msg.py'))
# print('文件大小', os.path.getsize(r'E:\study\python\python_reptile\bs4基本操作-tag.py'))
# print('文件修改时间', os.path.getmtime(r'E:\study\python\python_reptile\auto_send_msg.py'))

# print('目录是否存在', os.path.exists(targetDir))
# print('是否是目录', os.path.isdir(targetDir))

# 可以递归的删除某个目录所有的子目录和子文件
def delFDTree(dir):
    import shutil
    shutil.rmtree(dir, ignore_errors=True)

# delFDTree('ddd')

# 拷贝文件,如果拷贝前，f1文件已经存在，则会被拷贝覆盖
def copyFile(f0, f1):
    from shutil import copyfile
    copyfile(f0, f1)

# 拷贝目录 如果 d1目录已经存在，执行到copytree时，就会报错
def copyDir(d0, d1):
    from shutil import copytree
    copytree(d0, d1)

# 递归的遍历目录下面所有的文件
def getAllFile(targetDir):
    files = []
    dirs = []

    # 下面的三个变量 dirpath, dirnames, filenames
    # dirpath 代表当前遍历到的目录名
    # dirnames 是列表对象，存放当前dirpath中的所有子目录名
    # filenames 是列表对象，存放当前dirpath中的所有文件名

    for (dirpath, dirnames, filenames) in os.walk(targetDir):
        files += filenames
        dirs += dirnames

    print(files)
    print(dirs)


# 递归的遍历目录下面所有的文件,并拿到完整路径
def getFullPath(targetDir):
    for (dirpath, dirnames, filenames) in os.walk(targetDir):
        for fn in filenames:
            # 把 dirpath 和 每个文件名拼接起来 就是全路径
            fpath = os.path.join(dirpath, fn)
            print(fpath)


# 得到目录中所有的文件和子目录名
def getAllFileChildrenDir(targetDir):
    files = os.listdir(targetDir)
    print(files)


# 得到目录中指定扩展名的文件和子目录
def getAppointFile():
    import glob
    pythonsFile = glob.glob(r'E:\study\python\**\*.py')
    print(pythonsFile)


# getFullPath(targetDir)
# getAllFile(targetDir)
# getAllFileChildrenDir(targetDir)
# getAppointFile()

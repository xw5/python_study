# -*-coding:utf-8-*-
# 更新远光家园H5资源
import os
import shutil

os.system('chcp 65001')
# 修改当前工作目录
os.chdir(r"D:\work\workspace\financialHome_web")


# git操作
def git_action():
    # 展示分支
    print('H5资源当前分支')
    os.system(r'git symbolic-ref --short -q HEAD')
    # 拉取代码
    git_pull = os.system(r'git pull')
    if git_pull == 0:
        print('最新代码拉取成功！')


# git_action()

# 进行构建命令
result = os.system(r'npm run build:prod-uniapp')
# result = 0

source_dir = r'D:\work\workspace\financialHome_web\dist\static'
source_file = r'D:\work\workspace\financialHome_web\dist\index.html'
target_dir = r'D:\work\workspace\EH.YGhome\uni-app\hybrid\html\static'
target_file = r'D:\work\workspace\EH.YGhome\uni-app\hybrid\html\index.html'


# 删除待更新的旧文件
def del_old_files():
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir, )
    if os.path.exists(target_file):
        os.remove(target_file)


# 拷贝打包的文件到目标目录
def copy_files():
    if os.path.exists(source_file):
        shutil.copyfile(source_file, target_file)
    else:
        print('没有指定文件{}'.format(source_file))
    if os.path.exists(source_dir):
        shutil.copytree(source_dir, target_dir)
    else:
        print('没有指定目录{}'.format(source_dir))


# 展示家园项目分支情况
def git_ygapp():
    os.chdir(r"D:\work\workspace\EH.YGhome")
    print('家园项目当前所处分支：')
    os.system(r'git symbolic-ref --short -q HEAD')


print('开始更新资源{}'.format(result))
if result == 0:
    del_old_files()
    copy_files()
    print("家园H5资源更新成功！")
    git_ygapp()
else:
    print("家园H5资源更新失败！")

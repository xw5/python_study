# -*-coding:utf-8-*-
# 远光家园H5牵分支
import os

os.system('chcp 65001')
# 修改当前工作目录
os.chdir(r"D:\work\workspace\EH.YGhome")

# 进行构建命令
os.system(r'git checkout master')
os.system(r'git pull')
branch_name = input('请输入发版分支名：YGHome/2021-10-30-v4.8.1')
if branch_name:
    os.system(r'git checkout -b %s' % branch_name)
    os.system(r'git push --set-upstream origin %s' % branch_name)
else:
    print('分支名不能为空')


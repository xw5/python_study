import os
import zipfile
z = zipfile.ZipFile('test.zip', 'w')
for x in os.listdir('newFolder'):
    z.write('newFolder' + os.sep + x)
z.close()

with zipfile.ZipFile('with.zip', 'w') as w:
    for y in os.listdir('newFolder'):
        w.write('newFolder' + os.sep + y)

# 解压
f = zipfile.ZipFile('test.zip', 'r')
for file in f.namelist():
    print(file)
    f.extract(file, 'temp/')

with open(file='os_test.py', mode='r', encoding='utf-8') as ostest:
    # print(ostest.readlines())
    print(ostest.readline())

with open(file='test.txt', mode='a', encoding='utf-8') as txttest:
    print(txttest.write('珠海远光软件'))
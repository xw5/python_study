# encoding=utf-8
import os
import csv
import requests
import threading
import datetime

# 去掉https的安全警告
requests.packages.urllib3.disable_warnings()

# 防止内存爆定最多同时开10个线程下载 如果想越快可以调大，但是电脑内存怕扛不住
sem = threading.Semaphore(10)
today = datetime.datetime.today()
format_today = today.strftime('%y-%m-%d-%H-%M-%S')  # 下载的图片会保存当前python同目录并以日期命名的目录下
filename = './0111-topic.csv'  # 指定csv文件名
img_column = 4  # 要下载的图片数据在哪一列
data = []
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'
}

# 读取csv文件内容
with open(filename, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    for row in csv_reader:  # 将csv 文件中的数据保存到data中
        data.append(row[img_column - 1])  # 选择某一列加入到data数组中
    print(data)


# 下载图片方法
def download_img(path_url):
    img_file_name = path_url.split('/')[-1]
    print(img_file_name)
    res = requests.get(path_url, headers=headers, verify=False)
    if not os.path.exists(format_today):
        os.makedirs(format_today)
    with open(format_today + '/' + img_file_name, 'wb') as f:
        f.write(res.content)
    sem.release()


# 遍历数据开始下载
for index, path_url in enumerate(data):
    # 只有以http开头的链接，才下载
    if path_url.find('http') == 0:
        sem.acquire()
        threading.Thread(target=download_img, args=(path_url,)).start()

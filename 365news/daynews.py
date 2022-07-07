import requests
from lxml import etree
import time
import random
import os
import datetime
# from txtToAudioModule import textToAudio

os.chdir(r"E:\study\python\python_reptile\365news")

def getNews():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    res = requests.get(url='https://www.163.com/dy/media/T1603594732083.html', headers=headers)

    selecter = etree.HTML(res.text)
    # print(res.text)
    url = selecter.xpath("//div[@class='tab_content']/ul/li/a/@href")[0]
    dateStr = selecter.xpath("//div[@class='tab_content']/ul/li/div[@class='desc']/div/span/text()")[0]
    dateStr = dateStr.replace("-", "")
    dateStr = dateStr.replace(":", "")
    dateStr = dateStr.split(" ")[0]

    print(url)
    print(dateStr)

    time.sleep(random.random() * 3)
    resDetail = requests.get(url=url, headers=headers)

    selecterDetail = etree.HTML(resDetail.text)

    news = selecterDetail.xpath("//div[@class='post_body']/p[2]/text()")

    print(news)
    newContent = '\n'.join(news[1:])
    with open('./new.txt', 'w', encoding='utf-8') as f0:
        f0.write(newContent)
    with open('./{}.txt'.format(dateStr), 'w', encoding='utf-8') as f1:
        f1.write(newContent)
    # textToAudio(newContent, '每日新闻')

curr_time = datetime.datetime.now()
newsFileName = curr_time.strftime("%Y%m%d")

# 判断今天新闻是否已经爬取过
if os.path.exists(newsFileName):
    pass
else:
    getNews()


import requests
from lxml import etree
import time
import random
import os
import datetime
import re
from fake_useragent import UserAgent
ua = UserAgent()
# from txtToAudioModule import textToAudio

os.chdir(r"E:\study\python\python_reptile\peoplehotnews")

def getNews():

    headers = {
        'User-Agent': ua.random
    }

    res = requests.get(url='http://www.people.com.cn/', headers=headers)

    selecter = etree.HTML(res.text)
    # print(res.text)
    url = selecter.xpath("//div[@class='layout section_main cf']/div[@class='tit1 cf']/h2[2]/a/@href")
    print(url)

    time.sleep(random.random() * 3)
    resDetail = requests.get(url=url[0], headers=headers)
    resDetail.encoding = resDetail.apparent_encoding
    selecterDetail = etree.HTML(resDetail.text)

    # 获取时间
    tempDateStr = selecterDetail.xpath("//td[@class='wt'][2]/text()")
    dateStr = re.sub(r'\D', '', tempDateStr[0])
    print(dateStr)

    # 获取新闻
    newsLi = selecterDetail.xpath("//td[@class='p6']/li")
    news = []
    for index, newsItem in enumerate(newsLi):
        tempText = newsItem.xpath('string(.)')
        news.append(str(index + 1) + '、' + tempText.replace('\n', ''))
    print(news)

    # 新闻定入本地
    newsArr = tempDateStr + news
    newContent = '\n'.join(newsArr)
    with open('./new.txt', 'w', encoding='utf-8') as f0:
        f0.write(newContent)
    with open('./{}.txt'.format(dateStr), 'w', encoding='utf-8') as f1:
        f1.write(newContent)

curr_time = datetime.datetime.now()
newsFileName = curr_time.strftime("%Y%m%d")

# 判断今天新闻是否已经爬取过
if os.path.exists(newsFileName):
    pass
else:
    getNews()


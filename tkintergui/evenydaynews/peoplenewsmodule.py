#coding=utf-8
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
def getNews(url, uiName, callBack=None, next=None):
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    res = requests.get(url=url, headers=headers)
    selecter = etree.HTML(res.text)
    # print(res.text)
    url = selecter.xpath("//div[@class='layout section_main cf']/div[@class='tit1 cf']/h2[2]/a/@href")
    # print(url)
    time.sleep(random.random() * 3)
    resDetail = requests.get(url=url[0], headers=headers)
    resDetail.encoding = resDetail.apparent_encoding
    selecterDetail = etree.HTML(resDetail.text)
    # 获取时间
    tempDateStr = selecterDetail.xpath("//td[@class='wt'][2]/text()")
    # 获取新闻
    newsLi = selecterDetail.xpath("//td[@class='p6']/li")
    news = []
    for index, newsItem in enumerate(newsLi):
        tempText = newsItem.xpath('string(.)')
        news.append(str(index + 1) + '、' + tempText.replace('\n', ''))
    # print(news)
    # 新闻定入本地
    newsArr = tempDateStr + news
    newContent = '\n'.join(newsArr)
    if callBack:
        callBack(newContent)
    if next:
        next(uiName, newContent)
    return newContent
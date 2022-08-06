#coding=utf-8
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def getNews(url, uiName, callBack=None, next=None):
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    res = requests.get(url=url, headers=headers, verify=False)
    selecter = etree.HTML(res.text)
    # print(res.text)
    url = selecter.xpath("//div[@class='tab_content']/ul/li/a/@href")[0]
    time.sleep(random.random() * 3)
    resDetail = requests.get(url=url, headers=headers, verify=False)
    selecterDetail = etree.HTML(resDetail.text)
    news = selecterDetail.xpath("//div[@class='post_body']/p[2]/text()")
    print(news)
    newContent = '\n'.join(news[1:])
    if callBack:
        callBack(newContent)
    if next:
        next(uiName, newContent)
    return newContent

import requests
from lxml import etree
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

res = requests.get(url='https://www.163.com/dy/media/T1603594732083.html', headers=headers)

selecter = etree.HTML(res.text)

url = selecter.xpath("//li[@class='media_article']/a/@href")[0]
dateStr = selecter.xpath("//li[@class='media_article']/div/p[@class='media_article_date']/text()")[0]
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
with open('./new.txt'.format(dateStr), 'w', encoding='utf-8') as f0:
    f0.write('\n'.join(news[1:-1]))
with open('./{}.txt'.format(dateStr), 'w', encoding='utf-8') as f1:
    f1.write('\n'.join(news[1:-1]))

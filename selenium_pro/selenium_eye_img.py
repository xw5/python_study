# coding = utf-8
from selenium import webdriver
import requests
import time

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

browser.get("https://image.baidu.com/search/index?ct=&z=0&tn=baiduimage&ipn=r&word=%E5%A3%81%E7%BA%B8%20%E6%8A%A4%E7%9C%BC&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=&lm=-1&st=-1&fr=&fmq=1630398791088_R&ic=4&se=&sme=&width=1920&height=1080&face=0&hd=0&latest=0&copyright=0")

browser.implicitly_wait(10)

imgList = browser.find_elements_by_css_selector('li.imgitem div.imgbox a')
imgUrl = []
print(len(imgList))
for item in imgList:
    imgUrl.append(item.get_attribute('href'))

for item in imgUrl:
    browser.get(item)
    time.sleep(5)
    imgName = browser.find_element_by_css_selector('div.pic-title span').get_attribute('title')
    print(imgName)
    print('=' * 30)
    if "日历" in imgName or not imgName:
        continue
    uploadImg = browser.find_element_by_class_name('btn-download').get_attribute('href')
    ext = uploadImg.split('.')[-1]
    print(imgName, ext)
    imgResultUrl = 'https://image.baidu.com'+uploadImg
    response = requests.get(imgResultUrl, allow_redirects = False, headers=headers)
    with open('./img/{}.{}'.format(imgName, ext), 'wb') as f:
        f.write(response.content)
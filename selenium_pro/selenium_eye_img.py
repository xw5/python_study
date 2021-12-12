# coding = utf-8
from selenium import webdriver
import requests
import time
import os
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrone.exe"
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=options)
if not os.path.exists('./img'):
    os.mkdir('./img')
browser.get("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&hs=0&xthttps=111110&sf=1&fmq=1631116298726_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A3%81%E7%BA%B8+%E6%8A%A4%E7%9C%BC")

browser.implicitly_wait(10)

temp_height = 0
while True:
    browser.execute_script("window.scrollBy(0, 10000)")
    time.sleep(5)
    check_height = browser.execute_script("return document.documentElement.scrollTop")
    if check_height == temp_height:
        break
    temp_height = check_height
    print(check_height)

imgList = browser.find_elements_by_css_selector('li.imgitem div.imgbox a')
imgUrl = []
print(len(imgList))
for item in imgList:
    imgUrl.append(item.get_attribute('href'))

for item in imgUrl:
    browser.get(item)
    time.sleep(3)
    try:
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
    except:
        continue
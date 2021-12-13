# coding = utf-8
from selenium import webdriver
import requests
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrone.exe"
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                           options=options)
if not os.path.exists('./img0'):
    os.mkdir('./img0')
browser.get(
    "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E5%A3%81%E7%BA%B8%20%E6%8A%A4%E7%9C%BC&step_word=&hs=0&pn=0&spn=0&di=220&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=&lm=-1&st=-1&cs=2738203891%2C3253001257&os=587913007%2C858062903&simid=2738203891%2C3253001257&adpicid=0&lpn=0&ln=3434&fr=&fmq=1639404851156_R&fm=index&ic=0&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=1360&height=768&face=undefined&ist=&jit=&cg=wallpaper&bdtype=0&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fimage.lnstzy.cn%2Faoaodcom%2F2018-08%2F05%2F20180805072728293.jpg.w1360.h768.jpg%3Fdown%26refer%3Dhttp%3A%2F%2Fimage.lnstzy.cn%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1641996890%26t%3D5afc00234b96659efd07718fcde078f5&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bw5w51_z%26e3Bv54AzdH3FI42-d9AzdH3Fda8l0-d009l_z%26e3Bfip4s&gsm=1&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined")

browser.implicitly_wait(10)
count = 0
preUrl = ''
while True:
    try:
        uploadImg = browser.find_element_by_class_name('btn-download').get_attribute('href')
        imgResultUrl = 'https://image.baidu.com' + uploadImg
        response = requests.get(imgResultUrl, allow_redirects=False, headers=headers)
        with open('./img0/{}.{}'.format(count, 'jpg'), 'wb') as f:
            f.write(response.content)
        count += 1
        imtNext = browser.find_element_by_css_selector('.img-next')
        imtNext.click()
        time.sleep(3)
        if preUrl == browser.current_url:
            break
        preUrl = browser.current_url
    except Exception:
        print(Exception)
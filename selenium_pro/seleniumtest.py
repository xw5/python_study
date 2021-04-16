# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
browser = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

browser.get("https://www.baidu.com")

time.sleep(2)

browser.find_element_by_id('kw').send_keys("uniapp")
browser.find_element_by_id("su").click()
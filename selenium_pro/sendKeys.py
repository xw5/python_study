# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 需要引入keys包
import time

driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
driver.get("http://10.51.104.185:8080/login?from=%2F")

time.sleep(3)
driver.maximize_window()
# 浏览器全屏显示
userName = driver.find_element_by_id("j_username")
userName.clear()
userName.send_keys("admin")
# tab的定位相相于清除了密码框的默认提示信息，等同上面的clear()
time.sleep(1)
userName.send_keys(Keys.TAB)
password = driver.find_element_by_name("j_password")
password.send_keys("1234.abcd")
# 通过定位密码框，enter（回车）来代替登陆按钮
password.send_keys(Keys.ENTER)
'''
#也可定位登陆按钮，通过enter（回车）代替click()
driver.find_element_by_id("login").send_keys(Keys.ENTER)
'''
